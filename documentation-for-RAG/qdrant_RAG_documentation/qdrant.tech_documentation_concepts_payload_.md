---
url: "https://qdrant.tech/documentation/concepts/payload/"
title: "Payload - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Payload

# [Anchor](https://qdrant.tech/documentation/concepts/payload/\#payload) Payload

One of the significant features of Qdrant is the ability to store additional information along with vectors.
This information is called `payload` in Qdrant terminology.

Qdrant allows you to store any information that can be represented using JSON.

Here is an example of a typical payload:

```json
{
    "name": "jacket",
    "colors": ["red", "blue"],
    "count": 10,
    "price": 11.99,
    "locations": [\
        {\
            "lon": 52.5200,\
            "lat": 13.4050\
        }\
    ],
    "reviews": [\
        {\
            "user": "alice",\
            "score": 4\
        },\
        {\
            "user": "bob",\
            "score": 5\
        }\
    ]
}

```

## [Anchor](https://qdrant.tech/documentation/concepts/payload/\#payload-types) Payload types

In addition to storing payloads, Qdrant also allows you search based on certain kinds of values.
This feature is implemented as additional filters during the search and will enable you to incorporate custom logic on top of semantic similarity.

During the filtering, Qdrant will check the conditions over those values that match the type of the filtering condition. If the stored value type does not fit the filtering condition - it will be considered not satisfied.

