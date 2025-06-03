---
url: "https://qdrant.tech/articles/langchain-integration/"
title: "Using LangChain for Question Answering with Qdrant - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Using LangChain for Question Answering with Qdrant

[Back to Practical Examples](https://qdrant.tech/articles/practicle-examples/)

# Using LangChain for Question Answering with Qdrant

Kacper Łukawski

·

January 31, 2023

![Using LangChain for Question Answering with Qdrant](https://qdrant.tech/articles_data/langchain-integration/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/langchain-integration/\#streamlining-question-answering-simplifying-integration-with-langchain-and-qdrant) Streamlining Question Answering: Simplifying Integration with LangChain and Qdrant

Building applications with Large Language Models doesn’t have to be complicated. A lot has been going on recently to simplify the development,
so you can utilize already pre-trained models and support even complex pipelines with a few lines of code. [LangChain](https://langchain.readthedocs.io/)
provides unified interfaces to different libraries, so you can avoid writing boilerplate code and focus on the value you want to bring.

## [Anchor](https://qdrant.tech/articles/langchain-integration/\#why-use-qdrant-for-question-answering-with-langchain) Why Use Qdrant for Question Answering with LangChain?

It has been reported millions of times recently, but let’s say that again. ChatGPT-like models struggle with generating factual statements if no context
is provided. They have some general knowledge but cannot guarantee to produce a valid answer consistently. Thus, it is better to provide some facts we
know are actual, so it can just choose the valid parts and extract them from all the provided contextual data to give a comprehensive answer. [Vector database,\\
such as Qdrant](https://qdrant.tech/), is of great help here, as their ability to perform a [semantic search](https://qdrant.tech/documentation/tutorials/search-beginners/) over a huge knowledge base is crucial to preselect some possibly valid
documents, so they can be provided into the LLM. That’s also one of the **chains** implemented in [LangChain](https://qdrant.tech/documentation/frameworks/langchain/), which is called `VectorDBQA`. And Qdrant got
integrated with the library, so it might be used to build it effortlessly.

### [Anchor](https://qdrant.tech/articles/langchain-integration/\#the-two-model-approach) The Two-Model Approach

Surprisingly enough, there will be two models required to set things up. First of all, we need an embedding model that will convert the set of facts into
vectors, and store those into Qdrant. That’s an identical process to any other semantic search application. We’re going to use one of the
`SentenceTransformers` models, so it can be hosted locally. The embeddings created by that model will be put into Qdrant and used to retrieve the most
similar documents, given the query.

However, when we receive a query, there are two steps involved. First of all, we ask Qdrant to provide the most relevant documents and simply combine all
of them into a single text. Then, we build a prompt to the LLM (in our case [OpenAI](https://openai.com/)), including those documents as a context, of course together with the
question asked. So the input to the LLM looks like the following:

```text
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
It's as certain as 2 + 2 = 4
...

Question: How much is 2 + 2?
Helpful Answer:

```

There might be several context documents combined, and it is solely up to LLM to choose the right piece of content. But our expectation is, the model should
respond with just `4`.

## [Anchor](https://qdrant.tech/articles/langchain-integration/\#why-do-we-need-two-different-models) Why do we need two different models?

Both solve some different tasks. The first model performs feature extraction, by converting the text into vectors, while
the second one helps in text generation or summarization. Disclaimer: This is not the only way to solve that task with LangChain. Such a chain is called `stuff`
in the library nomenclature.

![](https://qdrant.tech/articles_data/langchain-integration/flow-diagram.png)

Enough theory! This sounds like a pretty complex application, as it involves several systems. But with LangChain, it might be implemented in just a few lines
of code, thanks to the recent integration with [Qdrant](https://qdrant.tech/). We’re not even going to work directly with `QdrantClient`, as everything is already done in the background
by LangChain. If you want to get into the source code right away, all the processing is available as a
[Google Colab notebook](https://colab.research.google.com/drive/19RxxkZdnq_YqBH5kBV10Rt0Rax-kminD?usp=sharing).

## [Anchor](https://qdrant.tech/articles/langchain-integration/\#how-to-implement-question-answering-with-langchain-and-qdrant) How to Implement Question Answering with LangChain and Qdrant

### [Anchor](https://qdrant.tech/articles/langchain-integration/\#step-1-configuration) Step 1: Configuration

A journey of a thousand miles begins with a single step, in our case with the configuration of all the services. We’ll be using [Qdrant Cloud](https://cloud.qdrant.io/),
so we need an API key. The same is for OpenAI - the API key has to be obtained from their website.

![](https://qdrant.tech/articles_data/langchain-integration/code-configuration.png)

### [Anchor](https://qdrant.tech/articles/langchain-integration/\#step-2-building-the-knowledge-base) Step 2: Building the knowledge base

We also need some facts from which the answers will be generated. There is plenty of public datasets available, and
[Natural Questions](https://ai.google.com/research/NaturalQuestions/visualization) is one of them. It consists of the whole HTML content of the websites they were
scraped from. That means we need some preprocessing to extract plain text content. As a result, we’re going to have two lists of strings - one for questions and
the other one for the answers.

The answers have to be vectorized with the first of our models. The `sentence-transformers/all-mpnet-base-v2` is one of the possibilities, but there are some
other options available. LangChain will handle that part of the process in a single function call.

![](https://qdrant.tech/articles_data/langchain-integration/code-qdrant.png)

### [Anchor](https://qdrant.tech/articles/langchain-integration/\#step-3-setting-up-qa-with-qdrant-in-a-loop) Step 3: Setting up QA with Qdrant in a loop

`VectorDBQA` is a chain that performs the process described above. So it, first of all, loads some facts from Qdrant and then feeds them into OpenAI LLM which
should analyze them to find the answer to a given question. The only last thing to do before using it is to put things together, also with a single function call.

![](https://qdrant.tech/articles_data/langchain-integration/code-vectordbqa.png)

## [Anchor](https://qdrant.tech/articles/langchain-integration/\#step-4-testing-out-the-chain) Step 4: Testing out the chain

And that’s it! We can put some queries, and LangChain will perform all the required processing to find the answer in the provided context.

![](https://qdrant.tech/articles_data/langchain-integration/code-answering.png)

```text
> what kind of music is scott joplin most famous for
 Scott Joplin is most famous for composing ragtime music.

> who died from the band faith no more
 Chuck Mosley

> when does maggie come on grey's anatomy
 Maggie first appears in season 10, episode 1, which aired on September 26, 2013.

> can't take my eyes off you lyrics meaning
 I don't know.

> who lasted the longest on alone season 2
 David McIntyre lasted the longest on Alone season 2, with a total of 66 days.

```

The great thing about such a setup is that the knowledge base might be easily extended with some new facts and those will be included in the prompts
sent to LLM later on. Of course, assuming their similarity to the given question will be in the top results returned by Qdrant.

If you want to run the chain on your own, the simplest way to reproduce it is to open the
[Google Colab notebook](https://colab.research.google.com/drive/19RxxkZdnq_YqBH5kBV10Rt0Rax-kminD?usp=sharing).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/langchain-integration.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/langchain-integration.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574738466&cv=11&fst=1748574738466&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Flangchain-integration%2F&hn=www.googleadservices.com&frm=0&tiba=Using%20LangChain%20for%20Question%20Answering%20with%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=1838115865.1748574738&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574738448&cv=11&fst=1748574738448&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Flangchain-integration%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Using%20LangChain%20for%20Question%20Answering%20with%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1838115865.1748574738&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4ba55ea8-e6b1-40f8-a774-6fbf36251316&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3df645d1-fd06-45bd-a8a0-e16e030453c9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Flangchain-integration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4ba55ea8-e6b1-40f8-a774-6fbf36251316&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3df645d1-fd06-45bd-a8a0-e16e030453c9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Flangchain-integration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574739894&cv=11&fst=1748574739894&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Flangchain-integration%2F&hn=www.googleadservices.com&frm=0&tiba=Using%20LangChain%20for%20Question%20Answering%20with%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1838115865.1748574738&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)