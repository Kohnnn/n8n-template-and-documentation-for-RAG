---
url: "https://qdrant.tech/articles/what-are-embeddings/"
title: "What are Vector Embeddings? - Revolutionize Your Search Experience - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- What are Vector Embeddings? - Revolutionize Your Search Experience

[Back to Vector Search Manuals](https://qdrant.tech/articles/vector-search-manuals/)

# What are Vector Embeddings? - Revolutionize Your Search Experience

Sabrina Aquino

·

February 06, 2024

![What are Vector Embeddings? - Revolutionize Your Search Experience](https://qdrant.tech/articles_data/what-are-embeddings/preview/title.jpg)

> **Embeddings** are numerical machine learning representations of the semantic of the input data. They capture the meaning of complex, high-dimensional data, like text, images, or audio, into vectors. Enabling algorithms to process and analyze the data more efficiently.

You know when you’re scrolling through your social media feeds and the content just feels incredibly tailored to you? There’s the news you care about, followed by a perfect tutorial with your favorite tech stack, and then a meme that makes you laugh so hard you snort.

Or what about how YouTube recommends videos you ended up loving. It’s by creators you’ve never even heard of and you didn’t even send YouTube a note about your ideal content lineup.

This is the magic of embeddings.

These are the result of **deep learning models** analyzing the data of your interactions online. From your likes, shares, comments, searches, the kind of content you linger on, and even the content you decide to skip. It also allows the algorithm to predict future content that you are likely to appreciate.

The same embeddings can be repurposed for search, ads, and other features, creating a highly personalized user experience.

![How embeddings are applied to perform recommendantions and other use cases](https://qdrant.tech/articles_data/what-are-embeddings/Embeddings-Use-Case.jpg)

They make [high-dimensional](https://www.sciencedirect.com/topics/computer-science/high-dimensional-data) data more manageable. This reduces storage requirements, improves computational efficiency, and makes sense of a ton of **unstructured** data.

## [Anchor](https://qdrant.tech/articles/what-are-embeddings/\#why-use-vector-embeddings) Why use vector embeddings?

The **nuances** of natural language or the hidden **meaning** in large datasets of images, sounds, or user interactions are hard to fit into a table. Traditional relational databases can’t efficiently query most types of data being currently used and produced, making the **retrieval** of this information very limited.

In the embeddings space, synonyms tend to appear in similar contexts and end up having similar embeddings. The space is a system smart enough to understand that “pretty” and “attractive” are playing for the same team. Without being explicitly told so.

That’s the magic.

At their core, vector embeddings are about semantics. They take the idea that “a word is known by the company it keeps” and apply it on a grand scale.

![Example of how synonyms are placed closer together in the embeddings space](https://qdrant.tech/articles_data/what-are-embeddings/Similar-Embeddings.jpg)

This capability is crucial for creating search systems, recommendation engines, retrieval augmented generation (RAG) and any application that benefits from a deep understanding of content.

## [Anchor](https://qdrant.tech/articles/what-are-embeddings/\#how-do-embeddings-work) How do embeddings work?

Embeddings are created through neural networks. They capture complex relationships and semantics into [dense vectors](https://www1.se.cuhk.edu.hk/~seem5680/lecture/semantics-with-dense-vectors-2018.pdf) which are more suitable for machine learning and data processing applications. They can then project these vectors into a proper **high-dimensional** space, specifically, a [Vector Database](https://qdrant.tech/articles/what-is-a-vector-database/).

![The process for turning raw data into embeddings and placing them into the vector space](https://qdrant.tech/articles_data/what-are-embeddings/How-Embeddings-Work.jpg)

The meaning of a data point is implicitly defined by its **position** on the vector space. After the vectors are stored, we can use their spatial properties to perform [nearest neighbor searches](https://en.wikipedia.org/wiki/Nearest_neighbor_search#:~:text=Nearest%20neighbor%20search%20%28NNS%29%2C,the%20larger%20the%20function%20values.). These searches retrieve semantically similar items based on how close they are in this space.

> The quality of the vector representations drives the performance. The embedding model that works best for you depends on your use case.

### [Anchor](https://qdrant.tech/articles/what-are-embeddings/\#creating-vector-embeddings) Creating vector embeddings

Embeddings translate the complexities of human language to a format that computers can understand. It uses neural networks to assign **numerical values** to the input data, in a way that similar data has similar values.

![The process of using Neural Networks to create vector embeddings](https://qdrant.tech/articles_data/what-are-embeddings/How-Do-Embeddings-Work_.jpg)

For example, if I want to make my computer understand the word ‘right’, I can assign a number like 1.3. So when my computer sees 1.3, it sees the word ‘right’.

Now I want to make my computer understand the context of the word ‘right’. I can use a two-dimensional vector, such as \[1.3, 0.8\], to represent ‘right’. The first number 1.3 still identifies the word ‘right’, but the second number 0.8 specifies the context.

We can introduce more dimensions to capture more nuances. For example, a third dimension could represent formality of the word, a fourth could indicate its emotional connotation (positive, neutral, negative), and so on.

The evolution of this concept led to the development of embedding models like [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) and [GloVe](https://en.wikipedia.org/wiki/GloVe). They learn to understand the context in which words appear to generate high-dimensional vectors for each word, capturing far more complex properties.

![How Word2Vec model creates the embeddings for a word](https://qdrant.tech/articles_data/what-are-embeddings/Word2Vec-model.jpg)

However, these models still have limitations. They generate a single vector per word, based on its usage across texts. This means all the nuances of the word “right” are blended into one vector representation. That is not enough information for computers to fully understand the context.

So, how do we help computers grasp the nuances of language in different contexts? In other words, how do we differentiate between:

- “your answer is right”
- “turn right at the corner”
- “everyone has the right to freedom of speech”

Each of these sentences use the word ‘right’, with different meanings.

More advanced models like [BERT](https://en.wikipedia.org/wiki/BERT_%28language_model%29) and [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer) use deep learning models based on the [transformer architecture](https://arxiv.org/abs/1706.03762), which helps computers consider the full context of a word. These models pay attention to the entire context. The model understands the specific use of a word in its **surroundings**, and then creates different embeddings for each.

![How the BERT model creates the embeddings for a word](https://qdrant.tech/articles_data/what-are-embeddings/BERT-model.jpg)

But how does this process of understanding and interpreting work in practice? Think of the term: “biophilic design”, for example. To generate its embedding, the transformer architecture can use the following contexts:

- “Biophilic design incorporates natural elements into architectural planning.”
- “Offices with biophilic design elements report higher employee well-being.”
- “…plant life, natural light, and water features are key aspects of biophilic design.”

And then it compares contexts to known architectural and design principles:

- “Sustainable designs prioritize environmental harmony.”
- “Ergonomic spaces enhance user comfort and health.”

The model creates a vector embedding for “biophilic design” that encapsulates the concept of integrating natural elements into man-made environments. Augmented with attributes that highlight the correlation between this integration and its positive impact on health, well-being, and environmental sustainability.

### [Anchor](https://qdrant.tech/articles/what-are-embeddings/\#integration-with-embedding-apis) Integration with embedding APIs

Selecting the right embedding model for your use case is crucial to your application performance. Qdrant makes it easier by offering seamless integration with the best selection of embedding APIs, including [Cohere](https://qdrant.tech/documentation/embeddings/cohere/), [Gemini](https://qdrant.tech/documentation/embeddings/gemini/), [Jina Embeddings](https://qdrant.tech/documentation/embeddings/jina-embeddings/), [OpenAI](https://qdrant.tech/documentation/embeddings/openai/), [Aleph Alpha](https://qdrant.tech/documentation/embeddings/aleph-alpha/), [Fastembed](https://github.com/qdrant/fastembed), and [AWS Bedrock](https://qdrant.tech/documentation/embeddings/bedrock/).

If you’re looking for NLP and rapid prototyping, including language translation, question-answering, and text generation, OpenAI is a great choice. Gemini is ideal for image search, duplicate detection, and clustering tasks.

Fastembed, which we’ll use on the example below, is designed for efficiency and speed, great for applications needing low-latency responses, such as autocomplete and instant content recommendations.

We plan to go deeper into selecting the best model based on performance, cost, integration ease, and scalability in a future post.

## [Anchor](https://qdrant.tech/articles/what-are-embeddings/\#create-a-neural-search-service-with-fastmbed) Create a neural search service with Fastmbed

Now that you’re familiar with the core concepts around vector embeddings, how about start building your own [Neural Search Service](https://qdrant.tech/documentation/tutorials/neural-search/)?

Tutorial guides you through a practical application of how to use Qdrant for document management based on descriptions of companies from [startups-list.com](https://www.startups-list.com/). From embedding data, integrating it with Qdrant’s vector database, constructing a search API, and finally deploying your solution with FastAPI.

Check out what the final version of this project looks like on the [live online demo](https://qdrant.to/semantic-search-demo).

Let us know what you’re building with embeddings! Join our [Discord](https://discord.gg/qdrant-907569970500743200) community and share your projects!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/what-are-embeddings.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/what-are-embeddings.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575236921&cv=11&fst=1748575236921&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhat-are-embeddings%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=What%20are%20Vector%20Embeddings%3F%20-%20Revolutionize%20Your%20Search%20Experience%20-%20Qdrant&npa=0&pscdl=noapi&auid=104352312.1748575237&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575236902&cv=11&fst=1748575236902&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhat-are-embeddings%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=What%20are%20Vector%20Embeddings%3F%20-%20Revolutionize%20Your%20Search%20Experience%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=104352312.1748575237&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=46f97b13-6942-4728-bc71-af6b05ed5340&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9dc31a58-884d-4bba-a804-70cc35b8eca9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhat-are-embeddings%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=46f97b13-6942-4728-bc71-af6b05ed5340&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9dc31a58-884d-4bba-a804-70cc35b8eca9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhat-are-embeddings%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575237720&cv=11&fst=1748575237720&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhat-are-embeddings%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=What%20are%20Vector%20Embeddings%3F%20-%20Revolutionize%20Your%20Search%20Experience%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=104352312.1748575237&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)