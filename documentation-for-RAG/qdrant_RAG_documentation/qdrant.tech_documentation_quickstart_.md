---
url: "https://qdrant.tech/documentation/quickstart/"
title: "Local Quickstart - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- Local Quickstart

# [Anchor](https://qdrant.tech/documentation/quickstart/\#how-to-get-started-with-qdrant-locally) How to Get Started with Qdrant Locally

In this short example, you will use the Python Client to create a Collection, load data into it and run a basic search query.

## [Anchor](https://qdrant.tech/documentation/quickstart/\#download-and-run) Download and run

First, download the latest Qdrant image from Dockerhub:

```bash
docker pull qdrant/qdrant

```

Then, run the service:

```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant

```

Under the default configuration all data will be stored in the `./qdrant_storage` directory. This will also be the only directory that both the Container and the host machine can both see.

Qdrant is now accessible:

- REST API: [localhost:6333](http://localhost:6333/)
- Web UI: [localhost:6333/dashboard](http://localhost:6333/dashboard)
- GRPC API: [localhost:6334](http://localhost:6334/)

## [Anchor](https://qdrant.tech/documentation/quickstart/\#initialize-the-client) Initialize the client

pythontypescriptrustjavacsharpgo

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

```

```rust
use qdrant_client::Qdrant;

// The Rust client uses Qdrant's gRPC interface
let client = Qdrant::from_url("http://localhost:6334").build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

// The Java client uses Qdrant's gRPC interface
QdrantClient client = new QdrantClient(
    QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

```

```csharp
using Qdrant.Client;

// The C# client uses Qdrant's gRPC interface
var client = new QdrantClient("localhost", 6334);

```

```go
import "github.com/qdrant/go-client/qdrant"

// The Go client uses Qdrant's gRPC interface
client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

```

## [Anchor](https://qdrant.tech/documentation/quickstart/\#create-a-collection) Create a collection

You will be storing all of your vector data in a Qdrant collection. Let’s call it `test_collection`. This collection will be using a dot product distance metric to compare vectors.

pythontypescriptrustjavacsharpgo

```python
from qdrant_client.models import Distance, VectorParams

client.create_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=4, distance=Distance.DOT),
)

```

```typescript
await client.createCollection("test_collection", {
  vectors: { size: 4, distance: "Dot" },
});

```

```rust
use qdrant_client::qdrant::{CreateCollectionBuilder, VectorParamsBuilder};

client
    .create_collection(
        CreateCollectionBuilder::new("test_collection")
            .vectors_config(VectorParamsBuilder::new(4, Distance::Dot)),
    )
    .await?;

```

```java
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.VectorParams;

client.createCollectionAsync("test_collection",
        VectorParams.newBuilder().setDistance(Distance.Dot).setSize(4).build()).get();

```

```csharp
using Qdrant.Client.Grpc;

await client.CreateCollectionAsync(collectionName: "test_collection", vectorsConfig: new VectorParams
{
    Size = 4, Distance = Distance.Dot
});

```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     4,
		Distance: qdrant.Distance_Cosine,
	}),
})

```

## [Anchor](https://qdrant.tech/documentation/quickstart/\#add-vectors) Add vectors

Let’s now add a few vectors with a payload. Payloads are other data you want to associate with the vector:

pythontypescriptrustjavacsharpgo

```python
from qdrant_client.models import PointStruct

operation_info = client.upsert(
    collection_name="test_collection",
    wait=True,
    points=[\
        PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),\
        PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),\
        PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),\
        PointStruct(id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}),\
        PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}),\
        PointStruct(id=6, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mumbai"}),\
    ],
)

print(operation_info)

```

```typescript
const operationInfo = await client.upsert("test_collection", {
  wait: true,
  points: [\
    { id: 1, vector: [0.05, 0.61, 0.76, 0.74], payload: { city: "Berlin" } },\
    { id: 2, vector: [0.19, 0.81, 0.75, 0.11], payload: { city: "London" } },\
    { id: 3, vector: [0.36, 0.55, 0.47, 0.94], payload: { city: "Moscow" } },\
    { id: 4, vector: [0.18, 0.01, 0.85, 0.80], payload: { city: "New York" } },\
    { id: 5, vector: [0.24, 0.18, 0.22, 0.44], payload: { city: "Beijing" } },\
    { id: 6, vector: [0.35, 0.08, 0.11, 0.44], payload: { city: "Mumbai" } },\
  ],
});

console.debug(operationInfo);

```

```rust
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};

let points = vec![\
    PointStruct::new(1, vec![0.05, 0.61, 0.76, 0.74], [("city", "Berlin".into())]),\
    PointStruct::new(2, vec![0.19, 0.81, 0.75, 0.11], [("city", "London".into())]),\
    PointStruct::new(3, vec![0.36, 0.55, 0.47, 0.94], [("city", "Moscow".into())]),\
    // ..truncated\
];

let response = client
    .upsert_points(UpsertPointsBuilder::new("test_collection", points).wait(true))
    .await?;

dbg!(response);

```

```java
import java.util.List;
import java.util.Map;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.UpdateResult;

UpdateResult operationInfo =
    client
        .upsertAsync(
            "test_collection",
            List.of(
                PointStruct.newBuilder()
                    .setId(id(1))
                    .setVectors(vectors(0.05f, 0.61f, 0.76f, 0.74f))
                    .putAllPayload(Map.of("city", value("Berlin")))
                    .build(),
                PointStruct.newBuilder()
                    .setId(id(2))
                    .setVectors(vectors(0.19f, 0.81f, 0.75f, 0.11f))
                    .putAllPayload(Map.of("city", value("London")))
                    .build(),
                PointStruct.newBuilder()
                    .setId(id(3))
                    .setVectors(vectors(0.36f, 0.55f, 0.47f, 0.94f))
                    .putAllPayload(Map.of("city", value("Moscow")))
                    .build()))
                // Truncated
            .get();

System.out.println(operationInfo);

```

```csharp
using Qdrant.Client.Grpc;

var operationInfo = await client.UpsertAsync(collectionName: "test_collection", points: new List<PointStruct>
{
    new()
    {
        Id = 1,
            Vectors = new float[]
            {
                0.05f, 0.61f, 0.76f, 0.74f
            },
            Payload = {
                ["city"] = "Berlin"
            }
    },
    new()
    {
        Id = 2,
            Vectors = new float[]
            {
                0.19f, 0.81f, 0.75f, 0.11f
            },
            Payload = {
                ["city"] = "London"
            }
    },
    new()
    {
        Id = 3,
            Vectors = new float[]
            {
                0.36f, 0.55f, 0.47f, 0.94f
            },
            Payload = {
                ["city"] = "Moscow"
            }
    },
    // Truncated
});

Console.WriteLine(operationInfo);

```

```go
import (
	"context"
	"fmt"

	"github.com/qdrant/go-client/qdrant"
)

operationInfo, err := client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "test_collection",
	Points: []*qdrant.PointStruct{
		{
			Id:      qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectors(0.05, 0.61, 0.76, 0.74),
			Payload: qdrant.NewValueMap(map[string]any{"city": "Berlin"}),
		},
		{
			Id:      qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectors(0.19, 0.81, 0.75, 0.11),
			Payload: qdrant.NewValueMap(map[string]any{"city": "London"}),
		},
		{
			Id:      qdrant.NewIDNum(3),
			Vectors: qdrant.NewVectors(0.36, 0.55, 0.47, 0.94),
			Payload: qdrant.NewValueMap(map[string]any{"city": "Moscow"}),
		},
        // Truncated
	},
})
if err != nil {
	panic(err)
}
fmt.Println(operationInfo)

```

**Response:**

pythontypescriptrustjavacsharpgo

```python
operation_id=0 status=<UpdateStatus.COMPLETED: 'completed'>

```

```typescript
{ operation_id: 0, status: 'completed' }

```

```rust
PointsOperationResponse {
    result: Some(
        UpdateResult {
            operation_id: Some(
                0,
            ),
            status: Completed,
        },
    ),
    time: 0.00094027,
}

```

```java
operation_id: 0
status: Completed

```

```csharp
{ "operationId": "0", "status": "Completed" }

```

```go
operation_id:0  status:Acknowledged

```

## [Anchor](https://qdrant.tech/documentation/quickstart/\#run-a-query) Run a query

Let’s ask a basic question - Which of our stored vectors are most similar to the query vector `[0.2, 0.1, 0.9, 0.7]`?

pythontypescriptrustjavacsharpgo

```python
search_result = client.query_points(
    collection_name="test_collection",
    query=[0.2, 0.1, 0.9, 0.7],
    with_payload=False,
    limit=3
).points

print(search_result)

```

```typescript
let searchResult = await client.query(
    "test_collection", {
    query: [0.2, 0.1, 0.9, 0.7],
    limit: 3
});

console.debug(searchResult.points);

```

```rust
use qdrant_client::qdrant::QueryPointsBuilder;

let search_result = client
    .query(
        QueryPointsBuilder::new("test_collection")
            .query(vec![0.2, 0.1, 0.9, 0.7])
    )
    .await?;

dbg!(search_result);

```

```java
import java.util.List;

import io.qdrant.client.grpc.Points.ScoredPoint;
import io.qdrant.client.grpc.Points.QueryPoints;

import static io.qdrant.client.QueryFactory.nearest;

List<ScoredPoint> searchResult =
    client.queryAsync(QueryPoints.newBuilder()
                .setCollectionName("test_collection")
                .setLimit(3)
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .build()).get();

System.out.println(searchResult);

```

```csharp
var searchResult = await client.QueryAsync(
    collectionName: "test_collection",
    query: new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
    limit: 3,
);

Console.WriteLine(searchResult);

```

```go
import (
	"context"
	"fmt"

	"github.com/qdrant/go-client/qdrant"
)

searchResult, err := client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "test_collection",
	Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
})
if err != nil {
	panic(err)
}

fmt.Println(searchResult)

```

**Response:**

```json
[\
  {\
    "id": 4,\
    "version": 0,\
    "score": 1.362,\
    "payload": null,\
    "vector": null\
  },\
  {\
    "id": 1,\
    "version": 0,\
    "score": 1.273,\
    "payload": null,\
    "vector": null\
  },\
  {\
    "id": 3,\
    "version": 0,\
    "score": 1.208,\
    "payload": null,\
    "vector": null\
  }\
]

```

The results are returned in decreasing similarity order. Note that payload and vector data is missing in these results by default.
See [payload and vector in the result](https://qdrant.tech/documentation/concepts/search/#payload-and-vector-in-the-result) on how to enable it.

## [Anchor](https://qdrant.tech/documentation/quickstart/\#add-a-filter) Add a filter

We can narrow down the results further by filtering by payload. Let’s find the closest results that include “London”.

pythontypescriptrustjavacsharpgo

```python
from qdrant_client.models import Filter, FieldCondition, MatchValue

search_result = client.query_points(
    collection_name="test_collection",
    query=[0.2, 0.1, 0.9, 0.7],
    query_filter=Filter(
        must=[FieldCondition(key="city", match=MatchValue(value="London"))]
    ),
    with_payload=True,
    limit=3,
).points

print(search_result)

```

```typescript
searchResult = await client.query("test_collection", {
    query: [0.2, 0.1, 0.9, 0.7],
    filter: {
        must: [{ key: "city", match: { value: "London" } }],
    },
    with_payload: true,
    limit: 3,
});

console.debug(searchResult);

```

```rust
use qdrant_client::qdrant::{Condition, Filter, QueryPointsBuilder};

let search_result = client
    .query(
        QueryPointsBuilder::new("test_collection")
            .query(vec![0.2, 0.1, 0.9, 0.7])
            .filter(Filter::must([Condition::matches(\
                "city",\
                "London".to_string(),\
            )]))
            .with_payload(true),
    )
    .await?;

dbg!(search_result);

```

```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

List<ScoredPoint> searchResult =
    client.queryAsync(QueryPoints.newBuilder()
                .setCollectionName("test_collection")
                .setLimit(3)
                .setFilter(Filter.newBuilder().addMust(matchKeyword("city", "London")))
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .setWithPayload(enable(true))
                .build()).get();

System.out.println(searchResult);

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

var searchResult = await client.QueryAsync(
    collectionName: "test_collection",
    query: new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
    filter: MatchKeyword("city", "London"),
    limit: 3,
    payloadSelector: true
);

Console.WriteLine(searchResult);

```

```go
import (
	"context"
	"fmt"

	"github.com/qdrant/go-client/qdrant"
)

searchResult, err := client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "test_collection",
	Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("city", "London"),
		},
	},
	WithPayload: qdrant.NewWithPayload(true),
})
if err != nil {
	panic(err)
}

fmt.Println(searchResult)

```

**Response:**

```json
[\
    {\
        "id": 2,\
        "version": 0,\
        "score": 0.871,\
        "payload": {\
            "city": "London"\
        },\
        "vector": null\
    }\
]

```

You have just conducted vector search. You loaded vectors into a database and queried the database with a vector of your own. Qdrant found the closest results and presented you with a similarity score.

## [Anchor](https://qdrant.tech/documentation/quickstart/\#next-steps) Next steps

Now you know how Qdrant works. Getting started with [Qdrant Cloud](https://qdrant.tech/documentation/cloud/quickstart-cloud/) is just as easy. [Create an account](https://qdrant.to/cloud) and use our SaaS completely free. We will take care of infrastructure maintenance and software updates.

To move onto some more complex examples of vector search, read our [Tutorials](https://qdrant.tech/documentation/tutorials/) and create your own app with the help of our [Examples](https://qdrant.tech/documentation/examples/).

**Note:** There is another way of running Qdrant locally. If you are a Python developer, we recommend that you try Local Mode in [Qdrant Client](https://github.com/qdrant/qdrant-client), as it only takes a few moments to get setup.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/quickstart.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/quickstart.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=27e7063a-cb9a-4cc9-8109-bbc33615bf0e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=85c5792d-6439-479b-9761-737d8afe5fb1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fquickstart%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575536746&cv=11&fst=1748575536746&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fquickstart%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Local%20Quickstart%20-%20Qdrant&npa=0&pscdl=noapi&auid=609416405.1748575536&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575536689&cv=11&fst=1748575536689&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fquickstart%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Local%20Quickstart%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=609416405.1748575536&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575536826&cv=11&fst=1748575536826&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fquickstart%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Local%20Quickstart%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=609416405.1748575536&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=27e7063a-cb9a-4cc9-8109-bbc33615bf0e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=85c5792d-6439-479b-9761-737d8afe5fb1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fquickstart%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)