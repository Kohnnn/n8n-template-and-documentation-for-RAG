---
url: "https://qdrant.tech/documentation/embeddings/voyage/"
title: "Voyage AI - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Voyage AI

# [Anchor](https://qdrant.tech/documentation/embeddings/voyage/\#voyage-ai) Voyage AI

Qdrant supports working with [Voyage AI](https://voyageai.com/) embeddings. The supported models’ list can be found [here](https://docs.voyageai.com/docs/embeddings).

You can generate an API key from the [Voyage AI dashboard](https://dash.voyageai.com/) to authenticate the requests.

### [Anchor](https://qdrant.tech/documentation/embeddings/voyage/\#setting-up-the-qdrant-and-voyage-clients) Setting up the Qdrant and Voyage clients

pythontypescript

```python
from qdrant_client import QdrantClient
import voyageai

VOYAGE_API_KEY = "<YOUR_VOYAGEAI_API_KEY>"

qclient = QdrantClient(":memory:")
vclient = voyageai.Client(api_key=VOYAGE_API_KEY)

texts = [\
    "Qdrant is the best vector search engine!",\
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",\
]

```

```typescript
import {QdrantClient} from '@qdrant/js-client-rest';

const VOYAGEAI_BASE_URL = "https://api.voyageai.com/v1/embeddings"
const VOYAGEAI_API_KEY = "<YOUR_VOYAGEAI_API_KEY>"

const client = new QdrantClient({ url: 'http://localhost:6333' });

const headers = {
    "Authorization": "Bearer " + VOYAGEAI_API_KEY,
    "Content-Type": "application/json"
}

const texts = [\
    "Qdrant is the best vector search engine!",\
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",\
]

```

The following example shows how to embed documents with the [`voyage-large-2`](https://docs.voyageai.com/docs/embeddings#model-choices) model that generates sentence embeddings of size 1536.

### [Anchor](https://qdrant.tech/documentation/embeddings/voyage/\#embedding-documents) Embedding documents

pythontypescript

```python
response = vclient.embed(texts, model="voyage-large-2", input_type="document")

```

```typescript
let body = {
    "input": texts,
    "model": "voyage-large-2",
    "input_type": "document",
}

let response = await fetch(VOYAGEAI_BASE_URL, {
    method: "POST",
    body: JSON.stringify(body),
    headers
});

let response_body = await response.json();

```

### [Anchor](https://qdrant.tech/documentation/embeddings/voyage/\#converting-the-model-outputs-to-qdrant-points) Converting the model outputs to Qdrant points

pythontypescript

```python
from qdrant_client.models import PointStruct

points = [\
    PointStruct(\
        id=idx,\
        vector=embedding,\
        payload={"text": text},\
    )\
    for idx, (embedding, text) in enumerate(zip(response.embeddings, texts))\
]

```

```typescript
let points = response_body.data.map((data, i) => {
    return {
        id: i,
        vector: data.embedding,
        payload: {
            text: texts[i]
        }
    }
});

```

### [Anchor](https://qdrant.tech/documentation/embeddings/voyage/\#creating-a-collection-to-insert-the-documents) Creating a collection to insert the documents

pythontypescript

```python
from qdrant_client.models import VectorParams, Distance

COLLECTION_NAME = "example_collection"

qclient.create_collection(
    COLLECTION_NAME,
    vectors_config=VectorParams(
        size=1536,
        distance=Distance.COSINE,
    ),
)
qclient.upsert(COLLECTION_NAME, points)

```

```typescript
const COLLECTION_NAME = "example_collection"

await client.createCollection(COLLECTION_NAME, {
    vectors: {
        size: 1536,
        distance: 'Cosine',
    }
});

await client.upsert(COLLECTION_NAME, {
    wait: true,
    points
});

```

### [Anchor](https://qdrant.tech/documentation/embeddings/voyage/\#searching-for-documents-with-qdrant) Searching for documents with Qdrant

Once the documents are added, you can search for the most relevant documents.

pythontypescript

```python
response = vclient.embed(
    ["What is the best to use for vector search scaling?"],
    model="voyage-large-2",
    input_type="query",
)

qclient.search(
    collection_name=COLLECTION_NAME,
    query_vector=response.embeddings[0],
)

```

```typescript
body = {
    "input": ["What is the best to use for vector search scaling?"],
    "model": "voyage-large-2",
    "input_type": "query",
};

response = await fetch(VOYAGEAI_BASE_URL, {
    method: "POST",
    body: JSON.stringify(body),
    headers
});

response_body = await response.json();

await client.search(COLLECTION_NAME, {
    vector: response_body.data[0].embedding,
});

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/voyage.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/voyage.md)
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