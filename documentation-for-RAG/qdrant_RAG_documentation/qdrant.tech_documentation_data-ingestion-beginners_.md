---
url: "https://qdrant.tech/documentation/data-ingestion-beginners/"
title: "Data Ingestion for Beginners - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- Data Ingestion for Beginners

![data-ingestion-beginners-7](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-7.png)

# [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#send-s3-data-to-qdrant-vector-store-with-langchain) Send S3 Data to Qdrant Vector Store with LangChain

| Time: 30 min | Level: Beginner |  |  |
| --- | --- | --- | --- |

**Data ingestion into a vector store** is essential for building effective search and retrieval algorithms, especially since nearly 80% of data is unstructured, lacking any predefined format.

In this tutorial, we’ll create a streamlined data ingestion pipeline, pulling data directly from **AWS S3** and feeding it into Qdrant. We’ll dive into vector embeddings, transforming unstructured data into a format that allows you to search documents semantically. Prepare to discover new ways to uncover insights hidden within unstructured data!

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#ingestion-workflow-architecture) Ingestion Workflow Architecture

We’ll set up a powerful document ingestion and analysis pipeline in this workflow using cloud storage, natural language processing (NLP) tools, and embedding technologies. Starting with raw data in an S3 bucket, we’ll preprocess it with LangChain, apply embedding APIs for both text and images and store the results in Qdrant – a vector database optimized for similarity search.

**Figure 1: Data Ingestion Workflow Architecture**

![data-ingestion-beginners-5](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-5.png)

Let’s break down each component of this workflow:

