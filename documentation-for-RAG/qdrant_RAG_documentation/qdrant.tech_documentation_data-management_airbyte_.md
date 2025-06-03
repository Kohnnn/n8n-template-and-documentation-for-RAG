---
url: "https://qdrant.tech/documentation/data-management/airbyte/"
title: "Airbyte - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- Airbyte

# [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#airbyte) Airbyte

[Airbyte](https://airbyte.com/) is an open-source data integration platform that helps you replicate your data
between different systems. It has a [growing list of connectors](https://docs.airbyte.io/integrations) that can
be used to ingest data from multiple sources. Building data pipelines is also crucial for managing the data in
Qdrant, and Airbyte is a great tool for this purpose.

Airbyte may take care of the data ingestion from a selected source, while Qdrant will help you to build a search
engine on top of it. There are three supported modes of how the data can be ingested into Qdrant:

- **Full Refresh Sync**
- **Incremental - Append Sync**
- **Incremental - Append + Deduped**

You can read more about these modes in the [Airbyte documentation](https://docs.airbyte.io/integrations/destinations/qdrant).

## [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#prerequisites) Prerequisites

Before you start, make sure you have the following:

1. Airbyte instance, either [Open Source](https://airbyte.com/solutions/airbyte-open-source),
[Self-Managed](https://airbyte.com/solutions/airbyte-enterprise), or [Cloud](https://airbyte.com/solutions/airbyte-cloud).
2. Running instance of Qdrant. It has to be accessible by URL from the machine where Airbyte is running.
You can follow the [installation guide](https://qdrant.tech/documentation/guides/installation/) to set up Qdrant.

## [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#setting-up-qdrant-as-a-destination) Setting up Qdrant as a destination

Once you have a running instance of Airbyte, you can set up Qdrant as a destination directly in the UI.
Airbyte’s Qdrant destination is connected with a single collection in Qdrant.

![Airbyte Qdrant destination](https://qdrant.tech/documentation/frameworks/airbyte/qdrant-destination.png)

### [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#text-processing) Text processing

Airbyte has some built-in mechanisms to transform your texts into embeddings. You can choose how you want to
chunk your fields into pieces before calculating the embeddings, but also which fields should be used to
create the point payload.

![Processing settings](https://qdrant.tech/documentation/frameworks/airbyte/processing.png)

### [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#embeddings) Embeddings

You can choose the model that will be used to calculate the embeddings. Currently, Airbyte supports multiple
models, including OpenAI and Cohere.

![Embeddings settings](https://qdrant.tech/documentation/frameworks/airbyte/embedding.png)

Using some precomputed embeddings from your data source is also possible. In this case, you can pass the field
name containing the embeddings and their dimensionality.

![Precomputed embeddings settings](https://qdrant.tech/documentation/frameworks/airbyte/precomputed-embedding.png)

### [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#qdrant-connection-details) Qdrant connection details

Finally, we can configure the target Qdrant instance and collection. In case you use the built-in authentication
mechanism, here is where you can pass the token.

![Qdrant connection details](https://qdrant.tech/documentation/frameworks/airbyte/qdrant-config.png)

Once you confirm creating the destination, Airbyte will test if a specified Qdrant cluster is accessible and
might be used as a destination.

## [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#setting-up-connection) Setting up connection

Airbyte combines sources and destinations into a single entity called a connection. Once you have a destination
configured and a source, you can create a connection between them. It doesn’t matter what source you use, as
long as Airbyte supports it. The process is pretty straightforward, but depends on the source you use.

![Airbyte connection](https://qdrant.tech/documentation/frameworks/airbyte/connection.png)

## [Anchor](https://qdrant.tech/documentation/data-management/airbyte/\#further-reading) Further Reading

- [Airbyte documentation](https://docs.airbyte.com/understanding-airbyte/connections/).
- [Source Code](https://github.com/airbytehq/airbyte/tree/master/airbyte-integrations/connectors/destination-qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/airbyte.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/airbyte.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574810670&cv=11&fst=1748574810670&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairbyte%2F&hn=www.googleadservices.com&frm=0&tiba=Airbyte%20-%20Qdrant&npa=0&pscdl=noapi&auid=734919367.1748574811&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574810631&cv=11&fst=1748574810631&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairbyte%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Airbyte%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=734919367.1748574811&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9103a088-eb1e-46f7-bb25-e785d6b36392&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f8581e43-8ae2-4d7f-a63a-b50ed1ffdf1d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairbyte%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9103a088-eb1e-46f7-bb25-e785d6b36392&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f8581e43-8ae2-4d7f-a63a-b50ed1ffdf1d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairbyte%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574812856&cv=11&fst=1748574812856&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairbyte%2F&hn=www.googleadservices.com&frm=0&tiba=Airbyte%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=734919367.1748574811&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)