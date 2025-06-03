---
url: "https://qdrant.tech/blog/qdrant-n8n/"
title: "Chat with a codebase using Qdrant and N8N - Qdrant"
---

0

# Chat with a codebase using Qdrant and N8N

Anush Shetty

·

January 06, 2024

![Chat with a codebase using Qdrant and N8N](https://qdrant.tech/blog/qdrant-n8n/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n%2F&text=Chat%20with%20a%20codebase%20using%20Qdrant%20and%20N8N "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n%2F "LinkedIn")

n8n (pronounced n-eight-n) helps you connect any app with an API. You can then manipulate its data with little or no code. With the Qdrant node on n8n, you can build AI-powered workflows visually.

Let’s go through the process of building a workflow. We’ll build a chat with a codebase service.

## [Anchor](https://qdrant.tech/blog/qdrant-n8n/\#prerequisites) Prerequisites

- A running Qdrant instance. If you need one, use our [Quick start guide](https://qdrant.tech/documentation/quick-start/) to set it up.
- An OpenAI API Key. Retrieve your key from the [OpenAI API page](https://platform.openai.com/account/api-keys) for your account.
- A GitHub access token. If you need to generate one, start at the [GitHub Personal access tokens page](https://github.com/settings/tokens/).

## [Anchor](https://qdrant.tech/blog/qdrant-n8n/\#building-the-app) Building the App

Our workflow has two components. Refer to the [n8n quick start guide](https://docs.n8n.io/workflows/create/) to get acquainted with workflow semantics.

- A workflow to ingest a GitHub repository into Qdrant
- A workflow for a chat service with the ingested documents

#### [Anchor](https://qdrant.tech/blog/qdrant-n8n/\#workflow-1-github-repository-ingestion-into-qdrant) Workflow 1: GitHub Repository Ingestion into Qdrant

![GitHub to Qdrant workflow](https://qdrant.tech/blog/qdrant-n8n/load-demo.gif)

For this workflow, we’ll use the following nodes:

- [Qdrant Vector Store - Insert](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/#insert-documents): Configure with [Qdrant credentials](https://docs.n8n.io/integrations/builtin/credentials/qdrant/) and a collection name. If the collection doesn’t exist, it’s automatically created with the appropriate configurations.

- [GitHub Document Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader/): Configure the GitHub access token, repository name, and branch. In this example, we’ll use [qdrant/demo-food-discovery@main](https://github.com/qdrant/demo-food-discovery).

- [Embeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai/): Configure with OpenAI credentials and the embedding model options. We use the [text-embedding-ada-002](https://platform.openai.com/docs/models/embeddings) model.

- [Recursive Character Text Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter/): Configure the [text splitter options](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter/#node-parameters). We use the defaults in this example.


Connect the workflow to a manual trigger. Click “Test Workflow” to run it. You should be able to see the progress in real-time as the data is fetched from GitHub, transformed into vectors and loaded into Qdrant.

#### [Anchor](https://qdrant.tech/blog/qdrant-n8n/\#workflow-2-chat-service-with-ingested-documents) Workflow 2: Chat Service with Ingested Documents

![Chat workflow](https://qdrant.tech/blog/qdrant-n8n/chat.png)

The workflow use the following nodes:

- [Qdrant Vector Store - Retrieve](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/#retrieve-documents-for-agentchain): Configure with [Qdrant credentials](https://docs.n8n.io/integrations/builtin/credentials/qdrant/) and the name of the collection the data was loaded into in workflow 1.

- [Retrieval Q&A Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/): Configure with default values.

- [Embeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai/): Configure with OpenAI credentials and the embedding model options. We use the [text-embedding-ada-002](https://platform.openai.com/docs/models/embeddings) model.

- [OpenAI Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/): Configure with OpenAI credentials and the chat model name. We use [gpt-3.5-turbo](https://platform.openai.com/docs/models/gpt-3-5) for the demo.


Once configured, hit the “Chat” button to initiate the chat interface and begin a conversation with your codebase.

![Chat demo](https://qdrant.tech/blog/qdrant-n8n/chat-demo.png)

To embed the chat in your applications, consider using the [@n8n/chat](https://www.npmjs.com/package/@n8n/chat) package. Additionally, N8N supports scheduled workflows and can be triggered by events across various applications.

## [Anchor](https://qdrant.tech/blog/qdrant-n8n/\#further-reading) Further reading

- [n8n Documentation](https://docs.n8n.io/)
- [n8n Qdrant Node documentation](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/#qdrant-vector-store)

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=61ef9283-386c-48a6-8bb9-fe06ff5a5f85)

![](https://qdrant.tech/img/rocket.svg)

Up!

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=15efec16-f6fc-4e8f-a98d-a9fde98a9f1b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d8c16657-9377-43ad-a2a1-8a454b369aee&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574448710&cv=11&fst=1748574448710&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Chat%20with%20a%20codebase%20using%20Qdrant%20and%20N8N%20-%20Qdrant&npa=0&pscdl=noapi&auid=2027260002.1748574448&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574448698&cv=11&fst=1748574448698&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Chat%20with%20a%20codebase%20using%20Qdrant%20and%20N8N%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2027260002.1748574448&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=15efec16-f6fc-4e8f-a98d-a9fde98a9f1b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d8c16657-9377-43ad-a2a1-8a454b369aee&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?enableResponsiveStyles=true)