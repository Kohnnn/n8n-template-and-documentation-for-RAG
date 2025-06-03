---
url: "https://qdrant.tech/articles/search-as-you-type/"
title: "Semantic Search As You Type - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Semantic Search As You Type

[Back to Practical Examples](https://qdrant.tech/articles/practicle-examples/)

# Semantic Search As You Type

Andre Bogus

·

August 14, 2023

![Semantic Search As You Type](https://qdrant.tech/articles_data/search-as-you-type/preview/title.jpg)

Qdrant is one of the fastest vector search engines out there, so while looking for a demo to show off, we came upon the idea to do a search-as-you-type box with a fully semantic search backend. Now we already have a semantic/keyword hybrid search on our website. But that one is written in Python, which incurs some overhead for the interpreter. Naturally, I wanted to see how fast I could go using Rust.

Since Qdrant doesn’t embed by itself, I had to decide on an embedding model. The prior version used the [SentenceTransformers](https://www.sbert.net/) package, which in turn employs Bert-based [All-MiniLM-L6-V2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/tree/main) model. This model is battle-tested and delivers fair results at speed, so not experimenting on this front I took an [ONNX version](https://huggingface.co/optimum/all-MiniLM-L6-v2/tree/main) and ran that within the service.

The workflow looks like this:

![Search Qdrant by Embedding](https://qdrant.tech/articles_data/search-as-you-type/Qdrant_Search_by_Embedding.png)

This will, after tokenizing and embedding send a `/collections/site/points/search` POST request to Qdrant, sending the following JSON:

```json
POST collections/site/points/search
{
  "vector": [-0.06716014,-0.056464013, ...(382 values omitted)],
  "limit": 5,
  "with_payload": true,
}

```

Even with avoiding a network round-trip, the embedding still takes some time. As always in optimization, if you cannot do the work faster, a good solution is to avoid work altogether (please don’t tell my employer). This can be done by pre-computing common prefixes and calculating embeddings for them, then storing them in a `prefix_cache` collection. Now the [`recommend`](https://api.qdrant.tech/api-reference/search/recommend-points) API method can find the best matches without doing any embedding. For now, I use short (up to and including 5 letters) prefixes, but I can also parse the logs to get the most common search terms and add them to the cache later.

![Qdrant Recommendation](https://qdrant.tech/articles_data/search-as-you-type/Qdrant_Recommendation.png)

Making that work requires setting up the `prefix_cache` collection with points that have the prefix as their `point_id` and the embedding as their `vector`, which lets us do the lookup with no search or index. The `prefix_to_id` function currently uses the `u64` variant of `PointId`, which can hold eight bytes, enough for this use. If the need arises, one could instead encode the names as UUID, hashing the input. Since I know all our prefixes are within 8 bytes, I decided against this for now.

The `recommend` endpoint works roughly the same as `search_points`, but instead of searching for a vector, Qdrant searches for one or more points (you can also give negative example points the search engine will try to avoid in the results). It was built to help drive recommendation engines, saving the round-trip of sending the current point’s vector back to Qdrant to find more similar ones. However Qdrant goes a bit further by allowing us to select a different collection to lookup the points, which allows us to keep our `prefix_cache` collection separate from the site data. So in our case, Qdrant first looks up the point from the `prefix_cache`, takes its vector and searches for that in the `site` collection, using the precomputed embeddings from the cache. The API endpoint expects a POST of the following JSON to `/collections/site/points/recommend`:

```json
POST collections/site/points/recommend
{
  "positive": [1936024932],
  "limit": 5,
  "with_payload": true,
  "lookup_from": {
    "collection": "prefix_cache"
  }
}

```

Now I have, in the best Rust tradition, a blazingly fast semantic search.

To demo it, I used our [Qdrant documentation website](https://qdrant.tech/documentation/)’s page search, replacing our previous Python implementation. So in order to not just spew empty words, here is a benchmark, showing different queries that exercise different code paths.

Since the operations themselves are far faster than the network whose fickle nature would have swamped most measurable differences, I benchmarked both the Python and Rust services locally. I’m measuring both versions on the same AMD Ryzen 9 5900HX with 16GB RAM running Linux. The table shows the average time and error bound in milliseconds. I only measured up to a thousand concurrent requests. None of the services showed any slowdown with more requests in that range. I do not expect our service to become DDOS’d, so I didn’t benchmark with more load.

Without further ado, here are the results:

| query length | Short | Long |
| --- | --- | --- |
| Python 🐍 | 16 ± 4 ms | 16 ± 4 ms |
| Rust 🦀 | 1½ ± ½ ms | 5 ± 1 ms |

The Rust version consistently outperforms the Python version and offers a semantic search even on few-character queries. If the prefix cache is hit (as in the short query length), the semantic search can even get more than ten times faster than the Python version. The general speed-up is due to both the relatively lower overhead of Rust + Actix Web compared to Python + FastAPI (even if that already performs admirably), as well as using ONNX Runtime instead of SentenceTransformers for the embedding. The prefix cache gives the Rust version a real boost by doing a semantic search without doing any embedding work.

As an aside, while the millisecond differences shown here may mean relatively little for our users, whose latency will be dominated by the network in between, when typing, every millisecond more or less can make a difference in user perception. Also search-as-you-type generates between three and five times as much load as a plain search, so the service will experience more traffic. Less time per request means being able to handle more of them.

Mission accomplished! But wait, there’s more!

### [Anchor](https://qdrant.tech/articles/search-as-you-type/\#prioritizing-exact-matches-and-headings) Prioritizing Exact Matches and Headings

To improve on the quality of the results, Qdrant can do multiple searches in parallel, and then the service puts the results in sequence, taking the first best matches. The extended code searches:

1. Text matches in titles
2. Text matches in body (paragraphs or lists)
3. Semantic matches in titles
4. Any Semantic matches

Those are put together by taking them in the above order, deduplicating as necessary.

![merge workflow](https://qdrant.tech/articles_data/search-as-you-type/sayt_merge.png)

Instead of sending a `search` or `recommend` request, one can also send a `search/batch` or `recommend/batch` request, respectively. Each of those contain a `"searches"` property with any number of search/recommend JSON requests:

```json
POST collections/site/points/search/batch
{
  "searches": [\
    {\
      "vector": [-0.06716014,-0.056464013, ...],\
      "filter": {\
        "must": [\
          { "key": "text", "match": { "text": <query> }},\
          { "key": "tag", "match": { "any": ["h1", "h2", "h3"] }},\
        ]\
      }\
      ...,\
    },\
    {\
      "vector": [-0.06716014,-0.056464013, ...],\
      "filter": {\
        "must": [ { "key": "body", "match": { "text": <query> }} ]\
      }\
      ...,\
    },\
    {\
      "vector": [-0.06716014,-0.056464013, ...],\
      "filter": {\
        "must": [ { "key": "tag", "match": { "any": ["h1", "h2", "h3"] }} ]\
      }\
      ...,\
    },\
    {\
      "vector": [-0.06716014,-0.056464013, ...],\
      ...,\
    },\
  ]
}

```

As the queries are done in a batch request, there isn’t any additional network overhead and only very modest computation overhead, yet the results will be better in many cases.

The only additional complexity is to flatten the result lists and take the first 5 results, deduplicating by point ID. Now there is one final problem: The query may be short enough to take the recommend code path, but still not be in the prefix cache. In that case, doing the search _sequentially_ would mean two round-trips between the service and the Qdrant instance. The solution is to _concurrently_ start both requests and take the first successful non-empty result.

![sequential vs. concurrent flow](https://qdrant.tech/articles_data/search-as-you-type/sayt_concurrency.png)

While this means more load for the Qdrant vector search engine, this is not the limiting factor. The relevant data is already in cache in many cases, so the overhead stays within acceptable bounds, and the maximum latency in case of prefix cache misses is measurably reduced.

The code is available on the [Qdrant github](https://github.com/qdrant/page-search)

To sum up: Rust is fast, recommend lets us use precomputed embeddings, batch requests are awesome and one can do a semantic search in mere milliseconds.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/search-as-you-type.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/search-as-you-type.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574489102&cv=11&fst=1748574489102&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fsearch-as-you-type%2F&hn=www.googleadservices.com&frm=0&tiba=Semantic%20Search%20As%20You%20Type%20-%20Qdrant&npa=0&pscdl=noapi&auid=684434009.1748574489&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574489089&cv=11&fst=1748574489089&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fsearch-as-you-type%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Semantic%20Search%20As%20You%20Type%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=684434009.1748574489&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=064ee380-c67c-49fb-9082-c528de9872de&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ee67ef03-6d9d-41c1-b599-df2b18958152&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fsearch-as-you-type%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=064ee380-c67c-49fb-9082-c528de9872de&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ee67ef03-6d9d-41c1-b599-df2b18958152&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fsearch-as-you-type%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574490220&cv=11&fst=1748574490220&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fsearch-as-you-type%2F&hn=www.googleadservices.com&frm=0&tiba=Semantic%20Search%20As%20You%20Type%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=684434009.1748574489&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)