---
url: "https://qdrant.tech/documentation/data-management/nifi/"
title: "Apache NiFi - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- Apache NiFi

# [Anchor](https://qdrant.tech/documentation/data-management/nifi/\#apache-nifi) Apache NiFi

[NiFi](https://nifi.apache.org/) is a real-time data ingestion platform, which can transfer and manage data transfer between numerous sources and destination systems. It supports many protocols and offers a web-based user interface for developing and monitoring data flows.

NiFi supports ingesting and querying data in Qdrant via its processor modules.

## [Anchor](https://qdrant.tech/documentation/data-management/nifi/\#configuration) Configuration

![NiFi Qdrant configuration](https://qdrant.tech/documentation/frameworks/nifi/nifi-conifg.png)

You can configure Qdrant NiFi processors with your Qdrant credentials, query/upload configurations. The processors offer 2 built-in embedding providers to encode data into vector embeddings - HuggingFace, OpenAI.

## [Anchor](https://qdrant.tech/documentation/data-management/nifi/\#put-qdrant) Put Qdrant

![NiFI Put Qdrant](https://qdrant.tech/documentation/frameworks/nifi/nifi-put-qdrant.png)

The `Put Qdrant` processor can ingest NiFi [FlowFile](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html#intro) data into a Qdrant collection.

## [Anchor](https://qdrant.tech/documentation/data-management/nifi/\#query-qdrant) Query Qdrant

![NiFI Query Qdrant](https://qdrant.tech/documentation/frameworks/nifi/nifi-query-qdrant.png)

The `Query Qdrant` processor can perform a similarity search across a Qdrant collection and return a [FlowFile](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html#intro) result.

## [Anchor](https://qdrant.tech/documentation/data-management/nifi/\#further-reading) Further Reading

- [NiFi Documentation](https://nifi.apache.org/documentation/v2/).
- [Source Code](https://github.com/apache/nifi-python-extensions)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/nifi.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/nifi.md)
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