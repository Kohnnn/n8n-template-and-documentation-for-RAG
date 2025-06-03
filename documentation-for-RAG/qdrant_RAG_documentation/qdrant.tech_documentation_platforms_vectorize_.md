---
url: "https://qdrant.tech/documentation/platforms/vectorize/"
title: "Vectorize.io - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Platforms](https://qdrant.tech/documentation/platforms/)
- Vectorize.io

# [Anchor](https://qdrant.tech/documentation/platforms/vectorize/\#vectorizeio) Vectorize.io

[Vectorize](https://vectorize.io/) is a SaaS platform that automates data extraction from [several sources](https://docs.vectorize.io/integrations/source-connectors) and lets you quickly deploy real-time RAG pipelines for your unstructured data. It also includes evaluation to help figure out the best strategies for the RAG system.

Vectorize pipelines natively integrate with Qdrant by converting unstructured data into vector embeddings and storing them in a collection. When a pipeline is running, any new change in the source data is immediately processed, keeping the vector index up-to-date.

## [Anchor](https://qdrant.tech/documentation/platforms/vectorize/\#watch-the-video) Watch the Video

Load Data to Qdrant: How to Chunk and Vectorize Text in 5 Minutes - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Load Data to Qdrant: How to Chunk and Vectorize Text in 5 Minutes](https://www.youtube.com/watch?v=zHJ3TZmKEeY)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=zHJ3TZmKEeY&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

0:00

0:00 / 5:38
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=zHJ3TZmKEeY "Watch on YouTube")

## [Anchor](https://qdrant.tech/documentation/platforms/vectorize/\#prerequisites) Prerequisites

1. A Qdrant instance to connect to. You can get a free cloud instance at [cloud.qdrant.io](https://cloud.qdrant.io/?ajs_anonymous_id=72bf60e1-00ac-4b75-8f1b-07f4ff812f22).
2. An account at [Vectorize.io](https://vectorize.io/) for building those seamless pipelines.

## [Anchor](https://qdrant.tech/documentation/platforms/vectorize/\#set-up) Set Up

- From the Vectorize dashboard, click `Vector Databases` -\> `New Vector Database Integration` and select Qdrant.

- Set up a connection using the hostname and API key of your Qdrant instance.


![Vectorize connection](https://qdrant.tech/documentation/platforms/vectorize/vectorize-connection.png)

- You can now select this Qdrant instance when setting up a [RAG pipeline](https://docs.vectorize.io/rag-pipelines/creating). Enter the name of the collection to use. It’ll be created automatically if it doesn’t exist.

![Vectorize collection](https://qdrant.tech/documentation/platforms/vectorize/vectorize-collection.png)

- Select an embeddings provider.

![Vectorize Embeddings](https://qdrant.tech/documentation/platforms/vectorize/vectorize-embeddings.png)

- Select a source from which to ingest data.

![Vectorize Sources](https://qdrant.tech/documentation/platforms/vectorize/vectorize-sources.png)

Your Vectorize pipeline powered by Qdrant should now be up and ready to be scheduled and monitored.

## [Anchor](https://qdrant.tech/documentation/platforms/vectorize/\#further-reading) Further Reading

- Vectorize [Documentation](https://docs.vectorize.io/)
- Vectorize [Tutorials](https://docs.vectorize.io/tutorials/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/platforms/vectorize.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/platforms/vectorize.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=de851cab-5cdb-407a-8c3c-d1d37cc02d4f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=88a2e1ee-e279-441e-a953-e23ce9056161&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fvectorize%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=de851cab-5cdb-407a-8c3c-d1d37cc02d4f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=88a2e1ee-e279-441e-a953-e23ce9056161&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fplatforms%2Fvectorize%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)