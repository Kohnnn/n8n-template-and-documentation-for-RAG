---
url: "https://qdrant.tech/documentation/platforms/apify/"
title: "Apify - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Platforms](https://qdrant.tech/documentation/platforms/)
- Apify

# [Anchor](https://qdrant.tech/documentation/platforms/apify/\#apify) Apify

[Apify](https://apify.com/) is a web scraping and browser automation platform featuring an [app store](https://apify.com/store) with over 1,500 pre-built micro-apps known as Actors. These serverless cloud programs, which are essentially dockers under the hood, are designed for various web automation applications, including data collection.

One such Actor, built especially for AI and RAG applications, is [Website Content Crawler](https://apify.com/apify/website-content-crawler).

It’s ideal for this purpose because it has built-in HTML processing and data-cleaning functions. That means you can easily remove fluff, duplicates, and other things on a web page that aren’t relevant, and provide only the necessary data to the language model.

The Markdown can then be used to feed Qdrant to train AI models or supply them with fresh web content.

Qdrant is available as an [official integration](https://apify.com/apify/qdrant-integration) to load Apify datasets into a collection.

You can refer to the [Apify documentation](https://docs.apify.com/platform/integrations/qdrant) to set up the integration via the Apify UI.

## [Anchor](https://qdrant.tech/documentation/platforms/apify/\#programmatic-usage) Programmatic Usage

Apify also supports programmatic access to integrations via the [Apify Python SDK](https://docs.apify.com/sdk/python/).

1. Install the Apify Python SDK by running the following command:



```sh
pip install apify-client

```

2. Create a Python script and import all the necessary modules:



```python
from apify_client import ApifyClient

APIFY_API_TOKEN = "YOUR-APIFY-TOKEN"
OPENAI_API_KEY = "YOUR-OPENAI-API-KEY"
# COHERE_API_KEY = "YOUR-COHERE-API-KEY"

QDRANT_URL = "YOUR-QDRANT-URL"
QDRANT_API_KEY = "YOUR-QDRANT-API-KEY"

client = ApifyClient(APIFY_API_TOKEN)

```

3. Call the [Website Content Crawler](https://apify.com/apify/website-content-crawler) Actor to crawl the Qdrant documentation and extract text content from the web pages:



```python
actor_call = client.actor("apify/website-content-crawler").call(
       run_input={"startUrls": [{"url": "https://qdrant.tech/documentation/"}]}
)

```

4. Call the Qdrant integration and store all data in the Qdrant Vector Database:



```python
qdrant_integration_inputs = {
       "qdrantUrl": QDRANT_URL,
       "qdrantApiKey": QDRANT_API_KEY,
       "qdrantCollectionName": "apify",
       "qdrantAutoCreateCollection": True,
       "datasetId": actor_call["defaultDatasetId"],
       "datasetFields": ["text"],
       "enableDeltaUpdates": True,
       "deltaUpdatesPrimaryDatasetFields": ["url"],
       "expiredObjectDeletionPeriodDays": 30,
       "embeddingsProvider": "OpenAI", # "Cohere"
       "embeddingsApiKey": OPENAI_API_KEY,
       "performChunking": True,
       "chunkSize": 1000,
       "chunkOverlap": 0,
}
actor_call = client.actor("apify/qdrant-integration").call(run_input=qdrant_integration_inputs)

```


Upon running the script, the data from [https://qdrant.tech/documentation/](https://qdrant.tech/documentation/) will be scraped, transformed into vector embeddings and stored in the Qdrant collection.

## [Anchor](https://qdrant.tech/documentation/platforms/apify/\#further-reading) Further Reading

- Apify [Documentation](https://docs.apify.com/)
- Apify [Templates](https://apify.com/templates)
- Integration [Source Code](https://github.com/apify/actor-vector-database-integrations)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/platforms/apify.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/platforms/apify.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574373825&cv=11&fst=1748574373825&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fapify%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Apify%20-%20Qdrant&npa=0&pscdl=noapi&auid=1539726984.1748574374&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574373793&cv=11&fst=1748574373793&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308614&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fapify%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Apify%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1539726984.1748574374&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8b8e91a9-baf7-4adf-a0f6-66b93dec92ec&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=72e164df-64dc-4a7e-96ad-3575ced8f7dc&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fapify%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8b8e91a9-baf7-4adf-a0f6-66b93dec92ec&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=72e164df-64dc-4a7e-96ad-3575ced8f7dc&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fapify%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574374952&cv=11&fst=1748574374952&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fapify%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Apify%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1539726984.1748574374&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)