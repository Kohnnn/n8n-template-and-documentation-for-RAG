---
url: "https://qdrant.tech/documentation/frameworks/dsrag/"
title: "dsRAG - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- dsRAG

# [Anchor](https://qdrant.tech/documentation/frameworks/dsrag/\#dsrag) dsRAG

[dsRAG](https://github.com/D-Star-AI/dsRAG) is a retrieval engine for unstructured data. It is especially good at handling challenging queries over dense text, like financial reports, legal documents, and academic papers. dsRAG achieves substantially higher accuracy than vanilla RAG baselines on complex open-book question answering tasks

You can use the Qdrant connector in dsRAG to add and semantically retrieve documents from your collections.

## [Anchor](https://qdrant.tech/documentation/frameworks/dsrag/\#usage-example) Usage Example

```python
from dsrag.database.vector import QdrantVectorDB
import numpy as np
from qdrant_clien import models

db = QdrantVectorDB(kb_id=self.kb_id, url="http://localhost:6334", prefer_grpc=True)
vectors = [np.array([1, 0]), np.array([0, 1])]

# You can use any document loaders available with dsRAG
# We'll use literals for demonstration
documents = [\
    {\
        "doc_id": "1",\
        "chunk_index": 0,\
        "chunk_header": "Header1",\
        "chunk_text": "Text1",\
    },\
    {\
        "doc_id": "2",\
        "chunk_index": 1,\
        "chunk_header": "Header2",\
        "chunk_text": "Text2",\
    },\
]

db.add_vectors(vectors, documents)

metadata_filter = models.Filter(
    must=[models.FieldCondition(key="doc_id", match=models.MatchValue(value="1"))]
)

db.search(query_vector, top_k=4, metadata_filter=metadata_filter)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/dsrag/\#further-reading) Further Reading

- [dsRAG Source](https://github.com/D-Star-AI/dsRAG).
- [dsRAG Examples](https://github.com/D-Star-AI/dsRAG/tree/main/examples)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dsrag.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dsrag.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=aa226814-34d6-4062-9dc2-3dcb3123a835&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=84837336-a5d7-4d75-8156-a6368ad83785&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdsrag%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=aa226814-34d6-4062-9dc2-3dcb3123a835&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=84837336-a5d7-4d75-8156-a6368ad83785&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdsrag%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)