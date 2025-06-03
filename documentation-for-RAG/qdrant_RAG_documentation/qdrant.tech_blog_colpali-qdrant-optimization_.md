---
url: "https://qdrant.tech/blog/colpali-qdrant-optimization/"
title: "Optimizing ColPali for Retrieval at Scale, 13x Faster Results - Qdrant"
---

0

# Optimizing ColPali for Retrieval at Scale, 13x Faster Results

Evgeniya Sukhodolskaya, Sabrina Aquino

·

November 27, 2024

![Optimizing ColPali for Retrieval at Scale, 13x Faster Results](https://qdrant.tech/blog/colpali-qdrant-optimization/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcolpali-qdrant-optimization%2F&text=Optimizing%20ColPali%20for%20Retrieval%20at%20Scale,%2013x%20Faster%20Results "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcolpali-qdrant-optimization%2F "LinkedIn")

ColPali is a fascinating leap in document retrieval. Its precision in handling visually rich PDFs is phenomenal, but scaling it to handle real-world datasets comes with its share of computational challenges.

Here’s how we solved these challenges to make ColPali 13x faster without sacrificing the precision it’s known for.

## [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#the-scaling-dilemma) The Scaling Dilemma

ColPali generates **1,030 vectors for just one page of a PDF.** While this is manageable for small-scale tasks, in a real-world production setting where you may need to store hundreds od thousands of PDFs, the challenge of scaling becomes significant.

Consider this scenario:

- **Dataset Size:** 20,000 PDF pages.
- **Number of Vectors:** Each page generates ~1,000 vectors of 128 dimensions.

The total number of comparisons is calculated as:

1,000⋅1,000⋅20,000⋅128=2.56×1012 comparisons!

That’s trillions of comparisons needed to build the index. Even advanced indexing algorithms like **HNSW** struggle with this scale, as computational costs grow quadratically with amount of multivectors per page.

We turned to a hybrid optimization strategy combining **pooling** (to reduce computational overhead) and **reranking** (to preserve accuracy).

Before we go any deeper, watch our [Webinar video](https://www.youtube.com/live/_h6SN1WwnLs?si=n8gwiIjJ5dnfucXC) for the full demo walkthrough.

Optimizing ColPali for Retrieval at Scale, from Theory to Practice - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Optimizing ColPali for Retrieval at Scale, from Theory to Practice](https://www.youtube.com/watch?v=_h6SN1WwnLs)

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

[Watch on](https://www.youtube.com/watch?t=922&v=_h6SN1WwnLs&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

15:22

15:22 / 1:00:58
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=_h6SN1WwnLs "Watch on YouTube")

For those eager to explore, the [codebase is available here](https://github.com/qdrant/demo-colpali-optimized).

## [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#two-stage-retrieval-process) Two-Stage Retrieval Process

### [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#pooling) Pooling

Pooling is well-known in machine learning as a way to compress data while keeping important information. For ColPali, we reduced 1,030 vectors per page to just 38 vectors by pooling rows in the document’s 32x32 grid.

![](https://qdrant.tech/blog/colpali-optimization/rows.png)

Max and mean pooling are the two most popular types, so we decided to test both approaches on the rows of the grid. Likewise, we could apply pooling on columns, which we plan to explore in the future.

- **Mean Pooling:** Averages values across rows.
- **Max Pooling:** Selects the maximum value for each feature.

32 vectors represent the pooled rows, while 6 vectors encode contextual information derived from ColPali’s special tokens (e.g., for the beginning of the sequence, and task-specific instructions like “Describe the image”).

For our experiments, we chose to preserve these 6 additional vectors.

### [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#the-colpali-as-a-reranker-experiment) The “ColPali as a Reranker” Experiment

Pooling drastically reduces retrieval costs, but there’s a risk of losing fine-grained precision. To address this, we implemented a **two-stage retrieval system**, where embeddings generated with ColPali were max/mean pooled by grid rows to create lightweight vectors for the initial retrieval stage, followed by reranking with the original high-resolution embeddings:

1. **Pooled Retrieval:** Quickly retrieves the top 200 candidates using lightweight pooled embeddings.
2. **Full Reranking:** Refines these candidates using the original, high-resolution embeddings, delivering the final top 20 results.

### [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#implementation) Implementation

We created a custom dataset with over 20,000 unique PDF pages by merging:

- **ViDoRe Benchmark:** Designed for PDF documents retrieval evaluation.
- **UFO Dataset:** Visually rich documents paired with synthetic queries [generated by Daniel van Strien](https://huggingface.co/datasets/davanstrien/ufo-ColPali).
- **DocVQA Dataset:** A large set of document-derived Q&A pairs.

Each document was processed into 32x32 grids, generating both full-resolution and pooled embeddings. **Full-resolution** embeddings consisted of 1,030 vectors per page, while **pooled embeddings** included mean and max pooling variants.

All embeddings were were stored and kept in RAM to avoid caching effects during retrieval speed experiments.

### [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#experiment-setup) Experiment Setup

We evaluated retrieval quality with 1,000 queries. First, pooled embeddings retrieved the top 200 candidates. Then, full-resolution embeddings reranked them to produce the final top 20 results.

To measure performance, we used:

- **NDCG@20:** Measures ranking quality (how well the top results align with expectations).
- **Recall@20:** Measures the overlap between this method and the original ColPali retrieval.

## [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#results) Results

The experiment showed promising improvements in speed and accuracy. Retrieval time improved **13x** compared to using full-resolution embeddings alone.

### [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#metrics) Metrics

| Pooling Type | NDCG@20 | Recall@20 |
| --- | --- | --- |
| **Mean** | 0.952 | 0.917 |
| **Max** | 0.759 | 0.656 |

Mean pooling preserved nearly identical quality to the original ColPali, with NDCG@20 = 0.952 and Recall@20 = 0.917. Max pooling did not perform well enough to be considered viable since it sacrificed significant accuracy without delivering a meaningful speed advantage.

## [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#whats-next) What’s Next?

Future experiments could push these results even further:

- Investigating column-wise pooling for additional compression.
- Testing half-precision (float16) vectors to balance memory use and speed.
- Skipping special multivectors during prefetch to streamline retrieval.
- Combining quantization with oversampling for even faster search.

### [Anchor](https://qdrant.tech/blog/colpali-qdrant-optimization/\#try-it-yourself) Try It Yourself

Curious to see this in action? Explore the full codebase and experiment with ColPali optimizations:

- **Demo Notebook:** [GitHub Repository](https://github.com/qdrant/demo-colpali-optimized)
- **Webinar Walkthrough:** [Watch Here](https://www.youtube.com/live/_h6SN1WwnLs?si=n8gwiIjJ5dnfucXC)

[Join the community](https://discord.com/invite/qdrant) and share your results!

* * *

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=8bc6fa33-1fb5-46db-85da-90d8e4c8f9a7)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d2d27209-778a-4e41-a0b1-01c3951f43f3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1217f327-2aa5-4bee-bca6-1aa29c4eaafc&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcolpali-qdrant-optimization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d2d27209-778a-4e41-a0b1-01c3951f43f3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1217f327-2aa5-4bee-bca6-1aa29c4eaafc&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcolpali-qdrant-optimization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcolpali-qdrant-optimization%2F&portalId=139603372&pageTitle=Optimizing+ColPali+for+Retrieval+at+Scale%2C+13x+Faster+Results+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=126e450eb62717a83229c569cf699bea&hssc=265983056.1.1748575406657&hstc=265983056.126e450eb62717a83229c569cf699bea.1748575406657.1748575406657.1748575406657.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcolpali-qdrant-optimization%2F&pageTitle=Optimizing+ColPali+for+Retrieval+at+Scale%2C+13x+Faster+Results+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=126e450eb62717a83229c569cf699bea&hssc=265983056.1.1748575406657&hstc=265983056.126e450eb62717a83229c569cf699bea.1748575406657.1748575406657.1748575406657.1&hsfp=3707738794).