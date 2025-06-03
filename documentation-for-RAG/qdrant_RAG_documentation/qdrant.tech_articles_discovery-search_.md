---
url: "https://qdrant.tech/articles/discovery-search/"
title: "Discovery needs context - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Discovery needs context

[Back to Data Exploration](https://qdrant.tech/articles/data-exploration/)

# Discovery needs context

Luis Cossío

·

January 31, 2024

![Discovery needs context](https://qdrant.tech/articles_data/discovery-search/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/discovery-search/\#discovery-needs-context) Discovery needs context

When Christopher Columbus and his crew sailed to cross the Atlantic Ocean, they were not looking for the Americas. They were looking for a new route to India because they were convinced that the Earth was round. They didn’t know anything about a new continent, but since they were going west, they stumbled upon it.

They couldn’t reach their _target_, because the geography didn’t let them, but once they realized it wasn’t India, they claimed it a new “discovery” for their crown. If we consider that sailors need water to sail, then we can establish a _context_ which is positive in the water, and negative on land. Once the sailor’s search was stopped by the land, they could not go any further, and a new route was found. Let’s keep these concepts of _target_ and _context_ in mind as we explore the new functionality of Qdrant: **Discovery search**.

## [Anchor](https://qdrant.tech/articles/discovery-search/\#what-is-discovery-search) What is discovery search?

In version 1.7, Qdrant [released](https://qdrant.tech/articles/qdrant-1.7.x/) this novel API that lets you constrain the space in which a search is performed, relying only on pure vectors. This is a powerful tool that lets you explore the vector space in a more controlled way. It can be used to find points that are not necessarily closest to the target, but are still relevant to the search.

You can already select which points are available to the search by using payload filters. This by itself is very versatile because it allows us to craft complex filters that show only the points that satisfy their criteria deterministically. However, the payload associated with each point is arbitrary and cannot tell us anything about their position in the vector space. In other words, filtering out irrelevant points can be seen as creating a _mask_ rather than a hyperplane –cutting in between the positive and negative vectors– in the space.

## [Anchor](https://qdrant.tech/articles/discovery-search/\#understanding-context) Understanding context

This is where a **vector _context_** can help. We define _context_ as a list of pairs. Each pair is made up of a positive and a negative vector. With a context, we can define hyperplanes within the vector space, which always prefer the positive over the negative vectors. This effectively partitions the space where the search is performed. After the space is partitioned, we then need a _target_ to return the points that are more similar to it.

![Discovery search visualization](https://qdrant.tech/articles_data/discovery-search/discovery-search.png)

While positive and negative vectors might suggest the use of the [recommendation interface](https://qdrant.tech/documentation/concepts/explore/#recommendation-api), in the case of _context_ they require to be paired up in a positive-negative fashion. This is inspired from the machine-learning concept of [_triplet loss_](https://en.wikipedia.org/wiki/Triplet_loss), where you have three vectors: an anchor, a positive, and a negative. Triplet loss is an evaluation of how much the anchor is closer to the positive than to the negative vector, so that learning happens by “moving” the positive and negative points to try to get a better evaluation. However, during discovery, we consider the positive and negative vectors as static points, and we search through the whole dataset for the “anchors”, or result candidates, which fit this characteristic better.

![Triplet loss](https://qdrant.tech/articles_data/discovery-search/triplet-loss.png)

[**Discovery search**](https://qdrant.tech/articles/discovery-search/#discovery-search), then, is made up of two main inputs:

- **target**: the main point of interest
- **context**: the pairs of positive and negative points we just defined.

However, it is not the only way to use it. Alternatively, you can **only** provide a context, which invokes a [**Context Search**](https://qdrant.tech/articles/discovery-search/#context-search). This is useful when you want to explore the space defined by the context, but don’t have a specific target in mind. But hold your horses, we’ll get to that [later ↪](https://qdrant.tech/articles/discovery-search/#context-search).

## [Anchor](https://qdrant.tech/articles/discovery-search/\#real-world-discovery-search-applications) Real-world discovery search applications

Let’s talk about the first case: context with a target.

To understand why this is useful, let’s take a look at a real-world example: using a multimodal encoder like [CLIP](https://openai.com/blog/clip/) to search for images, from text **and** images.
CLIP is a neural network that can embed both images and text into the same vector space. This means that you can search for images using either a text query or an image query. For this example, we’ll reuse our [food recommendations demo](https://food-discovery.qdrant.tech/) by typing “burger” in the text input:

![Burger text input in food demo](https://qdrant.tech/articles_data/discovery-search/search-for-burger.png)

This is basically nearest neighbor search, and while technically we have only images of burgers, one of them is a logo representation of a burger. We’re looking for actual burgers, though. Let’s try to exclude images like that by adding it as a negative example:

![Try to exclude burger drawing](https://qdrant.tech/articles_data/discovery-search/try-to-exclude-non-burger.png)

Wait a second, what has just happened? These pictures have **nothing** to do with burgers, and still, they appear on the first results. Is the demo broken?

Turns out, multimodal encoders [might not work how you expect them to](https://modalitygap.readthedocs.io/en/latest/). Images and text are embedded in the same space, but they are not necessarily close to each other. This means that we can create a mental model of the distribution as two separate planes, one for images and one for text.

![Mental model of CLIP embeddings](https://qdrant.tech/articles_data/discovery-search/clip-mental-model.png)

This is where discovery excels because it allows us to constrain the space considering the same mode (images) while using a target from the other mode (text).

![Cross-modal search with discovery](https://qdrant.tech/articles_data/discovery-search/clip-discovery.png)

Discovery search also lets us keep giving feedback to the search engine in the shape of more context pairs, so we can keep refining our search until we find what we are looking for.

Another intuitive example: imagine you’re looking for a fish pizza, but pizza names can be confusing, so you can just type “pizza”, and prefer a fish over meat. Discovery search will let you use these inputs to suggest a fish pizza… even if it’s not called fish pizza!

![Simple discovery example](https://qdrant.tech/articles_data/discovery-search/discovery-example-with-images.png)

## [Anchor](https://qdrant.tech/articles/discovery-search/\#context-search) Context search

Now, the second case: only providing context.

Ever been caught in the same recommendations on your favorite music streaming service? This may be caused by getting stuck in a similarity bubble. As user input gets more complex, diversity becomes scarce, and it becomes harder to force the system to recommend something different.

![Context vs recommendation search](https://qdrant.tech/articles_data/discovery-search/context-vs-recommendation.png)

**Context search** solves this by de-focusing the search around a single point. Instead, it selects points randomly from within a zone in the vector space. This search is the most influenced by _triplet loss_, as the score can be thought of as _“how much a point is closer to a negative than a positive vector?”_. If it is closer to the positive one, then its score will be zero, same as any other point within the same zone. But if it is on the negative side, it will be assigned a more and more negative score the further it gets.

![Context search visualization](https://qdrant.tech/articles_data/discovery-search/context-search.png)

Creating complex tastes in a high-dimensional space becomes easier since you can just add more context pairs to the search. This way, you should be able to constrain the space enough so you select points from a per-search “category” created just from the context in the input.

![A more complex context search](https://qdrant.tech/articles_data/discovery-search/complex-context-search.png)

This way you can give refreshing recommendations, while still being in control by providing positive and negative feedback, or even by trying out different permutations of pairs.

## [Anchor](https://qdrant.tech/articles/discovery-search/\#key-takeaways) Key takeaways:

- Discovery search is a powerful tool for controlled exploration in vector spaces.
Context, consisting of positive and negative vectors constrain the search space, while a target guides the search.
- Real-world applications include multimodal search, diverse recommendations, and context-driven exploration.
- Ready to learn more about the math behind it and how to use it? Check out the [documentation](https://qdrant.tech/documentation/concepts/explore/#discovery-api)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/discovery-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/discovery-search.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=448e9fd6-6641-4cf5-a70f-0aa24b2103a5&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b41e2944-6171-45c9-aae6-07256f7ea4eb&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdiscovery-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573589971&cv=11&fst=1748573589971&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103158~103103160~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdiscovery-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Discovery%20needs%20context%20-%20Qdrant&npa=0&pscdl=noapi&auid=953215023.1748573590&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573589949&cv=11&fst=1748573589949&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103158~103103160~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdiscovery-search%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Discovery%20needs%20context%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=953215023.1748573590&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=448e9fd6-6641-4cf5-a70f-0aa24b2103a5&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b41e2944-6171-45c9-aae6-07256f7ea4eb&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdiscovery-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573591030&cv=11&fst=1748573591030&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103158~103103160~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdiscovery-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Discovery%20needs%20context%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=953215023.1748573590&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)