---
url: "https://qdrant.tech/blog/using-qdrant-and-langchain/"
title: "Integrating Qdrant and LangChain for Advanced Vector Similarity Search - Qdrant"
---

0

# Integrating Qdrant and LangChain for Advanced Vector Similarity Search

David Myriel

·

March 12, 2024

![Integrating Qdrant and LangChain for Advanced Vector Similarity Search](https://qdrant.tech/blog/using-qdrant-and-langchain/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fusing-qdrant-and-langchain%2F&text=Integrating%20Qdrant%20and%20LangChain%20for%20Advanced%20Vector%20Similarity%20Search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fusing-qdrant-and-langchain%2F "LinkedIn")

> _“Building AI applications doesn’t have to be complicated. You can leverage pre-trained models and support complex pipelines with a few lines of code. LangChain provides a unified interface, so that you can avoid writing boilerplate code and focus on the value you want to bring.”_ Kacper Lukawski, Developer Advocate, Qdrant

## [Anchor](https://qdrant.tech/blog/using-qdrant-and-langchain/\#long-term-memory-for-your-genai-app) Long-Term Memory for Your GenAI App

Qdrant’s vector database quickly grew due to its ability to make Generative AI more effective. On its own, an LLM can be used to build a process-altering invention. With Qdrant, you can turn this invention into a production-level app that brings real business value.

The use of vector search in GenAI now has a name: **Retrieval Augmented Generation (RAG)**. [In our previous article](https://qdrant.tech/articles/rag-is-dead/), we argued why RAG is an essential component of AI setups, and why large-scale AI can’t operate without it. Numerous case studies explain that AI applications are simply too costly and resource-intensive to run using only LLMs.

> Going forward, the solution is to leverage composite systems that use models and vector databases.

**What is RAG?** Essentially, a RAG setup turns Qdrant into long-term memory storage for LLMs. As a vector database, Qdrant manages the efficient storage and retrieval of user data.

Adding relevant context to LLMs can vastly improve user experience, leading to better retrieval accuracy, faster query speed and lower use of compute. Augmenting your AI application with vector search reduces hallucinations, a situation where AI models produce legitimate-sounding but made-up responses.

Qdrant streamlines this process of retrieval augmentation, making it faster, easier to scale and efficient. When you are accessing vast amounts of data (hundreds or thousands of documents), vector search helps your sort through relevant context. **This makes RAG a primary candidate for enterprise-scale use cases.**

## [Anchor](https://qdrant.tech/blog/using-qdrant-and-langchain/\#why-langchain) Why LangChain?

Retrieval Augmented Generation is not without its challenges and limitations. One of the main setbacks for app developers is managing the entire setup. The integration of a retriever and a generator into a single model can lead to a raised level of complexity, thus increasing the computational resources required.

[LangChain](https://www.langchain.com/) is a framework that makes developing RAG-based applications much easier. It unifies interfaces to different libraries, including major embedding providers like OpenAI or Cohere and vector stores like Qdrant. With LangChain, you can focus on creating tangible GenAI applications instead of writing your logic from the ground up.

> Qdrant is one of the **top supported vector stores** on LangChain, with [extensive documentation](https://python.langchain.com/docs/integrations/vectorstores/qdrant) and [examples](https://python.langchain.com/docs/integrations/retrievers/self_query/qdrant_self_query).

**How it Works:** LangChain receives a query and retrieves the query vector from an embedding model. Then, it dispatches the vector to a vector database, retrieving relevant documents. Finally, both the query and the retrieved documents are sent to the large language model to generate an answer.

![qdrant-langchain-rag](https://qdrant.tech/blog/using-qdrant-and-langchain/flow-diagram.png)

When supported by LangChain, Qdrant can help you set up effective question-answer systems, detection systems and chatbots that leverage RAG to its full potential. When it comes to long-term memory storage, developers can use LangChain to easily add relevant documents, chat history memory & rich user data to LLM app prompts via Qdrant.

## [Anchor](https://qdrant.tech/blog/using-qdrant-and-langchain/\#common-use-cases) Common Use Cases

Integrating Qdrant and LangChain can revolutionize your AI applications. Let’s take a look at what this integration can do for you:

_Enhance Natural Language Processing (NLP):_
LangChain is great for developing question-answering **chatbots**, where Qdrant is used to contextualize and retrieve results for the LLM. We cover this in [our article](https://qdrant.tech/articles/langchain-integration/), and in OpenAI’s [cookbook examples](https://cookbook.openai.com/examples/vector_databases/qdrant/qa_with_langchain_qdrant_and_openai) that use LangChain and GPT to process natural language.

_Improve Recommendation Systems:_
Food delivery services thrive on indecisive customers. Businesses need to accomodate a multi-aim search process, where customers seek recommendations though semantic search. With LangChain you can build systems for **e-commerce, content sharing, or even dating apps**.

_Advance Data Analysis and Insights:_ Sometimes you just want to browse results that are not necessarily closest, but still relevant. Semantic search helps user discover products in **online stores**. Customers don’t exactly know what they are looking for, but require constrained space in which a search is performed.

_Offer Content Similarity Analysis:_ Ever been stuck seeing the same recommendations on your **local news portal**? You may be held in a similarity bubble! As inputs get more complex, diversity becomes scarce, and it becomes harder to force the system to show something different. LangChain developers can use semantic search to develop further context.

## [Anchor](https://qdrant.tech/blog/using-qdrant-and-langchain/\#building-a-chatbot-with-langchain) Building a Chatbot with LangChain

_Now that you know how Qdrant and LangChain work together - it’s time to build something!_

Follow Daniel Romero’s video and create a RAG Chatbot completely from scratch. You will only use OpenAI, Qdrant and LangChain.
Here is what this basic tutorial will teach you:

**1\. How to set up a chatbot using Qdrant and LangChain:** You will use LangChain to create a RAG pipeline that retrieves information from a dataset and generates output. This will demonstrate the difference between using an LLM by itself and leveraging a vector database like Qdrant for memory retrieval.

**2\. Preprocess and format data for use by the chatbot:** First, you will download a sample dataset based on some academic journals. Then, you will process this data into embeddings and store it as vectors inside of Qdrant.

**3\. Implement vector similarity search algorithms:** Second, you will create and test a chatbot that only uses the LLM. Then, you will enable the memory component offered by Qdrant. This will allow your chatbot to be modified and updated, giving it long-term memory.

**4\. Optimize the chatbot’s performance:** In the last step, you will query the chatbot in two ways. First query will retrieve parametric data from the LLM, while the second one will get contexual data via Qdrant.

The goal of this exercise is to show that RAG is simple to implement via LangChain and yields much better results than using LLMs by itself.

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

## [Anchor](https://qdrant.tech/blog/using-qdrant-and-langchain/\#scaling-qdrant-and-langchain) Scaling Qdrant and LangChain

If you are looking to scale up and keep the same level of performance, Qdrant and LangChain are a rock-solid combination. Getting started with both is a breeze and the [documentation](https://python.langchain.com/docs/integrations/vectorstores/qdrant) covers a broad number of cases. However, the main strength of Qdrant is that it can consistently support the user way past the prototyping and launch phases.

> _“We are all-in on performance and reliability. Every release we make Qdrant faster, more stable and cost-effective for the user. When others focus on prototyping, we are already ready for production. Very soon, our users will build successful products and go to market. At this point, I anticipate a great need for a reliable vector store. Qdrant will be there for LangChain and the entire community.”_

Whether you are building a bank fraud-detection system, RAG for e-commerce, or services for the federal government - you will need to leverage a scalable architecture for your product. Qdrant offers different features to help you considerably increase your application’s performance and lower your hosting costs.

> Read more about out how we foster [best practices for large-scale deployments](https://qdrant.tech/articles/multitenancy/).

## [Anchor](https://qdrant.tech/blog/using-qdrant-and-langchain/\#next-steps) Next Steps

Now that you know how Qdrant and LangChain can elevate your setup - it’s time to try us out.

- Qdrant is open source and you can [quickstart locally](https://qdrant.tech/documentation/quick-start/), [install it via Docker](https://qdrant.tech/documentation/quick-start/), [or to Kubernetes](https://github.com/qdrant/qdrant-helm/).

- We also offer [a free-tier of Qdrant Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=57610583-0fc4-4edb-a5ac-2a64e10e0597) for prototyping and testing.

- For best integration with LangChain, read the [official LangChain documentation](https://python.langchain.com/docs/integrations/vectorstores/qdrant/).

- For all other cases, [Qdrant documentation](https://qdrant.tech/documentation/integrations/langchain/) is the best place to get there.


> We offer additional support tailored to your business needs. [Contact us](https://qdrant.to/contact-us) to learn more about implementation strategies and integrations that suit your company.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=57610583-0fc4-4edb-a5ac-2a64e10e0597)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=798860c6-28aa-4874-b20b-ccf1bce1c0af&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c09d34d3-293d-4542-8e85-a142953028c4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fusing-qdrant-and-langchain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=798860c6-28aa-4874-b20b-ccf1bce1c0af&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c09d34d3-293d-4542-8e85-a142953028c4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fusing-qdrant-and-langchain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)