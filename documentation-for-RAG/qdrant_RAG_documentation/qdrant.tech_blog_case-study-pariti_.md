---
url: "https://qdrant.tech/blog/case-study-pariti/"
title: "How Pariti Doubled Its Fill Rate with Qdrant - Qdrant"
---

0

# How Pariti Doubled Its Fill Rate with Qdrant

Daniel Azoulai

·

May 01, 2025

![How Pariti Doubled Its Fill Rate with Qdrant](https://qdrant.tech/blog/case-study-pariti/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pariti%2F&text=How%20Pariti%20Doubled%20Its%20Fill%20Rate%20with%20Qdrant "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pariti%2F "LinkedIn")

## [Anchor](https://qdrant.tech/blog/case-study-pariti/\#from-manual-bottlenecks-to-millisecond-matching-connecting-africas-best-talent) From Manual Bottlenecks to Millisecond Matching: Connecting Africa’s Best Talent

![Pariti slashes vetting time and boosted candidate placement success.](https://qdrant.tech/blog/case-study-pariti/case-study-pariti-summary-dark.jpg)

Pariti’s mission is bold: connect Africa’s best talent with the continent’s most-promising startups—fast. Its referral-driven marketplace lets anyone nominate a great candidate, but viral growth triggered an avalanche of data. A single job post now attracts more than 300 applicants within 72 hours, yet Pariti still promises clients an interview-ready shortlist inside those same five days.

By 2023 the strain was obvious. Analysts spent four minutes vetting each résumé and frequently worked through 400+ candidate backlogs. As fatigue set in, strong profiles buried near the bottom went unseen. Meanwhile, roughly 70,000 historical candidates sat idle because there was no practical way to resurface them. Fill-rate plateaued at just 20 percent.

### [Anchor](https://qdrant.tech/blog/case-study-pariti/\#a-laptop-experiment-shows-the-way) A Laptop Experiment Shows the Way

Data Scientist Chiara Stramaccioni built a quick Python script on her laptop: encode the text requirements of a new role, embed every candidate’s experience, compare vectors, and rank the results. Quality looked excellent, but each query took half a minute of local compute, and only Chiara could run it. The prototype proved feasibility, but it did not solve scale.

### [Anchor](https://qdrant.tech/blog/case-study-pariti/\#dropping-qdrant-into-production) Dropping Qdrant into Production

Engineering Lead Elvis Moraa needed a production-grade vector database that could ship immediately and stay out of the team’s way. He chose Qdrant Cloud for three pragmatic reasons:

1. Zero-ops deployment—a managed cluster spun up in minutes with regional hosting on Google Cloud, keeping latency low.

2. An intuitive Python SDK—analysts could call it as easily as Pandas, without wrestling with Kafka or index-tuning ceremonies.

3. Clear documentation to move from “Hello, vectors” to a live integration in a single afternoon.


Pariti ingested the entire 70,000-candidate corpus, and a lightweight back-end now creates embeddings the moment new data arrives. Queries travel over HTTP and come back in between 22 and 40 milliseconds with 0 percent downtime since launch.

### [Anchor](https://qdrant.tech/blog/case-study-pariti/\#what-the-workflow-looks-like-today) What the Workflow Looks Like Today

Hiring analysts open an internal web app, paste or tweak the role description, and adjust sliders that weight features such as industry expertise or publication history. The app hits Qdrant, which returns a ranked shortlist instantly. Because the vectors already sit in memory, each retrieval saves an average of 34 seconds compared with the old monthly-refreshed pickle file.

Every recommendation still gets a human glance, but that glance is now brief: vetting time has fallen from four minutes to one minute per candidate—a 70 percent reduction. When a new vacancy closely resembles past roles, the analysts skip manual sourcing almost entirely. They refine the filters, review the top suggestions, and send them onward. For these “database finds”, 24 percent of candidates make it to interviews, quadruple the 6 percent success rate of traditional channels.

Accuracy remains the north star. Pariti defines “true high performers” as applicants who ultimately receive an offer from a client. Over the past quarter 94 percent of those winners were already sitting in the application’s top decile, giving hiring managers near-perfect confidence that they are seeing the best talent first.

### [Anchor](https://qdrant.tech/blog/case-study-pariti/\#better-search-results--more-hires) Better search results = more hires

- Fill-rate soared from 20 percent to 48 percent, and Pariti now averages eight successful placements every month, sustaining a vacancy-fill rate comfortably above 40 percent.

- Analysts reclaimed entire workdays each week; instead of drowning in résumé triage, they spend time coaching clients and candidates.

- The platform handles 100-plus searches per day without breaking a sweat, and has logged zero unplanned outages since migrating to Qdrant.


“Qdrant is the last thing I worry about breaking.” — Elvis Moraa, Engineering Lead, Pariti

### [Anchor](https://qdrant.tech/blog/case-study-pariti/\#the-road-ahead) The Road Ahead

The team is productising the tool as a customer-facing portal. Hiring managers will tune ranking sliders themselves and watch shortlists refresh in real time. To meet the coming spike in traffic, Pariti is evaluating GPU-assisted indexing and vector quantization—features already built into Qdrant—while keeping costs in line with the challenging realities of many African startup budgets.

What began as an after–hours experiment on a single laptop has become the backbone of a talent marketplace that moves at startup speed. With Qdrant handling the heavy lifting in 22 milliseconds, Pariti can focus on its real job: unlocking opportunity.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=e27288b6-a631-4df2-bd87-b5db6933b9fc)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574900905&cv=11&fst=1748574900905&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pariti%2F&hn=www.googleadservices.com&frm=0&tiba=How%20Pariti%20Doubled%20Its%20Fill%20Rate%20with%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=1156726119.1748574901&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574900873&cv=11&fst=1748574900873&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pariti%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=How%20Pariti%20Doubled%20Its%20Fill%20Rate%20with%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1156726119.1748574901&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0fe60845-1eec-4ac3-8b9d-8fe1f35efec3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f938fa5e-2990-48e0-88e6-27b256997a53&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pariti%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0fe60845-1eec-4ac3-8b9d-8fe1f35efec3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f938fa5e-2990-48e0-88e6-27b256997a53&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pariti%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=2c80c3871664178376428cc4d4189012&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574902070&cv=11&fst=1748574902070&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pariti%2F&hn=www.googleadservices.com&frm=0&tiba=How%20Pariti%20Doubled%20Its%20Fill%20Rate%20with%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1156726119.1748574901&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)