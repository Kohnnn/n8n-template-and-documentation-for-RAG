---
url: "https://qdrant.tech/articles/filtrable-hnsw/"
title: "Filtrable HNSW - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Filtrable HNSW

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Filtrable HNSW

Andrei Vasnetsov

·

November 24, 2019

![Filtrable HNSW](https://qdrant.tech/articles_data/filtrable-hnsw/preview/title.jpg)

If you need to find some similar objects in vector space, provided e.g. by embeddings or matching NN, you can choose among a variety of libraries: Annoy, FAISS or NMSLib.
All of them will give you a fast approximate neighbors search within almost any space.

But what if you need to introduce some constraints in your search?
For example, you want search only for products in some category or select the most similar customer of a particular brand.
I did not find any simple solutions for this.
There are several discussions like [this](https://github.com/spotify/annoy/issues/263), but they only suggest to iterate over top search results and apply conditions consequently after the search.

Let’s see if we could somehow modify any of ANN algorithms to be able to apply constrains during the search itself.

Annoy builds tree index over random projections.
Tree index implies that we will meet same problem that appears in relational databases:
if field indexes were built independently, then it is possible to use only one of them at a time.
Since nobody solved this problem before, it seems that there is no easy approach.

There is another algorithm which shows top results on the [benchmark](https://github.com/erikbern/ann-benchmarks).
It is called HNSW which stands for Hierarchical Navigable Small World.

The [original paper](https://arxiv.org/abs/1603.09320) is well written and very easy to read, so I will only give the main idea here.
We need to build a navigation graph among all indexed points so that the greedy search on this graph will lead us to the nearest point.
This graph is constructed by sequentially adding points that are connected by a fixed number of edges to previously added points.
In the resulting graph, the number of edges at each point does not exceed a given threshold m and always contains the nearest considered points.

![NSW](https://qdrant.tech/articles_data/filtrable-hnsw/NSW.png)

### [Anchor](https://qdrant.tech/articles/filtrable-hnsw/\#how-can-we-modify-it) How can we modify it?

What if we simply apply the filter criteria to the nodes of this graph and use in the greedy search only those that meet these criteria?
It turns out that even with this naive modification algorithm can cover some use cases.

One such case is if your criteria do not correlate with vector semantics.
For example, you use a vector search for clothing names and want to filter out some sizes.
In this case, the nodes will be uniformly filtered out from the entire cluster structure.
Therefore, the theoretical conclusions obtained in the [Percolation theory](https://en.wikipedia.org/wiki/Percolation_theory) become applicable:

> Percolation is related to the robustness of the graph (called also network). Given a random graph of n nodes and an average degree ⟨k⟩ . Next we remove randomly a fraction 1−p of nodes and leave only a fraction p. There exists a critical percolation threshold pc=1⟨k⟩ below which the network becomes fragmented while above pc a giant connected component exists.

This statement also confirmed by experiments:

![Dependency of connectivity to the number of edges](https://qdrant.tech/articles_data/filtrable-hnsw/exp_connectivity_glove_m0.png)

Dependency of connectivity to the number of edges

![Dependency of connectivity to the number of point (no dependency).](https://qdrant.tech/articles_data/filtrable-hnsw/exp_connectivity_glove_num_elements.png)

Dependency of connectivity to the number of point (no dependency).

There is a clear threshold when the search begins to fail.
This threshold is due to the decomposition of the graph into small connected components.
The graphs also show that this threshold can be shifted by increasing the m parameter of the algorithm, which is responsible for the degree of nodes.

Let’s consider some other filtering conditions we might want to apply in the search:

- Categorical filtering
  - Select only points in a specific category
  - Select points which belong to a specific subset of categories
  - Select points with a specific set of labels
- Numerical range
- Selection within some geographical region

In the first case, we can guarantee that the HNSW graph will be connected simply by creating additional edges
inside each category separately, using the same graph construction algorithm, and then combining them into the original graph.
In this case, the total number of edges will increase by no more than 2 times, regardless of the number of categories.

Second case is a little harder. A connection may be lost between two categories if they lie in different clusters.

![category clusters](https://qdrant.tech/articles_data/filtrable-hnsw/hnsw_graph_category.png)

The idea here is to build same navigation graph but not between nodes, but between categories.
Distance between two categories might be defined as distance between category entry points (or, for precision, as the average distance between a random sample). Now we can estimate expected graph connectivity by number of excluded categories, not nodes.
It still does not guarantee that two random categories will be connected, but allows us to switch to multiple searches in each category if connectivity threshold passed. In some cases, multiple searches can be even faster if you take advantage of parallel processing.

![Dependency of connectivity to the random categories included in search](https://qdrant.tech/articles_data/filtrable-hnsw/exp_random_groups.png)

Dependency of connectivity to the random categories included in search

Third case might be resolved in a same way it is resolved in classical databases.
Depending on labeled subsets size ration we can go for one of the following scenarios:

- if at least one subset is small: perform search over the label containing smallest subset and then filter points consequently.
- if large subsets give large intersection: perform regular search with constraints expecting that intersection size fits connectivity threshold.
- if large subsets give small intersection: perform linear search over intersection expecting that it is small enough to fit a time frame.

Numerical range case can be reduces to the previous one if we split numerical range into a buckets containing equal amount of points.
Next we also connect neighboring buckets to achieve graph connectivity. We still need to filter some results which presence in border buckets but do not fulfill actual constraints, but their amount might be regulated by the size of buckets.

Geographical case is a lot like a numerical one.
Usual geographical search involves [geohash](https://en.wikipedia.org/wiki/Geohash), which matches any geo-point to a fixes length identifier.

![Geohash example](https://qdrant.tech/articles_data/filtrable-hnsw/geohash.png)

We can use this identifiers as categories and additionally make connections between neighboring geohashes.
It will ensure that any selected geographical region will also contain connected HNSW graph.

## [Anchor](https://qdrant.tech/articles/filtrable-hnsw/\#conclusion) Conclusion

It is possible to enchant HNSW algorithm so that it will support filtering points in a first search phase.
Filtering can be carried out on the basis of belonging to categories,
which in turn is generalized to such popular cases as numerical ranges and geo.

Experiments were carried by modification [python implementation](https://github.com/generall/hnsw-python) of the algorithm,
but real production systems require much faster version, like [NMSLib](https://github.com/nmslib/nmslib).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/filtrable-hnsw.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/filtrable-hnsw.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0c317d15-0509-4a07-8261-bcff65da81ea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d787d5ca-b6ab-47a0-a692-cb31665aa1cf&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffiltrable-hnsw%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573628987&cv=11&fst=1748573628987&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffiltrable-hnsw%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Filtrable%20HNSW%20-%20Qdrant&npa=0&pscdl=noapi&auid=846779140.1748573629&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573628977&cv=11&fst=1748573628977&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffiltrable-hnsw%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Filtrable%20HNSW%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=846779140.1748573629&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0c317d15-0509-4a07-8261-bcff65da81ea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d787d5ca-b6ab-47a0-a692-cb31665aa1cf&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffiltrable-hnsw%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573629825&cv=11&fst=1748573629825&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Ffiltrable-hnsw%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Filtrable%20HNSW%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=846779140.1748573629&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)