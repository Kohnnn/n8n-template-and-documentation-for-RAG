---
url: "https://qdrant.tech/articles/distance-based-exploration/"
title: "Distance-based data exploration - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Distance-based data exploration

[Back to Data Exploration](https://qdrant.tech/articles/data-exploration/)

# Distance-based data exploration

Andrey Vasnetsov

·

March 11, 2025

![Distance-based data exploration](https://qdrant.tech/articles_data/distance-based-exploration/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#hidden-structure) Hidden Structure

When working with large collections of documents, images, or other arrays of unstructured data, it often becomes useful to understand the big picture.
Examining data points individually is not always the best way to grasp the structure of the data.

![Data visualization](https://qdrant.tech/articles_data/distance-based-exploration/no-context-data.png)

Datapoints without context, pretty much useless

As numbers in a table obtain meaning when plotted on a graph, visualising distances (similar/dissimilar) between unstructured data items can reveal hidden structures and patterns.

![Data visualization](https://qdrant.tech/articles_data/distance-based-exploration/data-on-chart.png)

Vizualized chart, very intuitive

There are many tools to investigate data similarity, and Qdrant’s [1.12 release](https://qdrant.tech/blog/qdrant-1.12.x/) made it much easier to start this investigation. With the new [Distance Matrix API](https://qdrant.tech/documentation/concepts/explore/#distance-matrix), Qdrant handles the most computationally expensive part of the process—calculating the distances between data points.

In many implementations, the distance matrix calculation was part of the clustering or visualization processes, requiring either brute-force computation or building a temporary index. With Qdrant, however, the data is already indexed, and the distance matrix can be computed relatively cheaply.

In this article, we will explore several methods for data exploration using the Distance Matrix API.

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#dimensionality-reduction) Dimensionality Reduction

Initially, we might want to visualize an entire dataset, or at least a large portion of it, at a glance. However, high-dimensional data cannot be directly visualized. We must apply dimensionality reduction techniques to convert data into a lower-dimensional representation while preserving important data properties.

In this article, we will use [UMAP](https://github.com/lmcinnes/umap) as our dimensionality reduction algorithm.

Here is a **very** simplified but intuitive explanation of UMAP:

1. _Randomly generate points in 2D space_: Assign a random 2D point to each high-dimensional point.
2. _Compute distance matrix for high-dimensional points_: Calculate distances between all pairs of points.
3. _Compute distance matrix for 2D points_: Perform similarly to step 2.
4. _Match both distance matrices_: Adjust 2D points to minimize differences.

![UMAP](https://qdrant.tech/articles_data/distance-based-exploration/umap.png)

Canonical example of UMAP results, [source](https://github.com/lmcinnes/umap?tab=readme-ov-file#performance-and-examples)

UMAP preserves the relative distances between high-dimensional points; the actual coordinates are not essential. If we already have the distance matrix, step 2 can be skipped entirely.

Let’s use Qdrant to calculate the distance matrix and apply UMAP.
We will use one of the default datasets perfect for experimenting in Qdrant– [Midjourney Styles dataset](https://midlibrary.io/).

Use this command to download and import the dataset into Qdrant:

```http
PUT /collections/midlib/snapshots/recover
{
  "location": "http://snapshots.qdrant.io/midlib.snapshot"
}

```

We also need to prepare our python enviroment:

```bash
pip install umap-learn seaborn matplotlib qdrant-client

```

Import the necessary libraries:

```python
# Used to talk to Qdrant
from qdrant_client import QdrantClient
# Package with original UMAP implementation
from umap import UMAP
# Python implementation for sparse matrices
from scipy.sparse import csr_matrix
# For vizualization
import seaborn as sns

```

Establish connection to Qdrant:

```python
client = QdrantClient("http://localhost:6333")

```

After this is done, we can compute the distance matrix:

```python

# Request distances matrix from Qdrant
# `_offsets` suffix defines a format of the output matrix.
result = client.search_matrix_offsets(
  collection_name="midlib",
  sample=1000, # Select a subset of the data, as the whole dataset might be too large
  limit=20, # For performance reasons, limit the number of closest neighbors to consider
)

# Convert distances matrix to python-native format
matrix = csr_matrix(
    (result.scores, (result.offsets_row, result.offsets_col))
)

# Make the matrix symmetric, as UMAP expects it.
# Distance matrix is always symmetric, but qdrant only computes half of it.
matrix = matrix + matrix.T

```

Now we can apply UMAP to the distance matrix:

```python
umap = UMAP(
    metric="precomputed", # We provide ready-made distance matrix
    n_components=2, # output dimension
    n_neighbors=20, # Same as the limit in the search_matrix_offsets
)

vectors_2d = umap.fit_transform(matrix)

```

That’s all that is needed to get the 2d representation of the data.

![UMAP on Midlib](https://qdrant.tech/articles_data/distance-based-exploration/umap-midlib.png)

UMAP applied to Midlib dataset

UMAP isn’t the only algorithm compatible with our distance matrix API. For example, `scikit-learn` also offers:

- [Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html) \- Non-linear dimensionality reduction through Isometric Mapping.
- [SpectralEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html) \- Forms an affinity matrix given by the specified function and applies spectral decomposition to the corresponding graph Laplacian.
- [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) \- well-known algorithm for dimensionality reduction.

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#clustering) Clustering

Another approach to data structure understanding is clustering–grouping similar items.

_Note that there’s no universally best clustering criterion or algorithm._

![Clustering](https://qdrant.tech/articles_data/distance-based-exploration/clustering.png)

Clustering example, [source](https://scikit-learn.org/)

Many clustering algorithms accept precomputed distance matrix as input, so we can use the same distance matrix we calculated before.

Let’s consider a simple example of clustering the Midlib dataset with **KMeans algorithm**.

From [scikit-learn.cluster documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) we know that `fit()` method of KMeans algorithm prefers as an input:

> `X : {array-like, sparse matrix} of shape (n_samples, n_features)`:
>
> Training instances to cluster. It must be noted that the data will be converted to C ordering, which will cause a memory copy if the given data is not C-contiguous. If a sparse matrix is passed, a copy will be made if it’s not in CSR format.

So we can re-use `matrix` from the previous example:

```python
from sklearn.cluster import KMeans

# Initialize KMeans with 10 clusters
kmeans = KMeans(n_clusters=10)

# Generate index of the cluster each sample belongs to
cluster_labels = kmeans.fit_predict(matrix)

```

With this simple code, we have clustered the data into 10 clusters, while the main CPU-intensive part of the process was done by Qdrant.

![Clustering on Midlib](https://qdrant.tech/articles_data/distance-based-exploration/clustering-midlib.png)

Clustering applied to Midlib dataset

How to plot this chart

```python
sns.scatterplot(
    # Coordinates obtained from UMAP
    x=vectors_2d[:, 0], y=vectors_2d[:, 1],
    # Color datapoints by cluster
    hue=cluster_labels,
    palette=sns.color_palette("pastel", 10),
    legend="full",
)

```

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#graphs) Graphs

Clustering and dimensionality reduction both aim to provide a more transparent overview of the data.
However, they share a common characteristic - they require a training step before the results can be visualized.

This also implies that introducing new data points necessitates re-running the training step, which may be computationally expensive.

Graphs offer an alternative approach to data exploration, enabling direct, interactive visualization of relationships between data points.
In a graph representation, each data point is a node, and similarities between data points are represented as edges connecting the nodes.

Such a graph can be rendered in real-time using [force-directed layout](https://en.wikipedia.org/wiki/Force-directed_graph_drawing) algorithms, which aim to minimize the system’s energy by repositioning nodes dynamically–the more similar the data points are, the stronger the edges between them.

Adding new data points to the graph is as straightforward as inserting new nodes and edges without the need to re-run any training steps.

In practice, rendering a graph for an entire dataset at once may be computationally expensive and overwhelming for the user. Therefore, let’s explore a few strategies to address this issue.

### [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#expanding-from-a-single-node) Expanding from a single node

This is the simplest approach, where we start with a single node and expand the graph by adding the most similar nodes to the graph.

![Graph](https://qdrant.tech/articles_data/distance-based-exploration/graph.gif)

Graph representation of the data

### [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#sampling-from-a-collection) Sampling from a collection

Expanding a single node works well if you want to explore neighbors of a single point, but what if you want to explore the whole dataset?
If your dataset is small enough, you can render relations for all the data points at once. But it is a rare case in practice.

Instead, we can sample a subset of the data and render the graph for this subset.
This way, we can get a good overview of the data without overwhelming the user with too much information.

Let’s try to do so in [Qdrant’s Graph Exploration Tool](https://qdrant.tech/blog/qdrant-1.11.x/#web-ui-graph-exploration-tool):

```json
{
  "limit": 5, # node neighbors to consider
  "sample": 100 # nodes
}

```

![Graph](https://qdrant.tech/articles_data/distance-based-exploration/graph-sampled.png)

Graph representation of the data ( [Qdrant’s Graph Exploration Tool](https://qdrant.tech/blog/qdrant-1.11.x/#web-ui-graph-exploration-tool))

This graph captures some high-level structure of the data, but as you might have noticed, it is quite noisy.
This is because the differences in similarities are relatively small, and they might be overwhelmed by the stretches and compressions of the force-directed layout algorithm.

To make the graph more readable, let’s concentrate on the most important similarities and build a so called [Minimum/Maximum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree).

```json
{
  "limit": 5,
  "sample": 100,
  "tree": true
}

```

![Graph](https://qdrant.tech/articles_data/distance-based-exploration/spanning-tree.png)

Spanning tree of the graph ( [Qdrant’s Graph Exploration Tool](https://qdrant.tech/blog/qdrant-1.11.x/#web-ui-graph-exploration-tool))

This algorithm will only keep the most important edges and remove the rest while keeping the graph connected.
By doing so, we can reveal clusters of the data and the most important relations between them.

In some sense, this is similar to hierarchical clustering, but with the ability to interactively explore the data.
Another analogy might be a dynamically constructed mind map.

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#conclusion) Conclusion

Vector similarity goes beyond looking up the nearest neighbors–it provides a powerful tool for data exploration.
Many algorithms can construct human-readable data representations, and Qdrant makes using them easy.

Several data exploration instruments are available in the Qdrant Web UI ( [Visualization and Graph Exploration Tools](https://qdrant.tech/articles/web-ui-gsoc/)), and for more advanced use cases, you could directly utilise our distance matrix API.

Try it with your data and see what hidden structures you can reveal!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/distance-based-exploration.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/distance-based-exploration.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575299222&cv=11&fst=1748575299222&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdistance-based-exploration%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Distance-based%20data%20exploration%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=632581765.1748575299&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575299315&cv=11&fst=1748575299315&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdistance-based-exploration%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Distance-based%20data%20exploration%20-%20Qdrant&npa=0&pscdl=noapi&auid=632581765.1748575299&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=6c4d535f-8050-4206-97c2-06ac08865326&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=91beedae-47e1-4fbf-9c53-18c2cd0308d3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdistance-based-exploration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=6c4d535f-8050-4206-97c2-06ac08865326&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=91beedae-47e1-4fbf-9c53-18c2cd0308d3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdistance-based-exploration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575300426&cv=11&fst=1748575300426&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdistance-based-exploration%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Distance-based%20data%20exploration%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=632581765.1748575299&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)