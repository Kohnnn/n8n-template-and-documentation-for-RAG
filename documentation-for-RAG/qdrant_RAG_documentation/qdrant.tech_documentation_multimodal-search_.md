---
url: "https://qdrant.tech/documentation/multimodal-search/"
title: "Multilingual & Multimodal RAG with LlamaIndex - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- Multilingual & Multimodal RAG with LlamaIndex

# [Anchor](https://qdrant.tech/documentation/multimodal-search/\#multilingual--multimodal-search-with-llamaindex) Multilingual & Multimodal Search with LlamaIndex

![Snow prints](https://qdrant.tech/documentation/examples/multimodal-search/image-1.png)

| Time: 15 min | Level: Beginner | Output: [GitHub](https://github.com/qdrant/examples/blob/master/multimodal-search/Multimodal_Search_with_LlamaIndex.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/qdrant/examples/blob/master/multimodal-search/Multimodal_Search_with_LlamaIndex.ipynb) |
| --- | --- | --- | --- |

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#overview) Overview

We often understand and share information more effectively when combining different types of data. For example, the taste of comfort food can trigger childhood memories. We might describe a song with just “pam pam clap” sounds. Instead of writing paragraphs. Sometimes, we may use emojis and stickers to express how we feel or to share complex ideas.

Modalities of data such as **text**, **images**, **video** and **audio** in various combinations form valuable use cases for Semantic Search applications.

Vector databases, being **modality-agnostic**, are perfect for building these applications.

In this simple tutorial, we are working with two simple modalities: **image** and **text** data. However, you can create a Semantic Search application with any combination of modalities if you choose the right embedding model to bridge the **semantic gap**.

> The **semantic gap** refers to the difference between low-level features (aka brightness) and high-level concepts (aka cuteness).

For example, the [vdr-2b-multi-v1 model](https://huggingface.co/llamaindex/vdr-2b-multi-v1) from LlamaIndex is designed for multilingual embedding, particularly effective for visual document retrieval across multiple languages and domains. It allows for searching and querying visually rich multilingual documents without the need for OCR or other data extraction pipelines.

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#setup) Setup

First, install the required libraries `qdrant-client` and `llama-index-embeddings-huggingface`.

```bash
pip install qdrant-client llama-index-embeddings-huggingface

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#dataset) Dataset

To make the demonstration simple, we created a tiny dataset of images and their captions for you.

Images can be downloaded from [here](https://github.com/qdrant/examples/tree/master/multimodal-search/images). It’s **important** to place them in the same folder as your code/notebook, in the folder named `images`.

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#vectorize-data) Vectorize data

`LlamaIndex`’s `vdr-2b-multi-v1` model supports cross-lingual retrieval, allowing for effective searches across languages and domains. It encodes document page screenshots into dense single-vector representations, eliminating the need for OCR and other complex data extraction processes.

Let’s embed the images and their captions in the **shared embedding space**.

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

model = HuggingFaceEmbedding(
    model_name="llamaindex/vdr-2b-multi-v1",
    device="cpu",  # "mps" for mac, "cuda" for nvidia GPUs
    trust_remote_code=True,
)

documents = [\
    {"caption": "An image about plane emergency safety.", "image": "images/image-1.png"},\
    {"caption": "An image about airplane components.", "image": "images/image-2.png"},\
    {"caption": "An image about COVID safety restrictions.", "image": "images/image-3.png"},\
    {"caption": "An confidential image about UFO sightings.", "image": "images/image-4.png"},\
    {"caption": "An image about unusual footprints on Aralar 2011.", "image": "images/image-5.png"},\
]

text_embeddings = model.get_text_embedding_batch([doc["caption"] for doc in documents])
image_embeddings = model.get_image_embedding_batch([doc["image"] for doc in documents])

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#upload-data-to-qdrant) Upload data to Qdrant

1. **Create a client object for Qdrant**.

```python
from qdrant_client import QdrantClient, models

# docker run -p 6333:6333 qdrant/qdrant
client = QdrantClient(url="http://localhost:6333/")

```

2. **Create a new collection for the images with captions**.

```python
COLLECTION_NAME = "llama-multi"

if not client.collection_exists(COLLECTION_NAME):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={
            "image": models.VectorParams(size=len(image_embeddings[0]), distance=models.Distance.COSINE),
            "text": models.VectorParams(size=len(text_embeddings[0]), distance=models.Distance.COSINE),
        }
    )

```

3. **Upload our images with captions to the Collection**.

```python
client.upload_points(
    collection_name=COLLECTION_NAME,
    points=[\
        models.PointStruct(\
            id=idx,\
            vector={\
                "text": text_embeddings[idx],\
                "image": image_embeddings[idx],\
            },\
            payload=doc\
        )\
        for idx, doc in enumerate(documents)\
    ]
)

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#search) Search

### [Anchor](https://qdrant.tech/documentation/multimodal-search/\#text-to-image) Text-to-Image

Let’s see what image we will get to the query “ _Adventures on snow hills_”.

```python
from PIL import Image

find_image = model.get_query_embedding("Adventures on snow hills")

Image.open(client.query_points(
    collection_name=COLLECTION_NAME,
    query=find_image,
    using="image",
    with_payload=["image"],
    limit=1
).points[0].payload['image'])

```

Let’s also run the same query in Italian and compare the results.

### [Anchor](https://qdrant.tech/documentation/multimodal-search/\#multilingual-search) Multilingual Search

Now, let’s do a multilingual search using an Italian query:

```python
Image.open(client.query_points(
    collection_name=COLLECTION_NAME,
    query=model.get_query_embedding("Avventure sulle colline innevate"),
    using="image",
    with_payload=["image"],
    limit=1
).points[0].payload['image'])

```

**Response:**

![Snow prints](https://qdrant.tech/documentation/advanced-tutorials/snow-prints.png)

### [Anchor](https://qdrant.tech/documentation/multimodal-search/\#image-to-text) Image-to-Text

Now, let’s do a reverse search with the following image:

![Airplane](https://qdrant.tech/documentation/advanced-tutorials/airplane.png)

```python
client.query_points(
    collection_name=COLLECTION_NAME,
    query=model.get_image_embedding("images/image-2.png"),
    # Now we are searching only among text vectors with our image query
    using="text",
    with_payload=["caption"],
    limit=1
).points[0].payload['caption']

```

**Response:**

```text
'An image about plane emergency safety.'

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#next-steps) Next steps

Use cases of even just Image & Text Multimodal Search are countless: E-Commerce, Media Management, Content Recommendation, Emotion Recognition Systems, Biomedical Image Retrieval, Spoken Sign Language Transcription, etc.

Imagine a scenario: a user wants to find a product similar to a picture they have, but they also have specific textual requirements, like “ _in beige colour_”. You can search using just texts or images and combine their embeddings in a **late fusion manner** (summing and weighting might work surprisingly well).

Moreover, using [Discovery Search](https://qdrant.tech/articles/discovery-search/) with both modalities, you can provide users with information that is impossible to retrieve unimodally!

Join our [Discord community](https://qdrant.to/discord), where we talk about vector search and similarity learning, experiment, and have fun!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/multimodal-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/multimodal-search.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575507510&cv=11&fst=1748575507510&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fmultimodal-search%2F&hn=www.googleadservices.com&frm=0&tiba=Multilingual%20%26%20Multimodal%20RAG%20with%20LlamaIndex%20-%20Qdrant&npa=0&pscdl=noapi&auid=96024242.1748575507&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575507467&cv=11&fst=1748575507467&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fmultimodal-search%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Multilingual%20%26%20Multimodal%20RAG%20with%20LlamaIndex%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=96024242.1748575507&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d958ab69-063a-4dca-a1a6-f2fe11735064&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a76fa6a9-e7fc-4360-90fc-07631eb6845b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fmultimodal-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d958ab69-063a-4dca-a1a6-f2fe11735064&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a76fa6a9-e7fc-4360-90fc-07631eb6845b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fmultimodal-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575508554&cv=11&fst=1748575508554&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fmultimodal-search%2F&hn=www.googleadservices.com&frm=0&tiba=Multilingual%20%26%20Multimodal%20RAG%20with%20LlamaIndex%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=96024242.1748575507&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)