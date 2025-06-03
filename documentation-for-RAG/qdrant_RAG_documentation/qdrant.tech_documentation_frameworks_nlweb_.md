---
url: "https://qdrant.tech/documentation/frameworks/nlweb/"
title: "Microsoft NLWeb - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Microsoft NLWeb

# [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#nlweb) NLWeb

Microsoft’s [NLWeb](https://github.com/microsoft/NLWeb) is a proposed framework that enables natural language interfaces for websites, using Schema.org, formats like RSS and the emerging [MCP protocol](https://github.com/microsoft/NLWeb/blob/main/docs/RestAPI.md).

Qdrant is supported as a vector store backend within NLWeb for embedding storage and context retrieval.

## [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#usage) Usage

NLWeb includes Qdrant integration by default. You can install and configure it to use Qdrant as the retrieval engine.

### [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#installation) Installation

Clone the repo and set up your environment:

```bash
git clone https://github.com/microsoft/NLWeb
cd NLWeb
python -m venv .venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
cd code
pip install -r requirements.txt

```

### [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#configuring-qdrant) Configuring Qdrant

To use **Qdrant**, update your configuration.

#### [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#1-copy-and-edit-the-environment-variables-file) 1\. Copy and edit the environment variables file

```bash
cp .env.template .env

```

Ensure the following values are set in your `.env` file:

```text
QDRANT_URL="https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6333"
QDRANT_API_KEY="<your-api-key-here>"

```

#### [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#2-update-config-files-in-codeconfig) 2\. Update config files in `code/config`

- **`config_retrieval.yaml`**

```yaml
retrieval_engine: qdrant_url

```

Alternatively, you can use an in-memory Qdrant instance for experimentation.

```yaml
retrieval_engine: qdrant_local

endpoints:
  qdrant_local:
    # Path to a local directory
    database_path: "../data/"
    # Set the collection name to use
    index_name: nlweb_collection
    # Specify the database type
    db_type: qdrant

```

### [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#loading-data) Loading Data

Once configured, load your content using RSS feeds.

From the `code` directory:

```bash
python -m tools.db_load https://feeds.libsyn.com/121695/rss Behind-the-Tech

```

This will ingest the content into your local Qdrant instance.

### [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#running-the-server) Running the Server

To start NLWeb, from the `code` directory, run:

```bash
python app-file.py

```

You can now query your content via natural language using either the web UI at [http://localhost:8000/](http://localhost:8000/) or directly through the MCP-compatible [REST API](https://github.com/microsoft/NLWeb/blob/main/docs/RestAPI.md).

## [Anchor](https://qdrant.tech/documentation/frameworks/nlweb/\#further-reading) Further Reading

- [Source](https://github.com/microsoft/NLWeb)
- [Life of a Chat Query](https://github.com/microsoft/NLWeb/tree/main/docs/LifeOfAChatQuery.md)
- [Modifying behavior by changing prompts](https://github.com/microsoft/NLWeb/tree/main/docs/Prompts.md)
- [Modifying control flow](https://github.com/microsoft/NLWeb/tree/main/docs/ControlFlow.md)
- [Modifying the user interface](https://github.com/microsoft/NLWeb/tree/main/docs/UserInterface.md)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/nlweb.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/nlweb.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573614854&cv=11&fst=1748573614854&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fnlweb%2F&hn=www.googleadservices.com&frm=0&tiba=Microsoft%20NLWeb%20-%20Qdrant&npa=0&pscdl=noapi&auid=1832981725.1748573615&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573614800&cv=11&fst=1748573614800&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fnlweb%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Microsoft%20NLWeb%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1832981725.1748573615&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d1d2be6c-c331-4362-9dc1-2407e4d8313e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4a677ce3-c23a-411b-a516-31b28786c4db&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fnlweb%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d1d2be6c-c331-4362-9dc1-2407e4d8313e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4a677ce3-c23a-411b-a516-31b28786c4db&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fnlweb%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573615823&cv=11&fst=1748573615823&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fnlweb%2F&hn=www.googleadservices.com&frm=0&tiba=Microsoft%20NLWeb%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1832981725.1748573615&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)