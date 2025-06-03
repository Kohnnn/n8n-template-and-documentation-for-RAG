---
url: "https://qdrant.tech/documentation/data-management/spark/"
title: "Apache Spark - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- Apache Spark

# [Anchor](https://qdrant.tech/documentation/data-management/spark/\#apache-spark) Apache Spark

[Spark](https://spark.apache.org/) is a distributed computing framework designed for big data processing and analytics. The [Qdrant-Spark connector](https://github.com/qdrant/qdrant-spark) enables Qdrant to be a storage destination in Spark.

## [Anchor](https://qdrant.tech/documentation/data-management/spark/\#installation) Installation

To integrate the connector into your Spark environment, get the JAR file from one of the sources listed below.

- GitHub Releases

The packaged `jar` file with all the required dependencies can be found [here](https://github.com/qdrant/qdrant-spark/releases).

- Building from Source

To build the `jar` from source, you need [JDK@8](https://www.azul.com/downloads/#zulu) and [Maven](https://maven.apache.org/) installed. Once the requirements have been satisfied, run the following command in the [project root](https://github.com/qdrant/qdrant-spark).

```bash
mvn package -DskipTests

```

The JAR file will be written into the `target` directory by default.

- Maven Central

Find the project on Maven Central [here](https://central.sonatype.com/artifact/io.qdrant/spark).

## [Anchor](https://qdrant.tech/documentation/data-management/spark/\#usage) Usage

### [Anchor](https://qdrant.tech/documentation/data-management/spark/\#creating-a-spark-session-with-qdrant-support) Creating a Spark session with Qdrant support

pythonscalajava

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.config(
        "spark.jars",
        "path/to/file/spark-VERSION.jar",  # Specify the path to the downloaded JAR file
    )
    .master("local[*]")
    .appName("qdrant")
    .getOrCreate()

```

```scala
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder
  .config("spark.jars", "path/to/file/spark-VERSION.jar") // Specify the path to the downloaded JAR file
  .master("local[*]")
  .appName("qdrant")
  .getOrCreate()

```

```java
import org.apache.spark.sql.SparkSession;

public class QdrantSparkJavaExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .config("spark.jars", "path/to/file/spark-VERSION.jar") // Specify the path to the downloaded JAR file
                .master("local[*]")
                .appName("qdrant")
                .getOrCreate();
    }
}

```

### [Anchor](https://qdrant.tech/documentation/data-management/spark/\#loading-data) Loading data

Before loading the data using this connector, a collection has to be [created](https://qdrant.tech/documentation/concepts/collections/#create-a-collection) in advance with the appropriate vector dimensions and configurations.

The connector supports ingesting multiple named/unnamed, dense/sparse vectors.

_Click each to expand._

**Unnamed/Default vector**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", <QDRANT_GRPC_URL>)
   .option("collection_name", <QDRANT_COLLECTION_NAME>)
   .option("embedding_field", <EMBEDDING_FIELD_NAME>)  # Expected to be a field of type ArrayType(FloatType)
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

**Named vector**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", <QDRANT_GRPC_URL>)
   .option("collection_name", <QDRANT_COLLECTION_NAME>)
   .option("embedding_field", <EMBEDDING_FIELD_NAME>)  # Expected to be a field of type ArrayType(FloatType)
   .option("vector_name", <VECTOR_NAME>)
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

> #### NOTE
>
> The `embedding_field` and `vector_name` options are maintained for backward compatibility. It is recommended to use `vector_fields` and `vector_names` for named vectors as shown below.

**Multiple named vectors**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", "<QDRANT_GRPC_URL>")
   .option("collection_name", "<QDRANT_COLLECTION_NAME>")
   .option("vector_fields", "<COLUMN_NAME>,<ANOTHER_COLUMN_NAME>")
   .option("vector_names", "<VECTOR_NAME>,<ANOTHER_VECTOR_NAME>")
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

**Sparse vectors**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", "<QDRANT_GRPC_URL>")
   .option("collection_name", "<QDRANT_COLLECTION_NAME>")
   .option("sparse_vector_value_fields", "<COLUMN_NAME>")
   .option("sparse_vector_index_fields", "<COLUMN_NAME>")
   .option("sparse_vector_names", "<SPARSE_VECTOR_NAME>")
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

**Multiple sparse vectors**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", "<QDRANT_GRPC_URL>")
   .option("collection_name", "<QDRANT_COLLECTION_NAME>")
   .option("sparse_vector_value_fields", "<COLUMN_NAME>,<ANOTHER_COLUMN_NAME>")
   .option("sparse_vector_index_fields", "<COLUMN_NAME>,<ANOTHER_COLUMN_NAME>")
   .option("sparse_vector_names", "<SPARSE_VECTOR_NAME>,<ANOTHER_SPARSE_VECTOR_NAME>")
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

**Combination of named dense and sparse vectors**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", "<QDRANT_GRPC_URL>")
   .option("collection_name", "<QDRANT_COLLECTION_NAME>")
   .option("vector_fields", "<COLUMN_NAME>,<ANOTHER_COLUMN_NAME>")
   .option("vector_names", "<VECTOR_NAME>,<ANOTHER_VECTOR_NAME>")
   .option("sparse_vector_value_fields", "<COLUMN_NAME>,<ANOTHER_COLUMN_NAME>")
   .option("sparse_vector_index_fields", "<COLUMN_NAME>,<ANOTHER_COLUMN_NAME>")
   .option("sparse_vector_names", "<SPARSE_VECTOR_NAME>,<ANOTHER_SPARSE_VECTOR_NAME>")
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

**Multi-vectors**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", "<QDRANT_GRPC_URL>")
   .option("collection_name", "<QDRANT_COLLECTION_NAME>")
   .option("multi_vector_fields", "<COLUMN_NAME>")
   .option("multi_vector_names", "<MULTI_VECTOR_NAME>")
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

**Multiple Multi-vectors**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", "<QDRANT_GRPC_URL>")
   .option("collection_name", "<QDRANT_COLLECTION_NAME>")
   .option("multi_vector_fields", "<COLUMN_NAME>,<ANOTHER_COLUMN_NAME>")
   .option("multi_vector_names", "<MULTI_VECTOR_NAME>,<ANOTHER_MULTI_VECTOR_NAME>")
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

**No vectors - Entire dataframe is stored as payload**

```python
  <pyspark.sql.DataFrame>
   .write
   .format("io.qdrant.spark.Qdrant")
   .option("qdrant_url", "<QDRANT_GRPC_URL>")
   .option("collection_name", "<QDRANT_COLLECTION_NAME>")
   .option("schema", <pyspark.sql.DataFrame>.schema.json())
   .mode("append")
   .save()

```

## [Anchor](https://qdrant.tech/documentation/data-management/spark/\#databricks) Databricks

You can use the `qdrant-spark` connector as a library in [Databricks](https://www.databricks.com/).

- Go to the `Libraries` section in your Databricks cluster dashboard.
- Select `Install New` to open the library installation modal.
- Search for `io.qdrant:spark:VERSION` in the Maven packages and click `Install`.

![Databricks](https://qdrant.tech/documentation/frameworks/spark/databricks.png)

## [Anchor](https://qdrant.tech/documentation/data-management/spark/\#datatype-support) Datatype support

The appropriate Spark data types are mapped to the Qdrant payload based on the provided `schema`.

## [Anchor](https://qdrant.tech/documentation/data-management/spark/\#options-and-spark-types) Options and Spark types

| Option | Description | Column DataType | Required |
| --- | --- | --- | --- |
| `qdrant_url` | gRPC URL of the Qdrant instance. Eg: [http://localhost:6334](http://localhost:6334/) | - | ✅ |
| `collection_name` | Name of the collection to write data into | - | ✅ |
| `schema` | JSON string of the dataframe schema | - | ✅ |
| `embedding_field` | Name of the column holding the embeddings (Deprecated - Use `vector_fields` instead) | `ArrayType(FloatType)` | ❌ |
| `id_field` | Name of the column holding the point IDs. Default: Random UUID | `StringType` or `IntegerType` | ❌ |
| `batch_size` | Max size of the upload batch. Default: 64 | - | ❌ |
| `retries` | Number of upload retries. Default: 3 | - | ❌ |
| `api_key` | Qdrant API key for authentication | - | ❌ |
| `vector_name` | Name of the vector in the collection. | - | ❌ |
| `vector_fields` | Comma-separated names of columns holding the vectors. | `ArrayType(FloatType)` | ❌ |
| `vector_names` | Comma-separated names of vectors in the collection. | - | ❌ |
| `sparse_vector_index_fields` | Comma-separated names of columns holding the sparse vector indices. | `ArrayType(IntegerType)` | ❌ |
| `sparse_vector_value_fields` | Comma-separated names of columns holding the sparse vector values. | `ArrayType(FloatType)` | ❌ |
| `sparse_vector_names` | Comma-separated names of the sparse vectors in the collection. | - | ❌ |
| `multi_vector_fields` | Comma-separated names of columns holding the multi-vector values. | `ArrayType(ArrayType(FloatType))` | ❌ |
| `multi_vector_names` | Comma-separated names of the multi-vectors in the collection. | - | ❌ |
| `shard_key_selector` | Comma-separated names of custom shard keys to use during upsert. | - | ❌ |
| `wait` | Wait for each batch upsert to complete. `true` or `false`. Defaults to `true`. | - | ❌ |

For more information, be sure to check out the [Qdrant-Spark GitHub repository](https://github.com/qdrant/qdrant-spark). The Apache Spark guide is available [here](https://spark.apache.org/docs/latest/quick-start.html). Happy data processing!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/spark.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/spark.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574425513&cv=11&fst=1748574425513&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fspark%2F&hn=www.googleadservices.com&frm=0&tiba=Apache%20Spark%20-%20Qdrant&npa=0&pscdl=noapi&auid=978019491.1748574425&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574425493&cv=11&fst=1748574425493&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fspark%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Apache%20Spark%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=978019491.1748574425&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=a48d1ddd-6ccf-4e6b-8b0d-2161075f90ef&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=705f97da-4985-4722-8d99-3a20d97c4303&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fspark%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=a48d1ddd-6ccf-4e6b-8b0d-2161075f90ef&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=705f97da-4985-4722-8d99-3a20d97c4303&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fspark%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574426628&cv=11&fst=1748574426628&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fspark%2F&hn=www.googleadservices.com&frm=0&tiba=Apache%20Spark%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=978019491.1748574425&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)