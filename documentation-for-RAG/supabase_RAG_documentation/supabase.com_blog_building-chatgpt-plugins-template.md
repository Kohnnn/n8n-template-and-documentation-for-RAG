---
url: "https://supabase.com/blog/building-chatgpt-plugins-template"
title: "Building ChatGPT Plugins with Supabase Edge Runtime"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Building ChatGPT Plugins with Supabase Edge Runtime

15 May 2023

•

10 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Building ChatGPT Plugins with Supabase Edge Runtime](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-15-chatgpt-plugin-temnplate-deno%2Fchatgpt_plugin_template_deno.jpeg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

ChatGPT Plugins support is [rolling out in beta](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) this week! To help you get up and running quickly, we're releasing a [plugin template](https://github.com/supabase-community/chatgpt-plugin-template-deno) written in TypeScript and running on [Supabase Edge Runtime](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)!

Want to get started right away? [Fork the template on GitHub](https://github.com/supabase-community/chatgpt-plugin-template-deno)!

Building ChatGPT Plugins with Supabase Edge Runtime - YouTube

Supabase

54.4K subscribers

[Building ChatGPT Plugins with Supabase Edge Runtime](https://www.youtube.com/watch?v=4pa-eEXQHJQ)

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

[Watch on YouTube](https://www.youtube.com/watch?v=4pa-eEXQHJQ "Watch on YouTube")

## Serving the manifest file [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#serving-the-manifest-file)

The `ai-plugin.json` [manifest file](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest) is required for ChatGPT to identify our plugin, know what kind of authentication mechanism is used, understand where to find the OpenAPI definition, and some other details about our plugin. You can find the full list of supported parameters in the [OpenAI docs](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest).

Supabase Edge Runtime does currently not support hosting/serving of static files, however, we can import JSON files in our function and serve them as a JSON response. As this needs to be at the root of our domain, we add this to our [main function handler](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/functions/main/index.ts#L69-L74):

`
// functions/main/index.ts
import aiPlugins from './ai-plugins.json' with { type: 'json' }
// [...]
// Serve /.well-known/ai-plugin.json
if (service_name === '.well-known') {
return new Response(JSON.stringify(aiPlugins), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
})
}
`

Now, when running Edge Runtime locally via Docker, our plugin manifest will be available at [http://localhost:8000/.well-known/ai-plugin.json](http://localhost:8000/.well-known/ai-plugin.json)

## Generating the OpenAPI definition with swagger-jsdoc [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#generating-the-openapi-definition-with-swagger-jsdoc)

The [OpenAPI definition](https://platform.openai.com/docs/plugins/getting-started/openapi-definition) is required for ChatGPT to know how to underact with our API. Only endpoints included in there will be exposed to ChatGPT, which allows you to selectively make our endpoints available, or add specific endpoints for ChatGPT.

The OpenAPI definition can be either in YAML or JSON format. We’ll be using JSON and the same approach as above to serve it. Writing an OpenAPI definition is not something we will want to do by hand, luckily there is an open source tool called [swagger-jsdoc](https://github.com/Surnet/swagger-jsdoc) which we can use to annotate our endpoints with JSDoc comments and generate the OpenAPI definition with a [little script](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/scripts/generate-openapi-spec.ts).

``
// /scripts/generate-openapi-spec.ts
import swaggerJsdoc from 'npm:swagger-jsdoc@6.2.8'
const options = {
definition: {
    openapi: '3.0.1',
    info: {
      title: 'TODO Plugin',
      description: `A plugin that allows the user to create and manage a TODO list using ChatGPT. If you do not know the user's username, ask them first before making queries to the plugin. Otherwise, use the username "global".`,
      version: '1.0.0',
    },
    servers: [{ url: 'http://localhost:8000' }],
},
apis: ['./functions/chatgpt-plugin/index.ts'], // files containing annotations as above
}
const openapiSpecification = swaggerJsdoc(options)
const openapiString = JSON.stringify(openapiSpecification, null, 2)
const encoder = new TextEncoder()
const data = encoder.encode(openapiString)
await Deno.writeFile('./functions/chatgpt-plugin/openapi.json', data)
console.log(openapiString)
``

Since this script is run outside of the function execution, e.g. as a GitHub Action, we can use [npm specifiers](https://deno.com/manual/node/npm_specifiers) to import `swagger-jsdoc`.

Next, we create our `/functions/chatgpt-plugin/index.ts` [file](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/functions/chatgpt-plugin/index.ts) where we use the [Deno oak router](https://deno.land/x/oak) to build our API and annotate it with JSDOC comments.

``
// /functions/chatgpt-plugin/index.ts
import { Application, Router } from 'https://deno.land/x/oak@v11.1.0/mod.ts'
import openapi from './openapi.json' with { type: 'json' }
console.log('Hello from `chatgpt-plugin` Function!')
const _TODOS: { [key: string]: Array<string> } = {
user: ['Build your own ChatGPT Plugin!'],
}
/**
* @openapi
* components:
*   schemas:
*     getTodosResponse:
*       type: object
*       properties:
*         todos:
*           type: array
*           items:
*             type: string
*           description: The list of todos.
*/
const router = new Router()
router
.get('/chatgpt-plugin', (ctx) => {
    ctx.response.body = 'Building ChatGPT plugins with Deno!'
})
/**
* @openapi
* /chatgpt-plugin/todos/{username}:
*   get:
*     operationId: getTodos
*     summary: Get the list of todos
*     parameters:
*     - in: path
*       name: username
*       schema:
*         type: string
*       required: true
*       description: The name of the user.
*     responses:
*       200:
*         description: OK
*         content:
*           application/json:
*             schema:
*               $ref: '#/components/schemas/getTodosResponse'
*/
.get('/chatgpt-plugin/todos/:username', (ctx) => {
    const username = ctx.params.username.toLowerCase()
    ctx.response.body = _TODOS[username] ?? []
})
.get('/chatgpt-plugin/openapi.json', (ctx) => {
    ctx.response.body = JSON.stringify(openapi)
    ctx.response.headers.set('Content-Type', 'application/json')
})
const app = new Application()
app.use(router.routes())
app.use(router.allowedMethods())
await app.listen({ port: 8000 })
``

With our JSDoc annotation in place, we can now run the generation script in the terminal:

`
deno run --allow-read --allow-write scripts/generate-openapi-spec.ts
`

## Adding the CORS headers [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#adding-the-cors-headers)

Lastly, we need to add some CORS headers to make the browser happy. We define them in a `/functions/_shared/cors.ts` [file](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/functions/_shared/cors.ts) so we can easily reuse them across our `main` and `chatgpt-plugins` function.

`
// /functions/_shared/cors.ts
export const corsHeaders = {
'Access-Control-Allow-Origin': 'https://chat.openai.com',
'Access-Control-Allow-Credentials': 'true',
'Access-Control-Allow-Private-Network': 'true',
'Access-Control-Allow-Headers': '*',
}
`

Now we can easily add them to all our `chatgpt-plugin` routes a middleware for our oak application.

`
// /functions/chatgpt-plugin/index.ts
import { Application, Router } from 'https://deno.land/x/oak@v11.1.0/mod.ts'
import { corsHeaders } from '../_shared/cors.ts'
// [...]
const app = new Application()
// ChatGPT specific CORS headers
app.use(async (ctx, next) => {
await next()
let key: keyof typeof corsHeaders
for (key in corsHeaders) {
    ctx.response.headers.set(key, corsHeaders[key])
}
})
app.use(router.routes())
app.use(router.allowedMethods())
await app.listen({ port: 8000 })
`

## Running locally with Docker [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#running-locally-with-docker)

Now that we’ve got all the pieces in place, let’s spin up Edge Runtime locally and test things out. For this, we need a [Dockerfile](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/Dockerfile) and for convenience, we can add a [docker-compose file](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/docker-compose.yml) also.

`
// Dockerfile
FROM ghcr.io/supabase/edge-runtime:v1.2.18
COPY ./functions /home/deno/functions
CMD [ "start", "--main-service", "/home/deno/functions/main" ]
`

This will pull down Edge Runtime v1.2.18 (you can check the l [atest release here](https://github.com/supabase/edge-runtime/releases)) and start up the main service (our `/functions/main/index.ts` function).

`
// docker-compose.yml
version: "3.9"
services:
web:
    build: .
    volumes:
      - type: bind
        source: ./functions
        target: /home/deno/functions
    ports:
      - "8000:9000"
`

Edge Runtime will serve requests on port `9000`, so we’re creating a mapping from `[localhost:8000](http://localhost:8000)` where we want to serve our requests locally (of course you can adapt this to your needs) to port `9000` of our Docker container.

Furthermore, we’re using [bind mounts](https://docs.docker.com/storage/bind-mounts/) to mount our functions directory into the container. This allows us to make modifications to our functions without needing to rebuild the container after, making for a great local developer experience.

That’s it, now we can build and spin up our container from the terminal:

`
docker compose up --build
`

Go ahead and try it out by visiting:

- [http://localhost:8000/chatgpt-plugin](http://localhost:8000/chatgpt-plugin)
- [http://localhost:8000/.well-known/ai-plugin.json](http://localhost:8000/.well-known/ai-plugin.json)
- [http://localhost:8000/chatgpt-plugin/openapi.json](http://localhost:8000/chatgpt-plugin/openapi.json)
- [http://localhost:8000/chatgpt-plugin/todos/user](http://localhost:8000/chatgpt-plugin/todos/user)

## Installing and testing the plugin locally [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#installing-and-testing-the-plugin-locally)

You can conveniently test your plugin while running it on [localhost](http://localhost/) using the [ChatGPT UI](https://chat.openai.com/):

1. Select the plugin model from the top drop down, then select “Plugins”, “Plugin Store”, and finally “Develop your own plugin”.
2. Enter `localhost:8000` and click "Find manifest file".
3. Confirm with “Install [localhost](http://localhost/) plugin”.

That’s it, now go ahead and ask some questions, e.g. you can start with “Do I have any todos?”

![ChatGPT Plugin demo on localhost](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-15-chatgpt-plugin-temnplate-deno%2Fchatgpt_plugin_demo_localhost.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

There you are, now go ahead and build your own plugin as it says on your todo list ;)

## Deploying to Fly.io [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#deploying-to-flyio)

Once you’re happy with the functionality of your plugin, go ahead and deploy it to [Fly.io](http://fly.io/). After installing the [flyctl cli](https://fly.io/docs/hands-on/install-flyctl/), it only takes a couple of steps:

- Change `http://localhost:8000` to your Fly domain in the `/main/ai-plugins.json` file
- Open `fly.toml` and update the app name and optionally the region etc.
- In your terminal, run `fly apps create` and specify the app name you just set in your `fly.toml` file.
- Finally, run `fly deploy`.

There you go, now you’re ready to [release your plugin to the world](https://platform.openai.com/docs/plugins/production/faq) \\o/

## Conclusion [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#conclusion)

ChatGPT is a powerful new interface and its usage is growing rapidly. With ChatGPT Plugins you can allow your users to access your service directly from ChatGPT, using cutting edge technologies like TypeScript and Deno.

In a next step you can add authentication to your plugin, let us know on [Twitter](https://twitter.com/Supabase) if you’d be interested in a tutorial for that. We can’t wait to see what you will build!

## More AI resources [\#](https://supabase.com/blog/building-chatgpt-plugins-template\#more-ai-resources)

- [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
- [pgvector v0.5.0: Faster semantic search with HNSW indexes](https://supabase.com/blog/pgvector-v0-5-0-hnsw)
- [OpenAI ChatGPT Plugin docs](https://platform.openai.com/docs/plugins/introduction)
- [Docs pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&t=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)

[Last post\\
\\
**ChatGPT plugins now support Postgres & Supabase** \\
\\
25 May 2023](https://supabase.com/blog/chatgpt-plugins-support-postgres)

[Next post\\
\\
**Flutter Hackathon** \\
\\
12 May 2023](https://supabase.com/blog/flutter-hackathon)

[AI](https://supabase.com/blog/tags/AI) [tutorial](https://supabase.com/blog/tags/tutorial) [functions](https://supabase.com/blog/tags/functions)

On this page

- [Serving the manifest file](https://supabase.com/blog/building-chatgpt-plugins-template#serving-the-manifest-file)
- [Generating the OpenAPI definition with swagger-jsdoc](https://supabase.com/blog/building-chatgpt-plugins-template#generating-the-openapi-definition-with-swagger-jsdoc)
- [Adding the CORS headers](https://supabase.com/blog/building-chatgpt-plugins-template#adding-the-cors-headers)
- [Running locally with Docker](https://supabase.com/blog/building-chatgpt-plugins-template#running-locally-with-docker)
- [Installing and testing the plugin locally](https://supabase.com/blog/building-chatgpt-plugins-template#installing-and-testing-the-plugin-locally)
- [Deploying to Fly.io](https://supabase.com/blog/building-chatgpt-plugins-template#deploying-to-flyio)
- [Conclusion](https://supabase.com/blog/building-chatgpt-plugins-template#conclusion)
- [More AI resources](https://supabase.com/blog/building-chatgpt-plugins-template#more-ai-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&t=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)