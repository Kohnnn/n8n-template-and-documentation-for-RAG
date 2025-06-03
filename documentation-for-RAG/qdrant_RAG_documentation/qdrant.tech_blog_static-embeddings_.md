---
url: "https://qdrant.tech/blog/static-embeddings/"
title: "Static Embeddings: should you pay attention? - Qdrant"
---

0

# Static Embeddings: should you pay attention?

Kacper Łukawski

·

January 17, 2025

![Static Embeddings: should you pay attention?](https://qdrant.tech/blog/static-embeddings/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fstatic-embeddings%2F&text=Static%20Embeddings:%20should%20you%20pay%20attention? "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fstatic-embeddings%2F "LinkedIn")

In the world of resource-constrained computing, a quiet revolution is taking place. While transformers dominate
leaderboards with their impressive capabilities, static embeddings are making an unexpected comeback, offering
remarkable speed improvements with surprisingly small quality trade-offs. **We evaluated how Qdrant users can benefit**
**from this renaissance, and the results are promising**.

## [Anchor](https://qdrant.tech/blog/static-embeddings/\#what-makes-static-embeddings-different) What makes static embeddings different?

Transformers are often seen as the only way to go when it comes to embeddings. The use of attention mechanisms helps to
capture the relationships between the input tokens, so each token gets a vector representation that is context-aware
and defined not only by the token itself but also by the surrounding tokens. Transformer-based models easily beat the
quality of the older methods, such as word2vec or GloVe, which could only create a single vector embedding per each
word. As a result, the word “bank” would have identical representation in the context of “river bank” and “financial
institution”.

![Static embeddings](https://qdrant.tech/blog/static-embeddings/financial-river-bank.png)

Transformer-based models would represent the word “bank” differently in each of the contexts. However, transformers come
with a cost. They are computationally expensive and usually require a lot of memory, although the embeddings models
usually have fewer parameters than the Large Language Models. Still, GPUs are preferred to be used, even for inference.

Static embeddings are still a thing, though! [MinishLab](https://minishlab.github.io/) introduced their [model2vec\\
technique](https://huggingface.co/blog/Pringled/model2vec) in October 2024, achieving a remarkable 15x reduction in
model size and up to 500x speed increase while maintaining impressive performance levels. Their idea was to distill the
knowledge from the transformer-based sentence transformer and create a static embedding model that would be much faster
and less memory-consuming. This introduction seems to be a catalyst for the static embeddings renaissance, as we can see
static embeddings to be integrated even into popular [Sentence Transformers](https://www.sbert.net/) library. The
[recent blog post on the Hugging Face blog](https://huggingface.co/blog/static-embeddings) by [Tom\\
Aarsen](https://www.tomaarsen.com/) reveals how to train a static embedding model using Sentence Transformers and still
get up to 85% of transformer-level quality at a fraction of computational cost. The blog post also introduces an
embedding model for English text retrieval, which is called `static-retrieval-mrl-en-v1`.

## [Anchor](https://qdrant.tech/blog/static-embeddings/\#static-embeddings-in-qdrant) Static embeddings in Qdrant

From the vector database perspective, static embeddings are not different from any other embedding models. They are
dense vectors after all, and you can simply store them in a Qdrant collection. Here is how you do it with the
`sentence-transformers/static-retrieval-mrl-en-v1` model:

```python
import uuid

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models

# The model produces vectors of size 1024
model = SentenceTransformer(
    "sentence-transformers/static-retrieval-mrl-en-v1"
)

# Let's assume we have a collection "my_collection"
# with a single vector called "static"
client = QdrantClient("http://localhost:6333")

# Calling the sentence transformer model to encode
# the text is not different compared to any other model
client.upsert(
    "my_collection",
    points=[\
        models.PointStruct(\
            id=uuid.uuid4().hex,\
            vector=model.encode("Hello, world!"),\
            payload={"static": "Hello, world!"},\
        )\
    ]
)

```

The retrieval is not going to be any faster just because you use static embeddings. However, **you will experience a**
**huge speedup in creating the vectors from your data**, what is usually a bottleneck. The Hugging Face blog post mentions
that the model might be even up to 400x faster on a CPU than the state-of-the-art embedding model.

We didn’t perform any proper benchmarking of the encoding speed, but one of the experiments done on `TREC-COVID` dataset
from [BeIR](https://github.com/beir-cellar/beir) shows that we can **encode and fully index 171K documents in Qdrant in**
**around 7.5 minutes**. All of it done on a consumer-grade laptop, without GPU acceleration.

## [Anchor](https://qdrant.tech/blog/static-embeddings/\#quantization-of-the-static-embeddings) Quantization of the static embeddings

What can actually make the retrieval faster is the use of Matryoshka Embeddings, as the `static-retrieval-mrl-en-v1`
model was trained with that technique in mind. However, that’s not the only way to speed up search. Quantization
methods are really popular among our users, and we were curious to check if they might be applied to the static
embeddings with the same success.

We took the `static-retrieval-mrl-en-v1` model and tested it on various subsets of
[BeIR](https://github.com/beir-cellar/beir) with and without Binary Quantization, to see how much if affects the
retrieval quality. The results are really promising, as shown in our NDCG@10 measurements (a metric that evaluates the
ranking quality of search results, with higher scores indicating better performance):

|  | NDCG@10 |
| --- | --- |
| Dataset | Original vectors | Binary Quantization, no rescoring |
| --- | --- | --- |
| SciFact | 0.59348 | 0.54195 |
| TREC-COVID | 0.4428 | 0.44185 |
| ArguAna | 0.44393 | 0.42164 |
| NFCorpus | 0.30045 | 0.28027 |

Binary Quantization definitely speeds up the retrieval, and make it cheaper, but also seems not to affect the quality of
the retrieval much in some cases. **However, that’s something you should carefully verify on your own data**. If you are
a Qdrant user, then you can just enable quantization on an existing collection and [measure the impact on the retrieval\\
quality](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/).

All the tests we did were performed using [`beir-qdrant`](https://github.com/kacperlukawski/beir-qdrant), and might be
reproduced by running [the script available on the project\\
repo](https://github.com/kacperlukawski/beir-qdrant/blob/main/examples/retrieval/search/evaluate_static_embeddings.py).

## [Anchor](https://qdrant.tech/blog/static-embeddings/\#who-should-use-static-embeddings) Who should use static embeddings?

Static embeddings seem to be a budget-friendly option for those who would like to use semantic search in their
applications, but can’t afford hosting standard representation models, or cannot do it, i.e. due to hardware
constraints. Some of the use cases might be:

- **Mobile applications** \- although many smartphones have powerful CPUs or even GPUs, the battery life is still a
concern, and the static embeddings might be a good compromise between the quality and the power consumption. Moreover,
the static embeddings can be used in the applications that require offline mode.
- **Web browser extensions** \- running a transformer-based model in a web browser is usually not quite an option, but
static embeddings might be a good choice, as they have fewer parameters and are faster to encode.
- **Embedded systems** \- the static embeddings might be a good choice for the devices with limited computational power,
such as IoT devices or microcontrollers.

If you are one of the above, then you should definitely give static embeddings a try. **However, if the search quality**
**is not the top of your priorities, then you might consider using static embeddings even in the high-performance**
**environments**. The speedup in the encoding process might be a game-changer for you.

### [Anchor](https://qdrant.tech/blog/static-embeddings/\#customization-of-the-static-embeddings) Customization of the static embeddings

Last, but not least. The training pipeline published by [Tom Aarsen](https://www.tomaarsen.com/) can help you to train
your own static embeddings models, so **you can adjust it the specifics of your data easily**. This training process
will also be way faster than for a transformer-based model, so you can even retrain it more often. Recomputing the
embeddings is a bottleneck of the semantic search systems, and the static embeddings might be a good solution to this
problem. Whether a custom static embedding model can beat a general pre-trained model remains an open question, but it’s
definitely worth trying.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup)

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