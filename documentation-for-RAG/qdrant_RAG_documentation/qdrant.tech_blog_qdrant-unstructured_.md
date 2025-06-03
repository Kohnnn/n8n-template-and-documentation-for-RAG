---
url: "https://qdrant.tech/blog/qdrant-unstructured/"
title: "Loading Unstructured.io Data into Qdrant from the Terminal - Qdrant"
---

0

# Loading Unstructured.io Data into Qdrant from the Terminal

Anush Shetty

·

January 09, 2024

![Loading Unstructured.io Data into Qdrant from the Terminal](https://qdrant.tech/blog/qdrant-unstructured/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-unstructured%2F&text=Loading%20Unstructured.io%20Data%20into%20Qdrant%20from%20the%20Terminal "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-unstructured%2F "LinkedIn")

Building powerful applications with Qdrant starts with loading vector representations into the system. Traditionally, this involves scraping or extracting data from sources, performing operations such as cleaning, chunking, and generating embeddings, and finally loading it into Qdrant. While this process can be complex, Unstructured.io includes Qdrant as an ingestion destination.

In this blog post, we’ll demonstrate how to load data into Qdrant from the channels of a Discord server. You can use a similar process for the [20+ vetted data sources](https://unstructured-io.github.io/unstructured/ingest/source_connectors.html) supported by Unstructured.

### [Anchor](https://qdrant.tech/blog/qdrant-unstructured/\#prerequisites) Prerequisites

- A running Qdrant instance. Refer to our [Quickstart guide](https://qdrant.tech/documentation/quick-start/) to set up an instance.
- A Discord bot token. Generate one [here](https://discord.com/developers/applications) after adding the bot to your server.
- Unstructured CLI with the required extras. For more information, see the Discord [Getting Started guide](https://discord.com/developers/docs/getting-started). Install it with the following command:

```bash
pip install unstructured[discord,local-inference,qdrant]

```

Once you have the prerequisites in place, let’s begin the data ingestion.

### [Anchor](https://qdrant.tech/blog/qdrant-unstructured/\#retrieving-data-from-discord) Retrieving Data from Discord

To generate structured data from Discord using the Unstructured CLI, run the following command with the [channel IDs](https://www.pythondiscord.com/pages/guides/pydis-guides/contributing/obtaining-discord-ids/):

```bash
unstructured-ingest \
  discord \
  --channels <CHANNEL_IDS> \
  --token "<YOUR_BOT_TOKEN>" \
  --output-dir "discord-output"

```

This command downloads and structures the data in the `"discord-output"` directory.

For a complete list of options supported by this source, run:

```bash
unstructured-ingest discord --help

```

### [Anchor](https://qdrant.tech/blog/qdrant-unstructured/\#ingesting-into-qdrant) Ingesting into Qdrant

Before loading the data, set up a collection with the information you need for the following REST call. In this example we use a local Huggingface model generating 384-dimensional embeddings. You can create a Qdrant [API key](https://qdrant.tech/documentation/cloud/authentication/#create-api-keys) and set names for your Qdrant [collections](https://qdrant.tech/documentation/concepts/collections/).

We set up the collection with the following command:

```bash
curl -X PUT \
  <QDRANT_URL>/collections/<COLLECTION_NAME> \
  -H 'Content-Type: application/json' \
  -H 'api-key: <QDRANT_API_KEY>' \
  -d '{
    "vectors": {
      "size": 384,
      "distance": "Cosine"
    }
}'

```

You should receive a response similar to:

```console
{"result":true,"status":"ok","time":0.196235768}

```

To ingest the Discord data into Qdrant, run:

```bash
unstructured-ingest \
  local \
  --input-path "discord-output" \
  --embedding-provider "langchain-huggingface" \
  qdrant \
  --collection-name "<COLLECTION_NAME>" \
  --api-key "<QDRANT_API_KEY>" \
  --location "<QDRANT_URL>"

```

This command loads structured Discord data into Qdrant with sensible defaults. You can configure the data fields for which embeddings are generated in the command options. Qdrant ingestion also supports partitioning and chunking of your data, configurable directly from the CLI. Learn more about it in the [Unstructured documentation](https://unstructured-io.github.io/unstructured/core.html).

To list all the supported options of the Qdrant ingestion destination, run:

```bash
unstructured-ingest local qdrant --help

```

Unstructured can also be used programmatically or via the hosted API. Refer to the [Unstructured Reference Manual](https://unstructured-io.github.io/unstructured/introduction.html).

For more information about the Qdrant ingest destination, review how Unstructured.io configures their [Qdrant](https://unstructured-io.github.io/unstructured/ingest/destination_connectors/qdrant.html) interface.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=5113b7c3-aa5d-4322-87e3-33e47438ecc1)

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

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=745f37d7be0e530b98218683bf2ee377&enableResponsiveStyles=true)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=bb4defe7-d4ab-45ec-9f9a-4d1c375525b1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b92b1a19-0958-4c2d-94b7-a8cd8a74f0be&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-unstructured%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573819972&cv=11&fst=1748573819972&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-unstructured%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Loading%20Unstructured.io%20Data%20into%20Qdrant%20from%20the%20Terminal%20-%20Qdrant&npa=0&pscdl=noapi&auid=2059169579.1748573819&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573819931&cv=11&fst=1748573819931&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-unstructured%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Loading%20Unstructured.io%20Data%20into%20Qdrant%20from%20the%20Terminal%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2059169579.1748573819&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573820130&cv=11&fst=1748573820130&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-unstructured%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Loading%20Unstructured.io%20Data%20into%20Qdrant%20from%20the%20Terminal%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2059169579.1748573819&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=bb4defe7-d4ab-45ec-9f9a-4d1c375525b1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b92b1a19-0958-4c2d-94b7-a8cd8a74f0be&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-unstructured%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)