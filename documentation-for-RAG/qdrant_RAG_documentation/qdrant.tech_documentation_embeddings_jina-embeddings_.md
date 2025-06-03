---
url: "https://qdrant.tech/documentation/embeddings/jina-embeddings/"
title: "Jina Embeddings - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Jina Embeddings

# [Anchor](https://qdrant.tech/documentation/embeddings/jina-embeddings/\#jina-embeddings) Jina Embeddings

Qdrant is compatible with [Jina AI](https://jina.ai/) embeddings. You can get a free trial key from [Jina Embeddings](https://jina.ai/embeddings/) to get embeddings.

Qdrant users can receive a 10% discount on Jina AI APIs by using the code **QDRANT**.

## [Anchor](https://qdrant.tech/documentation/embeddings/jina-embeddings/\#technical-summary) Technical Summary

| Model | Dimension | Language | MRL (matryoshka) | Context |
| --- | --- | --- | --- | --- |
| **jina-clip-v2** | **1024** | **Multilingual (100+, focus on 30)** | **Yes** | **Text/Image** |
| jina-embeddings-v3 | 1024 | Multilingual (89 languages) | Yes | 8192 |
| jina-embeddings-v2-base-en | 768 | English | No | 8192 |
| jina-embeddings-v2-base-de | 768 | German & English | No | 8192 |
| jina-embeddings-v2-base-es | 768 | Spanish & English | No | 8192 |
| jina-embeddings-v2-base-zh | 768 | Chinese & English | No | 8192 |

> Jina recommends using `jina-embeddings-v3` for text-only tasks and `jina-clip-v2` for multimodal tasks or when enhanced visual retrieval is required.

On top of the backbone, `jina-embeddings-v3` has been trained with 5 task-specific adapters for different embedding uses. Include `task` in your request to optimize your downstream application:

- **retrieval.query**: Used to encode user queries or questions in retrieval tasks.
- **retrieval.passage**: Used to encode large documents in retrieval tasks at indexing time.
- **classification**: Used to encode text for text classification tasks.
- **text-matching**: Used to encode text for similarity matching, such as measuring similarity between two sentences.
- **separation**: Used for clustering or reranking tasks.

`jina-embeddings-v3` and `jina-clip-v2` support **Matryoshka Representation Learning**, allowing users to control the embedding dimension with minimal performance loss.

Include `dimensions` in your request to select the desired dimension.

By default, **dimensions** is set to 1024, and a number between 256 and 1024 is recommended.

You can reference the table below for hints on dimension vs. performance:

| Dimension | 32 | 64 | 128 | 256 | 512 | 768 | 1024 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Average Retrieval Performance (nDCG@10) | 52.54 | 58.54 | 61.64 | 62.72 | 63.16 | 63.3 | 63.35 |

`jina-embeddings-v3` supports [Late Chunking](https://jina.ai/news/late-chunking-in-long-context-embedding-models/), the technique to leverage the model’s long-context capabilities for generating contextual chunk embeddings. Include `late_chunking=True` in your request to enable contextual chunked representation. When set to true, Jina AI API will concatenate all sentences in the input field and feed them as a single string to the model. Internally, the model embeds this long concatenated string and then performs late chunking, returning a list of embeddings that matches the size of the input list.

## [Anchor](https://qdrant.tech/documentation/embeddings/jina-embeddings/\#example) Example

### [Anchor](https://qdrant.tech/documentation/embeddings/jina-embeddings/\#jina-embeddings-v3) Jina Embeddings v3

The code below demonstrates how to use `jina-embeddings-v3` with Qdrant:

```python
import requests

import qdrant_client
from qdrant_client.models import Distance, VectorParams, Batch

# Provide Jina API key and choose one of the available models.
JINA_API_KEY = "jina_xxxxxxxxxxx"
MODEL = "jina-embeddings-v3"
DIMENSIONS = 1024 # Or choose your desired output vector dimensionality.
TASK = 'retrieval.passage' # For indexing, or set to retrieval.query for querying

# Get embeddings from the API
url = "https://api.jina.ai/v1/embeddings"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {JINA_API_KEY}",
}

data = {
    "input": ["Your text string goes here", "You can send multiple texts"],
    "model": MODEL,
    "dimensions": DIMENSIONS,
    "task": TASK,
    "late_chunking": True,
}

response = requests.post(url, headers=headers, json=data)
embeddings = [d["embedding"] for d in response.json()["data"]]

# Index the embeddings into Qdrant
client = qdrant_client.QdrantClient(":memory:")
client.create_collection(
    collection_name="MyCollection",
    vectors_config=VectorParams(size= DIMENSIONS, distance=Distance.DOT),
)

qdrant_client.upsert(
    collection_name="MyCollection",
    points=Batch(
        ids=list(range(len(embeddings))),
        vectors=embeddings,
    ),
)

```

### [Anchor](https://qdrant.tech/documentation/embeddings/jina-embeddings/\#jina-clip-v2) Jina CLIP v2

The code below demonstrates how to use `jina-clip-v2` with Qdrant:

```python
import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Provide your Jina API key and choose the model.
JINA_API_KEY = "jina_xxxxxxxxxxx"
MODEL = "jina-clip-v2"
DIMENSIONS = 1024  # Set the desired output vector dimensionality.

# Define the inputs
text_input = "A blue cat"
image_url = "https://i.pinimg.com/600x315/21/48/7e/21487e8e0970dd366dafaed6ab25d8d8.jpg"

# Get embeddings from the Jina API
url = "https://api.jina.ai/v1/embeddings"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {JINA_API_KEY}",
}
data = {
    "input": [\
        {"text": text_input},\
        {"image": image_url},\
    ],
    "model": MODEL,
    "dimensions": DIMENSIONS,
}

response = requests.post(url, headers=headers, json=data)
response_data = response.json()["data"]

# The model doesn't differentiate between images and text, so we extract output based on the input order.
text_embedding = response_data[0]["embedding"]
image_embedding = response_data[1]["embedding"]

# Initialize Qdrant client
client = QdrantClient(url="http://localhost:6333/")

# Create a collection with named vectors
collection_name = "MyCollection"
client.recreate_collection(
    collection_name=collection_name,
    vectors_config={
        "text_vector": VectorParams(size=DIMENSIONS, distance=Distance.DOT),
        "image_vector": VectorParams(size=DIMENSIONS, distance=Distance.DOT),
    },
)

client.upsert(
    collection_name=collection_name,
    points=[\
        PointStruct(\
            id=0,\
            vector={\
                "text_vector": text_embedding,\
                "image_vector": image_embedding,\
            }\
        )\
    ],
)

# Now let's query the collection
search_query = "A purple cat"

# Get the embedding for the search query from the Jina API
url = "https://api.jina.ai/v1/embeddings"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {JINA_API_KEY}",
}
data = {
    "input": [{"text": search_query}],
    "model": MODEL,
    "dimensions": DIMENSIONS,
    # "task": "retrieval.query" # Uncomment this line for text-to-text retrieval tasks
}

response = requests.post(url, headers=headers, json=data)
query_embedding = response.json()["data"][0]["embedding"]

search_results = client.query_points(
    collection_name=collection_name,
    query=query_embedding,
    using="image_vector",
    limit=5
).points

for result in search_results:
    print(f"ID: {result.id}, Score: {result.score}")

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/jina-embeddings.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/jina-embeddings.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574437437&cv=11&fst=1748574437437&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fjina-embeddings%2F&hn=www.googleadservices.com&frm=0&tiba=Jina%20Embeddings%20-%20Qdrant&npa=0&pscdl=noapi&auid=1434405672.1748574437&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574437392&cv=11&fst=1748574437392&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308614&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fjina-embeddings%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Jina%20Embeddings%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1434405672.1748574437&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c3674ea9-8242-47cb-b5a9-a675da225f4f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b34ddb4c-2d3b-497a-8d4a-6c79345cbb35&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fjina-embeddings%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c3674ea9-8242-47cb-b5a9-a675da225f4f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b34ddb4c-2d3b-497a-8d4a-6c79345cbb35&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fjina-embeddings%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574438591&cv=11&fst=1748574438591&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fjina-embeddings%2F&hn=www.googleadservices.com&frm=0&tiba=Jina%20Embeddings%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1434405672.1748574437&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)