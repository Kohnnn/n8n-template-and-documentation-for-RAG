---
url: "https://qdrant.tech/documentation/platforms/mulesoft/"
title: "Salesforce Mulesoft - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Platforms](https://qdrant.tech/documentation/platforms/)
- Salesforce Mulesoft

# [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#salesforce-mulesoft) Salesforce Mulesoft

[MuleSoft Anypoint](https://www.salesforce.com/in/mulesoft/anypoint-platform/) is an integration platform to connect applications, data, and devices across on-premises and cloud environments. It provides a unified platform to build, manage, and secure APIs and integrations, making digital transformation smoother and more scalable.

[MAC Project](https://mac-project.ai/) is an open-source initiative to bring AI capabilities into the MuleSoft ecosystem. It provides connectors to add AI capabilities to an Anypoint project by integrating LLMs, vector databases including Qdrant.

## [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#setup) Setup

To use Qdrant with Anypoint, you can install the [Mulesoft Vectors connector](https://mac-project.ai/docs/ms-vectors). Paste the following Maven Dependency into your Mule application pom file.

```xml
<dependency>
    <groupId>io.github.mulesoft-ai-chain-project</groupId>
    <artifactId>mule4-vectors-connector</artifactId>
    <version>0.3.0</version>
    <classifier>mule-plugin</classifier>
</dependency>

```

The project will now rebuild with the connector. You also need to install the optional dependencies for the Qdrant connector.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="..." >

...

<build>
 <plugins>
  ...
  <plugin>
   <groupId>org.mule.tools.maven</groupId>
   <artifactId>mule-maven-plugin</artifactId>
   <version>4.3.0</version>
   <extensions>true</extensions>
   <configuration>
    <additionalPluginDependencies>
     <plugin>
      <groupId>io.github.mulesoft-ai-chain-project</groupId>
      <artifactId>mule4-vectors-connector</artifactId>
      <additionalDependencies>
       <!-- QDRANT CONNECTOR DEPENDENCY -->
       <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-qdrant</artifactId>
        <version>0.35.0</version>
       </dependency>
       <!-- QDRANT CONNECTOR DEPENDENCY -->
      </additionalDependencies>
     </plugin>
    </additionalPluginDependencies>
   </configuration>
  </plugin>
 </plugins>
</build>
...
</project>

```

## [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#usage) Usage

The MuleSoft Vectors connector is shipped with 3 different categories of operations: Document, Embedding and Store. For each category a dedicated configuration must be defined.

The store configuration allows to pick-up the right vector store option among the available ones. When configuring the connection to a specific vector store it’s also possible to test it.

Go to the `Global Elements` in your MuleSoft project, and create a new configuration. In the `Connector Configuration`, you will find the `MuleSoft Vectors Connector Store` config.

Upon selecting `Qdrant`, you’ll be presented with the following parameters to set up the connection to a Qdrant instance.

![Qdrant Connection](https://qdrant.tech/documentation/platforms/mulesoft/qdrant-connection.png)

Once a connection is set up, you can now use the following Qdrant operations in your workflows.

### [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#store-add) Store Add

The Add operation adds a document or text to a collection.

![Qdrant Add](https://qdrant.tech/documentation/platforms/mulesoft/qdrant-add.png)

### [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#store-list) Store List

The List sources operation lists all entries in a collection.

![Qdrant List](https://qdrant.tech/documentation/platforms/mulesoft/qdrant-list.png)

### [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#store-query) Store Query

The Query operation retrieves information from a collection based on a query a embedding and an optional filter.

![Qdrant Query](https://qdrant.tech/documentation/platforms/mulesoft/qdrant-query.png)

### [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#store-remove) Store Remove

The Remove operation remove all entries from a collection based on a filter.

![Qdrant Add](https://qdrant.tech/documentation/platforms/mulesoft/qdrant-remove.png)

## [Anchor](https://qdrant.tech/documentation/platforms/mulesoft/\#further-reading) Further reading

- [Mulesoft Anypoint Studio](https://docs.mulesoft.com/studio/latest/)
- [MAC Project](https://mac-project.ai/)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/platforms/mulesoft.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/platforms/mulesoft.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573887493&cv=11&fst=1748573887493&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fmulesoft%2F&hn=www.googleadservices.com&frm=0&tiba=Salesforce%20Mulesoft%20-%20Qdrant&npa=0&pscdl=noapi&auid=2059362710.1748573887&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573887456&cv=11&fst=1748573887456&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fmulesoft%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Salesforce%20Mulesoft%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2059362710.1748573887&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=07a2bc5c-ad4c-4322-8652-67220942f624&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ac4fb0b-7ebe-4852-9970-537f73d695cf&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fmulesoft%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=07a2bc5c-ad4c-4322-8652-67220942f624&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ac4fb0b-7ebe-4852-9970-537f73d695cf&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fmulesoft%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)