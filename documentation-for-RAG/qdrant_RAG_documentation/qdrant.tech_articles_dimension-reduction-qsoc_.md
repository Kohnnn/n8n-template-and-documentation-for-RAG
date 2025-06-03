---
url: "https://qdrant.tech/articles/dimension-reduction-qsoc/"
title: "Qdrant Summer of Code 2024 - WASM based Dimension Reduction - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Qdrant Summer of Code 2024 - WASM based Dimension Reduction

[Back to Ecosystem](https://qdrant.tech/articles/ecosystem/)

# Qdrant Summer of Code 2024 - WASM based Dimension Reduction

Jishan Bhattacharya

·

August 31, 2024

![Qdrant Summer of Code 2024 - WASM based Dimension Reduction](https://qdrant.tech/articles_data/dimension-reduction-qsoc/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/dimension-reduction-qsoc/\#introduction) Introduction

Hello, everyone! I’m Jishan Bhattacharya, and I had the incredible opportunity to intern at Qdrant this summer as part of the Qdrant Summer of Code 2024. Under the mentorship of [Andrey Vasnetsov](https://www.linkedin.com/in/andrey-vasnetsov-75268897/), I dived into the world of performance optimization, focusing on enhancing vector visualization using WebAssembly (WASM). In this article, I’ll share the insights, challenges, and accomplishments from my journey — one filled with learning, experimentation, and plenty of coding adventures.

## [Anchor](https://qdrant.tech/articles/dimension-reduction-qsoc/\#project-overview) Project Overview

Qdrant is a robust vector database and search engine designed to store vector data and perform tasks like similarity search and clustering. One of its standout features is the ability to visualize high-dimensional vectors in a 2D space. However, the existing implementation faced performance bottlenecks, especially when scaling to large datasets. My mission was to tackle this challenge by leveraging a WASM-based solution for dimensionality reduction in the visualization process.

## [Anchor](https://qdrant.tech/articles/dimension-reduction-qsoc/\#learnings--challenges) Learnings & Challenges

Our weapon of choice was Rust, paired with WASM, and we employed the t-SNE algorithm for dimensionality reduction. For those unfamiliar, t-SNE (t-Distributed Stochastic Neighbor Embedding) is a technique that helps visualize high-dimensional data by projecting it into two or three dimensions. It operates in two main steps:

1. **Computing Pairwise Similarity:** This step involves calculating the similarity between each pair of data points in the original high-dimensional space.

2. **Iterative Optimization:** The second step is iterative, where the embedding is refined using gradient descent. Here, the similarity matrix from the first step plays a crucial role.


At the outset, Andrey tasked me with rewriting the existing JavaScript implementation of t-SNE in Rust, introducing multi-threading along the way. Setting up WASM with Vite for multi-threaded execution was no small feat, but the effort paid off. The resulting Rust implementation outperformed the single-threaded JavaScript version, although it still struggled with large datasets.

Next came the challenge of optimizing the algorithm further. A key aspect of t-SNE’s first step is finding the nearest neighbors for each data point, which requires an efficient data structure. I opted for a [Vantage Point Tree](https://en.wikipedia.org/wiki/Vantage-point_tree) (also known as a Ball Tree) to speed up this process. As for the second step, while it is inherently sequential, there was still room for improvement. I incorporated Barnes-Hut approximation to accelerate the gradient calculation. This method approximates the forces between points in low dimensional space, making the process more efficient.

To illustrate, imagine dividing a 2D space into quadrants, each containing multiple points. Every quadrant is again subdivided into four quadrants. This is done until every point belongs to a single cell.

![Calculating the resultant force on red point using Barnes-Hut approximation](https://qdrant.tech/articles_data/dimension-reduction-qsoc/barnes_hut.png)

Barnes-Hut Approximation

We then calculate the center of mass for each cell represented by a blue circle as shown in the figure. Now let’s say we want to find all the forces, represented by dotted lines, on the red point. Barnes Hut’s approximation states that for points that are sufficiently distant, instead of computing the force for each individual point, we use the center of mass as a proxy, significantly reducing the computational load. This is represented by the blue dotted line in the figure.

These optimizations made a remarkable difference — Barnes-Hut t-SNE was eight times faster than the exact t-SNE for 10,000 vectors.

![Image of visualizing 10,000 vectors using exact t-SNE which took 884.728s](https://qdrant.tech/articles_data/dimension-reduction-qsoc/rust_rewrite.jpg)

Exact t-SNE - Total time: 884.728s

![Image of visualizing 10,000 vectors using Barnes-Hut t-SNE which took 110.728s](https://qdrant.tech/articles_data/dimension-reduction-qsoc/rust_bhtsne.jpg)

Barnes-Hut t-SNE - Total time: 104.191s

Despite these improvements, the first step of the algorithm was still a bottleneck, leading to noticeable delays and blank screens. I experimented with approximate nearest neighbor algorithms, but the performance gains were minimal. After consulting with my mentor, we decided to compute the nearest neighbors on the server side, passing the distance matrix directly to the visualization process instead of the raw vectors.

While waiting for the distance-matrix API to be ready, I explored further optimizations. I observed that the worker thread sent results to the main thread for rendering at specific intervals, causing unnecessary delays due to serialization and deserialization.

![Image showing serialization and deserialization overhead due to message passing between threads](https://qdrant.tech/articles_data/dimension-reduction-qsoc/channels.png)

Serialization and Deserialization Overhead

To address this, I implemented a `SharedArrayBuffer`, allowing the main thread to access changes made by the worker thread instantly. This change led to noticeable improvements.

Additionally, the previous architecture resulted in choppy animations due to the fixed intervals at which the worker thread sent results.

![Image showing the previous architecture of the frontend with fixed intervals for sending results](https://qdrant.tech/articles_data/dimension-reduction-qsoc/prev_arch.png)

Previous architecture with fixed intervals

I introduced a “rendering-on-demand” approach, where the main thread would signal the worker thread when it was ready to render the next result. This created smoother, more responsive animations.

![Image showing the current architecture of the frontend with rendering-on-demand approach](https://qdrant.tech/articles_data/dimension-reduction-qsoc/curr_arch.png)

Current architecture with rendering-on-demand

With these optimizations in place, the final step was wrapping up the project by creating a Node.js [package](https://www.npmjs.com/package/wasm-dist-bhtsne). This package exposed the necessary interfaces to accept the distance matrix, perform calculations, and return the results, making the solution easy to integrate into various projects.

## [Anchor](https://qdrant.tech/articles/dimension-reduction-qsoc/\#areas-for-improvement) Areas for Improvement

While reflecting on this transformative journey, there are still areas that offer room for improvement and future enhancements:

1. **Payload Parsing:** When requesting a large number of vectors, parsing the payload on the main thread can make the user interface unresponsive. Implementing a faster parser could mitigate this issue.

2. **Direct Data Requests:** Allowing the worker thread to request data directly could eliminate the initial transfer of data from the main thread, speeding up the overall process.

3. **Chart Library Optimization:** Profiling revealed that nearly 80% of the time was spent on the Chart.js update function. Switching to a WebGL-accelerated chart library could dramatically improve performance, especially for large datasets.
![Image showing profiling results with 80% time spent on Chart.js update function](https://qdrant.tech/articles_data/dimension-reduction-qsoc/profiling.png)

Profiling Result


## [Anchor](https://qdrant.tech/articles/dimension-reduction-qsoc/\#conclusion) Conclusion

Participating in the Qdrant Summer of Code 2024 was a deeply rewarding experience. I had the chance to push the boundaries of my coding skills while exploring new technologies like Rust and WebAssembly. I’m incredibly grateful for the guidance and support from my mentor and the entire Qdrant team, who made this journey both educational and enjoyable.

This experience has not only honed my technical skills but also ignited a deeper passion for optimizing performance in real-world applications. I’m excited to apply the knowledge and skills I’ve gained to future projects and to see how Qdrant’s enhanced vector visualization feature will benefit users worldwide.

This experience has not only honed my technical skills but also ignited a deeper passion for optimizing performance in real-world applications. I’m excited to apply the knowledge and skills I’ve gained to future projects and to see how Qdrant’s enhanced vector visualization feature will benefit users worldwide.

Thank you for joining me on this coding adventure. I hope you found something valuable in my journey, and I look forward to sharing more exciting projects with you in the future. Happy coding!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/dimension-reduction-qsoc.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/dimension-reduction-qsoc.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574572428&cv=11&fst=1748574572428&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdimension-reduction-qsoc%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%202024%20-%20WASM%20based%20Dimension%20Reduction%20-%20Qdrant&npa=0&pscdl=noapi&auid=175380425.1748574572&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574572387&cv=11&fst=1748574572387&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdimension-reduction-qsoc%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%202024%20-%20WASM%20based%20Dimension%20Reduction%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=175380425.1748574572&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ad400e87-6d0d-4a87-b32d-d19efae5f7e6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7815ad64-d942-4df2-b0ca-c8cfcf1705d2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdimension-reduction-qsoc%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ad400e87-6d0d-4a87-b32d-d19efae5f7e6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7815ad64-d942-4df2-b0ca-c8cfcf1705d2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdimension-reduction-qsoc%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574573874&cv=11&fst=1748574573874&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdimension-reduction-qsoc%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%202024%20-%20WASM%20based%20Dimension%20Reduction%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=175380425.1748574572&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)