---
url: "https://docs.browserless.io/browserql/writing-bql/advanced-options"
title: "Advanced Options | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/writing-bql/advanced-options#__docusaurus_skipToContent_fallback)

On this page

BrowserQL offers advanced options allows developers to create dynamic, condition-based workflows, capture visual data, and interact programmatically with web pages. These options enhance the flexibility of web automation, making it possible to tackle complex scenarios with ease. Below, you’ll find detailed examples and use cases to help you with these advanced features.

- [Conditional Behaviors](https://docs.browserless.io/browserql/writing-bql/advanced-options#conditional-behaviors)
- [Scraping Structured Data](https://docs.browserless.io/browserql/writing-bql/advanced-options#scraping-structured-data)
- [Taking Screenshots](https://docs.browserless.io/browserql/writing-bql/advanced-options#taking-screenshots)
- [Generating PDFs](https://docs.browserless.io/browserql/writing-bql/advanced-options#generating-pdfs)

## Conditional Behaviors [​](https://docs.browserless.io/browserql/writing-bql/advanced-options\#conditional-behaviors "Direct link to Conditional Behaviors")

You can use `if` or `ifnot` mutations to trigger nested work branches based on specific conditions. A common use case for this is when a browser interaction receives a 403 code, indicating the need to use a verification or captcha-solving mutation.

The example below will only trigger the `verify` mutation when the `goto` returns a 403 code:

```codeBlockLines_p187
mutation ConditionalCase {
  goto(url: "https://www.browserless.io/", waitUntil: domContentLoaded) {
    status
  }
  if(response: {codes: 403}) {
    waitForTimeout(time: 2000) {
      time
    }
    verify(type: cloudflare) {
      solved
    }
  }
}

```

Now, a `ifnot` can be used to treat cases where the code isn't 403. For example, the code below retrieves the page's title when any other code is returned:

```codeBlockLines_p187
mutation ConditionalCase {
  goto(url: "https://www.browserless.io/", waitUntil: domContentLoaded) {
    status
  }
  if(response: {codes: 403}) {
    waitForTimeout(time: 2000) {
      time
    }
    verify(type: cloudflare) {
      solved
    }
  }

  ifnot(response: {codes: 403}) {
    title {
      title
    }
  }
}

```

This example opens up two different work branches, one that will be triggered when a code 403 is received, and a second one to handle when any other code is returned.

## Scraping Structured Data [​](https://docs.browserless.io/browserql/writing-bql/advanced-options\#scraping-structured-data "Direct link to Scraping Structured Data")

Many pages have structure to them where one can infer a data hierarchy. This can simple things like a list of products, their prices, and even reviews. In such cases where you run into these hierarchies we heavily recommend using the `mapSelector` query to "map" over this data and return a well structured response.

This query allows you to functionally "map" over repetitive, hierarchical data in the page and extract data. This query is very powerful in that you can get _any_ kind of data out of the page, including data in attributes, textual data, or even further nested data.

Let's take a look at the Hacker News as an example. This site has posts that are easily retrieved by mapping over the `submission` class on the page. In BrowserQL, this would look like this:

```codeBlockLines_p187
mutation MapHN {
  goto(url: "https://news.ycombinator.com/", waitUntil: domContentLoaded) {
    status
  }

  posts: mapSelector(selector: ".post") {
    itemId: id
  }
}

```

Here, we're using the `post` class as a way to target each post on the page, and then we ask for the "id" attribute of the post. We also are using aliases to further give semantic meaning to these actions as well so it's clear what we're getting in response. When ran this will return a data structure like so:

```codeBlockLines_p187
{
  "data": {
    "goto": {
      "status": 200
    },
    "posts": [\
      {\
        "itemId": "43128253"\
      },\
      {\
        "itemId": "43130732"\
      },\
    ...\
}\
\
```\
\
Taking this a step further, we can now map over each _post_ and get more details like author, rank, and even comment count. Since these each have their own repetitive structure within the page, we can nest a second `mapSelector` call and get that nested data:\
\
```codeBlockLines_p187\
mutation MapHN {\
  goto(url: "https://news.ycombinator.com", waitUntil: networkIdle) {\
    status\
  }\
\
  # Iterate over each submission\
  posts: mapSelector(selector: ".submission") {\
    itemId: id\
\
    # Get the ranking of the submission\
    rank: mapSelector(selector: ".rank", wait: true) {\
      rank: innerText\
    }\
\
    # Get the link of the submission\
    link: mapSelector(selector: ".titleline > a", wait: true) {\
      # You can query for arbitrary tags attributes as well by using the "attribute" mechanism.\
      link: attribute(name: "href") {\
        value\
      }\
    }\
  }\
}\
\
```\
\
When using a nested `mapSelector` this will keep hierarchy intact. This means that each "rank" and "link" in the data will be the items that are nested in each submission.\
\
Finally, since mapping is a functional programming concept, this means that all responses returned are iterable, meaning an array of items even if it is just a single item. In this case, rank and links are a single item in an array.\
\
## Taking Screenshots [​](https://docs.browserless.io/browserql/writing-bql/advanced-options\#taking-screenshots "Direct link to Taking Screenshots")\
\
BrowserQL can be used to take screenshots from any website. With the screenshot mutator, you can generate any image, and BQL will return a base64 encoded string of the new image.\
\
For example, the code below takes a picture of [https://example.com/](https://example.com/), focusing on the middle section using the `clip` argument to define the image's size, and screen position.\
\
- Screenshot\
- With Selector\
- Response\
\
```codeBlockLines_p187\
mutation TakeScreenshot {\
  goto(url: "https://example.com/") {\
    status\
  }\
  screenshot(clip: {width: 720, height: 300, x: 150, y: 65}) {\
    base64\
  }\
}\
\
```\
\
```codeBlockLines_p187\
mutation TakeScreenshot {\
  goto(url: "https://example.com/") {\
    status\
  }\
  screenshot(selector: "div.logo_footer.w-embed") {\
    base64\
  }\
}\
\
```\
\
```codeBlockLines_p187\
{\
  "data": {\
    "goto": {\
      "status": 200\
    },\
    "screenshot": {\
      "base64": "iVBORw0KGgoAAAANSUhEUgAAAtAAAAEsCAIAAABl...AAEA6ggMAAEhHcAAAAOkIDgAAIB3BAQAApCM4AACAdAQHAACQjuAAAADS/QfLjprKnsPc9AAAAABJRU5ErkJggg=="\
    }\
  }\
}\
\
```\
\
Available arguments\
\
Refer to the [Mutation Reference](https://docs.browserless.io/bql-schema/operations/mutations/screenshot) page for full details on the available arguments and response from the screenshot mutation.\
\
Now, with the image's base64, you can use it, as exemplified below, replacing `<PASTE_YOUR_BASE64_HERE>` with your base64 string:\
\
- HTML\
- Save File\
\
```codeBlockLines_p187\
<!DOCTYPE html>\
<html>\
<head>\
    <title>Base64 Image Viewer</title>\
</head>\
<body>\
    <img src="data:image/png;base64,<PASTE_YOUR_BASE64_HERE>" alt="Base64 Image">\
</body>\
</html>\
\
```\
\
```codeBlockLines_p187\
import base64\
\
# Base64 string\
base64_string = "<PASTE_YOUR_BASE64_HERE>"\
\
# Decode and save as a file\
with open("output.png", "wb") as file:\
    file.write(base64.b64decode(base64_string))\
\
```\
\
## Generating PDFs [​](https://docs.browserless.io/browserql/writing-bql/advanced-options\#generating-pdfs "Direct link to Generating PDFs")\
\
Similarly to taking screenshots, there is the `pdf` mutation to generate PDFs. BQL will generate a base64 encoded string from any website.\
\
```codeBlockLines_p187\
mutation GetPDF {\
  goto(url: "https://example.com/") {\
    status\
  }\
  pdf {\
    base64\
  }\
}\
\
```\
\
Available arguments\
\
Refer to the [Mutation Reference](https://docs.browserless.io/bql-schema/operations/mutations/pdf) page for full details on the available arguments and response from the pdf mutation.\
\
With the PDF's base64 string, you can generate the PDF file, or make it downloadable in your own site.\
\
- HTML\
- Save File\
\
```codeBlockLines_p187\
<!DOCTYPE html>\
<html>\
<head>\
    <title>Base64 PDF Viewer</title>\
</head>\
<body>\
    <iframe src="data:application/pdf;base64,<PASTE_YOUR_BASE64_HERE>" width="600" height="400"></iframe>\
    <a href="data:application/pdf;base64,<PASTE_YOUR_BASE64_HERE>" download="document.pdf">Download PDF</a>\
</body>\
</html>\
\
```\
\
```codeBlockLines_p187\
import base64\
\
# Base64 string\
base64_string = "<PASTE_YOUR_BASE64_HERE>"\
\
# Decode and save as a file\
with open("output_document.pdf", "wb") as file:\
    file.write(base64.b64decode(base64_string))\
\
```\
\
- [Conditional Behaviors](https://docs.browserless.io/browserql/writing-bql/advanced-options#conditional-behaviors)\
- [Scraping Structured Data](https://docs.browserless.io/browserql/writing-bql/advanced-options#scraping-structured-data)\
- [Taking Screenshots](https://docs.browserless.io/browserql/writing-bql/advanced-options#taking-screenshots)\
- [Generating PDFs](https://docs.browserless.io/browserql/writing-bql/advanced-options#generating-pdfs)