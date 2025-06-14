---
url: "https://supabase.com/blog/vecs"
title: "Supabase Vecs: a vector client for Postgres"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Vecs: a vector client for Postgres

29 May 2023

•

6 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![Supabase Vecs: a vector client for Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-06-01-vecs%2Fog-image.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Vecs](https://github.com/supabase/vecs) is a new Python library for managing embeddings in your Postgres database with the pgvector extension.

It handles:

- Creating and indexing tables
- Querying vectors by cosine distance, l2 distance, and max inner dot product
- Filtering based on user-defined metadata

## Goals [\#](https://supabase.com/blog/vecs\#goals)

Our goal for `vecs` is to provide an interface that lets Postgres + pgvector look and feel like a dedicated vector store. It works with any Postgres database (or platform) that [supports pgvector](https://github.com/pgvector/pgvector/issues/54).
It was designed with ease-of-use, interactivity, and exploratory data analysis in mind, but works equally well as a search workhorse.

If you're interested in the nuts and bolts of what's going on, it's trivial to drop into the SQL layer and see what's happening.
Alternatively, folks who don't want to know what's happening in the database, don't need to care.

## Usage [\#](https://supabase.com/blog/vecs\#usage)

`Vecs` makes it easy to create a collection (table) and insert a few records - just 5 lines of code.

### Connecting [\#](https://supabase.com/blog/vecs\#connecting)

`
import vecs
DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"
# create vector store client
vx = vecs.create_client(DB_CONNECTION)
# create a collection of vectors with 3 dimensions
docs = vx.get_or_create_collection(name="docs", dimension=3)
`

The `get_or_create_collection` call sets up a table in the Postgres database specified by `DB_CONNECTION` in a schema named `vecs` with the user defined name `docs`.

Or, more specifically:

`
create table vecs.docs (
    id text primary key,
    vec vector(3) not null,
    metadata jsonb not null default '{}'::jsonb
);
`

### Insert/Update [\#](https://supabase.com/blog/vecs\#insertupdate)

We can insert a few records in that new SQL table/vecs collection using `Collection.upsert`.

`
# add records to the collection
docs.upsert(
    vectors=[\
        (\
          "vec0",           # the records user defined identifier\
          [0.1, 0.2, 0.3],  # the vector. A list or np.array\
          {"year": 1973}    # associated metadata\
        )\
    ]
)
`

which will add the records to our table if the `id` `"vec0"` does not exist, or updates the existing record if it does exist.

### Query [\#](https://supabase.com/blog/vecs\#query)

You can query a vecs collection at any time without an index, but it's a best practices to create an index on your collection after inserting
data.

`
docs.index()
`

Where `index` optionally takes an argument for the distance measure to index.

Finally, we can search the collection for similar vectors using the `query` method:

`
docs.query(
    query_vector=[0.10,0.21,0.29],   # required
    limit=1,                         # (optional) number of records to return
    filters={"year": {"$eq": 1973}}, # (optional) metadata filters
    measure="cosine_distance",       # (optional) distance measure to use
    include_value=False,             # (optional) should distance measure values be returned?
    include_metadata=False,          # (optional) should record metadata be returned?
)
`

Which returns:

`
[("vec1", 0.000697, {"year": 1973})]
`

Since all metadata is stored in a `jsonb` column, there's a [lightweight but flexible DSL](https://supabase.github.io/vecs/concepts_metadata/) wrapped around it for filtering.

When you're done, disconnect with:

`
vx.disconnect()
`

And 90% of the time, that minimal interface is all you'll need to touch.

For more in-depth information about `vecs`, checkout the [API Quickstart](https://supabase.github.io/vecs/api/),
[celebrity look-alike demo](https://github.com/supabase/supabase/blob/be1f4ea85e10cc8134e389dcdbe6a092b08612f1/examples/ai/face_similarity.ipynb),
or [OpenAI integration example](https://supabase.github.io/vecs/integrations_openai/)

## Deploying with Supabase [\#](https://supabase.com/blog/vecs\#deploying-with-supabase)

As usual, if you combine [supabase/vecs](https://github.com/supabase/vecs) with the rest of Supabase, you get more than the sum of the parts.
Once you're happy with your vecs collection, you can make it accessible to your front-end through a supabase client library by exposing the collection as a view
in your public schema.

![Expose with view](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-06-01-vecs%2Fsingle-database.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

For example, you could create a view

`
create view public.docs as
    select
        id,
        embedding,
        metadata, # Expose the metadata as JSON
        (metadata->>'url')::text as url # Extract the URL as a string
    from
        vecs.docs
`

And then access it with the supabase-js client library within your applications:

`
const { data, error } = await supabase
.from('docs')
.select('id, embedding, metadata')
.eq('url', '/hello-world')
`

For more deployment options, including enterprise scalable architecture, check out the [engineering for scale guide](https://supabase.com/docs/guides/ai/engineering-for-scale#simple-workloads).

## Future ideas [\#](https://supabase.com/blog/vecs\#future-ideas)

Currently, `vecs` is unopinionated about where vectors come from or how they're produced. While there will always be a need for generic vector
storage and querying, it's becoming clear that text and image vectorization make up +95% of usage. That gives us the opportunity to
streamline those workflows for users.

One option we're exploring is to optionally assign transformation pipelines to collections along the lines of:

`
# This is mock code only, not currently functional
docs: Collection =vx.get_or_create_collection(
    docs='docs',
    dimension=512,
    transform = TextPreprocessor(  # this is new
        model="sentence-transformers/all-Mini-L6-v2"
    )
)
docs.upsert([\
    ("id_0", "# Some markdown", {}),\
    ("id_1", "# Some more markdown", {})\
])
`

so users can choose to work with their preferred media type without ever thinking about vectors.

Another direction we're considering is adding an async client to avoid blocking when waiting on the database or network i.e.

`
# This is mock code only, not currently functional
await docs.upsert([\
    ("id_0", [0.1, 0.2, 0.3], {}),\
])
`

Both possibilities are still up for debate. If you have view on either, feel free to weigh in on the
[Feature Request: Preprocessing Transform](https://github.com/supabase/vecs/issues/5)
and [Feature Request: Async Client](https://github.com/supabase/vecs/issues/6) GitHub issues.

## More info [\#](https://supabase.com/blog/vecs\#more-info)

- Source code: [github.com/supabase/vecs](https://github.com/supabase/vecs)
- Vecs Docs: [supabase.github.io/vecs/](https://supabase.github.io/vecs/)
- Supabase Vector Toolkit: [supabase.com/docs/guides/ai](https://supabase.com/docs/guides/ai)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&t=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)

[Last post\\
\\
**Flutter Hackathon Winners** \\
\\
29 May 2023](https://supabase.com/blog/flutter-hackathon-winners)

[Next post\\
\\
**ChatGPT plugins now support Postgres & Supabase** \\
\\
25 May 2023](https://supabase.com/blog/chatgpt-plugins-support-postgres)

[postgres](https://supabase.com/blog/tags/postgres) [AI](https://supabase.com/blog/tags/AI) [python](https://supabase.com/blog/tags/python)

On this page

- [Goals](https://supabase.com/blog/vecs#goals)
- [Usage](https://supabase.com/blog/vecs#usage)
  - [Connecting](https://supabase.com/blog/vecs#connecting)
  - [Insert/Update](https://supabase.com/blog/vecs#insertupdate)
  - [Query](https://supabase.com/blog/vecs#query)
- [Deploying with Supabase](https://supabase.com/blog/vecs#deploying-with-supabase)
- [Future ideas](https://supabase.com/blog/vecs#future-ideas)
- [More info](https://supabase.com/blog/vecs#more-info)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&t=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)