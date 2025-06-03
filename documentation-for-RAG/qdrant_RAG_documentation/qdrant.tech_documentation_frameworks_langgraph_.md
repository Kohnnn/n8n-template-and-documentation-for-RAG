---
url: "https://qdrant.tech/documentation/frameworks/langgraph/"
title: "LangGraph - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- LangGraph

# [Anchor](https://qdrant.tech/documentation/frameworks/langgraph/\#langgraph) LangGraph

[LangGraph](https://github.com/langchain-ai/langgraph) is a library for building stateful, multi-actor applications, ideal for creating agentic workflows. It provides fine-grained control over both the flow and state of your application, crucial for creating reliable agents.

You can define flows that involve cycles, essential for most agentic architectures, differentiating it from DAG-based solutions. Additionally, LangGraph includes built-in persistence, enabling advanced human-in-the-loop and memory features.

LangGraph works seamlessly with all the components of LangChain. This means we can utilize Qdrant’s [Langchain integration](https://qdrant.tech/documentation/frameworks/langchain/) to create retrieval nodes in LangGraph, available in both Python and Javascript!

## [Anchor](https://qdrant.tech/documentation/frameworks/langgraph/\#usage) Usage

- Install the required dependencies

pythontypescript

```python
$ pip install langgraph langchain_community langchain_qdrant fastembed

```

```typescript
$ npm install @langchain/langgraph langchain @langchain/qdrant @langchain/openai

```

- Create a retriever tool to add to the LangGraph workflow.

pythontypescript

```python

from langchain.tools.retriever import create_retriever_tool
from langchain_community.embeddings import FastEmbedEmbeddings

from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode

# We'll set up Qdrant to retrieve documents using Hybrid search.
# Learn more at https://qdrant.tech/articles/hybrid-search/
retriever = QdrantVectorStore.from_texts(
    url="http://localhost:6333/",
    collection_name="langgraph-collection",
    embedding=FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5"),
    sparse_embedding=FastEmbedSparse(model_name="Qdrant/bm25"),
    retrieval_mode=RetrievalMode.HYBRID,
    texts=["<SOME_KNOWLEDGE_TEXT>", "<SOME_OTHER_TEXT>", ...]
).as_retriever()

retriever_tool = create_retriever_tool(
    retriever,
    "retrieve_my_texts",
    "Retrieve texts stored in the Qdrant collection",
)

```

```typescript
import { QdrantVectorStore } from "@langchain/qdrant";
import { OpenAIEmbeddings } from "@langchain/openai";
import { createRetrieverTool } from "langchain/tools/retriever";

const vectorStore = await QdrantVectorStore.fromTexts(
    ["<SOME_KNOWLEDGE_TEXT>", "<SOME_OTHER_TEXT>"],
    [{ id: 2 }, { id: 1 }],
    new OpenAIEmbeddings(),
    {
        url: "http://localhost:6333/",
        collectionName: "goldel_escher_bach",
    }
);

const retriever = vectorStore.asRetriever();

const tool = createRetrieverTool(
  retriever,
  {
    name: "retrieve_my_texts",
    description:
      "Retrieve texts stored in the Qdrant collection",
  },
);

```

- Add the retriever tool as a node in LangGraph

pythontypescript

```python
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode

workflow = StateGraph()

# Define other the nodes which we'll cycle between.
workflow.add_node("retrieve_qdrant", ToolNode([retriever_tool]))

graph = workflow.compile()

```

```typescript
import { StateGraph } from "@langchain/langgraph";
import { ToolNode } from "@langchain/langgraph/prebuilt";

// Define the graph
const workflow = new StateGraph(SomeGraphState)
  // Define the nodes which we'll cycle between.
  .addNode("retrieve", new ToolNode([tool]));

const graph = workflow.compile();

```

## [Anchor](https://qdrant.tech/documentation/frameworks/langgraph/\#further-reading) Further Reading

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph End-to-End Guides](https://langchain-ai.github.io/langgraph/tutorials/)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/langgraph.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/langgraph.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=42baf9f9-439d-4603-ba29-a941efdcbe09&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e4bfbfb1-54fa-4f36-9b18-338f25531897&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flanggraph%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575507560&cv=11&fst=1748575507560&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flanggraph%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=LangGraph%20-%20Qdrant&npa=0&pscdl=noapi&auid=1684668229.1748575507&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575507421&cv=11&fst=1748575507421&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flanggraph%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=LangGraph%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1684668229.1748575507&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575507739&cv=11&fst=1748575507739&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flanggraph%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=LangGraph%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1684668229.1748575507&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=42baf9f9-439d-4603-ba29-a941efdcbe09&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e4bfbfb1-54fa-4f36-9b18-338f25531897&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flanggraph%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)