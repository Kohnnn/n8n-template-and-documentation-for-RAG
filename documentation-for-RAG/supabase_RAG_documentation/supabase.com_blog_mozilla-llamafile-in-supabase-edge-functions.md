---
url: "https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions"
title: "Mozilla Llamafile in Supabase Edge Functions"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Mozilla Llamafile in Supabase Edge Functions

21 Aug 2024

•

7 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Mozilla Llamafile in Supabase Edge Functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmozilla-llamafile%2Fmozilla-llamafile-og.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

A few months back, we introduced support for running [AI Inference directly from Supabase Edge Functions](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions).

Today we are adding [Mozilla Llamafile](https://github.com/Mozilla-Ocho/llamafile), in addition to [Ollama](https://supabase.com/docs/guides/functions/ai-models#using-large-language-models), to be used as the Inference Server with your functions.

Mozilla Llamafile lets you distribute and run LLMs with a single file that runs locally on most computers, with no installation! In addition to a local web UI chat server, Llamafile also provides an OpenAI API compatible server, that is now integrated with Supabase Edge Functions.

Mozilla Llamafile in Supabase Edge Functions - YouTube

Supabase

54.4K subscribers

[Mozilla Llamafile in Supabase Edge Functions](https://www.youtube.com/watch?v=_6L-dnBn2wg)

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

[Watch on](https://www.youtube.com/watch?v=_6L-dnBn2wg&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=_6L-dnBn2wg "Watch on YouTube")

Want to jump straight into the code? You can find the examples on [GitHub](https://github.com/supabase/supabase/blob/master/examples/ai/llamafile-edge)!

## Getting started [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#getting-started)

Follow the [Llamafile Quickstart Guide](https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file#quickstart) to get up and running with the [Llamafile of your choice](https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file#other-example-llamafiles).

Once your Llamafile is up and running, create and initialize a new Supabase project locally:

`
npx supabase bootstrap scratch
`

If using VS Code, when promptedt `Generate VS Code settings for Deno? [y/N]` select `y` and follow the steps. Then open the project in your favoiurte code editor.

## Call Llamafile with functions-js [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#call-llamafile-with-functions-js)

Supabase Edge Functions now comes with an OpenAI API compatible mode, allowing you to call a Llamafile server easily via `@supabase/functions-js`.

Set a function secret called AI\_INFERENCE\_API\_HOST to point to the Llamafile server. If you don't have one already, create a new `.env` file in the `functions/` directory of your Supabase project.

supabase/functions/.env

`
AI_INFERENCE_API_HOST=http://host.docker.internal:8080
`

Next, create a new function called `llamafile`:

`
npx supabase functions new llamafile
`

Then, update the `supabase/functions/llamafile/index.ts` file to look like this:

supabase/functions/llamafile/index.ts

`
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
const session = new Supabase.ai.Session('LLaMA_CPP')
Deno.serve(async (req: Request) => {
const params = new URL(req.url).searchParams
const prompt = params.get('prompt') ?? ''
// Get the output as a stream
const output = await session.run(
    {
      messages: [\
        {\
          role: 'system',\
          content:\
            'You are LLAMAfile, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests.',\
        },\
        {\
          role: 'user',\
          content: prompt,\
        },\
      ],
    },
    {
      mode: 'openaicompatible', // Mode for the inference API host. (default: 'ollama')
      stream: false,
    }
)
console.log('done')
return Response.json(output)
})
`

## Call Llamafile with the OpenAI Deno SDK [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#call-llamafile-with-the-openai-deno-sdk)

Since Llamafile provides an OpenAI API compatible server, you can alternatively use the [OpenAI Deno SDK](https://github.com/openai/openai-deno) to call Llamafile from your Supabase Edge Functions.

For this, you will need to set the following two environment variables in your Supabase project. If you don't have one already, create a new `.env` file in the `functions/` directory of your Supabase project.

supabase/functions/.env

`
OPENAI_BASE_URL=http://host.docker.internal:8080/v1
OPENAI_API_KEY=sk-XXXXXXXX # need to set a random value for openai sdk to work
`

Now, replace the code in your `llamafile` function with the following:

supabase/functions/llamafile/index.ts

`
import OpenAI from 'https://deno.land/x/openai@v4.53.2/mod.ts'
Deno.serve(async (req) => {
const client = new OpenAI()
const { prompt } = await req.json()
const stream = true
const chatCompletion = await client.chat.completions.create({
    model: 'LLaMA_CPP',
    stream,
    messages: [\
      {\
        role: 'system',\
        content:\
          'You are LLAMAfile, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests.',\
      },\
      {\
        role: 'user',\
        content: prompt,\
      },\
    ],
})
if (stream) {
    const headers = new Headers({
      'Content-Type': 'text/event-stream',
      Connection: 'keep-alive',
    })
    // Create a stream
    const stream = new ReadableStream({
      async start(controller) {
        const encoder = new TextEncoder()
        try {
          for await (const part of chatCompletion) {
            controller.enqueue(encoder.encode(part.choices[0]?.delta?.content || ''))
          }
        } catch (err) {
          console.error('Stream error:', err)
        } finally {
          controller.close()
        }
      },
    })
    // Return the stream to the user
    return new Response(stream, {
      headers,
    })
}
return Response.json(chatCompletion)
})
`

Note that the model parameter doesn't have any effect here! The model depends on which Llamafile is currently running!

## Serve your functions locally [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#serve-your-functions-locally)

To serve your functions locally, you need to install the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started#running-supabase-locally) as well as [Docker Desktop](https://docs.docker.com/desktop) or [Orbstack](https://orbstack.dev/).

You can now serve your functions locally by running:

`
supabase start
supabase functions serve --env-file supabase/functions/.env
`

Execute the function

`
curl --get "http://localhost:54321/functions/v1/llamafile" \
 --data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \
 -H "Authorization: $ANON_KEY"
`

## Deploying a Llamafile [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#deploying-a-llamafile)

There is a great guide on how to [containerize a Lllamafile](https://www.docker.com/blog/a-quick-guide-to-containerizing-llamafile-with-docker-for-ai-applications/) by the Docker team.

You can then use a service like [Fly.io](https://fly.io/) to deploy your dockerized Llamafile.

## Deploying your Supabase Edge Functions [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#deploying-your-supabase-edge-functions)

Set the secret on your hosted Supabase project to point to your deployed Llamafile server:

`
supabase secrets set --env-file supabase/functions/.env
`

Deploy your Supabase Edge Functions:

`
supabase functions deploy
`

Execute the function:

`
curl --get "https://project-ref.supabase.co/functions/v1/llamafile" \
 --data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \
 -H "Authorization: $ANON_KEY"
`

## Get access to Supabase Hosted LLMs [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#get-access-to-supabase-hosted-llms)

Access to open-source LLMs is currently invite-only while we manage demand for the GPU instances. Please [get in touch](https://forms.supabase.com/supabase.ai-llm-early-access) if you need early access.

We plan to extend support for more models. [Let us know](https://forms.supabase.com/supabase.ai-llm-early-access) which models you want next. We're looking to support fine-tuned models too!

## More Supabase Resources [\#](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions\#more-supabase-resources)

- Edge Functions: [supabase.com/docs/guides/functions](https://supabase.com/docs/guides/functions)
- Vectors: [supabase.com/docs/guides/ai](https://supabase.com/docs/guides/ai)
- [Semantic search demo](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions)
- [Store and query embeddings](https://supabase.com/docs/guides/ai/vector-columns#querying-a-vector--embedding) in Postgres and use them for Retrieval Augmented Generation (RAG) and Semantic Search

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmozilla-llamafile-in-supabase-edge-functions&text=Mozilla%20Llamafile%20in%20Supabase%20Edge%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmozilla-llamafile-in-supabase-edge-functions&text=Mozilla%20Llamafile%20in%20Supabase%20Edge%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmozilla-llamafile-in-supabase-edge-functions&t=Mozilla%20Llamafile%20in%20Supabase%20Edge%20Functions)

[Last post\\
\\
**Supabase Launch Week 12 Hackathon** \\
\\
26 August 2024](https://supabase.com/blog/supabase-lw12-hackathon)

[Next post\\
\\
**Top 10 Launches of Launch Week 12** \\
\\
16 August 2024](https://supabase.com/blog/launch-week-12-top-10)

[functions](https://supabase.com/blog/tags/functions) [AI](https://supabase.com/blog/tags/AI)

On this page

- [Getting started](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#getting-started)
- [Call Llamafile with functions-js](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#call-llamafile-with-functions-js)
- [Call Llamafile with the OpenAI Deno SDK](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#call-llamafile-with-the-openai-deno-sdk)
- [Serve your functions locally](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#serve-your-functions-locally)
- [Deploying a Llamafile](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#deploying-a-llamafile)
- [Deploying your Supabase Edge Functions](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#deploying-your-supabase-edge-functions)
- [Get access to Supabase Hosted LLMs](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#get-access-to-supabase-hosted-llms)
- [More Supabase Resources](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions#more-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmozilla-llamafile-in-supabase-edge-functions&text=Mozilla%20Llamafile%20in%20Supabase%20Edge%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmozilla-llamafile-in-supabase-edge-functions&text=Mozilla%20Llamafile%20in%20Supabase%20Edge%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmozilla-llamafile-in-supabase-edge-functions&t=Mozilla%20Llamafile%20in%20Supabase%20Edge%20Functions)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)