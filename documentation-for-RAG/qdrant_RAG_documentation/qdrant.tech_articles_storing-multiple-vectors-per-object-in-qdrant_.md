---
url: "https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/"
title: "Optimizing Semantic Search by Managing Multiple Vectors - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Optimizing Semantic Search by Managing Multiple Vectors

[Back to Vector Search Manuals](https://qdrant.tech/articles/vector-search-manuals/)

# Optimizing Semantic Search by Managing Multiple Vectors

Kacper Łukawski

·

October 05, 2022

![Optimizing Semantic Search by Managing Multiple Vectors](https://qdrant.tech/articles_data/storing-multiple-vectors-per-object-in-qdrant/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#how-to-optimize-vector-storage-by-storing-multiple-vectors-per-object) How to Optimize Vector Storage by Storing Multiple Vectors Per Object

In a real case scenario, a single object might be described in several different ways. If you run an e-commerce business, then your items will typically have a name, longer textual description and also a bunch of photos. While cooking, you may care about the list of ingredients, and description of the taste but also the recipe and the way your meal is going to look. Up till now, if you wanted to enable [semantic search](https://qdrant.tech/documentation/tutorials/search-beginners/) with multiple vectors per object, Qdrant would require you to create separate collections for each vector type, even though they could share some other attributes in a payload. However, since Qdrant 0.10 you are able to store all those vectors together in the same collection and share a single copy of the payload!

Running the new version of Qdrant is as simple as it always was. By running the following command, you are able to set up a single instance that will also expose the HTTP API:

```
docker run -p 6333:6333 qdrant/qdrant:v0.10.1

```

## [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#creating-a-collection) Creating a collection

Adding new functionalities typically requires making some changes to the interfaces, so no surprise we had to do it to enable the multiple vectors support. Currently, if you want to create a collection, you need to define the configuration of all the vectors you want to store for each object. Each vector type has its own name and the distance function used to measure how far the points are.

```python
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

client = QdrantClient()
client.create_collection(
   collection_name="multiple_vectors",
   vectors_config={
       "title": VectorParams(
           size=100,
           distance=Distance.EUCLID,
       ),
       "image": VectorParams(
           size=786,
           distance=Distance.COSINE,
       ),
   }
)

```

In case you want to keep a single vector per collection, you can still do it without putting a name though.

```python
client.create_collection(
   collection_name="single_vector",
   vectors_config=VectorParams(
       size=100,
       distance=Distance.COSINE,
   )
)

```

All the search-related operations have slightly changed their interfaces as well, so you can choose which vector to use in a specific request. However, it might be easier to see all the changes by following an end-to-end Qdrant usage on a real-world example.

## [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#building-service-with-multiple-embeddings) Building service with multiple embeddings

Quite a common approach to building search engines is to combine semantic textual capabilities with image search as well. For that purpose, we need a dataset containing both images and their textual descriptions. There are several datasets available with [MS\_COCO\_2017\_URL\_TEXT](https://huggingface.co/datasets/ChristophSchuhmann/MS_COCO_2017_URL_TEXT) being probably the simplest available. And because it’s available on HuggingFace, we can easily use it with their [datasets](https://huggingface.co/docs/datasets/index) library.

```python
from datasets import load_dataset

dataset = load_dataset("ChristophSchuhmann/MS_COCO_2017_URL_TEXT")

```

Right now, we have a dataset with a structure containing the image URL and its textual description in English. For simplicity, we can convert it to the DataFrame, as this structure might be quite convenient for future processing.

```python
import pandas as pd

dataset_df = pd.DataFrame(dataset["train"])

```

The dataset consists of two columns: _TEXT_ and _URL_. Thus, each data sample is described by two separate pieces of information and each of them has to be encoded with a different model.

## [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#processing-the-data-with-pretrained-models) Processing the data with pretrained models

Thanks to [embetter](https://github.com/koaning/embetter), we can reuse some existing pretrained models and use a convenient scikit-learn API, including pipelines. This library also provides some utilities to load the images, but only supports the local filesystem, so we need to create our own class that will download the file, given its URL.

```python
from pathlib import Path
from urllib.request import urlretrieve
from embetter.base import EmbetterBase

class DownloadFile(EmbetterBase):

   def __init__(self, out_dir: Path):
       self.out_dir = out_dir

   def transform(self, X, y=None):
       output_paths = []
       for x in X:
           output_file = self.out_dir / Path(x).name
           urlretrieve(x, output_file)
           output_paths.append(str(output_file))
       return output_paths

```

Now we’re ready to define the pipelines to process our images and texts using _all-MiniLM-L6-v2_ and _vit\_base\_patch16\_224_ models respectively. First of all, let’s start with Qdrant configuration.

## [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#creating-qdrant-collection) Creating Qdrant collection

We’re going to put two vectors per object (one for image and another one for text), so we need to create a collection with a configuration allowing us to do so.

```python
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

client = QdrantClient(timeout=None)
client.create_collection(
   collection_name="ms-coco-2017",
   vectors_config={
       "text": VectorParams(
           size=384,
           distance=Distance.EUCLID,
       ),
       "image": VectorParams(
           size=1000,
           distance=Distance.COSINE,
       ),
   },
)

```

## [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#defining-the-pipelines) Defining the pipelines

And since we have all the puzzles already in place, we can start the processing to convert raw data into the embeddings we need. The pretrained models come in handy.

```python
from sklearn.pipeline import make_pipeline
from embetter.grab import ColumnGrabber
from embetter.vision import ImageLoader, TimmEncoder
from embetter.text import SentenceEncoder

output_directory = Path("./images")

image_pipeline = make_pipeline(
   ColumnGrabber("URL"),
   DownloadFile(output_directory),
   ImageLoader(),
   TimmEncoder("vit_base_patch16_224"),
)

text_pipeline = make_pipeline(
   ColumnGrabber("TEXT"),
   SentenceEncoder("all-MiniLM-L6-v2"),
)

```

Thanks to the scikit-learn API, we can simply call each pipeline on the created DataFrame and put created vectors into Qdrant to enable fast vector search. For convenience, we’re going to put the vectors as other columns in our DataFrame.

```python
sample_df = dataset_df.sample(n=2000, random_state=643)
image_vectors = image_pipeline.transform(sample_df)
text_vectors = text_pipeline.transform(sample_df)
sample_df["image_vector"] = image_vectors.tolist()
sample_df["text_vector"] = text_vectors.tolist()

```

The created vectors might be easily put into Qdrant. For the sake of simplicity, we’re going to skip it, but if you are interested in details, please check out the [Jupyter notebook](https://gist.github.com/kacperlukawski/961aaa7946f55110abfcd37fbe869b8f) going step by step.

## [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#searching-with-multiple-vectors) Searching with multiple vectors

If you decided to describe each object with several [neural embeddings](https://qdrant.tech/articles/neural-search-tutorial/), then at each search operation you need to provide the vector name along with the [vector embedding](https://qdrant.tech/articles/what-are-embeddings/), so the engine knows which one to use. The interface of the search operation is pretty straightforward and requires an instance of NamedVector.

```python
from qdrant_client.http.models import NamedVector

text_results = client.search(
   collection_name="ms-coco-2017",
   query_vector=NamedVector(
       name="text",
       vector=row["text_vector"],
   ),
   limit=5,
   with_vectors=False,
   with_payload=True,
)

```

If we, on the other hand, decided to search using the image embedding, then we just provide the vector name we have chosen while creating the collection, so instead of “text”, we would provide “image”, as this is how we configured it at the very beginning.

## [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#the-results-image-vs-text-search) The results: image vs text search

Since we have two different vectors describing each object, we can perform the search query using any of those. That shouldn’t be surprising then, that the results are different depending on the chosen embedding method. The images below present the results returned by Qdrant for the image/text on the left-hand side.

### [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#image-search) Image search

If we query the system using image embedding, then it returns the following results:

![](https://qdrant.tech/blog/from_cms/0_5nqlmjznjkvdrjhj.webp)Image search results

### [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#text-search) Text search

However, if we use textual description embedding, then the results are slightly different:

![](https://qdrant.tech/blog/from_cms/0_3sdgctswb99xtexl.webp)Text search However, if we use textual description embedding, then the results are slightly different:

It is not surprising that a method used for creating neural encoding plays an important role in the search process and its quality. If your data points might be described using several vectors, then the latest release of Qdrant gives you an opportunity to store them together and reuse the payloads, instead of creating several collections and querying them separately.

### [Anchor](https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/\#summary) Summary:

- Qdrant 0.10 introduces efficient vector storage optimization, allowing seamless management of multiple vectors per object within a single collection.
- This update streamlines semantic search capabilities by eliminating the need for separate collections for each vector type, enhancing search accuracy and performance.
- With Qdrant’s new features, users can easily configure vector parameters, including size and distance functions, for each vector type, optimizing search results and user experience.

If you’d like to check out some other examples, please check out our [full notebook](https://gist.github.com/kacperlukawski/961aaa7946f55110abfcd37fbe869b8f) presenting the search results and the whole pipeline implementation.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/storing-multiple-vectors-per-object-in-qdrant.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/storing-multiple-vectors-per-object-in-qdrant.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575547741&cv=11&fst=1748575547741&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fstoring-multiple-vectors-per-object-in-qdrant%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Optimizing%20Semantic%20Search%20by%20Managing%20Multiple%20Vectors%20-%20Qdrant&npa=0&pscdl=noapi&auid=2049254303.1748575548&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575547726&cv=11&fst=1748575547726&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fstoring-multiple-vectors-per-object-in-qdrant%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Optimizing%20Semantic%20Search%20by%20Managing%20Multiple%20Vectors%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2049254303.1748575548&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=2ad12ce2-2757-4d3c-be38-11e0ebd3b97a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eddeba50-f362-4f34-888c-aaa3c46a8ac9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fstoring-multiple-vectors-per-object-in-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=2ad12ce2-2757-4d3c-be38-11e0ebd3b97a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eddeba50-f362-4f34-888c-aaa3c46a8ac9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fstoring-multiple-vectors-per-object-in-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575548746&cv=11&fst=1748575548746&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fstoring-multiple-vectors-per-object-in-qdrant%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Optimizing%20Semantic%20Search%20by%20Managing%20Multiple%20Vectors%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2049254303.1748575548&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)