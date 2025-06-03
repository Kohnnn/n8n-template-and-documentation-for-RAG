---
url: "https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/"
title: "Blog-Reading Chatbot with GPT-4o - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Blog-Reading Chatbot with GPT-4o

# [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#blog-reading-chatbot-with-gpt-4o) Blog-Reading Chatbot with GPT-4o

| Time: 90 min | Level: Advanced | [GitHub](https://github.com/qdrant/examples/blob/langchain-lcel-rag/langchain-lcel-rag/Langchain-LCEL-RAG-Demo.ipynb) |  |
| --- | --- | --- | --- |

In this tutorial, you will build a RAG system that combines blog content ingestion with the capabilities of semantic search. **OpenAI’s GPT-4o LLM** is powerful, but scaling its use requires us to supply context systematically.

RAG enhances the LLM’s generation of answers by retrieving relevant documents to aid the question-answering process. This setup showcases the integration of advanced search and AI language processing to improve information retrieval and generation tasks.

A notebook for this tutorial is available on [GitHub](https://github.com/qdrant/examples/blob/langchain-lcel-rag/langchain-lcel-rag/Langchain-LCEL-RAG-Demo.ipynb).

**Data Privacy and Sovereignty:** RAG applications often rely on sensitive or proprietary internal data. Running the entire stack within your own environment becomes crucial for maintaining control over this data. Qdrant Hybrid Cloud deployed on [Scaleway](https://www.scaleway.com/) addresses this need perfectly, offering a secure, scalable platform that still leverages the full potential of RAG. Scaleway offers serverless [Functions](https://www.scaleway.com/en/serverless-functions/) and serverless [Jobs](https://www.scaleway.com/en/serverless-jobs/), both of which are ideal for embedding creation in large-scale RAG cases.

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#components) Components

- **Cloud Host:** [Scaleway on managed Kubernetes](https://www.scaleway.com/en/kubernetes-kapsule/) for compatibility with Qdrant Hybrid Cloud.
- **Vector Database:** Qdrant Hybrid Cloud as the vector search engine for retrieval.
- **LLM:** GPT-4o, developed by OpenAI is utilized as the generator for producing answers.
- **Framework:** [LangChain](https://www.langchain.com/) for extensive RAG capabilities.

![Architecture diagram](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/architecture-diagram.png)

> Langchain [supports a wide range of LLMs](https://python.langchain.com/docs/integrations/chat/), and GPT-4o is used as the main generator in this tutorial. You can easily swap it out for your preferred model that might be launched on your premises to complete the fully private setup. For the sake of simplicity, we used the OpenAI APIs, but LangChain makes the transition seamless.

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#deploying-qdrant-hybrid-cloud-on-scaleway) Deploying Qdrant Hybrid Cloud on Scaleway

[Scaleway Kapsule](https://www.scaleway.com/en/kubernetes-kapsule/) and [Kosmos](https://www.scaleway.com/en/kubernetes-kosmos/) are managed Kubernetes services from [Scaleway](https://www.scaleway.com/en/). They abstract away the complexities of managing and operating a Kubernetes cluster. The primary difference being, Kapsule clusters are composed solely of Scaleway Instances. Whereas, a Kosmos cluster is a managed multi-cloud Kubernetes engine that allows you to connect instances from any cloud provider to a single managed Control-Plane.

1. To start using managed Kubernetes on Scaleway, follow the [platform-specific documentation](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/#scaleway).
2. Once your Kubernetes clusters are up, [you can begin deploying Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/).

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#prerequisites) Prerequisites

To prepare the environment for working with Qdrant and related libraries, it’s necessary to install all required Python packages. This can be done using Poetry, a tool for dependency management and packaging in Python. The code snippet imports various libraries essential for the tasks ahead, including `bs4` for parsing HTML and XML documents, `langchain` and its community extensions for working with language models and document loaders, and `Qdrant` for vector storage and retrieval. These imports lay the groundwork for utilizing Qdrant alongside other tools for natural language processing and machine learning tasks.

Qdrant will be running on a specific URL and access will be restricted by the API key. Make sure to store them both as environment variables as well:

```shell
export QDRANT_URL="https://qdrant.example.com"
export QDRANT_API_KEY="your-api-key"

```

_Optional:_ Whenever you use LangChain, you can also [configure LangSmith](https://docs.smith.langchain.com/), which will help us trace, monitor and debug LangChain applications. You can sign up for LangSmith [here](https://smith.langchain.com/).

```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY="your-api-key"
export LANGCHAIN_PROJECT="your-project"  # if not specified, defaults to "default"

```

Now you can get started:

```python
import getpass
import os

import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_qdrant import Qdrant
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

```

Set up the OpenAI API key:

```python
os.environ["OPENAI_API_KEY"] = getpass.getpass()

```

Initialize the language model:

```python
llm = ChatOpenAI(model="gpt-4o")

```

It is here that we configure both the Embeddings and LLM. You can replace this with your own models using Ollama or other services. Scaleway has some great [L4 GPU Instances](https://www.scaleway.com/en/l4-gpu-instance/) you can use for compute here.

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#download-and-parse-data) Download and parse data

To begin working with blog post contents, the process involves loading and parsing the HTML content. This is achieved using `urllib` and `BeautifulSoup`, which are tools designed for such tasks. After the content is loaded and parsed, it is indexed using Qdrant, a powerful tool for managing and querying vector data. The code snippet demonstrates how to load, chunk, and index the contents of a blog post by specifying the URL of the blog and the specific HTML elements to parse. This step is crucial for preparing the data for further processing and analysis with Qdrant.

```python
# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

```

### [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#chunking-data) Chunking data

When dealing with large documents, such as a blog post exceeding 42,000 characters, it’s crucial to manage the data efficiently for processing. Many models have a limited context window and struggle with long inputs, making it difficult to extract or find relevant information. To overcome this, the document is divided into smaller chunks. This approach enhances the model’s ability to process and retrieve the most pertinent sections of the document effectively.

In this scenario, the document is split into chunks using the `RecursiveCharacterTextSplitter` with a specified chunk size and overlap. This method ensures that no critical information is lost between chunks. Following the splitting, these chunks are then indexed into Qdrant—a vector database for efficient similarity search and storage of embeddings. The `Qdrant.from_documents` function is utilized for indexing, with documents being the split chunks and embeddings generated through `OpenAIEmbeddings`. The entire process is facilitated within an in-memory database, signifying that the operations are performed without the need for persistent storage, and the collection is named “lilianweng” for reference.

This chunking and indexing strategy significantly improves the management and retrieval of information from large documents, making it a practical solution for handling extensive texts in data processing workflows.

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

vectorstore = Qdrant.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(),
    collection_name="lilianweng",
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
)

```

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#retrieve-and-generate-content) Retrieve and generate content

The `vectorstore` is used as a retriever to fetch relevant documents based on vector similarity. The `hub.pull("rlm/rag-prompt")` function is used to pull a specific prompt from a repository, which is designed to work with retrieved documents and a question to generate a response.

The `format_docs` function formats the retrieved documents into a single string, preparing them for further processing. This formatted string, along with a question, is passed through a chain of operations. Firstly, the context (formatted documents) and the question are processed by the retriever and the prompt. Then, the result is fed into a large language model ( `llm`) for content generation. Finally, the output is parsed into a string format using `StrOutputParser()`.

This chain of operations demonstrates a sophisticated approach to information retrieval and content generation, leveraging both the semantic understanding capabilities of vector search and the generative prowess of large language models.

Now, retrieve and generate data using relevant snippets from the blogL

```python
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

```

### [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#invoking-the-rag-chain) Invoking the RAG Chain

```python
rag_chain.invoke("What is Task Decomposition?")

```

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#next-steps) Next steps:

We built a solid foundation for a simple chatbot, but there is still a lot to do. If you want to make the
system production-ready, you should consider implementing the mechanism into your existing stack. We recommend

Our vector database can easily be hosted on [Scaleway](https://www.scaleway.com/), our trusted [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) partner. This means that Qdrant can be run from your Scaleway region, but the database itself can still be managed from within Qdrant Cloud’s interface. Both products have been tested for compatibility and scalability, and we recommend their [managed Kubernetes](https://www.scaleway.com/en/kubernetes-kapsule/) service.
Their French deployment regions e.g. France are excellent for network latency and data sovereignty. For hosted GPUs, try [rendering with L4 GPU instances](https://www.scaleway.com/en/l4-gpu-instance/).

If you have any questions, feel free to ask on our [Discord community](https://qdrant.to/discord).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/rag-chatbot-scaleway.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/rag-chatbot-scaleway.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574400267&cv=11&fst=1748574400267&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frag-chatbot-scaleway%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Blog-Reading%20Chatbot%20with%20GPT-4o%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=295924227.1748574400&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574400340&cv=11&fst=1748574400340&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frag-chatbot-scaleway%2F&hn=www.googleadservices.com&frm=0&tiba=Blog-Reading%20Chatbot%20with%20GPT-4o%20-%20Qdrant&npa=0&pscdl=noapi&auid=295924227.1748574400&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d9b711cf-486a-4489-a71c-befe1148197d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=59be2cdd-46a4-404c-877d-0a2d702a284d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frag-chatbot-scaleway%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d9b711cf-486a-4489-a71c-befe1148197d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=59be2cdd-46a4-404c-877d-0a2d702a284d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frag-chatbot-scaleway%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574401137&cv=11&fst=1748574401137&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frag-chatbot-scaleway%2F&hn=www.googleadservices.com&frm=0&tiba=Blog-Reading%20Chatbot%20with%20GPT-4o%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=295924227.1748574400&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)