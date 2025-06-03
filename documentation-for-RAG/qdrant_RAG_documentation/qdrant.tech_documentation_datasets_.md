---
url: "https://qdrant.tech/documentation/datasets/"
title: "Practice Datasets - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- Practice Datasets

# [Anchor](https://qdrant.tech/documentation/datasets/\#common-datasets-in-snapshot-format) Common Datasets in Snapshot Format

You may find that creating embeddings from datasets is a very resource-intensive task.
If you need a practice dataset, feel free to pick one of the ready-made snapshots on this page.
These snapshots contain pre-computed vectors that you can easily import into your Qdrant instance.

## [Anchor](https://qdrant.tech/documentation/datasets/\#available-datasets) Available datasets

Our snapshots are usually generated from publicly available datasets, which are often used for
non-commercial or academic purposes. The following datasets are currently available. Please click
on a dataset name to see its detailed description.

| Dataset | Model | Vector size | Documents | Size | Qdrant snapshot | HF Hub |
| --- | --- | --- | --- | --- | --- | --- |
| [Arxiv.org titles](https://qdrant.tech/documentation/datasets/#arxivorg-titles) | [InstructorXL](https://huggingface.co/hkunlp/instructor-xl) | 768 | 2.3M | 7.1 GB | [Download](https://snapshots.qdrant.io/arxiv_titles-3083016565637815127-2023-05-29-13-56-22.snapshot) | [Open](https://huggingface.co/datasets/Qdrant/arxiv-titles-instructorxl-embeddings) |
| [Arxiv.org abstracts](https://qdrant.tech/documentation/datasets/#arxivorg-abstracts) | [InstructorXL](https://huggingface.co/hkunlp/instructor-xl) | 768 | 2.3M | 8.4 GB | [Download](https://snapshots.qdrant.io/arxiv_abstracts-3083016565637815127-2023-06-02-07-26-29.snapshot) | [Open](https://huggingface.co/datasets/Qdrant/arxiv-abstracts-instructorxl-embeddings) |
| [Wolt food](https://qdrant.tech/documentation/datasets/#wolt-food) | [clip-ViT-B-32](https://huggingface.co/sentence-transformers/clip-ViT-B-32) | 512 | 1.7M | 7.9 GB | [Download](https://snapshots.qdrant.io/wolt-clip-ViT-B-32-2446808438011867-2023-12-14-15-55-26.snapshot) | [Open](https://huggingface.co/datasets/Qdrant/wolt-food-clip-ViT-B-32-embeddings) |

Once you download a snapshot, you need to [restore it](https://qdrant.tech/documentation/concepts/snapshots/#restore-snapshot)
using the Qdrant CLI upon startup or through the API.

## [Anchor](https://qdrant.tech/documentation/datasets/\#qdrant-on-hugging-face) Qdrant on Hugging Face

[![HuggingFace](https://qdrant.tech/content/images/hf-logo-with-title.svg)](https://huggingface.co/Qdrant)

[Hugging Face](https://huggingface.co/) provides a platform for sharing and using ML models and
datasets. [Qdrant](https://huggingface.co/Qdrant) is one of the organizations there! We aim to
provide you with datasets containing neural embeddings that you can use to practice with Qdrant
and build your applications based on semantic search. **Please let us know if you’d like to see**
**a specific dataset!**

If you are not familiar with [Hugging Face datasets](https://huggingface.co/docs/datasets/index),
or would like to know how to combine it with Qdrant, please refer to the [tutorial](https://qdrant.tech/documentation/tutorials/huggingface-datasets/).

## [Anchor](https://qdrant.tech/documentation/datasets/\#arxivorg) Arxiv.org

[Arxiv.org](https://arxiv.org/) is a highly-regarded open-access repository of electronic preprints in multiple
fields. Operated by Cornell University, arXiv allows researchers to share their findings with
the scientific community and receive feedback before they undergo peer review for formal
publication. Its archives host millions of scholarly articles, making it an invaluable resource
for those looking to explore the cutting edge of scientific research. With a high frequency of
daily submissions from scientists around the world, arXiv forms a comprehensive, evolving dataset
that is ripe for mining, analysis, and the development of future innovations.

### [Anchor](https://qdrant.tech/documentation/datasets/\#arxivorg-titles) Arxiv.org titles

This dataset contains embeddings generated from the paper titles only. Each vector has a
payload with the title used to create it, along with the DOI (Digital Object Identifier).

```json
{
    "title": "Nash Social Welfare for Indivisible Items under Separable, Piecewise-Linear Concave Utilities",
    "DOI": "1612.05191"
}

```

The embeddings generated with InstructorXL model have been generated using the following
instruction:

> Represent the Research Paper title for retrieval; Input:

The following code snippet shows how to generate embeddings using the InstructorXL model:

```python
from InstructorEmbedding import INSTRUCTOR

model = INSTRUCTOR("hkunlp/instructor-xl")
sentence = "3D ActionSLAM: wearable person tracking in multi-floor environments"
instruction = "Represent the Research Paper title for retrieval; Input:"
embeddings = model.encode([[instruction, sentence]])

```

The snapshot of the dataset might be downloaded [here](https://snapshots.qdrant.io/arxiv_titles-3083016565637815127-2023-05-29-13-56-22.snapshot).

#### [Anchor](https://qdrant.tech/documentation/datasets/\#importing-the-dataset) Importing the dataset

The easiest way to use the provided dataset is to recover it via the API by passing the
URL as a location. It works also in [Qdrant Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=bdb6eeb7-7111-44cb-91f7-caf219c42940). The following
code snippet shows how to create a new collection and fill it with the snapshot data:

```http
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "https://snapshots.qdrant.io/arxiv_titles-3083016565637815127-2023-05-29-13-56-22.snapshot"
}

```

### [Anchor](https://qdrant.tech/documentation/datasets/\#arxivorg-abstracts) Arxiv.org abstracts

This dataset contains embeddings generated from the paper abstracts. Each vector has a
payload with the abstract used to create it, along with the DOI (Digital Object Identifier).

```json
{
    "abstract": "Recently Cole and Gkatzelis gave the first constant factor approximation\nalgorithm for the problem of allocating indivisible items to agents, under\nadditive valuations, so as to maximize the Nash Social Welfare. We give\nconstant factor algorithms for a substantial generalization of their problem --\nto the case of separable, piecewise-linear concave utility functions. We give\ntwo such algorithms, the first using market equilibria and the second using the\ntheory of stable polynomials.\n  In AGT, there is a paucity of methods for the design of mechanisms for the\nallocation of indivisible goods and the result of Cole and Gkatzelis seemed to\nbe taking a major step towards filling this gap. Our result can be seen as\nanother step in this direction.\n",
    "DOI": "1612.05191"
}

```

The embeddings generated with InstructorXL model have been generated using the following
instruction:

> Represent the Research Paper abstract for retrieval; Input:

The following code snippet shows how to generate embeddings using the InstructorXL model:

```python
from InstructorEmbedding import INSTRUCTOR

model = INSTRUCTOR("hkunlp/instructor-xl")
sentence = "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train."
instruction = "Represent the Research Paper abstract for retrieval; Input:"
embeddings = model.encode([[instruction, sentence]])

```

The snapshot of the dataset might be downloaded [here](https://snapshots.qdrant.io/arxiv_abstracts-3083016565637815127-2023-06-02-07-26-29.snapshot).

#### [Anchor](https://qdrant.tech/documentation/datasets/\#importing-the-dataset-1) Importing the dataset

The easiest way to use the provided dataset is to recover it via the API by passing the
URL as a location. It works also in [Qdrant Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=bdb6eeb7-7111-44cb-91f7-caf219c42940). The following
code snippet shows how to create a new collection and fill it with the snapshot data:

```http
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "https://snapshots.qdrant.io/arxiv_abstracts-3083016565637815127-2023-06-02-07-26-29.snapshot"
}

```

## [Anchor](https://qdrant.tech/documentation/datasets/\#wolt-food) Wolt food

Our [Food Discovery demo](https://food-discovery.qdrant.tech/) relies on the dataset of
food images from the Wolt app. Each point in the collection represents a dish with a single
image. The image is represented as a vector of 512 float numbers. There is also a JSON
payload attached to each point, which looks similar to this:

```json
{
    "cafe": {
        "address": "VGX7+6R2 Vecchia Napoli, Valletta",
        "categories": ["italian", "pasta", "pizza", "burgers", "mediterranean"],
        "location": {"lat": 35.8980154, "lon": 14.5145106},
        "menu_id": "610936a4ee8ea7a56f4a372a",
        "name": "Vecchia Napoli Is-Suq Tal-Belt",
        "rating": 9,
        "slug": "vecchia-napoli-skyparks-suq-tal-belt"
    },
    "description": "Tomato sauce, mozzarella fior di latte, crispy guanciale, Pecorino Romano cheese and a hint of chilli",
    "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/610936a4ee8ea7a56f4a372a/005dfeb2-e734-11ec-b667-ced7a78a5abd_l_amatriciana_pizza_joel_gueller1.jpeg",
    "name": "L'Amatriciana"
}

```

The embeddings generated with clip-ViT-B-32 model have been generated using the following
code snippet:

```python
from PIL import Image
from sentence_transformers import SentenceTransformer

image_path = "5dbfd216-5cce-11eb-8122-de94874ad1c8_ns_takeaway_seelachs_ei_baguette.jpeg"

model = SentenceTransformer("clip-ViT-B-32")
embedding = model.encode(Image.open(image_path))

```

The snapshot of the dataset might be downloaded [here](https://snapshots.qdrant.io/wolt-clip-ViT-B-32-2446808438011867-2023-12-14-15-55-26.snapshot).

#### [Anchor](https://qdrant.tech/documentation/datasets/\#importing-the-dataset-2) Importing the dataset

The easiest way to use the provided dataset is to recover it via the API by passing the
URL as a location. It works also in [Qdrant Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=bdb6eeb7-7111-44cb-91f7-caf219c42940). The following
code snippet shows how to create a new collection and fill it with the snapshot data:

```http
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "https://snapshots.qdrant.io/wolt-clip-ViT-B-32-2446808438011867-2023-12-14-15-55-26.snapshot"
}

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/datasets.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/datasets.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574058365&cv=11&fst=1748574058365&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatasets%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Practice%20Datasets%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=425975894.1748574058&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574058445&cv=11&fst=1748574058445&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatasets%2F&hn=www.googleadservices.com&frm=0&tiba=Practice%20Datasets%20-%20Qdrant&npa=0&pscdl=noapi&auid=425975894.1748574058&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ee088d01-b557-4019-8ea1-67fa25b0b800&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4a1b4199-4302-46dc-b297-e25fc864458c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatasets%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ee088d01-b557-4019-8ea1-67fa25b0b800&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4a1b4199-4302-46dc-b297-e25fc864458c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatasets%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)