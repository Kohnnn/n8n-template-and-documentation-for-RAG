---
url: "https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation"
title: "pg_jsonschema: JSON Schema support for Postgres"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# pg\_jsonschema: JSON Schema support for Postgres

19 Aug 2022

•

6 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![pg_jsonschema: JSON Schema support for Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-pg_jsonschema%2Fjsonschema-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Released on the Supabase platform today, [pg\_jsonschema](https://github.com/supabase/pg_jsonschema) is a Postgres extension
which adds [JSON Schema](https://json-schema.org/) validation support for `json` and `jsonb` data types.

## The use-case for JSON validation [\#](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation\#the-use-case-for-json-validation)

Despite Supabase being an SQL shop, even our most zealous relational data model advocates (begrudgingly) recognize some advantages to the document data model.
Mainly, if some complex data will always be consumed together, a document data type can be a good fit.

**For Example**:

If our application receives data via a webhook:

`
{
"status_code": 200,
"checksum": "89b623f6332d2b9b42b4e17eaf1bcc60"
"headers": {
    "Content-Type": "application/json",
    "Last-Modified": "Tue, 09 Aug 2022 09:14:10 GMT"
},
"payload": {
    {
      "success": true,
      "content": {
        "account_id": "d928b484-16bd-4f10-a827-3eb959b4cc14",
        "event": "SUBSCRIBED",
        "subscriptions": [\
          {"subscription_id": 481, "exp": 1660050940},\
          {"subscription_id": 121, "exp": 1660041852},\
        ]
      }
    }
}
}
`

A reasonable swing at normalizing that data into tables might look like this:

![pg_jsonschema_erd.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-pg_jsonschema%2Fpg_jsonschema_erd.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

That's a lot of architecting! Moreover, the query to recover the original input requires 5 joins!

A solution that aligns better with our intent would be to persist whatever we receive from the external service so long as it meets a minimum set of requirements.
With Postgres' `json` data type we can achieve half of that goal.

![pg_jsonschema_erd2.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-pg_jsonschema%2Fpg_jsonschema_erd2.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Treating the webhook contents as a `json` document simplifies our data model. It is also robust to changing payloads and more efficient to query, update, and delete.

Now what about this part?

> so long as it meets a minimum set of requirements

## Challenges [\#](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation\#challenges)

The flexibility of document types also comes with some downsides.

The schema of the json payload from the previous example is a little intense for a blog post, so let's instead say we intend for a table's `json` column to hold objects with a `string` attribute named `foo` and no additional attributes.

Without constraints, the setup would be:

`
create table some_table (
id serial primary key,
metadata json not null
);
insert into some_table (metadata)
values (<SQL Input>);
`

But the resulting schema is much more permissive than our intent. When inserting a mix of correct and incorrect values:

![Check constraints](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-pg_jsonschema%2Ftable-1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Only 2 of our 8 test cases were handled appropriately by our data model.

A core strength of SQL databases is their ability to constrain data's [types](https://www.postgresql.org/docs/current/datatype.html), nullability,
[referential integrity](https://www.postgresql.org/docs/current/tutorial-fk.html), [uniqueness](https://www.postgresql.org/docs/current/ddl-constraints.html),
and even [arbitrary developer-defined rules](https://www.postgresql.org/docs/current/sql-createtrigger.html).
Those constraints are a lot to sacrifice to gain the convenience of document types.

Fortunately, the challenge of validating `json` documents isn't specific to SQL databases. NoSQL/Document databases, like MongoDB,
[optionally enforce data constraints](https://www.mongodb.com/docs/atlas/app-services/schemas/) so there's plenty of prior art for us to draw from.

## JSON Schema [\#](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation\#json-schema)

[JSON Schema](https://json-schema.org/) is a specification for validating the shape and contents of `json` documents.
It can describe constraints for documents similar to those applied by relational databases.

Translating our constraints from the previous example into a JSON Schema we get:

`
// objects with a string attribute
// named foo and no additional attributes
{
"type": "object",
"properties": {
    "foo": {
      "type": "string"
    }
},
"required": ["foo"],
"additionalProperties": false
}
`

Which is a formal and human-readable description of our intent. A tutorial on the JSON Schema language is out-of-scope
for this article but you can find a full introduction in [their guide](https://json-schema.org/understanding-json-schema/index.html).

So now we have:

✅ flexible document data type → `json`

✅ a language to describe constraints on `json` documents → JSON Schema

❌ a way to enforce JSON Schema constraints on `json` documents in Postgres

## pg\_jsonschema [\#](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation\#pg_jsonschema)

[pg\_jsonschema](https://github.com/supabase/pg_jsonschema) is a Postgres extension that can validate `json` and `jsonb` data types
against a [JSON Schema](https://json-schema.org/). The extension offers two functions:

`
-- Validates a json *instance* against a JSON Schema *schema*
json_matches_schema(schema json, instance json) returns bool
-- Validates a jsonb *instance* against a JSON Schema *schema*
jsonb_matches_schema(schema json, instance jsonb) returns bool
`

We can use those functions in combination with a [check constraint](https://www.postgresql.org/docs/current/ddl-constraints.html) to more completely describe our data model.

`
create table some_table(
id serial primary key,
metadata json not null,
check (
    json_matches_schema(
      schema :='{
         "type": "object",
         "properties": {
          "foo": {
           "type": "string"
          }
         },
         "required": ["foo"],
         "additionalProperties": false
      }',
      instance := metadata
    )
)
);
insert into some_table(metadata)
values
(<SQL input>);
`

With that check constraint in place, we re-run the same test cases:

![Check constraints 2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-pg_jsonschema%2Ftable-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now all 8 tests are handled correctly. In cases where records failed to insert, Postgres throws an error referencing the failing constraint.

> ERROR: new row for relation "some\_table" violates check constraint "some\_table\_metadata\_check"
>
> DETAIL: Failing row contains (1, null).
>
> SQL state: 23514

With these tools you can wield the flexibility of `json`/ `jsonb` data types without sacrificing the guarantees of a well specified data model!

To get started with `pg_jsonschema`, fire up a new supabase project and enable the extension with

`
create extension pg_jsonschema;
`

or follow the [Docker Compose instructions](https://github.com/supabase/pg_jsonschema#try-it-out) in the [repo's README](https://github.com/supabase/pg_jsonschema/blob/master/README.md).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-jsonschema-a-postgres-extension-for-json-validation&text=pg_jsonschema%3A%20JSON%20Schema%20support%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-jsonschema-a-postgres-extension-for-json-validation&text=pg_jsonschema%3A%20JSON%20Schema%20support%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-jsonschema-a-postgres-extension-for-json-validation&t=pg_jsonschema%3A%20JSON%20Schema%20support%20for%20Postgres)

[Last post\\
\\
**One more thing** \\
\\
19 August 2022](https://supabase.com/blog/launch-week-5-one-more-thing)

[Next post\\
\\
**PostgREST v10: EXPLAIN and Improved Relationship Detection** \\
\\
19 August 2022](https://supabase.com/blog/postgrest-v10)

[launch-week](https://supabase.com/blog/tags/launch-week) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [The use-case for JSON validation](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation#the-use-case-for-json-validation)
- [Challenges](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation#challenges)
- [JSON Schema](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation#json-schema)
- [pg\_jsonschema](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation#pg_jsonschema)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-jsonschema-a-postgres-extension-for-json-validation&text=pg_jsonschema%3A%20JSON%20Schema%20support%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-jsonschema-a-postgres-extension-for-json-validation&text=pg_jsonschema%3A%20JSON%20Schema%20support%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-jsonschema-a-postgres-extension-for-json-validation&t=pg_jsonschema%3A%20JSON%20Schema%20support%20for%20Postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)