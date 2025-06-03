---
url: "https://supabase.com/blog/hugging-face-supabase"
title: "Hugging Face is now supported in Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Hugging Face is now supported in Supabase

07 Aug 2023

•

10 minute read

[![Greg Richardson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgregnr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Greg RichardsonEngineering](https://github.com/gregnr)

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![Hugging Face is now supported in Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-1%2Fhugging-face-supabase-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Since launching our [Vector Toolkit](https://supabase.com/vector) a few months ago, the number of AI applications on Supabase has grown - a lot. Hundreds of new databases every week are using [pgvector](https://github.com/pgvector/pgvector).

98% of those applications use OpenAI to store embeddings using the `text-embedding-ada-002` model. While OpenAI is easy, it’s not open source, which means it can’t be self-hosted.

Our goal at Supabase is to [promote open source collaboration](https://supabase.com/docs/guides/getting-started/architecture#support-existing-tools), and [Hugging Face](https://huggingface.co/) is one of the open source communities we admire most. Today, we’re adding first-class support for Hugging Face, starting with embeddings. Why embeddings? Because this is one area where open source models are [measurably ahead](https://supabase.com/blog/fewer-dimensions-are-better-pgvector) for pgvector performance.

We’ve added support in our [Python Vector Client](https://supabase.com/docs/guides/ai/python/api) and [Edge Functions](https://supabase.com/docs/guides/functions) (Deno/Javascript). Let’s start with Python.

Use Hugging Face AI models with Supabase 🤖 - YouTube

Supabase

54.4K subscribers

[Use Hugging Face AI models with Supabase 🤖](https://www.youtube.com/watch?v=RJccSbJ9Go4)

Supabase

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=RJccSbJ9Go4 "Watch on YouTube")

## Hugging Face with Python [\#](https://supabase.com/blog/hugging-face-supabase\#hugging-face-with-python)

[supabase/vecs](https://github.com/supabase/vecs) is our Python client for vector projects. Today, we're releasing a new feature for vecs called "adapters".

Adapters transform your input into a new format when upserting and querying. For example, you can split large text into smaller chunks, or transform it into embeddings. And, of course, Adapters have first-class support for Hugging Face models.

As an example, let’s look at how we might adapt text input. If we're inserting large text documents, it might be a good idea to chunk the text into paragraphs using the ParagraphChunker before creating an embedding for each paragraph with the TextEmbedding adapter step.

`
import vecs
from vecs.adapter import Adapter, ParagraphChunker, TextEmbedding
vx = vecs.create_client("postgresql://<user>:<password>@<host>:<port>/<db_name>")
# create a new collection with an associated adapter
docs = vx.get_or_create_collection(
    name="docs",
    # here comes the new part
    adapter=Adapter(
        [\
            ParagraphChunker(skip_during_query=True),\
            TextEmbedding(model='Supabase/gte-small'),\
        ]
    )
)
`

In the example, we're using the `gte-small` model, but any model compatible with [sentence transformers](https://www.sbert.net/docs/pretrained_models.html) can be used in its place.

Once the adapter is registered with the collection we can upsert data using plain text and records are automatically converted to vectors:

`
# Upsert
docs.upsert(
    records=[\
        (\
         "vec0",\
         "the diameter of a 747 ...", # <- inserting text!\
         {"publish_year": 2019}\
        )\
    ]
)
`

Similarly, queries are transparently converted into vectors:

`
# Search by text
docs.query(data="how many ping pong balls fit in a Boeing ...")
# Results: [...]
`

## Hugging Face with Edge Functions [\#](https://supabase.com/blog/hugging-face-supabase\#hugging-face-with-edge-functions)

AI/ML is primarily the domain of the Python community, but thanks to some amazing work by [Joshua](https://twitter.com/xenovacom) at Hugging Face, you can now run inference workloads in Deno/JavaScript. This is an exciting development. It opens up the world of AI/ML to millions of new developers. We’re hoping to accelerate this with better Hugging Face tooling within Supabase Edge Functions.

Let’s step through a small demo where we accept some text, convert it into an embedding, and then store it in our Postgres database. You can create a new function with supabase functions new embed and fill it with the following code snippet:

`
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { env, pipeline } from 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.5.0'
import { createClient } from 'jsr:@supabase/supabase-js@2'
// Preparation for Deno runtime
env.useBrowserCache = false
env.allowLocalModels = false
const supabase = createClient(
'https://xyzcompany.supabase.co',
'public-anon-key',
)
// Construct pipeline outside of serve for faster warm starts
const pipe = await pipeline(
'feature-extraction',
'Supabase/gte-small',
)
// Deno Handler
serve(async (req) => {
const { input } = await req.json()
// Generate the embedding from the user input
const output = await pipe(input, {
    pooling: 'mean',
    normalize: true,
})
// Get the embedding output
const embedding = Array.from(output.data)
// Store the embedding
const { data, error } = await supabase
    .from('collections')
    .insert({ embedding })
// Return the embedding
return new Response(
    { new_row: data },
    { headers: { 'Content-Type': 'application/json' } },
)
})
`

Now run `supabase functions serve` and you’re ready to call your function locally:

`
curl --request POST 'http://localhost:54321/functions/v1/embed' \
  --header 'Authorization: Bearer ANON_KEY' \
  --header 'Content-Type: application/json' \
  --data '{ "input": "hello world" }'
`

With just 40 lines of code, we’ve created an API route that can accept some user content, convert it to an embedding, store it in your database, and then return the database row as JSON. This is especially useful for sensitive data since you can run this entirely on your own infrastructure.

Supabase also provides [Database Webhooks](https://supabase.com/docs/guides/database/webhooks) which can trigger an Edge Function any time a row is inserted. This means you can upload plain text to your database and use a background job to convert the text to an embedding.

## Hugging Face from the browser [\#](https://supabase.com/blog/hugging-face-supabase\#hugging-face-from-the-browser)

One of the coolest ideas we’ve seen so far is the ability to support Hugging Face models directly in the browser. With sufficiently small models, you can embed them directly into your application and cut out an entire network hop.

![Hugging Face from the browser example](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-1%2Fhugging-face-from-the-browser-middleware.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This is great for search, where you might want to “debounce” the user query as they type. Of course, this is only helpful if you have a database that allows access from the browser. Fortunately, Supabase provides that functionality using Postgres Row Level Security and PostgREST:

![Hugging Face from the browser with postgREST](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-1%2Fhugging-face-from-the-browser-postgrest.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

For example, if we were storing image embeddings inside our database, we could provide search functionality using a simple Postgres function, powered by pgvector:

`
create function match_images (
    query_embedding vector(512),
    match_threshold float,
    match_count int
)
returns setof images
language sql stable
as $$
	select *, 1 - (image_embedding <=> query_embedding) as similarity
	from images
	where 1 - (image_embedding <=> query_embedding) > match_threshold
	order by similarity desc
	limit match_count;
$$;
`

Now, we can call that function directly from the browser using [supabase-js](https://supabase.com/docs/reference/javascript/installing):

`
let { data: images, error } = await supabase.rpc('match_images', {
query_embedding,
match_threshold,
match_count,
})
`

Of course, even the [smallest](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) quantized models in the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) are around 20 MB - so you won’t be seeing this on an e-commerce store any time soon. But for some web-based applications or browser extensions it’s an exciting prospect.

Check out [this demo](https://huggingface.co/spaces/Xenova/semantic-image-search) for inspiration, which uses the Unsplash data set and provides image search functionality using natural language:

![Hugging Face from the browser - demo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-1%2Fhugging-face-from-the-browser-demo.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Choosing a Hugging Face model [\#](https://supabase.com/blog/hugging-face-supabase\#choosing-a-hugging-face-model)

Supabase is mainly used to store embeddings, so that’s where we’re starting. Over time we’ll add more Hugging Face support - even beyond embeddings. To help you identify which Hugging Face model to use, we ran a detailed analysis and found that embeddings with [fewer dimensions are better](https://supabase.com/blog/fewer-dimensions-are-better-pgvector) within pgvector. Fewer dimensions have several advantages:

1. They require less space in your database (saving you money!)
2. Retrieval is faster

To simplify your choice we’ve shortlisted a few recommendations in the official [Supabase org on Hugging Face](https://huggingface.co/Supabase). The [gte-small](https://huggingface.co/Supabase/gte-small) model is the best (it even [outperforms OpenAI’s embedding model](https://huggingface.co/spaces/mteb/leaderboard) in some tasks), but it’s only trained on English text, so you’ll need to find another model if you have non-English text.

Remember also, you can continue to use OpenAI for generative use cases. This means you get the best of both worlds - fast embeddings with Hugging Face and advanced AI with OpenAI’s GPT-3.5/4.

## Plans for the future [\#](https://supabase.com/blog/hugging-face-supabase\#plans-for-the-future)

We’re in the early stages of development, and we have some exciting ideas to overcome the limitations of this initial release.

### Reducing cold starts [\#](https://supabase.com/blog/hugging-face-supabase\#reducing-cold-starts)

Cold starts are the time it takes for the “initial load” of an Edge Function. Because the model needs to be downloaded to the Edge Function, cold starts can take anywhere from ~2-6s (based on the model). Loading the initial model and building the pipeline usually contributes to it. We are experimenting with the idea of attaching a “read-only disk” of models to our [Edge Runtime](https://github.com/supabase/edge-runtime) which mitigate any download penalties. We’ll share more details about these optimizations in a future blog post.

### Handling heavier workloads [\#](https://supabase.com/blog/hugging-face-supabase\#handling-heavier-workloads)

The current quotas provided by Edge Functions are sufficient for running common embedding models. Larger AI models and tasks may require extra memory, CPU, and wall-clock limits to run successfully. We will offer customizable compute resources for Edge Functions in the next few months. If you have a workload that may require extra resources [reach out](https://supabase.com/support) for early access.

### Audio and image models [\#](https://supabase.com/blog/hugging-face-supabase\#audio-and-image-models)

Working with audio and image data in Edge Functions is a work in progress. AI models expect audio and image content to be decoded into their raw formats before performing inference, and this isn’t yet turn-key in a Deno environment.

For example, the Whisper audio transcription model requires audio to be passed in as 32-bit floating point pulse-code modulation (PCM) data sampled at exactly 16000Hz. Assuming your audio is stored in an encoded format like MP3, you first need to both decode and possibly resample the data before Whisper can understand it. In the browser, the Web Audio API is available which Transformers.js uses for decoding, but this API isn’t currently available in a Deno environment.

Images have the same challenge. Models like CLIP, which can generate embeddings from images, require images to be decoded into their raw RGBA values and sometimes resized. Transformers.js uses the Canvas API in the browser and `sharp` in Node.js to perform these operations, but Deno doesn’t yet have a turn-key solution ( `sharp` uses Node.js C++ bindings).

## Getting started [\#](https://supabase.com/blog/hugging-face-supabase\#getting-started)

If you’re a Python Dev, check out our [Hello World notebook](https://supabase.com/docs/guides/ai/quickstarts/hello-world). If you’re a JavaScript developer, check out our [Text Embeddings docs](https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings).

And no matter your language preference, remember to jump into the [Hugging Face community](https://github.com/huggingface) and show your support.

## More Launch Week 8 [\#](https://supabase.com/blog/hugging-face-supabase\#more-launch-week-8)

- [Day 2: Supabase Local Dev: migrations, branching, and observability](https://supabase.com/blog/supabase-local-dev)
- [Launch Week 8](https://supabase.com/launch-week)
- [Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber)
- [Why we'll stay remote](https://supabase.com/blog/why-supabase-remote)
- [Postgres Language Server](https://github.com/supabase/postgres_lsp)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhugging-face-supabase&text=Hugging%20Face%20is%20now%20supported%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhugging-face-supabase&text=Hugging%20Face%20is%20now%20supported%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhugging-face-supabase&t=Hugging%20Face%20is%20now%20supported%20in%20Supabase)

[Last post\\
\\
**Supabase Local Dev: migrations, branching, and observability** \\
\\
8 August 2023](https://supabase.com/blog/supabase-local-dev)

[Next post\\
\\
**Why we'll stay remote** \\
\\
5 August 2023](https://supabase.com/blog/why-supabase-remote)

[launch-week](https://supabase.com/blog/tags/launch-week) [announcements](https://supabase.com/blog/tags/announcements)

On this page

- [Hugging Face with Python](https://supabase.com/blog/hugging-face-supabase#hugging-face-with-python)
- [Hugging Face with Edge Functions](https://supabase.com/blog/hugging-face-supabase#hugging-face-with-edge-functions)
- [Hugging Face from the browser](https://supabase.com/blog/hugging-face-supabase#hugging-face-from-the-browser)
- [Choosing a Hugging Face model](https://supabase.com/blog/hugging-face-supabase#choosing-a-hugging-face-model)
- [Plans for the future](https://supabase.com/blog/hugging-face-supabase#plans-for-the-future)
  - [Reducing cold starts](https://supabase.com/blog/hugging-face-supabase#reducing-cold-starts)
  - [Handling heavier workloads](https://supabase.com/blog/hugging-face-supabase#handling-heavier-workloads)
  - [Audio and image models](https://supabase.com/blog/hugging-face-supabase#audio-and-image-models)
- [Getting started](https://supabase.com/blog/hugging-face-supabase#getting-started)
- [More Launch Week 8](https://supabase.com/blog/hugging-face-supabase#more-launch-week-8)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhugging-face-supabase&text=Hugging%20Face%20is%20now%20supported%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhugging-face-supabase&text=Hugging%20Face%20is%20now%20supported%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhugging-face-supabase&t=Hugging%20Face%20is%20now%20supported%20in%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)