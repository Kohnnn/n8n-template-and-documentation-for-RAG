---
url: "https://qdrant.tech/articles/qdrant-introduces-full-text-filters-and-indexes/"
title: "Full-text filter and index are already available! - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Full-text filter and index are already available!

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Full-text filter and index are already available!

Kacper Łukawski

·

November 16, 2022

![Full-text filter and index are already available!](https://qdrant.tech/articles_data/qdrant-introduces-full-text-filters-and-indexes/preview/title.jpg)

Qdrant is designed as an efficient vector database, allowing for a quick search of the nearest neighbours. But, you may find yourself in need of applying some extra filtering on top of the semantic search. Up to version 0.10, Qdrant was offering support for keywords only. Since 0.10, there is a possibility to apply full-text constraints as well. There is a new type of filter that you can use to do that, also combined with every other filter type.

## [Anchor](https://qdrant.tech/articles/qdrant-introduces-full-text-filters-and-indexes/\#using-full-text-filters-without-the-payload-index) Using full-text filters without the payload index

Full-text filters without the index created on a field will return only those entries which contain all the terms included in the query. That is effectively a substring match on all the individual terms but **not a substring on a whole query**.

![](https://qdrant.tech/blog/from_cms/1_ek61_uvtyn89duqtmqqztq.webp)An example of how to search for “long\_sleeves” in a “detail\_desc” payload field.

## [Anchor](https://qdrant.tech/articles/qdrant-introduces-full-text-filters-and-indexes/\#full-text-search-behaviour-on-an-indexed-payload-field) Full-text search behaviour on an indexed payload field

There are more options if you create a full-text index on a field you will filter by.

![](https://qdrant.tech/blog/from_cms/1_pohx4eznqpgoxak6ppzypq.webp)Full-text search behaviour on an indexed payload field There are more options if you create a full-text index on a field you will filter by.

First and foremost, you can choose the tokenizer. It defines how Qdrant should split the text into tokens. There are three options available:

- **word** — spaces, punctuation marks and special characters define the token boundaries
- **whitespace** — token boundaries defined by whitespace characters
- **prefix** — token boundaries are the same as for the “word” tokenizer, but in addition to that, there are prefixes created for every single token. As a result, “Qdrant” will be indexed as “Q”, “Qd”, “Qdr”, “Qdra”, “Qdran”, and “Qdrant”.

There are also some additional parameters you can provide, such as

- **min\_token\_len** — minimal length of the token
- **max\_token\_len** — maximal length of the token
- **lowercase** — if set to _true_, then the index will be case-insensitive, as Qdrant will convert all the texts to lowercase

## [Anchor](https://qdrant.tech/articles/qdrant-introduces-full-text-filters-and-indexes/\#using-text-filters-in-practice) Using text filters in practice

![](https://qdrant.tech/blog/from_cms/1_pbtd2tzqtjqqlbi61r8czg.webp)There are also some additional parameters you can provide, such as min\_token\_len — minimal length of the token max\_token\_len — maximal length of the token lowercase — if set to true, then the index will be case-insensitive, as Qdrant will convert all the texts to lowercase Using text filters in practice

The main difference between using full-text filters on the indexed vs non-indexed field is the performance of such query. In a simple benchmark, performed on the [H&M dataset](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations) (with over 105k examples), the average query time looks as follows (n=1000):

![](https://qdrant.tech/blog/from_cms/screenshot_31.png)

It is evident that creating a filter on a field that we’ll query often, may lead us to substantial performance gains without much effort.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/full-text-filter-and-index-are-already-available.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/full-text-filter-and-index-are-already-available.md)
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