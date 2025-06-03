---
url: "https://qdrant.tech/articles/what-is-rag-in-ai/"
title: "What is RAG: Understanding Retrieval-Augmented Generation - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- What is RAG: Understanding Retrieval-Augmented Generation

[Back to RAG & GenAI](https://qdrant.tech/articles/rag-and-genai/)

# What is RAG: Understanding Retrieval-Augmented Generation

Sabrina Aquino

·

March 19, 2024

![What is RAG: Understanding Retrieval-Augmented Generation](https://qdrant.tech/articles_data/what-is-rag-in-ai/preview/title.jpg)

> Retrieval-augmented generation (RAG) integrates external information retrieval into the process of generating responses by Large Language Models (LLMs). It searches a database for information beyond its pre-trained knowledge base, significantly improving the accuracy and relevance of the generated responses.

Language models have exploded on the internet ever since ChatGPT came out, and rightfully so. They can write essays, code entire programs, and even make memes (though we’re still deciding on whether that’s a good thing).

But as brilliant as these chatbots become, they still have **limitations** in tasks requiring external knowledge and factual information. Yes, it can describe the honeybee’s waggle dance in excruciating detail. But they become far more valuable if they can generate insights from **any data** that we provide, rather than just their original training data. Since retraining those large language models from scratch costs millions of dollars and takes months, we need better ways to give our existing LLMs access to our custom data.

While you could be more creative with your prompts, it is only a short-term solution. LLMs can consider only a **limited** amount of text in their responses, known as a [context window](https://www.hopsworks.ai/dictionary/context-window-for-llms). Some models like GPT-3 can see up to around 12 pages of text (that’s 4,096 tokens of context). That’s not good enough for most knowledge bases.

![How a RAG works](https://qdrant.tech/articles_data/what-is-rag-in-ai/how-rag-works.jpg)

The image above shows how a basic RAG system works. Before forwarding the question to the LLM, we have a layer that searches our knowledge base for the “relevant knowledge” to answer the user query. Specifically, in this case, the spending data from the last month. Our LLM can now generate a **relevant non-hallucinated** response about our budget.

As your data grows, you’ll need [efficient ways](https://qdrant.tech/rag/rag-evaluation-guide/) to identify the most relevant information for your LLM’s limited memory. This is where you’ll want a proper way to store and retrieve the specific data you’ll need for your query, without needing the LLM to remember it.

**Vector databases** store information as **vector embeddings**. This format supports efficient similarity searches to retrieve relevant data for your query. For example, Qdrant is specifically designed to perform fast, even in scenarios dealing with billions of vectors.

This article will focus on RAG systems and architecture. If you’re interested in learning more about vector search, we recommend the following articles: [What is a Vector Database?](https://qdrant.tech/articles/what-is-a-vector-database/) and [What are Vector Embeddings?](https://qdrant.tech/articles/what-are-embeddings/).

## [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#rag-architecture) RAG architecture

At its core, a RAG architecture includes the **retriever** and the **generator**. Let’s start by understanding what each of these components does.

### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#the-retriever) The Retriever

When you ask a question to the retriever, it uses **similarity search** to scan through a vast knowledge base of vector embeddings. It then pulls out the most **relevant** vectors to help answer that query. There are a few different techniques it can use to know what’s relevant:

#### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#how-indexing-works-in-rag-retrievers) How indexing works in RAG retrievers

The indexing process organizes the data into your vector database in a way that makes it easily searchable. This allows the RAG to access relevant information when responding to a query.

![How indexing works](https://qdrant.tech/articles_data/what-is-rag-in-ai/how-indexing-works.jpg)

As shown in the image above, here’s the process:

- Start with a _loader_ that gathers _documents_ containing your data. These documents could be anything from articles and books to web pages and social media posts.
- Next, a _splitter_ divides the documents into smaller chunks, typically sentences or paragraphs.
- This is because RAG models work better with smaller pieces of text. In the diagram, these are _document snippets_.
- Each text chunk is then fed into an _embedding machine_. This machine uses complex algorithms to convert the text into [vector embeddings](https://qdrant.tech/articles/what-are-embeddings/).

All the generated vector embeddings are stored in a knowledge base of indexed information. This supports efficient retrieval of similar pieces of information when needed.

#### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#query-vectorization) Query vectorization

Once you have vectorized your knowledge base you can do the same to the user query. When the model sees a new query, it uses the same preprocessing and embedding techniques. This ensures that the query vector is compatible with the document vectors in the index.

![How retrieval works](https://qdrant.tech/articles_data/what-is-rag-in-ai/how-retrieval-works.jpg)

#### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#retrieval-of-relevant-documents) Retrieval of relevant documents

When the system needs to find the most relevant documents or passages to answer a query, it utilizes vector similarity techniques. **Vector similarity** is a fundamental concept in machine learning and natural language processing (NLP) that quantifies the resemblance between vectors, which are mathematical representations of data points.

The system can employ different vector similarity strategies depending on the type of vectors used to represent the data:

##### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#sparse-vector-representations) Sparse vector representations

A sparse vector is characterized by a high dimensionality, with most of its elements being zero.

The classic approach is **keyword search**, which scans documents for the exact words or phrases in the query. The search creates sparse vector representations of documents by counting word occurrences and inversely weighting common words. Queries with rarer words get prioritized.

![Sparse vector representation](https://qdrant.tech/articles_data/what-is-rag-in-ai/sparse-vectors.jpg)

[TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (Term Frequency-Inverse Document Frequency) and [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) are two classic related algorithms. They’re simple and computationally efficient. However, they can struggle with synonyms and don’t always capture semantic similarities.

If you’re interested in going deeper, refer to our article on [Sparse Vectors](https://qdrant.tech/articles/sparse-vectors/).

##### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#dense-vector-embeddings) Dense vector embeddings

This approach uses large language models like [BERT](https://en.wikipedia.org/wiki/BERT_%28language_model%29) to encode the query and passages into dense vector embeddings. These models are compact numerical representations that capture semantic meaning. Vector databases like Qdrant store these embeddings, allowing retrieval based on **semantic similarity** rather than just keywords using distance metrics like cosine similarity.

This allows the retriever to match based on semantic understanding rather than just keywords. So if I ask about “compounds that cause BO,” it can retrieve relevant info about “molecules that create body odor” even if those exact words weren’t used. We explain more about it in our [What are Vector Embeddings](https://qdrant.tech/articles/what-are-embeddings/) article.

#### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#hybrid-search) Hybrid search

However, neither keyword search nor vector search are always perfect. Keyword search may miss relevant information expressed differently, while vector search can sometimes struggle with specificity or neglect important statistical word patterns. Hybrid methods aim to combine the strengths of different techniques.

![Hybrid search overview](https://qdrant.tech/articles_data/what-is-rag-in-ai/hybrid-search.jpg)

Some common hybrid approaches include:

- Using keyword search to get an initial set of candidate documents. Next, the documents are re-ranked/re-scored using semantic vector representations.
- Starting with semantic vectors to find generally topically relevant documents. Next, the documents are filtered/re-ranked e based on keyword matches or other metadata.
- Considering both semantic vector closeness and statistical keyword patterns/weights in a combined scoring model.
- Having multiple stages were different techniques. One example: start with an initial keyword retrieval, followed by semantic re-ranking, then a final re-ranking using even more complex models.

When you combine the powers of different search methods in a complementary way, you can provide higher quality, more comprehensive results. Check out our article on [Hybrid Search](https://qdrant.tech/articles/hybrid-search/) if you’d like to learn more.

### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#the-generator) The Generator

With the top relevant passages retrieved, it’s now the generator’s job to produce a final answer by synthesizing and expressing that information in natural language.

The LLM is typically a model like GPT, BART or T5, trained on massive datasets to understand and generate human-like text. It now takes not only the query (or question) as input but also the relevant documents or passages that the retriever identified as potentially containing the answer to generate its response.

![How a Generator works](https://qdrant.tech/articles_data/what-is-rag-in-ai/how-generation-works.png)

The retriever and generator don’t operate in isolation. The image bellow shows how the output of the retrieval feeds the generator to produce the final generated response.

![The entire architecture of a RAG system](https://qdrant.tech/articles_data/what-is-rag-in-ai/rag-system.jpg)

## [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#where-is-rag-being-used) Where is RAG being used?

Because of their more knowledgeable and contextual responses, we can find RAG models being applied in many areas today, especially those who need factual accuracy and knowledge depth.

### [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#real-world-applications) Real-World Applications:

**Question answering:** This is perhaps the most prominent use case for RAG models. They power advanced question-answering systems that can retrieve relevant information from large knowledge bases and then generate fluent answers.

**Language generation:** RAG enables more factual and contextualized text generation for contextualized text summarization from multiple sources

**Data-to-text generation:** By retrieving relevant structured data, RAG models can generate product/business intelligence reports from databases or describing insights from data visualizations and charts

**Multimedia understanding:** RAG isn’t limited to text - it can retrieve multimodal information like images, video, and audio to enhance understanding. Answering questions about images/videos by retrieving relevant textual context.

## [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#creating-your-first-rag-chatbot-with-langchain-groq-and-openai) Creating your first RAG chatbot with Langchain, Groq, and OpenAI

Are you ready to create your own RAG chatbot from the ground up? We have a video explaining everything from the beginning. Daniel Romero’s will guide you through:

- Setting up your chatbot
- Preprocessing and organizing data for your chatbot’s use
- Applying vector similarity search algorithms
- Enhancing the efficiency and response quality

After building your RAG chatbot, you’ll be able to [evaluate its performance](https://qdrant.tech/rag/rag-evaluation-guide/) against that of a chatbot powered solely by a Large Language Model (LLM).

Chatbot with RAG, using LangChain, OpenAI, and Groq - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Chatbot with RAG, using LangChain, OpenAI, and Groq](https://www.youtube.com/watch?v=O60-KuZZeQA)

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

[Watch on](https://www.youtube.com/watch?v=O60-KuZZeQA&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 20:14
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=O60-KuZZeQA "Watch on YouTube")

## [Anchor](https://qdrant.tech/articles/what-is-rag-in-ai/\#whats-next) What’s next?

Have a RAG project you want to bring to life? Join our [Discord community](https://discord.gg/qdrant) where we’re always sharing tips and answering questions on vector search and retrieval.

Learn more about how to properly evaluate your RAG responses: [Evaluating Retrieval Augmented Generation - a framework for assessment](https://superlinked.com/vectorhub/evaluating-retrieval-augmented-generation-a-framework-for-assessment).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/what-is-rag-in-ai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/what-is-rag-in-ai.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1566fac2-70a6-46fe-8ce6-49162d67999d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f3b3d65c-b206-4a3f-99cc-586a8c0b2851&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhat-is-rag-in-ai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1566fac2-70a6-46fe-8ce6-49162d67999d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f3b3d65c-b206-4a3f-99cc-586a8c0b2851&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhat-is-rag-in-ai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)