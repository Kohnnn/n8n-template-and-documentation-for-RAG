---
url: "https://qdrant.tech/articles/scalar-quantization/"
title: "Scalar Quantization: Background, Practices & More | Qdrant - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Scalar Quantization: Background, Practices & More \| Qdrant

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Scalar Quantization: Background, Practices & More \| Qdrant

Kacper Łukawski

·

March 27, 2023

![Scalar Quantization: Background, Practices & More | Qdrant](https://qdrant.tech/articles_data/scalar-quantization/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/scalar-quantization/\#efficiency-unleashed-the-power-of-scalar-quantization) Efficiency Unleashed: The Power of Scalar Quantization

High-dimensional vector embeddings can be memory-intensive, especially when working with
large datasets consisting of millions of vectors. Memory footprint really starts being
a concern when we scale things up. A simple choice of the data type used to store a single
number impacts even billions of numbers and can drive the memory requirements crazy. The
higher the precision of your type, the more accurately you can represent the numbers.
The more accurate your vectors, the more precise is the distance calculation. But the
advantages stop paying off when you need to order more and more memory.

Qdrant chose `float32` as a default type used to store the numbers of your embeddings.
So a single number needs 4 bytes of the memory and a 512-dimensional vector occupies
2 kB. That’s only the memory used to store the vector. There is also an overhead of the
HNSW graph, so as a rule of thumb we estimate the memory size with the following formula:

```text
memory_size = 1.5 * number_of_vectors * vector_dimension * 4 bytes

```

While Qdrant offers various options to store some parts of the data on disk, starting
from version 1.1.0, you can also optimize your memory by compressing the embeddings.
We’ve implemented the mechanism of **Scalar Quantization**! It turns out to have not
only a positive impact on memory but also on the performance.

## [Anchor](https://qdrant.tech/articles/scalar-quantization/\#scalar-quantization) Scalar quantization

Scalar quantization is a data compression technique that converts floating point values
into integers. In case of Qdrant `float32` gets converted into `int8`, so a single number
needs 75% less memory. It’s not a simple rounding though! It’s a process that makes that
transformation partially reversible, so we can also revert integers back to floats with
a small loss of precision.

### [Anchor](https://qdrant.tech/articles/scalar-quantization/\#theoretical-background) Theoretical background

Assume we have a collection of `float32` vectors and denote a single value as `f32`.
In reality neural embeddings do not cover a whole range represented by the floating
point numbers, but rather a small subrange. Since we know all the other vectors, we can
establish some statistics of all the numbers. For example, the distribution of the values
will be typically normal:

![A distribution of the vector values](https://qdrant.tech/articles_data/scalar-quantization/float32-distribution.png)

Our example shows that 99% of the values come from a `[-2.0, 5.0]` range. And the
conversion to `int8` will surely lose some precision, so we rather prefer keeping the
representation accuracy within the range of 99% of the most probable values and ignoring
the precision of the outliers. There might be a different choice of the range width,
actually, any value from a range `[0, 1]`, where `0` means empty range, and `1` would
keep all the values. That’s a hyperparameter of the procedure called `quantile`. A value
of `0.95` or `0.99` is typically a reasonable choice, but in general `quantile ∈ [0, 1]`.

#### [Anchor](https://qdrant.tech/articles/scalar-quantization/\#conversion-to-integers) Conversion to integers

Let’s talk about the conversion to `int8`. Integers also have a finite set of values that
might be represented. Within a single byte they may represent up to 256 different values,
either from `[-128, 127]` or `[0, 255]`.

![Value ranges represented by int8](https://qdrant.tech/articles_data/scalar-quantization/int8-value-range.png)

Since we put some boundaries on the numbers that might be represented by the `f32`, and
`i8` has some natural boundaries, the process of converting the values between those
two ranges is quite natural:

f32=α×i8+offset

i8=f32−offsetα

The parameters α and offset has to be calculated for a given set of vectors,
but that comes easily by putting the minimum and maximum of the represented range for
both `f32` and `i8`.

![Float32 to int8 conversion](https://qdrant.tech/articles_data/scalar-quantization/float32-to-int8-conversion.png)

For the unsigned `int8` it will go as following:

{−2=α×0+offset5=α×255+offset

In case of signed `int8`, we’ll just change the represented range boundaries:

{−2=α×(−128)+offset5=α×127+offset

For any set of vector values we can simply calculate the α and offset and
those values have to be stored along with the collection to enable to conversion between
the types.

#### [Anchor](https://qdrant.tech/articles/scalar-quantization/\#distance-calculation) Distance calculation

We do not store the vectors in the collections represented by `int8` instead of `float32`
just for the sake of compressing the memory. But the coordinates are being used while we
calculate the distance between the vectors. Both dot product and cosine distance requires
multiplying the corresponding coordinates of two vectors, so that’s the operation we
perform quite often on `float32`. Here is how it would look like if we perform the
conversion to `int8`:

f32×f32′==(α×i8+offset)×(α×i8′+offset)==α2×i8×i8′+offset×α×i8′+offset×α×i8+offset2⏟pre-compute

The first term, α2×i8×i8′ has to be calculated when we measure the
distance as it depends on both vectors. However, both the second and the third term
(offset×α×i8′ and offset×α×i8 respectively),
depend only on a single vector and those might be precomputed and kept for each vector.
The last term, offset2 does not depend on any of the values, so it might be even
computed once and reused.

If we had to calculate all the terms to measure the distance, the performance could have
been even worse than without the conversion. But thanks for the fact we can precompute
the majority of the terms, things are getting simpler. And in turns out the scalar
quantization has a positive impact not only on the memory usage, but also on the
performance. As usual, we performed some benchmarks to support this statement!

## [Anchor](https://qdrant.tech/articles/scalar-quantization/\#benchmarks) Benchmarks

We simply used the same approach as we use in all [the other benchmarks we publish](https://qdrant.tech/benchmarks/).
Both [Arxiv-titles-384-angular-no-filters](https://github.com/qdrant/ann-filtering-benchmark-datasets)
and [Gist-960](https://github.com/erikbern/ann-benchmarks/) datasets were chosen to make
the comparison between non-quantized and quantized vectors. The results are summarized
in the tables:

#### [Anchor](https://qdrant.tech/articles/scalar-quantization/\#arxiv-titles-384-angular-no-filters) Arxiv-titles-384-angular-no-filters

|  | ef = 128 | ef = 256 | ef = 512 |
| --- | --- | --- | --- |
|  | Upload and indexing time | Mean search precision | Mean search time | Mean search precision | Mean search time | Mean search precision | Mean search time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Non-quantized vectors | 649 s | 0.989 | 0.0094 | 0.994 | 0.0932 | 0.996 | 0.161 |
| Scalar Quantization | 496 s | 0.986 | 0.0037 | 0.993 | 0.060 | 0.996 | 0.115 |
| Difference | -23.57% | -0.3% | -60.64% | -0.1% | -35.62% | 0% | -28.57% |

A slight decrease in search precision results in a considerable improvement in the
latency. Unless you aim for the highest precision possible, you should not notice the
difference in your search quality.

#### [Anchor](https://qdrant.tech/articles/scalar-quantization/\#gist-960) Gist-960

|  | ef = 128 | ef = 256 | ef = 512 |
| --- | --- | --- | --- |
|  | Upload and indexing time | Mean search precision | Mean search time | Mean search precision | Mean search time | Mean search precision | Mean search time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Non-quantized vectors | 452 | 0.802 | 0.077 | 0.887 | 0.135 | 0.941 | 0.231 |
| Scalar Quantization | 312 | 0.802 | 0.043 | 0.888 | 0.077 | 0.941 | 0.135 |
| Difference | -30.79% | 0% | -44,16% | +0.11% | -42.96% | 0% | -41,56% |

In all the cases, the decrease in search precision is negligible, but we keep a latency
reduction of at least 28.57%, even up to 60,64%, while searching. As a rule of thumb,
the higher the dimensionality of the vectors, the lower the precision loss.

### [Anchor](https://qdrant.tech/articles/scalar-quantization/\#oversampling-and-rescoring) Oversampling and rescoring

A distinctive feature of the Qdrant architecture is the ability to combine the search for quantized and original vectors in a single query.
This enables the best combination of speed, accuracy, and RAM usage.

Qdrant stores the original vectors, so it is possible to rescore the top-k results with
the original vectors after doing the neighbours search in quantized space. That obviously
has some impact on the performance, but in order to measure how big it is, we made the
comparison in different search scenarios.
We used a machine with a very slow network-mounted disk and tested the following scenarios with different amounts of allowed RAM:

| Setup | RPS | Precision |
| --- | --- | --- |
| 4.5GB memory | 600 | 0.99 |
| 4.5GB memory + SQ + rescore | 1000 | 0.989 |

And another group with more strict memory limits:

| Setup | RPS | Precision |
| --- | --- | --- |
| 2GB memory | 2 | 0.99 |
| 2GB memory + SQ + rescore | 30 | 0.989 |
| 2GB memory + SQ + no rescore | 1200 | 0.974 |

In those experiments, throughput was mainly defined by the number of disk reads, and quantization efficiently reduces it by allowing more vectors in RAM.
Read more about on-disk storage in Qdrant and how we measure its performance in our article: [Minimal RAM you need to serve a million vectors](https://qdrant.tech/articles/memory-consumption/).

The mechanism of Scalar Quantization with rescoring disabled pushes the limits of low-end
machines even further. It seems like handling lots of requests does not require an
expensive setup if you can agree to a small decrease in the search precision.

### [Anchor](https://qdrant.tech/articles/scalar-quantization/\#accessing-best-practices) Accessing best practices

Qdrant documentation on [Scalar Quantization](https://qdrant.tech/documentation/quantization/#setting-up-quantization-in-qdrant)
is a great resource describing different scenarios and strategies to achieve up to 4x
lower memory footprint and even up to 2x performance increase.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/scalar-quantization.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/scalar-quantization.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=69e268ef-3225-4cf1-946b-59f678d79116&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=379b33ee-7a58-4f93-9002-4e9083cd049a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fscalar-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574350061&cv=11&fst=1748574350061&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fscalar-quantization%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Scalar%20Quantization%3A%20Background%2C%20Practices%20%26%20More%20%7C%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=798418430.1748574350&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574350046&cv=11&fst=1748574350046&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247~103308614&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fscalar-quantization%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Scalar%20Quantization%3A%20Background%2C%20Practices%20%26%20More%20%7C%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=798418430.1748574350&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574350233&cv=11&fst=1748574350233&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fscalar-quantization%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Scalar%20Quantization%3A%20Background%2C%20Practices%20%26%20More%20%7C%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=798418430.1748574350&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=69e268ef-3225-4cf1-946b-59f678d79116&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=379b33ee-7a58-4f93-9002-4e9083cd049a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fscalar-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)