---
url: "https://qdrant.tech/documentation/private-cloud/backups/"
title: "Backups - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Private cloud](https://qdrant.tech/documentation/private-cloud/)
- Backups

# [Anchor](https://qdrant.tech/documentation/private-cloud/backups/\#backups) Backups

To create a one-time backup, create a `QdrantClusterSnapshot` resource:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantClusterSnapshot
metadata:
  name: "qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-timestamp"
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  retention: 1h

```

You can also create a recurring backup with the `QdrantClusterScheduledSnapshot` resource:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantClusterScheduledSnapshot
metadata:
  name: "qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-timestamp"
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  scheduleShortId: a7d8d973
  cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  # every hour
  schedule: "0 * * * *"
  retention: 1h

```

To resture from a backup, create a `QdrantClusterRestore` resource:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantClusterRestore
metadata:
  name: "qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-restore-01"
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  source:
    snapshotName: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-timestamp
    namespace: qdrant-private-cloud
  destination:
    name: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840
    namespace: qdrant-private-cloud

```

Note that with all resources `cluster-id` and `customer-id` label must be set to the values of the corresponding `QdrantCluster` resource.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/backups.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/backups.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c3ccb320-9d78-440b-bfd8-ae11dbd8d5b0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a1e6ae90-fb72-4805-97ae-1219500e9797&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fbackups%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575260332&cv=11&fst=1748575260332&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fbackups%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Backups%20-%20Qdrant&npa=0&pscdl=noapi&auid=1924656974.1748575260&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575260293&cv=11&fst=1748575260293&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fbackups%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Backups%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1924656974.1748575260&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c3ccb320-9d78-440b-bfd8-ae11dbd8d5b0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a1e6ae90-fb72-4805-97ae-1219500e9797&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fbackups%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)