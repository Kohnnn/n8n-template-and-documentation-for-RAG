---
url: "https://qdrant.tech/documentation/cloud-quickstart/"
title: "Cloud Quickstart - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- Cloud Quickstart

# [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#how-to-get-started-with-qdrant-cloud) How to Get Started With Qdrant Cloud

How to Get Started With Qdrant Cloud - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[How to Get Started With Qdrant Cloud](https://www.youtube.com/watch?v=3hrQP3hh69Y)

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

[Why am I seeing this?](https://support.google.com/youtube/answer/9004474?hl=en)

[Watch on](https://www.youtube.com/watch?v=3hrQP3hh69Y&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 1:53
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=3hrQP3hh69Y "Watch on YouTube")

You can try vector search on Qdrant Cloud in three steps.

Instructions are below, but the video is faster:

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#setup-a-qdrant-cloud-cluster) Setup a Qdrant Cloud Cluster

1. Register for a [Cloud account](https://cloud.qdrant.io/signup?ajs_anonymous_id=492f8120-7c63-4769-a25d-7f1bda864ae7) with your email, Google or Github credentials.
2. Go to **Clusters** and follow the onboarding instructions under **Create First Cluster**.

![create a cluster](https://qdrant.tech/docs/gettingstarted/gui-quickstart/create-cluster.png)

3. When you create it, you will receive an API key. You will need to copy it and store it somewhere self. It will not be displayed again. If you loose it, you can always create a new one on the **Cluster Detail Page** later.

![get api key](https://qdrant.tech/docs/gettingstarted/gui-quickstart/api-key.png)

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#access-the-cluster-ui) Access the Cluster UI

1. Click on **Cluster UI** on the **Cluster Detail Page** to access the cluster UI dashboard.
2. Paste your new API key here. You can revoke and create new API keys in the **API Keys** tab on your **Cluster Detail Page**.
3. The key will grant you access to your Qdrant instance. Now you can see the cluster Dashboard.

![access the dashboard](https://qdrant.tech/docs/gettingstarted/gui-quickstart/access-dashboard.png)

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#authenticate-via-sdks) Authenticate via SDKs

Now that you have your cluster and key, you can use our official SDKs to access Qdrant Cloud from within your application.

bashpythontypescriptrustjavacsharpgo

```bash
curl \
  -X GET https://xyz-example.eu-central.aws.cloud.qdrant.io:6333 \
  --header 'api-key: <your-api-key>'

# Alternatively, you can use the `Authorization` header with the `Bearer` prefix
curl \
  -X GET https://xyz-example.eu-central.aws.cloud.qdrant.io:6333 \
  --header 'Authorization: Bearer <your-api-key>'

```

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    host="xyz-example.eu-central.aws.cloud.qdrant.io",
    api_key="<your-api-key>",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  apiKey: "<your-api-key>",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.eu-central.aws.cloud.qdrant.io:6334")
    .api_key("<your-api-key>")
    .build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder(
                "xyz-example.eu-central.aws.cloud.qdrant.io",
                6334,
                true)
            .withApiKey("<your-api-key>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  https: true,
  apiKey: "<your-api-key>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.eu-central.aws.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<your-api-key>",
	UseTLS: true,
})

```

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#try-the-tutorial-sandbox) Try the Tutorial Sandbox

1. Open the interactive **Tutorial**. Here, you can test basic Qdrant API requests.
2. Using the **Quickstart** instructions, create a collection, add vectors and run a search.
3. The output on the right will show you some basic semantic search results.

![interactive-tutorial](https://qdrant.tech/docs/gettingstarted/gui-quickstart/interactive-tutorial.png)

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#thats-vector-search) That’s Vector Search!

You can stay in the sandbox and continue trying our different API calls.

When ready, use the Console and our complete REST API to try other operations.

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#whats-next) What’s Next?

Now that you have a Qdrant Cloud cluster up and running, you should [test remote access](https://qdrant.tech/documentation/cloud/authentication/#test-cluster-access) with a Qdrant Client.

For more about Qdrant Cloud, check our [dedicated documentation](https://qdrant.tech/documentation/cloud-intro/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-quickstart.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-quickstart.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7aefd500-a30f-46d1-8025-dab2770d5c97&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=06490325-cf83-4fca-9ac2-295cc283c36e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-quickstart%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7aefd500-a30f-46d1-8025-dab2770d5c97&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=06490325-cf83-4fca-9ac2-295cc283c36e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-quickstart%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)