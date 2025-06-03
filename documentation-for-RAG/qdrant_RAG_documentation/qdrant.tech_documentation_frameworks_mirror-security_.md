---
url: "https://qdrant.tech/documentation/frameworks/mirror-security/"
title: "VectaX - Mirror Security - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- VectaX - Mirror Security

![VectaX Logo](https://qdrant.tech/documentation/frameworks/mirror-security/vectax-logo.png)

[VectaX](https://mirrorsecurity.io/vectax) by Mirror Security is an AI-centric access control and encryption system designed for managing and protecting vector embeddings. It combines similarity-preserving encryption with fine-grained RBAC to enable secure storage, retrieval, and operations on vector data.

It can be integrated with Qdrant to secure vector searches.

We’ll see how to do so using basic VectaX vector encryption and the sophisticated RBAC mechanism. You can obtain an API key and the Mirror SDK from the [Mirror Security Platform](https://platform.mirrorsecurity.io/en/login).

Let’s set up both the VectaX and Qdrant clients.

```python
from mirror_sdk.core.mirror_core import MirrorSDK, MirrorConfig
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

# Get your API key from
# https://platform.mirrorsecurity.io
config = MirrorConfig(
    api_key="<your_api_key>",
    server_url="https://mirrorapi.azure-api.net/v1",
    secret="<your_encrypt_secret>",
)
mirror_sdk = MirrorSDK(config)

# Connects to http://localhost:6333/ by default
qdrant = QdrantClient()

```

## [Anchor](https://qdrant.tech/documentation/frameworks/mirror-security/\#vector-encryption) Vector Encryption

Now, let’s secure vector embeddings using VectaX encryption.

```python
from qdrant_client.models import PointStruct
from mirror_sdk.core.models import VectorData

# Generate or retrieve vector embeddings
# embedding = generate_document_embedding()

vector_data = VectorData(vector=embedding, id="doc1")
encrypted = mirror_sdk.vectax.encrypt(vector_data)

point = PointStruct(
    id=0,
    vector=encrypted.ciphertext,
    payload={
        "content": "Document content",
        "iv": encrypted.iv,
        "auth_hash": encrypted.auth_hash
    }
)
qdrant.upsert(collection_name="vectax", points=[point])

# Encrypt a query vector for secure search
# query_embedding = generate_query_embedding(...)

encrypted_query = mirror_sdk.vectax.encrypt(
    VectorData(vector=query_embedding, id="query")
)

results = qdrant.query_points(
    collection_name="vectax",
    query=encrypted_query.ciphertext,
    limit=5
).points

```

## [Anchor](https://qdrant.tech/documentation/frameworks/mirror-security/\#vector-search-with-rbac) Vector Search with RBAC

RBAC allows fine-grained access control over encrypted vector data based on roles, groups, and departments.

### [Anchor](https://qdrant.tech/documentation/frameworks/mirror-security/\#defining-access-policies) Defining Access Policies

```python
app_policy = {
    "roles": ["admin", "analyst", "user"],
    "groups": ["team_a", "team_b"],
    "departments": ["research", "engineering"],
}
mirror_sdk.set_policy(app_policy)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/mirror-security/\#generating-access-keys) Generating Access Keys

```python
# Generate a secret key for use by the 'admin' role holders.
admin_key = mirror_sdk.rbac.generate_user_secret_key(
    {"roles": ["admin"], "groups": ["team_a"], "departments": ["research"]}
)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/mirror-security/\#storing-encrypted-data-with-rbac-policies) Storing Encrypted Data with RBAC Policies

We can now store data that is only accessible to users with the “admin” role.

```python
from mirror_sdk.core.models import RBACVectorData
from mirror_sdk.utils import encode_binary_data

policy = {
    "roles": ["admin"],
    "groups": ["team_a"],
    "departments": ["research"],
}
# vector_embedding = generate_vector_embedding(...)
vector_data = RBACVectorData(
    # Generate or retrieve vector embeddings
    vector=vector_embedding,
    id=1,
    access_policy=policy,
)
encrypted = mirror_sdk.rbac.encrypt(vector_data)

qdrant.upsert(
    collection_name="vectax",
    points=[\
        models.PointStruct(\
            id=1,\
            vector=encrypted.crypto.ciphertext,\
            payload={\
                "encrypted_header": encrypted.encrypted_header,\
                "encrypted_vector_metadata": encode_binary_data(\
                    encrypted.crypto.serialize()\
                ),\
                "content": "My content",\
            },\
        )\
    ],
)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/mirror-security/\#querying-with-role-based-decryption) Querying with Role-Based Decryption

Using the admin key, only accessible data will be decrypted.

```python
from mirror_sdk.core import MirrorError
from mirror_sdk.core.models import MirrorCrypto
from mirror_sdk.utils import decode_binary_data

# Encrypt a query vector for secure search
# query_embedding = generate_query_embedding(...)

query_data = RBACVectorData(vector=query_embedding, id="query", access_policy=policy)
encrypted_query = mirror_sdk.rbac.encrypt(query_data)

results = qdrant.query_points(
    collection_name="vectax", query=encrypted_query.crypto.ciphertext, limit=10
)

accessible_results = []
for point in results.points:
    try:
        encrypted_vector_metadata = decode_binary_data(
            point.payload["encrypted_vector_metadata"]
        )
        mirror_data = MirrorCrypto.deserialize(encrypted_vector_metadata)
        admin_decrypted = mirror_sdk.rbac.decrypt(
            mirror_data,
            point.payload["encrypted_header"],
            admin_key,
        )
        accessible_results.append(
            {
                "id": point.id,
                "content": point.payload["content"],
                "score": point.score,
                "accessible": True,
            }
        )

    except MirrorError as e:
        print(f"Access denied for point {point.id}: {e}")

# Proceed to only use results within `accessible_results`.

```

## [Anchor](https://qdrant.tech/documentation/frameworks/mirror-security/\#further-reading) Further Reading

- [Mirror Security Docs](https://docs.mirrorsecurity.io/introduction)
- [Mirror Security Blog](https://mirrorsecurity.io/blog)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/mirror-security.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/mirror-security.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574757356&cv=11&fst=1748574757356&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fmirror-security%2F&hn=www.googleadservices.com&frm=0&tiba=VectaX%20-%20Mirror%20Security%20-%20Qdrant&npa=0&pscdl=noapi&auid=15903776.1748574757&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574757328&cv=11&fst=1748574757328&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fmirror-security%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=VectaX%20-%20Mirror%20Security%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=15903776.1748574757&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c8be05ea-40a1-4cdc-9a6f-b05eec6ff420&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6a9cd5a0-fa5c-4a2b-85e5-94553f97fc27&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fmirror-security%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c8be05ea-40a1-4cdc-9a6f-b05eec6ff420&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6a9cd5a0-fa5c-4a2b-85e5-94553f97fc27&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fmirror-security%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574758416&cv=11&fst=1748574758416&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fmirror-security%2F&hn=www.googleadservices.com&frm=0&tiba=VectaX%20-%20Mirror%20Security%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=15903776.1748574757&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)