- **S3 Bucket:** This is our starting point—a centralized, scalable storage solution for various file types like PDFs, images, and text.
- **LangChain:** Acting as the pipeline’s orchestrator, LangChain handles extraction, preprocessing, and manages data flow for embedding generation. It simplifies processing PDFs, so you won’t need to worry about applying OCR (Optical Character Recognition) here.
- **Qdrant:** As your vector database, Qdrant stores embeddings and their [payloads](https://qdrant.tech/documentation/concepts/payload/), enabling efficient similarity search and retrieval across all content types.

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#prerequisites) Prerequisites

![data-ingestion-beginners-11](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-11.png)

In this section, you’ll get a step-by-step guide on ingesting data from an S3 bucket. But before we dive in, let’s make sure you’re set up with all the prerequisites:

|  |  |
| --- | --- |
| Sample Data | We’ll use a sample dataset, where each folder includes product reviews in text format along with corresponding images. |
| AWS Account | An active [AWS account](https://aws.amazon.com/free/) with access to S3 services. |
| Qdrant Cloud | A [Qdrant Cloud account](https://cloud.qdrant.io/) with access to the WebUI for managing collections and running queries. |
| LangChain | You will use this [popular framework](https://www.langchain.com/) to tie everything together. |

#### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#supported-document-types) Supported Document Types

The documents used for ingestion can be of various types, such as PDFs, text files, or images. We will organize a structured S3 bucket with folders with the supported document types for testing and experimentation.

#### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#python-environment) Python Environment

Ensure you have a Python environment (Python 3.9 or higher) with these libraries installed:

```python
boto3
langchain-community
langchain
python-dotenv
unstructured
unstructured[pdf]
qdrant_client
fastembed

```

* * *

**Access Keys:** Store your AWS access key, S3 secret key, and Qdrant API key in a .env file for easy access. Here’s a sample `.env` file.

```text
ACCESS_KEY = ""
SECRET_ACCESS_KEY = ""
QDRANT_KEY = ""

```

* * *

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#step-1-ingesting-data-from-s3) Step 1: Ingesting Data from S3

![data-ingestion-beginners-9.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-9.png)

The LangChain framework makes it easy to ingest data from storage services like AWS S3, with built-in support for loading documents in formats such as PDFs, images, and text files.

To connect LangChain with S3, you’ll use the `S3DirectoryLoader`, which lets you load files directly from an S3 bucket into LangChain’s pipeline.

### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#example-configuring-langchain-to-load-files-from-s3) Example: Configuring LangChain to Load Files from S3

Here’s how to set up LangChain to ingest data from an S3 bucket:

```python
from langchain_community.document_loaders import S3DirectoryLoader

# Initialize the S3 document loader
loader = S3DirectoryLoader(
   "product-dataset",  # S3 bucket name
   "p_1", #S3 Folder name containing the data for the first product
   aws_access_key_id=aws_access_key_id,  # AWS Access Key
   aws_secret_access_key=aws_secret_access_key  # AWS Secret Access Key
)

# Load documents from the specified S3 bucket
docs = loader.load()

```

* * *

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#step-2-turning-documents-into-embeddings) Step 2. Turning Documents into Embeddings

[Embeddings](https://qdrant.tech/articles/what-are-embeddings/) are the secret sauce here—they’re numerical representations of data (like text, images, or audio) that capture the “meaning” in a form that’s easy to compare. By converting text and images into embeddings, you’ll be able to perform similarity searches quickly and efficiently. Think of embeddings as the bridge to storing and retrieving meaningful insights from your data in Qdrant.

### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#models-well-use-for-generating-embeddings) Models We’ll Use for Generating Embeddings

To get things rolling, we’ll use two powerful models:

1. **`sentence-transformers/all-MiniLM-L6-v2` Embeddings** for transforming text data.
2. **`CLIP` (Contrastive Language-Image Pretraining)** for image data.

* * *

### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#document-processing-function) Document Processing Function

![data-ingestion-beginners-8.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-8.png)

Next, we’ll define two functions — `process_text` and `process_image` to handle different file types in our document pipeline. The `process_text` function extracts and returns the raw content from a text-based document, while `process_image` retrieves an image from an S3 source and loads it into memory.

```python
from PIL import Image

def process_text(doc):
    source = doc.metadata['source']  # Extract document source (e.g., S3 URL)

    text = doc.page_content  # Extract the content from the text file
    print(f"Processing text from {source}")
    return source, text

def process_image(doc):
    source = doc.metadata['source']  # Extract document source (e.g., S3 URL)
    print(f"Processing image from {source}")

    bucket_name, object_key = parse_s3_url(source)  # Parse the S3 URL
    response = s3.get_object(Bucket=bucket_name, Key=object_key)  # Fetch image from S3
    img_bytes = response['Body'].read()

    img = Image.open(io.BytesIO(img_bytes))
    return source, img

```

### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#helper-functions-for-document-processing) Helper Functions for Document Processing

To retrieve images from S3, a helper function `parse_s3_url` breaks down the S3 URL into its bucket and critical components. This is essential for fetching the image from S3 storage.

```python
def parse_s3_url(s3_url):
    parts = s3_url.replace("s3://", "").split("/", 1)
    bucket_name = parts[0]
    object_key = parts[1]
    return bucket_name, object_key

```

* * *

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#step-3-loading-embeddings-into-qdrant) Step 3: Loading Embeddings into Qdrant

![data-ingestion-beginners-10](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-10.png)

Now that your documents have been processed and converted into embeddings, the next step is to load these embeddings into Qdrant.

### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#creating-a-collection-in-qdrant) Creating a Collection in Qdrant

In Qdrant, data is organized in collections, each representing a set of embeddings (or points) and their associated metadata (payload). To store the embeddings generated earlier, you’ll first need to create a collection.

Here’s how to create a collection in Qdrant to store both text and image embeddings:

```python
def create_collection(collection_name):
    qdrant_client.create_collection(
        collection_name,
        vectors_config={
            "text_embedding": models.VectorParams(
                size=384,  # Dimension of text embeddings
                distance=models.Distance.COSINE,  # Cosine similarity is used for comparison
            ),
            "image_embedding": models.VectorParams(
                size=512,  # Dimension of image embeddings
                distance=models.Distance.COSINE,  # Cosine similarity is used for comparison
            ),
        },
    )

create_collection("products-data")

```

* * *

This function creates a collection for storing text (384 dimensions) and image (512 dimensions) embeddings, using cosine similarity to compare embeddings within the collection.

Once the collection is set up, you can load the embeddings into Qdrant. This involves inserting (or updating) the embeddings and their associated metadata (payload) into the specified collection.

Here’s the code for loading embeddings into Qdrant:

```python
def ingest_data(points):
    operation_info = qdrant_client.upsert(
        collection_name="products-data",  # Collection where data is being inserted
        points=points
    )
    return operation_info

```

* * *

**Explanation of Ingestion**

1. **Upserting the Data Point:** The upsert method on the `qdrant_client` inserts each PointStruct into the specified collection. If a point with the same ID already exists, it will be updated with the new values.
2. **Operation Info:** The function returns `operation_info`, which contains details about the upsert operation, such as success status or any potential errors.

**Running the Ingestion Code**

Here’s how to call the function and ingest data:

```python
from qdrant_client import models

if __name__ == "__main__":
    collection_name = "products-data"
    create_collection(collection_name)
    for i in range(1,6): # Five documents
        folder = f"p_{i}"
        loader = S3DirectoryLoader(
            "product-dataset",
            folder,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        docs = loader.load()
        points, text_review, product_image = [], "", ""
        for idx, doc in enumerate(docs):
            source = doc.metadata['source']
            if source.endswith(".txt") or source.endswith(".pdf"):
                _text_review_source, text_review = process_text(doc)
            elif source.endswith(".png"):
                product_image_source, product_image = process_image(doc)
        if text_review:
            point = models.PointStruct(
                id=idx,  # Unique identifier for each point
                vector={
                    "text_embedding": models.Document(
                        text=text_review, model="sentence-transformers/all-MiniLM-L6-v2"
                    ),
                    "image_embedding": models.Image(
                        image=product_image, model="Qdrant/clip-ViT-B-32-vision"
                    ),
                },
                payload={"review": text_review, "product_image": product_image_source},
            )
            points.append(point)
    operation_info = ingest_data(points)
    print(operation_info)

```

The `PointStruct` is instantiated with these key parameters:

- **id:** A unique identifier for each embedding, typically an incremental index.

- **vector:** A dictionary holding the text and image inputs to be embedded. `qdrant-client` uses [FastEmbed](https://github.com/qdrant/fastembed) under the hood to automatically generate vector representations from these inputs locally.

- **payload:** A dictionary storing additional metadata, like product reviews and image references, which is invaluable for retrieval and context during searches.


The code dynamically loads folders from an S3 bucket, processes text and image files separately, and stores their embeddings and associated data in dedicated lists. It then creates a `PointStruct` for each data entry and calls the ingestion function to load it into Qdrant.

### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#exploring-the-qdrant-webui-dashboard) Exploring the Qdrant WebUI Dashboard

Once the embeddings are loaded into Qdrant, you can use the WebUI dashboard to visualize and manage your collections. The dashboard provides a clear, structured interface for viewing collections and their data. Let’s take a closer look in the next section.

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#step-4-visualizing-data-in-qdrant-webui) Step 4: Visualizing Data in Qdrant WebUI

To start visualizing your data in the Qdrant WebUI, head to the **Overview** section and select **Access the database**.

**Figure 2: Accessing the Database from the Qdrant UI**![data-ingestion-beginners-2.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-2.png)

When prompted, enter your API key. Once inside, you’ll be able to view your collections and the corresponding data points. You should see your collection displayed like this:

**Figure 3: The product-data Collection in Qdrant**![data-ingestion-beginners-4.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-4.png)

Here’s a look at the most recent point ingested into Qdrant:

**Figure 4: The Latest Point Added to the product-data Collection**![data-ingestion-beginners-6.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-6.png)

The Qdrant WebUI’s search functionality allows you to perform vector searches across your collections. With options to apply filters and parameters, retrieving relevant embeddings and exploring relationships within your data becomes easy. To start, head over to the **Console** in the left panel, where you can create queries:

**Figure 5: Overview of Console in Qdrant**![data-ingestion-beginners-1.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-1.png)

The first query retrieves all collections, the second fetches points from the product-data collection, and the third performs a sample query. This demonstrates how straightforward it is to interact with your data in the Qdrant UI.

Now, let’s retrieve some documents from the database using a query!.

**Figure 6: Querying the Qdrant Client to Retrieve Relevant Documents**![data-ingestion-beginners-3.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-3.png)

In this example, we queried **Phones with improved design**. Then, we converted the text to vectors using OpenAI and retrieved a relevant phone review highlighting design improvements.

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#conclusion) Conclusion

In this guide, we set up an S3 bucket, ingested various data types, and stored embeddings in Qdrant. Using LangChain, we dynamically processed text and image files, making it easy to work with each file type.

Now, it’s your turn. Try experimenting with different data types, such as videos, and explore Qdrant’s advanced features to enhance your applications. To get started, [sign up](https://cloud.qdrant.io/signup?ajs_anonymous_id=c9b80369-4e73-42c3-9948-b22580c7d0ad) for Qdrant today.

![data-ingestion-beginners-12](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-12.png)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-ingestion-beginners.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-ingestion-beginners.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f296d14e-21c1-4ad2-b324-ec5f763d5d77&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3f3e8b7d-ae8d-4e56-9837-3d57b2d98c46&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-ingestion-beginners%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573922229&cv=11&fst=1748573922229&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-ingestion-beginners%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Data%20Ingestion%20for%20Beginners%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1893448060.1748573920&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573922241&cv=11&fst=1748573922241&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-ingestion-beginners%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Data%20Ingestion%20for%20Beginners%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1893448060.1748573920&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573922216&cv=11&fst=1748573922216&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-ingestion-beginners%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Data%20Ingestion%20for%20Beginners%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1893448060.1748573920&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f296d14e-21c1-4ad2-b324-ec5f763d5d77&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3f3e8b7d-ae8d-4e56-9837-3d57b2d98c46&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-ingestion-beginners%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)