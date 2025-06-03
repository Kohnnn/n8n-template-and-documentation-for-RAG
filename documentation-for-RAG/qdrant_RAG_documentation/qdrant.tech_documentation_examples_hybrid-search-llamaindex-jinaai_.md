---
url: "https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/"
title: "Chat With Product PDF Manuals Using Hybrid Search - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Chat With Product PDF Manuals Using Hybrid Search

# [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#chat-with-product-pdf-manuals-using-hybrid-search) Chat With Product PDF Manuals Using Hybrid Search

| Time: 120 min | Level: Advanced | Output: [GitHub](https://github.com/infoslack/qdrant-example/blob/main/HC-demo/HC-DO-LlamaIndex-Jina-v2.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/infoslack/qdrant-example/blob/main/HC-demo/HC-DO-LlamaIndex-Jina-v2.ipynb) |
| --- | --- | --- | --- |

With the proliferation of digital manuals and the increasing demand for quick and accurate customer support, having a chatbot capable of efficiently parsing through complex PDF documents and delivering precise information can be a game-changer for any business.

In this tutorial, we’ll walk you through the process of building a RAG-based chatbot, designed specifically to assist users with understanding the operation of various household appliances.
We’ll cover the essential steps required to build your system, including data ingestion, natural language understanding, and response generation for customer support use cases.

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#components) Components

- **Embeddings:** Jina Embeddings, served via the [Jina Embeddings API](https://jina.ai/embeddings/#apiform)
- **Database:** [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/), deployed in a managed Kubernetes cluster on [DigitalOcean\\
(DOKS)](https://www.digitalocean.com/products/kubernetes)
- **LLM:** [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) language model on HuggingFace
- **Framework:** [LlamaIndex](https://www.llamaindex.ai/) for extended RAG functionality and [Hybrid Search support](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/).
- **Parser:** [LlamaParse](https://github.com/run-llama/llama_parse) as a way to parse complex documents with embedded objects such as tables and figures.

![Architecture diagram](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/architecture-diagram.png)

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#procedure) Procedure

Retrieval Augmented Generation (RAG) combines search with language generation. An external information retrieval system is used to identify documents likely to provide information relevant to the user’s query. These documents, along with the user’s request, are then passed on to a text-generating language model, producing a natural response.

This method enables a language model to respond to questions and access information from a much larger set of documents than it could see otherwise. The language model only looks at a few relevant sections of the documents when generating responses, which also helps to reduce inexplicable errors.

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#heading)

[Service Managed Kubernetes](https://www.ovhcloud.com/en-in/public-cloud/kubernetes/), powered by OVH Public Cloud Instances, a leading European cloud provider. With OVHcloud Load Balancers and disks built in. OVHcloud Managed Kubernetes provides high availability, compliance, and CNCF conformance, allowing you to focus on your containerized software layers with total reversibility.

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#prerequisites) Prerequisites

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#deploying-qdrant-hybrid-cloud-on-digitalocean) Deploying Qdrant Hybrid Cloud on DigitalOcean

[DigitalOcean Kubernetes (DOKS)](https://www.digitalocean.com/products/kubernetes) is a managed Kubernetes service that lets you deploy Kubernetes clusters without the complexities of handling the control plane and containerized infrastructure. Clusters are compatible with standard Kubernetes toolchains and integrate natively with DigitalOcean Load Balancers and volumes.

1. To start using managed Kubernetes on DigitalOcean, follow the [platform-specific documentation](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/#digital-ocean).
2. Once your Kubernetes clusters are up, [you can begin deploying Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/).
3. Once it’s deployed, you should have a running Qdrant cluster with an API key.

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#development-environment) Development environment

Then, install all dependencies:

```python
!pip install -U  \
    llama-index  \
    llama-parse \
    python-dotenv \
    llama-index-embeddings-jinaai  \
    llama-index-llms-huggingface  \
    llama-index-vector-stores-qdrant  \
    "huggingface_hub[inference]"  \
    datasets

```

Set up secret key values on `.env` file:

```bash
JINAAI_API_KEY
HF_INFERENCE_API_KEY
LLAMA_CLOUD_API_KEY
QDRANT_HOST
QDRANT_API_KEY

```

Load all environment variables:

```python
import os
from dotenv import load_dotenv
load_dotenv('./.env')

```

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#implementation) Implementation

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#connect-jina-embeddings-and-mixtral-llm) Connect Jina Embeddings and Mixtral LLM

LlamaIndex provides built-in support for the [Jina Embeddings API](https://jina.ai/embeddings/#apiform). To use it, you need to initialize the `JinaEmbedding` object with your API Key and model name.

For the LLM, you need wrap it in a subclass of `llama_index.llms.CustomLLM` to make it compatible with LlamaIndex.

```python
# connect embeddings
from llama_index.embeddings.jinaai import JinaEmbedding

jina_embedding_model = JinaEmbedding(
    model="jina-embeddings-v2-base-en",
    api_key=os.getenv("JINAAI_API_KEY"),
)

# connect LLM
from llama_index.llms.huggingface import HuggingFaceInferenceAPI

mixtral_llm = HuggingFaceInferenceAPI(
    model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=os.getenv("HF_INFERENCE_API_KEY"),
)

```

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#prepare-data-for-rag) Prepare data for RAG

This example will use household appliance manuals, which are generally available as PDF documents.
LlamaPar
In the `data` folder, we have three documents, and we will use it to extract the textual content from the PDF and use it as a knowledge base in a simple RAG.

The free LlamaIndex Cloud plan is sufficient for our example:

```python
import nest_asyncio
nest_asyncio.apply()
from llama_parse import LlamaParse

llamaparse_api_key = os.getenv("LLAMA_CLOUD_API_KEY")

llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data([\
    "data/DJ68-00682F_0.0.pdf",\
    "data/F500E_WF80F5E_03445F_EN.pdf",\
    "data/O_ME4000R_ME19R7041FS_AA_EN.pdf"\
])

```

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#store-data-into-qdrant) Store data into Qdrant

The code below does the following:

- create a vector store with Qdrant client;
- get an embedding for each chunk using Jina Embeddings API;
- combines `sparse` and `dense` vectors for hybrid search;
- stores all data into Qdrant;

Hybrid search with Qdrant must be enabled from the beginning - we can simply set `enable_hybrid=True`.

```python
# By default llamaindex uses OpenAI models
# setting embed_model to Jina and llm model to Mixtral
from llama_index.core import Settings
Settings.embed_model = jina_embedding_model
Settings.llm = mixtral_llm

from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client

client = qdrant_client.QdrantClient(
    url=os.getenv("QDRANT_HOST"),
    api_key=os.getenv("QDRANT_API_KEY")
)

vector_store = QdrantVectorStore(
    client=client, collection_name="demo", enable_hybrid=True, batch_size=20
)
Settings.chunk_size = 512

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents=llama_parse_documents,
    storage_context=storage_context
)

```

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#prepare-a-prompt) Prepare a prompt

Here we will create a custom prompt template. This prompt asks the LLM to use only the context information retrieved from Qdrant. When querying with hybrid mode, we can set `similarity_top_k` and `sparse_top_k` separately:

- `sparse_top_k` represents how many nodes will be retrieved from each dense and sparse query.
- `similarity_top_k` controls the final number of returned nodes. In the above setting, we end up with 10 nodes.

Then, we assemble the query engine using the prompt.

```python
from llama_index.core import PromptTemplate

qa_prompt_tmpl = (
    "Context information is below.\n"
    "-------------------------------"
    "{context_str}\n"
    "-------------------------------"
    "Given the context information and not prior knowledge,"
    "answer the query. Please be concise, and complete.\n"
    "If the context does not contain an answer to the query,"
    "respond with \"I don't know!\"."
    "Query: {query_str}\n"
    "Answer: "
)
qa_prompt = PromptTemplate(qa_prompt_tmpl)

from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer
from llama_index.core import Settings
Settings.embed_model = jina_embedding_model
Settings.llm = mixtral_llm

# retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=2,
    sparse_top_k=12,
    vector_store_query_mode="hybrid"
)

# response synthesizer
response_synthesizer = get_response_synthesizer(
    llm=mixtral_llm,
    text_qa_template=qa_prompt,
    response_mode="compact",
)

# query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)

```

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#run-a-test-query) Run a test query

Now you can ask questions and receive answers based on the data:

**Question**

```python
result = query_engine.query("What temperature should I use for my laundry?")
print(result.response)

```

**Answer**

```text
The water temperature is set to 70 ˚C during the Eco Drum Clean cycle. You cannot change the water temperature. However, the temperature for other cycles is not specified in the context.

```

And that’s it! Feel free to scale this up to as many documents and complex PDFs as you like.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/hybrid-search-llamaindex-jinaai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/hybrid-search-llamaindex-jinaai.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575420822&cv=11&fst=1748575420822&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fhybrid-search-llamaindex-jinaai%2F&hn=www.googleadservices.com&frm=0&tiba=Chat%20With%20Product%20PDF%20Manuals%20Using%20Hybrid%20Search%20-%20Qdrant&npa=0&pscdl=noapi&auid=60157591.1748575421&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575420799&cv=11&fst=1748575420799&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fhybrid-search-llamaindex-jinaai%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Chat%20With%20Product%20PDF%20Manuals%20Using%20Hybrid%20Search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=60157591.1748575421&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=05a6307c-3386-4961-b34b-54b3d1069410&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=70042804-7853-4787-adb0-4884ba01f82b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fhybrid-search-llamaindex-jinaai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=05a6307c-3386-4961-b34b-54b3d1069410&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=70042804-7853-4787-adb0-4884ba01f82b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fhybrid-search-llamaindex-jinaai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575421718&cv=11&fst=1748575421718&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fhybrid-search-llamaindex-jinaai%2F&hn=www.googleadservices.com&frm=0&tiba=Chat%20With%20Product%20PDF%20Manuals%20Using%20Hybrid%20Search%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=60157591.1748575421&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)