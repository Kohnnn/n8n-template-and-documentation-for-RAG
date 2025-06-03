---
url: "https://qdrant.tech/documentation/frameworks/dspy/"
title: "Stanford DSPy - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Stanford DSPy

# [Anchor](https://qdrant.tech/documentation/frameworks/dspy/\#stanford-dspy) Stanford DSPy

[DSPy](https://github.com/stanfordnlp/dspy) is the framework for solving advanced tasks with language models (LMs) and retrieval models (RMs). It unifies techniques for prompting and fine-tuning LMs — and approaches for reasoning, self-improvement, and augmentation with retrieval and tools.

- Provides composable and declarative modules for instructing LMs in a familiar Pythonic syntax.

- Introduces an automatic compiler that teaches LMs how to conduct the declarative steps in your program.


Qdrant can be used as a retrieval mechanism in the DSPy flow.

## [Anchor](https://qdrant.tech/documentation/frameworks/dspy/\#installation) Installation

For the Qdrant retrieval integration, include `dspy-ai` with the `qdrant` extra:

```bash
pip install dspy-ai dspy-qdrant

```

## [Anchor](https://qdrant.tech/documentation/frameworks/dspy/\#usage) Usage

We can configure `DSPy` settings to use the Qdrant retriever model like so:

```python
import dspy
from dspy_qdrant import QdrantRM

from qdrant_client import QdrantClient

turbo = dspy.OpenAI(model="gpt-3.5-turbo")
qdrant_client = QdrantClient()  # Defaults to a local instance at http://localhost:6333/
qdrant_retriever_model = QdrantRM("collection-name", qdrant_client, k=3)

dspy.settings.configure(lm=turbo, rm=qdrant_retriever_model)

```

Using the retriever is pretty simple. The `dspy.Retrieve(k)` module will search for the top-k passages that match a given query.

```python
retrieve = dspy.Retrieve(k=3)
question = "Some question about my data"
topK_passages = retrieve(question).passages

print(f"Top {retrieve.k} passages for question: {question} \n", "\n")

for idx, passage in enumerate(topK_passages):
    print(f"{idx+1}]", passage, "\n")

```

With Qdrant configured as the retriever for contexts, you can set up a DSPy module like so:

```python
class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()

        self.retrieve = dspy.Retrieve(k=num_passages)
        ...

    def forward(self, question):
        context = self.retrieve(question).passages
        ...

```

With the generic RAG blueprint now in place, you can add the many interactions offered by DSPy with context retrieval powered by Qdrant.

## [Anchor](https://qdrant.tech/documentation/frameworks/dspy/\#next-steps) Next steps

- Find DSPy usage docs and examples [here](https://github.com/stanfordnlp/dspy#4-documentation--tutorials).

- [Source Code](https://github.com/stanfordnlp/dspy/blob/main/dspy/retrieve/qdrant_rm.py)


##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dspy.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dspy.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574190373&cv=11&fst=1748574190373&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdspy%2F&hn=www.googleadservices.com&frm=0&tiba=Stanford%20DSPy%20-%20Qdrant&npa=0&pscdl=noapi&auid=1032051705.1748574190&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574190336&cv=11&fst=1748574190336&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdspy%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Stanford%20DSPy%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1032051705.1748574190&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9a487a16-9f9b-4eba-bd0b-1385b7ce5c3e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=58b87660-e603-46df-9b1b-6f2a9896e2ec&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdspy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9a487a16-9f9b-4eba-bd0b-1385b7ce5c3e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=58b87660-e603-46df-9b1b-6f2a9896e2ec&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdspy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574191495&cv=11&fst=1748574191495&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdspy%2F&hn=www.googleadservices.com&frm=0&tiba=Stanford%20DSPy%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1032051705.1748574190&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)