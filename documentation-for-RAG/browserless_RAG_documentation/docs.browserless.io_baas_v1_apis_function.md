---
url: "https://docs.browserless.io/baas/v1/apis/function"
title: "/function API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/function#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/function) or [BrowserQL](https://docs.browserless.io/browserql/start).

A quick way to run commands with Browserless is via our `/function` API. You can use Python, NodeJS or any other language that supports making HTTP requests, so you don't need to install any libraries on your end.

The `/function` endpoint allows for `POST` ing of custom `code` and `context` to run them with. The `code` function, which only supports puppeteer code, gets called with an object containing several properties: a `page` property, [which is a puppeteer page object](https://pptr.dev/api/puppeteer.page), and `context` which is the context you provide in the JSON body.

Functions should return an object with two properties: `data` and `type`. `data` can be whatever you'd like ( `Buffer`, `JSON`, or plain `text`) and `type` is a string describing the content-type of `data`. Browserless reads both of these from your functions return value and resolves the request appropriately.

Check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_function).

> If you want to see more examples, checkout how other [REST API's are handled in our GitHub project](https://github.com/browserless/browserless/tree/v1/functions).

## Basic Usage [​](https://docs.browserless.io/baas/v1/apis/function\#basic-usage "Direct link to Basic Usage")

**JS code**

```codeBlockLines_p187
// Read the `url` from context, goto the page and return the results
module.exports = async ({ page, context }) => {
  const { url } = context;
  await page.goto(url);

  const data = await page.content();

  return {
    data,
    // Make sure to match the appropriate content here
    // You'll likely want 'application/json'
    type: 'application/html',
  };
};

```

**context**

```codeBlockLines_p187
{
  "url": "https://example.com"
}

```

Since you can't have multi-line strings in JSON we've minified our above code with the [online babel repl](https://babeljs.io/repl) and use it in the below `curl` call.

**cURL request**

```codeBlockLines_p187
curl -X POST \
  'https://chrome.browserless.io/function?TOKEN=YOUR-API-TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
  "code": "module.exports=async({page:a,context:b})=>{const{url:c}=b;await a.goto(c);const d=await a.content();return{data:d,type:\"application/html\"}};",
  "context": {
    "url": "https://example.com/"
  }
}'

```

## Detached functions [​](https://docs.browserless.io/baas/v1/apis/function\#detached-functions "Direct link to Detached functions")

Functions that are "detached" resolve _immediately_ with a JSON payload exposing the job's ID. These are useful if you don't want to hold onto the connection with browserless while it's running, but are relying on the side-effects of having a browserless run the function. You can also call external services with any results (like webhooks or your own API's). Since it's harder to track detached functions, browserless will call them with another parameter if `id` which is the same `id` that they immediately resolve with.

In order to detach a function you'll need to pass in a third parameter of `detached: true` in the JSON POST body.

> You can currently require 'url', 'util', 'path', 'querystring', 'lodash', 'node-fetch', and 'request' in your functions. Please contact us for adding a module

**code**

```codeBlockLines_p187
const fetch = require('node-fetch');

// ID here is dynamic, and matches up with the immediate response from
// browserless but allows you to track it in third-party systems
module.exports = async ({ page, context, id }) => {
  const { url } = context;
  await page.goto(url);

  const data = await page.content();

  // POST the content to a third-party service
  return fetch('https://my-third-party-service.com/content', {
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      pageContent: data,
      sessionId: id,
    }),
    method: 'POST',
  });
};

```

**context**

```codeBlockLines_p187
{
  "url": "https://example.com"
}

```

To force functions to operate in a detached way, simply add a `detached: true` to the POSTed body.

**cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/function?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
    "code": "const fetch=require('\''node-fetch'\'');module.exports=async({page:a,context:b,id:c})=>{const{url:d}=b;await a.goto(d);const e=await a.content();return fetch('\''https://my-third-party-service.com/content'\'',{headers:{'\''Content-Type'\'':'\''application/json'\''},body:JSON.stringify({pageContent:e,sessionId:c}),method:'\''POST'\''})};",
    "context": {
        "url": "https://example.com/"
    },
    "detached": true
}'

```

- [Basic Usage](https://docs.browserless.io/baas/v1/apis/function#basic-usage)
- [Detached functions](https://docs.browserless.io/baas/v1/apis/function#detached-functions)