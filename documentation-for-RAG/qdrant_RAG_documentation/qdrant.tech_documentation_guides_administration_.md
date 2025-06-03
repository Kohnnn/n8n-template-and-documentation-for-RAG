---
url: "https://qdrant.tech/documentation/guides/administration/"
title: "Administration - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Administration

# [Anchor](https://qdrant.tech/documentation/guides/administration/\#administration) Administration

Qdrant exposes administration tools which enable to modify at runtime the behavior of a qdrant instance without changing its configuration manually.

## [Anchor](https://qdrant.tech/documentation/guides/administration/\#locking) Locking

A locking API enables users to restrict the possible operations on a qdrant process.
It is important to mention that:

- The configuration is not persistent therefore it is necessary to lock again following a restart.
- Locking applies to a single node only. It is necessary to call lock on all the desired nodes in a distributed deployment setup.

Lock request sample:

```http
POST /locks
{
    "error_message": "write is forbidden",
    "write": true
}

```

Write flags enables/disables write lock.
If the write lock is set to true, qdrant doesn’t allow creating new collections or adding new data to the existing storage.
However, deletion operations or updates are not forbidden under the write lock.
This feature enables administrators to prevent a qdrant process from using more disk space while permitting users to search and delete unnecessary data.

You can optionally provide the error message that should be used for error responses to users.

## [Anchor](https://qdrant.tech/documentation/guides/administration/\#recovery-mode) Recovery mode

_Available as of v1.2.0_

Recovery mode can help in situations where Qdrant fails to start repeatedly.
When starting in recovery mode, Qdrant only loads collection metadata to prevent
going out of memory. This allows you to resolve out of memory situations, for
example, by deleting a collection. After resolving Qdrant can be restarted
normally to continue operation.

In recovery mode, collection operations are limited to
[deleting](https://qdrant.tech/documentation/concepts/collections/#delete-collection) a
collection. That is because only collection metadata is loaded during recovery.

To enable recovery mode with the Qdrant Docker image you must set the
environment variable `QDRANT_ALLOW_RECOVERY_MODE=true`. The container will try
to start normally first, and restarts in recovery mode if initialisation fails
due to an out of memory error. This behavior is disabled by default.

If using a Qdrant binary, recovery mode can be enabled by setting a recovery
message in an environment variable, such as
`QDRANT__STORAGE__RECOVERY_MODE="My recovery message"`.

## [Anchor](https://qdrant.tech/documentation/guides/administration/\#strict-mode) Strict mode

_Available as of v1.13.0_

Strict mode is a feature to restrict certain type of operations on the collection in order to protect it.

The goal is to prevent inefficient usage patterns that could overload the collections.

This configuration ensures a more predictible and responsive service when you do not have control over the queries that are being executed.

Here is a non exhaustive list of operations that can be restricted using strict mode:

- Preventing querying non indexed payload which can be very slow
- Maximum number of filtering conditions in a query
- Maximum batch size when inserting vectors
- Maximum collection size (in terms of vectors or payload size)

See [schema definitions](https://api.qdrant.tech/api-reference/collections/create-collection#request.body.strict_mode_config) for all the `strict_mode_config` parameters.

Upon crossing a limit, the server will return a client side error with the information about the limit that was crossed.

As part of the config, the `enabled` field act as a toggle to enable or disable the strict mode dynamically.

The `strict_mode_config` can be enabled when [creating](https://qdrant.tech/documentation/guides/administration/#create-a-collection) a collection, for instance below to activate the `unindexed_filtering_retrieve` limit.

Setting `unindexed_filtering_retrieve` to false prevents the usage of filtering on a non indexed payload key.

httpbashpythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}
{
    "strict_mode_config": {
        "enabled": true,
        "unindexed_filtering_retrieve": false
    }
}

```

```bash
curl -X PUT http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "strict_mode_config": {
        "enabled":" true,
        "unindexed_filtering_retrieve": false
    }
  }'

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    strict_mode_config=models.StrictModeConfig(enabled=True, unindexed_filtering_retrieve=false),
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  strict_mode_config: {
    enabled: true,
    unindexed_filtering_retrieve: false,
  },
});

```

```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{CreateCollectionBuilder, StrictModeConfigBuilder};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .strict_config_mode(StrictModeConfigBuilder::default().enabled(true).unindexed_filtering_retrieve(false)),
    )
    .await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.StrictModeCOnfig;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setStrictModeConfig(
                StrictModeConfig.newBuilder().setEnabled(true).setUnindexedFilteringRetrieve(false).build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  strictModeConfig: new StrictModeConfig { enabled = true, unindexed_filtering_retrieve = false }
);

