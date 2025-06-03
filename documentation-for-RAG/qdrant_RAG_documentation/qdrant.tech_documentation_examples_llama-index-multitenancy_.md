---
url: "https://qdrant.tech/documentation/examples/llama-index-multitenancy/"
title: "Multitenancy with LlamaIndex - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Multitenancy with LlamaIndex

# [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#multitenancy-with-llamaindex) Multitenancy with LlamaIndex

If you are building a service that serves vectors for many independent users, and you want to isolate their
data, the best practice is to use a single collection with payload-based partitioning. This approach is
called **multitenancy**. Our guide on the [Separate Partitions](https://qdrant.tech/documentation/guides/multiple-partitions/) describes
how to set it up in general, but if you use [LlamaIndex](https://qdrant.tech/documentation/integrations/llama-index/) as a
backend, you may prefer reading a more specific instruction. So here it is!

## [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#prerequisites) Prerequisites

This tutorial assumes that you have already installed Qdrant and LlamaIndex. If you haven’t, please run the
following commands:

```bash
pip install llama-index llama-index-vector-stores-qdrant

```

We are going to use a local Docker-based instance of Qdrant. If you want to use a remote instance, please
adjust the code accordingly. Here is how we can start a local instance:

```bash
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant:latest

```

## [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#setting-up-llamaindex-pipeline) Setting up LlamaIndex pipeline

We are going to implement an end-to-end example of multitenant application using LlamaIndex. We’ll be
indexing the documentation of different Python libraries, and we definitely don’t want any users to see the
results coming from a library they are not interested in. In real case scenarios, this is even more dangerous,
as the documents may contain sensitive information.

### [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#creating-vector-store) Creating vector store

[QdrantVectorStore](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo.html) is a
wrapper around Qdrant that provides all the necessary methods to work with your vector database in LlamaIndex.
Let’s create a vector store for our collection. It requires setting a collection name and passing an instance
of `QdrantClient`.

```python
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore

client = QdrantClient("http://localhost:6333")

vector_store = QdrantVectorStore(
    collection_name="my_collection",
    client=client,
)

```

### [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#defining-chunking-strategy-and-embedding-model) Defining chunking strategy and embedding model

Any semantic search application requires a way to convert text queries into vectors - an embedding model.
`ServiceContext` is a bundle of commonly used resources used during the indexing and querying stage in any
LlamaIndex application. We can also use it to set up an embedding model - in our case, a local
[BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5).
set up

```python
from llama_index.core import ServiceContext

service_context = ServiceContext.from_defaults(
    embed_model="local:BAAI/bge-small-en-v1.5",
)

```

_Note_, in case you are using Large Language Model different from OpenAI’s ChatGPT, you should specify
`llm` parameter for `ServiceContext`.

We can also control how our documents are split into chunks, or nodes using LLamaIndex’s terminology.
The `SimpleNodeParser` splits documents into fixed length chunks with an overlap. The defaults are
reasonable, but we can also adjust them if we want to. Both values are defined in tokens.

```python
from llama_index.core.node_parser import SimpleNodeParser

node_parser = SimpleNodeParser.from_defaults(chunk_size=512, chunk_overlap=32)

```

Now we also need to inform the `ServiceContext` about our choices:

```python
service_context = ServiceContext.from_defaults(
    embed_model="local:BAAI/bge-large-en-v1.5",
    node_parser=node_parser,
)

```

Both embedding model and selected node parser will be implicitly used during the indexing and querying.

### [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#combining-everything-together) Combining everything together

The last missing piece, before we can start indexing, is the `VectorStoreIndex`. It is a wrapper around
`VectorStore` that provides a convenient interface for indexing and querying. It also requires a
`ServiceContext` to be initialized.

```python
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, service_context=service_context
)

```

## [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#indexing-documents) Indexing documents

No matter how our documents are generated, LlamaIndex will automatically split them into nodes, if
required, encode using selected embedding model, and then store in the vector store. Let’s define
some documents manually and insert them into Qdrant collection. Our documents are going to have
a single metadata attribute - a library name they belong to.

```python
from llama_index.core.schema import Document

documents = [\
    Document(\
        text="LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models.",\
        metadata={\
            "library": "llama-index",\
        },\
    ),\
    Document(\
        text="Qdrant is a vector database & vector similarity search engine.",\
        metadata={\
            "library": "qdrant",\
        },\
    ),\
]

```

Now we can index them using our `VectorStoreIndex`:

```python
for document in documents:
    index.insert(document)

```

### [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#performance-considerations) Performance considerations

Our documents have been split into nodes, encoded using the embedding model, and stored in the vector
store. However, we don’t want to allow our users to search for all the documents in the collection,
but only for the documents that belong to a library they are interested in. For that reason, we need
to set up the Qdrant [payload index](https://qdrant.tech/documentation/concepts/indexing/#payload-index), so the search
is more efficient.

```python
from qdrant_client import models

client.create_payload_index(
    collection_name="my_collection",
    field_name="metadata.library",
    field_type=models.PayloadSchemaType.KEYWORD,
)

```

The payload index is not the only thing we want to change. Since none of the search
queries will be executed on the whole collection, we can also change its configuration, so the HNSW
graph is not built globally. This is also done due to [performance reasons](https://qdrant.tech/documentation/guides/multiple-partitions/#calibrate-performance).
**You should not be changing these parameters, if you know there will be some global search operations**
**done on the collection.**

```python
client.update_collection(
    collection_name="my_collection",
    hnsw_config=models.HnswConfigDiff(payload_m=16, m=0),
)

```

Once both operations are completed, we can start searching for our documents.

## [Anchor](https://qdrant.tech/documentation/examples/llama-index-multitenancy/\#querying-documents-with-constraints) Querying documents with constraints

Let’s assume we are searching for some information about large language models, but are only allowed to
use Qdrant documentation. LlamaIndex has a concept of retrievers, responsible for finding the most
relevant nodes for a given query. Our `VectorStoreIndex` can be used as a retriever, with some additional
constraints - in our case value of the `library` metadata attribute.

```python
from llama_index.core.vector_stores.types import MetadataFilters, ExactMatchFilter

qdrant_retriever = index.as_retriever(
    filters=MetadataFilters(
        filters=[\
            ExactMatchFilter(\
                key="library",\
                value="qdrant",\
            )\
        ]
    )
)

nodes_with_scores = qdrant_retriever.retrieve("large language models")
for node in nodes_with_scores:
    print(node.text, node.score)
# Output: Qdrant is a vector database & vector similarity search engine. 0.60551536

```

The description of Qdrant was the best match, even though it didn’t mention large language models
at all. However, it was the only document that belonged to the `qdrant` library, so there was no
other choice. Let’s try to search for something that is not present in the collection.

Let’s define another retrieve, this time for the `llama-index` library:

```python
llama_index_retriever = index.as_retriever(
    filters=MetadataFilters(
        filters=[\
            ExactMatchFilter(\
                key="library",\
                value="llama-index",\
            )\
        ]
    )
)

nodes_with_scores = llama_index_retriever.retrieve("large language models")
for node in nodes_with_scores:
    print(node.text, node.score)
# Output: LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models. 0.63576734

```

The results returned by both retrievers are different, due to the different constraints, so we implemented
a real multitenant search application!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/llama-index-multitenancy.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/llama-index-multitenancy.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573695083&cv=11&fst=1748573695083&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fllama-index-multitenancy%2F&hn=www.googleadservices.com&frm=0&tiba=Multitenancy%20with%20LlamaIndex%20-%20Qdrant&npa=0&pscdl=noapi&auid=2032165385.1748573695&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573695040&cv=11&fst=1748573695040&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308614&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fllama-index-multitenancy%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Multitenancy%20with%20LlamaIndex%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2032165385.1748573695&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=76cf580e-d87d-4233-b9da-d467df0a20c2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ef390f88-a05a-4a07-b5df-0cd6e0355247&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fllama-index-multitenancy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=76cf580e-d87d-4233-b9da-d467df0a20c2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ef390f88-a05a-4a07-b5df-0cd6e0355247&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fllama-index-multitenancy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573696110&cv=11&fst=1748573696110&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fllama-index-multitenancy%2F&hn=www.googleadservices.com&frm=0&tiba=Multitenancy%20with%20LlamaIndex%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2032165385.1748573695&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)