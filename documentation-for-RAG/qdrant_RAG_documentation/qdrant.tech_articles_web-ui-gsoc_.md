---
url: "https://qdrant.tech/articles/web-ui-gsoc/"
title: "Google Summer of Code 2023 - Web UI for Visualization and Exploration - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Google Summer of Code 2023 - Web UI for Visualization and Exploration

[Back to Ecosystem](https://qdrant.tech/articles/ecosystem/)

# Google Summer of Code 2023 - Web UI for Visualization and Exploration

Kartik Gupta

·

August 28, 2023

![Google Summer of Code 2023 - Web UI for Visualization and Exploration](https://qdrant.tech/articles_data/web-ui-gsoc/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#introduction) Introduction

Hello everyone! My name is Kartik Gupta, and I am thrilled to share my coding journey as part of the Google Summer of Code 2023 program. This summer, I had the incredible opportunity to work on an exciting project titled “Web UI for Visualization and Exploration” for Qdrant, a vector search engine. In this article, I will take you through my experience, challenges, and achievements during this enriching coding journey.

## [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#project-overview) Project Overview

Qdrant is a powerful vector search engine widely used for similarity search and clustering. However, it lacked a user-friendly web-based UI for data visualization and exploration. My project aimed to bridge this gap by developing a web-based user interface that allows users to easily interact with and explore their vector data.

## [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#milestones-and-achievements) Milestones and Achievements

The project was divided into six milestones, each focusing on a specific aspect of the web UI development. Let’s go through each of them and my achievements during the coding period.

**1\. Designing a friendly UI on Figma**

I started by designing the user interface on Figma, ensuring it was easy to use, visually appealing, and responsive on different devices. I focused on usability and accessibility to create a seamless user experience. ( [Figma Design](https://www.figma.com/file/z54cAcOErNjlVBsZ1DrXyD/Qdant?type=design&node-id=0-1&mode=design&t=Pu22zO2AMFuGhklG-0))

**2\. Building the layout**

The layout route served as a landing page with an overview of the application’s features and navigation links to other routes.

**3\. Creating a view collection route**

This route enabled users to view a list of collections available in the application. Users could click on a collection to see more details, including the data and vectors associated with it.

![Collection Page](https://qdrant.tech/articles_data/web-ui-gsoc/collections-page.png)

Collection Page

**4\. Developing a data page with “find similar” functionality**

I implemented a data page where users could search for data and find similar data using a recommendation API. The recommendation API suggested similar data based on the Data’s selected ID, providing valuable insights.

![Points Page](https://qdrant.tech/articles_data/web-ui-gsoc/points-page.png)

Points Page

**5\. Developing query editor page libraries**

This milestone involved creating a query editor page that allowed users to write queries in a custom language. The editor provided syntax highlighting, autocomplete, and error-checking features for a seamless query writing experience.

![Query Editor Page](https://qdrant.tech/articles_data/web-ui-gsoc/console-page.png)

Query Editor Page

**6\. Developing a route for visualizing vector data points**

This is done by the reduction of n-dimensional vector in 2-D points and they are displayed with their respective payloads.

![visualization-page](https://qdrant.tech/articles_data/web-ui-gsoc/visualization-page.png)

Vector Visuliztion Page

## [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#challenges-and-learning) Challenges and Learning

Throughout the project, I encountered a series of challenges that stretched my engineering capabilities and provided unique growth opportunities. From mastering new libraries and technologies to ensuring the user interface (UI) was both visually appealing and user-friendly, every obstacle became a stepping stone toward enhancing my skills as a developer. However, each challenge provided an opportunity to learn and grow as a developer. I acquired valuable experience in vector search and dimension reduction techniques.

The most significant learning for me was the importance of effective project management. Setting realistic timelines, collaborating with mentors, and staying proactive with feedback allowed me to complete the milestones efficiently.

### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#technical-learning-and-skill-development) Technical Learning and Skill Development

One of the most significant aspects of this journey was diving into the intricate world of vector search and dimension reduction techniques. These areas, previously unfamiliar to me, required rigorous study and exploration. Learning how to process vast amounts of data efficiently and extract meaningful insights through these techniques was both challenging and rewarding.

### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#effective-project-management) Effective Project Management

Undoubtedly, the most impactful lesson was the art of effective project management. I quickly grasped the importance of setting realistic timelines and goals. Collaborating closely with mentors and maintaining proactive communication proved indispensable. This approach enabled me to navigate the complex development process and successfully achieve the project’s milestones.

### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#overcoming-technical-challenges) Overcoming Technical Challenges

#### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#autocomplete-feature-in-console) Autocomplete Feature in Console

One particularly intriguing challenge emerged while working on the autocomplete feature within the console. Finding a solution was proving elusive until a breakthrough came from an unexpected direction. My mentor, Andrey, proposed creating a separate module that could support autocomplete based on OpenAPI for our custom language. This ingenious approach not only resolved the issue but also showcased the power of collaborative problem-solving.

#### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#optimization-with-web-workers) Optimization with Web Workers

The high-processing demands of vector reduction posed another significant challenge. Initially, this task was straining browsers and causing performance issues. The solution materialized in the form of web workers—an independent processing instance that alleviated the strain on browsers. However, a new question arose: how to terminate these workers effectively? With invaluable insights from my mentor, I gained a deeper understanding of web worker dynamics and successfully tackled this challenge.

#### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#console-integration-complexity) Console Integration Complexity

Integrating the console interaction into the application presented multifaceted challenges. Crafting a custom language in Monaco, parsing text to make API requests, and synchronizing the entire process demanded meticulous attention to detail. Overcoming these hurdles was a testament to the complexity of real-world engineering endeavours.

#### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#codelens-multiplicity-issue) Codelens Multiplicity Issue

An unexpected issue cropped up during the development process: the codelen (run button) registered multiple times, leading to undesired behaviour. This hiccup underscored the importance of thorough testing and debugging, even in seemingly straightforward features.

### [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#key-learning-points) Key Learning Points

Amidst these challenges, I garnered valuable insights that have significantly enriched my engineering prowess:

**Vector Reduction Techniques**: Navigating the realm of vector reduction techniques provided a deep understanding of how to process and interpret data efficiently. This knowledge opens up new avenues for developing data-driven applications in the future.

**Web Workers Efficiency**: Mastering the intricacies of web workers not only resolved performance concerns but also expanded my repertoire of optimization strategies. This newfound proficiency will undoubtedly find relevance in various future projects.

**Monaco Editor and UI Frameworks**: Working extensively with the Monaco Editor, Material-UI (MUI), and Vite enriched my familiarity with these essential tools. I honed my skills in integrating complex UI components seamlessly into applications.

## [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#areas-for-improvement-and-future-enhancements) Areas for Improvement and Future Enhancements

While reflecting on this transformative journey, I recognize several areas that offer room for improvement and future enhancements:

1. Enhanced Autocomplete: Further refining the autocomplete feature to support key-value suggestions in JSON structures could greatly enhance the user experience.

2. Error Detection in Console: Integrating the console’s error checker with OpenAPI could enhance its accuracy in identifying errors and offering precise suggestions for improvement.

3. Expanded Vector Visualization: Exploring additional visualization methods and optimizing their performance could elevate the utility of the vector visualization route.


## [Anchor](https://qdrant.tech/articles/web-ui-gsoc/\#conclusion) Conclusion

Participating in the Google Summer of Code 2023 and working on the “Web UI for Visualization and Exploration” project has been an immensely rewarding experience. I am grateful for the opportunity to contribute to Qdrant and develop a user-friendly interface for vector data exploration.

I want to express my gratitude to my mentors and the entire Qdrant community for their support and guidance throughout this journey. This experience has not only improved my coding skills but also instilled a deeper passion for web development and data analysis.

As my coding journey continues beyond this project, I look forward to applying the knowledge and experience gained here to future endeavours. I am excited to see how Qdrant evolves with the newly developed web UI and how it positively impacts users worldwide.

Thank you for joining me on this coding adventure, and I hope to share more exciting projects in the future! Happy coding!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/web-ui-gsoc.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/web-ui-gsoc.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575253707&cv=11&fst=1748575253707&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fweb-ui-gsoc%2F&hn=www.googleadservices.com&frm=0&tiba=Google%20Summer%20of%20Code%202023%20-%20Web%20UI%20for%20Visualization%20and%20Exploration%20-%20Qdrant&npa=0&pscdl=noapi&auid=1409301134.1748575253&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575253617&cv=11&fst=1748575253617&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fweb-ui-gsoc%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Google%20Summer%20of%20Code%202023%20-%20Web%20UI%20for%20Visualization%20and%20Exploration%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1409301134.1748575253&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1fe1813c-ec89-4ed4-9c5d-bfd7af94f214&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d4fac0d8-08cb-4024-ae31-4a169124a9a1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fweb-ui-gsoc%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1fe1813c-ec89-4ed4-9c5d-bfd7af94f214&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d4fac0d8-08cb-4024-ae31-4a169124a9a1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fweb-ui-gsoc%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)