---
url: "https://qdrant.tech/documentation/frameworks/langchain4j/"
title: "Langchain4J - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Langchain4J

# [Anchor](https://qdrant.tech/documentation/frameworks/langchain4j/\#langchain-for-java) LangChain for Java

LangChain for Java, also known as [Langchain4J](https://github.com/langchain4j/langchain4j), is a community port of [Langchain](https://www.langchain.com/) for building context-aware AI applications in Java

You can use Qdrant as a vector store in Langchain4J through the [`langchain4j-qdrant`](https://central.sonatype.com/artifact/dev.langchain4j/langchain4j-qdrant) module.

## [Anchor](https://qdrant.tech/documentation/frameworks/langchain4j/\#setup) Setup

Add the `langchain4j-qdrant` to your project dependencies.

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-qdrant</artifactId>
    <version>VERSION</version>
</dependency>

```

## [Anchor](https://qdrant.tech/documentation/frameworks/langchain4j/\#usage) Usage

Before you use the following code sample, customize the following values for your configuration:

- `YOUR_COLLECTION_NAME`: Use our [Collections](https://qdrant.tech/documentation/concepts/collections/) guide to create or
list collections.
- `YOUR_HOST_URL`: Use the GRPC URL for your system. If you used the [Quick Start](https://qdrant.tech/documentation/quick-start/) guide,
it may be http://localhost:6334. If you’ve deployed in the [Qdrant Cloud](https://qdrant.tech/documentation/cloud/), you may have a
longer URL such as `https://example.location.cloud.qdrant.io:6334`.
- `YOUR_API_KEY`: Substitute the API key associated with your configuration.

```java
import dev.langchain4j.store.embedding.EmbeddingStore;
import dev.langchain4j.store.embedding.qdrant.QdrantEmbeddingStore;

EmbeddingStore<TextSegment> embeddingStore =
    QdrantEmbeddingStore.builder()
        // Ensure the collection is configured with the appropriate dimensions
        // of the embedding model.
        // Reference https://qdrant.tech/documentation/concepts/collections/
        .collectionName("YOUR_COLLECTION_NAME")
        .host("YOUR_HOST_URL")
        // GRPC port of the Qdrant server
        .port(6334)
        .apiKey("YOUR_API_KEY")
        .build();

```

`QdrantEmbeddingStore` supports all the semantic features of Langchain4J.

## [Anchor](https://qdrant.tech/documentation/frameworks/langchain4j/\#further-reading) Further Reading

- You can refer to the [Langchain4J examples](https://github.com/langchain4j/langchain4j-examples/) to get started.
- [Source Code](https://github.com/langchain4j/langchain4j/tree/main/langchain4j-qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/langchain4j.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/langchain4j.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574153856&cv=11&fst=1748574153856&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain4j%2F&hn=www.googleadservices.com&frm=0&tiba=Langchain4J%20-%20Qdrant&npa=0&pscdl=noapi&auid=482172372.1748574154&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574153831&cv=11&fst=1748574153831&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain4j%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Langchain4J%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=482172372.1748574154&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5e2264d2-a3a7-4ef7-afab-e3f12357f0fa&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=100dc29f-5495-4388-b852-8b196aec2240&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain4j%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5e2264d2-a3a7-4ef7-afab-e3f12357f0fa&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=100dc29f-5495-4388-b852-8b196aec2240&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain4j%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574155174&cv=11&fst=1748574155174&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain4j%2F&hn=www.googleadservices.com&frm=0&tiba=Langchain4J%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=482172372.1748574154&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)