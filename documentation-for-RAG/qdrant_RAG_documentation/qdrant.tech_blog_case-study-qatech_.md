---
url: "https://qdrant.tech/blog/case-study-qatech/"
title: "Empowering QA.tech’s Testing Agents with Real-Time Precision and Scale - Qdrant"
---

0

# Empowering QA.tech’s Testing Agents with Real-Time Precision and Scale

Qdrant

·

November 21, 2024

![Empowering QA.tech’s Testing Agents with Real-Time Precision and Scale](https://qdrant.tech/blog/case-study-qatech/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-qatech%2F&text=Empowering%20QA.tech%e2%80%99s%20Testing%20Agents%20with%20Real-Time%20Precision%20and%20Scale "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-qatech%2F "LinkedIn")

![qdrant-qatech-1](https://qdrant.tech/blog/case-study-qatech/qdrant-qatech-1.png)

[QA.tech](https://qa.tech/), a company specializing in AI-driven automated testing solutions, found that building and **fully testing web applications, especially end-to-end, can be complex and time-consuming**. Unlike unit tests, end-to-end tests reveal what’s actually happening in the browser, often uncovering issues that other methods miss.

Traditional solutions like hard-coded tests are not only labor-intensive to set up but also challenging to maintain over time. Alternatively, hiring QA testers can be a solution, but for startups, it quickly becomes a bottleneck. With every release, more testers are needed, and if testing is outsourced, managing timelines and ensuring quality becomes even harder.

To address this, QA.tech has developed **testing agents** that perform tasks on the browser just like a user would - for example, purchasing a ticket on a travel app. These agents navigate the entire booking process, from searching for flights to completing the purchase, all while assessing their success. **They document errors, record the process, and flag issues for developers to review.** With access to console logs and network calls, developers can easily analyze each step, quickly understanding and debugging any issues that arise.

![qdrant-qatech-2](https://qdrant.tech/blog/case-study-qatech/qdrant-qatech-2.png)

_Output from a QA.tech AI agent_

## [Anchor](https://qdrant.tech/blog/case-study-qatech/\#what-prompted-qatech-to-use-a-vector-database) What prompted QA.tech to use a vector database?

QA.tech initially used **pgvector** for simpler vector use cases but encountered scalability limitations as their requirements grew, prompting them to adopt Qdrant. They needed a [vector database](https://qdrant.tech/qdrant-vector-database/) capable of handling high-velocity, real-time analysis to support their AI agents, which operate within an analysis layer that observes and interprets actions across web pages. This analysis layer relies heavily on multimodal models and substantial subprocessing to enable the AI agent to make informed, real-time decisions.

In some web interfaces, hundreds of actions can occur, and processing them in real time - especially with each click - can be slow. Dynamic web elements and changing identifiers further complicate this, making traditional methods unreliable. To address these challenges, QA.tech trained custom embeddings on specific actions, which significantly accelerates decision-making.

This setup requires frequent embedding lookups, generating a high volume of database calls for each interaction. As **Vilhelm von Ehrenheim from QA.tech** explained:

> “You get a lot of embeddings, a lot of calls, a lot of lookups towards the database for every click, and that needs to scale nicely.”

Qdrant’s fast, scalable [vector search](https://qdrant.tech/advanced-search/) enables QA.tech to handle these high-velocity lookups seamlessly, ensuring that the agent remains responsive and capable of making quick, accurate decisions in real time.

## [Anchor](https://qdrant.tech/blog/case-study-qatech/\#why-qatech-chose-qdrant-for-its-ai-agent-platform) Why QA.tech chose Qdrant for its AI Agent platform

QA.tech’s AI Agents handle high-velocity web actions, requiring efficient real-time operations and scalable infrastructure. The team faced challenges with managing network overhead, CPU load, and the need to store [multiple embeddings](https://qdrant.tech/documentation/concepts/vectors/#multivectors) for different use cases. Qdrant provided the solution to address these issues.

**Reducing Network Overhead with Batch Operations**

Handling hundreds of simultaneous actions on a web interface individually created significant network overhead. Von Ehrenheim explained that “doing all of those in separate calls creates a lot of network overhead.” Qdrant’s batch operations allowed QA.tech to process multiple actions at once, reducing network traffic and improving efficiency. This capability is essential for AI Agents, where real-time responsiveness is critical.

**Optimizing CPU Load for Embedding Processing**

PostgreSQL’s transaction guarantees resulted in high CPU usage when processing embeddings, especially at scale. Von Ehrenheim noted that adding many new embeddings “requires much more CPU,” which led to performance bottlenecks. Qdrant’s architecture efficiently handled large-scale embeddings, preventing CPU overload and ensuring smooth, uninterrupted performance, a key requirement for AI Agents.

**Managing Multiple Embeddings for Different Use Cases**

AI Agents need flexibility in handling both real-time actions and context-aware tasks. QA.tech required different embeddings for immediate action processing and deeper semantic searches. Von Ehrenheim mentioned, _“We use one embedding for high-velocity actions, but I also want to store other types of embeddings for analytical purposes.”_

> Qdrant’s ability to store multiple embeddings per data point allowed QA.tech to meet these diverse needs without added complexity.

## [Anchor](https://qdrant.tech/blog/case-study-qatech/\#how-qatech-overcame-key-challenges-in-ai-agent-development) How QA.tech Overcame Key Challenges in AI Agent Development

Building reliable AI agents presents unique complexities, particularly as workflows grow more multi-step and dynamic.

> “The more steps you ask an agent to take, the harder it becomes to ensure consistent performance,” Vilhelm von Ehrenheim, Co-Founder of QA.tech.

Each additional action adds layers of interdependent variables, creating pathways that can easily lead to errors if not managed carefully.

Von Ehrenheim also points out the limitations of current large language models (LLMs), noting that _“LLMs are getting more powerful, but they still struggle with multi-step reasoning and for example handling subtle visual changes like dark mode or adaptive UIs.”_ These challenges make it essential for agents to have precise planning capabilities and context awareness, which QA.tech has addressed by implementing custom embeddings and multimodal models.

_“This is where scalable, adaptable infrastructure becomes crucial,”_ von Ehrenheim adds. Qdrant has been instrumental for QA.tech, providing stable, high-performance vector search to support the demanding workflows. **“With Qdrant, we’re able to handle these complex, high-velocity tasks without compromising on reliability.”**

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=c2b7dd32-8d46-411e-9138-da0c422d6cc3)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575402252&cv=11&fst=1748575402252&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-qatech%2F&hn=www.googleadservices.com&frm=0&tiba=Empowering%20QA.tech%E2%80%99s%20Testing%20Agents%20with%20Real-Time%20Precision%20and%20Scale%20-%20Qdrant&npa=0&pscdl=noapi&auid=1358807938.1748575402&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575402230&cv=11&fst=1748575402230&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-qatech%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Empowering%20QA.tech%E2%80%99s%20Testing%20Agents%20with%20Real-Time%20Precision%20and%20Scale%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1358807938.1748575402&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9c86f34c-729e-441e-95f8-ab4ce69f83d4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e57e8338-312a-4ecf-ac31-5cc617551bcb&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-qatech%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575402990&cv=11&fst=1748575402990&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-qatech%2F&hn=www.googleadservices.com&frm=0&tiba=Empowering%20QA.tech%E2%80%99s%20Testing%20Agents%20with%20Real-Time%20Precision%20and%20Scale%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1358807938.1748575402&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9c86f34c-729e-441e-95f8-ab4ce69f83d4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e57e8338-312a-4ecf-ac31-5cc617551bcb&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-qatech%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)