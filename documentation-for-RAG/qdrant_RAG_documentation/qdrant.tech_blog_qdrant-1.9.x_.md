---
url: "https://qdrant.tech/blog/qdrant-1.9.x/"
title: "Qdrant 1.9.0 - Heighten Your Security With Role-Based Access Control Support - Qdrant"
---

0

# Qdrant 1.9.0 - Heighten Your Security With Role-Based Access Control Support

David Myriel

·

April 24, 2024

![Qdrant 1.9.0 - Heighten Your Security With Role-Based Access Control Support](https://qdrant.tech/blog/qdrant-1.9.x/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.9.x%2F&text=Qdrant%201.9.0%20-%20Heighten%20Your%20Security%20With%20Role-Based%20Access%20Control%20Support "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.9.x%2F "LinkedIn")

[Qdrant 1.9.0 is out!](https://github.com/qdrant/qdrant/releases/tag/v1.9.0) This version complements the release of our new managed product [Qdrant Hybrid Cloud](https://qdrant.tech/hybrid-cloud/) with key security features valuable to our enterprise customers, and all those looking to productionize large-scale Generative AI. **Data privacy, system stability and resource optimizations** are always on our mind - so let’s see what’s new:

- **Granular access control:** You can further specify access control levels by using JSON Web Tokens.
- **Optimized shard transfers:** The synchronization of shards between nodes is now significantly faster!
- **Support for byte embeddings:** Reduce the memory footprint of Qdrant with official `uint8` support.

## [Anchor](https://qdrant.tech/blog/qdrant-1.9.x/\#new-access-control-options-via-json-web-tokens) New access control options via JSON Web Tokens

Historically, our API key supported basic read and write operations. However, recognizing the evolving needs of our user base, especially large organizations, we’ve implemented additional options for finer control over data access within internal environments.

Qdrant now supports [granular access control using JSON Web Tokens (JWT)](https://qdrant.tech/documentation/guides/security/#granular-access-control-with-jwt). JWT will let you easily limit a user’s access to the specific data they are permitted to view. Specifically, JWT-based authentication leverages tokens with restricted access to designated data segments, laying the foundation for implementing role-based access control (RBAC) on top of it. **You will be able to define permissions for users and restrict access to sensitive endpoints.**

**Dashboard users:** For your convenience, we have added a JWT generation tool the Qdrant Web UI under the 🔑 tab. If you’re using the default url, you will find it at `http://localhost:6333/dashboard#/jwt`.

![jwt-web-ui](https://qdrant.tech/blog/qdrant-1.9.x/jwt-web-ui.png)

We highly recommend this feature to enterprises using [Qdrant Hybrid Cloud](https://qdrant.tech/hybrid-cloud/), as it is tailored to those who need additional control over company data and user access. RBAC empowers administrators to define roles and assign specific privileges to users based on their roles within the organization. In combination with [Hybrid Cloud’s data sovereign architecture](https://qdrant.tech/documentation/hybrid-cloud/), this feature reinforces internal security and efficient collaboration by granting access only to relevant resources.

> **Documentation:** [Read the access level breakdown](https://qdrant.tech/documentation/guides/security/#table-of-access) to see which actions are allowed or denied.

## [Anchor](https://qdrant.tech/blog/qdrant-1.9.x/\#faster-shard-transfers-on-node-recovery) Faster shard transfers on node recovery

We now offer a streamlined approach to [data synchronization between shards](https://qdrant.tech/documentation/guides/distributed_deployment/#shard-transfer-method) during node upgrades or recovery processes. Traditional methods used to transfer the entire dataset, but our new `wal_delta` method focuses solely on transmitting the difference between two existing shards. By leveraging the Write-Ahead Log (WAL) of both shards, this method selectively transmits missed operations to the target shard, ensuring data consistency.

In some cases, where transfers can take hours, this update **reduces transfers down to a few minutes.**

The advantages of this approach are twofold:

1. **It is faster** since only the differential data is transmitted, avoiding the transfer of redundant information.
2. It upholds robust **ordering guarantees**, crucial for applications reliant on strict sequencing.

For more details on how this works, check out the [shard transfer documentation](https://qdrant.tech/documentation/guides/distributed_deployment/#shard-transfer-method).

> **Note:** There are limitations to consider. First, this method only works with existing shards. Second, while the WALs typically retain recent operations, their capacity is finite, potentially impeding the transfer process if exceeded. Nevertheless, for scenarios like rapid node restarts or upgrades, where the WAL content remains manageable, WAL delta transfer is an efficient solution.

Overall, this is a great optional optimization measure and serves as the **auto-recovery default for shard transfers**. It’s safe to use everywhere because it’ll automatically fall back to streaming records transfer if no difference can be resolved. By minimizing data redundancy and expediting transfer processes, it alleviates the strain on the cluster during recovery phases, enabling faster node catch-up.

## [Anchor](https://qdrant.tech/blog/qdrant-1.9.x/\#native-support-for-uint8-embeddings) Native support for uint8 embeddings

Our latest version introduces [support for uint8 embeddings within Qdrant collections](https://qdrant.tech/documentation/concepts/collections/#vector-datatypes). This feature supports embeddings provided by companies in a pre-quantized format. Unlike previous iterations where indirect support was available via [quantization methods](https://qdrant.tech/documentation/guides/quantization/), this update empowers users with direct integration capabilities.

In the case of `uint8`, elements within the vector are represented as unsigned 8-bit integers, encompassing values ranging from 0 to 255. Using these embeddings gives you a **4x memory saving and about a 30% speed-up in search**, while keeping 99.99% of the response quality. As opposed to the original quantization method, with this feature you can spare disk usage if you directly implement pre-quantized embeddings.

The configuration is simple. To create a collection with uint8 embeddings, simply add the following `datatype`:

```bash
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 1024,
      "distance": "Dot",
      "datatype": "uint8"
    }
}

```

> **Note:** When using Quantization to optimize vector search, you can use this feature to `rescore` binary vectors against new byte vectors. With double the speedup, you will be able to achieve a better result than if you rescored with float vectors. With each byte vector quantized at the binary level, the result will deliver unparalleled efficiency and savings. To learn more about this optimization method, read our [Quantization docs](https://qdrant.tech/documentation/guides/quantization/).

## [Anchor](https://qdrant.tech/blog/qdrant-1.9.x/\#minor-improvements-and-new-features) Minor improvements and new features

- Greatly improve write performance while creating a snapshot of a large collection - [#3420](https://github.com/qdrant/qdrant/pull/3420), [#3938](https://github.com/qdrant/qdrant/pull/3938)
- Report pending optimizations awaiting an update operation in collection info - [#3962](https://github.com/qdrant/qdrant/pull/3962), [#3971](https://github.com/qdrant/qdrant/pull/3971)
- Improve `indexed_only` reliability on proxy shards - [#3998](https://github.com/qdrant/qdrant/pull/3998)
- Make shard diff transfer fall back to streaming records - [#3798](https://github.com/qdrant/qdrant/pull/3798)
- Cancel shard transfers when the shard is deleted - [#3784](https://github.com/qdrant/qdrant/pull/3784)
- Improve sparse vectors search performance by another 7% - [#4037](https://github.com/qdrant/qdrant/pull/4037)
- Build Qdrant with a single codegen unit to allow better compile-time optimizations - [#3982](https://github.com/qdrant/qdrant/pull/3982)
- Remove `vectors_count` from collection info because it is unreliable. **Check if you use this field before upgrading** \- [#4052](https://github.com/qdrant/qdrant/pull/4052)
- Remove shard transfer method field from abort shard transfer operation - [#3803](https://github.com/qdrant/qdrant/pull/3803)

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=055a1eaf-2f3b-4282-a105-50f5bff8264d)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5c1bff78-305d-4760-a35a-b4458432ca53&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=709ed9a3-dc45-4c0d-81c2-ca22b4765a01&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.9.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574412618&cv=11&fst=1748574412618&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.9.x%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.9.0%20-%20Heighten%20Your%20Security%20With%20Role-Based%20Access%20Control%20Support%20-%20Qdrant&npa=0&pscdl=noapi&auid=152910983.1748574412&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574412607&cv=11&fst=1748574412607&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.9.x%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.9.0%20-%20Heighten%20Your%20Security%20With%20Role-Based%20Access%20Control%20Support%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=152910983.1748574412&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5c1bff78-305d-4760-a35a-b4458432ca53&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=709ed9a3-dc45-4c0d-81c2-ca22b4765a01&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.9.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=b06ea169001ce528139223302e6f78e1&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574413479&cv=11&fst=1748574413479&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.9.x%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.9.0%20-%20Heighten%20Your%20Security%20With%20Role-Based%20Access%20Control%20Support%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=152910983.1748574412&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)