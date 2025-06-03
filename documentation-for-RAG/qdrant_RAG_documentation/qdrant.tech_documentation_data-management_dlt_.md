---
url: "https://qdrant.tech/documentation/data-management/dlt/"
title: "DLT - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- DLT

# [Anchor](https://qdrant.tech/documentation/data-management/dlt/\#dltdata-load-tool) DLT(Data Load Tool)

[DLT](https://dlthub.com/) is an open-source library that you can add to your Python scripts to load data from various and often messy data sources into well-structured, live datasets.

With the DLT-Qdrant integration, you can now select Qdrant as a DLT destination to load data into.

**DLT Enables**

- Automated maintenance - with schema inference, alerts and short declarative code, maintenance becomes simple.
- Run it where Python runs - on Airflow, serverless functions, notebooks. Scales on micro and large infrastructure alike.
- User-friendly, declarative interface that removes knowledge obstacles for beginners while empowering senior professionals.

## [Anchor](https://qdrant.tech/documentation/data-management/dlt/\#usage) Usage

To get started, install `dlt` with the `qdrant` extra.

```bash
pip install "dlt[qdrant]"

```

Configure the destination in the DLT secrets file. The file is located at `~/.dlt/secrets.toml` by default. Add the following section to the secrets file.

```toml
[destination.qdrant.credentials]
location = "https://your-qdrant-url"
api_key = "your-qdrant-api-key"

```

The location will default to `http://localhost:6333` and `api_key` is not defined - which are the defaults for a local Qdrant instance.
Find more information about DLT configurations [here](https://dlthub.com/docs/general-usage/credentials).

Define the source of the data.

```python
import dlt
from dlt.destinations.qdrant import qdrant_adapter

movies = [\
    {\
        "title": "Blade Runner",\
        "year": 1982,\
        "description": "The film is about a dystopian vision of the future that combines noir elements with sci-fi imagery."\
    },\
    {\
        "title": "Ghost in the Shell",\
        "year": 1995,\
        "description": "The film is about a cyborg policewoman and her partner who set out to find the main culprit behind brain hacking, the Puppet Master."\
    },\
    {\
        "title": "The Matrix",\
        "year": 1999,\
        "description": "The movie is set in the 22nd century and tells the story of a computer hacker who joins an underground group fighting the powerful computers that rule the earth."\
    }\
]

```

Define the pipeline.

```python
pipeline = dlt.pipeline(
    pipeline_name="movies",
    destination="qdrant",
    dataset_name="movies_dataset",
)

```

Run the pipeline.

```python
info = pipeline.run(
    qdrant_adapter(
        movies,
        embed=["title", "description"]
    )
)

```

The data is now loaded into Qdrant.

To use vector search after the data has been loaded, you must specify which fields Qdrant needs to generate embeddings for. You do that by wrapping the data (or [DLT resource](https://dlthub.com/docs/general-usage/resource)) with the `qdrant_adapter` function.

## [Anchor](https://qdrant.tech/documentation/data-management/dlt/\#write-disposition) Write disposition

A DLT [write disposition](https://dlthub.com/docs/dlt-ecosystem/destinations/qdrant/#write-disposition) defines how the data should be written to the destination. All write dispositions are supported by the Qdrant destination.

## [Anchor](https://qdrant.tech/documentation/data-management/dlt/\#dlt-sync) DLT Sync

Qdrant destination supports syncing of the [`DLT` state](https://dlthub.com/docs/general-usage/state#syncing-state-with-destination).

## [Anchor](https://qdrant.tech/documentation/data-management/dlt/\#next-steps) Next steps

- The comprehensive Qdrant DLT destination documentation can be found [here](https://dlthub.com/docs/dlt-ecosystem/destinations/qdrant/).
- [Source Code](https://github.com/dlt-hub/dlt/tree/devel/dlt/destinations/impl/qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/dlt.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/dlt.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574756090&cv=11&fst=1748574756090&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fdlt%2F&hn=www.googleadservices.com&frm=0&tiba=DLT%20-%20Qdrant&npa=0&pscdl=noapi&auid=1362483581.1748574756&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574756073&cv=11&fst=1748574756073&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fdlt%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=DLT%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1362483581.1748574756&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d7106672-3efe-421c-a3b6-0f1c6f8a77d1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e62c372e-2a28-4ca9-9ce9-b47f91975ec8&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fdlt%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d7106672-3efe-421c-a3b6-0f1c6f8a77d1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e62c372e-2a28-4ca9-9ce9-b47f91975ec8&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fdlt%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574757202&cv=11&fst=1748574757202&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fdlt%2F&hn=www.googleadservices.com&frm=0&tiba=DLT%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1362483581.1748574756&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)