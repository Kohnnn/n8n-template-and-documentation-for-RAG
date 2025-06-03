---
url: "https://qdrant.tech/blog/cohere-embedding-v3/"
title: "From Content Quality to Compression: The Evolution of Embedding Models at Cohere with Nils Reimers - Qdrant"
---

0

# From Content Quality to Compression: The Evolution of Embedding Models at Cohere with Nils Reimers

Demetrios Brinkmann

·

November 19, 2023

![From Content Quality to Compression: The Evolution of Embedding Models at Cohere with Nils Reimers](https://qdrant.tech/blog/cohere-embedding-v3/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcohere-embedding-v3%2F&text=From%20Content%20Quality%20to%20Compression:%20The%20Evolution%20of%20Embedding%20Models%20at%20Cohere%20with%20Nils%20Reimers "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcohere-embedding-v3%2F "LinkedIn")

For the second edition of our Vector Space Talks we were joined by none other than Cohere’s Head of Machine Learning Nils Reimers.

## [Anchor](https://qdrant.tech/blog/cohere-embedding-v3/\#key-takeaways) Key Takeaways

Let’s dive right into the five key takeaways from Nils’ talk:

1. Content Quality Estimation: Nils explained how embeddings have traditionally focused on measuring topic match, but content quality is just as important. He demonstrated how their model can differentiate between informative and non-informative documents.

2. Compression-Aware Training: He shared how they’ve tackled the challenge of reducing the memory footprint of embeddings, making it more cost-effective to run vector databases on platforms like [Qdrant](https://cloud.qdrant.io/login?ajs_anonymous_id=b567953f-3845-4136-9cfb-7f58a149870a).

3. Reinforcement Learning from Human Feedback: Nils revealed how they’ve borrowed a technique from reinforcement learning and applied it to their embedding models. This allows the model to learn preferences based on human feedback, resulting in highly informative responses.

4. Evaluating Embedding Quality: Nils emphasized the importance of evaluating embedding quality in relative terms rather than looking at individual vectors. It’s all about understanding the context and how embeddings relate to each other.

5. New Features in the Pipeline: Lastly, Nils gave us a sneak peek at some exciting features they’re developing, including input type support for Langchain and improved compression techniques.


Now, here’s a fun fact from the episode: Did you know that the content quality estimation model _can’t_ differentiate between true and fake statements? It’s a challenging task, and the model relies on the information present in its pretraining data.

We loved having Nils as our guest, check out the full talk below. If you or anyone you know would like to come on the Vector Space Talks

Cohere Embed V3 - Nils Reimers \| Vector Space Talks #002 - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Cohere Embed V3 - Nils Reimers \| Vector Space Talks #002](https://www.youtube.com/watch?v=Abh3YCahyqU)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=Abh3YCahyqU&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 24:31
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=Abh3YCahyqU "Watch on YouTube")

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=b567953f-3845-4136-9cfb-7f58a149870a)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5928a489-b38d-4841-bb9a-cf5dcb4b46df&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e470f14d-f0ce-4e87-8588-923913e32155&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcohere-embedding-v3%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5928a489-b38d-4841-bb9a-cf5dcb4b46df&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e470f14d-f0ce-4e87-8588-923913e32155&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcohere-embedding-v3%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)