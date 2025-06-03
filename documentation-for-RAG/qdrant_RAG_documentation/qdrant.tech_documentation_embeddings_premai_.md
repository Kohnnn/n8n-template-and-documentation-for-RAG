---
url: "https://qdrant.tech/documentation/embeddings/premai/"
title: "Prem AI - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Prem AI

# [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#prem-ai) Prem AI

[PremAI](https://premai.io/) is a unified generative AI development platform for fine-tuning deploying, and monitoring AI models.

Qdrant is compatible with PremAI APIs.

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#installing-the-sdks) Installing the SDKs

```bash
pip install premai qdrant-client

```

To install the npm package:

```bash
npm install @premai/prem-sdk @qdrant/js-client-rest

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#import-all-required-packages) Import all required packages

pythontypescript

```python
from premai import Prem

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

```

```typescript
import Prem from '@premai/prem-sdk';
import { QdrantClient } from '@qdrant/js-client-rest';

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#define-all-the-constants) Define all the constants

We need to define the project ID and the embedding model to use. You can learn more about obtaining these in the PremAI [docs](https://docs.premai.io/quick-start).

pythontypescript

```python
PROJECT_ID = 123
EMBEDDING_MODEL = "text-embedding-3-large"
COLLECTION_NAME = "prem-collection-py"
QDRANT_SERVER_URL = "http://localhost:6333"
DOCUMENTS = [\
    "This is a sample python document",\
    "We will be using qdrant and premai python sdk"\
]

```

```typescript
const PROJECT_ID = 123;
const EMBEDDING_MODEL = "text-embedding-3-large";
const COLLECTION_NAME = "prem-collection-js";
const SERVER_URL = "http://localhost:6333"
const DOCUMENTS = [\
    "This is a sample javascript document",\
    "We will be using qdrant and premai javascript sdk"\
];

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#set-up-premai-and-qdrant-clients) Set up PremAI and Qdrant clients

pythontypescript

```python
prem_client = Prem(api_key="xxxx-xxx-xxx")
qdrant_client = QdrantClient(url=QDRANT_SERVER_URL)

```

```typescript
const premaiClient = new Prem({
    apiKey: "xxxx-xxx-xxx"
})
const qdrantClient = new QdrantClient({ url: SERVER_URL });

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#generating-embeddings) Generating Embeddings

pythontypescript

```python
from typing import Union, List

def get_embeddings(
    project_id: int,
    embedding_model: str,
    documents: Union[str, List[str]]
) -> List[List[float]]:
    """
    Helper function to get the embeddings from premai sdk
    Args
        project_id (int): The project id from prem saas platform.
        embedding_model (str): The embedding model alias to choose
        documents (Union[str, List[str]]): Single texts or list of texts to embed
    Returns:
        List[List[int]]: A list of list of integers that represents different
            embeddings
    """
    embeddings = []
    documents = [documents] if isinstance(documents, str) else documents
    for embedding in prem_client.embeddings.create(
        project_id=project_id,
        model=embedding_model,
        input=documents
    ).data:
        embeddings.append(embedding.embedding)

    return embeddings

```

```typescript
async function getEmbeddings(projectID, embeddingModel, documents) {
    const response = await premaiClient.embeddings.create({
        project_id: projectID,
        model: embeddingModel,
        input: documents
    });
    return response;
}

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#converting-embeddings-to-qdrant-points) Converting Embeddings to Qdrant Points

pythontypescript

```python
from qdrant_client.models import PointStruct

embeddings = get_embeddings(
    project_id=PROJECT_ID,
    embedding_model=EMBEDDING_MODEL,
    documents=DOCUMENTS
)

points = [\
    PointStruct(\
        id=idx,\
        vector=embedding,\
        payload={"text": text},\
    ) for idx, (embedding, text) in enumerate(zip(embeddings, DOCUMENTS))\
]

```

```typescript
function convertToQdrantPoints(embeddings, texts) {
    return embeddings.data.map((data, i) => {
        return {
            id: i,
            vector: data.embedding,
            payload: {
                text: texts[i]
            }
        };
    });
}

const embeddings = await getEmbeddings(PROJECT_ID, EMBEDDING_MODEL, DOCUMENTS);
const points = convertToQdrantPoints(embeddings, DOCUMENTS);

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#set-up-a-qdrant-collection) Set up a Qdrant Collection

pythontypescript

```python
qdrant_client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=3072, distance=Distance.DOT)
)

```

```typescript
await qdrantClient.createCollection(COLLECTION_NAME, {
    vectors: {
        size: 3072,
        distance: 'Cosine'
    }
})

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#insert-documents-into-the-collection) Insert Documents into the Collection

pythontypescript

```python
doc_ids = list(range(len(embeddings)))

qdrant_client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
 )

```

```typescript
await qdrantClient.upsert(COLLECTION_NAME, {
        wait: true,
        points
    });

```

### [Anchor](https://qdrant.tech/documentation/embeddings/premai/\#perform-a-search) Perform a Search

pythontypescript

```python
query = "what is the extension of python document"

query_embedding = get_embeddings(
    project_id=PROJECT_ID,
    embedding_model=EMBEDDING_MODEL,
    documents=query
)

qdrant_client.search(collection_name=COLLECTION_NAME, query_vector=query_embedding[0])

```

```typescript
const query = "what is the extension of javascript document"
const query_embedding_response = await getEmbeddings(PROJECT_ID, EMBEDDING_MODEL, query)

await qdrantClient.search(COLLECTION_NAME, {
    vector: query_embedding_response.data[0].embedding
});

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/premai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/premai.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8449b916-f8e9-436c-9c8d-683032bf9c2f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1224e4ae-ea66-4a6a-a16f-fcaa2348521b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fpremai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574444318&cv=11&fst=1748574444318&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fpremai%2F&hn=www.googleadservices.com&frm=0&tiba=Prem%20AI%20-%20Qdrant&npa=0&pscdl=noapi&auid=1616898788.1748574444&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574444306&cv=11&fst=1748574444306&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fpremai%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Prem%20AI%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1616898788.1748574444&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574444378&cv=11&fst=1748574444378&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fpremai%2F&hn=www.googleadservices.com&frm=0&tiba=Prem%20AI%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1616898788.1748574444&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8449b916-f8e9-436c-9c8d-683032bf9c2f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1224e4ae-ea66-4a6a-a16f-fcaa2348521b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fpremai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)