For example, you will get an empty output if you apply the [range condition](https://qdrant.tech/documentation/concepts/filtering/#range) on the string data.

However, arrays (multiple values of the same type) are treated a little bit different. When we apply a filter to an array, it will succeed if at least one of the values inside the array meets the condition.

The filtering process is discussed in detail in the section [Filtering](https://qdrant.tech/documentation/concepts/filtering/).

Let’s look at the data types that Qdrant supports for searching:

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#integer) Integer

`integer` \- 64-bit integer in the range from `-9223372036854775808` to `9223372036854775807`.

Example of single and multiple `integer` values:

```json
{
    "count": 10,
    "sizes": [35, 36, 38]
}

```

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#float) Float

`float` \- 64-bit floating point number.

Example of single and multiple `float` values:

```json
{
    "price": 11.99,
    "ratings": [9.1, 9.2, 9.4]
}

```

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#bool) Bool

Bool - binary value. Equals to `true` or `false`.

Example of single and multiple `bool` values:

```json
{
    "is_delivered": true,
    "responses": [false, false, true, false]
}

```

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#keyword) Keyword

`keyword` \- string value.

Example of single and multiple `keyword` values:

```json
{
    "name": "Alice",
    "friends": [\
        "bob",\
        "eva",\
        "jack"\
    ]
}

```

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#geo) Geo

`geo` is used to represent geographical coordinates.

Example of single and multiple `geo` values:

```json
{
    "location": {
        "lon": 52.5200,
        "lat": 13.4050
    },
    "cities": [\
        {\
            "lon": 51.5072,\
            "lat": 0.1276\
        },\
        {\
            "lon": 40.7128,\
            "lat": 74.0060\
        }\
    ]
}

```

Coordinate should be described as an object containing two fields: `lon` \- for longitude, and `lat` \- for latitude.

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#datetime) Datetime

_Available as of v1.8.0_

`datetime` \- date and time in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format.

See the following examples of single and multiple `datetime` values:

```json
{
    "created_at": "2023-02-08T10:49:00Z",
    "updated_at": [\
        "2023-02-08T13:52:00Z",\
        "2023-02-21T21:23:00Z"\
    ]
}

```

The following formats are supported:

- `"2023-02-08T10:49:00Z"` ( [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6), UTC)
- `"2023-02-08T11:49:00+01:00"` ( [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6), with timezone)
- `"2023-02-08T10:49:00"` (without timezone, UTC is assumed)
- `"2023-02-08T10:49"` (without timezone and seconds)
- `"2023-02-08"` (only date, midnight is assumed)

Notes about the format:

- `T` can be replaced with a space.
- The `T` and `Z` symbols are case-insensitive.
- UTC is always assumed when the timezone is not specified.
- Timezone can have the following formats: `±HH:MM`, `±HHMM`, `±HH`, or `Z`.
- Seconds can have up to 6 decimals, so the finest granularity for `datetime` is microseconds.

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#uuid) UUID

_Available as of v1.11.0_

In addition to the basic `keyword` type, Qdrant supports `uuid` type for storing UUID values.
Functionally, it works the same as `keyword`, internally stores parsed UUID values.

```json
{
    "uuid": "550e8400-e29b-41d4-a716-446655440000",
    "uuids": [\
        "550e8400-e29b-41d4-a716-446655440000",\
        "550e8400-e29b-41d4-a716-446655440001"\
    ]
}

```

String representation of UUID (e.g. `550e8400-e29b-41d4-a716-446655440000`) occupies 36 bytes.
But when numeric representation is used, it is only 128 bits (16 bytes).

Usage of `uuid` index type is recommended in payload-heavy collections to save RAM and improve search performance.

## [Anchor](https://qdrant.tech/documentation/concepts/payload/\#create-point-with-payload) Create point with payload

REST API ( [Schema](https://api.qdrant.tech/api-reference/points/upsert-points))

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}/points
{
    "points": [\
        {\
            "id": 1,\
            "vector": [0.05, 0.61, 0.76, 0.74],\
            "payload": {"city": "Berlin", "price": 1.99}\
        },\
        {\
            "id": 2,\
            "vector": [0.19, 0.81, 0.75, 0.11],\
            "payload": {"city": ["Berlin", "London"], "price": 1.99}\
        },\
        {\
            "id": 3,\
            "vector": [0.36, 0.55, 0.47, 0.94],\
            "payload": {"city": ["Berlin", "Moscow"], "price": [1.99, 2.99]}\
        }\
    ]
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.upsert(
    collection_name="{collection_name}",
    points=[\
        models.PointStruct(\
            id=1,\
            vector=[0.05, 0.61, 0.76, 0.74],\
            payload={\
                "city": "Berlin",\
                "price": 1.99,\
            },\
        ),\
        models.PointStruct(\
            id=2,\
            vector=[0.19, 0.81, 0.75, 0.11],\
            payload={\
                "city": ["Berlin", "London"],\
                "price": 1.99,\
            },\
        ),\
        models.PointStruct(\
            id=3,\
            vector=[0.36, 0.55, 0.47, 0.94],\
            payload={\
                "city": ["Berlin", "Moscow"],\
                "price": [1.99, 2.99],\
            },\
        ),\
    ],
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
  points: [\
    {\
      id: 1,\
      vector: [0.05, 0.61, 0.76, 0.74],\
      payload: {\
        city: "Berlin",\
        price: 1.99,\
      },\
    },\
    {\
      id: 2,\
      vector: [0.19, 0.81, 0.75, 0.11],\
      payload: {\
        city: ["Berlin", "London"],\
        price: 1.99,\
      },\
    },\
    {\
      id: 3,\
      vector: [0.36, 0.55, 0.47, 0.94],\
      payload: {\
        city: ["Berlin", "Moscow"],\
        price: [1.99, 2.99],\
      },\
    },\
  ],
});

```

```rust
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};
use qdrant_client::{Payload, Qdrant, QdrantError};
use serde_json::json;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![\
    PointStruct::new(\
        1,\
        vec![0.05, 0.61, 0.76, 0.74],\
        Payload::try_from(json!({"city": "Berlin", "price": 1.99})).unwrap(),\
    ),\
    PointStruct::new(\
        2,\
        vec![0.19, 0.81, 0.75, 0.11],\
        Payload::try_from(json!({"city": ["Berlin", "London"]})).unwrap(),\
    ),\
    PointStruct::new(\
        3,\
        vec![0.36, 0.55, 0.47, 0.94],\
        Payload::try_from(json!({"city": ["Berlin", "Moscow"], "price": [1.99, 2.99]}))\
            .unwrap(),\
    ),\
];

client
    .upsert_points(UpsertPointsBuilder::new("{collection_name}", points).wait(true))
    .await?;

```

```java
import java.util.List;
import java.util.Map;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.PointStruct;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(vectors(0.05f, 0.61f, 0.76f, 0.74f))
                .putAllPayload(Map.of("city", value("Berlin"), "price", value(1.99)))
                .build(),
            PointStruct.newBuilder()
                .setId(id(2))
                .setVectors(vectors(0.19f, 0.81f, 0.75f, 0.11f))
                .putAllPayload(
                    Map.of("city", list(List.of(value("Berlin"), value("London")))))
                .build(),
            PointStruct.newBuilder()
                .setId(id(3))
                .setVectors(vectors(0.36f, 0.55f, 0.47f, 0.94f))
                .putAllPayload(
                    Map.of(
                        "city",
                        list(List.of(value("Berlin"), value("London"))),
                        "price",
                        list(List.of(value(1.99), value(2.99)))))
                .build()))
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new PointStruct
        {
            Id = 1,
            Vectors = new[] { 0.05f, 0.61f, 0.76f, 0.74f },
            Payload = { ["city"] = "Berlin", ["price"] = 1.99 }
        },
        new PointStruct
        {
            Id = 2,
            Vectors = new[] { 0.19f, 0.81f, 0.75f, 0.11f },
            Payload = { ["city"] = new[] { "Berlin", "London" } }
        },
        new PointStruct
        {
            Id = 3,
            Vectors = new[] { 0.36f, 0.55f, 0.47f, 0.94f },
            Payload =
            {
                ["city"] = new[] { "Berlin", "Moscow" },
                ["price"] = new Value
                {
                    ListValue = new ListValue { Values = { new Value[] { 1.99, 2.99 } } }
                }
            }
        }
    }
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
    CollectionName: "{collection_name}",
    Points: []*qdrant.PointStruct{
        {
            Id:      qdrant.NewIDNum(1),
            Vectors: qdrant.NewVectors(0.05, 0.61, 0.76, 0.74),
            Payload: qdrant.NewValueMap(map[string]any{
                "city": "Berlin", "price": 1.99}),
        },
        {
            Id:      qdrant.NewIDNum(2),
            Vectors: qdrant.NewVectors(0.19, 0.81, 0.75, 0.11),
            Payload: qdrant.NewValueMap(map[string]any{
                "city": []any{"Berlin", "London"}}),
        },
        {
            Id:      qdrant.NewIDNum(3),
            Vectors: qdrant.NewVectors(0.36, 0.55, 0.47, 0.94),
            Payload: qdrant.NewValueMap(map[string]any{
                "city":  []any{"Berlin", "London"},
                "price": []any{1.99, 2.99}}),
        },
    },
})

