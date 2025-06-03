---
url: "https://qdrant.tech/blog/case-study-deutsche-telekom/"
title: "How Deutsche Telekom Built a Multi-Agent Enterprise Platform Leveraging Qdrant - Qdrant"
---

0

# How Deutsche Telekom Built a Multi-Agent Enterprise Platform Leveraging Qdrant

Manuel Meyer

·

March 07, 2025

![How Deutsche Telekom Built a Multi-Agent Enterprise Platform Leveraging Qdrant](https://qdrant.tech/blog/case-study-deutsche-telekom/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-deutsche-telekom%2F&text=How%20Deutsche%20Telekom%20Built%20a%20Multi-Agent%20Enterprise%20Platform%20Leveraging%20Qdrant "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-deutsche-telekom%2F "LinkedIn")

**How Deutsche Telekom Built a Scalable, Multi-Agent Enterprise Platform Leveraging Qdrant—Powering Over 2 Million Conversations Across Europe**

![Deutsche Telekom’s AI Competence Center team leading the LMOS platform development](https://qdrant.tech/blog/case-study-deutsche-telekom/dtag-team.jpg)

[Arun Joseph](https://www.linkedin.com/in/arun-joseph-ab47102a/), who leads engineering and architecture for [Deutsche Telekom’s AI Competence Center (AICC)](https://www.telekom.com/en/company/digital-responsibility/details/artificial-intelligence-at-deutsche-telekom-1055154), faced a critical challenge: how do you efficiently and scalably deploy AI-powered assistants across a vast enterprise ecosystem? The goal was to deploy GenAI for customer sales and service operations to resolve customer queries faster across the 10 countries where Deutsche Telekom operates in Europe.

To achieve this, Telekom developed [_Frag Magenta OneBOT_](https://www.telekom.de/hilfe/frag-magenta?samChecked=true) _(Eng: Ask Magenta)_, a platform that includes chatbots and voice bots, built as a Platform as a Service (PaaS) to ensure scalability across Deutsche Telekom’s ten European subsidiaries.

“We knew from the start that we couldn’t just deploy RAG, tool calling, and workflows at scale without a platform-first approach,” Arun explains. “When I looked at the challenge, it looked a lot like a distributed systems and engineering challenge, not just an AI problem.”

### [Anchor](https://qdrant.tech/blog/case-study-deutsche-telekom/\#key-requirements-for-scaling-enterprise-ai-agents) Key Requirements for Scaling Enterprise AI Agents

While flashy AI demos are easy to build, Deutsche Telekom’s team quickly discovered that scaling AI agents for enterprise use presents a far more complex challenge. “This isn’t just about AI,” Arun explains. “It’s a distributed systems problem that requires rigorous engineering.” Based on their experience deploying AI across multiple regions, they identified three key challenges in scaling AI agents in production:

1. **Handling Tenancy & Memory Management:** AI workloads spanning 10 different countries require strict data segregation and compliance.
2. **Horizontal Scaling & Context Sharing**: AI agents require real-time processing while maintaining historical context, so efficiently storing, retrieving, and processing AI-generated context at scale is critical.
3. **Non-Deterministic Agent Collaboration:** AI agents often exhibit unpredictable behavior, making seamless inter-agent communication and workflow orchestration complex.

“From our experience, these challenges are fundamentally distributed systems problems, not just AI problems,” Arun explains. “We need feedback loops, state management, lifecycle orchestration, and intelligent routing for staggered rollouts. Microservices alone aren’t enough — we need a domain-driven approach to AI agent design.”

This insight led to the formation of [LMOS as an open-source Eclipse Foundation project](https://eclipse.dev/lmos/). Now, other companies can leverage LMOS for their own AI agent development.

### [Anchor](https://qdrant.tech/blog/case-study-deutsche-telekom/\#why-deutsche-telekom-had-to-rethink-its-ai-stack-from-the-ground-up) Why Deutsche Telekom Had to Rethink Its AI Stack from the Ground Up

The team started its journey in June 2023 with a small-scale Generative AI initiative, focusing on chatbots with customized AI models. Initially, they used LangChain and a major vector database provider for vector search and retrieval, alongside a custom Dense Passage Retrieval (DPR) model fine-tuned for German language use cases.

However, as they scaled, these issues quickly emerged:

- Memory spikes and operational instability due to the sheer number of components used in the previous provide
- Complex maintenance requirements, with frequent dependency issues, high operational overhead due to missing memory optimizations, and streamlined deployment.

Despite efforts to improve annotations and tuning, it became evident that this approach wouldn’t scale for Deutsche Telekom.

Additionally, there was a strong need to leverage existing engineering assets, as most developers and systems were already equipped with SDKs and familiar tooling. Rather than building an entirely new stack from scratch, the focus shifted to enabling developers to build AI agents within the tools and frameworks they were already comfortable with. This approach allowed domain experts who understood the APIs and enterprise systems to quickly develop AI agents without disrupting existing workflows.

Recognizing this, the team made a bold decision: to build a **fully-fledged PaaS platform for AI agents**, streamlining development and accelerating deployment of AI Agents.

### [Anchor](https://qdrant.tech/blog/case-study-deutsche-telekom/\#lmos-deutsche-telekoms-open-source-multi-agent-ai-paas-for-enterprise-ai) LMOS: Deutsche Telekom’s Open-Source Multi-Agent AI PaaS for Enterprise AI

Recognizing that an AI-driven platform required deep engineering rigor, the Telekom team designed **LMOS (Language Models Operating System)** — a multi-agent PaaS designed for high scalability and modular AI agent deployment. Key technical decisions included:

- **Choosing Kotlin and JVM** to ensure engineers familiar with existing Deutsche Telekom systems could easily integrate with LMOS.
- **Moving away from pre-built frameworks** in favor of a ground-up, highly optimized solution tailored to Deutsche Telekom’s specific needs.
- **Providing a Heroku-like experience** where engineers don’t need to worry about classifiers, agent lifecycles, deployment models, monitoring, and horizontal scaling.
- **Enterprise Grade while being flexible:** LMOS was built with enterprise-grade scalability, versioning, and multi-tenancy in mind, while also offering the flexibility to integrate agents from other frameworks — not just JVM-based solutions — ensuring interoperability across diverse AI ecosystems.

“Our engineers already knew their APIs — billing, shopping, user profiles. Why should we introduce new abstractions that only complicate the stack?” Arun notes, “also, I envisioned us building the foundations of what I call **agentic computing**, playing a role in shaping the application stacks of the future on top of LLMs.”

![LMOS architecture diagram showing AI agent collaboration and lifecycle management](https://qdrant.tech/blog/case-study-deutsche-telekom/lmos-architecture.png)

LMOS architecture powering AI agent collaboration and lifecycle management in a cloud-native environment.

### [Anchor](https://qdrant.tech/blog/case-study-deutsche-telekom/\#why-qdrant-finding-the-right-vector-database-for-lmos) Why Qdrant? Finding the Right Vector Database for LMOS

When Deutsche Telekom began searching for a scalable, high-performance vector database, they faced operational challenges with their initial choice. Seeking a solution better suited to their PaaS-first approach and multitenancy requirements, they evaluated alternatives, and [Qdrant](https://qdrant.tech/qdrant-vector-database/) quickly stood out.

“I was looking for open-source components with deep technical expertise behind them,” Arun recalls. “I looked at Qdrant and immediately loved the simplicity, [Rust-based efficiency](https://qdrant.tech/articles/why-rust/), and [memory management capabilities](https://qdrant.tech/articles/memory-consumption/). These guys knew what they were doing.”

The team structured its evaluation around two key metrics:

1. **Qualitative metrics**: developer experience, ease of use, memory efficiency features.
2. **Operational simplicity**: how well it fit into their PaaS-first approach and [multitenancy requirements](https://qdrant.tech/documentation/guides/multiple-partitions/).

Deutsche Telekom’s engineers also cited several standout features that made Qdrant the right fit:

1. **Simplicity in operations**—Qdrant is lightweight and doesn’t require an excessive component stack.
2. **Developer experience**—libraries, multi-language clients, and cross-framework support make integrations seamless.
3. **WebUI & Collection Visualization**—engineers found Qdrant’s [built-in collection visualization](https://qdrant.tech/documentation/web-ui/) tools highly useful.

As part of their evaluation, Deutsche Telekom engineers compared multiple solutions, weighing operational simplicity and reliability.

One engineer summarized their findings: “Qdrant has way fewer components, compared to the another that required required Kafka, Zookeeper, and only had a hot standby for its index and query nodes. If you rescale it, you get downtime. Qdrant stays up.”

### [Anchor](https://qdrant.tech/blog/case-study-deutsche-telekom/\#scaling-ai-at-deutsche-telekom--the-future-of-lmos) Scaling AI at Deutsche Telekom & The Future of LMOS

Today, LMOS with Qdrant serves as the backbone for Deutsche Telekom’s AI services, processing over 2 million conversations across three countries. The time required to develop a new agent has dropped from 15 days to just 2.

With [LMOS now part of the Eclipse Foundation](https://projects.eclipse.org/projects/technology.lmos), Deutsche Telekom is opening up its platform to the broader AI engineering community. Arun sees a future ecosystem of like-minded developers coalescing around LMOS, Qdrant, and other AI infrastructure components.

“For enterprises looking to build their own AI agent platforms, the future isn’t just about AI models — it’s about scalable, open, and opinionated infrastructure. And that’s exactly what we’ve built,” says Arun Joseph.

You can learn more about Deutsche Telekom’s AI Agents and Arun’s vision for LMOS in his [talk](https://www.infoq.com/presentations/ai-agents-platform%20) at the InfoQ Dev Summit Boston.

### [Anchor](https://qdrant.tech/blog/case-study-deutsche-telekom/\#watch-livestream-with-arun) Watch livestream with Arun

In this Vector Space talk, Thierry from Qdrant and Arun from Deutsche Telekom talk about the key requirements for scaling enterprise AI agents, key AI stack considerations, and how the team built a Platform as a Service (PaaS) - LMOS (Language Models Operating System) — a multi-agent PaaS designed for high scalability and modular AI agent deployment.

How Deutsche Telekom Scaled an Enterprise Multi-Agent Platform w/ Qdrant, Powering 2M+ Convos - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[How Deutsche Telekom Scaled an Enterprise Multi-Agent Platform w/ Qdrant, Powering 2M+ Convos](https://www.youtube.com/watch?v=l_4EDFqx1qk)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=l_4EDFqx1qk&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 1:01:42
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=l_4EDFqx1qk "Watch on YouTube")

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=d4b07ce0-8012-4d55-95b5-a011c7746daa)

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

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-deutsche-telekom%2F&portalId=139603372&pageTitle=How+Deutsche+Telekom+Built+a+Multi-Agent+Enterprise+Platform+Leveraging+Qdrant+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=0c77cb3528cd969b6d8eb13df3ae35b0&hssc=265983056.1.1748574961390&hstc=265983056.0c77cb3528cd969b6d8eb13df3ae35b0.1748574961390.1748574961390.1748574961390.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-deutsche-telekom%2F&pageTitle=How+Deutsche+Telekom+Built+a+Multi-Agent+Enterprise+Platform+Leveraging+Qdrant+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=0c77cb3528cd969b6d8eb13df3ae35b0&hssc=265983056.1.1748574961390&hstc=265983056.0c77cb3528cd969b6d8eb13df3ae35b0.1748574961390.1748574961390.1748574961390.1&hsfp=3707738794).

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=44caac85-061f-45b1-ae76-73044ff90d76&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4b2b21d6-b958-4fb4-ae9d-aaaf91f5d9d9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-deutsche-telekom%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=44caac85-061f-45b1-ae76-73044ff90d76&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4b2b21d6-b958-4fb4-ae9d-aaaf91f5d9d9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-deutsche-telekom%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)