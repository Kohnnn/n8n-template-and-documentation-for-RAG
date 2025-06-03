---
url: "https://qdrant.tech/documentation/frameworks/autogen/"
title: "Autogen - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Autogen

# [Anchor](https://qdrant.tech/documentation/frameworks/autogen/\#microsoft-autogen) Microsoft Autogen

[AutoGen](https://github.com/microsoft/autogen/tree/0.2) is an open-source programming framework for building AI agents and facilitating cooperation among multiple agents to solve tasks.

- Multi-agent conversations: AutoGen agents can communicate with each other to solve tasks. This allows for more complex and sophisticated applications than would be possible with a single LLM.

- Customization: AutoGen agents can be customized to meet the specific needs of an application. This includes the ability to choose the LLMs to use, the types of human input to allow, and the tools to employ.

- Human participation: AutoGen allows human participation. This means that humans can provide input and feedback to the agents as needed.


With the [Autogen-Qdrant integration](https://microsoft.github.io/autogen/0.2/docs/reference/agentchat/contrib/vectordb/qdrant/), you build Autogen workflows backed by Qdrant’t performant retrievals.

## [Anchor](https://qdrant.tech/documentation/frameworks/autogen/\#installation) Installation

```bash
pip install "autogen-agentchat[retrievechat-qdrant]"

```

## [Anchor](https://qdrant.tech/documentation/frameworks/autogen/\#usage) Usage

#### [Anchor](https://qdrant.tech/documentation/frameworks/autogen/\#configuration) Configuration

```python
import autogen

config_list = autogen.config_list_from_json("OAI_CONFIG_LIST")

```

The `config_list_from_json` function first looks for the environment variable `OAI_CONFIG_LIST` which needs to be a valid JSON string. If not found, it then looks for a JSON file named `OAI_CONFIG_LIST`. A sample file can be found [here](https://github.com/microsoft/autogen/blob/0.2/OAI_CONFIG_LIST_sample).

#### [Anchor](https://qdrant.tech/documentation/frameworks/autogen/\#construct-agents-for-retrievechat) Construct agents for RetrieveChat

We start by initializing the RetrieveAssistantAgent and QdrantRetrieveUserProxyAgent. The system message needs to be set to “You are a helpful assistant.” for RetrieveAssistantAgent. The detailed instructions are given in the user message.

```python
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

# 1. Create an AssistantAgent instance named "assistant"
assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
    llm_config={
        "timeout": 600,
        "cache_seed": 42,
        "config_list": config_list,
    },
)

sentence_transformer_ef = SentenceTransformer("all-distilroberta-v1").encode
client = QdrantClient(url="http://localhost:6333/")

# 2. Create the RetrieveUserProxyAgent instance named "ragproxyagent"
# Refer to https://microsoft.github.io/autogen/docs/reference/agentchat/contrib/retrieve_user_proxy_agent
# for more information on the RetrieveUserProxyAgent
ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    retrieve_config={
        "task": "code",
        "docs_path": [\
            "path/to/some/doc.md",\
            "path/to/some/other/doc.md",\
        ],
        "chunk_token_size": 2000,
        "model": config_list[0]["model"],
        "vector_db": "qdrant",
        "db_config": {"client": client},
        "get_or_create": True,
        "overwrite": True,
        "embedding_function": sentence_transformer_ef,  # Defaults to "BAAI/bge-small-en-v1.5" via FastEmbed
    },
    code_execution_config=False,
)

```

#### [Anchor](https://qdrant.tech/documentation/frameworks/autogen/\#run-the-agent) Run the agent

```python
# Always reset the assistant before starting a new conversation.
assistant.reset()

# We use the ragproxyagent to generate a prompt to be sent to the assistant as the initial message.
# The assistant receives it and generates a response. The response will be sent back to the ragproxyagent for processing.
# The conversation continues until the termination condition is met.

qa_problem = "What is the .....?"
chat_results = ragproxyagent.initiate_chat(assistant, message=ragproxyagent.message_generator, problem=qa_problem)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/autogen/\#next-steps) Next steps

- AutoGen [documentation](https://microsoft.github.io/autogen/0.2)
- Autogen [examples](https://microsoft.github.io/autogen/0.2/docs/Examples)
- [Source Code](https://github.com/microsoft/autogen/blob/0.2/autogen/agentchat/contrib/vectordb/qdrant.py)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/autogen.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/autogen.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574843442&cv=11&fst=1748574843442&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fautogen%2F&hn=www.googleadservices.com&frm=0&tiba=Autogen%20-%20Qdrant&npa=0&pscdl=noapi&auid=252880864.1748574843&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574843424&cv=11&fst=1748574843424&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fautogen%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Autogen%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=252880864.1748574843&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b08fe7c6-028e-4c2f-a323-1570c8292d7b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6c86a17b-0bcb-4a89-bd32-2fd87089522c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fautogen%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b08fe7c6-028e-4c2f-a323-1570c8292d7b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6c86a17b-0bcb-4a89-bd32-2fd87089522c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fautogen%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574844518&cv=11&fst=1748574844518&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fautogen%2F&hn=www.googleadservices.com&frm=0&tiba=Autogen%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=252880864.1748574843&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)