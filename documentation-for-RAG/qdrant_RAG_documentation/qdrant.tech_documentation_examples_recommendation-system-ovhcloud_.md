---
url: "https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/"
title: "Movie Recommendation System - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Movie Recommendation System

# [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#movie-recommendation-system) Movie Recommendation System

| Time: 120 min | Level: Advanced | Output: [GitHub](https://github.com/infoslack/qdrant-example/blob/main/HC-demo/HC-OVH.ipynb) |  |
| --- | --- | --- | --- |

In this tutorial, you will build a mechanism that recommends movies based on defined preferences. Vector databases like Qdrant are good for storing high-dimensional data, such as user and item embeddings. They can enable personalized recommendations by quickly retrieving similar entries based on advanced indexing techniques. In this specific case, we will use [sparse vectors](https://qdrant.tech/articles/sparse-vectors/) to create an efficient and accurate recommendation system.

**Privacy and Sovereignty:** Since preference data is proprietary, it should be stored in a secure and controlled environment. Our vector database can easily be hosted on [OVHcloud](https://ovhcloud.com/), our trusted [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) partner. This means that Qdrant can be run from your OVHcloud region, but the database itself can still be managed from within Qdrant Cloud’s interface. Both products have been tested for compatibility and scalability, and we recommend their [managed Kubernetes](https://www.ovhcloud.com/en/public-cloud/kubernetes/) service.

> To see the entire output, use our [notebook with complete instructions](https://github.com/infoslack/qdrant-example/blob/main/HC-demo/HC-OVH.ipynb).

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#components) Components

- **Dataset:** The [MovieLens dataset](https://grouplens.org/datasets/movielens/) contains a list of movies and ratings given by users.
- **Cloud:** [OVHcloud](https://ovhcloud.com/), with managed Kubernetes.
- **Vector DB:** [Qdrant Hybrid Cloud](https://hybrid-cloud.qdrant.tech/) running on [OVHcloud](https://ovhcloud.com/).

**Methodology:** We’re adopting a collaborative filtering approach to construct a recommendation system from the dataset provided. Collaborative filtering works on the premise that if two users share similar tastes, they’re likely to enjoy similar movies. Leveraging this concept, we’ll identify users whose ratings align closely with ours, and explore the movies they liked but we haven’t seen yet. To do this, we’ll represent each user’s ratings as a vector in a high-dimensional, sparse space. Using Qdrant, we’ll index these vectors and search for users whose ratings vectors closely match ours. Ultimately, we will see which movies were enjoyed by users similar to us.

![](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/architecture-diagram.png)

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#deploying-qdrant-hybrid-cloud-on-ovhcloud) Deploying Qdrant Hybrid Cloud on OVHcloud

[Service Managed Kubernetes](https://www.ovhcloud.com/en-in/public-cloud/kubernetes/), powered by OVH Public Cloud Instances, a leading European cloud provider. With OVHcloud Load Balancers and disks built in. OVHcloud Managed Kubernetes provides high availability, compliance, and CNCF conformance, allowing you to focus on your containerized software layers with total reversibility.

1. To start using managed Kubernetes on OVHcloud, follow the [platform-specific documentation](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/#ovhcloud).
2. Once your Kubernetes clusters are up, [you can begin deploying Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/).

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#prerequisites) Prerequisites

Download and unzip the MovieLens dataset:

```shell
mkdir -p data
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip -d data

```

The necessary \* libraries are installed using `pip`, including `pandas` for data manipulation, `qdrant-client` for interfacing with Qdrant, and `*-dotenv` for managing environment variables.

```python
!pip install -U  \
    pandas  \
    qdrant-client \
    *-dotenv

```

The `.env` file is used to store sensitive information like the Qdrant host URL and API key securely.

```shell
QDRANT_HOST
QDRANT_API_KEY

```

Load all environment variables into the setup:

```python
import os
from dotenv import load_dotenv
load_dotenv('./.env')

```

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#implementation) Implementation

Load the data from the MovieLens dataset into pandas DataFrames to facilitate data manipulation and analysis.

```python
from qdrant_client import QdrantClient, models
import pandas as pd

```

Load user data:

```python
users = pd.read_csv(
    'data/ml-1m/users.dat',
    sep='::',
    names=['user_id', 'gender', 'age', 'occupation', 'zip'],
    engine='*'
)
users.head()

```

Add movies:

```python
movies = pd.read_csv(
    'data/ml-1m/movies.dat',
    sep='::',
    names=['movie_id', 'title', 'genres'],
    engine='*',
    encoding='latin-1'
)
movies.head()

```

Finally, add the ratings:

```python
ratings = pd.read_csv(
    'data/ml-1m/ratings.dat',
    sep='::',
    names=['user_id', 'movie_id', 'rating', 'timestamp'],
    engine='*'
)
ratings.head()

```

### [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#normalize-the-ratings) Normalize the ratings

Sparse vectors can use advantage of negative values, so we can normalize ratings to have a mean of 0 and a standard deviation of 1. This normalization ensures that ratings are consistent and centered around zero, enabling accurate similarity calculations. In this scenario we can take into account movies that we don’t like.

```python
ratings.rating = (ratings.rating - ratings.rating.mean()) / ratings.rating.std()

```

To get the results:

```python
ratings.head()

```

### [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#data-preparation) Data preparation

Now you will transform user ratings into sparse vectors, where each vector represents ratings for different movies. This step prepares the data for indexing in Qdrant.

First, create a collection with configured sparse vectors. For sparse vectors, you don’t need to specify the dimension, because it’s extracted from the data automatically.

```python
from collections import defaultdict

user_sparse_vectors = defaultdict(lambda: {"values": [], "indices": []})

for row in ratings.itertuples():
    user_sparse_vectors[row.user_id]["values"].append(row.rating)
    user_sparse_vectors[row.user_id]["indices"].append(row.movie_id)

```

Connect to Qdrant and create a collection called **movielens**:

```python
client = QdrantClient(
    url = os.getenv("QDRANT_HOST"),
    api_key = os.getenv("QDRANT_API_KEY")
)

client.create_collection(
    "movielens",
    vectors_config={},
    sparse_vectors_config={
        "ratings": models.SparseVectorParams()
    }
)

```

Upload user ratings to the **movielens** collection in Qdrant as sparse vectors, along with user metadata. This step populates the database with the necessary data for recommendation generation.

```python
def data_generator():
    for user in users.itertuples():
        yield models.PointStruct(
            id=user.user_id,
            vector={
                "ratings": user_sparse_vectors[user.user_id]
            },
            payload=user._asdict()
        )

client.upload_points(
    "movielens",
    data_generator()
)

```

## [Anchor](https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/\#recommendations) Recommendations

Personal movie ratings are specified, where positive ratings indicate likes and negative ratings indicate dislikes. These ratings serve as the basis for finding similar users with comparable tastes.

Personal ratings are converted into a sparse vector representation suitable for querying Qdrant. This vector represents the user’s preferences across different movies.

Let’s try to recommend something for ourselves:

```
1 = Like
-1 = dislike

```

```python
# Search with movies[movies.title.str.contains("Matrix", case=False)].

my_ratings = {
    2571: 1,  # Matrix
    329: 1,   # Star Trek
    260: 1,   # Star Wars
    2288: -1, # The Thing
    1: 1,     # Toy Story
    1721: -1, # Titanic
    296: -1,  # Pulp Fiction
    356: 1,   # Forrest Gump
    2116: 1,  # Lord of the Rings
    1291: -1, # Indiana Jones
    1036: -1  # Die Hard
}

inverse_ratings = {k: -v for k, v in my_ratings.items()}

def to_vector(ratings):
    vector = models.SparseVector(
        values=[],
        indices=[]
    )
    for movie_id, rating in ratings.items():
        vector.values.append(rating)
        vector.indices.append(movie_id)
    return vector

```

Query Qdrant to find users with similar tastes based on the provided personal ratings. The search returns a list of similar users along with their ratings, facilitating collaborative filtering.

```python
results = client.query_points(
    "movielens",
    query=to_vector(my_ratings),
    using="ratings",
    with_vectors=True, # We will use those to find new movies
    limit=20
).points

```

Movie scores are computed based on how frequently each movie appears in the ratings of similar users, weighted by their ratings. This step identifies popular movies among users with similar tastes. Calculate how frequently each movie is found in similar users’ ratings

```python
def results_to_scores(results):
    movie_scores = defaultdict(lambda: 0)

    for user in results:
        user_scores = user.vector['ratings']
        for idx, rating in zip(user_scores.indices, user_scores.values):
            if idx in my_ratings:
                continue
            movie_scores[idx] += rating

    return movie_scores

```

The top-rated movies are sorted based on their scores and printed as recommendations for the user. These recommendations are tailored to the user’s preferences and aligned with their tastes. Sort movies by score and print top five:

```python
movie_scores = results_to_scores(results)
top_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

for movie_id, score in top_movies[:5]:
    print(movies[movies.movie_id == movie_id].title.values[0], score)

```

Result:

```text
Star Wars: Episode V - The Empire Strikes Back (1980) 20.02387858
Star Wars: Episode VI - Return of the Jedi (1983) 16.443184379999998
Princess Bride, The (1987) 15.840068229999996
Raiders of the Lost Ark (1981) 14.94489462
Sixth Sense, The (1999) 14.570322149999999

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/recommendation-system-ovhcloud.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/recommendation-system-ovhcloud.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574666440&cv=11&fst=1748574666440&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frecommendation-system-ovhcloud%2F&hn=www.googleadservices.com&frm=0&tiba=Movie%20Recommendation%20System%20-%20Qdrant&npa=0&pscdl=noapi&auid=1072728157.1748574666&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574666349&cv=11&fst=1748574666349&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frecommendation-system-ovhcloud%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Movie%20Recommendation%20System%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1072728157.1748574666&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=04efd9da-8236-487d-a634-2734171cfdee&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a66959c9-a674-4fa7-879c-477b52a76297&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frecommendation-system-ovhcloud%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=04efd9da-8236-487d-a634-2734171cfdee&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a66959c9-a674-4fa7-879c-477b52a76297&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frecommendation-system-ovhcloud%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574667656&cv=11&fst=1748574667656&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Frecommendation-system-ovhcloud%2F&hn=www.googleadservices.com&frm=0&tiba=Movie%20Recommendation%20System%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1072728157.1748574666&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)