```

```go
import (
  "context"

  "github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
  Host: "localhost",
  Port: 6334,
})

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
  CollectionName: "{collection_name}",
  StrictModeConfig: &qdrant.StrictModeConfig{
    Enabled: qdrant.PtrOf(true),
    IndexingThreshold: qdrant.PtrOf(false),
  },
})

```

Or activate it later on an existing collection through the [collection update](https://qdrant.tech/documentation/guides/administration/#update-collection-parameters) API:

httpbashpythontypescriptrustjavacsharpgo

```http
PATCH /collections/{collection_name}
{
    "strict_mode_config": {
        "enabled": true,
        "unindexed_filtering_retrieve": false
    }
}

```

```bash
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "strict_mode_config": {
        "enabled": true,
        "unindexed_filtering_retrieve": false
    }
  }'

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.update_collection(
    collection_name="{collection_name}",
    strict_mode_config=models.StrictModeConfig(enabled=True, unindexed_filtering_retrieve=False),
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.updateCollection("{collection_name}", {
  strict_mode_config: {
    enabled: true,
    unindexed_filtering_retrieve: false,
  },
});

```

```rust
use qdrant_client::qdrant::{StrictModeConfigBuilder, UpdateCollectionBuilder};

client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}").strict_mode_config(
            StrictModeConfigBuilder::default().enabled(true).unindexed_filtering_retrieve(false),
        ),
    )
    .await?;

```

```java
import io.qdrant.client.grpc.Collections.StrictModeConfigBuilder;
import io.qdrant.client.grpc.Collections.UpdateCollection;

client.updateCollectionAsync(
    UpdateCollection.newBuilder()
        .setCollectionName("{collection_name}")
        .setStrictModeConfig(
            StrictModeConfig.newBuilder().setEnabled(true).setUnindexedFilteringRetrieve(false).build())
        .build());

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
  collectionName: "{collection_name}",
  strictModeConfig: new StrictModeConfig { Enabled = true, UnindexedFilteringRetrieve = false }
);

```

```go
import (
  "context"

  "github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
  Host: "localhost",
  Port: 6334,
})

client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
  CollectionName: "{collection_name}",
  StrictModeConfig: &qdrant.StrictModeConfig{
    Enabled: qdrant.PtrOf(true),
    UnindexedFilteringRetrieve: qdrant.PtrOf(false),
  },
})

```

To disable completely strict mode on an existing collection use:

httpbashpythontypescriptrustjavacsharpgo

```http
PATCH /collections/{collection_name}
{
    "strict_mode_config": {
        "enabled": false
    }
}

```

```bash
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "strict_mode_config": {
        "enabled": false,
    }
  }'

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.update_collection(
    collection_name="{collection_name}",
    strict_mode_config=models.StrictModeConfig(enabled=False),
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.updateCollection("{collection_name}", {
  strict_mode_config: {
    enabled: false,
  },
});

```

```rust
use qdrant_client::qdrant::{StrictModeConfigBuilder, UpdateCollectionBuilder};

client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}").strict_mode_config(
            StrictModeConfigBuilder::default().enabled(false),
        ),
    )
    .await?;

```

```java
import io.qdrant.client.grpc.Collections.StrictModeConfigBuilder;
import io.qdrant.client.grpc.Collections.UpdateCollection;

client.updateCollectionAsync(
    UpdateCollection.newBuilder()
        .setCollectionName("{collection_name}")
        .setStrictModeConfig(
            StrictModeConfig.newBuilder().setEnabled(false).build())
        .build());

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
  collectionName: "{collection_name}",
  strictModeConfig: new StrictModeConfig { Enabled = false }
);

```

```go
import (
  "context"

  "github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
  Host: "localhost",
  Port: 6334,
})

client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
  CollectionName: "{collection_name}",
  StrictModeConfig: &qdrant.StrictModeConfig{
        Enabled: qdrant.PtrOf(false),
  },
})

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/administration.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/administration.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574018014&cv=11&fst=1748574018014&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fadministration%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Administration%20-%20Qdrant&npa=0&pscdl=noapi&auid=1811763257.1748574018&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574017990&cv=11&fst=1748574017990&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fadministration%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Administration%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1811763257.1748574018&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9b5e5ec2-7743-49f4-9f6a-bc0883a397ab&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e4ae3cef-09a0-486a-891e-dfce42c4356e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fadministration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9b5e5ec2-7743-49f4-9f6a-bc0883a397ab&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e4ae3cef-09a0-486a-891e-dfce42c4356e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fadministration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574018724&cv=11&fst=1748574018724&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fadministration%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Administration%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1811763257.1748574018&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)