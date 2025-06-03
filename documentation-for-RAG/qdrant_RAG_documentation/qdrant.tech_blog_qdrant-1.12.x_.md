---
url: "https://qdrant.tech/blog/qdrant-1.12.x/"
title: "Qdrant 1.12 - Distance Matrix, Facet Counting & On-Disk Indexing - Qdrant"
---

0

# Qdrant 1.12 - Distance Matrix, Facet Counting & On-Disk Indexing

David Myriel

·

October 08, 2024

![Qdrant 1.12 - Distance Matrix, Facet Counting & On-Disk Indexing](https://qdrant.tech/blog/qdrant-1.12.x/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.12.x%2F&text=Qdrant%201.12%20-%20Distance%20Matrix,%20Facet%20Counting%20&%20On-Disk%20Indexing "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.12.x%2F "LinkedIn")

[**Qdrant 1.12.0 is out!**](https://github.com/qdrant/qdrant/releases/tag/v1.12.0) Let’s look at major new features and a few minor additions:

**Distance Matrix API:** Efficiently calculate pairwise distances between vectors.

**GUI Data Exploration** Visually navigate your dataset and analyze vector relationships.

**Faceting API:** Dynamically aggregate and count unique values in specific fields.

**Text Index on disk:** Reduce memory usage by storing text indexing data on disk.

**Geo Index on disk:** Offload indexed geographic data on disk for memory efficiency.

## [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#distance-matrix-api-for-data-insights) Distance Matrix API for Data Insights

![distance-matrix-api](https://qdrant.tech/blog/qdrant-1.12.x/distance-matrix-api.png)

> **Qdrant** is a similarity search engine. Our mission is to give you the tools to **discover and understand connections** between vast amounts of semantically relevant data

The **Distance Matrix API** is here to lay the groundwork for such tools.

In data exploration, tasks like [**clustering**](https://en.wikipedia.org/wiki/DBSCAN) and [**dimensionality reduction**](https://en.wikipedia.org/wiki/Dimensionality_reduction) rely on calculating distances between data points.

**Use Case:** A retail company with 10,000 customers wants to segment them by purchasing behavior. Each customer is stored as a vector in Qdrant, but without a dedicated API, clustering would need 10,000 separate batch requests, making the process inefficient and costly.

You can use this API to compute a **sparse matrix of distances** that is optimized for large datasets. Then, you can filter through the retrieved data to find the exact vector relationships that matter.

In terms of endpoints, we offer two different formats to show results:

- **Pairs** are simple, intutitive and ideal for graph representation.
- **Offsets** are more complex, but also native when defining CSR sparse matrices.

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#output---pairs) Output - Pairs

Use the `pairs` endpoint to compare 10 random point pairs from your dataset:

```http
POST /collections/{collection_name}/points/search/matrix/pairs
{
    "sample": 10,
    "limit": 2
}

```

Configuring the `sample` will retrieve a random group of 10 points to compare. The `limit` is the number of semantic connections between points to consider.

Qdrant will list a sparse matrix of distances **between the closest pairs**:

```http
{
    "result": {
        "pairs": [\
            {"a": 1, "b": 3, "score": 1.4063001},\
            {"a": 1, "b": 4, "score": 1.2531},\
            {"a": 2, "b": 1, "score": 1.1550001},\
            {"a": 2, "b": 8, "score": 1.1359},\
            {"a": 3, "b": 1, "score": 1.4063001},\
            {"a": 3, "b": 4, "score": 1.2218001},\
            {"a": 4, "b": 1, "score": 1.2531},\
            {"a": 4, "b": 3, "score": 1.2218001},\
            {"a": 5, "b": 3, "score": 0.70239997},\
            {"a": 5, "b": 1, "score": 0.6146},\
            {"a": 6, "b": 3, "score": 0.6353},\
            {"a": 6, "b": 4, "score": 0.5093},\
            {"a": 7, "b": 3, "score": 1.0990001},\
            {"a": 7, "b": 1, "score": 1.0349001},\
            {"a": 8, "b": 2, "score": 1.1359},\
            {"a": 8, "b": 3, "score": 1.0553}\
        ]
    }
}

```

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#output---offsets) Output - Offsets

The `offsets` endpoint offer another format of showing the distance between points:

```http
POST /collections/{collection_name}/points/search/matrix/offsets
{
    "sample": 10,
    "limit": 2
}

```

Qdrant will return a compact representation of the distances between points in the **form of row and column offsets**.

Two arrays, `offsets_row` and `offsets_col`, represent the positions of non-zero distance values in the matrix. Each entry in these arrays corresponds to a pair of points with a calculated distance.

```http
{
    "result": {
        "offsets_row": [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
        "offsets_col": [2, 3, 0, 7, 0, 3, 0, 2, 2, 0, 2, 3, 2, 0, 1, 2],
        "scores": [\
            1.4063001, 1.2531, 1.1550001, 1.1359, 1.4063001,\
            1.2218001, 1.2531, 1.2218001, 0.70239997, 0.6146, 0.6353,\
            0.5093, 1.0990001, 1.0349001, 1.1359, 1.0553\
            ],
        "ids": [1, 2, 3, 4, 5, 6, 7, 8]
    }
}

```

_To learn more about the distance matrix, read [**The Distance Matrix documentation**](https://qdrant.tech/documentation/concepts/explore/#distance-matrix)._

## [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#distance-matrix-api-in-the-graph-ui) Distance Matrix API in the Graph UI

We are adding more visualization options to the [**Graph Exploration Tool**](https://qdrant.tech/blog/qdrant-1.11.x/#web-ui-graph-exploration-tool), introduced in v.1.11.

You can now leverage the **Distance Matrix API** from within this tool for a **clearer picture** of your data and its relationships.

**Example:** You can retrieve 900 `sample` points, with a `limit` of 5 connections per vector and a `tree` visualization:

```json
{
  "limit": 5,
  "sample": 900,
  "tree": true
}

```

The new graphing method is cleaner and reveals **relationships and outliers:**

![distance-matrix](https://qdrant.tech/blog/qdrant-1.12.x/distance-matrix.png)

_To learn more about the Web UI Dashboard, read the [**Interfaces documentation**](https://qdrant.tech/documentation/interfaces/web-ui/)._

## [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#facet-api-for-metadata-cardinality) Facet API for Metadata Cardinality

![facet-api](https://qdrant.tech/blog/qdrant-1.12.x/facet-api.png)

In modern applications like e-commerce, users often rely on [**filters**](https://qdrant.tech/articles/vector-search-filtering/), such as **brand** or **color**, to refine search results. The **Facet API** is designed to help users understand the distribution of values in a dataset.

The `facet` endpoint can efficiently count and aggregate values for a specific [**payload field**](https://qdrant.tech/documentation/concepts/payload/) in your dataset.

You can use it to retrieve unique values for a field, along with the number of points that contain each value. This functionality is similar to `GROUP BY` with `COUNT(*)` in SQL databases.

> **Note:** Facet counting can only be applied to fields that support `match` conditions, such as fields with a keyword index.

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#configuration) Configuration

Here’s a sample query using the REST API to facet on the `size` field, filtered by products where the `color` is red:

```http
POST /collections/{collection_name}/facet
{
    "key": "size",
    "filter": {
      "must": {
        "key": "color",
        "match": { "value": "red" }
      }
    }
}

```

This returns counts for each unique value in the `size` field, filtered by `color` = `red`:

```json
{
  "response": {
    "hits": [\
      {"value": "L", "count": 19},\
      {"value": "S", "count": 10},\
      {"value": "M", "count": 5},\
      {"value": "XL", "count": 1},\
      {"value": "XXL", "count": 1}\
    ]
  },
  "time": 0.0001
}

```

The results are sorted by count in descending order and only values with non-zero counts are returned.

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#configuration---precise-facet) Configuration - Precise Facet

By default, facet counting runs an approximate filter. If you need a precise count, you can enable the `exact` parameter:

```http
POST /collections/{collection_name}/facet
{
    "key": "size",
    "exact": true
}

```

This feature provides flexibility between performance and precision, depending on the needs of your application.

_To learn more about faceting, read the [**Facet API documentation**](https://qdrant.tech/documentation/concepts/payload/#facet-counts)._

## [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#text-index-on-disk-support) Text Index on Disk Support

![text-index-disk](https://qdrant.tech/blog/qdrant-1.12.x/text-index-disk.png)

[**Qdrant text indexing**](https://qdrant.tech/documentation/concepts/indexing/#full-text-index) tokenizes text into smaller units (tokens) based on chosen settings (e.g., tokenizer type, token length). These tokens are stored in an inverted index for fast text searches.

> With `on_disk` text indexing, the inverted index is stored on disk, reducing memory usage.

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#configuration-1) Configuration

Just like with other indexes, simply add `on_disk: true` when creating the index:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "review_text",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "min_token_len": 2,
        "max_token_len": 20,
        "lowercase": true,
        "on_disk": true
    }
}

```

_To learn more about indexes, read the [**Indexing documentation**](https://qdrant.tech/documentation/concepts/indexing/)._

## [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#geo-index-on-disk-support) Geo Index on Disk Support

For [**large-scale geographic datasets**](https://qdrant.tech/documentation/concepts/payload/#geo) where storing all indexes in memory is impractical, **geo indexing** allows efficient filtering of points based on geographic coordinates.

With `on_disk` geo indexing, the index is written to disk instead of residing in memory, making it possible to handle large datasets without exhausting system memory.

> This can be crucial when dealing with millions of geo points that don’t require real-time access.

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#configuration-2) Configuration

To enable this feature, modify the index schema for the geographic field by setting the `on_disk: true` flag.

```http
PUT /collections/{collection_name}/index
{
    "field_name": "location",
    "field_schema": {
        "type": "geo",
        "on_disk": true
    }
}

```

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#performance-considerations) Performance Considerations

- **Cold Query Latency:** On-disk indexes require I/O to load index segments, introducing slight latency on first access. Subsequent queries will benefit from disk caching.
- **Hot vs. Cold Indexes:** Fields frequently queried should stay in memory for faster performance, and on-disk indexes are better for large, infrequently queried fields.
- **Memory vs. Disk Trade-offs:** Users can manage memory by deciding which fields to store on disk.

![geo-index-disk](https://qdrant.tech/blog/qdrant-1.12.x/geo-index-disk.png)

> To learn how to get the best performance from Qdrant, read the [**Optimization Guide**](https://qdrant.tech/documentation/guides/optimize/).

## [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#just-the-beginning) Just the Beginning

The easiest way to reach that **Hello World** moment is to [**try vector search in a live cluster**](https://qdrant.tech/documentation/quickstart-cloud/). Our **interactive tutorial** will show you how to create a cluster, add data and try some filtering clauses.

**All of the new features from version 1.12 can be tested in the Web UI:**

![qdrant-filtering-tutorial](https://qdrant.tech/articles_data/vector-search-filtering/qdrant-filtering-tutorial.png)

### [Anchor](https://qdrant.tech/blog/qdrant-1.12.x/\#check-out-the-tutorial-video) Check Out the Tutorial Video

Visualizing Vector Embeddings: Qdrant’s WebUI Graph Tool - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Visualizing Vector Embeddings: Qdrant’s WebUI Graph Tool](https://www.youtube.com/watch?v=OzTHZ0SIulg)

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

[Watch on](https://www.youtube.com/watch?v=OzTHZ0SIulg&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 1:30
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=OzTHZ0SIulg "Watch on YouTube")

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=58025784-745b-4b20-ba88-91dbd4e62dff)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=3139c006-8b1c-423b-8702-8265309d9eea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0e35a8db-42e6-46c0-baf1-316b3eb7ff61&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.12.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=3139c006-8b1c-423b-8702-8265309d9eea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0e35a8db-42e6-46c0-baf1-316b3eb7ff61&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-1.12.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)