```

## [Anchor](https://qdrant.tech/documentation/concepts/payload/\#update-payload) Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The **set payload** method updates specific fields while keeping others unchanged, while the **overwrite** method replaces the entire payload. Developers can also use **clear payload** to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#set-payload) Set payload

Set only the given payload values on a point.

REST API ( [Schema](https://api.qdrant.tech/api-reference/points/set-payload)):

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
    "points": [\
        0, 3, 100\
    ]
}

```

```python
client.set_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
    points=[0, 3, 10],
)

```

```typescript
client.setPayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
  points: [0, 3, 10],
});

```

```rust
use qdrant_client::qdrant::{
    PointsIdsList, SetPayloadPointsBuilder,
};
use qdrant_client::Payload,;
use serde_json::json;

client
    .set_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;

```

```java
import java.util.List;
import java.util.Map;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;

client
    .setPayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        List.of(id(0), id(3), id(10)),
        true,
        null,
        null)
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.SetPayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
    ids: new ulong[] { 0, 3, 10 }
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

client.SetPayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

You don’t need to know the ids of the points you want to modify. The alternative
is to use filters.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
    "filter": {
        "must": [\
            {\
                "key": "color",\
                "match": {\
                    "value": "red"\
                }\
            }\
        ]
    }
}

```

```python
client.set_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
    points=models.Filter(
        must=[\
            models.FieldCondition(\
                key="color",\
                match=models.MatchValue(value="red"),\
            ),\
        ],
    ),
)

```

```typescript
client.setPayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
  filter: {
    must: [\
      {\
        key: "color",\
        match: {\
          value: "red",\
        },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, SetPayloadPointsBuilder};
use qdrant_client::Payload;
use serde_json::json;

client
    .set_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
        )
        .points_selector(Filter::must([Condition::matches(\
            "color",\
            "red".to_string(),\
        )]))
        .wait(true),
    )
    .await?;

```

