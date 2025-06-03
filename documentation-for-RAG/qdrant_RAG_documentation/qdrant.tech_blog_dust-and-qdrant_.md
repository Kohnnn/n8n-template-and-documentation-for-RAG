---
url: "https://qdrant.tech/blog/dust-and-qdrant/"
title: "Dust and Qdrant: Using AI to Unlock Company Knowledge and Drive Employee Productivity - Qdrant"
---

0

# Dust and Qdrant: Using AI to Unlock Company Knowledge and Drive Employee Productivity

Manuel Meyer

·

February 06, 2024

![Dust and Qdrant: Using AI to Unlock Company Knowledge and Drive Employee Productivity](https://qdrant.tech/blog/dust-and-qdrant/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fdust-and-qdrant%2F&text=Dust%20and%20Qdrant:%20Using%20AI%20to%20Unlock%20Company%20Knowledge%20and%20Drive%20Employee%20Productivity "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fdust-and-qdrant%2F "LinkedIn")

One of the major promises of artificial intelligence is its potential to
accelerate efficiency and productivity within businesses, empowering employees
and teams in their daily tasks. The French company [Dust](https://dust.tt/), co-founded by former
Open AI Research Engineer [Stanislas Polu](https://www.linkedin.com/in/spolu/), set out to deliver on this promise by
providing businesses and teams with an expansive platform for building
customizable and secure AI assistants.

## [Anchor](https://qdrant.tech/blog/dust-and-qdrant/\#challenge) Challenge

“The past year has shown that large language models (LLMs) are very useful but
complicated to deploy,” Polu says, especially in the context of their
application across business functions. This is why he believes that the goal of
augmenting human productivity at scale is especially a product unlock and not
only a research unlock, with the goal to identify the best way for companies to
leverage these models. Therefore, Dust is creating a product that sits between
humans and the large language models, with the focus on supporting the work of
a team within the company to ultimately enhance employee productivity.

A major challenge in leveraging leading LLMs like OpenAI, Anthropic, or Mistral
to their fullest for employees and teams lies in effectively addressing a
company’s wide range of internal use cases. These use cases are typically very
general and fluid in nature, requiring the use of very large language models.
Due to the general nature of these use cases, it is very difficult to finetune
the models - even if financial resources and access to the model weights are
available. The main reason is that “the data that’s available in a company is
a drop in the bucket compared to the data that is needed to finetune such big
models accordingly,” Polu says, “which is why we believe that retrieval
augmented generation is the way to go until we get much better at fine tuning”.

For successful retrieval augmented generation (RAG) in the context of employee
productivity, it is important to get access to the company data and to be able
to ingest the data that is considered ‘shared knowledge’ of the company. This
data usually sits in various SaaS applications across the organization.

## [Anchor](https://qdrant.tech/blog/dust-and-qdrant/\#solution) Solution

Dust provides companies with the core platform to execute on their GenAI bet
for their teams by deploying LLMs across the organization and providing context
aware AI assistants through [RAG](https://qdrant.tech/rag/rag-evaluation-guide/)
. Users can manage so-called data sources within
Dust and upload files or directly connect to it via APIs to ingest data from
tools like Notion, Google Drive, or Slack. Dust then handles the chunking
strategy with the embeddings models and performs retrieval augmented generation.

![solution-laptop-screen](https://qdrant.tech/case-studies/dust/laptop-solutions.jpg)

For this, Dust required a vector database and evaluated different options
including Pinecone and Weaviate, but ultimately decided on Qdrant as the
solution of choice. “We particularly liked Qdrant because it is open-source,
written in Rust, and it has a well-designed API,” Polu says. For example, Dust
was looking for high control and visibility in the context of their rapidly
scaling demand, which made the fact that Qdrant is open-source a key driver for
selecting Qdrant. Also, Dust’s existing system which is interfacing with Qdrant,
is written in Rust, which allowed Dust to create synergies with regards to
library support.

When building their solution with Qdrant, Dust took a two step approach:

1. **Get started quickly:** Initially, Dust wanted to get started quickly and opted for
[Qdrant Cloud](https://qdrant.to/cloud), Qdrant’s managed solution, to reduce the administrative load on
Dust’s end. In addition, they created clusters and deployed them on Google
Cloud since Dust wanted to have those run directly in their existing Google
Cloud environment. This added a lot of value as it allowed Dust to centralize
billing and increase security by having the instance live within the same VPC.
“The early setup worked out of the box nicely,” Polu says.

2. **Scale and optimize:** As the load grew, Dust started to take advantage of Qdrant’s
features to tune the setup for optimization and scale. They started to look into
how they map and cache data, as well as applying some of Qdrant’s [built-in\\
compression features](https://qdrant.tech/documentation/guides/quantization/). In particular, Dust leveraged the control of the [MMAP\\
payload threshold](https://qdrant.tech/documentation/concepts/storage/#configuring-memmap-storage) as well as [Scalar Quantization](https://qdrant.tech/articles/scalar-quantization/), which enabled Dust to manage
the balance between storing vectors on disk and keeping quantized vectors in RAM,
more effectively. “This allowed us to scale smoothly from there,” Polu says.


## [Anchor](https://qdrant.tech/blog/dust-and-qdrant/\#results) Results

Dust has seen success in using Qdrant as their vector database of choice, as Polu
acknowledges: “Qdrant’s ability to handle large-scale models and the flexibility
it offers in terms of data management has been crucial for us. The observability
features, such as historical graphs of RAM, Disk, and CPU, provided by Qdrant are
also particularly useful, allowing us to plan our scaling strategy effectively.”

![“We were able to reduce the footprint of vectors in memory, which led to a significant cost reduction as we don’t have to run lots of nodes in parallel. While being memory-bound, we were able to push the same instances further with the help of quantization. While you get pressure on MMAP in this case you maintain very good performance even if the RAM is fully used. With this we were able to reduce our cost by 2x.” - Stanislas Polu, Co-Founder of Dust](https://qdrant.tech/case-studies/dust/Dust-Quote.jpg)

Dust was able to scale its application with Qdrant while maintaining low latency
across hundreds of thousands of collections with retrieval only taking
milliseconds, as well as maintaining high accuracy. Additionally, Polu highlights
the efficiency gains Dust was able to unlock with Qdrant: “We were able to reduce the footprint of vectors in memory, which led to a significant cost reduction as
we don’t have to run lots of nodes in parallel. While being memory-bound, we were
able to push the same instances further with the help of quantization. While you
get pressure on MMAP in this case you maintain very good performance even if the
RAM is fully used. With this we were able to reduce our cost by 2x.”

## [Anchor](https://qdrant.tech/blog/dust-and-qdrant/\#outlook) Outlook

Dust will continue to build out their platform, aiming to be the platform of
choice for companies to execute on their internal GenAI strategy, unlocking
company knowledge and driving team productivity. Over the coming months, Dust
will add more connections, such as Intercom, Jira, or Salesforce. Additionally,
Dust will expand on its structured data capabilities.

To learn more about how Dust uses Qdrant to help employees in their day to day
tasks, check out our [Vector Space Talk](https://www.youtube.com/watch?v=toIgkJuysQ4) featuring Stanislas Polu, Co-Founder of Dust.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=ad097a1f-e975-4f32-b864-8137a442f1f9)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574839046&cv=11&fst=1748574839046&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fdust-and-qdrant%2F&hn=www.googleadservices.com&frm=0&tiba=Dust%20and%20Qdrant%3A%20Using%20AI%20to%20Unlock%20Company%20Knowledge%20and%20Drive%20Employee%20Productivity%20-%20Qdrant&npa=0&pscdl=noapi&auid=1903244805.1748574839&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574839036&cv=11&fst=1748574839036&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fdust-and-qdrant%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Dust%20and%20Qdrant%3A%20Using%20AI%20to%20Unlock%20Company%20Knowledge%20and%20Drive%20Employee%20Productivity%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1903244805.1748574839&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=998810d7-9e61-4820-a302-9ffa0c8491af&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3f619102-543a-4627-bb1c-38bbc0f2fa37&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fdust-and-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=998810d7-9e61-4820-a302-9ffa0c8491af&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3f619102-543a-4627-bb1c-38bbc0f2fa37&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fdust-and-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=4960769f1dc9068e6ad6be33e684a2a3&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574840011&cv=11&fst=1748574840011&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fdust-and-qdrant%2F&hn=www.googleadservices.com&frm=0&tiba=Dust%20and%20Qdrant%3A%20Using%20AI%20to%20Unlock%20Company%20Knowledge%20and%20Drive%20Employee%20Productivity%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1903244805.1748574839&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)