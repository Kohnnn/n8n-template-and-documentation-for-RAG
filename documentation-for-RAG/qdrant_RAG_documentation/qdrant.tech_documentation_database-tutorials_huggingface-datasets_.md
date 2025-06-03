---
url: "https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/"
title: "Load a HuggingFace Dataset - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Database tutorials](https://qdrant.tech/documentation/database-tutorials/)
- Load a HuggingFace Dataset

# [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#load-and-search-hugging-face-datasets-with-qdrant) Load and Search Hugging Face Datasets with Qdrant

[Hugging Face](https://huggingface.co/) provides a platform for sharing and using ML models and
datasets. [Qdrant](https://huggingface.co/Qdrant) also publishes datasets along with the
embeddings that you can use to practice with Qdrant and build your applications based on semantic
search. **Please [let us know](https://qdrant.to/discord) if you’d like to see a specific dataset!**

## [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#arxiv-titles-instructorxl-embeddings) arxiv-titles-instructorxl-embeddings

[This dataset](https://huggingface.co/datasets/Qdrant/arxiv-titles-instructorxl-embeddings) contains
embeddings generated from the paper titles only. Each vector has a payload with the title used to
create it, along with the DOI (Digital Object Identifier).

```json
{
    "title": "Nash Social Welfare for Indivisible Items under Separable, Piecewise-Linear Concave Utilities",
    "DOI": "1612.05191"
}

```

You can find a detailed description of the dataset in the [Practice Datasets](https://qdrant.tech/documentation/datasets/#journal-article-titles)
section. If you prefer loading the dataset from a Qdrant snapshot, it also linked there.

Loading the dataset is as simple as using the `load_dataset` function from the `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("Qdrant/arxiv-titles-instructorxl-embeddings")

```

The dataset contains 2,250,000 vectors. This is how you can check the list of the features in the dataset:

```python
dataset.features

```

### [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#streaming-the-dataset) Streaming the dataset

Dataset streaming lets you work with a dataset without downloading it. The data is streamed as
you iterate over the dataset. You can read more about it in the [Hugging Face\\
documentation](https://huggingface.co/docs/datasets/stream).

```python
from datasets import load_dataset

dataset = load_dataset(
    "Qdrant/arxiv-titles-instructorxl-embeddings", split="train", streaming=True
)

```

### [Anchor](https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/\#loading-the-dataset-into-qdrant) Loading the dataset into Qdrant

You can load the dataset into Qdrant using the [Python SDK](https://github.com/qdrant/qdrant-client).
The embeddings are already precomputed, so you can store them in a collection, that we’re going
to create in a second:

```python
from qdrant_client import QdrantClient, models

client = QdrantClient("http://localhost:6333")

client.create_collection(
    collection_name="arxiv-titles-instructorxl-embeddings",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE,
    ),
)

```

It is always a good idea to use batching, while loading a large dataset, so let’s do that.
We are going to need a helper function to split the dataset into batches:

```python
from itertools import islice

def batched(iterable, n):
    iterator = iter(iterable)
    while batch := list(islice(iterator, n)):
        yield batch

```

If you are a happy user of Python 3.12+, you can use the [`batched` function from the `itertools`](https://docs.python.org/3/library/itertools.html#itertools.batched) package instead.

No matter what Python version you are using, you can use the `upsert` method to load the dataset,
batch by batch, into Qdrant:

```python
batch_size = 100

for batch in batched(dataset, batch_size):
    ids = [point.pop("id") for point in batch]
    vectors = [point.pop("vector") for point in batch]

    client.upsert(
        collection_name="arxiv-titles-instructorxl-embeddings",
        points=models.Batch(
            ids=ids,
            vectors=vectors,
            payloads=batch,
        ),
    )

```

Your collection is ready to be used for search! Please [let us know using Discord](https://qdrant.to/discord)
if you would like to see more datasets published on Hugging Face hub.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/huggingface-datasets.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/huggingface-datasets.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574539478&cv=11&fst=1748574539478&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fhuggingface-datasets%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Load%20a%20HuggingFace%20Dataset%20-%20Qdrant&npa=0&pscdl=noapi&auid=327808662.1748574539&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574539445&cv=11&fst=1748574539445&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fhuggingface-datasets%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Load%20a%20HuggingFace%20Dataset%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=327808662.1748574539&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0c7c745f-8695-4f93-9846-9ba9212ceed3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a03331ae-202d-438b-b49b-de41993a7df6&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fhuggingface-datasets%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0c7c745f-8695-4f93-9846-9ba9212ceed3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a03331ae-202d-438b-b49b-de41993a7df6&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fhuggingface-datasets%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574540673&cv=11&fst=1748574540673&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fhuggingface-datasets%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Load%20a%20HuggingFace%20Dataset%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=327808662.1748574539&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)