```java
import java.util.Map;

import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.ValueFactory.value;

client
    .setPayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true,
        null,
        null)
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.SetPayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
    filter: MatchKeyword("color", "red")
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

client.SetPayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelectorFilter(&qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatch("color", "red"),
        },
    }),
})

```

_Available as of v1.8.0_

It is possible to modify only a specific key of the payload by using the `key` parameter.

For instance, given the following payload JSON object on a point:

```json
{
    "property1": {
        "nested_property": "foo",
    },
    "property2": {
        "nested_property": "bar",
    }
}

```

You can modify the `nested_property` of `property1` with the following request:

```http
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "nested_property": "qux",
    },
    "key": "property1",
    "points": [1]
}

```

Resulting in the following payload:

```json
{
    "property1": {
        "nested_property": "qux",
    },
    "property2": {
        "nested_property": "bar",
    }
}

```

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#overwrite-payload) Overwrite payload

Fully replace any existing payload with the given one.

REST API ( [Schema](https://api.qdrant.tech/api-reference/points/overwrite-payload)):

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
    "points": [\
        0, 3, 100\
    ]
}

```

```python
client.overwrite_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
    points=[0, 3, 10],
)

```

```typescript
client.overwritePayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
  points: [0, 3, 10],
});

```

```rust
use qdrant_client::qdrant::{PointsIdsList, SetPayloadPointsBuilder};
use qdrant_client::Payload;
use serde_json::json;

client
    .overwrite_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;

client
    .overwritePayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        List.of(id(0), id(3), id(10)),
        true,
        null,
        null)
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.OverwritePayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
    ids: new ulong[] { 0, 3, 10 }
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

client.OverwritePayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

