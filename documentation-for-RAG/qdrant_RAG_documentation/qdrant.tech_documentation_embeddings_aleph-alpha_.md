---
url: "https://qdrant.tech/documentation/embeddings/aleph-alpha/"
title: "Aleph Alpha - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Aleph Alpha

# [Anchor](https://qdrant.tech/documentation/embeddings/aleph-alpha/\#using-aleph-alpha-embeddings-with-qdrant) Using Aleph Alpha Embeddings with Qdrant

Aleph Alpha is a multimodal and multilingual embeddings’ provider. Their API allows creating the embeddings for text and images, both
in the same latent space. They maintain an [official Python client](https://github.com/Aleph-Alpha/aleph-alpha-client) that might be
installed with pip:

```bash
pip install aleph-alpha-client

```

There is both synchronous and asynchronous client available. Obtaining the embeddings for an image and storing it into Qdrant might
be done in the following way:

```python
import qdrant_client
from qdrant_client.models import Batch

from aleph_alpha_client import (
    Prompt,
    AsyncClient,
    SemanticEmbeddingRequest,
    SemanticRepresentation,
    ImagePrompt
)

aa_token = "<< your_token >>"
model = "luminous-base"

qdrant_client = qdrant_client.QdrantClient()
async with AsyncClient(token=aa_token) as client:
    prompt = ImagePrompt.from_file("./path/to/the/image.jpg")
    prompt = Prompt.from_image(prompt)

    query_params = {
        "prompt": prompt,
        "representation": SemanticRepresentation.Symmetric,
        "compress_to_size": 128,
    }
    query_request = SemanticEmbeddingRequest(**query_params)
    query_response = await client.semantic_embed(
        request=query_request, model=model
    )

    qdrant_client.upsert(
        collection_name="MyCollection",
        points=Batch(
            ids=[1],
            vectors=[query_response.embedding],
        )
    )

```

If we wanted to create text embeddings with the same model, we wouldn’t use `ImagePrompt.from_file`, but simply provide the input
text into the `Prompt.from_text` method.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/aleph-alpha.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/aleph-alpha.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574321090&cv=11&fst=1748574321090&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Faleph-alpha%2F&hn=www.googleadservices.com&frm=0&tiba=Aleph%20Alpha%20-%20Qdrant&npa=0&pscdl=noapi&auid=1229665381.1748574321&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574321057&cv=11&fst=1748574321057&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Faleph-alpha%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Aleph%20Alpha%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1229665381.1748574321&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7c6e51ae-35e0-4721-b6cb-d4ce07bf4018&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8aa5c7cb-a3c6-4866-a521-c30ce3ff7573&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Faleph-alpha%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7c6e51ae-35e0-4721-b6cb-d4ce07bf4018&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8aa5c7cb-a3c6-4866-a521-c30ce3ff7573&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Faleph-alpha%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574322231&cv=11&fst=1748574322231&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Faleph-alpha%2F&hn=www.googleadservices.com&frm=0&tiba=Aleph%20Alpha%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1229665381.1748574321&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)