---
url: "https://qdrant.tech/documentation/embeddings/mixedbread/"
title: "MixedBread - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- MixedBread

# [Anchor](https://qdrant.tech/documentation/embeddings/mixedbread/\#using-mixedbread-with-qdrant) Using MixedBread with Qdrant

MixedBread is a unique provider offering embeddings across multiple domains. Their models are versatile for various search tasks when integrated with Qdrant. MixedBread is creating state-of-the-art models and tools that make search smarter, faster, and more relevant. Whether you’re building a next-gen search engine or RAG (Retrieval Augmented Generation) systems, or whether you’re enhancing your existing search solution, they’ve got the ingredients to make it happen.

## [Anchor](https://qdrant.tech/documentation/embeddings/mixedbread/\#installation) Installation

You can install the required package using the following pip command:

```bash
pip install mixedbread

```

## [Anchor](https://qdrant.tech/documentation/embeddings/mixedbread/\#integration-example) Integration Example

Below is an example of how to obtain embeddings using MixedBread’s API and store them in a Qdrant collection:

```python
import qdrant_client
from qdrant_client.models import Batch
from mixedbread import MixedBreadModel

# Initialize MixedBread model
model = MixedBreadModel("mixedbread-variant")

# Generate embeddings
text = "MixedBread provides versatile embeddings for various domains."
embeddings = model.embed(text)

# Initialize Qdrant client
qdrant_client = qdrant_client.QdrantClient(host="localhost", port=6333)

# Upsert the embedding into Qdrant
qdrant_client.upsert(
    collection_name="VersatileEmbeddings",
    points=Batch(
        ids=[1],
        vectors=[embeddings],
    )
)

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/mixedbread.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/mixedbread.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574568445&cv=11&fst=1748574568445&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104611959~104611961&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixedbread%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=MixedBread%20-%20Qdrant&npa=0&pscdl=noapi&auid=1418220167.1748574568&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574568420&cv=11&fst=1748574568420&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104611959~104611961~103308615&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixedbread%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=MixedBread%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1418220167.1748574568&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=88be95e2-23e0-434c-b26b-46f08638070b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8307c5a5-072e-4515-85df-5104a22b3759&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixedbread%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=88be95e2-23e0-434c-b26b-46f08638070b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8307c5a5-072e-4515-85df-5104a22b3759&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixedbread%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574569395&cv=11&fst=1748574569395&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104611959~104611961&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmixedbread%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=MixedBread%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1418220167.1748574568&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)