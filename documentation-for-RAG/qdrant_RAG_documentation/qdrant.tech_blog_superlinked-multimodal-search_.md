---
url: "https://qdrant.tech/blog/superlinked-multimodal-search/"
title: "Beyond Multimodal Vectors: Hotel Search With Superlinked and Qdrant - Qdrant"
---

0

# Beyond Multimodal Vectors: Hotel Search With Superlinked and Qdrant

Filip Makraduli, David Myriel

·

April 24, 2025

![Beyond Multimodal Vectors: Hotel Search With Superlinked and Qdrant](https://qdrant.tech/blog/superlinked-multimodal-search/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fsuperlinked-multimodal-search%2F&text=Beyond%20Multimodal%20Vectors:%20Hotel%20Search%20With%20Superlinked%20and%20Qdrant "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fsuperlinked-multimodal-search%2F "LinkedIn")

## [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#more-than-just-multimodal-search) More Than Just Multimodal Search?

AI has transformed how we find products, services, and content. Now users express needs in **natural language** and expect precise, tailored results.

For example, you might search for hotels in Paris with specific criteria:

![superlinked-search](https://qdrant.tech/blog/superlinked-multimodal-search/superlinked-search.png)

_“Affordable luxury hotels near Eiffel Tower with lots of good reviews and free parking.”_ This isn’t just a search query—it’s a complex set of interrelated preferences spanning multiple data types.

> In this blog, we’ll show you how we built [**The Hotel Search Demo**](https://hotel-search-recipe.superlinked.io/).

**Figure 1:** Superlinked generates vectors of different modalities which are indexed and served by Qdrant for fast, accurate hotel search.
![superlinked-hotel-search](https://qdrant.tech/blog/superlinked-multimodal-search/frontend.gif)

What makes this app particularly powerful is how it breaks down your natural language query into precise parameters. As you type your question at the top, you can observe the query parameters dynamically update in the left sidebar.

In this blog, we’ll show you how Qdrant and Superlinked combine **textual understanding**, **numerical reasoning**, and **categorical filtering** to create a seamless search experience that meets modern user expectations.

## [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#core-components) Core Components

**Figure 2:** In a typical search or RAG app, the embedding framework (Superlinked) combines your data and its metadata into vectors. They are ingested into a Qdrant collection and indexed.

![superlinked-architecture](https://qdrant.tech/blog/superlinked-multimodal-search/superlinked-architecture.png)

Superlinked makes search smarter by embedding data into specialized “spaces” designed for each type of attribute, rather than using a single embedding method for everything.

When a user queries **“Affordable luxury hotels near Eiffel Tower with lots of good reviews and free parking”**, Superlinked uses an LLM to do natural query understanding and set weights. These weights determine:

- Preference direction (negative for lower values, positive for higher values).
- Preference strength (higher numbers have stronger influence).
- Balance between different attributes (e.g., price\_weight: -1.0 and rating\_weight: 1.0 are balanced).

This flexibility with weights allows users to rapidly iterate, experiment, and implement business logic or context much faster than rebuilding entire search systems from scratch. Superlinked then applies mandatory hard filters to narrow results, then ranks them using weighted nearest neighbors search, providing nuanced, accurate results tailored to user preferences. All vectors are stored in Qdrant.

**SuperLinked Framework Setup:** Once you [**setup the Superlinked server**](https://github.com/superlinked/superlinked-recipes/tree/main/projects/hotel-search), most of the prototype work is done right out of the [**sample notebook**](https://github.com/superlinked/superlinked-recipes/blob/main/projects/hotel-search/notebooks/superlinked-queries.ipynb). Once ready, you can host from a GitHub repository and deploy via Actions.

**Qdrant Vector Database:** The easiest way to store vectors is to [**create a free Qdrant Cloud cluster**](https://cloud.qdrant.io/login?ajs_anonymous_id=a335857b-fc71-442e-b141-5096dd16bfca). We have simple docs that show you how to [**grab the API key**](https://qdrant.tech/documentation/quickstart-cloud/) and upsert your new vectors and run some basic searches. For this demo, we have deployed a live Qdrant Cloud cluster.

**OpenAI API Key:** For natural language queries and generating the weights you will need an OpenAI API key

### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#1-vector-spaces-the-building-blocks-of-intelligent-search) 1\. Vector Spaces: The Building Blocks of Intelligent Search

![superlinked-hotel-1](https://qdrant.tech/blog/superlinked-multimodal-search/superlinked-hotel-1.jpg)

At the heart of Superlinked’s innovation are [**Spaces**](https://docs.superlinked.com/concepts/overview) \- specialized vector embedding environments designed for different data types. Unlike conventional approaches that force all data into a single embedding format, these spaces respect the inherent characteristics of different data types.

In our demo, four distinct spaces work together: **Description**, **Rating**, **Price** and **Rating Count**. Here is how they are defined:

```python
# Text data is embedded using a specialized language model
description_space = sl.TextSimilaritySpace(
    text=hotel_schema.description,
    model=settings.text_embedder_name  # all-mpnet-base-v2
)

# Numerical data uses dedicated numerical embeddings with appropriate scaling
rating_space = sl.NumberSpace(
    hotel_schema.rating,
    min_value=0,
    max_value=10,
    mode=sl.Mode.MAXIMUM  # Linear scale for bounded ratings
)

price_space = sl.NumberSpace(
    hotel_schema.price,
    min_value=0,
    max_value=1000,
    mode=sl.Mode.MAXIMUM,
    scale=sl.LogarithmicScale()  # Log scale for prices that vary widely
)

rating_count_space = sl.NumberSpace(
    hotel_schema.rating_count,
    min_value=0,
    max_value=22500,
    mode=sl.Mode.MAXIMUM,
    scale=sl.LogarithmicScale()  # Log scale for wide-ranging review counts
)

```

What makes this powerful is that each space properly preserves the semantic relationships within its domain - all while allowing these different spaces to be combined into a cohesive search experience.

**Prices** are embedded to maintain their proportional relationships, **Text** embeddings capture semantic meanings, **Ratings** preserve their relative quality indicators, and the **Ratings Count** uses logarithmic scaling to properly weight the significance of review volume.

### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#2-beyond-multimodal-vector-search-the-full-picture) 2\. Beyond Multimodal Vector Search: The Full Picture

Both **Qdrant and Superlinked** support a rich multimodal search environment where different data types collaborate rather than compete. For our hotel demo, this means:

- **Text descriptions** are embedded using state-of-the-art language models that understand semantics.
- **Prices use** logarithmic scaling to properly handle a wide ranges of values.
- **Ratings** are embedded linearly to preserve their quality indicators.
- **Review counts** use logarithmic scaling to account for the diminishing returns of additional reviews.

Unlike approaches that stringify all data into text before embedding (resulting in unpredictable non-monotonic relationships between numbers), or systems that maintain separate indices for different attributes, Superlinked creates a unified search space where multiple attributes can be considered simultaneously with appropriate semantic relationships preserved.

The declaration of this unified index is remarkably straightforward:

```python
index = sl.Index(
    spaces=[\
        description_space,\
        price_space,\
        rating_space,\
        rating_count_space,\
    ],
    # Additional fields for hard filtering
    fields=[hotel_schema.city, hotel_schema.amenities, ...]
)

```

If you want to have a deeper understanding of the algorithm and how multi vector embeddings work, you can have a read in-depth in our [article.](https://links.superlinked.com/multi_attribute_search_qd)

### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#3-intelligent-query-processing-from-natural-language-to-results) 3\. Intelligent Query Processing: From Natural Language to Results

The query processing system in Superlinked simplifies the way search queries are built and executed. This system allows users to interact using natural language, which is then converted into multi-dimensional vector operations, thereby moving away from rigid query structures.

The query construction in the hotel demo demonstrates this power:

```python
query = (
    sl.Query(
        index,
        weights={
            price_space: sl.Param("price_weight", description=price_description),
            rating_space: sl.Param("rating_weight", description=rating_description),
            # Additional space weights...
        },
    )
    .find(hotel_schema)
    .similar(description_space.text, sl.Param("description"))
    .filter(hotel_schema.city.in_(sl.Param("city")))
    # Additional filters...
    .with_natural_query(natural_query=sl.Param("natural_query"))
)

```

#### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#breaking-down-the-query) Breaking Down the Query

![superlinked-query](https://qdrant.tech/blog/superlinked-multimodal-search/superlinked-query.svg)

This setup enables queries like _“Affordable luxury hotels near Eiffel Tower with lots of good reviews and free parking.”_ to be automatically translated into:

- A text similarity search for **“luxury”** and **“Eiffel Tower”** concepts
- Appropriate weighting for **“affordable” price** (lower range)
- Hard filtering for **“free parking”** as an amenity
- Search for **“lots” (rating count) + good reviews (rating)**

Unlike systems that rely on reranking after retrieval (which can miss relevant results if the initial retrieval is too restrictive) or metadata filters (which convert fuzzy preferences like “affordable” to rigid boundaries), this approach maintains the nuance of the search throughout the entire process.

### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#4-hybrid-search-reimagined-solving-the-modern-search-problem) 4\. Hybrid Search Reimagined: Solving the Modern Search Problem

Today’s search landscape is dominated by discussions of hybrid search - the combination of keyword matching for precision with vector search for semantic understanding. The hotel search demo takes this concept further by implementing a multimodal hybrid search method that spans not just text retrieval methods but entire data domains.

In the hotel search demo, we see hybrid search reimagined across multiple dimensions:

- Text hybrid search: Combining exact matching (for city names, amenity keywords) with semantic similarity (for concepts like “luxury” or “family-friendly”)
- Numerical hybrid search: Blending exact range filters (minimum/maximum price) with preference-based vector similarity (for concepts like “affordable” or “high-rated”)
- Categorical hybrid search: Integrating hard categorical constraints (must be in Paris) with soft preferences (prefer hotels with specific amenities)

This multi-dimensional hybrid approach solves challenges facing conventional search systems:

1. Single-modal vector search fails when queries span multiple data types
2. Traditional hybrid search still separates keyword and vector components, which means they have to be weighed appropriately
3. Separate storage per attribute forces complex result reconciliation that loses semantic nuance
4. Pure filtering approaches convert preferences into binary decisions, missing the “strength” of preference
5. Re-ranking strategies may lead to weaker initial retrieval, especially with broad queries

This unified approach maintains the semantic relationships of all attributes in a multi-dimensional search space, where preferences become weights rather than filters, and where hard constraints and soft preferences seamlessly coexist in the same query.

The result is a search experience that feels intuitive and “just works” - whether users are looking for “pet-friendly boutique hotels with good reviews near the city center” or “affordable family suites with pool access in resort areas” - because the system understands both the semantics and the relationships between different attributes of what users are asking for.

The hotel search demo showcases this vision in action, a glimpse into a future where search understands not just the words we use, but the complex, nuanced preferences they represent.

## [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#how-to-build-the-app) How to Build the App

For more details, [check out the repository](https://github.com/superlinked/hotel-search-recipe-qdrant).

Otherwise, you can clone the app:

```shell
git clone https://github.com/superlinked/hotel-search-recipe-qdrant.git

```

The backend is located under `superlinked_app`, while the frontend has to be built from `frontend_app`.

### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#deploy-the-backend) Deploy the Backend

Use `superlinked_app/.env-example` as a template, create `superlinked_app/.env` and set `OPENAI_API_KEY` required for Natural Query Interface, `QDRANT_URL` and `QDRANT_API_KEY` required for Qdrant Vector Database.

```shell
python3.11 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
APP_MODULE_PATH=superlinked_app python -m superlinked.server

```

It will take some time (depending on the network) to download the sentence-transformers model for the very first time.

API docs will be available at [localhost:8080/docs](http://localhost:8080/docs).

To ingest the dataset, run this command in your terminal:

```shell
curl -X 'POST' \
  'http://localhost:8080/data-loader/hotel/run' \
  -H 'accept: application/json' \
  -d ''

```

Please wait until the ingestion is finished. You will see the message.

#### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#inspecting-collections-in-qdrant-cloud-dashboard) Inspecting Collections in Qdrant Cloud Dashboard

Once your Superlinked vectors are ingested, log in to the Qdrant Cloud dashboard to navigate to **Collections** and select your `default` hotel collection.

![default-collection](https://qdrant.tech/blog/superlinked-multimodal-search/default-collection.png)

You can browse individual points under the **Data** tab to view payload metadata (price, rating, amenities) alongside their raw vector embeddings.

![collection-information](https://qdrant.tech/blog/superlinked-multimodal-search/collection-information.png)

In the **Collection Information** section, you can use the **Search** tab to apply metadata filters or search by vector. In the **Search Quality** section, you can also monitor performance metrics (throughput, latency).

When scaling up your app, go back to **Qdrant Cloud Dashboard** to configure autoscaling, backups, and snapshots. These options will keep your service reliable and cost-efficient.

### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#build-the-frontend) Build the Frontend

```shell
cd frontend_app
python3.11 -m venv .venv-frontend
. .venv-frontend/bin/activate
pip install -e .
python -m streamlit run app/frontend/main.py

```

The Frontend UI will be available at [localhost:8501](http://localhost:8501/).

![superlinked-hotel-search](https://qdrant.tech/blog/superlinked-multimodal-search/superlinked-hotel-search.png)

#### [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#superlinked-cli) Superlinked CLI

> **Note:** If you need Superlinked for larger scale projects, you can use **Superlinked Cloud**.

With ‘superlinked cli’, you will be able to run a Superlinked application at scale with components such as batch processing engine, logging and more. For more details contact the Superlinked team at: [superlinked.com](https://superlinked.typeform.com/to/LXMRzHWk?typeform-source=hotel-search-recipe).

## [Anchor](https://qdrant.tech/blog/superlinked-multimodal-search/\#materials) Materials

- [Superlinked GitHub Repository](https://github.com/superlinked/superlinked)
- [Superlinked Documentation](https://docs.superlinked.com/)
- [Qdrant Vector Database](https://qdrant.tech/)
- [Qdrant Documentation](https://qdrant.tech/documentation)
- [Qdrant Cloud](https://cloud.qdrant.io/)
- [Qdrant Discord Community](https://discord.gg/qdrant)

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=a335857b-fc71-442e-b141-5096dd16bfca)

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

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=2a502730f559561177f397e2c1b2cfa0&enableResponsiveStyles=true)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c79c0086-d1d3-4990-963e-2867fe211911&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=cd240dfd-23d9-43f5-8ff2-57cafdfca1e4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fsuperlinked-multimodal-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573933894&cv=11&fst=1748573933894&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fsuperlinked-multimodal-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Beyond%20Multimodal%20Vectors%3A%20Hotel%20Search%20With%20Superlinked%20and%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=1883385194.1748573934&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573933881&cv=11&fst=1748573933881&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308614&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fsuperlinked-multimodal-search%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Beyond%20Multimodal%20Vectors%3A%20Hotel%20Search%20With%20Superlinked%20and%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1883385194.1748573934&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573933967&cv=11&fst=1748573933967&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fsuperlinked-multimodal-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Beyond%20Multimodal%20Vectors%3A%20Hotel%20Search%20With%20Superlinked%20and%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1883385194.1748573934&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c79c0086-d1d3-4990-963e-2867fe211911&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=cd240dfd-23d9-43f5-8ff2-57cafdfca1e4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fsuperlinked-multimodal-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)