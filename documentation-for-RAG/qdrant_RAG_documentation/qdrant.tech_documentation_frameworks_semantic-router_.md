---
url: "https://qdrant.tech/documentation/frameworks/semantic-router/"
title: "Semantic-Router - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Semantic-Router

# [Anchor](https://qdrant.tech/documentation/frameworks/semantic-router/\#semantic-router) Semantic-Router

[Semantic-Router](https://www.aurelio.ai/semantic-router/) is a library to build decision-making layers for your LLMs and agents. It uses vector embeddings to make tool-use decisions rather than LLM generations, routing our requests using semantic meaning.

Qdrant is available as a supported index in Semantic-Router for you to ingest route data and perform retrievals.

## [Anchor](https://qdrant.tech/documentation/frameworks/semantic-router/\#installation) Installation

To use Semantic-Router with Qdrant, install the `qdrant` extra:

```console
pip install semantic-router[qdrant]

```

## [Anchor](https://qdrant.tech/documentation/frameworks/semantic-router/\#usage) Usage

Set up `QdrantIndex` with the appropriate configurations:

```python
from semantic_router.index import QdrantIndex

qdrant_index = QdrantIndex(
    url="https://xyz-example.eu-central.aws.cloud.qdrant.io", api_key="<your-api-key>"
)

```

Once the Qdrant index is set up with the appropriate configurations, we can pass it to the `RouteLayer`.

```python
from semantic_router.layer import RouteLayer

RouteLayer(encoder=some_encoder, routes=some_routes, index=qdrant_index)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/semantic-router/\#complete-example) Complete Example

**Click to expand**

```python
import os

from semantic_router import Route
from semantic_router.encoders import OpenAIEncoder
from semantic_router.index import QdrantIndex
from semantic_router.layer import RouteLayer

# we could use this as a guide for our chatbot to avoid political conversations
politics = Route(
    name="politics value",
    utterances=[\
        "isn't politics the best thing ever",\
        "why don't you tell me about your political opinions",\
        "don't you just love the president",\
        "they're going to destroy this country!",\
        "they will save the country!",\
    ],
)

# this could be used as an indicator to our chatbot to switch to a more
# conversational prompt
chitchat = Route(
    name="chitchat",
    utterances=[\
        "how's the weather today?",\
        "how are things going?",\
        "lovely weather today",\
        "the weather is horrendous",\
        "let's go to the chippy",\
    ],
)

# we place both of our decisions together into single list
routes = [politics, chitchat]

os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"
encoder = OpenAIEncoder()

rl = RouteLayer(
    encoder=encoder,
    routes=routes,
    index=QdrantIndex(location=":memory:"),
)

print(rl("What have you been upto?").name)

```

This returns:

```console
[Out]: 'chitchat'

```

## [Anchor](https://qdrant.tech/documentation/frameworks/semantic-router/\#-further-reading) 📚 Further Reading

- Semantic-Router [Documentation](https://github.com/aurelio-labs/semantic-router/tree/main/docs)
- Semantic-Router [Video Course](https://www.aurelio.ai/course/semantic-router)
- [Source Code](https://github.com/aurelio-labs/semantic-router/blob/main/semantic_router/index/qdrant.py)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/semantic-router.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/semantic-router.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573586803&cv=11&fst=1748573586803&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsemantic-router%2F&hn=www.googleadservices.com&frm=0&tiba=Semantic-Router%20-%20Qdrant&npa=0&pscdl=noapi&auid=844493147.1748573587&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573586774&cv=11&fst=1748573586774&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsemantic-router%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Semantic-Router%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=844493147.1748573587&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=149de421-94ff-40c4-bd98-8db13bf8dcb2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c417d8f3-e81f-4050-a035-d5ac0eb8e7b3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsemantic-router%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=149de421-94ff-40c4-bd98-8db13bf8dcb2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c417d8f3-e81f-4050-a035-d5ac0eb8e7b3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsemantic-router%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573587793&cv=11&fst=1748573587793&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsemantic-router%2F&hn=www.googleadservices.com&frm=0&tiba=Semantic-Router%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=844493147.1748573587&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)