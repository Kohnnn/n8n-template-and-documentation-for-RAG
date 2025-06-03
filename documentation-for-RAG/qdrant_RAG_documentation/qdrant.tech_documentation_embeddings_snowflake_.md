---
url: "https://qdrant.tech/documentation/embeddings/snowflake/"
title: "Snowflake Models - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Snowflake Models

# [Anchor](https://qdrant.tech/documentation/embeddings/snowflake/\#snowflake) Snowflake

Qdrant supports working with [Snowflake](https://www.snowflake.com/blog/introducing-snowflake-arctic-embed-snowflakes-state-of-the-art-text-embedding-family-of-models/) text embedding models. You can find all the available models on [HuggingFace](https://huggingface.co/Snowflake).

### [Anchor](https://qdrant.tech/documentation/embeddings/snowflake/\#setting-up-the-qdrant-and-snowflake-models) Setting up the Qdrant and Snowflake models

pythontypescript

```python
from qdrant_client import QdrantClient
from fastembed import TextEmbedding

qclient = QdrantClient(":memory:")
embedding_model = TextEmbedding("snowflake/snowflake-arctic-embed-s")

texts = [\
    "Qdrant is the best vector search engine!",\
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",\
]

```

```typescript
import {QdrantClient} from '@qdrant/js-client-rest';
import { pipeline } from '@xenova/transformers';

const client = new QdrantClient({ url: 'http://localhost:6333' });

const extractor = await pipeline('feature-extraction', 'Snowflake/snowflake-arctic-embed-s');

const texts = [\
    "Qdrant is the best vector search engine!",\
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",\
]

```

The following example shows how to embed documents with the [`snowflake-arctic-embed-s`](https://huggingface.co/Snowflake/snowflake-arctic-embed-s) model that generates sentence embeddings of size 384.

### [Anchor](https://qdrant.tech/documentation/embeddings/snowflake/\#embedding-documents) Embedding documents

pythontypescript

```python
embeddings = embedding_model.embed(texts)

```

```typescript
const embeddings = await extractor(texts, { normalize: true, pooling: 'cls' });

```

### [Anchor](https://qdrant.tech/documentation/embeddings/snowflake/\#converting-the-model-outputs-to-qdrant-points) Converting the model outputs to Qdrant points

pythontypescript

```python
from qdrant_client.models import PointStruct

points = [\
    PointStruct(\
        id=idx,\
        vector=embedding,\
        payload={"text": text},\
    )\
    for idx, (embedding, text) in enumerate(zip(embeddings, texts))\
]

```

```typescript
let points = embeddings.tolist().map((embedding, i) => {
    return {
        id: i,
        vector: embedding,
        payload: {
            text: texts[i]
        }
    }
});

```

### [Anchor](https://qdrant.tech/documentation/embeddings/snowflake/\#creating-a-collection-to-insert-the-documents) Creating a collection to insert the documents

pythontypescript

```python
from qdrant_client.models import VectorParams, Distance

COLLECTION_NAME = "example_collection"

qclient.create_collection(
    COLLECTION_NAME,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE,
    ),
)
qclient.upsert(COLLECTION_NAME, points)

```

```typescript
const COLLECTION_NAME = "example_collection"

await client.createCollection(COLLECTION_NAME, {
    vectors: {
        size: 384,
        distance: 'Cosine',
    }
});

await client.upsert(COLLECTION_NAME, {
    wait: true,
    points
});

```

### [Anchor](https://qdrant.tech/documentation/embeddings/snowflake/\#searching-for-documents-with-qdrant) Searching for documents with Qdrant

Once the documents are added, you can search for the most relevant documents.

pythontypescript

```python
query_embedding = next(embedding_model.query_embed("What is the best to use for vector search scaling?"))

qclient.search(
    collection_name=COLLECTION_NAME,
    query_vector=query_embedding,
)

```

```typescript
const query_embedding = await extractor("What is the best to use for vector search scaling?", {
    normalize: true,
    pooling: 'cls'
});

await client.search(COLLECTION_NAME, {
    vector: query_embedding.tolist()[0],
});

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/snowflake.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/snowflake.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=a5cf6368-cffe-49eb-b8fb-44e06f0d86ca&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=87229aef-6f3c-4b64-bfc2-2b6de3022276&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fsnowflake%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573619635&cv=11&fst=1748573619635&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fsnowflake%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Snowflake%20Models%20-%20Qdrant&npa=0&pscdl=noapi&auid=989529663.1748573619&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573619608&cv=11&fst=1748573619608&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fsnowflake%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Snowflake%20Models%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=989529663.1748573619&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573620146&cv=11&fst=1748573620146&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fsnowflake%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Snowflake%20Models%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=989529663.1748573619&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=a5cf6368-cffe-49eb-b8fb-44e06f0d86ca&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=87229aef-6f3c-4b64-bfc2-2b6de3022276&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fsnowflake%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)