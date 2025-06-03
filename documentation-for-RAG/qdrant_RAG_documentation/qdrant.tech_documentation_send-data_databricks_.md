---
url: "https://qdrant.tech/documentation/send-data/databricks/"
title: "Qdrant on Databricks - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Send data](https://qdrant.tech/documentation/send-data/)
- Qdrant on Databricks

# [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#qdrant-on-databricks) Qdrant on Databricks

| Time: 30 min | Level: Intermediate | [Complete Notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4750876096379825/93425612168199/6949977306828869/latest.html) |
| --- | --- | --- |

[Databricks](https://www.databricks.com/) is a unified analytics platform for working with big data and AI. It’s built around Apache Spark, a powerful open-source distributed computing system well-suited for processing large-scale datasets and performing complex analytics tasks.

Apache Spark is designed to scale horizontally, meaning it can handle expensive operations like generating vector embeddings by distributing computation across a cluster of machines. This scalability is crucial when dealing with large datasets.

In this example, we will demonstrate how to vectorize a dataset with dense and sparse embeddings using Qdrant’s [FastEmbed](https://qdrant.github.io/fastembed/) library. We will then load this vectorized data into a Qdrant cluster using the [Qdrant Spark connector](https://qdrant.tech/documentation/frameworks/spark/) on Databricks.

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#setting-up-a-databricks-project) Setting up a Databricks project

- Set up a **[Databricks cluster](https://docs.databricks.com/en/compute/configure.html)** following the official documentation guidelines.

- Install the **[Qdrant Spark connector](https://qdrant.tech/documentation/frameworks/spark/)** as a library:

  - Navigate to the `Libraries` section in your cluster dashboard.

  - Click on `Install New` at the top-right to open the library installation modal.

  - Search for `io.qdrant:spark:VERSION` in the Maven packages and click on `Install`.

    ![Install the library](https://qdrant.tech/documentation/examples/databricks/library-install.png)
- Create a new **[Databricks notebook](https://docs.databricks.com/en/notebooks/index.html)** on your cluster to begin working with your data and libraries.


### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#download-a-dataset) Download a dataset

- **Install the required dependencies:**

```python
%pip install fastembed datasets

```

- **Download the dataset:**

```python
from datasets import load_dataset

dataset_name = "tasksource/med"
dataset = load_dataset(dataset_name, split="train")
# We'll use the first 100 entries from this dataset and exclude some unused columns.
dataset = dataset.select(range(100)).remove_columns(["gold_label", "genre"])

```

- **Convert the dataset into a Spark dataframe:**

```python
dataset.to_parquet("/dbfs/pq.pq")
dataset_df = spark.read.parquet("file:/dbfs/pq.pq")

```

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#vectorizing-the-data) Vectorizing the data

In this section, we’ll be generating both dense and sparse vectors for our rows using [FastEmbed](https://qdrant.github.io/fastembed/). We’ll create a user-defined function (UDF) to handle this step.

#### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#creating-the-vectorization-function) Creating the vectorization function

```python
from fastembed import TextEmbedding, SparseTextEmbedding

def vectorize(partition_data):
    # Initialize dense and sparse models
    dense_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    sparse_model = SparseTextEmbedding(model_name="Qdrant/bm25")

    for row in partition_data:
        # Generate dense and sparse vectors
        dense_vector = next(dense_model.embed(row.sentence1))
        sparse_vector = next(sparse_model.embed(row.sentence2))

        yield [\
            row.sentence1,  # 1st column: original text\
            row.sentence2,  # 2nd column: original text\
            dense_vector.tolist(),  # 3rd column: dense vector\
            sparse_vector.indices.tolist(),  # 4th column: sparse vector indices\
            sparse_vector.values.tolist(),  # 5th column: sparse vector values\
        ]

```

We’re using the [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) model for dense embeddings and [BM25](https://huggingface.co/Qdrant/bm25) for sparse embeddings.

#### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#applying-the-udf-on-our-dataframe) Applying the UDF on our dataframe

Next, let’s apply our `vectorize` UDF on our Spark dataframe to generate embeddings.

```python
embeddings = dataset_df.rdd.mapPartitions(vectorize)

```

The `mapPartitions()` method returns a [Resilient Distributed Dataset (RDD)](https://www.databricks.com/glossary/what-is-rdd) which should then be converted back to a Spark dataframe.

#### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#building-the-new-spark-dataframe-with-the-vectorized-data) Building the new Spark dataframe with the vectorized data

We’ll now create a new Spark dataframe ( `embeddings_df`) with the vectorized data using the specified schema.

```python
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, FloatType, IntegerType

# Define the schema for the new dataframe
schema = StructType([\
    StructField("sentence1", StringType()),\
    StructField("sentence2", StringType()),\
    StructField("dense_vector", ArrayType(FloatType())),\
    StructField("sparse_vector_indices", ArrayType(IntegerType())),\
    StructField("sparse_vector_values", ArrayType(FloatType()))\
])

# Create the new dataframe with the vectorized data
embeddings_df = spark.createDataFrame(data=embeddings, schema=schema)

```

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#uploading-the-data-to-qdrant) Uploading the data to Qdrant

- **Create a Qdrant collection:**


  - [Follow the documentation](https://qdrant.tech/documentation/concepts/collections/#create-a-collection) to create a collection with the appropriate configurations. Here’s an example request to support both dense and sparse vectors:

```json
PUT /collections/{collection_name}
{
  "vectors": {
    "dense": {
      "size": 384,
      "distance": "Cosine"
    }
  },
  "sparse_vectors": {
    "sparse": {}
  }
}

```

- **Upload the dataframe to Qdrant:**


```python
options = {
    "qdrant_url": "<QDRANT_GRPC_URL>",
    "api_key": "<QDRANT_API_KEY>",
    "collection_name": "<QDRANT_COLLECTION_NAME>",
    "vector_fields": "dense_vector",
    "vector_names": "dense",
    "sparse_vector_value_fields": "sparse_vector_values",
    "sparse_vector_index_fields": "sparse_vector_indices",
    "sparse_vector_names": "sparse",
    "schema": embeddings_df.schema.json(),
}

embeddings_df.write.format("io.qdrant.spark.Qdrant").options(**options).mode(
    "append"
).save()

```

Ensure to replace the placeholder values ( `<QDRANT_GRPC_URL>`, `<QDRANT_API_KEY>`, `<QDRANT_COLLECTION_NAME>`) with your actual values. If the `id_field` option is not specified, Qdrant Spark connector generates random UUIDs for each point.

The command output you should see is similar to:

```console
Command took 40.37 seconds -- by xxxxx90@xxxxxx.com at 4/17/2024, 12:13:28 PM on fastembed

```

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#conclusion) Conclusion

That wraps up our tutorial! Feel free to explore more functionalities and experiments with different models, parameters, and features available in Databricks, Spark, and Qdrant.

Happy data engineering!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/databricks.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/databricks.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574828432&cv=11&fst=1748574828432&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsend-data%2Fdatabricks%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20on%20Databricks%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1664685302.1748574828&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1~em.BI-OMq6JiBzU0PMlTnMSc3kiYbq8Gp00VKYUN-xHfqA&_ht=t.0~l.50&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574828487&cv=11&fst=1748574828487&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsend-data%2Fdatabricks%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20on%20Databricks%20-%20Qdrant&npa=0&pscdl=noapi&auid=1664685302.1748574828&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=76820ad2-2d32-4b7b-bf49-faf32958d3d9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb851c71-8df0-4060-af64-be6d395346b5&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsend-data%2Fdatabricks%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=76820ad2-2d32-4b7b-bf49-faf32958d3d9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb851c71-8df0-4060-af64-be6d395346b5&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsend-data%2Fdatabricks%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574829657&cv=11&fst=1748574829657&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsend-data%2Fdatabricks%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20on%20Databricks%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1664685302.1748574828&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)