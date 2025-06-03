---
url: "https://qdrant.tech/articles/cross-encoder-integration-gsoc/"
title: "Qdrant Summer of Code 2024 - ONNX Cross Encoders in Python - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Qdrant Summer of Code 2024 - ONNX Cross Encoders in Python

[Back to Machine Learning](https://qdrant.tech/articles/machine-learning/)

# Qdrant Summer of Code 2024 - ONNX Cross Encoders in Python

Huong (Celine) Hoang

·

October 14, 2024

![Qdrant Summer of Code 2024 - ONNX Cross Encoders in Python](https://qdrant.tech/articles_data/cross-encoder-integration-gsoc/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#introduction) Introduction

Hi everyone! I’m Huong (Celine) Hoang, and I’m thrilled to share my experience working at Qdrant this summer as part of their Summer of Code 2024 program. During my internship, I worked on integrating cross-encoders into the FastEmbed library for re-ranking tasks. This enhancement widened the capabilities of the Qdrant ecosystem, enabling developers to build more context-aware search applications, such as question-answering systems, using Qdrant’s suite of libraries.

This project was both technically challenging and rewarding, pushing me to grow my skills in handling large-scale ONNX (Open Neural Network Exchange) model integrations, tokenization, and more. Let me take you through the journey, the lessons learned, and where things are headed next.

## [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#project-overview) Project Overview

Qdrant is well known for its vector search capabilities, but my task was to go one step further — introducing cross-encoders for re-ranking. Traditionally, the FastEmbed library would generate embeddings, but cross-encoders don’t do that. Instead, they provide a list of scores based on how well a query matches a list of documents. This kind of re-ranking is critical when you want to refine search results and bring the most relevant answers to the top.

The project revolved around creating a new input-output scheme: text data to scores. For this, I designed a family of classes to support ONNX models. Some of the key models I worked with included Xenova/ms-marco-MiniLM-L-6-v2, Xenova/ms-marco-MiniLM-L-12-v2, and BAAI/bge-reranker, all designed for re-ranking tasks.

An important point to mention is that FastEmbed is a minimalistic library: it doesn’t have heavy dependencies like PyTorch or TensorFlow, and as a result, it is lightweight, occupying far less storage space.

Below is a diagram that represents the overall workflow for this project, detailing the key steps from user interaction to the final output validation:

![Search workflow with reranking](https://qdrant.tech/articles_data/cross-encoder-integration-gsoc/rerank-workflow.png)

Search workflow with reranking

## [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#technical-challenges) Technical Challenges

### [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#1-building-a-new-input-output-scheme) 1\. Building a New Input-Output Scheme

FastEmbed already had support for embeddings, but re-ranking with cross-encoders meant building a completely new family of classes. These models accept a query and a set of documents, then return a list of relevance scores. For that, I created the base classes like `TextCrossEncoderBase` and `OnnxCrossEncoder`, taking inspiration from existing text embedding models.

One thing I had to ensure was that the new class hierarchy was user-friendly. Users should be able to work with cross-encoders without needing to know the complexities of the underlying models. For instance, they should be able to just write:

```python
from fastembed.rerank.cross_encoder import TextCrossEncoder

encoder = TextCrossEncoder(model_name="Xenova/ms-marco-MiniLM-L-6-v2")
scores = encoder.rerank(query, documents)

```

Meanwhile, behind the scenes, we manage all the model loading, tokenization, and scoring.

### [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#2-handling-tokenization-for-cross-encoders) 2\. Handling Tokenization for Cross-Encoders

Cross-encoders require careful tokenization because they need to distinguish between the query and the documents. This is done using token type IDs, which help the model differentiate between the two. To implement this, I configured the tokenizer to handle pairs of inputs—concatenating the query with each document and assigning token types accordingly.

Efficient tokenization is critical to ensure the performance of the models, and I optimized it specifically for ONNX models.

### [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#3-model-loading-and-integration) 3\. Model Loading and Integration

One of the most rewarding parts of the project was integrating the ONNX models into the FastEmbed library. ONNX models need to be loaded into a runtime environment that efficiently manages the computations.

While PyTorch is a common framework for these types of tasks, FastEmbed exclusively supports ONNX models, making it both lightweight and efficient. I focused on extensive testing to ensure that the ONNX models performed equivalently to their PyTorch counterparts, ensuring users could trust the results.

I added support for batching as well, allowing users to re-rank large sets of documents without compromising speed.

### [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#4-debugging-and-code-reviews) 4\. Debugging and Code Reviews

During the project, I encountered a number of challenges, including issues with model configurations, tokenizers, and test cases. With the help of my mentor, George Panchuk, I was able to resolve these issues and improve my understanding of best practices, particularly around code readability, maintainability, and style.

One notable lesson was the importance of keeping the code organized and maintainable, with a strong focus on readability. This included properly structuring modules and ensuring the entire codebase followed a clear, consistent style.

### [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#5-testing-and-validation) 5\. Testing and Validation

To ensure the accuracy and performance of the models, I conducted extensive testing. I compared the output of ONNX models with their PyTorch counterparts, ensuring the conversion to ONNX was correct. A key part of this process was rigorous testing to verify the outputs and identify potential issues, such as incorrect conversions or bugs in our implementation.

For instance, a test to validate the model’s output was structured as follows:

```python
def test_rerank():
    is_ci = os.getenv("CI")

    for model_desc in TextCrossEncoder.list_supported_models():
        if not is_ci and model_desc["size_in_GB"] > 1:
            continue

        model_name = model_desc["model"]
        model = TextCrossEncoder(model_name=model_name)

        query = "What is the capital of France?"
        documents = ["Paris is the capital of France.", "Berlin is the capital of Germany."]
        scores = np.array(model.rerank(query, documents))

        canonical_scores = CANONICAL_SCORE_VALUES[model_name]
        assert np.allclose(
            scores, canonical_scores, atol=1e-3
        ), f"Model: {model_name}, Scores: {scores}, Expected: {canonical_scores}"

```

The `CANONICAL_SCORE_VALUES` were retrieved directly from the result of applying the original PyTorch models to the same input

## [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#outcomes-and-future-improvements) Outcomes and Future Improvements

By the end of my project, I successfully added cross-encoders to the FastEmbed library, allowing users to re-rank search results based on relevance scores. This enhancement opens up new possibilities for applications that rely on contextual ranking, such as search engines and recommendation systems.
This functionality will be available as of FastEmbed `0.4.0`.

Some areas for future improvements include:

- Expanding Model Support: We could add more cross-encoder models, especially from the sentence transformers library, to give users more options.
- Parallelization: Optimizing batch processing to handle even larger datasets could further improve performance.
- Custom Tokenization: For models with non-standard tokenization, like BAAI/bge-reranker, more specific tokenizer configurations could be added.

## [Anchor](https://qdrant.tech/articles/cross-encoder-integration-gsoc/\#overall-experience-and-wrapping-up) Overall Experience and Wrapping Up

Looking back, this internship has been an incredibly valuable experience. I’ve grown not only as a developer but also as someone who can take on complex projects and see them through from start to finish. The Qdrant team has been so supportive, especially during the debugging and review stages. I’ve learned so much about model integration, ONNX, and how to build tools that are user-friendly and scalable.

One key takeaway for me is the importance of understanding the user experience. It’s not just about getting the models to work but making sure they are easy to use and integrate into real-world applications. This experience has solidified my passion for building solutions that truly make an impact, and I’m excited to continue working on projects like this in the future.

Thank you for taking the time to read about my journey with Qdrant and the FastEmbed library. I’m excited to see how this work will continue to improve search experiences for users!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/cross-encoder-integration-gsoc.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/cross-encoder-integration-gsoc.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573849305&cv=11&fst=1748573849305&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fcross-encoder-integration-gsoc%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%202024%20-%20ONNX%20Cross%20Encoders%20in%20Python%20-%20Qdrant&npa=0&pscdl=noapi&auid=283265990.1748573849&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573849288&cv=11&fst=1748573849288&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fcross-encoder-integration-gsoc%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%202024%20-%20ONNX%20Cross%20Encoders%20in%20Python%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=283265990.1748573849&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d72cb7bb-5f1c-4bf0-b911-c8cb82e34b83&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b560856f-99f0-44ca-baab-16f6cebe8d37&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fcross-encoder-integration-gsoc%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d72cb7bb-5f1c-4bf0-b911-c8cb82e34b83&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b560856f-99f0-44ca-baab-16f6cebe8d37&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fcross-encoder-integration-gsoc%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)