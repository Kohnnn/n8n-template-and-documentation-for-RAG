---
url: "https://qdrant.tech/documentation/frameworks/rig-rs/"
title: "Rig-rs - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Rig-rs

# [Anchor](https://qdrant.tech/documentation/frameworks/rig-rs/\#rig-rs) Rig-rs

[Rig](http://rig.rs/) is a Rust library for building scalable, modular, and ergonomic LLM-powered applications. It has full support for LLM completion and embedding workflows with minimal boiler plate.

Rig supports Qdrant as a vectorstore to ingest and search for documents semantically.

## [Anchor](https://qdrant.tech/documentation/frameworks/rig-rs/\#installation) Installation

```console
cargo add rig-core rig-qdrant qdrant-client

```

## [Anchor](https://qdrant.tech/documentation/frameworks/rig-rs/\#usage) Usage

Here’s an example ingest and retrieve flow using Rig and Qdrant.

```rust
use qdrant_client::{
    qdrant::{PointStruct, QueryPointsBuilder, UpsertPointsBuilder},
    Payload, Qdrant,
};
use rig::{
    embeddings::EmbeddingsBuilder,
    providers::openai::{Client, TEXT_EMBEDDING_3_SMALL},
    vector_store::VectorStoreIndex,
};
use rig_qdrant::QdrantVectorStore;
use serde_json::json;

const COLLECTION_NAME: &str = "rig-collection";

// Initialize Qdrant client.
let client = Qdrant::from_url("http://localhost:6334").build()?;
// Initialize OpenAI client.
let openai_client = Client::new("<OPENAI_API_KEY>");
let model = openai_client.embedding_model(TEXT_EMBEDDING_3_SMALL);

let documents = EmbeddingsBuilder::new(model.clone())
    .simple_document("0981d983-a5f8-49eb-89ea-f7d3b2196d2e", "Definition of a *flurbo*: A flurbo is a green alien that lives on cold planets")
    .simple_document("62a36d43-80b6-4fd6-990c-f75bb02287d1", "Definition of a *glarb-glarb*: A glarb-glarb is a ancient tool used by the ancestors of the inhabitants of planet Jiro to farm the land.")
    .simple_document("f9e17d59-32e5-440c-be02-b2759a654824", "Definition of a *linglingdong*: A term used by inhabitants of the far side of the moon to describe humans.")
    .build()
    .await?;

let points: Vec<PointStruct> = documents
    .into_iter()
    .map(|d| {
        let vec: Vec<f32> = d.embeddings[0].vec.iter().map(|&x| x as f32).collect();
        PointStruct::new(
            d.id,
            vec,
            Payload::try_from(json!({
                "document": d.document,
            }))
            .unwrap(),
        )
    })
    .collect();

client
    .upsert_points(UpsertPointsBuilder::new(COLLECTION_NAME, points))
    .await?;

let query_params = QueryPointsBuilder::new(COLLECTION_NAME).with_payload(true);
let vector_store = QdrantVectorStore::new(client, model, query_params.build());

let results = vector_store
    .top_n::<serde_json::Value>("Define a glarb-glarb?", 1)
    .await?;

println!("Results: {:?}", results);

```

## [Anchor](https://qdrant.tech/documentation/frameworks/rig-rs/\#further-reading) Further reading

- [Rig-rs Documentation](https://rig.rs/)
- [Source Code](https://github.com/0xPlaygrounds/rig)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/rig-rs.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/rig-rs.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575076648&cv=11&fst=1748575076648&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Frig-rs%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Rig-rs%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=45033316.1748575076&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575076685&cv=11&fst=1748575076685&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Frig-rs%2F&hn=www.googleadservices.com&frm=0&tiba=Rig-rs%20-%20Qdrant&npa=0&pscdl=noapi&auid=45033316.1748575076&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=2d0daf26-e6a6-4c51-a0be-f03a93b1926a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7aa66a06-bcac-4e72-a30a-4172ab4ea0da&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Frig-rs%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=2d0daf26-e6a6-4c51-a0be-f03a93b1926a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7aa66a06-bcac-4e72-a30a-4172ab4ea0da&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Frig-rs%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575077586&cv=11&fst=1748575077586&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Frig-rs%2F&hn=www.googleadservices.com&frm=0&tiba=Rig-rs%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=45033316.1748575076&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)