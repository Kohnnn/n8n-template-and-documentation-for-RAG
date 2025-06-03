---
url: "https://qdrant.tech/documentation/frameworks/openai-agents/"
title: "OpenAI Agents - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- OpenAI Agents

# [Anchor](https://qdrant.tech/documentation/frameworks/openai-agents/\#openai-agents) OpenAI Agents

[OpenAI Agents](https://github.com/openai/openai-agents-python) is a Python framework to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It’s a production-ready upgrade of the experimental framework, [Swarm](https://github.com/openai/swarm).

## [Anchor](https://qdrant.tech/documentation/frameworks/openai-agents/\#getting-started) Getting Started

To start using OpenAI Agents, follow these steps:

- Install the package

```bash
pip install openai-agents

```

- Set up your OpenAI API key

```bash
export OPENAI_API_KEY="<YOUR_KEY>"

```

## [Anchor](https://qdrant.tech/documentation/frameworks/openai-agents/\#how-it-works) How It Works

The Agents SDK has a very small set of primitives:

- `Agents`, which are LLMs equipped with instructions and tools
- `Handoffs`, which allow agents to delegate to other agents for specific tasks
- `Guardrails`, which enable the inputs to agents to be validated

Used with Python, these building blocks make it easy to create real-world apps with tool-agent interactions and minimal learning curve. Plus, the SDK also includes tracing to help you debug, evaluate, and fine-tune your agent workflows.

## [Anchor](https://qdrant.tech/documentation/frameworks/openai-agents/\#creating-your-first-agents) Creating Your First Agents

Here’s a basic example of three agents:

- Triage Agent: Acts as the initial point of contact. It analyzes the user’s question and decides whether to route it to a specialized agent.
- Math Tutor: A specialist agent designed to help with math-related questions.
- History Tutor: A specialist agent focused on historical topics.

```python
from agents import Agent, Runner

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
)

# Run the interaction
result = Runner.run_sync(triage_agent, "I want some help with WW1.")
print(result.final_output)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/openai-agents/\#integrating-with-qdrant) Integrating with Qdrant

You can connect agents to retrieve or ingest data into a Qdrant collection. Thereby building your knowledge base. Here’s how to enable an agent to retrieve information from Qdrant.

Assume you have a Qdrant [collection created](https://qdrant.tech/documentation/concepts/collections/#create-a-collection) using the `"text-embedding-3-small"` model. The payload structure includes a `text` field for knowledge storage.

```python
import qdrant_client
from openai import OpenAI
from agents import Agent, function_tool

# Initialize clients
openai_client = OpenAI()
qdrant = qdrant_client.QdrantClient(host="localhost")

# Configuration
EMBEDDING_MODEL = "text-embedding-3-small"
COLLECTION_NAME = "help_center"
LIMIT = 5
SCORE_THRESHOLD = 0.7

@function_tool
def query_qdrant(query: str) -> str:
    """Retrieve semantically relevant content from Qdrant.

    Args:
        query: The query to search.
    """
    embedded_query = openai_client.embeddings.create(
        input=query,
        model=EMBEDDING_MODEL,
    ).data[0].embedding

    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=embedded_query,
        limit=LIMIT,
        score_threshold=SCORE_THRESHOLD,
    ).points

    if results:
        return "\n".join([point.payload["text"] for point in results])
    else:
        return "No results found."

qdrant_agent = Agent(
    name="Qdrant searcher",
    handoff_description="Specialist agent for retrieving info from a Qdrant collection",
    instructions="You help find answers for user queries using Qdrant. Do not make up any info on your own.",
    tools=[query_qdrant],
)

```

Our `qdrant_agent` can now query a Qdrant collection whenever deemed necessary to answer a user query.

## [Anchor](https://qdrant.tech/documentation/frameworks/openai-agents/\#further-reading) Further Reading

- [Agents Documentation](https://openai.github.io/openai-agents-python/)
- [Agents Examples](https://github.com/openai/openai-agents-python/tree/main/examples)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/openai-agents.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/openai-agents.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573596256&cv=11&fst=1748573596256&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fopenai-agents%2F&hn=www.googleadservices.com&frm=0&tiba=OpenAI%20Agents%20-%20Qdrant&npa=0&pscdl=noapi&auid=2082291110.1748573596&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573596131&cv=11&fst=1748573596131&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fopenai-agents%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=OpenAI%20Agents%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2082291110.1748573596&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ce4714a8-99d0-4757-bef7-5dc9d89c2ebd&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4b8ce61e-306f-4202-a12e-18f0905503a7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fopenai-agents%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ce4714a8-99d0-4757-bef7-5dc9d89c2ebd&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4b8ce61e-306f-4202-a12e-18f0905503a7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fopenai-agents%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)