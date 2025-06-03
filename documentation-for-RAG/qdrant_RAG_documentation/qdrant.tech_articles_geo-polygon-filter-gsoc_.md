---
url: "https://qdrant.tech/articles/geo-polygon-filter-gsoc/"
title: "Google Summer of Code 2023 - Polygon Geo Filter for Qdrant Vector Database - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Google Summer of Code 2023 - Polygon Geo Filter for Qdrant Vector Database

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Google Summer of Code 2023 - Polygon Geo Filter for Qdrant Vector Database

Zein Wen

·

October 12, 2023

![Google Summer of Code 2023 - Polygon Geo Filter for Qdrant Vector Database](https://qdrant.tech/articles_data/geo-polygon-filter-gsoc/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/geo-polygon-filter-gsoc/\#introduction) Introduction

Greetings, I’m Zein Wen, and I was a Google Summer of Code 2023 participant at Qdrant. I got to work with an amazing mentor, Arnaud Gourlay, on enhancing the Qdrant Geo Polygon Filter. This new feature allows users to refine their query results using polygons. As the latest addition to the Geo Filter family of radius and rectangle filters, this enhancement promises greater flexibility in querying geo data, unlocking interesting new use cases.

## [Anchor](https://qdrant.tech/articles/geo-polygon-filter-gsoc/\#project-overview) Project Overview

![A Use Case of Geo Filter](https://qdrant.tech/articles_data/geo-polygon-filter-gsoc/geo-filter-example.png)

A Use Case of Geo Filter ( [https://traveltime.com/blog/map-postcode-data-catchment-area](https://traveltime.com/blog/map-postcode-data-catchment-area))

Because Qdrant is a powerful query vector database it presents immense potential for machine learning-driven applications, such as recommendation. However, the scope of vector queries alone may not always meet user requirements. Consider a scenario where you’re seeking restaurant recommendations; it’s not just about a list of restaurants, but those within your neighborhood. This is where the Geo Filter comes into play, enhancing query by incorporating additional filtering criteria. Up until now, Qdrant’s geographic filter options were confined to circular and rectangular shapes, which may not align with the diverse boundaries found in the real world. This scenario was exactly what led to a user feature request and we decided it would be a good feature to tackle since it introduces greater capability for geo-related queries.

## [Anchor](https://qdrant.tech/articles/geo-polygon-filter-gsoc/\#technical-challenges) Technical Challenges

**1\. Geo Geometry Computation**

![Geo Space Basic Concept](https://qdrant.tech/articles_data/geo-polygon-filter-gsoc/basic-concept.png)

Geo Space Basic Concept

Internally, the Geo Filter doesn’t start by testing each individual geo location as this would be computationally expensive. Instead, we create a geo hash layer that [divides the world](https://en.wikipedia.org/wiki/Grid_%28spatial_index%29#Grid-based_spatial_indexing) into rectangles. When a spatial index is created for Qdrant entries it assigns the entry to the geohash for its location.

During a query we first identify all potential geo hashes that satisfy the filters and subsequently check for location candidates within those hashes. Accomplishing this search involves two critical geometry computations:

1. determining if a polygon intersects with a rectangle
2. ascertaining if a point lies within a polygon.

![Geometry Computation Testing](https://qdrant.tech/articles_data/geo-polygon-filter-gsoc/geo-computation-testing.png)

Geometry Computation Testing

While we have a geo crate (a Rust library) that provides APIs for these computations, we dug in deeper to understand the underlying algorithms and verify their accuracy. This lead us to conduct extensive testing and visualization to determine correctness. In addition to assessing the current crate, we also discovered that there are multiple algorithms available for these computations. We invested time in exploring different approaches, such as [winding windows](https://en.wikipedia.org/wiki/Point_in_polygon#Winding%20number%20algorithm:~:text=of%20the%20algorithm.-,Winding%20number%20algorithm,-%5Bedit%5D) and [ray casting](https://en.wikipedia.org/wiki/Point_in_polygon#Winding%20number%20algorithm:~:text=.%5B2%5D-,Ray%20casting%20algorithm,-%5Bedit%5D), to grasp their distinctions, and pave the way for future improvements.

Through this process, I enjoyed honing my ability to swiftly grasp unfamiliar concepts. In addition, I needed to develop analytical strategies to dissect and draw meaningful conclusions from them. This experience has been invaluable in expanding my problem-solving toolkit.

**2\. Proto and JSON format design**

Considerable effort was devoted to designing the ProtoBuf and JSON interfaces for this new feature. This component is directly exposed to users, requiring a consistent and user-friendly interface, which in turns help drive a a positive user experience and less code modifications in the future.

Initially, we contemplated aligning our interface with the [GeoJSON](https://geojson.org/) specification, given its prominence as a standard for many geo-related APIs. However, we soon realized that the way GeoJSON defines geometries significantly differs from our current JSON and ProtoBuf coordinate definitions for our point radius and rectangular filter. As a result, we prioritized API-level consistency and user experience, opting to align the new polygon definition with all our existing definitions.

In addition, we planned to develop a separate multi-polygon filter in addition to the polygon. However, after careful consideration, we recognize that, for our use case, polygon filters can achieve the same result as a multi-polygon filter. This relationship mirrors how we currently handle multiple circles or rectangles. Consequently, we deemed the multi-polygon filter redundant and would introduce unnecessary complexity to the API.

Doing this work illustrated to me the challenge of navigating real-world solutions that require striking a balance between adhering to established standards and prioritizing user experience. It also was key to understanding the wisdom of focusing on developing what’s truly necessary for users, without overextending our efforts.

## [Anchor](https://qdrant.tech/articles/geo-polygon-filter-gsoc/\#outcomes) Outcomes

**1\. Capability of Deep Dive**
Navigating unfamiliar code bases, concepts, APIs, and techniques is a common challenge for developers. Participating in GSoC was akin to me going from the safety of a swimming pool and right into the expanse of the ocean. Having my mentor’s support during this transition was invaluable. He provided me with numerous opportunities to independently delve into areas I had never explored before. I have grown into no longer fearing unknown technical areas, whether it’s unfamiliar code, techniques, or concepts in specific domains. I’ve gained confidence in my ability to learn them step by step and use them to create the things I envision.

**2\. Always Put User in Minds**
Another crucial lesson I learned is the importance of considering the user’s experience and their specific use cases. While development may sometimes entail iterative processes, every aspect that directly impacts the user must be approached and executed with empathy. Neglecting this consideration can lead not only to functional errors but also erode the trust of users due to inconsistency and confusion, which then leads to them no longer using my work.

**3\. Speak Up and Effectively Communicate**
Finally, In the course of development, encountering differing opinions is commonplace. It’s essential to remain open to others’ ideas, while also possessing the resolve to communicate one’s own perspective clearly. This fosters productive discussions and ultimately elevates the quality of the development process.

### [Anchor](https://qdrant.tech/articles/geo-polygon-filter-gsoc/\#wrap-up) Wrap up

Being selected for Google Summer of Code 2023 and collaborating with Arnaud and the other Qdrant engineers, along with all the other community members, has been a true privilege. I’m deeply grateful to those who invested their time and effort in reviewing my code, engaging in discussions about alternatives and design choices, and offering assistance when needed. Through these interactions, I’ve experienced firsthand the essence of open source and the culture that encourages collaboration. This experience not only allowed me to write Rust code for a real-world product for the first time, but it also opened the door to the amazing world of open source.

Without a doubt, I’m eager to continue growing alongside this community and contribute to new features and enhancements that elevate the product. I’ve also become an advocate for Qdrant, introducing this project to numerous coworkers and friends in the tech industry. I’m excited to witness new users and contributors emerge from within my own network!

If you want to try out my work, read the [documentation](https://qdrant.tech/documentation/concepts/filtering/#geo-polygon) and then, either sign up for a free [cloud account](https://cloud.qdrant.io/) or download the [Docker image](https://hub.docker.com/r/qdrant/qdrant). I look forward to seeing how people are using my work in their own applications!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/geo-polygon-filter-gsoc.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/geo-polygon-filter-gsoc.md)
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