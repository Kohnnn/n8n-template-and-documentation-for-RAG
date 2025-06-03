---
url: "https://qdrant.tech/blog/iris-agent-qdrant/"
title: "IrisAgent and Qdrant: Redefining Customer Support with AI - Qdrant"
---

0

# IrisAgent and Qdrant: Redefining Customer Support with AI

Manuel Meyer

·

March 06, 2024

![IrisAgent and Qdrant: Redefining Customer Support with AI](https://qdrant.tech/blog/iris-agent-qdrant/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Firis-agent-qdrant%2F&text=IrisAgent%20and%20Qdrant:%20Redefining%20Customer%20Support%20with%20AI "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Firis-agent-qdrant%2F "LinkedIn")

Artificial intelligence is evolving customer support, offering unprecedented capabilities for automating interactions, understanding user needs, and enhancing the overall customer experience. [IrisAgent](https://irisagent.com/), founded by former Google product manager [Palak Dalal Bhatia](https://www.linkedin.com/in/palakdalal/), demonstrates the concrete impact of AI on customer support with its AI-powered customer support automation platform.

Bhatia describes IrisAgent as “the system of intelligence which sits on top of existing systems of records like support tickets, engineering bugs, sales data, or product data,” with the main objective of leveraging AI and generative AI, to automatically detect the intent and tags behind customer support tickets, reply to a large number of support tickets chats improve the time to resolution and increase the deflection rate of support teams. Ultimately, IrisAgent enables support teams to more with less and be more effective in helping customers.

## [Anchor](https://qdrant.tech/blog/iris-agent-qdrant/\#the-challenge) The Challenge

Throughout her career Bhatia noticed a lot of manual and inefficient processes in support teams paired with information silos between important functions like customer support, product management, engineering teams, and sales teams. These silos typically prevent support teams from accurately solving customers’ pain points, as they are only able to access a fraction of the internal knowledge and don’t get the relevant information and insights that other teams have.

IrisAgent is addressing these challenges with AI and GenAI by generating meaningful customer experience insights about what the root cause of specific customer escalations or churn. “The platform allows support teams to gather these cross-functional insights and connect them to a single view of customer problems,” Bhatia says. Additionally, IrisAgent facilitates the automation of mundane and repetitive support processes. In the past, these tasks were difficult to automate effectively due to the limitations of early AI technologies. Support functions often depended on rudimentary solutions like legacy decision trees, which suffered from a lack of scalability and robustness, primarily relying on simplistic keyword matching. However, advancements in AI and GenAI technologies have now enabled more sophisticated and efficient automation of these support processes.

## [Anchor](https://qdrant.tech/blog/iris-agent-qdrant/\#the-solution) The Solution

“IrisAgent provides a very holistic product profile, as we are the operating system for support teams,” Bhatia says. The platform includes features like omni-channel customer support automation, which integrates with other parts of the business, such as engineering or sales platforms, to really understand customer escalation points. Long before the advent of technologies such as ChatGPT, IrisAgeny had already been refining and advancing their AI and ML stack. This has enabled them to develop a comprehensive range of machine learning models, including both proprietary solutions and those built on cloud technologies. Through this advancement, IrisAgent was able to finetune on public and private customer data to achieve the level of accuracy that is needed to successfully deflect and resolve customer issues at scale.

![Iris GPT info](https://qdrant.tech/blog/iris-agent-qdrant/iris_gpt.png)

Since IrisAgent built out a lot of their AI related processes in-house with proprietary technology, they wanted to find ways to augment these capabilities with RAG technologies and vector databases. This strategic move was aimed at abstracting much of the technical complexity, thereby simplifying the process for engineers and data scientists on the team to interact with data and develop a variety of solutions built on top of it.

![Quote from CEO of IrisAgent](https://qdrant.tech/blog/iris-agent-qdrant/iris_ceo_quote.png)

“We were looking at a lot of vector databases in the market and one of our core requirements was that the solution needed to be open source because we have a strong emphasis on data privacy and security,” Bhatia says. Also, performance played a key role for IrisAgent during their evaluation as Bhatia mentions: “Despite it being a relatively new project at the time we tested Qdrant, the performance was really good.” Additional evaluation criteria were the ease of ability to deployment, future maintainability, and the quality of available documentation. Ultimately, IrisAgent decided to build with Qdrant as their vector database of choice, given these reasons:

- **Open Source and Flexibility**: IrisAgent required a solution that was open source, to align with their data security needs and preference for self-hosting. Qdrant’s open-source nature allowed IrisAgent to deploy it on their cloud infrastructure seamlessly.
- **Performance**: Early on, IrisAgent recognized Qdrant’s superior performance, despite its relative newness in the market. This performance aspect was crucial for handling large volumes of data efficiently.
- **Ease of Use**: Qdrant’s user-friendly SDKs and compatibility with major programming languages like Go and Python made it an ideal choice for IrisAgent’s engineering team. Additionally, IrisAgent values Qdrant’s the solid documentation, which is easy to follow.
- **Maintainability**: IrisAgent prioritized future maintainability in their choice of Qdrant, notably valuing the robustness and efficiency Rust provides, ensuring a scalable and future-ready solution.

## [Anchor](https://qdrant.tech/blog/iris-agent-qdrant/\#optimizing-irisagents-ai-pipeline-the-evaluation-and-integration-of-qdrant) Optimizing IrisAgent’s AI Pipeline: The Evaluation and Integration of Qdrant

IrisAgent utilizes comprehensive testing and sandbox environments, ensuring no customer data is used during the testing of new features. Initially, they deployed Qdrant in these environments to evaluate its performance, leveraging their own test data and employing Qdrant’s console and SDK features to conduct thorough data exploration and apply various filters. The primary languages used in these processes are Go, for its efficiency, and Python, for its strength in data science tasks.

After the successful testing, Qdrant’s outputs are now integrated into IrisAgent’s AI pipeline, enhancing a suite of proprietary AI models designed for tasks such as detecting hallucinations and similarities, and classifying customer intents. With Qdrant, IrisAgent saw significant performance and quality gains for their RAG use cases. Beyond this, IrisAgent also performs fine-tuning further in the development process.

Qdrant’s emphasis on open-source technology and support for main programming languages (Go and Python) ensures ease of use and compatibility with IrisAgent’s production environment. IrisAgent is deploying Qdrant on Google Cloud in order to fully leverage Google Cloud’s robust infrastructure and innovative offerings.

![Iris agent flow chart](https://qdrant.tech/blog/iris-agent-qdrant/iris_agent_flow_chart.png)

## [Anchor](https://qdrant.tech/blog/iris-agent-qdrant/\#future-of-irisagent) Future of IrisAgent

Looking ahead, IrisAgent is committed to pushing the boundaries of AI in customer support, with ambitious plans to evolve their product further. The cornerstone of this vision is a feature that will allow support teams to leverage historical support data more effectively, by automating the generation of knowledge base content to redefine how FAQs and product documentation are created. This strategic initiative aims not just to reduce manual effort but also to enrich the self-service capabilities of users. As IrisAgent continues to refine its AI algorithms and expand its training datasets, the goal is to significantly elevate the support experience, making it more seamless and intuitive for end-users.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=76845615-bcc9-4059-8695-45b848fdaca5)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574783893&cv=11&fst=1748574783893&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Firis-agent-qdrant%2F&hn=www.googleadservices.com&frm=0&tiba=IrisAgent%20and%20Qdrant%3A%20Redefining%20Customer%20Support%20with%20AI%20-%20Qdrant&npa=0&pscdl=noapi&auid=1254288948.1748574784&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574783872&cv=11&fst=1748574783872&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Firis-agent-qdrant%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=IrisAgent%20and%20Qdrant%3A%20Redefining%20Customer%20Support%20with%20AI%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1254288948.1748574784&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9af4b585-fd21-4104-8ec7-24a36e74b333&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1a54cbc1-25d3-4be5-8461-cac1007f57fc&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Firis-agent-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9af4b585-fd21-4104-8ec7-24a36e74b333&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1a54cbc1-25d3-4be5-8461-cac1007f57fc&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Firis-agent-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=012ac40a6040b5fdf4673bc060382af5&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574784929&cv=11&fst=1748574784929&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Firis-agent-qdrant%2F&hn=www.googleadservices.com&frm=0&tiba=IrisAgent%20and%20Qdrant%3A%20Redefining%20Customer%20Support%20with%20AI%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1254288948.1748574784&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)