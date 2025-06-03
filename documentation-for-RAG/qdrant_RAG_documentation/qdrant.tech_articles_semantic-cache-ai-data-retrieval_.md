---
url: "https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/"
title: "Semantic Cache: Accelerating AI with Lightning-Fast Data Retrieval - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Semantic Cache: Accelerating AI with Lightning-Fast Data Retrieval

[Back to RAG & GenAI](https://qdrant.tech/articles/rag-and-genai/)

# Semantic Cache: Accelerating AI with Lightning-Fast Data Retrieval

Daniel Romero, David Myriel

·

May 07, 2024

![Semantic Cache: Accelerating AI with Lightning-Fast Data Retrieval](https://qdrant.tech/articles_data/semantic-cache-ai-data-retrieval/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/\#what-is-semantic-cache) What is Semantic Cache?

**Semantic cache** is a method of retrieval optimization, where similar queries instantly retrieve the same appropriate response from a knowledge base.

Semantic cache differs from traditional caching methods. In computing, **cache** refers to high-speed memory that efficiently stores frequently accessed data. In the context of [vector databases](https://qdrant.tech/articles/what-is-a-vector-database/), a **semantic cache** improves AI application performance by storing previously retrieved results along with the conditions under which they were computed. This allows the application to reuse those results when the same or similar conditions occur again, rather than finding them from scratch.

> The term **“semantic”** implies that the cache takes into account the meaning or semantics of the data or computation being cached, rather than just its syntactic representation. This can lead to more efficient caching strategies that exploit the structure or relationships within the data or computation.

![semantic-cache-question](https://qdrant.tech/articles_data/semantic-cache-ai-data-retrieval/semantic-cache-question.png)

Traditional caches operate on an exact match basis, while semantic caches search for the meaning of the key rather than an exact match. For example, **“What is the capital of Brazil?”** and **“Can you tell me the capital of Brazil?”** are semantically equivalent, but not exact matches. A semantic cache recognizes such semantic equivalence and provides the correct result.

In this blog and video, we will walk you through how to use Qdrant to implement a basic semantic cache system. You can also try the [notebook example](https://github.com/infoslack/qdrant-example/blob/main/semantic-cache.ipynb) for this implementation.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/infoslack/qdrant-example/blob/main/semantic-cache.ipynb)

## [Anchor](https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/\#semantic-cache-in-rag-the-key-value-mechanism) Semantic Cache in RAG: the Key-Value Mechanism

Semantic cache is increasingly used in Retrieval-Augmented Generation (RAG) applications. In RAG, when a user asks a question, we embed it and search our vector database, either by using keyword, semantic, or hybrid search methods. The matched context is then passed to a Language Model (LLM) along with the prompt and user question for response generation.

Qdrant is recommended for setting up semantic cache as semantically [evaluates](https://qdrant.tech/rag/rag-evaluation-guide/) the response. When semantic cache is implemented, we store common questions and their corresponding answers in a key-value cache. This way, when a user asks a question, we can retrieve the response from the cache if it already exists.

**Diagram:** Semantic cache improves [RAG](https://qdrant.tech/rag/rag-evaluation-guide/) by directly retrieving stored answers to the user. **Follow along with the gif** and see how semantic cache stores and retrieves answers.

![Alt Text](https://qdrant.tech/articles_data/semantic-cache-ai-data-retrieval/semantic-cache.gif)

When using a key-value cache, it’s important to consider that slight variations in question wording can lead to different hash values. The two questions convey the same query but differ in wording. A naive cache search might fail due to distinct hashed versions of the questions. Implementing a more nuanced approach is necessary to accommodate phrasing variations and ensure accurate responses.

To address this challenge, a semantic cache can be employed instead of relying solely on exact matches. This entails storing questions, answers, and their embeddings in a key-value structure.

When a user poses a question, a semantic search by Qdrant is conducted across all cached questions to identify the most similar one. If the similarity score surpasses a predefined threshold, the system assumes equivalence between the user’s question and the matched one, providing the corresponding answer accordingly.

## [Anchor](https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/\#benefits-of-semantic-cache-for-ai-applications) Benefits of Semantic Cache for AI Applications

Semantic cache contributes to scalability in AI applications by making it simpler to retrieve common queries from vast datasets. The retrieval process can be computationally intensive and implementing a cache component can reduce the load.

For instance, if hundreds of users repeat the same question, the system can retrieve the precomputed answer from the cache rather than re-executing the entire process. This cache stores questions as keys and their corresponding answers as values, providing an efficient means to handle repeated queries.

> There are **potential cost savings** associated with utilizing semantic cache. Using a semantic cache eliminates the need for repeated searches and generation processes for similar or duplicate questions, thus saving time and LLM API resources, especially when employing costly language model calls like OpenAI’s.

## [Anchor](https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/\#when-to-use-semantic-cache) When to Use Semantic Cache?

For applications like question-answering systems where facts are retrieved from documents, caching is beneficial due to the consistent nature of the queries. _However, for text generation tasks requiring varied responses, caching may not be ideal as it returns previous responses, potentially limiting variation._ Thus, the decision to use caching depends on the specific use case.

Using a cache might not be ideal for applications where diverse responses are desired across multiple queries. However, in question-answering systems, caching is advantageous since variations are insignificant. It serves as an effective performance optimization tool for chatbots by storing frequently accessed data.

One strategy involves creating ad-hoc patches for chatbot dialogues, where commonly asked questions are pre-mapped to prepared responses in the cache. This allows the chatbot to swiftly retrieve and deliver responses without relying on a Language Model (LLM) for each query.

## [Anchor](https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/\#implement-semantic-cache-a-step-by-step-guide) Implement Semantic Cache: A Step-by-Step Guide

The first part of this video explains how caching works. In the second part, you can follow along with the code with our [notebook example](https://github.com/infoslack/qdrant-example/blob/main/semantic-cache.ipynb).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/infoslack/qdrant-example/blob/main/semantic-cache.ipynb)

Optimize RAG Resource Use With Semantic Cache - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Optimize RAG Resource Use With Semantic Cache](https://www.youtube.com/watch?v=H53L_yHs9jE)

Qdrant - Vector Database & Search Engine

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=H53L_yHs9jE "Watch on YouTube")

## [Anchor](https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/\#embrace-the-future-of-ai-data-retrieval) Embrace the Future of AI Data Retrieval

[Qdrant](https://github.com/qdrant/qdrant) offers the most flexible way to implement vector search for your RAG and AI applications. You can test out semantic cache on your free Qdrant Cloud instance today! Simply sign up for or log into your [Qdrant Cloud account](https://cloud.qdrant.io/login?ajs_anonymous_id=226d0c07-1a80-463f-bc66-b158aa712597) and follow our [documentation](https://qdrant.tech/documentation/cloud/).

You can also deploy Qdrant locally and manage via our UI. To do this, check our [Hybrid Cloud](https://qdrant.tech/blog/hybrid-cloud/)!

[![hybrid-cloud-get-started](https://qdrant.tech/blog/hybrid-cloud-launch-partners/hybrid-cloud-get-started.png)](https://cloud.qdrant.io/login?ajs_anonymous_id=226d0c07-1a80-463f-bc66-b158aa712597)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/semantic-cache-ai-data-retrieval.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/semantic-cache-ai-data-retrieval.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=dad6923b-f861-4674-91ed-2853e427ed88&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e3d3ccc2-a930-4436-872e-9935e25da806&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fsemantic-cache-ai-data-retrieval%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=dad6923b-f861-4674-91ed-2853e427ed88&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e3d3ccc2-a930-4436-872e-9935e25da806&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fsemantic-cache-ai-data-retrieval%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)