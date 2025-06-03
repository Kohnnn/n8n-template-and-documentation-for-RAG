---
url: "https://qdrant.tech/blog/case-study-voiceflow/"
title: "Voiceflow & Qdrant: Powering No-Code AI Agent Creation with Scalable Vector Search - Qdrant"
---

0

# Voiceflow & Qdrant: Powering No-Code AI Agent Creation with Scalable Vector Search

Qdrant

·

December 10, 2024

![Voiceflow & Qdrant: Powering No-Code AI Agent Creation with Scalable Vector Search](https://qdrant.tech/blog/case-study-voiceflow/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-voiceflow%2F&text=Voiceflow%20&%20Qdrant:%20Powering%20No-Code%20AI%20Agent%20Creation%20with%20Scalable%20Vector%20Search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-voiceflow%2F "LinkedIn")

![voiceflow/image2.png](https://qdrant.tech/blog/case-study-voiceflow/image1.png)

[Voiceflow](https://www.voiceflow.com/) enables enterprises to create AI agents in a no-code environment by designing workflows through a drag-and-drop interface. The platform allows developers to host and customize chatbot interfaces without needing to build their own RAG pipeline, working out of the box and being easily adaptable to specific use cases. “Powered by technologies like Natural Language Understanding (NLU), Large Language Models (LLM), and Qdrant as a vector search engine, Voiceflow serves a diverse range of customers, including enterprises that develop chatbots for internal and external AI use cases,” says [Xavier Portillo Edo](https://www.linkedin.com/in/xavierportillaedo/), Head of Cloud Infrastructure at Voiceflow.

## [Anchor](https://qdrant.tech/blog/case-study-voiceflow/\#evaluation-criteria) Evaluation Criteria

[Denys Linkov](https://www.linkedin.com/in/denyslinkov/), Machine Learning Team Lead at Voiceflow, explained the journey of building a managed RAG solution. “Initially, our product focused on users manually defining steps on the canvas. After the release of ChatGPT, we added AI-based responses, leading to the launch of our managed RAG solution in the spring of 2023,” Linkov said.

As part of this development, the Voiceflow engineering team was looking for a [vector database](https://qdrant.tech/qdrant-vector-database/) solution to power their RAG setup. They evaluated various vector databases based on several key factors:

- **Performance**: The ability to [handle the scale](https://qdrant.tech/documentation/guides/distributed_deployment/) required by Voiceflow, supporting hundreds of thousands of projects efficiently.
- **Metadata**: The capability to tag data and chunks and retrieve based on those values, essential for organizing and accessing specific information swiftly.
- **Managed Solution**: The availability of a [managed service](https://qdrant.tech/documentation/cloud/) with automated maintenance, scaling, and security, freeing the team from infrastructure concerns.

_“We started with Pinecone but eventually switched to Qdrant,”_ Linkov noted. The reasons for the switch included:

- **Scaling Capabilities**: Qdrant offers a robust multi-node setup with [horizontal scaling](https://qdrant.tech/documentation/cloud/cluster-scaling/), allowing clusters to grow by adding more nodes and distributing data and load among them. This ensures high performance and resilience, which is crucial for handling large-scale projects.
- **Infrastructure**: “Qdrant provides robust infrastructure support, allowing integration with virtual private clouds on AWS using AWS Private Links and ensuring encryption with AWS KMS. This setup ensures high security and reliability,” says Portillo Edo.
- **Responsive Qdrant Team**: “The Qdrant team is very responsive, ships features quickly and is a great partner to build with,” Linkov added.

## [Anchor](https://qdrant.tech/blog/case-study-voiceflow/\#migration-and-onboarding) Migration and Onboarding

Voiceflow began its migration to Qdrant by creating [backups](https://qdrant.tech/documentation/cloud/backups/) and ensuring data consistency through random checks and key customer verifications. “Once we were confident in the stability, we transitioned the primary database to Qdrant, completing the migration smoothly,” Linkov explained.

During onboarding, Voiceflow transitioned from namespaces to Qdrant’s collections, which offer enhanced flexibility and advanced vector search capabilities. They also implemented Quantization to enhance data processing efficiency. This comprehensive process ensured a seamless transition to Qdrant’s robust infrastructure.

## [Anchor](https://qdrant.tech/blog/case-study-voiceflow/\#rag-pipeline-setup) RAG Pipeline Setup

Voiceflow’s RAG pipeline setup provides a streamlined process for uploading and managing data from various sources, designed to offer flexibility and customization at each step.

- **Data Upload**: Customers can upload data via API from sources such as URLs, PDFs, Word documents, and plain text formats. Integration with platforms like Zendesk is supported, and users can choose between single uploads or refresh-based uploads.
- **Data Ingestion**: Once data is ingested, Voiceflow offers preset strategies for data checking. Users can utilize these strategies or opt for more customization through the API to tailor the ingestion process as needed.
- **Metadata Tagging**: Metadata tags can be applied during the ingestion process, which helps organize and facilitate efficient data retrieval later on.
- **Data Retrieval**: At retrieval time, Voiceflow provides prompts that can modify user questions by adding context, variables, or other modifications. This customization includes adding personas or structuring responses as markdown. Depending on the type of interaction (e.g., button, carousel with an image for image retrieval), these prompts are displayed to users in a structured format.

This comprehensive setup ensures that Voiceflow users can efficiently manage and customize their data workflows, providing a robust solution for building AI-driven applications.

## [Anchor](https://qdrant.tech/blog/case-study-voiceflow/\#how-voiceflow-uses-qdrant) How Voiceflow Uses Qdrant

Voiceflow leverages Qdrant’s robust features and infrastructure to optimize their AI assistant platform. Here’s a breakdown of how they utilize these capabilities:

_Database Features:_

- **Quantization**: This feature helps Voiceflow to perform efficient data processing by reducing the size of vectors, making searches faster. The team uses [Product Quantization](https://qdrant.tech/articles/product-quantization/) in particular.
- **Chunking Search**: Voiceflow uses chunking search to improve search efficiency by breaking down large datasets into manageable chunks, which allows for faster and more efficient data retrieval.
- **Sparse Vector Search**: Although not yet implemented, this feature is being explored for more precise keyword searches. “This is an encouraging direction the Qdrant team is taking here as many users seek more exact keyword search,” said Linkov.

_Architecture:_

- **Node Pool**: A large node pool is used for public cloud users, ensuring scalability, while several smaller, isolated instances cater to private cloud users, providing enhanced security.

_Infrastructure:_

- **Private Link**: The ability to use Private Link connections across different instances is a significant advantage, requiring robust infrastructure support from Qdrant. “This setup was crucial for SOC2 compliance, and Qdrant’s support team made the process seamless by ensuring feasibility and aiding in the implementation,” Linkov explained.

By utilizing these features, Voiceflow ensures that its platform is scalable, secure, and efficient, meeting the diverse needs of its users.

## [Anchor](https://qdrant.tech/blog/case-study-voiceflow/\#the-outcome) The Outcome

Voiceflow achieved significant improvements and efficiencies by leveraging Qdrant’s capabilities:

- **Enhanced Metadata Tagging**: Implemented robust metadata tagging, allowing for custom fields and tags that facilitate efficient search filtering.
- **Optimized Performance**: Resolved concerns about retrieval times with a high number of tags by optimizing indexing strategies, achieving efficient performance.
- **Minimal Operational Overhead**: Experienced minimal overhead, streamlining their operational processes.
- **Future-Ready**: Anticipates further innovation in hybrid search with multi-token attention.
- **Multitenancy Support**: Utilized Qdrant’s efficient and [isolated data management](https://qdrant.tech/documentation/guides/multiple-partitions/) to support diverse user needs.

Overall, Qdrant’s features and infrastructure provided Voiceflow with a stable, scalable, and efficient solution for their data processing and retrieval needs.

## [Anchor](https://qdrant.tech/blog/case-study-voiceflow/\#whats-next) What’s Next

Voiceflow plans to enhance its platform with more filtering and customization options, allowing developers to host and customize chatbot interfaces without building their own [RAG](https://qdrant.tech/rag/) pipeline.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=709a6a45-0dc9-401f-8f4e-448ccc58e316)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574472867&cv=11&fst=1748574472867&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-voiceflow%2F&hn=www.googleadservices.com&frm=0&tiba=Voiceflow%20%26%20Qdrant%3A%20Powering%20No-Code%20AI%20Agent%20Creation%20with%20Scalable%20Vector%20Search%20-%20Qdrant&npa=0&pscdl=noapi&auid=1664791584.1748574473&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574472802&cv=11&fst=1748574472802&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-voiceflow%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Voiceflow%20%26%20Qdrant%3A%20Powering%20No-Code%20AI%20Agent%20Creation%20with%20Scalable%20Vector%20Search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1664791584.1748574473&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=011a6697-e859-41cb-929e-ff0b88c76d55&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a2c06be6-8685-403e-8b41-7036de262d57&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-voiceflow%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=011a6697-e859-41cb-929e-ff0b88c76d55&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a2c06be6-8685-403e-8b41-7036de262d57&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-voiceflow%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574473720&cv=11&fst=1748574473720&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-voiceflow%2F&hn=www.googleadservices.com&frm=0&tiba=Voiceflow%20%26%20Qdrant%3A%20Powering%20No-Code%20AI%20Agent%20Creation%20with%20Scalable%20Vector%20Search%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1664791584.1748574473&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)