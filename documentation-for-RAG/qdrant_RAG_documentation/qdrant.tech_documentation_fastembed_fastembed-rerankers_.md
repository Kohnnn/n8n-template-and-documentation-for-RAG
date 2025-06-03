---
url: "https://qdrant.tech/documentation/fastembed/fastembed-rerankers/"
title: "Reranking with FastEmbed - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Fastembed](https://qdrant.tech/documentation/fastembed/)
- Reranking with FastEmbed

# [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/\#how-to-use-rerankers-with-fastembed) How to use rerankers with FastEmbed

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/\#rerankers) Rerankers

A reranker is a model that improves the ordering of search results. A subset of documents is initially retrieved using a fast, simple method (e.g., BM25 or dense embeddings). Then, a reranker – a more powerful, precise, but slower and heavier model – re-evaluates this subset to refine document relevance to the query.

Rerankers analyze token-level interactions between the query and each document in depth, making them expensive to use but precise in defining relevance. They trade speed for accuracy, so they are best used on a limited candidate set rather than the entire corpus.

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/\#goal-of-this-tutorial) Goal of this Tutorial

It’s common to use [cross-encoder](https://sbert.net/examples/applications/cross-encoder/README.html) models as rerankers. This tutorial uses [Jina Reranker v2 Base Multilingual](https://jina.ai/news/jina-reranker-v2-for-agentic-rag-ultra-fast-multilingual-function-calling-and-code-search/) (licensed under CC-BY-NC-4.0) – a cross-encoder reranker supported in FastEmbed.

We use the `all-MiniLM-L6-v2` dense embedding model (also supported in FastEmbed) as a first-stage retriever and then refine results with `Jina Reranker v2`.

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/\#setup) Setup

Install `qdrant-client` with `fastembed`.

```python
pip install "qdrant-client[fastembed]>=1.14.1"

```

Import cross-encoders and text embeddings for the first-stage retrieval.

```python
from fastembed import TextEmbedding
from fastembed.rerank.cross_encoder import TextCrossEncoder

```

You can list the cross-encoder rerankers supported in FastEmbed using the following command.

```python
TextCrossEncoder.list_supported_models()

```

This command displays the available models, including details such as output embedding dimensions, model description, model size, model sources, and model file.

Avaliable models

```python
[{'model': 'Xenova/ms-marco-MiniLM-L-6-v2',\
  'size_in_GB': 0.08,\
  'sources': {'hf': 'Xenova/ms-marco-MiniLM-L-6-v2'},\
  'model_file': 'onnx/model.onnx',\
  'description': 'MiniLM-L-6-v2 model optimized for re-ranking tasks.',\
  'license': 'apache-2.0'},\
 {'model': 'Xenova/ms-marco-MiniLM-L-12-v2',\
  'size_in_GB': 0.12,\
  'sources': {'hf': 'Xenova/ms-marco-MiniLM-L-12-v2'},\
  'model_file': 'onnx/model.onnx',\
  'description': 'MiniLM-L-12-v2 model optimized for re-ranking tasks.',\
  'license': 'apache-2.0'},\
 {'model': 'BAAI/bge-reranker-base',\
  'size_in_GB': 1.04,\
  'sources': {'hf': 'BAAI/bge-reranker-base'},\
  'model_file': 'onnx/model.onnx',\
  'description': 'BGE reranker base model for cross-encoder re-ranking.',\
  'license': 'mit'},\
 {'model': 'jinaai/jina-reranker-v1-tiny-en',\
  'size_in_GB': 0.13,\
  'sources': {'hf': 'jinaai/jina-reranker-v1-tiny-en'},\
  'model_file': 'onnx/model.onnx',\
  'description': 'Designed for blazing-fast re-ranking with 8K context length and fewer parameters than jina-reranker-v1-turbo-en.',\
  'license': 'apache-2.0'},\
 {'model': 'jinaai/jina-reranker-v1-turbo-en',\
  'size_in_GB': 0.15,\
  'sources': {'hf': 'jinaai/jina-reranker-v1-turbo-en'},\
  'model_file': 'onnx/model.onnx',\
  'description': 'Designed for blazing-fast re-ranking with 8K context length.',\
  'license': 'apache-2.0'},\
 {'model': 'jinaai/jina-reranker-v2-base-multilingual',\
  'size_in_GB': 1.11,\
  'sources': {'hf': 'jinaai/jina-reranker-v2-base-multilingual'},\
  'model_file': 'onnx/model.onnx',\
  'description': 'A multi-lingual reranker model for cross-encoder re-ranking with 1K context length and sliding window',\
  'license': 'cc-by-nc-4.0'}]  # some of the fields are omitted for brevity

```

Now, load the first-stage retriever and reranker.

```python
encoder_name = "sentence-transformers/all-MiniLM-L6-v2"
dense_embedding_model = TextEmbedding(model_name=encoder_name)
reranker = TextCrossEncoder(model_name='jinaai/jina-reranker-v2-base-multilingual')

```

The model files will be fetched and downloaded, with progress displayed.

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/\#embed--index-data-for-the-first-stage-retrieval) Embed & index data for the first-stage retrieval

We will vectorize a toy movie description dataset using the `all-MiniLM-L6-v2` model and save the embeddings in Qdrant for first-stage retrieval.

Then, we will use a cross-encoder reranking model to rerank a small subset of data retrieved in the first stage.

Movie description dataset

```python
descriptions = ["In 1431, Jeanne d'Arc is placed on trial on charges of heresy. The ecclesiastical jurists attempt to force Jeanne to recant her claims of holy visions.",\
 "A film projectionist longs to be a detective, and puts his meagre skills to work when he is framed by a rival for stealing his girlfriend's father's pocketwatch.",\
 "A group of high-end professional thieves start to feel the heat from the LAPD when they unknowingly leave a clue at their latest heist.",\
 "A petty thief with an utter resemblance to a samurai warlord is hired as the lord's double. When the warlord later dies the thief is forced to take up arms in his place.",\
 "A young boy named Kubo must locate a magical suit of armour worn by his late father in order to defeat a vengeful spirit from the past.",\
 "A biopic detailing the 2 decades that Punjabi Sikh revolutionary Udham Singh spent planning the assassination of the man responsible for the Jallianwala Bagh massacre.",\
 "When a machine that allows therapists to enter their patients' dreams is stolen, all hell breaks loose. Only a young female therapist, Paprika, can stop it.",\
 "An ordinary word processor has the worst night of his life after he agrees to visit a girl in Soho whom he met that evening at a coffee shop.",\
 "A story that revolves around drug abuse in the affluent north Indian State of Punjab and how the youth there have succumbed to it en-masse resulting in a socio-economic decline.",\
 "A world-weary political journalist picks up the story of a woman's search for her son, who was taken away from her decades ago after she became pregnant and was forced to live in a convent.",\
 "Concurrent theatrical ending of the TV series Neon Genesis Evangelion (1995).",\
 "During World War II, a rebellious U.S. Army Major is assigned a dozen convicted murderers to train and lead them into a mass assassination mission of German officers.",\
 "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",\
 "A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.",\
 "After two male musicians witness a mob hit, they flee the state in an all-female band disguised as women, but further complications set in.",\
 "Exiled into the dangerous forest by her wicked stepmother, a princess is rescued by seven dwarf miners who make her part of their household.",\
 "A renegade reporter trailing a young runaway heiress for a big story joins her on a bus heading from Florida to New York, and they end up stuck with each other when the bus leaves them behind at one of the stops.",\
 "Story of 40-man Turkish task force who must defend a relay station.",\
 "Spinal Tap, one of England's loudest bands, is chronicled by film director Marty DiBergi on what proves to be a fateful tour.",\
 "Oskar, an overlooked and bullied boy, finds love and revenge through Eli, a beautiful but peculiar girl."]

```

```python
descriptions_embeddings = list(
    dense_embedding_model.embed(descriptions)
)

```

Let’s upload the embeddings to Qdrant.

Qdrant Client offers a simple in-memory mode, allowing you to experiment locally with small data volumes.

Alternatively, you can use [a free cluster](https://qdrant.tech/documentation/cloud/create-cluster/#create-a-cluster) in Qdrant Cloud for experiments.

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(":memory:")  # Qdrant is running from RAM.

```

Let’s create a [collection](https://qdrant.tech/documentation/concepts/collections/) with our movie data.

```python
client.create_collection(
    collection_name="movies",
    vectors_config={
        "embedding": models.VectorParams(
            size=client.get_embedding_size("sentence-transformers/all-MiniLM-L6-v2"),
            distance=models.Distance.COSINE
        )
    }
)

```

And upload the embeddings to it.

```python
client.upload_points(
    collection_name="movies",
    points=[\
        models.PointStruct(\
            id=idx,\
            payload={"description": description},\
            vector={"embedding": vector}\
        )\
        for idx, (description, vector) in enumerate(\
            zip(descriptions, descriptions_embeddings)\
        )\
    ],
)

```

Upload with implicit embeddings computation

```python
client.upload_points(
    collection_name="movies",
    points=[\
        models.PointStruct(\
            id=idx,\
            payload={"description": description},\
            vector={"embedding": models.Document(text=description, model=encoder_name)},\
        )\
        for idx, description in enumerate(descriptions)\
    ],
)

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/\#first-stage-retrieval) First-stage retrieval

Let’s see how relevant the results will be using only an `all-MiniLM-L6-v2`-based dense retriever.

```python
query = "A story about a strong historically significant female figure."
query_embedded = list(dense_embedding_model.query_embed(query))[0]

initial_retrieval = client.query_points(
    collection_name="movies",
    using="embedding",
    query=query_embedded,
    with_payload=True,
    limit=10
)

description_hits = []
for i, hit in enumerate(initial_retrieval.points):
    print(f'Result number {i+1} is \"{hit.payload["description"]}\"')
    description_hits.append(hit.payload["description"])

```

Query points with implicit embeddings computation

```python
query = "A story about a strong historically significant female figure."

initial_retrieval = client.query_points(
    collection_name="movies",
    using="embedding",
    query=models.Document(text=query, model=encoder_name),
    with_payload=True,
    limit=10
)

```

The result is as follows:

```bash
Result number 1 is "A world-weary political journalist picks up the story of a woman's search for her son, who was taken away from her decades ago after she became pregnant and was forced to live in a convent."
Result number 2 is "Exiled into the dangerous forest by her wicked stepmother, a princess is rescued by seven dwarf miners who make her part of their household."
...
Result number 9 is "A biopic detailing the 2 decades that Punjabi Sikh revolutionary Udham Singh spent planning the assassination of the man responsible for the Jallianwala Bagh massacre."
Result number 10 is "In 1431, Jeanne d'Arc is placed on trial on charges of heresy. The ecclesiastical jurists attempt to force Jeanne to recant her claims of holy visions."

```

We can see that the description of _“The Messenger: The Story of Joan of Arc”_, which is the most fitting, appears 10th in the results.

Let’s try refining the order of the retrieved subset with `Jina Reranker v2`. It takes a query and a set of documents (movie descriptions) as input and calculates a relevance score based on token-level interactions between the query and each document.

```python
new_scores = list(
    reranker.rerank(query, description_hits)
)  # returns scores between query and each document

ranking = [\
    (i, score) for i, score in enumerate(new_scores)\
]  # saving document indices
ranking.sort(
    key=lambda x: x[1], reverse=True
)  # sorting them in order of relevance defined by reranker

for i, rank in enumerate(ranking):
    print(f'''Reranked result number {i+1} is \"{description_hits[rank[0]]}\"''')

```

The reranker moves the desired movie to the first position based on relevance.

```bash
Reranked result number 1 is "In 1431, Jeanne d'Arc is placed on trial on charges of heresy. The ecclesiastical jurists attempt to force Jeanne to recant her claims of holy visions."
Reranked result number 2 is "Exiled into the dangerous forest by her wicked stepmother, a princess is rescued by seven dwarf miners who make her part of their household."
...
Reranked result number 9 is "An ordinary word processor has the worst night of his life after he agrees to visit a girl in Soho whom he met that evening at a coffee shop."
Reranked result number 10 is "A biopic detailing the 2 decades that Punjabi Sikh revolutionary Udham Singh spent planning the assassination of the man responsible for the Jallianwala Bagh massacre."

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/\#conclusion) Conclusion

Rerankers refine search results by reordering retrieved candidates through deeper semantic analysis. For efficiency, they should be applied **only to a small subset of retrieved results**.

Balance speed and accuracy in search by leveraging the power of rerankers!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-rerankers.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-rerankers.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575151292&cv=11&fst=1748575151292&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-rerankers%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Reranking%20with%20FastEmbed%20-%20Qdrant&npa=0&pscdl=noapi&auid=836694263.1748575151&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575151266&cv=11&fst=1748575151266&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-rerankers%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Reranking%20with%20FastEmbed%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=836694263.1748575151&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8f9b2876-4f1e-420c-a9c4-703d04d3490a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5718aaa9-f889-4305-8eaa-d094bc545b11&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-rerankers%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8f9b2876-4f1e-420c-a9c4-703d04d3490a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5718aaa9-f889-4305-8eaa-d094bc545b11&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-rerankers%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575153018&cv=11&fst=1748575153018&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-rerankers%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Reranking%20with%20FastEmbed%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=836694263.1748575151&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)