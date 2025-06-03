---
url: "https://qdrant.tech/documentation/cloud/authentication/"
title: "Authentication - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud](https://qdrant.tech/documentation/cloud/)
- Authentication

# [Anchor](https://qdrant.tech/documentation/cloud/authentication/\#database-authentication-in-qdrant-managed-cloud) Database Authentication in Qdrant Managed Cloud

This page describes what Database API keys are and shows you how to use the Qdrant Cloud Console to create a Database API key for a cluster. You will learn how to connect to your cluster using the new API key.

Database API keys can be configured with granular access control. Database API keys with granular access control can be recognized by starting with `eyJhb`. Please refer to the [Table of access](https://qdrant.tech/documentation/guides/security/#table-of-access) to understand what permissions you can configure.

Database API keys with granular access control are available for clusters using version **v1.11.0** and above.

## [Anchor](https://qdrant.tech/documentation/cloud/authentication/\#create-database-api-keys) Create Database API Keys

![API Key](https://qdrant.tech/documentation/cloud/create-api-key.png)

1. Go to the [Cloud Dashboard](https://qdrant.to/cloud).
2. Go to the **API Keys** section of the **Cluster Detail Page**.
3. Click **Create**.
4. Choose a name and an optional expiration (in days, the default is 90 days) for your API key. An empty expiration will result in no expiration.
5. By default, tokens are given cluster-wide permissions, with a choice between manage/write permissions (default) or read-only.



To restrict a token to a subset of collections, you can select the Collections tab and choose from the collections available in your cluster.
6. Click **Create** and retrieve your API key.

![API Key](https://qdrant.tech/documentation/cloud/api-key.png)

We recommend configuring an expiration and rotating your API keys regularly as a security best practice.

How to Use Qdrant's Database API Keys with Granular Access Control - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[How to Use Qdrant's Database API Keys with Granular Access Control](https://www.youtube.com/watch?v=3c-8tcBIVdQ)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=3c-8tcBIVdQ&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 3:00
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=3c-8tcBIVdQ "Watch on YouTube")

## [Anchor](https://qdrant.tech/documentation/cloud/authentication/\#admin-database-api-keys) Admin Database API Keys

The previous iteration of Database API keys, called Admin Database API keys, do not have granular access control. Clusters created before January 27, 2025 will still see the option to create Admin Database API keys. Older Admin Database API keys will continue to work, but we do recommend switching to Database API keys with granular access control to take advantage of better security controls.

To enable Database API keys with granular access control, click **Enable** on the **API Keys** section of the Cluster detail page.

After enabling Database API keys with granular access control for a cluster, existing Admin Database API keys will continue to work, but you will not be able to create new Admin Database API Keys.

## [Anchor](https://qdrant.tech/documentation/cloud/authentication/\#test-cluster-access) Test Cluster Access

After creation, you will receive a code snippet to access your cluster. Your generated request should look very similar to this one:

```bash
curl \
  -X GET 'https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6333' \
  --header 'api-key: <paste-your-api-key-here>'

```

Open Terminal and run the request. You should get a response that looks like this:

```bash
{"title":"qdrant - vector search engine","version":"1.13.0","commit":"ffda0b90c8c44fc43c99adab518b9787fe57bde6"}

```

> **Note:** You need to include the API key in the request header for every
> request over REST or gRPC.

## [Anchor](https://qdrant.tech/documentation/cloud/authentication/\#authenticate-via-sdk) Authenticate via SDK

Now that you have created your first cluster and key, you might want to access your database from within your application.
Our [official Qdrant clients](https://qdrant.tech/documentation/interfaces/) for Python, TypeScript, Go, Rust, .NET and Java all support the API key parameter.

bashpythontypescriptrustjavacsharpgo

```bash
curl \
  -X GET https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6333 \
  --header 'api-key: <provide-your-own-key>'

# Alternatively, you can use the `Authorization` header with the `Bearer` prefix
curl \
  -X GET https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6333 \
  --header 'Authorization: Bearer <provide-your-own-key>'

```

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
    api_key="<paste-your-api-key-here>",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  host: "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
  apiKey: "<paste-your-api-key-here>",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6334")
    .api_key("<paste-your-api-key-here>")
    .build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder(
                "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
                6334,
                true)
            .withApiKey("<paste-your-api-key-here>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
  https: true,
  apiKey: "<paste-your-api-key-here>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<paste-your-api-key-here>",
	UseTLS: true,
})

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/authentication.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/authentication.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5cb72c76-a7de-4c1d-a53b-c6d65bda6ad5&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4258845b-5a1d-42eb-8c3e-ca8922eca56f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fauthentication%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5cb72c76-a7de-4c1d-a53b-c6d65bda6ad5&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4258845b-5a1d-42eb-8c3e-ca8922eca56f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fauthentication%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)