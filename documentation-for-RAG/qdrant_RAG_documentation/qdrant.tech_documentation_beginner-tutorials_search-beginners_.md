---
url: "https://qdrant.tech/documentation/beginner-tutorials/search-beginners/"
title: "Semantic Search 101 - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Beginner tutorials](https://qdrant.tech/documentation/beginner-tutorials/)
- Semantic Search 101

# [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#build-your-first-semantic-search-engine-in-5-minutes) Build Your First Semantic Search Engine in 5 Minutes

| Time: 5 - 15 min | Level: Beginner |  |  |
| --- | --- | --- | --- |

Qdrant Tutorial - Semantic Search for Beginners - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Qdrant Tutorial - Semantic Search for Beginners](https://www.youtube.com/watch?v=AASiqmtKo54)

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

[Watch on](https://www.youtube.com/watch?v=AASiqmtKo54&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 5:18
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=AASiqmtKo54 "Watch on YouTube")

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#overview) Overview

If you are new to vector databases, this tutorial is for you. In 5 minutes you will build a semantic search engine for science fiction books. After you set it up, you will ask the engine about an impending alien threat. Your creation will recommend books as preparation for a potential space attack.

Before you begin, you need to have a [recent version of Python](https://www.python.org/downloads/) installed. If you don’t know how to run this code in a virtual environment, follow Python documentation for [Creating Virtual Environments](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) first.

This tutorial assumes you’re in the bash shell. Use the Python documentation to activate a virtual environment, with commands such as:

```bash
source tutorial-env/bin/activate

```

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#1-installation) 1\. Installation

You need to process your data so that the search engine can work with it. The [Sentence Transformers](https://www.sbert.net/) framework gives you access to common Large Language Models that turn raw data into embeddings.

```bash
pip install -U sentence-transformers

```

Once encoded, this data needs to be kept somewhere. Qdrant lets you store data as embeddings. You can also use Qdrant to run search queries against this data. This means that you can ask the engine to give you relevant answers that go way beyond keyword matching.

```bash
pip install -U qdrant-client

```

### [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#import-the-models) Import the models

Once the two main frameworks are defined, you need to specify the exact models this engine will use.

```python
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

```

The [Sentence Transformers](https://www.sbert.net/) framework contains many embedding models. We’ll take [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) as it has a good balance between speed and embedding quality for this tutorial.

```python
encoder = SentenceTransformer("all-MiniLM-L6-v2")

```

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#2-add-the-dataset) 2\. Add the dataset

[all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) will encode the data you provide. Here you will list all the science fiction books in your library. Each book has metadata, a name, author, publication year and a short description.

```python
documents = [\
    {\
        "name": "The Time Machine",\
        "description": "A man travels through time and witnesses the evolution of humanity.",\
        "author": "H.G. Wells",\
        "year": 1895,\
    },\
    {\
        "name": "Ender's Game",\
        "description": "A young boy is trained to become a military leader in a war against an alien race.",\
        "author": "Orson Scott Card",\
        "year": 1985,\
    },\
    {\
        "name": "Brave New World",\
        "description": "A dystopian society where people are genetically engineered and conditioned to conform to a strict social hierarchy.",\
        "author": "Aldous Huxley",\
        "year": 1932,\
    },\
    {\
        "name": "The Hitchhiker's Guide to the Galaxy",\
        "description": "A comedic science fiction series following the misadventures of an unwitting human and his alien friend.",\
        "author": "Douglas Adams",\
        "year": 1979,\
    },\
    {\
        "name": "Dune",\
        "description": "A desert planet is the site of political intrigue and power struggles.",\
        "author": "Frank Herbert",\
        "year": 1965,\
    },\
    {\
        "name": "Foundation",\
        "description": "A mathematician develops a science to predict the future of humanity and works to save civilization from collapse.",\
        "author": "Isaac Asimov",\
        "year": 1951,\
    },\
    {\
        "name": "Snow Crash",\
        "description": "A futuristic world where the internet has evolved into a virtual reality metaverse.",\
        "author": "Neal Stephenson",\
        "year": 1992,\
    },\
    {\
        "name": "Neuromancer",\
        "description": "A hacker is hired to pull off a near-impossible hack and gets pulled into a web of intrigue.",\
        "author": "William Gibson",\
        "year": 1984,\
    },\
    {\
        "name": "The War of the Worlds",\
        "description": "A Martian invasion of Earth throws humanity into chaos.",\
        "author": "H.G. Wells",\
        "year": 1898,\
    },\
    {\
        "name": "The Hunger Games",\
        "description": "A dystopian society where teenagers are forced to fight to the death in a televised spectacle.",\
        "author": "Suzanne Collins",\
        "year": 2008,\
    },\
    {\
        "name": "The Andromeda Strain",\
        "description": "A deadly virus from outer space threatens to wipe out humanity.",\
        "author": "Michael Crichton",\
        "year": 1969,\
    },\
    {\
        "name": "The Left Hand of Darkness",\
        "description": "A human ambassador is sent to a planet where the inhabitants are genderless and can change gender at will.",\
        "author": "Ursula K. Le Guin",\
        "year": 1969,\
    },\
    {\
        "name": "The Three-Body Problem",\
        "description": "Humans encounter an alien civilization that lives in a dying system.",\
        "author": "Liu Cixin",\
        "year": 2008,\
    },\
]

```

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#3-define-storage-location) 3\. Define storage location

You need to tell Qdrant where to store embeddings. This is a basic demo, so your local computer will use its memory as temporary storage.

```python
client = QdrantClient(":memory:")

```

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#4-create-a-collection) 4\. Create a collection

All data in Qdrant is organized by collections. In this case, you are storing books, so we are calling it `my_books`.

```python
client.create_collection(
    collection_name="my_books",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

```

- The `vector_size` parameter defines the size of the vectors for a specific collection. If their size is different, it is impossible to calculate the distance between them. 384 is the encoder output dimensionality. You can also use model.get\_sentence\_embedding\_dimension() to get the dimensionality of the model you are using.

- The `distance` parameter lets you specify the function used to measure the distance between two points.


## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#5-upload-data-to-collection) 5\. Upload data to collection

Tell the database to upload `documents` to the `my_books` collection. This will give each record an id and a payload. The payload is just the metadata from the dataset.

```python
client.upload_points(
    collection_name="my_books",
    points=[\
        models.PointStruct(\
            id=idx, vector=encoder.encode(doc["description"]).tolist(), payload=doc\
        )\
        for idx, doc in enumerate(documents)\
    ],
)

```

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#6--ask-the-engine-a-question) 6\. Ask the engine a question

Now that the data is stored in Qdrant, you can ask it questions and receive semantically relevant results.

```python
hits = client.query_points(
    collection_name="my_books",
    query=encoder.encode("alien invasion").tolist(),
    limit=3,
).points

for hit in hits:
    print(hit.payload, "score:", hit.score)

```

**Response:**

The search engine shows three of the most likely responses that have to do with the alien invasion. Each of the responses is assigned a score to show how close the response is to the original inquiry.

```text
{'name': 'The War of the Worlds', 'description': 'A Martian invasion of Earth throws humanity into chaos.', 'author': 'H.G. Wells', 'year': 1898} score: 0.570093257022374
{'name': "The Hitchhiker's Guide to the Galaxy", 'description': 'A comedic science fiction series following the misadventures of an unwitting human and his alien friend.', 'author': 'Douglas Adams', 'year': 1979} score: 0.5040468703143637
{'name': 'The Three-Body Problem', 'description': 'Humans encounter an alien civilization that lives in a dying system.', 'author': 'Liu Cixin', 'year': 2008} score: 0.45902943411768216

```

### [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#narrow-down-the-query) Narrow down the query

How about the most recent book from the early 2000s?

```python
hits = client.query_points(
    collection_name="my_books",
    query=encoder.encode("alien invasion").tolist(),
    query_filter=models.Filter(
        must=[models.FieldCondition(key="year", range=models.Range(gte=2000))]
    ),
    limit=1,
).points

for hit in hits:
    print(hit.payload, "score:", hit.score)

```

**Response:**

The query has been narrowed down to one result from 2008.

```text
{'name': 'The Three-Body Problem', 'description': 'Humans encounter an alien civilization that lives in a dying system.', 'author': 'Liu Cixin', 'year': 2008} score: 0.45902943411768216

```

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/search-beginners/\#next-steps) Next Steps

Congratulations, you have just created your very first search engine! Trust us, the rest of Qdrant is not that complicated, either. For your next tutorial you should try building an actual [Neural Search Service with a complete API and a dataset](https://qdrant.tech/documentation/tutorials/neural-search/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/search-beginners.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/search-beginners.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0993f1c3-cfef-45c6-97ee-20b43185aece&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=27578505-b291-48a9-a4fc-1ad6d8c8ef49&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fbeginner-tutorials%2Fsearch-beginners%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0993f1c3-cfef-45c6-97ee-20b43185aece&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=27578505-b291-48a9-a4fc-1ad6d8c8ef49&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fbeginner-tutorials%2Fsearch-beginners%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)