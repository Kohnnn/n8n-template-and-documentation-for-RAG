---
url: "https://supabase.com/blog/chatgpt-plugins-support-postgres"
title: "ChatGPT plugins now support Postgres & Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# ChatGPT plugins now support Postgres & Supabase

25 May 2023

•

10 minute read

[![Egor Romanov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fegor-romanov.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Egor RomanovEngineering](https://github.com/egor-romanov)

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![ChatGPT plugins now support Postgres & Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-plugins-support-postgres.jpeg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

One of the challenges that ChatGPT faces is being able to answer questions from a private dataset. We can solve this with “retrieval plugins”, which allow ChatGPT to access information from a database.

Supabase recently contributed to the OpenAI repo with a [Postgres](https://github.com/openai/chatgpt-retrieval-plugin#postgres) and a [Supabase](https://github.com/openai/chatgpt-retrieval-plugin#supabase) implementation to help developers build plugins using pgvector.

Let’s dig into the specifics of Retrieval plugins, then we can implement an example - we’ll ingest all of the Postgres docs into a Supabase database, then get ChatGPT to answer questions. It’s a contrived example since ChatGPT already knows about Postgres, but what other data source would Supabase want to use?

## What is ChatGPT Retrieval Plugin? [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#what-is-chatgpt-retrieval-plugin)

ChatGPT recently released [Plugins](https://openai.com/blog/chatgpt-plugins) which help ChatGPT access up-to-date information, run computations, or use third-party services.

A [Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin) is a Python project designed to inject external data into the ChatGPT. It allows ChatGPT to dynamically pull relevant information into conversations from your data sources. This could be PDF documents, Confluence, or Notion knowledge bases.

A retrieval plugin does a few things:

1. Turn documents into smaller chunks.
2. Converts chunks into embeddings using OpenAI's `text-embedding-ada-002` model.
3. Stores the embeddings into a vector database.
4. Queries the vector database for relevant documents when a question is asked.

You can choose your preferred vector database provider from a list of [supported options](https://github.com/openai/chatgpt-retrieval-plugin#choosing-a-vector-database).

## Adding Supabase and Postgres as Datastore options for ChatGPT Retrieval Plugin [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#adding-supabase-and-postgres-as-datastore-options-for-chatgpt-retrieval-plugin)

We've implemented two vector provider options: one for Postgres and one for Supabase. The main differences are:

- The Postgres version uses the `psycopg2` python library to directly connect to the database.
- The Supabase version interacts with the database via PostgREST. This is helpful if you want to use [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security) or if you are planning to use the data in the Retrieval store beyond ChatGPT.

The Postgres implementation is great to start with because there are now a [large number of providers](https://github.com/pgvector/pgvector/issues/54) supporting pgvector.

Both have the same schema so you can easily switch between them:

`
create table if not exists documents (
    id text primary key default gen_random_uuid()::text,
    source text,
    source_id text,
    content text,
    document_id text,
    author text,
    url text,
    created_at timestamptz default now(),
    embedding vector(1536)
);
`

When you create the retrieval store inside your database, a stored function is implemented to query and find relevant information for your question to ChatGPT:

`
create or replace function match_page_sections(
	in_embedding vector(1536),
	in_match_count int default 3,
	in_document_id text default '%%',
	in_source_id text default '%%',
	in_source text default '%%',
	in_author text default '%%',
	in_start_date timestamptz default '-infinity',
	in_end_date timestamptz default 'infinity'
)
returns table (
	id text,
	source text,
	source_id text,
	document_id text,
	url text,
	created_at timestamptz,
	author text,
	content text,
	embedding vector(1536),
	similarity float
)
language plpgsql
as $$
#variable_conflict use_variable
begin
return query
select
	documents.id,
	documents.source,
	documents.source_id,
	documents.document_id,
	documents.url,
	documents.created_at,
	documents.author,
	documents.content,
	documents.embedding,
	(documents.embedding <#> in_embedding) * -1 as similarity
from
	documents
where
	in_start_date <= documents.created_at and
documents.created_at <= in_end_date and
(documents.source_id like in_source_id or documents.source_id is null) and
(documents.source like in_source or documents.source is null) and
(documents.author like in_author or documents.author is null) and
(documents.document_id like in_document_id or documents.document_id is null)
order by
	documents.embedding <#> in_embedding
limit
	in_match_count;
end;
$$;
`

We apply filters based on the source, author, document, and date, and find the closest embeddings using the inner product distance function. This function offers the best performance when the embeddings are normalized, which is the case for OpenAI embeddings. The similarity is calculated as: `(documents.embedding <#> in_embedding) * -1 as similarity`. And that’s it, you can now seamlessly use the Retrieval Plugin with a Postgres Database underneath, eliminating the need for any manual implementation on your end.

## Example: Chat with Postgres Docs [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#example-chat-with-postgres-docs)

Let’s build an example where we can “ask ChatGPT questions” about the Postgres documentation.

This will require several steps:

1. Download all the [Postgres docs as a PDF](https://www.postgresql.org/files/documentation/pdf/15/postgresql-15-US.pdf)
2. Convert the docs into chunks of embedded text and store them in Supabase
3. Run our plugin locally so that we can ask questions about the Postgres docs.

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-plugin-scheme--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Step 1: Fork the ChatGPT Retrieval Plugin repository [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#step-1-fork-the-chatgpt-retrieval-plugin-repository)

Fork the ChatGPT Retrieval Plugin repository to your GitHub account and clone it to your local machine. Read through the `README.md` file to understand the project structure.

### Step 2: Install dependencies [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#step-2-install-dependencies)

Choose your desired datastore provider and remove unused dependencies from `pyproject.toml`. For this example, we'll use Supabase. And install dependencies with Poetry:

`
poetry install
`

### Step 3: Create a Supabase project [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#step-3-create-a-supabase-project)

Create a [Supabase project](https://supabase.com/dashboard) and database by following the instructions [here](https://supabase.com/docs/guides/platform). Export the environment variables required for the retrieval plugin to work:

`
export OPENAI_API_KEY=<open_ai_api_key>
export DATASTORE=supabase
export SUPABASE_URL=<supabase_url>
export SUPABASE_SERVICE_ROLE_KEY=<supabase_key>
`

For Postgres datastore, you'll need to export these environment variables instead:

`
export OPENAI_API_KEY=<open_ai_api_key>
export DATASTORE=postgres
export PG_HOST=<postgres_host_url>
export PG_PASSWORD=<postgres_password>
`

### Step 4: Run Postgres Locally [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#step-4-run-postgres-locally)

To start quicker you may use Supabase CLI to spin everything up locally as it already includes pgvector from the start. Install `supabase-cli`, go to the `examples/providers` folder in the repo and run:

`
supabase start
`

This will pull all docker images and run supabase stack in docker on your local machine. It will also apply all the necessary migrations to set the whole thing up. You can then use your local setup the same way, just export the environment variables and follow to the next steps.

Using `supabase-cli` is not required and you can use any other docker image or hosted version of PostgresDB that includes `pgvector`. Just make sure you run migrations from `examples/providers/supabase/migrations/20230414142107_init_pg_vector.sql`.

### Step 5: Obtain OpenAI API key [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#step-5-obtain-openai-api-key)

To create embeddings Plugin uses OpenAI API and `text-embedding-ada-002` model. Each time we add some data to our datastore, or try to query relevant information from it, embedding will be created either for inserted data chunk, or for the query itself. To make it work we need to export `OPENAI_API_KEY`. If you already have an account in OpenAI, you just need to go to [User Settings - API keys](https://platform.openai.com/account/api-keys) and Create new secret key.

![OpenAI Secret Keys](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fopenai-secret-keys.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Step 6: Run the plugin! [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#step-6-run-the-plugin)

Execute the following command to run the plugin:

`
poetry run dev
# output
INFO:     Will watch for changes in these directories: ['./chatgpt-retrieval-plugin']
INFO:     Uvicorn running on http://localhost:3333 (Press CTRL+C to quit)
INFO:     Started reloader process [87843] using WatchFiles
INFO:     Started server process [87849]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
`

The plugin will start on your localhost - port :3333 by default.

### Step 6: Populating data in the datastore [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#step-6-populating-data-in-the-datastore)

For this example, we'll upload Postgres documentation to the datastore. Download the [Postgres documentation](https://www.postgresql.org/files/documentation/pdf/15/postgresql-15-US.pdf) and use the `/upsert-file` endpoint to upload it:

`
curl -X POST -F \\"file=@./postgresql-15-US.pdf\\" <http://localhost:3333/upsert-file>
`

The plugin will split your data and documents into smaller chunks automatically. You can view the chunks using the Supabase dashboard or any other SQL client you prefer. For the whole Postgres Documentation I got 7,904 records in my documents table, which is not a lot, but we can try to add index for `embedding` column to speed things up by a little. To do so, you should run the following SQL command:

`
create index on documents
using ivfflat (embedding vector_ip_ops)
with (lists = 10);
`

This will create an index for the inner product distance function. Important to note that it is an approximate index. It will change the logic from performing the exact nearest neighbor search to the approximate nearest neighbor search.

We are using `lists = 10`, because as a general guideline, you should start looking for optimal lists constant value with the formula: `rows / 1000` when you have less than 1 million records in your table.

Now, it is time to add our plugin to ChatGPT.

### Empowering ChatGPT with Postgres knowledge [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#empowering-chatgpt-with-postgres-knowledge)

To integrate our plugin with ChatGPT, register it in the ChatGPT dashboard. Assuming you have access to ChatGPT Plugins and plugin development, select the Plugins model in a new chat, then choose "Plugin store" and "Develop your own plugin." Enter `localhost:3333` into the domain input, and your plugin is now part of ChatGPT.

![ChatGPT Change Model](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-change-model.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![ChatGPT Plugin Store](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-plugin-store.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![ChatGPT Local Plugin](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-local-plugin.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can now ask questions about Postgres and receive answers derived from the documentation!

Let's try it out: ask ChatGPT to find out when to use `check` and when to use `using`. You will be able to see what queries were sent to our plugin and what it responded to.

![Ask ChatGPT](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fask-chatgpt.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![ChatGPT Query](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-query.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

And after ChatGPT receives a response from the plugin it will answer your question with the data from the documentation.

![ChatGPT Reply](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-reply.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Wrap up [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#wrap-up)

It's easy to bring any context into the datastore and utilize it with ChatGPT. Simply export your knowledge base from platforms like Notion or Confluence, upload it to the datastore, and you're good to go. You can also use any other datastore provider you prefer.

And the good news is that you’re not limited by using it with ChatGPT, you can embed it in your website or documentation, and build a Slack bot or telegram bot to answer questions about your company or product. For that, you will only need to add a single call to OpenAI API to create a summary of data retrieved from the Plugin. You can find some inspiration on how to do that in our blog post about building [Supabase Clippy assistant](https://supabase.com/blog/chatgpt-supabase-docs).

Let us know on [Twitter](https://twitter.com/Supabase) if you are building ChatGPT Plugins. We can’t wait to see what you will build!

## More AI resources [\#](https://supabase.com/blog/chatgpt-plugins-support-postgres\#more-ai-resources)

- [OpenAI ChatGPT Plugin docs](https://platform.openai.com/docs/plugins/introduction)
- [ChatGPT Retrieval Plugin Repo](https://github.com/openai/chatgpt-retrieval-plugin)
- [How to build ChatGPT Plugin from scratch with Supabase Edge Runtime](https://supabase.com/blog/building-chatgpt-plugins-template).
- [Docs pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-plugins-support-postgres&text=ChatGPT%20plugins%20now%20support%20Postgres%20%26%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-plugins-support-postgres&text=ChatGPT%20plugins%20now%20support%20Postgres%20%26%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-plugins-support-postgres&t=ChatGPT%20plugins%20now%20support%20Postgres%20%26%20Supabase)

[Last post\\
\\
**Supabase Vecs: a vector client for Postgres** \\
\\
29 May 2023](https://supabase.com/blog/vecs)

[Next post\\
\\
**Building ChatGPT Plugins with Supabase Edge Runtime** \\
\\
15 May 2023](https://supabase.com/blog/building-chatgpt-plugins-template)

[AI](https://supabase.com/blog/tags/AI) [tutorial](https://supabase.com/blog/tags/tutorial) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [What is ChatGPT Retrieval Plugin?](https://supabase.com/blog/chatgpt-plugins-support-postgres#what-is-chatgpt-retrieval-plugin)
- [Adding Supabase and Postgres as Datastore options for ChatGPT Retrieval Plugin](https://supabase.com/blog/chatgpt-plugins-support-postgres#adding-supabase-and-postgres-as-datastore-options-for-chatgpt-retrieval-plugin)
- [Example: Chat with Postgres Docs](https://supabase.com/blog/chatgpt-plugins-support-postgres#example-chat-with-postgres-docs)
- [Wrap up](https://supabase.com/blog/chatgpt-plugins-support-postgres#wrap-up)
- [More AI resources](https://supabase.com/blog/chatgpt-plugins-support-postgres#more-ai-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-plugins-support-postgres&text=ChatGPT%20plugins%20now%20support%20Postgres%20%26%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-plugins-support-postgres&text=ChatGPT%20plugins%20now%20support%20Postgres%20%26%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-plugins-support-postgres&t=ChatGPT%20plugins%20now%20support%20Postgres%20%26%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-25-chatgpt-plugins-support-postgres%2Fchatgpt-plugin-scheme--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)