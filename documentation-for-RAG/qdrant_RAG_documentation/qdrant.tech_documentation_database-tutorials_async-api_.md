---
url: "https://qdrant.tech/documentation/database-tutorials/async-api/"
title: "Build With Async API - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Database tutorials](https://qdrant.tech/documentation/database-tutorials/)
- Build With Async API

# [Anchor](https://qdrant.tech/documentation/database-tutorials/async-api/\#using-qdrants-async-api-for-efficient-python-applications) Using Qdrant’s Async API for Efficient Python Applications

Asynchronous programming is being broadly adopted in the Python ecosystem. Tools such as FastAPI [have embraced this new\\
paradigm](https://fastapi.tiangolo.com/async/), but it is also becoming a standard for ML models served as SaaS. For example, the Cohere SDK
[provides an async client](https://github.com/cohere-ai/cohere-python/blob/856a4c3bd29e7a75fa66154b8ac9fcdf1e0745e0/src/cohere/client.py#L189) next to its synchronous counterpart.

Databases are often launched as separate services and are accessed via a network. All the interactions with them are IO-bound and can
be performed asynchronously so as not to waste time actively waiting for a server response. In Python, this is achieved by
using [`async/await`](https://docs.python.org/3/library/asyncio-task.html) syntax. That lets the interpreter switch to another task
while waiting for a response from the server.

## [Anchor](https://qdrant.tech/documentation/database-tutorials/async-api/\#when-to-use-async-api) When to use async API

There is no need to use async API if the application you are writing will never support multiple users at once (e.g it is a script that runs once per day). However, if you are writing a web service that multiple users will use simultaneously, you shouldn’t be
blocking the threads of the web server as it limits the number of concurrent requests it can handle. In this case, you should use
the async API.

Modern web frameworks like [FastAPI](https://fastapi.tiangolo.com/) and [Quart](https://quart.palletsprojects.com/en/latest/) support
async API out of the box. Mixing asynchronous code with an existing synchronous codebase might be a challenge. The `async/await` syntax
cannot be used in synchronous functions. On the other hand, calling an IO-bound operation synchronously in async code is considered
an antipattern. Therefore, if you build an async web service, exposed through an [ASGI](https://asgi.readthedocs.io/en/latest/) server,
you should use the async API for all the interactions with Qdrant.

### [Anchor](https://qdrant.tech/documentation/database-tutorials/async-api/\#using-qdrant-asynchronously) Using Qdrant asynchronously

The simplest way of running asynchronous code is to use define `async` function and use the `asyncio.run` in the following way to run it:

```python
from qdrant_client import models

import qdrant_client
import asyncio

async def main():
    client = qdrant_client.AsyncQdrantClient("localhost")

    # Create a collection
    await client.create_collection(
        collection_name="my_collection",
        vectors_config=models.VectorParams(size=4, distance=models.Distance.COSINE),
    )

    # Insert a vector
    await client.upsert(
        collection_name="my_collection",
        points=[\
            models.PointStruct(\
                id="5c56c793-69f3-4fbf-87e6-c4bf54c28c26",\
                payload={\
                    "color": "red",\
                },\
                vector=[0.9, 0.1, 0.1, 0.5],\
            ),\
        ],
    )

    # Search for nearest neighbors
    points = await client.query_points(
        collection_name="my_collection",
        query=[0.9, 0.1, 0.1, 0.5],
        limit=2,
    ).points

    # Your async code using AsyncQdrantClient might be put here
    # ...

asyncio.run(main())

```

The `AsyncQdrantClient` provides the same methods as the synchronous counterpart `QdrantClient`. If you already have a synchronous
codebase, switching to async API is as simple as replacing `QdrantClient` with `AsyncQdrantClient` and adding `await` before each
method call.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/async-api.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/async-api.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574805955&cv=11&fst=1748574805955&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fasync-api%2F&hn=www.googleadservices.com&frm=0&tiba=Build%20With%20Async%20API%20-%20Qdrant&npa=0&pscdl=noapi&auid=724686062.1748574806&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574805921&cv=11&fst=1748574805921&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fasync-api%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Build%20With%20Async%20API%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=724686062.1748574806&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=890299f3-0648-4944-a09a-370f7d6abd95&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=825e59a9-486e-4c50-bce9-a2ed7a5e129b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fasync-api%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=890299f3-0648-4944-a09a-370f7d6abd95&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=825e59a9-486e-4c50-bce9-a2ed7a5e129b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fasync-api%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574807074&cv=11&fst=1748574807074&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdatabase-tutorials%2Fasync-api%2F&hn=www.googleadservices.com&frm=0&tiba=Build%20With%20Async%20API%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=724686062.1748574806&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)