Like [set payload](https://qdrant.tech/documentation/concepts/payload/#set-payload), you don’t need to know the ids of the points
you want to modify. The alternative is to use filters.

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#clear-payload) Clear payload

This method removes all payload keys from specified points

REST API ( [Schema](https://api.qdrant.tech/api-reference/points/clear-payload)):

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/payload/clear
{
    "points": [0, 3, 100]
}

```

```python
client.clear_payload(
    collection_name="{collection_name}",
    points_selector=[0, 3, 100],
)

```

```typescript
client.clearPayload("{collection_name}", {
  points: [0, 3, 100],
});

```

```rust
use qdrant_client::qdrant::{ClearPayloadPointsBuilder, PointsIdsList};

client
    .clear_payload(
        ClearPayloadPointsBuilder::new("{collection_name}")
            .points(PointsIdsList {
                ids: vec![0.into(), 3.into(), 10.into()],
            })
            .wait(true),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.PointIdFactory.id;

client
    .clearPayloadAsync("{collection_name}", List.of(id(0), id(3), id(100)), true, null, null)
    .get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ClearPayloadAsync(collectionName: "{collection_name}", ids: new ulong[] { 0, 3, 100 });

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

client.ClearPayload(context.Background(), &qdrant.ClearPayloadPoints{
    CollectionName: "{collection_name}",
    Points: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

### [Anchor](https://qdrant.tech/documentation/concepts/payload/\#delete-payload-keys) Delete payload keys

Delete specific payload keys from points.

REST API ( [Schema](https://api.qdrant.tech/api-reference/points/delete-payload)):

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/payload/delete
{
    "keys": ["color", "price"],
    "points": [0, 3, 100]
}

```

```python
client.delete_payload(
    collection_name="{collection_name}",
    keys=["color", "price"],
    points=[0, 3, 100],
)

```

```typescript
client.deletePayload("{collection_name}", {
  keys: ["color", "price"],
  points: [0, 3, 100],
});

```

```rust
use qdrant_client::qdrant::{DeletePayloadPointsBuilder, PointsIdsList};

client
    .delete_payload(
        DeletePayloadPointsBuilder::new(
            "{collection_name}",
            vec!["color".to_string(), "price".to_string()],
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.PointIdFactory.id;

client
    .deletePayloadAsync(
        "{collection_name}",
        List.of("color", "price"),
        List.of(id(0), id(3), id(100)),
        true,
        null,
        null)
    .get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeletePayloadAsync(
    collectionName: "{collection_name}",
    keys: ["color", "price"],
    ids: new ulong[] { 0, 3, 100 }
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

client.DeletePayload(context.Background(), &qdrant.DeletePayloadPoints{
    CollectionName: "{collection_name}",
    Keys:           []string{"color", "price"},
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

Alternatively, you can use filters to delete payload keys from the points.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/payload/delete
{
    "keys": ["color", "price"],
    "filter": {
        "must": [\
            {\
                "key": "color",\
                "match": {\
                    "value": "red"\
                }\
            }\
        ]
    }
}

```

```python
client.delete_payload(
    collection_name="{collection_name}",
    keys=["color", "price"],
    points=models.Filter(
        must=[\
            models.FieldCondition(\
                key="color",\
                match=models.MatchValue(value="red"),\
            ),\
        ],
    ),
)

```

```typescript
client.deletePayload("{collection_name}", {
  keys: ["color", "price"],
  filter: {
    must: [\
      {\
        key: "color",\
        match: {\
          value: "red",\
        },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, DeletePayloadPointsBuilder, Filter};

client
    .delete_payload(
        DeletePayloadPointsBuilder::new(
            "{collection_name}",
            vec!["color".to_string(), "price".to_string()],
        )
        .points_selector(Filter::must([Condition::matches(\
            "color",\
            "red".to_string(),\
        )]))
        .wait(true),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.matchKeyword;

client
    .deletePayloadAsync(
        "{collection_name}",
        List.of("color", "price"),
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true,
        null,
        null)
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.DeletePayloadAsync(
    collectionName: "{collection_name}",
    keys: ["color", "price"],
    filter: MatchKeyword("color", "red")
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

client.DeletePayload(context.Background(), &qdrant.DeletePayloadPoints{
    CollectionName: "{collection_name}",
    Keys:           []string{"color", "price"},
    PointsSelector: qdrant.NewPointsSelectorFilter(
        &qdrant.Filter{
            Must: []*qdrant.Condition{qdrant.NewMatch("color", "red")},
        },
    ),
})

```

## [Anchor](https://qdrant.tech/documentation/concepts/payload/\#payload-indexing) Payload indexing

To search more efficiently with filters, Qdrant allows you to create indexes for payload fields by specifying the name and type of field it is intended to be.

The indexed fields also affect the vector index. See [Indexing](https://qdrant.tech/documentation/concepts/indexing/) for details.

In practice, we recommend creating an index on those fields that could potentially constrain the results the most.
For example, using an index for the object ID will be much more efficient, being unique for each record, than an index by its color, which has only a few possible values.

In compound queries involving multiple fields, Qdrant will attempt to use the most restrictive index first.

To create index for the field, you can use the following:

REST API ( [Schema](https://api.qdrant.tech/api-reference/indexes/create-field-index))

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": "keyword"
}

```

```python
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema="keyword",
)

```

```typescript
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: "keyword",
});

```

```rust
use qdrant_client::qdrant::{CreateFieldIndexCollectionBuilder, FieldType};

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Keyword,
        )
        .wait(true),
    )
    .await?;

```

```java
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

client.createPayloadIndexAsync(
    "{collection_name}",
    "name_of_the_field_to_index",
    PayloadSchemaType.Keyword,
    null,
    true,
    null,
    null);

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
    collectionName: "{collection_name}",
    fieldName: "name_of_the_field_to_index"
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
    CollectionName: "{collection_name}",
    FieldName:      "name_of_the_field_to_index",
    FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
})

```

The index usage flag is displayed in the payload schema with the [collection info API](https://api.qdrant.tech/api-reference/collections/get-collection).

Payload schema example:

```json
{
    "payload_schema": {
        "property1": {
            "data_type": "keyword"
        },
        "property2": {
            "data_type": "integer"
        }
    }
}

```

## [Anchor](https://qdrant.tech/documentation/concepts/payload/\#facet-counts) Facet counts

_Available as of v1.12.0_

Faceting is a special counting technique that can be used for various purposes:

- Know which unique values exist for a payload key.
- Know the number of points that contain each unique value.
- Know how restrictive a filter would become by matching a specific value.

Specifically, it is a counting aggregation for the values in a field, akin to a `GROUP BY` with `COUNT(*)` commands in SQL.

These results for a specific field is called a “facet”. For example, when you look at an e-commerce search results page, you might see a list of brands on the sidebar, showing the number of products for each brand. This would be a facet for a `"brand"` field.

To get the facet counts for a field, you can use the following:

REST API ( [Facet](https://api.qdrant.tech/v-1-13-x/api-reference/points/facet))

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/facet
{
    "key": "size",
    "filter": {
      "must": {
        "key": "color",
        "match": { "value": "red" }
      }
    }
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.facet(
    collection_name="{collection_name}",
    key="size",
    facet_filter=models.Filter(must=[models.Match("color", "red")]),
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.facet("{collection_name}", {
    filter: {
        must: [\
            {\
                key: "color",\
                match: {\
                    value: "red",\
                },\
            },\
        ],
    },
    key: "size",
});

```

```rust
use qdrant_client::qdrant::{Condition, FacetCountsBuilder, Filter};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .facet(
         FacetCountsBuilder::new("{collection_name}", "size")
             .limit(10)
             .filter(Filter::must(vec![Condition::matches(\
                 "color",\
                 "red".to_string(),\
             )])),
     )
     .await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

import static io.qdrant.client.ConditionFactory.matchKeyword;
import io.qdrant.client.grpc.Points;
import io.qdrant.client.grpc.Filter;

QdrantClient client = new QdrantClient(
                QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .facetAsync(
        Points.FacetCounts.newBuilder()
            .setCollectionName(collection_name)
            .setKey("size")
            .setFilter(Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
            .build())
        .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.FacetAsync(
    "{collection_name}",
    key: "size",
    filter: MatchKeyword("color", "red")
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

res, err := client.Facet(ctx, &qdrant.FacetCounts{
    CollectionName: "{collection_name}",
    Key:            "size",
        Filter: &qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatch("color", "red"),
        },
    },
})

```

The response will contain the counts for each unique value in the field:

```json
{
  "response": {
    "hits": [\
      {"value": "L", "count": 19},\
      {"value": "S", "count": 10},\
      {"value": "M", "count": 5},\
      {"value": "XL", "count": 1},\
      {"value": "XXL", "count": 1}\
    ]
  },
  "time": 0.0001
}

```

The results are sorted by the count in descending order, then by the value in ascending order.
Only values with non-zero counts will be returned.

By default, the way Qdrant the counts for each value is approximate to achieve fast results. This should accurate enough for most cases, but if you need to debug your storage, you can use the `exact` parameter to get exact counts.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/facet
{
    "key": "size",
    "exact": true
}

```

```python
client.facet(
    collection_name="{collection_name}",
    key="size",
    exact=True,
)

```

```typescript
client.facet("{collection_name}", {
    key: "size",
    exact: true,
});

```

```rust
use qdrant_client::qdrant::FacetCountsBuilder;

client
    .facet(
         FacetCountsBuilder::new("{collection_name}", "size")
             .limit(10)
             .exact(true),
     )
     .await?;

```

```java
 client
      .facetAsync(
          Points.FacetCounts.newBuilder()
              .setCollectionName(collection_name)
              .setKey("foo")
              .setExact(true)
              .build())
      .get();

```

```csharp
using Qdrant.Client;

await client.FacetAsync(
    "{collection_name}",
    key: "size",
    exact: true,
);

```

```go
res, err := client.Facet(ctx, &qdrant.FacetCounts{
    CollectionName: "{collection_name}",
    Key:            "key",
    Exact:          true,
})

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/payload.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/payload.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575341992&cv=11&fst=1748575341992&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fpayload%2F&hn=www.googleadservices.com&frm=0&tiba=Payload%20-%20Qdrant&npa=0&pscdl=noapi&auid=1657839847.1748575342&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575341943&cv=11&fst=1748575341943&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fpayload%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Payload%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1657839847.1748575342&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9641a24d-4293-4412-9bb5-994ae7082914&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5020ca99-3470-4a68-99fb-551b43996a97&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fpayload%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9641a24d-4293-4412-9bb5-994ae7082914&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5020ca99-3470-4a68-99fb-551b43996a97&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fpayload%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575343055&cv=11&fst=1748575343055&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fpayload%2F&hn=www.googleadservices.com&frm=0&tiba=Payload%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1657839847.1748575342&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)