---
url: "https://qdrant.tech/articles/dataset-quality/"
title: "Finding errors in datasets with Similarity Search - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Finding errors in datasets with Similarity Search

[Back to Data Exploration](https://qdrant.tech/articles/data-exploration/)

# Finding errors in datasets with Similarity Search

George Panchuk

·

July 18, 2022

![Finding errors in datasets with Similarity Search](https://qdrant.tech/articles_data/dataset-quality/preview/title.jpg)

Nowadays, people create a huge number of applications of various types and solve problems in different areas.
Despite such diversity, they have something in common - they need to process data.
Real-world data is a living structure, it grows day by day, changes a lot and becomes harder to work with.

In some cases, you need to categorize or label your data, which can be a tough problem given its scale.
The process of splitting or labelling is error-prone and these errors can be very costly.
Imagine that you failed to achieve the desired quality of the model due to inaccurate labels.
Worse, your users are faced with a lot of irrelevant items, unable to find what they need and getting annoyed by it.
Thus, you get poor retention, and it directly impacts company revenue.
It is really important to avoid such errors in your data.

## [Anchor](https://qdrant.tech/articles/dataset-quality/\#furniture-web-marketplace) Furniture web-marketplace

Let’s say you work on an online furniture marketplace.

![Furniture marketplace](https://storage.googleapis.com/demo-dataset-quality-public/article/furniture_marketplace.png)

Furniture marketplace

In this case, to ensure a good user experience, you need to split items into different categories: tables, chairs, beds, etc.
One can arrange all the items manually and spend a lot of money and time on this.
There is also another way: train a classification or similarity model and rely on it.
With both approaches it is difficult to avoid mistakes.
Manual labelling is a tedious task, but it requires concentration.
Once you got distracted or your eyes became blurred mistakes won’t keep you waiting.
The model also can be wrong.
You can analyse the most uncertain predictions and fix them, but the other errors will still leak to the site.
There is no silver bullet. You should validate your dataset thoroughly, and you need tools for this.

When you are sure that there are not many objects placed in the wrong category, they can be considered outliers or anomalies.
Thus, you can train a model or a bunch of models capable of looking for anomalies, e.g. autoencoder and a classifier on it.
However, this is again a resource-intensive task, both in terms of time and manual labour, since labels have to be provided for classification.
On the contrary, if the proportion of out-of-place elements is high enough, outlier search methods are likely to be useless.

### [Anchor](https://qdrant.tech/articles/dataset-quality/\#similarity-search) Similarity search

The idea behind similarity search is to measure semantic similarity between related parts of the data.
E.g. between category title and item images.
The hypothesis is, that unsuitable items will be less similar.

We can’t directly compare text and image data.
For this we need an intermediate representation - embeddings.
Embeddings are just numeric vectors containing semantic information.
We can apply a pre-trained model to our data to produce these vectors.
After embeddings are created, we can measure the distances between them.

Assume we want to search for something other than a single bed in «Single beds» category.

![Similarity search](https://storage.googleapis.com/demo-dataset-quality-public/article/similarity_search.png)

Similarity search

One of the possible pipelines would look like this:

- Take the name of the category as an anchor and calculate the anchor embedding.
- Calculate embeddings for images of each object placed into this category.
- Compare obtained anchor and object embeddings.
- Find the furthest.

For instance, we can do it with the [CLIP](https://huggingface.co/sentence-transformers/clip-ViT-B-32-multilingual-v1) model.

![Category vs. Image](https://storage.googleapis.com/demo-dataset-quality-public/article/category_vs_image_transparent.png)

Category vs. Image

We can also calculate embeddings for titles instead of images, or even for both of them to find more errors.

![Category vs. Title and Image](https://storage.googleapis.com/demo-dataset-quality-public/article/category_vs_name_and_image_transparent.png)

Category vs. Title and Image

As you can see, different approaches can find new errors or the same ones.
Stacking several techniques or even the same techniques with different models may provide better coverage.
Hint: Caching embeddings for the same models and reusing them among different methods can significantly speed up your lookup.

### [Anchor](https://qdrant.tech/articles/dataset-quality/\#diversity-search) Diversity search

Since pre-trained models have only general knowledge about the data, they can still leave some misplaced items undetected.
You might find yourself in a situation when the model focuses on non-important features, selects a lot of irrelevant elements, and fails to find genuine errors.
To mitigate this issue, you can perform a diversity search.

Diversity search is a method for finding the most distinctive examples in the data.
As similarity search, it also operates on embeddings and measures the distances between them.
The difference lies in deciding which point should be extracted next.

Let’s imagine how to get 3 points with similarity search and then with diversity search.

Similarity:

1. Calculate distance matrix
2. Choose your anchor
3. Get a vector corresponding to the distances from the selected anchor from the distance matrix
4. Sort fetched vector
5. Get top-3 embeddings

Diversity:

1. Calculate distance matrix
2. Initialize starting point (randomly or according to the certain conditions)
3. Get a distance vector for the selected starting point from the distance matrix
4. Find the furthest point
5. Get a distance vector for the new point
6. Find the furthest point from all of already fetched points

![Diversity search](https://storage.googleapis.com/demo-dataset-quality-public/article/diversity_transparent.png)

Diversity search

Diversity search utilizes the very same embeddings, and you can reuse them.
If your data is huge and does not fit into memory, vector search engines like [Qdrant](https://github.com/qdrant/qdrant) might be helpful.

Although the described methods can be used independently. But they are simple to combine and improve detection capabilities.
If the quality remains insufficient, you can fine-tune the models using a similarity learning approach (e.g. with [Quaterion](https://quaterion.qdrant.tech/) both to provide a better representation of your data and pull apart dissimilar objects in space.

## [Anchor](https://qdrant.tech/articles/dataset-quality/\#conclusion) Conclusion

In this article, we enlightened distance-based methods to find errors in categorized datasets.
Showed how to find incorrectly placed items in the furniture web store.
I hope these methods will help you catch sneaky samples leaked into the wrong categories in your data, and make your users\` experience more enjoyable.

Poke the [demo](https://dataset-quality.qdrant.tech/).

Stay tuned :)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/dataset-quality.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/dataset-quality.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574484795&cv=11&fst=1748574484795&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdataset-quality%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Finding%20errors%20in%20datasets%20with%20Similarity%20Search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=199274105.1748574485&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574484873&cv=11&fst=1748574484873&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdataset-quality%2F&hn=www.googleadservices.com&frm=0&tiba=Finding%20errors%20in%20datasets%20with%20Similarity%20Search%20-%20Qdrant&npa=0&pscdl=noapi&auid=199274105.1748574485&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4bf02929-5990-4cfc-85e2-480863c0cfee&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0d430bec-b605-4607-b685-9af189be4546&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdataset-quality%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4bf02929-5990-4cfc-85e2-480863c0cfee&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0d430bec-b605-4607-b685-9af189be4546&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdataset-quality%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574485873&cv=11&fst=1748574485873&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdataset-quality%2F&hn=www.googleadservices.com&frm=0&tiba=Finding%20errors%20in%20datasets%20with%20Similarity%20Search%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=199274105.1748574485&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)