---
url: "https://qdrant.tech/documentation/guides/usage-statistics/"
title: "Usage Statistics - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Usage Statistics

# [Anchor](https://qdrant.tech/documentation/guides/usage-statistics/\#usage-statistics) Usage statistics

The Qdrant open-source container image collects anonymized usage statistics from users in order to improve the engine by default. You can [deactivate](https://qdrant.tech/documentation/guides/usage-statistics/#deactivate-telemetry) at any time, and any data that has already been collected can be [deleted on request](https://qdrant.tech/documentation/guides/usage-statistics/#request-information-deletion).

Deactivating this will not affect your ability to monitor the Qdrant database yourself by accessing the `/metrics` or `/telemetry` endpoints of your database. It will just stop sending independend, anonymized usage statistics to the Qdrant team.

## [Anchor](https://qdrant.tech/documentation/guides/usage-statistics/\#why-do-we-collect-usage-statistics) Why do we collect usage statistics?

We want to make Qdrant fast and reliable. To do this, we need to understand how it performs in real-world scenarios.
We do a lot of benchmarking internally, but it is impossible to cover all possible use cases, hardware, and configurations.

In order to identify bottlenecks and improve Qdrant, we need to collect information about how it is used.

Additionally, Qdrant uses a bunch of internal heuristics to optimize the performance.
To better set up parameters for these heuristics, we need to collect timings and counters of various pieces of code.
With this information, we can make Qdrant faster for everyone.

## [Anchor](https://qdrant.tech/documentation/guides/usage-statistics/\#what-information-is-collected) What information is collected?

There are 3 types of information that we collect:

- System information - general information about the system, such as CPU, RAM, and disk type. As well as the configuration of the Qdrant instance.
- Performance - information about timings and counters of various pieces of code.
- Critical error reports - information about critical errors, such as backtraces, that occurred in Qdrant. This information would allow to identify problems nobody yet reported to us.

### [Anchor](https://qdrant.tech/documentation/guides/usage-statistics/\#we-never-collect-the-following-information) We **never** collect the following information:

- User’s IP address
- Any data that can be used to identify the user or the user’s organization
- Any data, stored in the collections
- Any names of the collections
- Any URLs

## [Anchor](https://qdrant.tech/documentation/guides/usage-statistics/\#how-do-we-anonymize-data) How do we anonymize data?

We understand that some users may be concerned about the privacy of their data.
That is why we make an extra effort to ensure your privacy.

There are several different techniques that we use to anonymize the data:

- We use a random UUID to identify instances. This UUID is generated on each startup and is not stored anywhere. There are no other ways to distinguish between different instances.
- We round all big numbers, so that the last digits are always 0. For example, if the number is 123456789, we will store 123456000.
- We replace all names with irreversibly hashed values. So no collection or field names will leak into the telemetry.
- All urls are hashed as well.

You can see exact version of anomymized collected data by accessing the [telemetry API](https://api.qdrant.tech/master/api-reference/service/telemetry) with `anonymize=true` parameter.

For example, [http://localhost:6333/telemetry?details\_level=6&anonymize=true](http://localhost:6333/telemetry?details_level=6&anonymize=true)

## [Anchor](https://qdrant.tech/documentation/guides/usage-statistics/\#deactivate-usage-statistics) Deactivate usage statistics

You can deactivate usage statistics by:

- setting the `QDRANT__TELEMETRY_DISABLED` environment variable to `true`
- setting the config option `telemetry_disabled` to `true` in the `config/production.yaml` or `config/config.yaml` files
- using cli option `--disable-telemetry`

Any of these options will prevent Qdrant from sending any usage statistics data.

If you decide to deactivate usage statistics, we kindly ask you to share your feedback with us in the [Discord community](https://qdrant.to/discord) or GitHub [discussions](https://github.com/qdrant/qdrant/discussions)

## [Anchor](https://qdrant.tech/documentation/guides/usage-statistics/\#request-information-deletion) Request information deletion

We provide an email address so that users can request the complete removal of their data from all of our tools.

To do so, send an email to [privacy@qdrant.com](mailto:privacy@qdrant.com) containing the unique identifier generated for your Qdrant installation.
You can find this identifier in the telemetry API response ( `"id"` field), or in the logs of your Qdrant instance.

Any questions regarding the management of the data we collect can also be sent to this email address.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/usage-statistics.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/usage-statistics.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573591465&cv=11&fst=1748573591465&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fusage-statistics%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Usage%20Statistics%20-%20Qdrant&npa=0&pscdl=noapi&auid=1341065874.1748573591&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573591425&cv=11&fst=1748573591425&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fusage-statistics%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Usage%20Statistics%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1341065874.1748573591&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1~em.zaMSasa6JyIocjOHypZW-mvbk0iqvYBUzqEVlJEAwIA&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=381a80af-d5bc-44f4-bf72-001c49885ab0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=813b95ec-d6e0-4002-aca7-b196eeba3e2e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fusage-statistics%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=381a80af-d5bc-44f4-bf72-001c49885ab0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=813b95ec-d6e0-4002-aca7-b196eeba3e2e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fusage-statistics%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573592322&cv=11&fst=1748573592322&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fusage-statistics%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Usage%20Statistics%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1341065874.1748573591&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)