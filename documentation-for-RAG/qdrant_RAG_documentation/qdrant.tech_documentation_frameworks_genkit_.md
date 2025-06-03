---
url: "https://qdrant.tech/documentation/frameworks/genkit/"
title: "Firebase Genkit - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Firebase Genkit

# [Anchor](https://qdrant.tech/documentation/frameworks/genkit/\#firebase-genkit) Firebase Genkit

[Genkit](https://firebase.google.com/products/genkit) is a framework to build, deploy, and monitor production-ready AI-powered apps.

You can build apps that generate custom content, use semantic search, handle unstructured inputs, answer questions with your business data, autonomously make decisions, orchestrate tool calls, and more.

You can use Qdrant for indexing/semantic retrieval of data in your Genkit applications via the [Qdrant-Genkit plugin](https://github.com/qdrant/qdrant-genkit).

Genkit currently supports server-side development in JavaScript/TypeScript (Node.js) with Go support in active development.

## [Anchor](https://qdrant.tech/documentation/frameworks/genkit/\#installation) Installation

```bash
npm i genkitx-qdrant

```

## [Anchor](https://qdrant.tech/documentation/frameworks/genkit/\#configuration) Configuration

To use this plugin, specify it when you call `configureGenkit()`:

```js
import { qdrant } from 'genkitx-qdrant';
import { textEmbeddingGecko } from '@genkit-ai/vertexai';

export default configureGenkit({
  plugins: [\
    qdrant([\
      {\
        clientParams: {\
          host: 'localhost',\
          port: 6333,\
        },\
        collectionName: 'some-collection',\
        embedder: textEmbeddingGecko,\
      },\
    ]),\
  ],
  // ...
});

```

You’ll need to specify a collection name, the embedding model you want to use and the Qdrant client parameters. In
addition, there are a few optional parameters:

- `embedderOptions`: Additional options to pass options to the embedder:



```js
embedderOptions: { taskType: 'RETRIEVAL_DOCUMENT' },

```

- `contentPayloadKey`: Name of the payload filed with the document content. Defaults to “content”.



```js
contentPayloadKey: 'content';

```

- `metadataPayloadKey`: Name of the payload filed with the document metadata. Defaults to “metadata”.



```js
metadataPayloadKey: 'metadata';

```

- `collectionCreateOptions`: [Additional options](https://qdrant.tech/documentation/concepts/collections/#create-a-collection/) when creating the Qdrant collection.


## [Anchor](https://qdrant.tech/documentation/frameworks/genkit/\#usage) Usage

Import retriever and indexer references like so:

```js
import { qdrantIndexerRef, qdrantRetrieverRef } from 'genkitx-qdrant';
import { Document, index, retrieve } from '@genkit-ai/ai/retriever';

```

Then, pass the references to `retrieve()` and `index()`:

jsjs

```js
// To specify an indexer:
export const qdrantIndexer = qdrantIndexerRef({
  collectionName: 'some-collection',
  displayName: 'Some Collection indexer',
});

await index({ indexer: qdrantIndexer, documents });

```

```js
// To specify a retriever:
export const qdrantRetriever = qdrantRetrieverRef({
  collectionName: 'some-collection',
  displayName: 'Some Collection Retriever',
});

let docs = await retrieve({ retriever: qdrantRetriever, query });

```

You can refer to [Retrieval-augmented generation](https://firebase.google.com/docs/genkit/rag) for a general
discussion on indexers and retrievers.

## [Anchor](https://qdrant.tech/documentation/frameworks/genkit/\#further-reading) Further Reading

- [Introduction to Genkit](https://firebase.google.com/docs/genkit)
- [Genkit Documentation](https://firebase.google.com/docs/genkit/get-started)
- [Source Code](https://github.com/qdrant/qdrant-genkit)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/genkit.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/genkit.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)

## Privacy Preference Center

Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.


[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)

Allow All

### Manage Consent Preferences

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b452a52a-f5b1-459d-8fc4-9b8e84204154&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=761e2b18-c8c2-4bef-8337-2016f073659d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fgenkit%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b452a52a-f5b1-459d-8fc4-9b8e84204154&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=761e2b18-c8c2-4bef-8337-2016f073659d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fgenkit%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573643015&cv=11&fst=1748573643015&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fgenkit%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Firebase%20Genkit%20-%20Qdrant&npa=0&pscdl=noapi&auid=411202122.1748573642&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573643002&cv=11&fst=1748573643002&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fgenkit%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Firebase%20Genkit%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=411202122.1748573642&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573643098&cv=11&fst=1748573643098&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fgenkit%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Firebase%20Genkit%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=411202122.1748573642&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)