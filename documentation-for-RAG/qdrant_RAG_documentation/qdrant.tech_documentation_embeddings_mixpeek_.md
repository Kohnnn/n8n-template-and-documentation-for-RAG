---
url: "https://qdrant.tech/documentation/embeddings/mixpeek/"
title: "Mixpeek - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Mixpeek

# [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#mixpeek-video-embeddings) Mixpeek Video Embeddings

Mixpeek’s video processing capabilities allow you to chunk and embed videos, while Qdrant provides efficient storage and retrieval of these embeddings.

## [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#prerequisites) Prerequisites

- Python 3.7+
- Mixpeek API key
- Mixpeek client installed ( `pip install mixpeek`)
- Qdrant client installed ( `pip install qdrant-client`)

## [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#installation) Installation

1. Install the required packages:

```bash
pip install mixpeek qdrant-client

```

2. Set up your Mixpeek API key:

```python
from mixpeek import Mixpeek

mixpeek = Mixpeek('your_api_key_here')

```

3. Initialize the Qdrant client:

```python
from qdrant_client import QdrantClient

client = QdrantClient("localhost", port=6333)

```

## [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#usage) Usage

### [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#1-create-qdrant-collection) 1\. Create Qdrant Collection

Make sure to create a Qdrant collection before inserting vectors. You can create a collection with the appropriate vector size (768 for “vuse-generic-v1” model) using:

```python
client.create_collection(
    collection_name="video_chunks",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)

```

### [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#2-process-and-embed-video) 2\. Process and Embed Video

First, process the video into chunks and embed each chunk:

```python
from mixpeek import Mixpeek
from qdrant_client import QdrantClient, models

mixpeek = Mixpeek('your_api_key_here')
client = QdrantClient("localhost", port=6333)

video_url = "https://mixpeek-public-demo.s3.us-east-2.amazonaws.com/starter/jurassic_park_trailer.mp4"

# Process video chunks
processed_chunks = mixpeek.tools.video.process(
    video_source=video_url,
    chunk_interval=1,  # 1 second intervals
    resolution=[720, 1280]
)

# Embed each chunk and insert into Qdrant
for index, chunk in enumerate(processed_chunks):
    print(f"Processing video chunk: {index}")

    embedding = mixpeek.embed.video(
        model_id="vuse-generic-v1",
        input=chunk['base64_chunk'],
        input_type="base64"
    )['embedding']

    # Insert into Qdrant
    client.upsert(
        collection_name="video_chunks",
        points=[models.PointStruct(\
            id=index,\
            vector=embedding,\
            payload={\
                "start_time": chunk["start_time"],\
                "end_time": chunk["end_time"]\
            }\
        )]
    )

    print(f"  Embedding preview: {embedding[:5] + ['...'] + embedding[-5:]}")

print(f"Processed and inserted {len(processed_chunks)} chunks")

```

### [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#3-search-for-similar-video-chunks) 3\. Search for Similar Video Chunks

To search for similar video chunks, you can use either text or video queries:

#### [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#text-query) Text Query

```python
query_text = "a car chase scene"

# Embed the text query
query_embedding = mixpeek.embed.video(
    model_id="vuse-generic-v1",
    input=query_text,
    input_type="text"
)['embedding']

# Search in Qdrant
search_results = client.query_points(
    collection_name="video_chunks",
    query=query_embedding,
    limit=5
).points

for result in search_results:
    print(f"Chunk ID: {result.id}, Score: {result.score}")
    print(f"Time range: {result.payload['start_time']} - {result.payload['end_time']}")

```

#### [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#video-query) Video Query

```python
query_video_url = "https://mixpeek-public-demo.s3.us-east-2.amazonaws.com/starter/jurassic_bunny.mp4"

# Embed the video query
query_embedding = mixpeek.embed.video(
    model_id="vuse-generic-v1",
    input=query_video_url,
    input_type="url"
)['embedding']

# Search in Qdrant
search_results = client.query_points(
    collection_name="video_chunks",
    query=query_embedding,
    limit=5
).points

for result in search_results:
    print(f"Chunk ID: {result.id}, Score: {result.score}")
    print(f"Time range: {result.payload['start_time']} - {result.payload['end_time']}")

```

## [Anchor](https://qdrant.tech/documentation/embeddings/mixpeek/\#resources) Resources

For more information on Mixpeek Embed, review the official documentation: [https://docs.mixpeek.com/api-documentation/inference/embed](https://docs.mixpeek.com/api-documentation/inference/embed)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/mixpeek.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/mixpeek.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574730205&cv=11&fst=1748574730205&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixpeek%2F&hn=www.googleadservices.com&frm=0&tiba=Mixpeek%20-%20Qdrant&npa=0&pscdl=noapi&auid=21165070.1748574730&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574730189&cv=11&fst=1748574730189&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixpeek%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Mixpeek%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=21165070.1748574730&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0ec97228-1124-4e06-abf5-32ccf3d9a538&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a0b24bbd-aaed-4efc-a57f-52f4e3ca812a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixpeek%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0ec97228-1124-4e06-abf5-32ccf3d9a538&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a0b24bbd-aaed-4efc-a57f-52f4e3ca812a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixpeek%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574731233&cv=11&fst=1748574731233&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixpeek%2F&hn=www.googleadservices.com&frm=0&tiba=Mixpeek%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=21165070.1748574730&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)