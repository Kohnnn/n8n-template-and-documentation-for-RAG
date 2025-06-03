---
url: "https://supabase.com/blog/edge-functions-background-tasks-websockets"
title: "Supabase Edge Functions: Introducing Background Tasks, Ephemeral Storage, and WebSockets"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Edge Functions: Introducing Background Tasks, Ephemeral Storage, and WebSockets

03 Dec 2024

•

10 minute read

[![Lakshan Perera avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Flaktek.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Lakshan PereraEngineering](https://github.com/laktek)

[![Nyannyacha avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fnyannyacha.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
NyannyachaEngineering](https://github.com/nyannyacha)

![Supabase Edge Functions: Introducing Background Tasks, Ephemeral Storage, and WebSockets](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-2-functions-background-tasks%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We are excited to announce three long-awaited features: Background Tasks, Ephemeral File Storage, and WebSockets.

Starting today, you can use these features in any project. Let's explore what exciting things you can build with them.

3 new things you can do with SupaCharged Edge Functions - YouTube

Supabase

54.4K subscribers

[3 new things you can do with SupaCharged Edge Functions](https://www.youtube.com/watch?v=envrsJ8VfAU)

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

[Watch on YouTube](https://www.youtube.com/watch?v=envrsJ8VfAU "Watch on YouTube")

## Background Tasks [\#](https://supabase.com/blog/edge-functions-background-tasks-websockets\#background-tasks)

Sometimes you need a backend logic to do more than respond to a request. For example, you might want to process a batch of files and upload the results to Supabase Storage. Or read multiple entries from a database table and generate embeddings for each entry.

With the introduction of background tasks, executing these long-running workloads with Edge Functions is super easy.

We've introduced a new method called `EdgeRuntime.waitUntil` , which accepts a promise. This ensures that the function isn't terminated until the promise is resolved.

Free projects can run background tasks for a maximum of 150 seconds (2m 30s). If you are on a paid plan, this limit increases to 400 seconds (6m 40s). We plan to introduce more flexible limits in the coming months.

You can subscribe to notifications when the function is about to be shut down by listening to `beforeunload` event. Read the guide for more details on [how to use background tasks](https://supabase.com/docs/guides/functions/background-tasks).

## Ephemeral Storage [\#](https://supabase.com/blog/edge-functions-background-tasks-websockets\#ephemeral-storage)

Edge Function invocations now have access to ephemeral storage. This is useful for background tasks, as it allows you to read and write files in the `/tmp` directory to store intermediate results.

Check the guide on how to access [ephemeral storage](https://supabase.com/docs/guides/functions/ephemeral-storage).

### Example: Extracting a zip file and uploading its content to Supabase Storage [\#](https://supabase.com/blog/edge-functions-background-tasks-websockets\#example-extracting-a-zip-file-and-uploading-its-content-to-supabase-storage)

Let's look at a real-world example using Background Tasks and Ephemeral Storage.

Imagine you're building a Photo Album app. You want your users to upload photos as a zip file. You would extract them in an Edge Function and upload them to storage.

One of the most straightforward ways to implement is using streams:

`
import { ZipReaderStream } from 'https://deno.land/x/zipjs/index.js'
import { createClient } from 'jsr:@supabase/supabase-js@2'
const supabase = createClient(
Deno.env.get('SUPABASE_URL'),
Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
)
Deno.serve(async (req) => {
const uploadId = crypto.randomUUID()
const { error } = await supabase.storage.createBucket(uploadId, {
    public: false,
})
for await (const entry of await req.body.pipeThrough(new ZipReaderStream())) {
    // write file to Supabase Storage
    const { error } = await supabase.storage
      .from(uploadId)
      .upload(entry.filename, entry.readable, {})
    console.log('uploaded', entry.filename)
}
return new Response(
    JSON.stringify({
      uploadId,
    }),
    {
      headers: {
        'content-type': 'application/json',
      },
    }
)
})
`

If you test out the streaming version, it will run into memory limit errors when you try to upload zip files over 100MB. This is because the streaming version has to keep every file in a zip archive in memory.

We can modify it instead to write the zip file to a temporary file. Then, use a background task to extract and upload it to Supabase Storage. This way, we only read parts of the zip file to the memory.

``
import { BlobWriter, ZipReader, ZipReaderStream } from 'https://deno.land/x/zipjs/index.js'
import { createClient } from 'jsr:@supabase/supabase-js@2'
const supabase = createClient(
Deno.env.get('SUPABASE_URL'),
Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
)
let numFilesUploaded = 0
async function processZipFile(uploadId, filepath) {
const file = await Deno.open(filepath, { read: true })
const zipReader = new ZipReader(file.readable)
const entries = await zipReader.getEntries()
await supabase.storage.createBucket(uploadId, {
    public: false,
})
await Promise.all(
    entries.map(async (entry) => {
      // read file entry
      const blobWriter = new BlobWriter()
      const blob = await entry.getData(blobWriter)
      if (entry.directory) {
        return
      }
      // write file to Supabase Storage
      await supabase.storage.from(uploadId).upload(entry.filename, blob, {})
      numFilesUploaded += 1
      console.log('uploaded', entry.filename)
    })
)
await zipReader.close()
}
// you can add a `beforeunload` event listener to be notified
// when Function Worker is about to terminate.
// use this to do any logging, save states.
globalThis.addEventListener('beforeunload', (ev) => {
console.log('function about to terminate: ', ev.detail.reason)
console.log('number of files uploaded: ', numFilesUploaded)
})
async function writeZipFile(filepath, stream) {
await Deno.writeFile(filepath, stream)
}
Deno.serve(async (req) => {
const uploadId = crypto.randomUUID()
await writeZipFile('/tmp/' + uploadId, req.body)
// process zip file in a background task
// calling EdgeRuntime.waitUntil() would ensure
// function worker wouldn't exit until the promise is completed.
EdgeRuntime.waitUntil(processZipFile(uploadId, '/tmp/' + uploadId))
return new Response(
    JSON.stringify({
      uploadId,
    }),
    {
      headers: {
        'content-type': 'application/json',
      },
    }
)
})
``

## WebSockets [\#](https://supabase.com/blog/edge-functions-background-tasks-websockets\#websockets)

Edge Functions now support establishing both inbound (server) and outbound (client) WebSocket connections. This enables a variety of new use cases.

### Example: Building an authenticated relay to OpenAI Realtime API [\#](https://supabase.com/blog/edge-functions-background-tasks-websockets\#example-building-an-authenticated-relay-to-openai-realtime-api)

OpenAI recently introduced a [Realtime API](https://openai.com/index/introducing-the-realtime-api/), which uses WebSockets. This is tricky to implement purely client-side because you'd need to expose your OpenAI key publicly. OpenAI [recommends](https://platform.openai.com/docs/guides/realtime/overview?text-generation-quickstart-example=audio) building a server to authenticate requests.

With our new support for WebSockets, you can easily do this in Edge Functions without standing up any infrastructure. Additionally, you can use [Supabase Auth](https://supabase.com/docs/guides/auth) to authenticate users and protect your OpenAI usage from being abused.

``
import { createClient } from 'jsr:@supabase/supabase-js@2'
const supabase = createClient(
Deno.env.get('SUPABASE_URL'),
Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
)
const OPENAI_API_KEY = Deno.env.get('OPENAI_API_KEY')
Deno.serve(async (req) => {
const upgrade = req.headers.get('upgrade') || ''
if (upgrade.toLowerCase() != 'websocket') {
    return new Response("request isn't trying to upgrade to websocket.")
}
// WebSocket browser clients does not support sending custom headers.
// We have to use the URL query params to provide user's JWT.
// Please be aware query params may be logged in some logging systems.
const url = new URL(req.url)
const jwt = url.searchParams.get('jwt')
if (!jwt) {
    console.error('Auth token not provided')
    return new Response('Auth token not provided', { status: 403 })
}
const { error, data } = await supabase.auth.getUser(jwt)
if (error) {
    console.error(error)
    return new Response('Invalid token provided', { status: 403 })
}
if (!data.user) {
    console.error('user is not authenticated')
    return new Response('User is not authenticated', { status: 403 })
}
const { socket, response } = Deno.upgradeWebSocket(req)
socket.onopen = () => {
    // initiate an outbound WebSocket connection to OpenAI
    const url = 'wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-10-01'
    // openai-insecure-api-key isn't a problem since this code runs in an Edge Function
    const openaiWS = new WebSocket(url, [\
      'realtime',\
      `openai-insecure-api-key.${OPENAI_API_KEY}`,\
      'openai-beta.realtime-v1',\
    ])
    openaiWS.onopen = () => {
      console.log('Connected to OpenAI server.')
      socket.onmessage = (e) => {
        console.log('socket message:', e.data)
        // only send the message if openAI ws is open
        if (openaiWS.readyState === 1) {
          openaiWS.send(e.data)
        } else {
          socket.send(
            JSON.stringify({
              type: 'error',
              msg: 'openAI connection not ready',
            })
          )
        }
      }
    }
    openaiWS.onmessage = (e) => {
      console.log(e.data)
      socket.send(e.data)
    }
    openaiWS.onerror = (e) => console.log('OpenAI error: ', e.message)
    openaiWS.onclose = (e) => console.log('OpenAI session closed')
}
socket.onerror = (e) => console.log('socket errored:', e.message)
socket.onclose = () => console.log('socket closed')
return response // 101 (Switching Protocols)
})
``

## Performance and stability [\#](https://supabase.com/blog/edge-functions-background-tasks-websockets\#performance-and-stability)

In the past few months, we have made many [performance, stability,](https://supabase.com/blog/edge-functions-faster-smaller) and [DX improvements](https://github.com/orgs/supabase/discussions/30307) to Edge Functions. While these improvements often aren't visible to the end-users, they are the foundation of the new features we are announcing today.

## What's next? [\#](https://supabase.com/blog/edge-functions-background-tasks-websockets\#whats-next)

We have a very exciting roadmap planned for 2025. One of the main priorities is to provide customizable compute limits (memory, CPU, and execution duration). We will soon announce an update on it.

Stay tuned for the upcoming launches this week. You will see how all these upcoming pieces fit like Lego bricks to make your developer life easy.

[Launch Week13](https://supabase.com/launch-week/13)

2-6 December 24

[Day 1 -Supabase AI Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2)

[Day 2 -Supabase Functions: Background Tasks and WebSockets](https://supabase.com/blog/edge-functions-background-tasks-websockets)

[Day 3 -Supabase Cron: Schedule Recurring Jobs in Postgres](https://supabase.com/blog/supabase-cron)

[Day 4 -Supabase Queues](https://supabase.com/blog/supabase-queues)

[Day 5 -database.build v2: Bring-Your-Own-LLM](https://supabase.com/blog/database-build-v2)

Build Stage

[01 -OrioleDB Public Alpha](https://supabase.com/blog/orioledb-launch)

[02 -Supabase CLI v2: Config as Code](https://supabase.com/blog/cli-v2-config-as-code)

[03 -High Performance Disks](https://supabase.com/blog/high-performance-disks)

[04 -Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project)

[05 -Hack the Base! with Supabase](https://supabase.com/blog/hack-the-base)

[Community Meetups](https://supabase.com/events?category=meetup)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-background-tasks-websockets&text=Supabase%20Edge%20Functions%3A%20Introducing%20Background%20Tasks%2C%20Ephemeral%20Storage%2C%20and%20WebSockets)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-background-tasks-websockets&text=Supabase%20Edge%20Functions%3A%20Introducing%20Background%20Tasks%2C%20Ephemeral%20Storage%2C%20and%20WebSockets)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-background-tasks-websockets&t=Supabase%20Edge%20Functions%3A%20Introducing%20Background%20Tasks%2C%20Ephemeral%20Storage%2C%20and%20WebSockets)

[Last post\\
\\
**Supabase CLI v2: Config as Code** \\
\\
4 December 2024](https://supabase.com/blog/cli-v2-config-as-code)

[Next post\\
\\
**Supabase AI Assistant v2** \\
\\
2 December 2024](https://supabase.com/blog/supabase-ai-assistant-v2)

[functions](https://supabase.com/blog/tags/functions) [launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Background Tasks](https://supabase.com/blog/edge-functions-background-tasks-websockets#background-tasks)
- [Ephemeral Storage](https://supabase.com/blog/edge-functions-background-tasks-websockets#ephemeral-storage)
  - [Example: Extracting a zip file and uploading its content to Supabase Storage](https://supabase.com/blog/edge-functions-background-tasks-websockets#example-extracting-a-zip-file-and-uploading-its-content-to-supabase-storage)
- [WebSockets](https://supabase.com/blog/edge-functions-background-tasks-websockets#websockets)
  - [Example: Building an authenticated relay to OpenAI Realtime API](https://supabase.com/blog/edge-functions-background-tasks-websockets#example-building-an-authenticated-relay-to-openai-realtime-api)
- [Performance and stability](https://supabase.com/blog/edge-functions-background-tasks-websockets#performance-and-stability)
- [What's next?](https://supabase.com/blog/edge-functions-background-tasks-websockets#whats-next)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-background-tasks-websockets&text=Supabase%20Edge%20Functions%3A%20Introducing%20Background%20Tasks%2C%20Ephemeral%20Storage%2C%20and%20WebSockets)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-background-tasks-websockets&text=Supabase%20Edge%20Functions%3A%20Introducing%20Background%20Tasks%2C%20Ephemeral%20Storage%2C%20and%20WebSockets)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-background-tasks-websockets&t=Supabase%20Edge%20Functions%3A%20Introducing%20Background%20Tasks%2C%20Ephemeral%20Storage%2C%20and%20WebSockets)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)