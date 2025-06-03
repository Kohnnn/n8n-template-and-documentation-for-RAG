---
url: "https://qdrant.tech/documentation/frameworks/smolagents/"
title: "SmolAgents - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- SmolAgents

# [Anchor](https://qdrant.tech/documentation/frameworks/smolagents/\#smolagents) SmolAgents

HuggingFace [SmolAgents](https://github.com/huggingface/smolagents) is a Python library for building AI agents. These agents write Python code to call tools and orchestrate other agents.

It uses `CodeAgent`. An LLM engine that writes its actions in code. SmolAgents suggests that this approach is demonstrated to work better than the current industry practice of letting the LLM output a dictionary of the tools it wants to call: [uses 30% fewer steps](https://huggingface.co/papers/2402.01030) (thus 30% fewer LLM calls)
and [reaches higher performance on difficult benchmarks](https://huggingface.co/papers/2411.01747).

## [Anchor](https://qdrant.tech/documentation/frameworks/smolagents/\#usage-with-qdrant) Usage with Qdrant

We’ll demonstrate how you can pair SmolAgents with Qdrant’s retrieval by building a movie recommendation agent.

### [Anchor](https://qdrant.tech/documentation/frameworks/smolagents/\#installation) Installation

```shell
pip install smolagents qdrant-client fastembed

```

### [Anchor](https://qdrant.tech/documentation/frameworks/smolagents/\#setup-a-qdrant-tool) Setup a Qdrant tool

We’ll build a SmolAgents tool that can query a Qdrant collection. This tool will vectorise queries locally using [FastEmbed](https://github.com/qdrant/fastembed).

Initially, we’ll be populating a Qdrant collection with information about 1000 movies from IMDb that we can search across.

```py
from fastembed import TextEmbedding
from qdrant_client import QdrantClient
from smolagents import Tool

class QdrantQueryTool(Tool):
    name = "qdrant_query"
    description = "Uses semantic search to retrieve movies from a Qdrant collection."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents.",
        }
    }
    output_type = "string"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collection_name = "smolagents"
        self.client = QdrantClient()

        if not self.client.collection_exists(self.collection_name):
            self.client.recover_snapshot(
                collection_name=self.collection_name,
                location="https://snapshots.qdrant.io/imdb-1000-jina.snapshot",
            )
        self.embedder = TextEmbedding(model_name="jinaai/jina-embeddings-v2-base-en")

    def forward(self, query: str) -> str:
        points = self.client.query_points(
            self.collection_name, query=next(self.embedder.query_embed(query)), limit=5
        ).points
        docs = "Retrieved documents:\n" + "".join(
            [\
                f"== Document {str(i)} ==\n"\
                + f"MOVIE TITLE: {point.payload['movie_name']}\n"\
                + f"MOVIE SUMMARY: {point.payload['description']}\n"\
                for i, point in enumerate(points)\
            ]
        )

        return docs

```

### [Anchor](https://qdrant.tech/documentation/frameworks/smolagents/\#define-the-agent) Define the agent

We can now set up `CodeAgent` to use our `QdrantQueryTool`.

```python
from smolagents import CodeAgent, HfApiModel
import os

# HuggingFace Access Token
# https://huggingface.co/docs/hub/en/security-tokens
os.environ["HF_TOKEN"] = "----------"

agent = CodeAgent(
    tools=[QdrantQueryTool()], model=HfApiModel(), max_iterations=4, verbose=True
)

```

Finally, we can run the agent with a user query.

```python
agent_output = agent.run("Movie about people taking a strong action for justice")
print(agent_output)

```

We should results similar to:

```console
[...truncated]

Out - Final answer: Jai Bhim
[Step 1: Duration 0.25 seconds| Input tokens: 4,497 | Output tokens: 134]
Jai Bhim

```

## [Anchor](https://qdrant.tech/documentation/frameworks/smolagents/\#further-reading) Further Reading

- [SmolAgents Blog](https://huggingface.co/blog/smolagents#code-agents)
- [SmolAgents Source](https://github.com/huggingface/smolagents)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/smolagents.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/smolagents.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574400494&cv=11&fst=1748574400494&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsmolagents%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=SmolAgents%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=299806540.1748574400&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574400669&cv=11&fst=1748574400669&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsmolagents%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=SmolAgents%20-%20Qdrant&npa=0&pscdl=noapi&auid=299806540.1748574400&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=608fcb12-a026-4b91-9bd2-6a603b897a5d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5f2e0166-1b3f-4fb0-b36b-08df053ed2e7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsmolagents%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=608fcb12-a026-4b91-9bd2-6a603b897a5d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5f2e0166-1b3f-4fb0-b36b-08df053ed2e7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsmolagents%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574401695&cv=11&fst=1748574401695&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsmolagents%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=SmolAgents%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=299806540.1748574400&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)