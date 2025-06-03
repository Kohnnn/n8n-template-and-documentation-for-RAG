---
url: "https://qdrant.tech/documentation/frameworks/spring-ai/"
title: "Spring AI - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Spring AI

# [Anchor](https://qdrant.tech/documentation/frameworks/spring-ai/\#spring-ai) Spring AI

[Spring AI](https://docs.spring.io/spring-ai/reference/) is a Java framework that provides a [Spring-friendly](https://spring.io/) API and abstractions for developing AI applications.

Qdrant is available as supported vector database for use within your Spring AI projects.

## [Anchor](https://qdrant.tech/documentation/frameworks/spring-ai/\#installation) Installation

You can find the Spring AI installation instructions [here](https://docs.spring.io/spring-ai/reference/getting-started.html).

Add the Qdrant boot starter package.

```xml
<dependency>
 <groupId>org.springframework.ai</groupId>
 <artifactId>spring-ai-qdrant-store-spring-boot-starter</artifactId>
</dependency>

```

## [Anchor](https://qdrant.tech/documentation/frameworks/spring-ai/\#usage) Usage

Configure Qdrant with Spring Boot’s `application.properties`.

```
spring.ai.vectorstore.qdrant.host=<host of your qdrant instance>
spring.ai.vectorstore.qdrant.port=<the GRPC port of your qdrant instance>
spring.ai.vectorstore.qdrant.api-key=<your api key>
spring.ai.vectorstore.qdrant.collection-name=<The name of the collection to use in Qdrant>

```

Learn more about these options in the [configuration reference](https://docs.spring.io/spring-ai/reference/api/vectordbs/qdrant.html#qdrant-vectorstore-properties).

Or you can set up the Qdrant vector store with the `QdrantVectorStoreConfig` options.

```java
@Bean
public QdrantVectorStoreConfig qdrantVectorStoreConfig() {

    return QdrantVectorStoreConfig.builder()
        .withHost("<QDRANT_HOSTNAME>")
        .withPort(<QDRANT_GRPC_PORT>)
        .withCollectionName("<QDRANT_COLLECTION_NAME>")
        .withApiKey("<QDRANT_API_KEY>")
        .build();
}

```

Build the vector store using the config and any of the support [Spring AI embedding providers](https://docs.spring.io/spring-ai/reference/api/embeddings.html#available-implementations).

```java
@Bean
public VectorStore vectorStore(QdrantVectorStoreConfig config, EmbeddingClient embeddingClient) {
    return new QdrantVectorStore(config, embeddingClient);
}

```

You can now use the `VectorStore` instance backed by Qdrant as a vector store in the Spring AI APIs.

## [Anchor](https://qdrant.tech/documentation/frameworks/spring-ai/\#-further-reading) 📚 Further Reading

- Spring AI [Qdrant reference](https://docs.spring.io/spring-ai/reference/api/vectordbs/qdrant.html)
- Spring AI [API reference](https://docs.spring.io/spring-ai/reference/index.html)
- [Source Code](https://github.com/spring-projects/spring-ai/tree/main/vector-stores/spring-ai-qdrant-store)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/spring-ai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/spring-ai.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574013192&cv=11&fst=1748574013192&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fspring-ai%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Spring%20AI%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1179854634.1748574013&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574013395&cv=11&fst=1748574013395&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fspring-ai%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Spring%20AI%20-%20Qdrant&npa=0&pscdl=noapi&auid=1179854634.1748574013&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=557aa5dd-8ec6-4f1f-9bbe-69df737114e2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3d6aa304-c1a2-4663-bc2f-7b6cc781dd7a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fspring-ai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=557aa5dd-8ec6-4f1f-9bbe-69df737114e2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3d6aa304-c1a2-4663-bc2f-7b6cc781dd7a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fspring-ai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574014587&cv=11&fst=1748574014587&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fspring-ai%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Spring%20AI%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1179854634.1748574013&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)