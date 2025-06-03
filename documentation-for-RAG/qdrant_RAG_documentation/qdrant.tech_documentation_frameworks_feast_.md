---
url: "https://qdrant.tech/documentation/frameworks/feast/"
title: "Feast - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Feast

## [Anchor](https://qdrant.tech/documentation/frameworks/feast/\#feast) Feast

[Feast ( **Fe** ature **St** ore)](https://docs.feast.dev/) is an open-source feature store that helps teams operate production ML systems at scale by allowing them to define, manage, validate, and serve features for production AI/ML.

Qdrant is available as a supported vectorstore in Feast to integrate in your workflows.

## [Anchor](https://qdrant.tech/documentation/frameworks/feast/\#insatallation) Insatallation

To use the Qdrant online store, you need to install Feast with the `qdrant` extra.

```bash
pip install 'feast[qdrant]'

```

## [Anchor](https://qdrant.tech/documentation/frameworks/feast/\#usage) Usage

An example config with Qdrant could look like:

```yaml
project: my_feature_repo
registry: data/registry.db
provider: local
online_store:
    type: qdrant
    host: xyz-example.eu-central.aws.cloud.qdrant.io
    port: 6333
    api_key: <your-own-key>
    vector_len: 384
    # Reference: https://qdrant.tech/documentation/concepts/vectors/#named-vectors
    # vector_name: text-vec
    write_batch_size: 100

```

You can refer to the Feast [documentation](https://docs.feast.dev/reference/alpha-vector-database#configuration-and-installation) for the full list of configuration options.

## [Anchor](https://qdrant.tech/documentation/frameworks/feast/\#retrieving-documents) Retrieving Documents

The Qdrant online store supports retrieving document vectors for a given list of entity keys. The document vectors are returned as a dictionary where the key is the entity key and the value being the vector.

```python
from feast import FeatureStore

feature_store = FeatureStore(repo_path="feature_store.yaml")

query_vector = [1.0, 2.0, 3.0, 4.0, 5.0]
top_k = 5

feature_values = feature_store.retrieve_online_documents(
    feature="my_feature",
    query=query_vector,
    top_k=top_k
)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/feast/\#-further-reading) 📚 Further Reading

- [Feast Documentation](http://docs.feast.dev/)
- [Source](https://github.com/feast-dev/feast/tree/master/sdk/python/feast/infra/online_stores/)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/feast.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/feast.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d724e8bc-a5c8-4f9d-94ce-0a8d8cede110&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=60366d67-3ce7-4d8c-93b0-c461d069071e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Ffeast%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575306975&cv=11&fst=1748575306975&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Ffeast%2F&hn=www.googleadservices.com&frm=0&tiba=Feast%20-%20Qdrant&npa=0&pscdl=noapi&auid=1808115673.1748575307&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575306950&cv=11&fst=1748575306950&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Ffeast%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Feast%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1808115673.1748575307&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575307228&cv=11&fst=1748575307228&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Ffeast%2F&hn=www.googleadservices.com&frm=0&tiba=Feast%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1808115673.1748575307&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d724e8bc-a5c8-4f9d-94ce-0a8d8cede110&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=60366d67-3ce7-4d8c-93b0-c461d069071e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Ffeast%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)