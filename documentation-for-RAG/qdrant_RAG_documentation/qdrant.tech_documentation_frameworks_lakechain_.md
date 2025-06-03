---
url: "https://qdrant.tech/documentation/frameworks/lakechain/"
title: "AWS Lakechain - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- AWS Lakechain

# [Anchor](https://qdrant.tech/documentation/frameworks/lakechain/\#aws-lakechain) AWS Lakechain

[Project Lakechain](https://awslabs.github.io/project-lakechain/) is a framework based on the AWS Cloud Development Kit (CDK), allowing to express and deploy scalable document processing pipelines on AWS using infrastructure-as-code. It emphasizes on modularity and extensibility of pipelines, and provides 60+ ready to use components for prototyping complex processing pipelines that scale out of the box to millions of documents.

The Qdrant storage connector available with Lakechain enables uploading vector embeddings produced by other middlewares to a Qdrant collection.

To use the Qdrant storage connector, you import it in your CDK stack, and connect it to a data source providing document embeddings.

> You need to specify a Qdrant API key to the connector, by specifying a reference to an [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) secret containing the API key.

```typescript
import { QdrantStorageConnector } from '@project-lakechain/qdrant-storage-connector';
import { CacheStorage } from '@project-lakechain/core';

class Stack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string) {
    const cache = new CacheStorage(this, 'Cache');

    const qdrantApiKey = secrets.Secret.fromSecretNameV2(
      this,
      'QdrantApiKey',
      process.env.QDRANT_API_KEY_SECRET_NAME as string
    );

    const connector = new QdrantStorageConnector.Builder()
      .withScope(this)
      .withIdentifier('QdrantStorageConnector')
      .withCacheStorage(cache)
      .withSource(source) // 👈 Specify a data source
      .withApiKey(qdrantApiKey)
      .withCollectionName('{collection_name}')
      .withUrl('https://xyz-example.eu-central.aws.cloud.qdrant.io:6333')
      .build();
  }
}

```

When the document being processed is a text document, you can choose to store the text of the document in the Qdrant payload. To do so, you can use the `withStoreText` and `withTextKey` options. If the document is not a text, this option is ignored.

```typescript
const connector = new QdrantStorageConnector.Builder()
  .withScope(this)
  .withIdentifier('QdrantStorageConnector')
  .withCacheStorage(cache)
  .withSource(source)
  .withApiKey(qdrantApiKey)
  .withCollectionName('{collection_name}')
  .withStoreText(true)
  .withTextKey('my-content')
  .withUrl('https://xyz-example.eu-central.aws.cloud.qdrant.io:6333')
  .build();

```

Since Qdrant supports [multiple vectors](https://qdrant.tech/documentation/concepts/vectors/#named-vectors) per point, you can use the `withVectorName` option to specify one. The connector defaults to unnamed (default) vector.

```typescript
const connector = new QdrantStorageConnector.Builder()
      .withScope(this)
      .withIdentifier('QdrantStorageConnector')
      .withCacheStorage(cache)
      .withSource(source)
      .withApiKey(qdrantApiKey)
      .withCollectionName('collection_name')
      .withVectorName('my-vector-name')
      .withUrl('https://xyz-example.eu-central.aws.cloud.qdrant.io:6333')
      .build();

```

## [Anchor](https://qdrant.tech/documentation/frameworks/lakechain/\#further-reading) Further Reading

- [Introduction to Lakechain](https://awslabs.github.io/project-lakechain/general/introduction/)
- [Lakechain Examples](https://github.com/awslabs/project-lakechain/tree/main/examples)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/lakechain.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/lakechain.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573914850&cv=11&fst=1748573914850&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flakechain%2F&hn=www.googleadservices.com&frm=0&tiba=AWS%20Lakechain%20-%20Qdrant&npa=0&pscdl=noapi&auid=1801971302.1748573915&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573914829&cv=11&fst=1748573914829&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flakechain%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=AWS%20Lakechain%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1801971302.1748573915&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e4999124-0c9c-4ac9-8a47-4212779efd11&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d3998999-45e6-4b0a-bd1c-23295d4e5db7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flakechain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e4999124-0c9c-4ac9-8a47-4212779efd11&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d3998999-45e6-4b0a-bd1c-23295d4e5db7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flakechain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573916076&cv=11&fst=1748573916076&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flakechain%2F&hn=www.googleadservices.com&frm=0&tiba=AWS%20Lakechain%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1801971302.1748573915&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)