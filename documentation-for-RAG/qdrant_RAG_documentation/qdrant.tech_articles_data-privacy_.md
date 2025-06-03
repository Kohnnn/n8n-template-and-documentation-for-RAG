---
url: "https://qdrant.tech/articles/data-privacy/"
title: "Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC) - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC)

[Back to Vector Search Manuals](https://qdrant.tech/articles/vector-search-manuals/)

# Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC)

Qdrant Team

·

June 18, 2024

![ Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC)](https://qdrant.tech/articles_data/data-privacy/preview/title.jpg)

Data stored in vector databases is often proprietary to the enterprise and may include sensitive information like customer records, legal contracts, electronic health records (EHR), financial data, and intellectual property. Moreover, strong security measures become critical to safeguarding this data. If the data stored in a vector database is not secured, it may open a vulnerability known as “ [embedding inversion attack](https://arxiv.org/abs/2004.00053),” where malicious actors could potentially [reconstruct the original data from the embeddings](https://arxiv.org/pdf/2305.03010) themselves.

Strict compliance regulations govern data stored in vector databases across various industries. For instance, healthcare must comply with HIPAA, which dictates how protected health information (PHI) is stored, transmitted, and secured. Similarly, the financial services industry follows PCI DSS to safeguard sensitive financial data. These regulations require developers to ensure data storage and transmission comply with industry-specific legal frameworks across different regions. **As a result, features that enable data privacy, security and sovereignty are deciding factors when choosing the right vector database.**

This article explores various strategies to ensure the security of your critical data while leveraging the benefits of vector search. Implementing some of these security approaches can help you build privacy-enhanced similarity search algorithms and integrate them into your AI applications.
Additionally, you will learn how to build a fully data-sovereign architecture, allowing you to retain control over your data and comply with relevant data laws and regulations.

> To skip right to the code implementation, [click here](https://qdrant.tech/articles/data-privacy/#jwt-on-qdrant).

## [Anchor](https://qdrant.tech/articles/data-privacy/\#vector-database-security-an-overview) Vector Database Security: An Overview

Vector databases are often unsecured by default to facilitate rapid prototyping and experimentation. This approach allows developers to quickly ingest data, build vector representations, and test similarity search algorithms without initial security concerns. However, in production environments, unsecured databases pose significant data breach risks.

For production use, robust security systems are essential. Authentication, particularly using static API keys, is a common approach to control access and prevent unauthorized modifications. Yet, simple API authentication is insufficient for enterprise data, which requires granular control.

The primary challenge with static API keys is their all-or-nothing access, inadequate for role-based data segregation in enterprise applications. Additionally, a compromised key could grant attackers full access to manipulate or steal data. To strengthen the security of the vector database, developers typically need the following:

1. **Encryption**: This ensures that sensitive data is scrambled as it travels between the application and the vector database. This safeguards against Man-in-the-Middle ( [MitM](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)) attacks, where malicious actors can attempt to intercept and steal data during transmission.
2. **Role-Based Access Control**: As mentioned before, traditional static API keys grant all-or-nothing access, which is a significant security risk in enterprise environments. RBAC offers a more granular approach by defining user roles and assigning specific data access permissions based on those roles. For example, an analyst might have read-only access to specific datasets, while an administrator might have full CRUD (Create, Read, Update, Delete) permissions across the database.
3. **Deployment Flexibility**: Data residency regulations like GDPR (General Data Protection Regulation) and industry-specific compliance requirements dictate where data can be stored, processed, and accessed. Developers would need to choose a database solution which offers deployment options that comply with these regulations. This might include on-premise deployments within a company’s private cloud or geographically distributed cloud deployments that adhere to data residency laws.

## [Anchor](https://qdrant.tech/articles/data-privacy/\#how-qdrant-handles-data-privacy-and-security) How Qdrant Handles Data Privacy and Security

One of the cornerstones of our design choices at Qdrant has been the focus on security features. We have built in a range of features keeping the enterprise user in mind, which allow building of granular access control on a fully data sovereign architecture.

A Qdrant instance is unsecured by default. However, when you are ready to deploy in production, Qdrant offers a range of security features that allow you to control access to your data, protect it from breaches, and adhere to regulatory requirements. Using Qdrant, you can build granular access control, segregate roles and privileges, and create a fully data sovereign architecture.

### [Anchor](https://qdrant.tech/articles/data-privacy/\#api-keys-and-tls-encryption) API Keys and TLS Encryption

For simpler use cases, Qdrant offers API key-based authentication. This includes both regular API keys and read-only API keys. Regular API keys grant full access to read, write, and delete operations, while read-only keys restrict access to data retrieval operations only, preventing write actions.

On Qdrant Cloud, you can create API keys using the [Cloud Dashboard](https://qdrant.to/cloud). This allows you to generate API keys that give you access to a single node or cluster, or multiple clusters. You can read the steps to do so [here](https://qdrant.tech/documentation/cloud/authentication/).

![web-ui](https://qdrant.tech/articles_data/data-privacy/web-ui.png)

For on-premise or local deployments, you’ll need to configure API key authentication. This involves specifying a key in either the Qdrant configuration file or as an environment variable. This ensures that all requests to the server must include a valid API key sent in the header.

When using the simple API key-based authentication, you should also turn on TLS encryption. Otherwise, you are exposing the connection to sniffing and MitM attacks. To secure your connection using TLS, you would need to create a certificate and private key, and then [enable TLS](https://qdrant.tech/documentation/guides/security/#tls) in the configuration.

API authentication, coupled with TLS encryption, offers a first layer of security for your Qdrant instance. However, to enable more granular access control, the recommended approach is to leverage JSON Web Tokens (JWTs).

### [Anchor](https://qdrant.tech/articles/data-privacy/\#jwt-on-qdrant) JWT on Qdrant

JSON Web Tokens (JWTs) are a compact, URL-safe, and stateless means of representing _claims_ to be transferred between two parties. These claims are encoded as a JSON object and are cryptographically signed.

JWT is composed of three parts: a header, a payload, and a signature, which are concatenated with dots (.) to form a single string. The header contains the type of token and algorithm being used. The payload contains the claims (explained in detail later). The signature is a cryptographic hash and ensures the token’s integrity.

In Qdrant, JWT forms the foundation through which powerful access controls can be built. Let’s understand how.

JWT is enabled on the Qdrant instance by specifying the API key and turning on the **jwt\_rbac** feature in the configuration (alternatively, they can be set as environment variables). For any subsequent request, the API key is used to encode or decode the token.

The way JWT works is that just the API key is enough to generate the token, and doesn’t require any communication with the Qdrant instance or server. There are several libraries that help generate tokens by encoding a payload, such as [PyJWT](https://pyjwt.readthedocs.io/en/stable/) (for Python), [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken) (for JavaScript), and [jsonwebtoken](https://crates.io/crates/jsonwebtoken) (for Rust). Qdrant uses the HS256 algorithm to encode or decode the tokens.

We will look at the payload structure shortly, but here’s how you can generate a token using PyJWT.

```python
import jwt
import datetime

# Define your API key and other payload data
api_key = "your_api_key"
payload = { ...
}

token = jwt.encode(payload, api_key, algorithm="HS256")
print(token)

```

Once you have generated the token, you should include it in the subsequent requests. You can do so by providing it as a bearer token in the Authorization header, or in the API Key header of your requests.

Below is an example of how to do so using QdrantClient in Python:

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    "http://localhost:6333",
    api_key="<JWT>", # the token goes here
)
# Example search vector
search_vector = [0.1, 0.2, 0.3, 0.4]

# Example similarity search request
response = qdrant_client.search(
    collection_name="demo_collection",
    query_vector=search_vector,
    limit=5  # Number of results to retrieve
)

```

For convenience, we have added a JWT generation tool in the Qdrant Web UI, which is present under the 🔑 tab. For your local deployments, you will find it at [http://localhost:6333/dashboard#/jwt](http://localhost:6333/dashboard#/jwt).

### [Anchor](https://qdrant.tech/articles/data-privacy/\#payload-configuration) Payload Configuration

There are several different options (claims) you can use in the JWT payload that help control access and functionality. Let’s look at them one by one.

**exp**: This claim is the expiration time of the token, and is a unix timestamp in seconds. After the expiration time, the token will be invalid.

**value\_exists**: This claim validates the token against a specific key-value stored in a collection. By using this claim, you can revoke access by simply changing a value without having to invalidate the API key.

**access**: This claim defines the access level of the token. The access level can be global read (r) or manage (m). It can also be specific to a collection, or even a subset of a collection, using read (r) and read-write (rw).

Let’s look at a few example JWT payload configurations.

**Scenario 1: 1-hour expiry time, and read-only access to a collection**

```json
{
  "exp": 1690995200,  // Set to 1 hour from the current time (Unix timestamp)
  "access": [\
    {\
      "collection": "demo_collection",\
      "access": "r"  // Read-only access\
    }\
  ]
}

```

**Scenario 2: 1-hour expiry time, and access to user with a specific role**

Suppose you have a ‘users’ collection and have defined specific roles for each user, such as ‘developer’, ‘manager’, ‘admin’, ‘analyst’, and ‘revoked’. In such a scenario, you can use a combination of **exp** and **value\_exists**.

```json
{
  "exp":  1690995200,
  "value_exists": {
    "collection": "users",
    "matches": [\
      { "key": "username", "value": "john" },\
      { "key": "role", "value": "developer" }\
    ],
  },
}

```

Now, if you ever want to revoke access for a user, simply change the value of their role. All future requests will be invalid using a token payload of the above type.

**Scenario 3: 1-hour expiry time, and read-write access to a subset of a collection**

You can even specify access levels specific to subsets of a collection. This can be especially useful when you are leveraging [multitenancy](https://qdrant.tech/documentation/guides/multiple-partitions/), and want to segregate access.

```json
{
  "exp": 1690995200,
  "access": [\
    {\
      "collection": "demo_collection",\
      "access": "r",\
      "payload": {\
        "user_id": "user_123456"\
      }\
    }\
  ]
}

```

By combining the claims, you can fully customize the access level that a user or a role has within the vector store.

### [Anchor](https://qdrant.tech/articles/data-privacy/\#creating-role-based-access-control-rbac-using-jwt) Creating Role-Based Access Control (RBAC) Using JWT

As we saw above, JWT claims create powerful levers through which you can create granular access control on Qdrant. Let’s bring it all together and understand how it helps you create Role-Based Access Control (RBAC).

In a typical enterprise application, you will have a segregation of users based on their roles and permissions. These could be:

1. **Admin or Owner:** with full access, and can generate API keys.
2. **Editor:** with read-write access levels to specific collections.
3. **Viewer:** with read-only access to specific collections.
4. **Data Scientist or Analyst:** with read-only access to specific collections.
5. **Developer:** with read-write access to development- or testing-specific collections, but limited access to production data.
6. **Guest:** with limited read-only access to publicly available collections.

In addition, you can create access levels within sections of a collection. In a multi-tenant application, where you have used payload-based partitioning, you can create read-only access for specific user roles for a subset of the collection that belongs to that user.

Your application requirements will eventually help you decide the roles and access levels you should create. For example, in an application managing customer data, you could create additional roles such as:

**Customer Support Representative**: read-write access to customer service-related data but no access to billing information.

**Billing Department**: read-only access to billing data and read-write access to payment records.

**Marketing Analyst**: read-only access to anonymized customer data for analytics.

Each role can be assigned a JWT with claims that specify expiration times, read/write permissions for collections, and validating conditions.

In such an application, an example JWT payload for a customer support representative role could be:

```json
{
  "exp": 1690995200,
  "access": [\
    {\
      "collection": "customer_data",\
      "access": "rw",\
      "payload": {\
        "department": "support"\
      }\
    }\
  ],
  "value_exists": {
    "collection": "departments",
    "matches": [\
      { "key": "department", "value": "support" }\
    ]
  }
}

```

As you can see, by implementing RBAC, you can ensure proper segregation of roles and their privileges, and avoid privacy loopholes in your application.

## [Anchor](https://qdrant.tech/articles/data-privacy/\#qdrant-hybrid-cloud-and-data-sovereignty) Qdrant Hybrid Cloud and Data Sovereignty

Data governance varies by country, especially for global organizations dealing with different regulations on data privacy, security, and access. This often necessitates deploying infrastructure within specific geographical boundaries.

To address these needs, the vector database you choose should support deployment and scaling within your controlled infrastructure. [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) offers this flexibility, along with features like sharding, replicas, JWT authentication, and monitoring.

Qdrant Hybrid Cloud integrates Kubernetes clusters from various environments—cloud, on-premises, or edge—into a unified managed service. This allows organizations to manage Qdrant databases through the Qdrant Cloud UI while keeping the databases within their infrastructure.

With JWT and RBAC, Qdrant Hybrid Cloud provides a secure, private, and sovereign vector store. Enterprises can scale their AI applications geographically, comply with local laws, and maintain strict data control.

## [Anchor](https://qdrant.tech/articles/data-privacy/\#conclusion) Conclusion

Vector similarity is increasingly becoming the backbone of AI applications that leverage unstructured data. By transforming data into vectors – their numerical representations – organizations can build powerful applications that harness semantic search, ranging from better recommendation systems to algorithms that help with personalization, or powerful customer support chatbots.

However, to fully leverage the power of AI in production, organizations need to choose a vector database that offers strong privacy and security features, while also helping them adhere to local laws and regulations.

Qdrant provides exceptional efficiency and performance, along with the capability to implement granular access control to data, Role-Based Access Control (RBAC), and the ability to build a fully data-sovereign architecture.

Interested in mastering vector search security and deployment strategies? [Join our Discord community](https://discord.gg/qdrant) to explore more advanced search strategies, connect with other developers and researchers in the industry, and stay updated on the latest innovations!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/data-privacy.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/data-privacy.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573623893&cv=11&fst=1748573623893&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdata-privacy%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Data%20Privacy%20with%20Qdrant%3A%20Implementing%20Role-Based%20Access%20Control%20(RBAC)%20-%20Qdrant&npa=0&pscdl=noapi&auid=2059190345.1748573624&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573623879&cv=11&fst=1748573623879&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdata-privacy%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Data%20Privacy%20with%20Qdrant%3A%20Implementing%20Role-Based%20Access%20Control%20(RBAC)%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2059190345.1748573624&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=cdace5f8-3a92-4805-961a-449abc08d1a9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=33bb14aa-d32e-4647-918e-8cb6e345290a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdata-privacy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=cdace5f8-3a92-4805-961a-449abc08d1a9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=33bb14aa-d32e-4647-918e-8cb6e345290a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdata-privacy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573624785&cv=11&fst=1748573624785&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdata-privacy%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Data%20Privacy%20with%20Qdrant%3A%20Implementing%20Role-Based%20Access%20Control%20(RBAC)%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2059190345.1748573624&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)