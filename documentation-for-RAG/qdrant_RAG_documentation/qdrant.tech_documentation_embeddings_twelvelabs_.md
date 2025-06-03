---
url: "https://qdrant.tech/documentation/embeddings/twelvelabs/"
title: "Twelve Labs - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Twelve Labs

# [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#twelve-labs) Twelve Labs

[Twelve Labs](https://twelvelabs.io/) Embed API provides powerful embeddings that represent videos, texts, images, and audio in a unified vector space. This space enables any-to-any searches across different types of content.

By natively processing all modalities, it captures interactions like visual expressions, speech, and context, enabling advanced applications such as sentiment analysis, anomaly detection, and recommendation systems with precision and efficiency.

We’ll look at how to work with Twelve Labs embeddings in Qdrant via the Python and Node SDKs.

### [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#installing-the-sdks) Installing the SDKs

pythontypescript

```python
$ pip install twelvelabs qdrant-client

```

```typescript
$ npm install twelvelabs-js @qdrant/js-client-rest

```

### [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#setting-up-the-clients) Setting up the clients

pythontypescript

```python
from twelvelabs import TwelveLabs
from qdrant_client import QdrantClient

# Get your API keys from:
# https://playground.twelvelabs.io/dashboard/api-key
TL_API_KEY = "<YOUR_TWELVE_LABS_API_KEY>"

twelvelabs_client = TwelveLabs(api_key=TL_API_KEY)
qdrant_client = QdrantClient(url="http://localhost:6333/")

```

```typescript
import { QdrantClient } from '@qdrant/js-client-rest';
import { TwelveLabs, EmbeddingsTask, SegmentEmbedding } from 'twelvelabs-js';

// Get your API keys from:
// https://playground.twelvelabs.io/dashboard/api-key
const TL_API_KEY = "<YOUR_TWELVE_LABS_API_KEY>"

const twelveLabsClient = new TwelveLabs({ apiKey: TL_API_KEY });
const qdrantClient = new QdrantClient({ url: 'http://localhost:6333' });

```

The following example uses the `"Marengo-retrieval-2.7"` model to embed a video. It generates vector embeddings of 1024 dimensionality and works with cosine similarity.

You can use the same model to embed audio, text and images into a common vector space. Enabling cross-modality searches!

### [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#embedding-videos) Embedding videos

pythontypescript

```python
task = twelvelabs_client.embed.task.create(
    model_name="Marengo-retrieval-2.7",
    video_url="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4"
)

task.wait_for_done(sleep_interval=3)

task_result = twelvelabs_client.embed.task.retrieve(task.id)

```

```typescript
const task = await twelveLabsClient.embed.task.create("Marengo-retrieval-2.7", {
    url: "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4"
})

await task.waitForDone(3)

const taskResult = await twelveLabsClient.embed.task.retrieve(task.id)

```

### [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#converting-the-model-outputs-to-qdrant-points) Converting the model outputs to Qdrant points

pythontypescript

```python
from qdrant_client.models import PointStruct

points = [\
    PointStruct(\
        id=idx,\
        vector=v.embeddings_float,\
        payload={\
            "start_offset_sec": v.start_offset_sec,\
            "end_offset_sec": v.end_offset_sec,\
            "embedding_scope": v.embedding_scope,\
        },\
    )\
    for idx, v in enumerate(task_result.video_embedding.segments)\
]

```

```typescript
let points = taskResult.videoEmbedding.segments.map((data, i) => {
    return {
        id: i,
        vector: data.embeddingsFloat,
        payload: {
            startOffsetSec: data.startOffsetSec,
            endOffsetSec: data.endOffsetSec,
            embeddingScope: data.embeddingScope
        }
    }
})

```

### [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#creating-a-collection-to-insert-the-vectors) Creating a collection to insert the vectors

pythontypescript

```python
from qdrant_client.models import VectorParams, Distance

collection_name = "twelve_labs_collection"

qdrant_client.create_collection(
    collection_name,
    vectors_config=VectorParams(
        size=1024,
        distance=Distance.COSINE,
    ),
)
qdrant_client.upsert(collection_name, points)

```

```typescript
const COLLECTION_NAME = "twelve_labs_collection"

await qdrantClient.createCollection(COLLECTION_NAME, {
    vectors: {
        size: 1024,
        distance: 'Cosine',
    }
});

await qdrantClient.upsert(COLLECTION_NAME, {
    wait: true,
    points
})

```

## [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#perform-a-search) Perform a search

Once the vectors are added, you can run semantic searches across different modalities. Let’s try text.

pythontypescript

```python
text_segment = twelvelabs_client.embed.create(
    model_name="Marengo-retrieval-2.7",
    text="<YOUR_QUERY_TEXT>",
).text_embedding.segments[0]

qdrant_client.query_points(
    collection_name=collection_name,
    query=text_segment.embeddings_float,
)

```

```typescript
const textSegment = (await twelveLabsClient.embed.create({
    modelName: "Marengo-retrieval-2.7",
    text: "<YOUR_QUERY_TEXT>"
})).textEmbedding.segments[0]

await qdrantClient.query(COLLECTION_NAME, {
    query: textSegment.embeddingsFloat,
});

```

Let’s try audio:

pythontypescript

```python
audio_segment = twelvelabs_client.embed.create(
    model_name="Marengo-retrieval-2.7",
    audio_url="https://codeskulptor-demos.commondatastorage.googleapis.com/descent/background%20music.mp3",
).audio_embedding.segments[0]

qdrant_client.query_points(
    collection_name=collection_name,
    query=audio_segment.embeddings_float,
)

```

```typescript
const audioSegment = (await twelveLabsClient.embed.create({
    modelName: "Marengo-retrieval-2.7",
    audioUrl: "https://codeskulptor-demos.commondatastorage.googleapis.com/descent/background%20music.mp3"
})).audioEmbedding.segments[0]

await qdrantClient.query(COLLECTION_NAME, {
    query: audioSegment.embeddingsFloat,
});

```

Similarly, querying by image:

pythontypescript

```python
image_segment = twelvelabs_client.embed.create(
    model_name="Marengo-retrieval-2.7",
    image_url="https://gratisography.com/wp-content/uploads/2024/01/gratisography-cyber-kitty-1170x780.jpg",
).image_embedding.segments[0]

qdrant_client.query_points(
    collection_name=collection_name,
    query=image_segment.embeddings_float,
)

```

```typescript
const imageSegment = (await twelveLabsClient.embed.create({
    modelName: "Marengo-retrieval-2.7",
    imageUrl: "https://gratisography.com/wp-content/uploads/2024/01/gratisography-cyber-kitty-1170x780.jpg"
})).imageEmbedding.segments[0]

await qdrantClient.query(COLLECTION_NAME, {
    query: imageSegment.embeddingsFloat,
});

```

## [Anchor](https://qdrant.tech/documentation/embeddings/twelvelabs/\#further-reading) Further Reading

- [Twelve Labs Documentation](https://docs.twelvelabs.io/)
- [Twelve Labs Examples](https://docs.twelvelabs.io/docs/sample-applications)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/twelvelabs.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/twelvelabs.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574458441&cv=11&fst=1748574458441&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Ftwelvelabs%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Twelve%20Labs%20-%20Qdrant&npa=0&pscdl=noapi&auid=1987652141.1748574458&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574458419&cv=11&fst=1748574458419&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Ftwelvelabs%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Twelve%20Labs%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1987652141.1748574458&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9904ab92-5b6c-40f1-9eb6-9003c0aa8301&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=83b6e3ab-b895-40aa-b7b8-dd0acb448525&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Ftwelvelabs%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9904ab92-5b6c-40f1-9eb6-9003c0aa8301&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=83b6e3ab-b895-40aa-b7b8-dd0acb448525&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Ftwelvelabs%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574459668&cv=11&fst=1748574459668&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Ftwelvelabs%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Twelve%20Labs%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1987652141.1748574458&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)