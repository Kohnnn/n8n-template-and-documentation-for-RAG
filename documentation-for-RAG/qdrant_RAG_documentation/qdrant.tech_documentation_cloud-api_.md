---
url: "https://qdrant.tech/documentation/cloud-api/"
title: "Qdrant Cloud API - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- Qdrant Cloud API

# [Anchor](https://qdrant.tech/documentation/cloud-api/\#qdrant-cloud-api) Qdrant Cloud API

The Qdrant Cloud API lets you manage Cloud accounts and their respective Qdrant clusters. You can use this API to manage your clusters, authentication methods, and cloud configurations.

| REST API | Documentation |
| --- | --- |
| v.0.1.0 | [OpenAPI Specification](https://cloud.qdrant.io/pa/v1/docs?ajs_anonymous_id=05ea9b8f-af45-44c4-ad39-458df130b580) |

**Note:** This is not the Qdrant REST API. For core product APIs & SDKs, see our list of [interfaces](https://qdrant.tech/documentation/interfaces/)

## [Anchor](https://qdrant.tech/documentation/cloud-api/\#authentication-connecting-to-cloud-api) Authentication: Connecting to Cloud API

To interact with the Qdrant Cloud API, you must authenticate using an API key. Each request to the API must include the API key in the **Authorization** header. The API key acts as a bearer token and grants access to your account’s resources.

You can create a Cloud API key in the Cloud Console UI. Go to **Access Management** \> **Qdrant Cloud API Keys**.
![Authentication](https://qdrant.tech/documentation/cloud/authentication.png)

**Note:** Ensure that the API key is kept secure and not exposed in public repositories or logs. Once authenticated, the API allows you to manage clusters, collections, and perform other operations available to your account.

## [Anchor](https://qdrant.tech/documentation/cloud-api/\#sample-api-request) Sample API Request

Here’s an example of a basic request to **list all clusters** in your Qdrant Cloud account:

```bash
curl -X 'GET' \
  'https://cloud.qdrant.io/pa/v1/accounts/<YOUR_ACCOUNT_ID>/clusters' \
  -H 'accept: application/json' \
  -H 'Authorization: apikey <YOUR_API_KEY>'

```

This request will return a list of clusters associated with your account in JSON format.

## [Anchor](https://qdrant.tech/documentation/cloud-api/\#cluster-management) Cluster Management

Use these endpoints to create and manage your Qdrant database clusters. The API supports fine-grained control over cluster resources (CPU, RAM, disk), node configurations, tolerations, and other operational characteristics across all cloud providers (AWS, GCP, Azure) and their respective regions in Qdrant Cloud, as well as Hybrid Cloud.

- **Get Cluster by ID**: Retrieve detailed information about a specific cluster using the cluster ID and associated account ID.
- **Delete Cluster**: Remove a cluster, with optional deletion of backups.
- **Update Cluster**: Apply modifications to a cluster’s configuration.
- **List Clusters**: Get all clusters associated with a specific account, filtered by region or other criteria.
- **Create Cluster**: Add new clusters to the account with configurable parameters such as nodes, cloud provider, and regions.
- **Get Booking**: Manage hosting across various cloud providers (AWS, GCP, Azure) and their respective regions.

## [Anchor](https://qdrant.tech/documentation/cloud-api/\#cluster-authentication-management) Cluster Authentication Management

Use these endpoints to manage your cluster API keys.

- **List API Keys**: Retrieve all API keys associated with an account.
- **Create API Key**: Generate a new API key for programmatic access.
- **Delete API Key**: Revoke access by deleting a specific API key.
- **Update API Key**: Modify attributes of an existing API key.

## [Anchor](https://qdrant.tech/documentation/cloud-api/\#terraform-provider) Terraform Provider

Qdrant Cloud also provides a Terraform provider to manage your Qdrant Cloud resources. [Learn more](https://qdrant.tech/documentation/infrastructure/terraform/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-api.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-api.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574702144&cv=11&fst=1748574702144&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-api%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Cloud%20API%20-%20Qdrant&npa=0&pscdl=noapi&auid=995774905.1748574702&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574702107&cv=11&fst=1748574702107&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-api%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Cloud%20API%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=995774905.1748574702&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=18efcd21-4ce1-4070-9889-9d07fa37ca5f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=40b175a1-a334-4d2a-a04e-8b5e24dcb375&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-api%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=18efcd21-4ce1-4070-9889-9d07fa37ca5f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=40b175a1-a334-4d2a-a04e-8b5e24dcb375&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-api%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574703065&cv=11&fst=1748574703065&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-api%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Cloud%20API%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=995774905.1748574702&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)