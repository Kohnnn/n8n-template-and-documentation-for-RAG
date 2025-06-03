---
url: "https://supabase.com/blog/openai-embeddings-postgres-vector"
title: "Storing OpenAI embeddings in Postgres with pgvector"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Storing OpenAI embeddings in Postgres with pgvector

06 Feb 2023

•

15 minute read

[![Greg Richardson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgregnr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Greg RichardsonEngineering](https://github.com/gregnr)

![Storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fembeddings%2Fog_pgvector.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

A new PostgreSQL extension is now available in Supabase: [`pgvector`](https://github.com/pgvector/pgvector), an open-source vector similarity search.

The exponential progress of AI functionality over the past year has inspired many new real world applications. One specific challenge has been the ability to store and query _embeddings_ at scale.
In this post we'll explain what embeddings are, why we might want to use them, and how we can store and query them in PostgreSQL using `pgvector`.

🆕 Supabase has now released an open source toolkit for developing AI applications using Postgres and pgvector. Learn more in the [AI & Vectors docs](https://supabase.com/docs/guides/ai).

## What are embeddings? [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#what-are-embeddings)

Embeddings capture the “relatedness” of text, images, video, or other types of information. This relatedness is most commonly used for:

- **Search:** how similar is a search term to a body of text?
- **Recommendations:** how similar are two products?
- **Classifications:** how do we categorize a body of text?
- **Clustering:** how do we identify trends?

Let's explore an example of text embeddings. Say we have three phrases:

1. “The cat chases the mouse”
2. “The kitten hunts rodents”
3. “I like ham sandwiches”

Your job is to group phrases with similar meaning. If you are a human, this should be obvious. Phrases 1 and 2 are almost identical, while phrase 3 has a completely different meaning.

Although phrases 1 and 2 are similar, they share no common vocabulary (besides “the”). Yet their meanings are nearly identical. How can we teach a computer that these are the same?

## Human language [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#human-language)

Humans use words and symbols to communicate language. But words in isolation are mostly meaningless - we need to draw from shared knowledge & experience in order to make sense of them. The phrase “You should Google it” only makes sense if you know that Google is a search engine and that people have been using it as a verb.

In the same way, we need to train a neural network model to understand human language. An effective model should be trained on millions of different examples to understand what each word, phrase, sentence, or paragraph could mean in different contexts.

So how does this relate to embeddings?

## How do embeddings work? [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#how-do-embeddings-work)

Embeddings compress discrete information (words & symbols) into distributed continuous-valued data (vectors). If we took our phrases from before and plot them on a chart, it might look something like this:

![Vector similarity](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fembeddings%2Fvector-similarity.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Phrases 1 and 2 would be plotted close to each other, since their meanings are similar. We would expect phrase 3 to live somewhere far away since it isn't related. If we had a fourth phrase, “Sally ate Swiss cheese”, this might exist somewhere between phrase 3 (cheese can go on sandwiches) and phrase 1 (mice like Swiss cheese).

In this example we only have 2 dimensions: the X and Y axis. In reality, we would need many more dimensions to effectively capture the complexities of human language.

## OpenAI embeddings [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#openai-embeddings)

OpenAI offers an [API](https://platform.openai.com/docs/guides/embeddings) to generate embeddings for a string of text using its language model. You feed it any text information (blog articles, documentation, your company's knowledge base), and it will output a vector of floating point numbers that represents the “meaning” of that text.

Compared to our 2-dimensional example above, their latest embedding model `text-embedding-ada-002` will output 1536 dimensions.

Why is this useful? Once we have generated embeddings on multiple texts, it is trivial to calculate how similar they are using vector math operations like cosine distance. A perfect use case for this is search. Your process might look something like this:

1. Pre-process your knowledge base and generate embeddings for each page
2. Store your embeddings to be referenced later (more on this)
3. Build a search page that prompts your user for input
4. Take user's input, generate a one-time embedding, then perform a similarity search against your pre-processed embeddings.
5. Return the most similar pages to the user

## Embeddings in practice [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#embeddings-in-practice)

At a small scale, you could store your embeddings in a CSV file, load them into Python, and use a library like `numPy` to calculate similarity between them using something like cosine distance or dot product. OpenAI has a cookbook [example](https://github.com/openai/openai-cookbook/blob/main/examples/Semantic_text_search_using_embeddings.ipynb) that does just that. Unfortunately this likely won't scale well:

- What if I need to store and search over a large number of documents and embeddings (more than can fit in memory)?
- What if I want to create/update/delete embeddings dynamically?
- What if I'm not using Python?

### Using PostgreSQL [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#using-postgresql)

Enter [`pgvector`](https://github.com/pgvector/pgvector), an extension for PostgreSQL that allows you to both store and query vector embeddings within your database. Let's try it out.

First we'll enable the **Vector** extension. In Supabase, this can be done from the web portal through `Database` → `Extensions`. You can also do this in SQL by running:

`
create extension vector;
`

Next let's create a table to store our documents and their embeddings:

`
create table documents (
id bigserial primary key,
content text,
embedding vector(1536)
);
`

`pgvector` introduces a new data type called `vector`. In the code above, we create a column named `embedding` with the `vector` data type. The size of the vector defines how many dimensions the vector holds. OpenAI's `text-embedding-ada-002` model outputs 1536 dimensions, so we will use that for our vector size.

We also create a `text` column named `content` to store the original document text that produced this embedding. Depending on your use case, you might just store a reference (URL or foreign key) to a document here instead.

Soon we're going to need to perform a similarity search over these embeddings. Let's create a function to do that:

`
create or replace function match_documents (
query_embedding vector(1536),
match_threshold float,
match_count int
)
returns table (
id bigint,
content text,
similarity float
)
language sql stable
as $$
select
    documents.id,
    documents.content,
    1 - (documents.embedding <=> query_embedding) as similarity
from documents
where documents.embedding <=> query_embedding < 1 - match_threshold
order by documents.embedding <=> query_embedding
limit match_count;
$$;
`

`pgvector` introduces 3 new operators that can be used to calculate similarity:

| Operator | Description |
| --- | --- |
| `<->` | Euclidean distance |
| `<#>` | negative inner product |
| `<=>` | cosine distance |

OpenAI recommends cosine similarity on their embeddings, so we will use that here.

Now we can call `match_documents()`, pass in our embedding, similarity threshold, and match count, and we'll get a list of all documents that match. And since this is all managed by Postgres, our application code becomes very simple.

### Indexing [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#indexing)

Once your table starts to grow with embeddings, you will likely want to add an index to speed up queries. Vector indexes are particularly important when you're ordering results because vectors are not grouped by similarity, so finding the closest by sequential scan is a resource-intensive operation.

Each distance operator requires a different type of index. We expect to order by cosine distance, so we need `vector_cosine_ops` index. A good starting number of lists is 4 \* sqrt(table\_rows):

`
create index on documents using ivfflat (embedding vector_cosine_ops)
with
(lists = 100);
`

You can read more about indexing on `pgvector`'s GitHub page [here](https://github.com/pgvector/pgvector#indexing).

### Generating embeddings [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#generating-embeddings)

Let's use JavaScript to generate embeddings and store them in Postgres:

`
import { createClient } from '@supabase/supabase-js'
import { Configuration, OpenAIApi } from 'openai'
import { supabaseClient } from './lib/supabase'
async function generateEmbeddings() {
const configuration = new Configuration({ apiKey: '<YOUR_OPENAI_API_KEY>' })
const openAi = new OpenAIApi(configuration)
const documents = await getDocuments() // Your custom function to load docs
// Assuming each document is a string
for (const document of documents) {
    // OpenAI recommends replacing newlines with spaces for best results
    const input = document.replace(/\n/g, ' ')
    const embeddingResponse = await openai.createEmbedding({
      model: 'text-embedding-ada-002',
      input,
    })
    const [{ embedding }] = embeddingResponse.data.data
    // In production we should handle possible errors
    await supabaseClient.from('documents').insert({
      content: document,
      embedding,
    })
}
}
`

### Building a simple search function [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#building-a-simple-search-function)

Finally, let's create an [Edge Function](https://supabase.com/docs/guides/functions) to perform our similarity search:

`
import { serve } from 'https://deno.land/std@0.170.0/http/server.ts'
import 'https://deno.land/x/xhr@0.2.1/mod.ts'
import { createClient } from 'jsr:@supabase/supabase-js@2'
import { Configuration, OpenAIApi } from 'https://esm.sh/openai@3.1.0'
import { supabaseClient } from './lib/supabase'
export const corsHeaders = {
'Access-Control-Allow-Origin': '*',
'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}
serve(async (req) => {
// Handle CORS
if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
}
// Search query is passed in request payload
const { query } = await req.json()
// OpenAI recommends replacing newlines with spaces for best results
const input = query.replace(/\n/g, ' ')
const configuration = new Configuration({ apiKey: '<YOUR_OPENAI_API_KEY>' })
const openai = new OpenAIApi(configuration)
// Generate a one-time embedding for the query itself
const embeddingResponse = await openai.createEmbedding({
    model: 'text-embedding-ada-002',
    input,
})
const [{ embedding }] = embeddingResponse.data.data
// In production we should handle possible errors
const { data: documents } = await supabaseClient.rpc('match_documents', {
    query_embedding: embedding,
    match_threshold: 0.78, // Choose an appropriate threshold for your data
    match_count: 10, // Choose the number of matches
})
return new Response(JSON.stringify(documents), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
})
})
`

### Building a smarter search function [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#building-a-smarter-search-function)

ChatGPT doesn't just return existing documents. It's able to assimilate a variety of information into a single, cohesive answer. To do this, we need to provide GPT with some relevant documents, and a prompt that it can use to formulate this answer.

One of the biggest challenges of OpenAI's `text-davinci-003` [completion model](https://beta.openai.com/docs/guides/completion) is the 4000 token limit. You must fit both your prompt and the resulting completion within the 4000 tokens. This makes it challenging if you wanted to prompt GPT-3 to answer questions about your own custom knowledge base that would never fit in a single prompt.

Embeddings can help solve this by splitting your prompts into a two-phased process:

1. Query your embedding database for the most relevant documents related to the question
2. Inject these documents as context for GPT-3 to reference in its answer

Here's another Edge Function that expands upon the simple example above:

``
import { serve } from 'https://deno.land/std@0.170.0/http/server.ts'
import 'https://deno.land/x/xhr@0.2.1/mod.ts'
import { createClient } from 'jsr:@supabase/supabase-js@2'
import GPT3Tokenizer from 'https://esm.sh/gpt3-tokenizer@1.1.5'
import { Configuration, OpenAIApi } from 'https://esm.sh/openai@3.1.0'
import { oneLine, stripIndent } from 'https://esm.sh/common-tags@1.8.2'
import { supabaseClient } from './lib/supabase'
export const corsHeaders = {
'Access-Control-Allow-Origin': '*',
'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}
serve(async (req) => {
// Handle CORS
if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
}
// Search query is passed in request payload
const { query } = await req.json()
// OpenAI recommends replacing newlines with spaces for best results
const input = query.replace(/\n/g, ' ')
const configuration = new Configuration({ apiKey: '<YOUR_OPENAI_API_KEY>' })
const openai = new OpenAIApi(configuration)
// Generate a one-time embedding for the query itself
const embeddingResponse = await openai.createEmbedding({
    model: 'text-embedding-ada-002',
    input,
})
const [{ embedding }] = embeddingResponse.data.data
// Fetching whole documents for this simple example.
//
// Ideally for context injection, documents are chunked into
// smaller sections at earlier pre-processing/embedding step.
const { data: documents } = await supabaseClient.rpc('match_documents', {
    query_embedding: embedding,
    match_threshold: 0.78, // Choose an appropriate threshold for your data
    match_count: 10, // Choose the number of matches
})
const tokenizer = new GPT3Tokenizer({ type: 'gpt3' })
let tokenCount = 0
let contextText = ''
// Concat matched documents
for (let i = 0; i < documents.length; i++) {
    const document = documents[i]
    const content = document.content
    const encoded = tokenizer.encode(content)
    tokenCount += encoded.text.length
    // Limit context to max 1500 tokens (configurable)
    if (tokenCount > 1500) {
      break
    }
    contextText += `${content.trim()}\n---\n`
}
const prompt = stripIndent`${oneLine`
    You are a very enthusiastic Supabase representative who loves
    to help people! Given the following sections from the Supabase
    documentation, answer the question using only that information,
    outputted in markdown format. If you are unsure and the answer
    is not explicitly written in the documentation, say
    "Sorry, I don't know how to help with that."`}
    Context sections:
    ${contextText}
    Question: """
    ${query}
    """
    Answer as markdown (including related code snippets if available):
`
// In production we should handle possible errors
const completionResponse = await openai.createCompletion({
    model: 'text-davinci-003',
    prompt,
    max_tokens: 512, // Choose the max allowed tokens in completion
    temperature: 0, // Set to 0 for deterministic results
})
const {
    id,
    choices: [{ text }],
} = completionResponse.data
return new Response(JSON.stringify({ id, text }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
})
})
``

### Streaming results [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#streaming-results)

OpenAI API responses take longer to depending on the length of the “answer”. ChatGPT has a nice UX for this by streaming the response to the user immediately. You can see a similar effect for the Supabase docs:

The OpenAI API supports [completion streaming](https://platform.openai.com/docs/api-reference/completions/create#completions/create-stream) with Server Side Events. Supabase Edge Functions are run Deno, which also supports [Server Side Events](https://deno.com/blog/deploy-streams#server-sent-events). Check out [this commit](https://github.com/supabase/supabase/pull/12056/commits/bd83e9ba2f7263440888228e3b29007604d94841) to see how we modified the Function above to build a streaming interface.

## Wrap up [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#wrap-up)

Storing embeddings in Postgres opens a world of possibilities. You can combine your search function with telemetry functions, add an user-provided feedback (thumbs up/down), and make your search feel more integrated with your products.

The [pgvector extension](https://supabase.com/docs/guides/ai/vector-columns) is available on all new Supabase projects today. To try it out, launch a new Postgres database: [database.new](https://database.new/)

## More pgvector and AI resources [\#](https://supabase.com/blog/openai-embeddings-postgres-vector\#more-pgvector-and-ai-resources)

- [Supabase Clippy: ChatGPT for Supabase Docs](https://supabase.com/blog/chatgpt-supabase-docs)
- [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
- [How to build ChatGPT Plugin from scratch with Supabase Edge Runtime](https://supabase.com/blog/building-chatgpt-plugins-template)
- [Docs pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
- [Choosing Compute Add-on for AI workloads](https://supabase.com/docs/guides/ai/choosing-compute-addon)
- [pgvector v0.5.0: Faster semantic search with HNSW indexes](https://supabase.com/blog/increase-performance-pgvector-hnsw)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopenai-embeddings-postgres-vector&text=Storing%20OpenAI%20embeddings%20in%20Postgres%20with%20pgvector)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopenai-embeddings-postgres-vector&text=Storing%20OpenAI%20embeddings%20in%20Postgres%20with%20pgvector)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fopenai-embeddings-postgres-vector&t=Storing%20OpenAI%20embeddings%20in%20Postgres%20with%20pgvector)

[Last post\\
\\
**Supabase Clippy: ChatGPT for Supabase Docs** \\
\\
7 February 2023](https://supabase.com/blog/chatgpt-supabase-docs)

[Next post\\
\\
**Supabase Beta December 2022** \\
\\
5 January 2023](https://supabase.com/blog/supabase-beta-december-2022)

[postgres](https://supabase.com/blog/tags/postgres) [AI](https://supabase.com/blog/tags/AI) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [What are embeddings?](https://supabase.com/blog/openai-embeddings-postgres-vector#what-are-embeddings)
- [Human language](https://supabase.com/blog/openai-embeddings-postgres-vector#human-language)
- [How do embeddings work?](https://supabase.com/blog/openai-embeddings-postgres-vector#how-do-embeddings-work)
- [OpenAI embeddings](https://supabase.com/blog/openai-embeddings-postgres-vector#openai-embeddings)
- [Embeddings in practice](https://supabase.com/blog/openai-embeddings-postgres-vector#embeddings-in-practice)
  - [Using PostgreSQL](https://supabase.com/blog/openai-embeddings-postgres-vector#using-postgresql)
  - [Indexing](https://supabase.com/blog/openai-embeddings-postgres-vector#indexing)
  - [Generating embeddings](https://supabase.com/blog/openai-embeddings-postgres-vector#generating-embeddings)
  - [Building a simple search function](https://supabase.com/blog/openai-embeddings-postgres-vector#building-a-simple-search-function)
  - [Building a smarter search function](https://supabase.com/blog/openai-embeddings-postgres-vector#building-a-smarter-search-function)
  - [Streaming results](https://supabase.com/blog/openai-embeddings-postgres-vector#streaming-results)
- [Wrap up](https://supabase.com/blog/openai-embeddings-postgres-vector#wrap-up)
- [More pgvector and AI resources](https://supabase.com/blog/openai-embeddings-postgres-vector#more-pgvector-and-ai-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopenai-embeddings-postgres-vector&text=Storing%20OpenAI%20embeddings%20in%20Postgres%20with%20pgvector)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopenai-embeddings-postgres-vector&text=Storing%20OpenAI%20embeddings%20in%20Postgres%20with%20pgvector)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fopenai-embeddings-postgres-vector&t=Storing%20OpenAI%20embeddings%20in%20Postgres%20with%20pgvector)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)