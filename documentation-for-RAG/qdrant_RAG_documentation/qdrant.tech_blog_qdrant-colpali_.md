---
url: "https://qdrant.tech/blog/qdrant-colpali/"
title: "Advanced Retrieval with ColPali & Qdrant Vector Database - Qdrant"
---

0

# Advanced Retrieval with ColPali & Qdrant Vector Database

Sabrina Aquino

·

November 05, 2024

![Advanced Retrieval with ColPali & Qdrant Vector Database](https://qdrant.tech/blog/qdrant-colpali/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-colpali%2F&text=Advanced%20Retrieval%20with%20ColPali%20&%20Qdrant%20Vector%20Database "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-colpali%2F "LinkedIn")

| Time: 30 min | Level: Advanced | Notebook: [GitHub](https://github.com/qdrant/examples/blob/master/colpali-and-binary-quantization/colpali_demo_binary.ipynb) |
| --- | --- | --- |

It’s no secret that even the most modern document retrieval systems have a hard time handling visually rich documents like **PDFs, containing tables, images, and complex layouts.**

ColPali introduces a multimodal retrieval approach that uses **Vision Language Models (VLMs)** instead of the traditional OCR and text-based extraction.

By processing document images directly, it creates **multi-vector embeddings** from both the visual and textual content, capturing the document’s structure and context more effectively. This method outperforms traditional techniques, as demonstrated by the [**Visual Document Retrieval Benchmark (ViDoRe)**](https://huggingface.co/vidore).

**Before we go any deeper, watch our short video:**

Optimizing Document Retrieval with ColPali and Qdrant's Binary Quantization - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Optimizing Document Retrieval with ColPali and Qdrant's Binary Quantization](https://www.youtube.com/watch?v=_A90A-grwIc)

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

[Watch on](https://www.youtube.com/watch?v=_A90A-grwIc&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 8:47
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=_A90A-grwIc "Watch on YouTube")

## [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#standard-retrieval-vs-colpali) Standard Retrieval vs ColPali

The standard approach starts by running **Optical Character Recognition (OCR)** to extract the text from a document. Once the text is extracted, a layout detection model interprets the structure, which is followed by chunking the text into smaller sections for embedding. This method works adequately for documents where the text content is the primary focus.

Imagine you have a PDF packed with complex layouts, tables, and images, and you need to extract meaningful information efficiently. Traditionally, this would involve several steps:

1. **Text Extraction:** Using OCR to pull words from each page.
2. **Layout Detection:** Identifying page elements like tables, paragraphs, and titles.
3. **Chunking:** Experimenting with methods to determine the best fit for your use case.
4. **Embedding Creation:** Finally generating and storing the embeddings.

### [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#why-is-colpali-better) Why is ColPali Better?

This entire process can require too many steps, especially for complex documents, with each page often taking over seven seconds to process. For text-heavy documents, this approach might suffice, but real-world data is often rich and complex, making traditional extraction methods less effective.

This is where ColPali comes into play. **ColPali, or Contextualized Late Interaction Over PaliGemma**, uses a vision language model (VLM) to simplify and enhance the document retrieval process.

Instead of relying on text-only methods, ColPali generates contextualized **multivector embeddings** directly from an image of a document page. The VLM considers visual elements, structure, and text all at once, creating a holistic representation of each page.

## [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#how-colpali-works-under-the-hood) How ColPali Works Under the Hood

![Qdrant and Colpali](https://qdrant.tech/blog/qdrant-colpali/qdrant-colpali-1.png)

Rather than relying on OCR, ColPali **processes the entire document as an image** using a Vision Encoder. It creates multi-vector embeddings that capture both the textual content and the visual structure of the document which are then passed through a Large Language Model (LLM), which integrates the information into a representation that retains both text and visual features.

Here’s a step-by-step look at the ColPali architecture and how it enhances document retrieval:

1. **Image Preprocessing:** The input image is divided into a 32x32 grid, resulting in 1,024 patches.
2. **Contextual Transformation:** Each patch undergoes transformations to capture local and global context and is represented by a 128-dimensional vector.
3. **Query Processing:** When a text query is sent, ColPali generates token-level embeddings for the query, comparing it with document patches using a similarity matrix (specifically MaxSim).
4. **MaxSim Similarity:** This similarity matrix computes similarities for each query token in every document patch, selecting maximum similarities to efficiently retrieve relevant pages. This late interaction approach helps ColPali capture intricate context across a document’s structure and text.

> ColPali’s late interaction strategy is inspired by ColBERT and improves search by analyzing layout and textual content in a single pass.

## [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#optimizing-with-binary-quantization) Optimizing with Binary Quantization

![Qdrant and Colpali](https://qdrant.tech/blog/qdrant-colpali/qdrant-colpali-3.png)

Binary Quantization further enhances the ColPali pipeline by **reducing storage and computational load** without compromising search performance. Binary Quantization, unlike Scalar Quantization, compresses vectors more aggressively, which can speed up search times and reduce memory usage.

In an experiment based on a [**blog post by Daniel Van Strien**](https://danielvanstrien.xyz/posts/post-with-code/colpali-qdrant/2024-10-02_using_colpali_with_qdrant.html), where ColPali and Qdrant were used to search a UFO document dataset, the results were compelling. By using Binary Quantization along with rescoring and oversampling techniques, we saw search time reduced by nearly half compared to Scalar Quantization, while maintaining similar accuracy.

## [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#using-colpali-with-qdrant) Using ColPali with Qdrant

**Now it’s time to try the code.**

Here’s a simplified Notebook to test ColPali for yourself:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sabrinaaquino/colpali-qdrant-demo/blob/main/colpali_demo_binary.ipynb)

Our goal is to go through a dataset of multilingual newspaper articles like the ones below. We will detect which images contain text about **UFO’s** and **Top Secret** events.

![Qdrant and Colpali](https://qdrant.tech/blog/qdrant-colpali/qdrant-colpali-4.png)

_The full dataset is accessible from the notebook._

### [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#procedure) Procedure

1. **Setup ColPali and Qdrant:** Import the necessary libraries, including a fine-tuned model optimized for your dataset (in this case, a UFO document set).
2. **Dataset Preparation:** Load your document images into ColPali, previewing complex images to appreciate the challenge for traditional retrieval methods.
3. **Qdrant Configuration:** Define your Qdrant collection, setting vector dimensions to 128. Enable Binary Quantization to optimize memory usage.
4. **Batch Uploading Vectors:** Use a retry checkpoint to handle any exceptions during indexing. Batch processing allows you to adjust batch size based on available GPU resources.
5. **Query Processing and Search:** Encode queries as multivectors for Qdrant. Set up rescoring and oversampling to fine-tune accuracy while optimizing speed.

### [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#results) Results

> Success! Tests shows that search time is 2x faster than with Scalar Quantization.

This is significantly faster than with Scalar Quantization, and we still retrieved the top document matches with remarkable accuracy.

However, keep in mind that this is just a quick experiment. Performance may vary, so it’s important to test Binary Quantization on your own datasets to see how it performs for your specific use case.

That said, it’s promising to see Binary Quantization maintaining search quality while potentially offering performance improvements with ColPali.

## [Anchor](https://qdrant.tech/blog/qdrant-colpali/\#future-directions-with-colpali) Future Directions with ColPali

![Qdrant and Colpali](https://qdrant.tech/blog/qdrant-colpali/qdrant-colpali-2.png)

ColPali offers a promising, streamlined approach to document retrieval, especially for visually rich, complex documents. Its integration with Qdrant enables efficient large-scale vector storage and retrieval, ideal for machine learning applications requiring sophisticated document understanding.

If you’re interested in trying ColPali on your own datasets, join our [**vector search community on Discord**](https://qdrant.to/discord) for discussions, tutorials, and more insights into advanced document retrieval methods. Let us know in how you’re using ColPali or what applications you envision for it!

Thank you for reading, and stay tuned for more insights on vector search!

**References:**

\[1\] Faysse, M., Sibille, H., Wu, T., Omrani, B., Viaud, G., Hudelot, C., Colombo, P. (2024). **ColPali: Efficient Document Retrieval with Vision Language Models.** arXiv. [https://doi.org/10.48550/arXiv.2407.01449](https://doi.org/10.48550/arXiv.2407.01449)

\[2\] van Strien, D. (2024). **Using ColPali with Qdrant to index and search a UFO document dataset.** Published October 2, 2024. Blog post: [https://danielvanstrien.xyz/posts/post-with-code/colpali-qdrant/2024-10-02\_using\_colpali\_with\_qdrant.html](https://danielvanstrien.xyz/posts/post-with-code/colpali-qdrant/2024-10-02_using_colpali_with_qdrant.html)

\[3\] Kacper Łukawski (2024). **Any Embedding Model Can Become a Late Interaction Model… If You Give It a Chance!** Qdrant Blog, August 14, 2024. Available at: [https://qdrant.tech/articles/late-interaction-models/](https://qdrant.tech/articles/late-interaction-models/)

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=7b9cd352-a790-4578-8283-825e7c2b5bb6)

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

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-colpali%2F&portalId=139603372&pageTitle=Advanced+Retrieval+with+ColPali+%26+Qdrant+Vector+Database+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=bc5c0b7ef9487d5a30eabda1ce1d663a&hssc=265983056.1.1748575244882&hstc=265983056.bc5c0b7ef9487d5a30eabda1ce1d663a.1748575244882.1748575244882.1748575244882.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-colpali%2F&pageTitle=Advanced+Retrieval+with+ColPali+%26+Qdrant+Vector+Database+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=bc5c0b7ef9487d5a30eabda1ce1d663a&hssc=265983056.1.1748575244882&hstc=265983056.bc5c0b7ef9487d5a30eabda1ce1d663a.1748575244882.1748575244882.1748575244882.1&hsfp=3707738794).

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=28cf5860-f1bd-4a30-8872-8005a5e48a31&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=44394fbc-a882-44ae-8c8c-c20cf6d530ed&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-colpali%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=28cf5860-f1bd-4a30-8872-8005a5e48a31&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=44394fbc-a882-44ae-8c8c-c20cf6d530ed&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-colpali%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)