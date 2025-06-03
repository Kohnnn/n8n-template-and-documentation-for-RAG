---
url: "https://qdrant.tech/documentation/frameworks/crewai/"
title: "CrewAI - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- CrewAI

# [Anchor](https://qdrant.tech/documentation/frameworks/crewai/\#crewai) CrewAI

[CrewAI](https://www.crewai.com/) is a framework for orchestrating role-playing, autonomous AI agents. By leveraging collaborative intelligence, CrewAI allows agents to work together seamlessly, tackling complex tasks.

The framework has a sophisticated memory system designed to significantly enhance the capabilities of AI agents. This system aids agents to remember, reason, and learn from past interactions. You can use Qdrant to store short-term memory and entity memories of CrewAI agents.

- Short-Term Memory

Temporarily stores recent interactions and outcomes using RAG, enabling agents to recall and utilize information relevant to their current context during the current executions.

- Entity Memory

Entity Memory Captures and organizes information about entities (people, places, concepts) encountered during tasks, facilitating deeper understanding and relationship mapping. Uses RAG for storing entity information.

## [Anchor](https://qdrant.tech/documentation/frameworks/crewai/\#usage-with-qdrant) Usage with Qdrant

We’ll learn how to customize CrewAI’s default memory storage to use Qdrant.

### [Anchor](https://qdrant.tech/documentation/frameworks/crewai/\#installation) Installation

First, install CrewAI and Qdrant client packages:

```shell
pip install 'crewai[tools]' 'qdrant-client[fastembed]'

```

### [Anchor](https://qdrant.tech/documentation/frameworks/crewai/\#setup-a-crewai-project) Setup a CrewAI Project

You can learn to set up a CrewAI project [here](https://docs.crewai.com/installation#create-a-new-crewai-project). Let’s assume the project was name `mycrew`.

### [Anchor](https://qdrant.tech/documentation/frameworks/crewai/\#define-the-qdrant-storage) Define the Qdrant storage

> src/mycrew/storage.py

```python
from typing import Any, Dict, List, Optional

from crewai.memory.storage.rag_storage import RAGStorage
from qdrant_client import QdrantClient

class QdrantStorage(RAGStorage):
    """
    Extends Storage to handle embeddings for memory entries using Qdrant.

    """

    def __init__(self, type, allow_reset=True, embedder_config=None, crew=None):
        super().__init__(type, allow_reset, embedder_config, crew)

    def search(
        self,
        query: str,
        limit: int = 3,
        filter: Optional[dict] = None,
        score_threshold: float = 0,
    ) -> List[Any]:
        points = self.client.query(
            self.type,
            query_text=query,
            query_filter=filter,
            limit=limit,
            score_threshold=score_threshold,
        )
        results = [\
            {\
                "id": point.id,\
                "metadata": point.metadata,\
                "context": point.document,\
                "score": point.score,\
            }\
            for point in points\
        ]

        return results

    def reset(self) -> None:
        self.client.delete_collection(self.type)

    def _initialize_app(self):
        self.client = QdrantClient()
        # uncomment the next line of code
        # and choose from the [supported embedders](https://qdrant.github.io/fastembed/examples/Supported_Models/)
        # if you don't want to use the default one
        # self.client._embedding_model_name = 'jinaai/jina-embeddings-v2-small-en'
        if not self.client.collection_exists(self.type):
            self.client.create_collection(
                collection_name=self.type,
                vectors_config=self.client.get_fastembed_vector_params(),
                sparse_vectors_config=self.client.get_fastembed_sparse_vector_params(),
            )

    def save(self, value: Any, metadata: Dict[str, Any]) -> None:
        self.client.add(self.type, documents=[value], metadata=[metadata or {}])

```

The `add` AND `query` methods use [FastEmbed](https://github.com/qdrant/fastembed/) to vectorize data. You can however customize it if required.

### [Anchor](https://qdrant.tech/documentation/frameworks/crewai/\#instantiate-your-crew) Instantiate your crew

You can learn about setting up agents and tasks for your crew [here](https://docs.crewai.com/quickstart). We can update the instantiation of `Crew` to use our storage mechanism.

> src/mycrew/crew.py

```python
from crewai import Crew
from crewai.memory.entity.entity_memory import EntityMemory
from crewai.memory.short_term.short_term_memory import ShortTermMemory

from mycrew.storage import QdrantStorage

Crew(
    # Import the agents and tasks here.
    memory=True,
    entity_memory=EntityMemory(storage=QdrantStorage("entity")),
    short_term_memory=ShortTermMemory(storage=QdrantStorage("short-term")),
)

```

You can now run your Crew workflow with `crew run`. It’ll use Qdrant for memory ingestion and retrieval.

## [Anchor](https://qdrant.tech/documentation/frameworks/crewai/\#further-reading) Further Reading

- [CrewAI Documentation](https://docs.crewai.com/introduction)
- [CrewAI Examples](https://github.com/crewAIInc/crewAI-examples)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/crewai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/crewai.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573995536&cv=11&fst=1748573995536&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcrewai%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=CrewAI%20-%20Qdrant&npa=0&pscdl=noapi&auid=1720255762.1748573995&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573995520&cv=11&fst=1748573995520&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcrewai%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=CrewAI%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1720255762.1748573995&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=03302f64-34cd-4019-a999-bcd2735dd161&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0fc195e3-52dc-4c7c-8f89-8610a9d78a1d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcrewai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=03302f64-34cd-4019-a999-bcd2735dd161&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0fc195e3-52dc-4c7c-8f89-8610a9d78a1d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcrewai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573996162&cv=11&fst=1748573996162&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcrewai%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=CrewAI%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1720255762.1748573995&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)

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