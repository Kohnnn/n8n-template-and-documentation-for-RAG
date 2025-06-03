---
url: "https://qdrant.tech/articles/fastembed/"
title: "FastEmbed: Qdrant's Efficient Python Library for Embedding Generation - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- FastEmbed: Qdrant's Efficient Python Library for Embedding Generation

[Back to Ecosystem](https://qdrant.tech/articles/ecosystem/)

# FastEmbed: Qdrant's Efficient Python Library for Embedding Generation

Nirant Kasliwal

·

October 18, 2023

![FastEmbed: Qdrant's Efficient Python Library for Embedding Generation](https://qdrant.tech/articles_data/fastembed/preview/title.jpg)

Data Science and Machine Learning practitioners often find themselves navigating through a labyrinth of models, libraries, and frameworks. Which model to choose, what embedding size, and how to approach tokenizing, are just some questions you are faced with when starting your work. We understood how many data scientists wanted an easier and more intuitive means to do their embedding work. This is why we built FastEmbed, a Python library engineered for speed, efficiency, and usability. We have created easy to use default workflows, handling the 80% use cases in NLP embedding.

## [Anchor](https://qdrant.tech/articles/fastembed/\#current-state-of-affairs-for-generating-embeddings) Current State of Affairs for Generating Embeddings

Usually you make embedding by utilizing PyTorch or TensorFlow models under the hood. However, using these libraries comes at a cost in terms of ease of use and computational speed. This is at least in part because these are built for both: model inference and improvement e.g. via fine-tuning.

To tackle these problems we built a small library focused on the task of quickly and efficiently creating text embeddings. We also decided to start with only a small sample of best in class transformer models. By keeping it small and focused on a particular use case, we could make our library focused without all the extraneous dependencies. We ship with limited models, quantize the model weights and seamlessly integrate them with the ONNX Runtime. FastEmbed strikes a balance between inference time, resource utilization and performance (recall/accuracy).

## [Anchor](https://qdrant.tech/articles/fastembed/\#quick-embedding-text-document-example) Quick Embedding Text Document Example

Here is an example of how simple we have made embedding text documents:

```python
documents: List[str] = [\
    "Hello, World!",\
    "fastembed is supported by and maintained by Qdrant."\
]
embedding_model = DefaultEmbedding()
embeddings: List[np.ndarray] = list(embedding_model.embed(documents))

```

These 3 lines of code do a lot of heavy lifting for you: They download the quantized model, load it using ONNXRuntime, and then run a batched embedding creation of your documents.

### [Anchor](https://qdrant.tech/articles/fastembed/\#code-walkthrough) Code Walkthrough

Let’s delve into a more advanced example code snippet line-by-line:

```python
from fastembed.embedding import DefaultEmbedding

```

Here, we import the FlagEmbedding class from FastEmbed and alias it as Embedding. This is the core class responsible for generating embeddings based on your chosen text model. This is also the class which you can import directly as DefaultEmbedding which is [BAAI/bge-small-en-v1.5](https://huggingface.co/baai/bge-small-en-v1.5)

```python
documents: List[str] = [\
    "passage: Hello, World!",\
    "query: How is the World?",\
    "passage: This is an example passage.",\
    "fastembed is supported by and maintained by Qdrant."\
]

```

In this list called documents, we define four text strings that we want to convert into embeddings.

Note the use of prefixes “passage” and “query” to differentiate the types of embeddings to be generated. This is inherited from the cross-encoder implementation of the BAAI/bge series of models themselves. This is particularly useful for retrieval and we strongly recommend using this as well.

The use of text prefixes like “query” and “passage” isn’t merely syntactic sugar; it informs the algorithm on how to treat the text for embedding generation. A “query” prefix often triggers the model to generate embeddings that are optimized for similarity comparisons, while “passage” embeddings are fine-tuned for contextual understanding. If you omit the prefix, the default behavior is applied, although specifying it is recommended for more nuanced results.

Next, we initialize the Embedding model with the default model: [BAAI/bge-small-en-v1.5](https://huggingface.co/baai/bge-small-en-v1.5).

```python
embedding_model = DefaultEmbedding()

```

The default model and several other models have a context window of a maximum of 512 tokens. This maximum limit comes from the embedding model training and design itself. If you’d like to embed sequences larger than that, we’d recommend using some pooling strategy to get a single vector out of the sequence. For example, you can use the mean of the embeddings of different chunks of a document. This is also what the [SBERT Paper recommends](https://lilianweng.github.io/posts/2021-05-31-contrastive/#sentence-bert)

This model strikes a balance between speed and accuracy, ideal for real-world applications.

```python
embeddings: List[np.ndarray] = list(embedding_model.embed(documents))

```

Finally, we call the `embed()` method on our embedding\_model object, passing in the documents list. The method returns a Python generator, so we convert it to a list to get all the embeddings. These embeddings are NumPy arrays, optimized for fast mathematical operations.

The `embed()` method returns a list of NumPy arrays, each corresponding to the embedding of a document in your original documents list. The dimensions of these arrays are determined by the model you chose e.g. for “BAAI/bge-small-en-v1.5” it’s a 384-dimensional vector.

You can easily parse these NumPy arrays for any downstream application—be it clustering, similarity comparison, or feeding them into a machine learning model for further analysis.

## [Anchor](https://qdrant.tech/articles/fastembed/\#3-key-features-of-fastembed) 3 Key Features of FastEmbed

FastEmbed is built for inference speed, without sacrificing (too much) performance:

1. 50% faster than PyTorch Transformers
2. Better performance than Sentence Transformers and OpenAI Ada-002
3. Cosine similarity of quantized and original model vectors is 0.92

We use `BAAI/bge-small-en-v1.5` as our DefaultEmbedding, hence we’ve chosen that for comparison:

![](https://qdrant.tech/articles_data/fastembed/throughput.png)

## [Anchor](https://qdrant.tech/articles/fastembed/\#under-the-hood-of-fastembed) Under the Hood of FastEmbed

**Quantized Models**: We quantize the models for CPU (and Mac Metal) – giving you the best buck for your compute model. Our default model is so small, you can run this in AWS Lambda if you’d like!

Shout out to Huggingface’s [Optimum](https://github.com/huggingface/optimum) – which made it easier to quantize models.

**Reduced Installation Time**:

FastEmbed sets itself apart by maintaining a low minimum RAM/Disk usage.

It’s designed to be agile and fast, useful for businesses looking to integrate text embedding for production usage. For FastEmbed, the list of dependencies is refreshingly brief:

> - onnx: Version ^1.11 – We’ll try to drop this also in the future if we can!
> - onnxruntime: Version ^1.15
> - tqdm: Version ^4.65 – used only at Download
> - requests: Version ^2.31 – used only at Download
> - tokenizers: Version ^0.13

This minimized list serves two purposes. First, it significantly reduces the installation time, allowing for quicker deployments. Second, it limits the amount of disk space required, making it a viable option even for environments with storage limitations.

Notably absent from the dependency list are bulky libraries like PyTorch, and there’s no requirement for CUDA drivers. This is intentional. FastEmbed is engineered to deliver optimal performance right on your CPU, eliminating the need for specialized hardware or complex setups.

**ONNXRuntime**: The ONNXRuntime gives us the ability to support multiple providers. The quantization we do is limited for CPU (Intel), but we intend to support GPU versions of the same in the future as well.  This allows for greater customization and optimization, further aligning with your specific performance and computational requirements.

## [Anchor](https://qdrant.tech/articles/fastembed/\#current-models) Current Models

We’ve started with a small set of supported models:

All the models we support are [quantized](https://pytorch.org/docs/stable/quantization.html) to enable even faster computation!

If you’re using FastEmbed and you’ve got ideas or need certain features, feel free to let us know. Just drop an issue on our GitHub page. That’s where we look first when we’re deciding what to work on next. Here’s where you can do it: [FastEmbed GitHub Issues](https://github.com/qdrant/fastembed/issues).

When it comes to FastEmbed’s DefaultEmbedding model, we’re committed to supporting the best Open Source models.

If anything changes, you’ll see a new version number pop up, like going from 0.0.6 to 0.1. So, it’s a good idea to lock in the FastEmbed version you’re using to avoid surprises.

## [Anchor](https://qdrant.tech/articles/fastembed/\#using-fastembed-with-qdrant) Using FastEmbed with Qdrant

Qdrant is a Vector Store, offering comprehensive, efficient, and scalable [enterprise solutions](https://qdrant.tech/enterprise-solutions/) for modern machine learning and AI applications. Whether you are dealing with billions of data points, require a low latency performant [vector database solution](https://qdrant.tech/qdrant-vector-database/), or specialized quantization methods – [Qdrant is engineered](https://qdrant.tech/documentation/overview/) to meet those demands head-on.

The fusion of FastEmbed with Qdrant’s vector store capabilities enables a transparent workflow for seamless embedding generation, storage, and retrieval. This simplifies the API design — while still giving you the flexibility to make significant changes e.g. you can use FastEmbed to make your own embedding other than the DefaultEmbedding and use that with Qdrant.

Below is a detailed guide on how to get started with FastEmbed in conjunction with Qdrant.

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-1-installation) Step 1: Installation

Before diving into the code, the initial step involves installing the Qdrant Client along with the FastEmbed library. This can be done using pip:

```
pip install qdrant-client[fastembed]

```

For those using zsh as their shell, you might encounter syntax issues. In such cases, wrap the package name in quotes:

```
pip install 'qdrant-client[fastembed]'

```

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-2-initializing-the-qdrant-client) Step 2: Initializing the Qdrant Client

After successful installation, the next step involves initializing the Qdrant Client. This can be done either in-memory or by specifying a database path:

```python
from qdrant_client import QdrantClient
# Initialize the client
client = QdrantClient(":memory:")  # or QdrantClient(path="path/to/db")

```

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-3-preparing-documents-metadata-and-ids) Step 3: Preparing Documents, Metadata, and IDs

Once the client is initialized, prepare the text documents you wish to embed, along with any associated metadata and unique IDs:

```python
docs = [\
    "Qdrant has Langchain integrations",\
    "Qdrant also has Llama Index integrations"\
]
metadata = [\
    {"source": "Langchain-docs"},\
    {"source": "LlamaIndex-docs"},\
]
ids = [42, 2]

```

Note that the add method we’ll use is overloaded: If you skip the ids, we’ll generate those for you. metadata is obviously optional. So, you can simply use this too:

```python
docs = [\
    "Qdrant has Langchain integrations",\
    "Qdrant also has Llama Index integrations"\
]

```

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-4-adding-documents-to-a-collection) Step 4: Adding Documents to a Collection

With your documents, metadata, and IDs ready, you can proceed to add these to a specified collection within Qdrant using the add method:

```python
client.add(
    collection_name="demo_collection",
    documents=docs,
    metadata=metadata,
    ids=ids
)

```

Inside this function, Qdrant Client uses FastEmbed to make the text embedding, generate ids if they’re missing, and then add them to the index with metadata. This uses the DefaultEmbedding model: [BAAI/bge-small-en-v1.5](https://huggingface.co/baai/bge-small-en-v1.5)

![INDEX TIME: Sequence Diagram for Qdrant and FastEmbed](https://qdrant.tech/articles_data/fastembed/generate-embeddings-from-docs.png)

### [Anchor](https://qdrant.tech/articles/fastembed/\#step-5-performing-queries) Step 5: Performing Queries

Finally, you can perform queries on your stored documents. Qdrant offers a robust querying capability, and the query results can be easily retrieved as follows:

```python
search_result = client.query(
    collection_name="demo_collection",
    query_text="This is a query document"
)
print(search_result)

```

Behind the scenes, we first convert the query\_text to the embedding and use that to query the vector index.

![QUERY TIME: Sequence Diagram for Qdrant and FastEmbed integration](https://qdrant.tech/articles_data/fastembed/generate-embeddings-query.png)

By following these steps, you effectively utilize the combined capabilities of FastEmbed and Qdrant, thereby streamlining your embedding generation and retrieval tasks.

Qdrant is designed to handle large-scale datasets with billions of data points. Its architecture employs techniques like [binary quantization](https://qdrant.tech/articles/binary-quantization/) and [scalar quantization](https://qdrant.tech/articles/scalar-quantization/) for efficient storage and retrieval. When you inject FastEmbed’s CPU-first design and lightweight nature into this equation, you end up with a system that can scale seamlessly while maintaining low latency.

## [Anchor](https://qdrant.tech/articles/fastembed/\#summary) Summary

If you’re curious about how FastEmbed and Qdrant can make your search tasks a breeze, why not take it for a spin? You get a real feel for what it can do. Here are two easy ways to get started:

1. **Cloud**: Get started with a free plan on the [Qdrant Cloud](https://qdrant.to/cloud?utm_source=qdrant&utm_medium=website&utm_campaign=fastembed&utm_content=article).

2. **Docker Container**: If you’re the DIY type, you can set everything up on your own machine. Here’s a quick guide to help you out: [Quick Start with Docker](https://qdrant.tech/documentation/quick-start/?utm_source=qdrant&utm_medium=website&utm_campaign=fastembed&utm_content=article).


So, go ahead, take it for a test drive. We’re excited to hear what you think!

Lastly, If you find FastEmbed useful and want to keep up with what we’re doing, giving our GitHub repo a star would mean a lot to us. Here’s the link to [star the repository](https://github.com/qdrant/fastembed).

If you ever have questions about FastEmbed, please ask them on the Qdrant Discord: [https://discord.gg/Qy6HCJK9Dc](https://discord.gg/Qy6HCJK9Dc)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/fastembed.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/fastembed.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575085840&cv=11&fst=1748575085840&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffastembed%2F&hn=www.googleadservices.com&frm=0&tiba=FastEmbed%3A%20Qdrant's%20Efficient%20Python%20Library%20for%20Embedding%20Generation%20-%20Qdrant&npa=0&pscdl=noapi&auid=434287649.1748575086&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575085821&cv=11&fst=1748575085821&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffastembed%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=FastEmbed%3A%20Qdrant's%20Efficient%20Python%20Library%20for%20Embedding%20Generation%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=434287649.1748575086&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=77fa9fe1-e57f-46a3-bcf3-0cbcf3707fc4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9adf04b7-037d-4ebf-a2b4-865d60013452&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffastembed%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=77fa9fe1-e57f-46a3-bcf3-0cbcf3707fc4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9adf04b7-037d-4ebf-a2b4-865d60013452&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffastembed%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575087397&cv=11&fst=1748575087397&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffastembed%2F&hn=www.googleadservices.com&frm=0&tiba=FastEmbed%3A%20Qdrant's%20Efficient%20Python%20Library%20for%20Embedding%20Generation%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=434287649.1748575086&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)