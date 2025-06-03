---
url: "https://qdrant.tech/documentation/frameworks/superduper/"
title: "Superduper - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Superduper

# [Anchor](https://qdrant.tech/documentation/frameworks/superduper/\#superduper) Superduper

[Superduper](https://superduper.io/) is a framework for building flexible, compositional AI applications which may be applied directly to databases using a declarative programming model. These applications declare and maintain a desired state of the database, and use the database directly to store outputs of AI components, meta-data about the components and data pertaining to the state of the system.

Qdrant is available as a vector search provider in Superduper.

## [Anchor](https://qdrant.tech/documentation/frameworks/superduper/\#installation) Installation

```bash
pip install superduper-framework

```

## [Anchor](https://qdrant.tech/documentation/frameworks/superduper/\#setup) Setup

- To use Qdrant for vector search layer, create a `settings.yaml` file with the following config.

> settings.yaml

```yaml
cluster:
  vector_search:
    type: qdrant

vector_search_kwargs:
  url: "http://localhost:6333"
  api_key: "<YOUR_API_KEY>
  # Supports all parameters of qdrant_client.QdrantClient

```

- Set the `SUPERDUPER_CONFIG` env value to the path of the config file.

```bash
export SUPERDUPER_CONFIG=path/to/settings.yaml

```

That’s all. You can now use Superduper backed by Qdrant.

## [Anchor](https://qdrant.tech/documentation/frameworks/superduper/\#example) Example

Here’s an example to run vector search using the configured Qdrant index.

```python
import json
import requests
from superduper import superduper, Document
from superduper.ext.sentence_transformers import SentenceTransformer

r = requests.get('https://superduperdb-public-demo.s3.amazonaws.com/text.json')

with open('text.json', 'wb') as f:
    f.write(r.content)

with open('text.json', 'r') as f:
    data = json.load(f)

db = superduper('mongomock://test')

_ = db['documents'].insert_many([Document({'txt': txt}) for txt in data]).execute()

model = SentenceTransformer(
    identifier="test",
    predict_kwargs={"show_progress_bar": True},
    model="all-MiniLM-L6-v2",
    device="cpu",
    postprocess=lambda x: x.tolist(),
)

vector_index = model.to_vector_index(select=db['documents'].find(), key='txt')

db.apply(vector_index)

query = db['documents'].like({'txt': 'Tell me about vector-search'}, vector_index=vector_index.identifier, n=3).find()
cursor = query.execute()

for r in cursor:
    print('=' * 100)
    print(r.unpack()['txt'])
    print('=' * 100)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/superduper/\#-further-reading) 📚 Further Reading

- Superduper [Intro](https://docs.superduper.io/docs/intro)
- Superduper [Source](https://github.com/superduper-io/superduper)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/superduper.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/superduper.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574488801&cv=11&fst=1748574488801&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsuperduper%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Superduper%20-%20Qdrant&npa=0&pscdl=noapi&auid=1399865673.1748574489&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574488780&cv=11&fst=1748574488780&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsuperduper%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Superduper%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1399865673.1748574489&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=38b29501-2979-4d14-97f0-2e75d7790a49&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=90ecf193-10fe-43bc-be65-802faa914cad&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsuperduper%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=38b29501-2979-4d14-97f0-2e75d7790a49&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=90ecf193-10fe-43bc-be65-802faa914cad&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsuperduper%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574489982&cv=11&fst=1748574489982&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsuperduper%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Superduper%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1399865673.1748574489&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)