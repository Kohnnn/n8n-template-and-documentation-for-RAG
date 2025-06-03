---
url: "https://qdrant.tech/articles/qdrant-1.2.x/"
title: "Introducing Qdrant 1.2.x - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Introducing Qdrant 1.2.x

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Introducing Qdrant 1.2.x

Kacper Łukawski

·

May 24, 2023

![Introducing Qdrant 1.2.x](https://qdrant.tech/articles_data/qdrant-1.2.x/preview/title.jpg)

A brand-new Qdrant 1.2 release comes packed with a plethora of new features, some of which
were highly requested by our users. If you want to shape the development of the Qdrant vector
database, please [join our Discord community](https://qdrant.to/discord) and let us know
how you use it!

## [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#new-features) New features

As usual, a minor version update of Qdrant brings some interesting new features. We love to see your
feedback, and we tried to include the features most requested by our community.

### [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#product-quantization) Product Quantization

The primary focus of Qdrant was always performance. That’s why we built it in Rust, but we were
always concerned about making vector search affordable. From the very beginning, Qdrant offered
support for disk-stored collections, as storage space is way cheaper than memory. That’s also
why we have introduced the [Scalar Quantization](https://qdrant.tech/articles/scalar-quantization/) mechanism recently,
which makes it possible to reduce the memory requirements by up to four times.

Today, we are bringing a new quantization mechanism to life. A separate article on [Product\\
Quantization](https://qdrant.tech/documentation/quantization/#product-quantization) will describe that feature in more
detail. In a nutshell, you can **reduce the memory requirements by up to 64 times**!

### [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#optional-named-vectors) Optional named vectors

Qdrant has been supporting multiple named vectors per point for quite a long time. Those may have
utterly different dimensionality and distance functions used to calculate similarity. Having multiple
embeddings per item is an essential real-world scenario. For example, you might be encoding textual
and visual data using different models. Or you might be experimenting with different models but
don’t want to make your payloads redundant by keeping them in separate collections.

![Optional vectors](https://qdrant.tech/articles_data/qdrant-1.2.x/optional-vectors.png)

However, up to the previous version, we requested that you provide all the vectors for each point. There
have been many requests to allow nullable vectors, as sometimes you cannot generate an embedding or
simply don’t want to for reasons we don’t need to know.

### [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#grouping-requests) Grouping requests

Embeddings are great for capturing the semantics of the documents, but we rarely encode larger pieces
of data into a single vector. Having a summary of a book may sound attractive, but in reality, we
divide it into paragraphs or some different parts to have higher granularity. That pays off when we
perform the semantic search, as we can return the relevant pieces only. That’s also how modern tools
like Langchain process the data. The typical way is to encode some smaller parts of the document and
keep the document id as a payload attribute.

![Query without grouping request](https://qdrant.tech/articles_data/qdrant-1.2.x/without-grouping-request.png)

There are cases where we want to find relevant parts, but only up to a specific number of results
per document (for example, only a single one). Up till now, we had to implement such a mechanism
on the client side and send several calls to the Qdrant engine. But that’s no longer the case.
Qdrant 1.2 provides a mechanism for [grouping requests](https://qdrant.tech/documentation/search/#grouping-api), which
can handle that server-side, within a single call to the database. This mechanism is similar to the
SQL `GROUP BY` clause.

![Query with grouping request](https://qdrant.tech/articles_data/qdrant-1.2.x/with-grouping-request.png)

You are not limited to a single result per document, and you can select how many entries will be
returned.

### [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#nested-filters) Nested filters

Unlike some other vector databases, Qdrant accepts any arbitrary JSON payload, including
arrays, objects, and arrays of objects. You can also [filter the search results using nested\\
keys](https://qdrant.tech/documentation/filtering/#nested-key), even though arrays (using the `[]` syntax).

Before Qdrant 1.2 it was impossible to express some more complex conditions for the
nested structures. For example, let’s assume we have the following payload:

```json
{
  "country": "Japan",
  "cities": [\
    {\
      "name": "Tokyo",\
      "population": 9.3,\
      "area": 2194\
    },\
    {\
      "name": "Osaka",\
      "population": 2.7,\
      "area": 223\
    },\
    {\
      "name": "Kyoto",\
      "population": 1.5,\
      "area": 827.8\
    }\
  ]
}

```

We want to filter out the results to include the countries with a city with over 2 million citizens
and an area bigger than 500 square kilometers but no more than 1000. There is no such a city in
Japan, looking at our data, but if we wrote the following filter, it would be returned:

```json
{
  "filter": {
    "must": [\
      {\
        "key": "country.cities[].population",\
        "range": {\
          "gte": 2\
        }\
      },\
      {\
        "key": "country.cities[].area",\
        "range": {\
          "gt": 500,\
          "lte": 1000\
        }\
      }\
    ]
  },
  "limit": 3
}

```

Japan would be returned because Tokyo and Osaka match the first criteria, while Kyoto fulfills
the second. But that’s not what we wanted to achieve. That’s the motivation behind introducing
a new type of nested filter.

```json
{
  "filter": {
    "must": [\
      {\
        "nested": {\
          "key": "country.cities",\
          "filter": {\
            "must": [\
              {\
                "key": "population",\
                "range": {\
                  "gte": 2\
                }\
              },\
              {\
                "key": "area",\
                "range": {\
                  "gt": 500,\
                  "lte": 1000\
                }\
              }\
            ]\
          }\
        }\
      }\
    ]
  },
  "limit": 3
}

```

The syntax is consistent with all the other supported filters and enables new possibilities. In
our case, it allows us to express the joined condition on a nested structure and make the results
list empty but correct.

## [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#important-changes) Important changes

The latest release focuses not only on the new features but also introduces some changes making
Qdrant even more reliable.

### [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#recovery-mode) Recovery mode

There has been an issue in memory-constrained environments, such as cloud, happening when users were
pushing massive amounts of data into the service using `wait=false`. This data influx resulted in an
overreaching of disk or RAM limits before the Write-Ahead Logging (WAL) was fully applied. This
situation was causing Qdrant to attempt a restart and reapplication of WAL, failing recurrently due
to the same memory constraints and pushing the service into a frustrating crash loop with many
Out-of-Memory errors.

Qdrant 1.2 enters recovery mode, if enabled, when it detects a failure on startup.
That makes the service halt the loading of collection data and commence operations in a partial state.
This state allows for removing collections but doesn’t support search or update functions.
**Recovery mode [has to be enabled by user](https://qdrant.tech/documentation/administration/#recovery-mode).**

### [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#appendable-mmap) Appendable mmap

For a long time, segments using mmap storage were `non-appendable` and could only be constructed by
the optimizer. Dynamically adding vectors to the mmap file is fairly complicated and thus not
implemented in Qdrant, but we did our best to implement it in the recent release. If you want
to read more about segments, check out our docs on [vector storage](https://qdrant.tech/documentation/storage/#vector-storage).

## [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#security) Security

There are two major changes in terms of [security](https://qdrant.tech/documentation/security/):

1. **API-key support** \- basic authentication with a static API key to prevent unwanted access. Previously
API keys were only supported in [Qdrant Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=3d1fa4b3-68f7-4a94-b48c-b3c21d5241f1).
2. **TLS support** \- to use encrypted connections and prevent sniffing/MitM attacks.

## [Anchor](https://qdrant.tech/articles/qdrant-1.2.x/\#release-notes) Release notes

As usual, [our release notes](https://github.com/qdrant/qdrant/releases/tag/v1.2.0) describe all the changes
introduced in the latest version.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.2.x.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.2.x.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574797585&cv=11&fst=1748574797585&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.2.x%2F&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%201.2.x%20-%20Qdrant&npa=0&pscdl=noapi&auid=47117801.1748574798&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574797568&cv=11&fst=1748574797568&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.2.x%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%201.2.x%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=47117801.1748574798&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=afcfe791-c58c-4598-a5fc-978a932ad59c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f11c6898-55f8-4e77-9e16-ddcd94dbcbc0&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.2.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=afcfe791-c58c-4598-a5fc-978a932ad59c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f11c6898-55f8-4e77-9e16-ddcd94dbcbc0&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.2.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574798609&cv=11&fst=1748574798609&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.2.x%2F&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%201.2.x%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=47117801.1748574798&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)