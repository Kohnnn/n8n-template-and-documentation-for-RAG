---
url: "https://qdrant.tech/documentation/concepts/filtering/"
title: "Filtering - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Filtering

# [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#filtering) Filtering

With Qdrant, you can set conditions when searching or retrieving points.
For example, you can impose conditions on both the [payload](https://qdrant.tech/documentation/concepts/payload/) and the `id` of the point.

Setting additional conditions is important when it is impossible to express all the features of the object in the embedding.
Examples include a variety of business requirements: stock availability, user location, or desired price range.

## [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#related-content) Related Content

| [A Complete Guide to Filtering in Vector Search](https://qdrant.tech/articles/vector-search-filtering/) | Developer advice on proper usage and advanced practices. |
| --- | --- |

## [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#filtering-clauses) Filtering clauses

Qdrant allows you to combine conditions in clauses.
Clauses are different logical operations, such as `OR`, `AND`, and `NOT`.
Clauses can be recursively nested into each other so that you can reproduce an arbitrary boolean expression.

Let’s take a look at the clauses implemented in Qdrant.

Suppose we have a set of points with the following payload:

```json
[\
  { "id": 1, "city": "London", "color": "green" },\
  { "id": 2, "city": "London", "color": "red" },\
  { "id": 3, "city": "London", "color": "blue" },\
  { "id": 4, "city": "Berlin", "color": "red" },\
  { "id": 5, "city": "Moscow", "color": "green" },\
  { "id": 6, "city": "Moscow", "color": "blue" }\
]

```

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#must) Must

Example:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [\
            { "key": "city", "match": { "value": "London" } },\
            { "key": "color", "match": { "value": "red" } }\
        ]
    }
    ...
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[\
            models.FieldCondition(\
                key="city",\
                match=models.MatchValue(value="London"),\
            ),\
            models.FieldCondition(\
                key="color",\
                match=models.MatchValue(value="red"),\
            ),\
        ]
    ),
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.scroll("{collection_name}", {
  filter: {
    must: [\
      {\
        key: "city",\
        match: { value: "London" },\
      },\
      {\
        key: "color",\
        match: { value: "red" },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must([\
            Condition::matches("city", "london".to_string()),\
            Condition::matches("color", "red".to_string()),\
        ])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addAllMust(
                        List.of(matchKeyword("city", "London"), matchKeyword("color", "red")))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

// & operator combines two conditions in an AND conjunction(must)
await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("city", "London") & MatchKeyword("color", "red")
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("city", "London"),
			qdrant.NewMatch("color", "red"),
		},
	},
})

```

Filtered points would be:

```json
[{ "id": 2, "city": "London", "color": "red" }]

```

When using `must`, the clause becomes `true` only if every condition listed inside `must` is satisfied.
In this sense, `must` is equivalent to the operator `AND`.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#should) Should

Example:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "should": [\
            { "key": "city", "match": { "value": "London" } },\
            { "key": "color", "match": { "value": "red" } }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        should=[\
            models.FieldCondition(\
                key="city",\
                match=models.MatchValue(value="London"),\
            ),\
            models.FieldCondition(\
                key="color",\
                match=models.MatchValue(value="red"),\
            ),\
        ]
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    should: [\
      {\
        key: "city",\
        match: { value: "London" },\
      },\
      {\
        key: "color",\
        match: { value: "red" },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::should([\
            Condition::matches("city", "london".to_string()),\
            Condition::matches("color", "red".to_string()),\
        ])),
    )
    .await?;

```

```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;
import java.util.List;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addAllShould(
                        List.of(matchKeyword("city", "London"), matchKeyword("color", "red")))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

// | operator combines two conditions in an OR disjunction(should)
await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("city", "London") | MatchKeyword("color", "red")
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Should: []*qdrant.Condition{
			qdrant.NewMatch("city", "London"),
			qdrant.NewMatch("color", "red"),
		},
	},
})

```

Filtered points would be:

```json
[\
  { "id": 1, "city": "London", "color": "green" },\
  { "id": 2, "city": "London", "color": "red" },\
  { "id": 3, "city": "London", "color": "blue" },\
  { "id": 4, "city": "Berlin", "color": "red" }\
]

```

When using `should`, the clause becomes `true` if at least one condition listed inside `should` is satisfied.
In this sense, `should` is equivalent to the operator `OR`.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#must-not) Must Not

Example:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must_not": [\
            { "key": "city", "match": { "value": "London" } },\
            { "key": "color", "match": { "value": "red" } }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must_not=[\
            models.FieldCondition(key="city", match=models.MatchValue(value="London")),\
            models.FieldCondition(key="color", match=models.MatchValue(value="red")),\
        ]
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must_not: [\
      {\
        key: "city",\
        match: { value: "London" },\
      },\
      {\
        key: "color",\
        match: { value: "red" },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must_not([\
            Condition::matches("city", "london".to_string()),\
            Condition::matches("color", "red".to_string()),\
        ])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addAllMustNot(
                        List.of(matchKeyword("city", "London"), matchKeyword("color", "red")))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

// The ! operator negates the condition(must not)
await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: !(MatchKeyword("city", "London") & MatchKeyword("color", "red"))
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		MustNot: []*qdrant.Condition{
			qdrant.NewMatch("city", "London"),
			qdrant.NewMatch("color", "red"),
		},
	},
})

```

Filtered points would be:

```json
[\
  { "id": 5, "city": "Moscow", "color": "green" },\
  { "id": 6, "city": "Moscow", "color": "blue" }\
]

```

When using `must_not`, the clause becomes `true` if none of the conditions listed inside `should` is satisfied.
In this sense, `must_not` is equivalent to the expression `(NOT A) AND (NOT B) AND (NOT C)`.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#clauses-combination) Clauses combination

It is also possible to use several clauses simultaneously:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [\
            { "key": "city", "match": { "value": "London" } }\
        ],
        "must_not": [\
            { "key": "color", "match": { "value": "red" } }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[\
            models.FieldCondition(key="city", match=models.MatchValue(value="London")),\
        ],
        must_not=[\
            models.FieldCondition(key="color", match=models.MatchValue(value="red")),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [\
      {\
        key: "city",\
        match: { value: "London" },\
      },\
    ],
    must_not: [\
      {\
        key: "color",\
        match: { value: "red" },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter {
            must: vec![Condition::matches("city", "London".to_string())],
            must_not: vec![Condition::matches("color", "red".to_string())],
            ..Default::default()
        }),
    )
    .await?;

```

```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(matchKeyword("city", "London"))
                    .addMustNot(matchKeyword("color", "red"))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("city", "London") & !MatchKeyword("color", "red")
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("city", "London"),
		},
		MustNot: []*qdrant.Condition{
			qdrant.NewMatch("color", "red"),
		},
	},
})

```

Filtered points would be:

```json
[\
  { "id": 1, "city": "London", "color": "green" },\
  { "id": 3, "city": "London", "color": "blue" }\
]

```

In this case, the conditions are combined by `AND`.

Also, the conditions could be recursively nested. Example:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must_not": [\
            {\
                "must": [\
                    { "key": "city", "match": { "value": "London" } },\
                    { "key": "color", "match": { "value": "red" } }\
                ]\
            }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must_not=[\
            models.Filter(\
                must=[\
                    models.FieldCondition(\
                        key="city", match=models.MatchValue(value="London")\
                    ),\
                    models.FieldCondition(\
                        key="color", match=models.MatchValue(value="red")\
                    ),\
                ],\
            ),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must_not: [\
      {\
        must: [\
          {\
            key: "city",\
            match: { value: "London" },\
          },\
          {\
            key: "color",\
            match: { value: "red" },\
          },\
        ],\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must_not([Filter::must(\
            [\
                Condition::matches("city", "London".to_string()),\
                Condition::matches("color", "red".to_string()),\
            ],\
        )\
        .into()])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.filter;
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMustNot(
                        filter(
                            Filter.newBuilder()
                                .addAllMust(
                                    List.of(
                                        matchKeyword("city", "London"),
                                        matchKeyword("color", "red")))
                                .build()))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: new Filter { MustNot = { MatchKeyword("city", "London") & MatchKeyword("color", "red") } }
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		MustNot: []*qdrant.Condition{
			qdrant.NewFilterAsCondition(&qdrant.Filter{
				Must: []*qdrant.Condition{
					qdrant.NewMatch("city", "London"),
					qdrant.NewMatch("color", "red"),
				},
			}),
		},
	},
})

```

Filtered points would be:

```json
[\
  { "id": 1, "city": "London", "color": "green" },\
  { "id": 3, "city": "London", "color": "blue" },\
  { "id": 4, "city": "Berlin", "color": "red" },\
  { "id": 5, "city": "Moscow", "color": "green" },\
  { "id": 6, "city": "Moscow", "color": "blue" }\
]

```

## [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#filtering-conditions) Filtering conditions

Different types of values in payload correspond to different kinds of queries that we can apply to them.
Let’s look at the existing condition variants and what types of data they apply to.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#match) Match

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "color",
  "match": {
    "value": "red"
  }
}

```

```python
models.FieldCondition(
    key="color",
    match=models.MatchValue(value="red"),
)

```

```typescript
{
    key: 'color',
    match: {value: 'red'}
}

```

```rust
Condition::matches("color", "red".to_string())

```

```java
matchKeyword("color", "red");

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchKeyword("color", "red");

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatch("color", "red")

```

For the other types, the match condition will look exactly the same, except for the type used:

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "count",
  "match": {
    "value": 0
  }
}

```

```python
models.FieldCondition(
    key="count",
    match=models.MatchValue(value=0),
)

```

```typescript
{
    key: 'count',
    match: {value: 0}
}

```

```rust
Condition::matches("count", 0)

```

```java
import static io.qdrant.client.ConditionFactory.match;

match("count", 0);

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

Match("count", 0);

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchInt("count", 0)

```

The simplest kind of condition is one that checks if the stored value equals the given one.
If several values are stored, at least one of them should match the condition.
You can apply it to [keyword](https://qdrant.tech/documentation/concepts/payload/#keyword), [integer](https://qdrant.tech/documentation/concepts/payload/#integer) and [bool](https://qdrant.tech/documentation/concepts/payload/#bool) payloads.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#match-any) Match Any

_Available as of v1.1.0_

In case you want to check if the stored value is one of multiple values, you can use the Match Any condition.
Match Any works as a logical OR for the given values. It can also be described as a `IN` operator.

You can apply it to [keyword](https://qdrant.tech/documentation/concepts/payload/#keyword) and [integer](https://qdrant.tech/documentation/concepts/payload/#integer) payloads.

Example:

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "color",
  "match": {
    "any": ["black", "yellow"]
  }
}

```

```python
models.FieldCondition(
    key="color",
    match=models.MatchAny(any=["black", "yellow"]),
)

```

```typescript
{
    key: 'color',
    match: {any: ['black', 'yellow']}
}

```

```rust
Condition::matches("color", vec!["black".to_string(), "yellow".to_string()])

```

```java
import static io.qdrant.client.ConditionFactory.matchKeywords;

matchKeywords("color", List.of("black", "yellow"));

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

Match("color", ["black", "yellow"]);

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchKeywords("color", "black", "yellow")

```

In this example, the condition will be satisfied if the stored value is either `black` or `yellow`.

If the stored value is an array, it should have at least one value matching any of the given values. E.g. if the stored value is `["black", "green"]`, the condition will be satisfied, because `"black"` is in `["black", "yellow"]`.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#match-except) Match Except

_Available as of v1.2.0_

In case you want to check if the stored value is not one of multiple values, you can use the Match Except condition.
Match Except works as a logical NOR for the given values.
It can also be described as a `NOT IN` operator.

You can apply it to [keyword](https://qdrant.tech/documentation/concepts/payload/#keyword) and [integer](https://qdrant.tech/documentation/concepts/payload/#integer) payloads.

Example:

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "color",
  "match": {
    "except": ["black", "yellow"]
  }
}

```

```python
models.FieldCondition(
    key="color",
    match=models.MatchExcept(**{"except": ["black", "yellow"]}),
)

```

```typescript
{
    key: 'color',
    match: {except: ['black', 'yellow']}
}

```

```rust
use qdrant_client::qdrant::r#match::MatchValue;

Condition::matches(
    "color",
    !MatchValue::from(vec!["black".to_string(), "yellow".to_string()]),
)

```

```java
import static io.qdrant.client.ConditionFactory.matchExceptKeywords;

matchExceptKeywords("color", List.of("black", "yellow"));

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

Match("color", ["black", "yellow"]);

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchExcept("color", "black", "yellow")

```

In this example, the condition will be satisfied if the stored value is neither `black` nor `yellow`.

If the stored value is an array, it should have at least one value not matching any of the given values. E.g. if the stored value is `["black", "green"]`, the condition will be satisfied, because `"green"` does not match `"black"` nor `"yellow"`.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#nested-key) Nested key

_Available as of v1.1.0_

Payloads being arbitrary JSON object, it is likely that you will need to filter on a nested field.

For convenience, we use a syntax similar to what can be found in the [Jq](https://stedolan.github.io/jq/manual/#Basicfilters) project.

Suppose we have a set of points with the following payload:

```json
[\
  {\
    "id": 1,\
    "country": {\
      "name": "Germany",\
      "cities": [\
        {\
          "name": "Berlin",\
          "population": 3.7,\
          "sightseeing": ["Brandenburg Gate", "Reichstag"]\
        },\
        {\
          "name": "Munich",\
          "population": 1.5,\
          "sightseeing": ["Marienplatz", "Olympiapark"]\
        }\
      ]\
    }\
  },\
  {\
    "id": 2,\
    "country": {\
      "name": "Japan",\
      "cities": [\
        {\
          "name": "Tokyo",\
          "population": 9.3,\
          "sightseeing": ["Tokyo Tower", "Tokyo Skytree"]\
        },\
        {\
          "name": "Osaka",\
          "population": 2.7,\
          "sightseeing": ["Osaka Castle", "Universal Studios Japan"]\
        }\
      ]\
    }\
  }\
]

```

You can search on a nested field using a dot notation.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "should": [\
            {\
                "key": "country.name",\
                "match": {\
                    "value": "Germany"\
                }\
            }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        should=[\
            models.FieldCondition(\
                key="country.name", match=models.MatchValue(value="Germany")\
            ),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    should: [\
      {\
        key: "country.name",\
        match: { value: "Germany" },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::should([\
            Condition::matches("country.name", "Germany".to_string()),\
        ])),
    )
    .await?;

```

```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addShould(matchKeyword("country.name", "Germany"))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(collectionName: "{collection_name}", filter: MatchKeyword("country.name", "Germany"));

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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Should: []*qdrant.Condition{
			qdrant.NewMatch("country.name", "Germany"),
		},
	},
})

```

You can also search through arrays by projecting inner values using the `[]` syntax.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "should": [\
            {\
                "key": "country.cities[].population",\
                "range": {\
                    "gte": 9.0,\
                }\
            }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        should=[\
            models.FieldCondition(\
                key="country.cities[].population",\
                range=models.Range(\
                    gt=None,\
                    gte=9.0,\
                    lt=None,\
                    lte=None,\
                ),\
            ),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    should: [\
      {\
        key: "country.cities[].population",\
        range: {\
          gt: null,\
          gte: 9.0,\
          lt: null,\
          lte: null,\
        },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, Range, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::should([\
            Condition::range(\
                "country.cities[].population",\
                Range {\
                    gte: Some(9.0),\
                    ..Default::default()\
                },\
            ),\
        ])),
    )
    .await?;

```

```java
import static io.qdrant.client.ConditionFactory.range;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.Range;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addShould(
                        range(
                            "country.cities[].population",
                            Range.newBuilder().setGte(9.0).build()))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: Range("country.cities[].population", new Qdrant.Client.Grpc.Range { Gte = 9.0 })
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Should: []*qdrant.Condition{
			qdrant.NewRange("country.cities[].population", &qdrant.Range{
				Gte: qdrant.PtrOf(9.0),
			}),
		},
	},
})

```

This query would only output the point with id 2 as only Japan has a city with population greater than 9.0.

And the leaf nested field can also be an array.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "should": [\
            {\
                "key": "country.cities[].sightseeing",\
                "match": {\
                    "value": "Osaka Castle"\
                }\
            }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        should=[\
            models.FieldCondition(\
                key="country.cities[].sightseeing",\
                match=models.MatchValue(value="Osaka Castle"),\
            ),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    should: [\
      {\
        key: "country.cities[].sightseeing",\
        match: { value: "Osaka Castle" },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::should([\
            Condition::matches("country.cities[].sightseeing", "Osaka Castle".to_string()),\
        ])),
    )
    .await?;

```

```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addShould(matchKeyword("country.cities[].sightseeing", "Germany"))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("country.cities[].sightseeing", "Germany")
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Should: []*qdrant.Condition{
			qdrant.NewMatch("country.cities[].sightseeing", "Germany"),
		},
	},
})

```

This query would only output the point with id 2 as only Japan has a city with the “Osaka castke” as part of the sightseeing.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#nested-object-filter) Nested object filter

_Available as of v1.2.0_

By default, the conditions are taking into account the entire payload of a point.

For instance, given two points with the following payload:

```json
[\
  {\
    "id": 1,\
    "dinosaur": "t-rex",\
    "diet": [\
      { "food": "leaves", "likes": false},\
      { "food": "meat", "likes": true}\
    ]\
  },\
  {\
    "id": 2,\
    "dinosaur": "diplodocus",\
    "diet": [\
      { "food": "leaves", "likes": true},\
      { "food": "meat", "likes": false}\
    ]\
  }\
]

```

The following query would match both points:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [\
            {\
                "key": "diet[].food",\
                  "match": {\
                    "value": "meat"\
                }\
            },\
            {\
                "key": "diet[].likes",\
                  "match": {\
                    "value": true\
                }\
            }\
        ]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[\
            models.FieldCondition(\
                key="diet[].food", match=models.MatchValue(value="meat")\
            ),\
            models.FieldCondition(\
                key="diet[].likes", match=models.MatchValue(value=True)\
            ),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [\
      {\
        key: "diet[].food",\
        match: { value: "meat" },\
      },\
      {\
        key: "diet[].likes",\
        match: { value: true },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must([\
            Condition::matches("diet[].food", "meat".to_string()),\
            Condition::matches("diet[].likes", true),\
        ])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addAllMust(
                        List.of(matchKeyword("diet[].food", "meat"), match("diet[].likes", true)))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("diet[].food", "meat") & Match("diet[].likes", true)
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("diet[].food", "meat"),
			qdrant.NewMatchBool("diet[].likes", true),
		},
	},
})

```

This happens because both points are matching the two conditions:

- the “t-rex” matches food=meat on `diet[1].food` and likes=true on `diet[1].likes`
- the “diplodocus” matches food=meat on `diet[1].food` and likes=true on `diet[0].likes`

To retrieve only the points which are matching the conditions on an array element basis, that is the point with id 1 in this example, you would need to use a nested object filter.

Nested object filters allow arrays of objects to be queried independently of each other.

It is achieved by using the `nested` condition type formed by a payload key to focus on and a filter to apply.

The key should point to an array of objects and can be used with or without the bracket notation (“data” or “data\[\]”).

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [{\
            "nested": {\
                "key": "diet",\
                "filter":{\
                    "must": [\
                        {\
                            "key": "food",\
                            "match": {\
                                "value": "meat"\
                            }\
                        },\
                        {\
                            "key": "likes",\
                            "match": {\
                                "value": true\
                            }\
                        }\
                    ]\
                }\
            }\
        }]
    }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[\
            models.NestedCondition(\
                nested=models.Nested(\
                    key="diet",\
                    filter=models.Filter(\
                        must=[\
                            models.FieldCondition(\
                                key="food", match=models.MatchValue(value="meat")\
                            ),\
                            models.FieldCondition(\
                                key="likes", match=models.MatchValue(value=True)\
                            ),\
                        ]\
                    ),\
                )\
            )\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [\
      {\
        nested: {\
          key: "diet",\
          filter: {\
            must: [\
              {\
                key: "food",\
                match: { value: "meat" },\
              },\
              {\
                key: "likes",\
                match: { value: true },\
              },\
            ],\
          },\
        },\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, NestedCondition, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must([NestedCondition {\
            key: "diet".to_string(),\
            filter: Some(Filter::must([\
                Condition::matches("food", "meat".to_string()),\
                Condition::matches("likes", true),\
            ])),\
        }\
        .into()])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.ConditionFactory.nested;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(
                        nested(
                            "diet",
                            Filter.newBuilder()
                                .addAllMust(
                                    List.of(
                                        matchKeyword("food", "meat"), match("likes", true)))
                                .build()))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: Nested("diet", MatchKeyword("food", "meat") & Match("likes", true))
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewNestedFilter("diet", &qdrant.Filter{
				Must: []*qdrant.Condition{
					qdrant.NewMatch("food", "meat"),
					qdrant.NewMatchBool("likes", true),
				},
			}),
		},
	},
})

```

The matching logic is modified to be applied at the level of an array element within the payload.

Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time.
Parent document is considered to match the condition if at least one element of the array matches the nested filter.

**Limitations**

The `has_id` condition is not supported within the nested object filter. If you need it, place it in an adjacent `must` clause.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
   "filter":{
      "must":[\
         {\
            "nested":{\
               "key":"diet",\
               "filter":{\
                  "must":[\
                     {\
                        "key":"food",\
                        "match":{\
                           "value":"meat"\
                        }\
                     },\
                     {\
                        "key":"likes",\
                        "match":{\
                           "value":true\
                        }\
                     }\
                  ]\
               }\
            }\
         },\
         {\
            "has_id":[\
               1\
            ]\
         }\
      ]
   }
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[\
            models.NestedCondition(\
                nested=models.Nested(\
                    key="diet",\
                    filter=models.Filter(\
                        must=[\
                            models.FieldCondition(\
                                key="food", match=models.MatchValue(value="meat")\
                            ),\
                            models.FieldCondition(\
                                key="likes", match=models.MatchValue(value=True)\
                            ),\
                        ]\
                    ),\
                )\
            ),\
            models.HasIdCondition(has_id=[1]),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [\
      {\
        nested: {\
          key: "diet",\
          filter: {\
            must: [\
              {\
                key: "food",\
                match: { value: "meat" },\
              },\
              {\
                key: "likes",\
                match: { value: true },\
              },\
            ],\
          },\
        },\
      },\
      {\
        has_id: [1],\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, NestedCondition, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must([\
            NestedCondition {\
                key: "diet".to_string(),\
                filter: Some(Filter::must([\
                    Condition::matches("food", "meat".to_string()),\
                    Condition::matches("likes", true),\
                ])),\
            }\
            .into(),\
            Condition::has_id([1]),\
        ])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.hasId;
import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.ConditionFactory.nested;
import static io.qdrant.client.PointIdFactory.id;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(
                        nested(
                            "diet",
                            Filter.newBuilder()
                                .addAllMust(
                                    List.of(
                                        matchKeyword("food", "meat"), match("likes", true)))
                                .build()))
                    .addMust(hasId(id(1)))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: Nested("diet", MatchKeyword("food", "meat") & Match("likes", true)) & HasId(1)
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewNestedFilter("diet", &qdrant.Filter{
				Must: []*qdrant.Condition{
					qdrant.NewMatch("food", "meat"),
					qdrant.NewMatchBool("likes", true),
				},
			}),
			qdrant.NewHasID(qdrant.NewIDNum(1)),
		},
	},
})

```

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#full-text-match) Full Text Match

_Available as of v0.10.0_

A special case of the `match` condition is the `text` match condition.
It allows you to search for a specific substring, token or phrase within the text field.

Exact texts that will match the condition depend on full-text index configuration.
Configuration is defined during the index creation and describe at [full-text index](https://qdrant.tech/documentation/concepts/indexing/#full-text-index).

If there is no full-text index for the field, the condition will work as exact substring match.

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "description",
  "match": {
    "text": "good cheap"
  }
}

```

```python
models.FieldCondition(
    key="description",
    match=models.MatchText(text="good cheap"),
)

```

```typescript
{
    key: 'description',
    match: {text: 'good cheap'}
}

```

```rust
use qdrant_client::qdrant::Condition;

Condition::matches_text("description", "good cheap")

```

```java
import static io.qdrant.client.ConditionFactory.matchText;

matchText("description", "good cheap");

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchText("description", "good cheap");

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchText("description", "good cheap")

```

If the query has several words, then the condition will be satisfied only if all of them are present in the text.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#range) Range

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "price",
  "range": {
    "gt": null,
    "gte": 100.0,
    "lt": null,
    "lte": 450.0
  }
}

```

```python
models.FieldCondition(
    key="price",
    range=models.Range(
        gt=None,
        gte=100.0,
        lt=None,
        lte=450.0,
    ),
)

```

```typescript
{
    key: 'price',
    range: {
        gt: null,
        gte: 100.0,
        lt: null,
        lte: 450.0
    }
}

```

```rust
use qdrant_client::qdrant::{Condition, Range};

Condition::range(
    "price",
    Range {
        gt: None,
        gte: Some(100.0),
        lt: None,
        lte: Some(450.0),
    },
)

```

```java
import static io.qdrant.client.ConditionFactory.range;

import io.qdrant.client.grpc.Points.Range;

range("price", Range.newBuilder().setGte(100.0).setLte(450).build());

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

Range("price", new Qdrant.Client.Grpc.Range { Gte = 100.0, Lte = 450 });

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewRange("price", &qdrant.Range{
	Gte: qdrant.PtrOf(100.0),
	Lte: qdrant.PtrOf(450.0),
})

```

The `range` condition sets the range of possible values for stored payload values.
If several values are stored, at least one of them should match the condition.

Comparisons that can be used:

- `gt` \- greater than
- `gte` \- greater than or equal
- `lt` \- less than
- `lte` \- less than or equal

Can be applied to [float](https://qdrant.tech/documentation/concepts/payload/#float) and [integer](https://qdrant.tech/documentation/concepts/payload/#integer) payloads.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#datetime-range) Datetime Range

The datetime range is a unique range condition, used for [datetime](https://qdrant.tech/documentation/concepts/payload/#datetime) payloads, which supports RFC 3339 formats.
You do not need to convert dates to UNIX timestaps. During comparison, timestamps are parsed and converted to UTC.

_Available as of v1.8.0_

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "date",
  "range": {
    "gt": "2023-02-08T10:49:00Z",
    "gte": null,
    "lt": null,
    "lte": "2024-01-31 10:14:31Z"
  }
}

```

```python
models.FieldCondition(
    key="date",
    range=models.DatetimeRange(
        gt="2023-02-08T10:49:00Z",
        gte=None,
        lt=None,
        lte="2024-01-31T10:14:31Z",
    ),
)

```

```typescript
{
    key: 'date',
    range: {
        gt: '2023-02-08T10:49:00Z',
        gte: null,
        lt: null,
        lte: '2024-01-31T10:14:31Z'
    }
}

```

```rust
use qdrant_client::qdrant::{Condition, DatetimeRange, Timestamp};

Condition::datetime_range(
    "date",
    DatetimeRange {
        gt: Some(Timestamp::date_time(2023, 2, 8, 10, 49, 0).unwrap()),
        gte: None,
        lt: None,
        lte: Some(Timestamp::date_time(2024, 1, 31, 10, 14, 31).unwrap()),
    },
)

```

```java
import static io.qdrant.client.ConditionFactory.datetimeRange;

import com.google.protobuf.Timestamp;
import io.qdrant.client.grpc.Points.DatetimeRange;
import java.time.Instant;

long gt = Instant.parse("2023-02-08T10:49:00Z").getEpochSecond();
long lte = Instant.parse("2024-01-31T10:14:31Z").getEpochSecond();

datetimeRange("date",
    DatetimeRange.newBuilder()
        .setGt(Timestamp.newBuilder().setSeconds(gt))
        .setLte(Timestamp.newBuilder().setSeconds(lte))
        .build());

```

```csharp
using Qdrant.Client.Grpc;

Conditions.DatetimeRange(
    field: "date",
    gt: new DateTime(2023, 2, 8, 10, 49, 0, DateTimeKind.Utc),
    lte: new DateTime(2024, 1, 31, 10, 14, 31, DateTimeKind.Utc)
);

```

```go
import (
	"time"

	"github.com/qdrant/go-client/qdrant"
	"google.golang.org/protobuf/types/known/timestamppb"
)

qdrant.NewDatetimeRange("date", &qdrant.DatetimeRange{
	Gt:  timestamppb.New(time.Date(2023, 2, 8, 10, 49, 0, 0, time.UTC)),
	Lte: timestamppb.New(time.Date(2024, 1, 31, 10, 14, 31, 0, time.UTC)),
})

```

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#uuid-match) UUID Match

_Available as of v1.11.0_

Matching of UUID values works similarly to the regular `match` condition for strings.
Functionally, it will work with `keyword` and `uuid` indexes exactly the same, but `uuid` index is more memory efficient.

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "uuid",
  "match": {
    "value": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
  }
}

```

```python
models.FieldCondition(
    key="uuid",
    match=models.MatchValue(value="f47ac10b-58cc-4372-a567-0e02b2c3d479"),
)

```

```typescript
{
    key: 'uuid',
    match: {value: 'f47ac10b-58cc-4372-a567-0e02b2c3d479'}
}

```

```rust
Condition::matches("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479".to_string())

```

```java
matchKeyword("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479");

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchKeyword("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479");

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatch("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479")

```

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#geo) Geo

#### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#geo-bounding-box) Geo Bounding Box

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "location",
  "geo_bounding_box": {
    "bottom_right": {
      "lon": 13.455868,
      "lat": 52.495862
    },
    "top_left": {
      "lon": 13.403683,
      "lat": 52.520711
    }
  }
}

```

```python
models.FieldCondition(
    key="location",
    geo_bounding_box=models.GeoBoundingBox(
        bottom_right=models.GeoPoint(
            lon=13.455868,
            lat=52.495862,
        ),
        top_left=models.GeoPoint(
            lon=13.403683,
            lat=52.520711,
        ),
    ),
)

```

```typescript
{
    key: 'location',
    geo_bounding_box: {
        bottom_right: {
            lon: 13.455868,
            lat: 52.495862
        },
        top_left: {
            lon: 13.403683,
            lat: 52.520711
        }
    }
}

```

```rust
use qdrant_client::qdrant::{Condition, GeoBoundingBox, GeoPoint};

Condition::geo_bounding_box(
    "location",
    GeoBoundingBox {
        bottom_right: Some(GeoPoint {
            lon: 13.455868,
            lat: 52.495862,
        }),
        top_left: Some(GeoPoint {
            lon: 13.403683,
            lat: 52.520711,
        }),
    },
)

```

```java
import static io.qdrant.client.ConditionFactory.geoBoundingBox;

geoBoundingBox("location", 52.520711, 13.403683, 52.495862, 13.455868);

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

GeoBoundingBox("location", 52.520711, 13.403683, 52.495862, 13.455868);

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewGeoBoundingBox("location", 52.520711, 13.403683, 52.495862, 13.455868)

```

It matches with `location` s inside a rectangle with the coordinates of the upper left corner in `bottom_right` and the coordinates of the lower right corner in `top_left`.

#### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#geo-radius) Geo Radius

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "location",
  "geo_radius": {
    "center": {
      "lon": 13.403683,
      "lat": 52.520711
    },
    "radius": 1000.0
  }
}

```

```python
models.FieldCondition(
    key="location",
    geo_radius=models.GeoRadius(
        center=models.GeoPoint(
            lon=13.403683,
            lat=52.520711,
        ),
        radius=1000.0,
    ),
)

```

```typescript
{
    key: 'location',
    geo_radius: {
        center: {
            lon: 13.403683,
            lat: 52.520711
        },
        radius: 1000.0
    }
}

```

```rust
use qdrant_client::qdrant::{Condition, GeoPoint, GeoRadius};

Condition::geo_radius(
    "location",
    GeoRadius {
        center: Some(GeoPoint {
            lon: 13.403683,
            lat: 52.520711,
        }),
        radius: 1000.0,
    },
)

```

```java
import static io.qdrant.client.ConditionFactory.geoRadius;

geoRadius("location", 52.520711, 13.403683, 1000.0f);

```

```csharp
using static Qdrant.Client.Grpc.Conditions;

GeoRadius("location", 52.520711, 13.403683, 1000.0f);

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewGeoRadius("location", 52.520711, 13.403683, 1000.0)

```

It matches with `location` s inside a circle with the `center` at the center and a radius of `radius` meters.

If several values are stored, at least one of them should match the condition.
These conditions can only be applied to payloads that match the [geo-data format](https://qdrant.tech/documentation/concepts/payload/#geo).

#### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#geo-polygon) Geo Polygon

Geo Polygons search is useful for when you want to find points inside an irregularly shaped area, for example a country boundary or a forest boundary. A polygon always has an exterior ring and may optionally include interior rings. A lake with an island would be an example of an interior ring. If you wanted to find points in the water but not on the island, you would make an interior ring for the island.

When defining a ring, you must pick either a clockwise or counterclockwise ordering for your points. The first and last point of the polygon must be the same.

Currently, we only support unprojected global coordinates (decimal degrees longitude and latitude) and we are datum agnostic.

jsonpythontypescriptrustjavacsharpgo

```json

{
  "key": "location",
  "geo_polygon": {
    "exterior": {
      "points": [\
        { "lon": -70.0, "lat": -70.0 },\
        { "lon": 60.0, "lat": -70.0 },\
        { "lon": 60.0, "lat": 60.0 },\
        { "lon": -70.0, "lat": 60.0 },\
        { "lon": -70.0, "lat": -70.0 }\
      ]
    },
    "interiors": [\
      {\
        "points": [\
          { "lon": -65.0, "lat": -65.0 },\
          { "lon": 0.0, "lat": -65.0 },\
          { "lon": 0.0, "lat": 0.0 },\
          { "lon": -65.0, "lat": 0.0 },\
          { "lon": -65.0, "lat": -65.0 }\
        ]\
      }\
    ]
  }
}

```

```python
models.FieldCondition(
    key="location",
    geo_polygon=models.GeoPolygon(
        exterior=models.GeoLineString(
            points=[\
                models.GeoPoint(\
                    lon=-70.0,\
                    lat=-70.0,\
                ),\
                models.GeoPoint(\
                    lon=60.0,\
                    lat=-70.0,\
                ),\
                models.GeoPoint(\
                    lon=60.0,\
                    lat=60.0,\
                ),\
                models.GeoPoint(\
                    lon=-70.0,\
                    lat=60.0,\
                ),\
                models.GeoPoint(\
                    lon=-70.0,\
                    lat=-70.0,\
                ),\
            ]
        ),
        interiors=[\
            models.GeoLineString(\
                points=[\
                    models.GeoPoint(\
                        lon=-65.0,\
                        lat=-65.0,\
                    ),\
                    models.GeoPoint(\
                        lon=0.0,\
                        lat=-65.0,\
                    ),\
                    models.GeoPoint(\
                        lon=0.0,\
                        lat=0.0,\
                    ),\
                    models.GeoPoint(\
                        lon=-65.0,\
                        lat=0.0,\
                    ),\
                    models.GeoPoint(\
                        lon=-65.0,\
                        lat=-65.0,\
                    ),\
                ]\
            )\
        ],
    ),
)

```

```typescript
{
  key: "location",
  geo_polygon: {
    exterior: {
      points: [\
        {\
          lon: -70.0,\
          lat: -70.0\
        },\
        {\
          lon: 60.0,\
          lat: -70.0\
        },\
        {\
          lon: 60.0,\
          lat: 60.0\
        },\
        {\
          lon: -70.0,\
          lat: 60.0\
        },\
        {\
          lon: -70.0,\
          lat: -70.0\
        }\
      ]
    },
    interiors: [\
      {\
        points: [\
          {\
            lon: -65.0,\
            lat: -65.0\
          },\
          {\
            lon: 0,\
            lat: -65.0\
          },\
          {\
            lon: 0,\
            lat: 0\
          },\
          {\
            lon: -65.0,\
            lat: 0\
          },\
          {\
            lon: -65.0,\
            lat: -65.0\
          }\
        ]\
      }\
    ]
  }
}

```

```rust
use qdrant_client::qdrant::{Condition, GeoLineString, GeoPoint, GeoPolygon};

Condition::geo_polygon(
    "location",
    GeoPolygon {
        exterior: Some(GeoLineString {
            points: vec![\
                GeoPoint {\
                    lon: -70.0,\
                    lat: -70.0,\
                },\
                GeoPoint {\
                    lon: 60.0,\
                    lat: -70.0,\
                },\
                GeoPoint {\
                    lon: 60.0,\
                    lat: 60.0,\
                },\
                GeoPoint {\
                    lon: -70.0,\
                    lat: 60.0,\
                },\
                GeoPoint {\
                    lon: -70.0,\
                    lat: -70.0,\
                },\
            ],
        }),
        interiors: vec![GeoLineString {\
            points: vec![\
                GeoPoint {\
                    lon: -65.0,\
                    lat: -65.0,\
                },\
                GeoPoint {\
                    lon: 0.0,\
                    lat: -65.0,\
                },\
                GeoPoint { lon: 0.0, lat: 0.0 },\
                GeoPoint {\
                    lon: -65.0,\
                    lat: 0.0,\
                },\
                GeoPoint {\
                    lon: -65.0,\
                    lat: -65.0,\
                },\
            ],\
        }],
    },
)

```

```java
import static io.qdrant.client.ConditionFactory.geoPolygon;

import io.qdrant.client.grpc.Points.GeoLineString;
import io.qdrant.client.grpc.Points.GeoPoint;

geoPolygon(
    "location",
    GeoLineString.newBuilder()
        .addAllPoints(
            List.of(
                GeoPoint.newBuilder().setLon(-70.0).setLat(-70.0).build(),
                GeoPoint.newBuilder().setLon(60.0).setLat(-70.0).build(),
                GeoPoint.newBuilder().setLon(60.0).setLat(60.0).build(),
                GeoPoint.newBuilder().setLon(-70.0).setLat(60.0).build(),
                GeoPoint.newBuilder().setLon(-70.0).setLat(-70.0).build()))
        .build(),
    List.of(
        GeoLineString.newBuilder()
            .addAllPoints(
                List.of(
                    GeoPoint.newBuilder().setLon(-65.0).setLat(-65.0).build(),
                    GeoPoint.newBuilder().setLon(0.0).setLat(-65.0).build(),
                    GeoPoint.newBuilder().setLon(0.0).setLat(0.0).build(),
                    GeoPoint.newBuilder().setLon(-65.0).setLat(0.0).build(),
                    GeoPoint.newBuilder().setLon(-65.0).setLat(-65.0).build()))
            .build()));

```

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

GeoPolygon(
	field: "location",
	exterior: new GeoLineString
	{
		Points =
		{
			new GeoPoint { Lat = -70.0, Lon = -70.0 },
			new GeoPoint { Lat = 60.0, Lon = -70.0 },
			new GeoPoint { Lat = 60.0, Lon = 60.0 },
			new GeoPoint { Lat = -70.0, Lon = 60.0 },
			new GeoPoint { Lat = -70.0, Lon = -70.0 }
		}
	},
	interiors: [\
		new()\
		{\
			Points =\
			{\
				new GeoPoint { Lat = -65.0, Lon = -65.0 },\
				new GeoPoint { Lat = 0.0, Lon = -65.0 },\
				new GeoPoint { Lat = 0.0, Lon = 0.0 },\
				new GeoPoint { Lat = -65.0, Lon = 0.0 },\
				new GeoPoint { Lat = -65.0, Lon = -65.0 }\
			}\
		}\
	]
);

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewGeoPolygon("location",
	&qdrant.GeoLineString{
		Points: []*qdrant.GeoPoint{
			{Lat: -70, Lon: -70},
			{Lat: 60, Lon: -70},
			{Lat: 60, Lon: 60},
			{Lat: -70, Lon: 60},
			{Lat: -70, Lon: -70},
		},
	}, &qdrant.GeoLineString{
		Points: []*qdrant.GeoPoint{
			{Lat: -65, Lon: -65},
			{Lat: 0, Lon: -65},
			{Lat: 0, Lon: 0},
			{Lat: -65, Lon: 0},
			{Lat: -65, Lon: -65},
		},
	})

```

A match is considered any point location inside or on the boundaries of the given polygon’s exterior but not inside any interiors.

If several location values are stored for a point, then any of them matching will include that point as a candidate in the resultset.
These conditions can only be applied to payloads that match the [geo-data format](https://qdrant.tech/documentation/concepts/payload/#geo).

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#values-count) Values count

In addition to the direct value comparison, it is also possible to filter by the amount of values.

For example, given the data:

```json
[\
  { "id": 1, "name": "product A", "comments": ["Very good!", "Excellent"] },\
  { "id": 2, "name": "product B", "comments": ["meh", "expected more", "ok"] }\
]

```

We can perform the search only among the items with more than two comments:

jsonpythontypescriptrustjavacsharpgo

```json
{
  "key": "comments",
  "values_count": {
    "gt": 2
  }
}

```

```python
models.FieldCondition(
    key="comments",
    values_count=models.ValuesCount(gt=2),
)

```

```typescript
{
    key: 'comments',
    values_count: {gt: 2}
}

```

```rust
use qdrant_client::qdrant::{Condition, ValuesCount};

Condition::values_count(
    "comments",
    ValuesCount {
        gt: Some(2),
        ..Default::default()
    },
)

```

```java
import static io.qdrant.client.ConditionFactory.valuesCount;

import io.qdrant.client.grpc.Points.ValuesCount;

valuesCount("comments", ValuesCount.newBuilder().setGt(2).build());

```

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

ValuesCount("comments", new ValuesCount { Gt = 2 });

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewValuesCount("comments", &qdrant.ValuesCount{
	Gt: qdrant.PtrOf(uint64(2)),
})

```

The result would be:

```json
[{ "id": 2, "name": "product B", "comments": ["meh", "expected more", "ok"] }]

```

If stored value is not an array - it is assumed that the amount of values is equals to 1.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#is-empty) Is Empty

Sometimes it is also useful to filter out records that are missing some value.
The `IsEmpty` condition may help you with that:

jsonpythontypescriptrustjavacsharpgo

```json
{
  "is_empty": {
    "key": "reports"
  }
}

```

```python
models.IsEmptyCondition(
    is_empty=models.PayloadField(key="reports"),
)

```

```typescript
{
  is_empty: {
    key: "reports"
  }
}

```

```rust
use qdrant_client::qdrant::Condition;

Condition::is_empty("reports")

```

```java
import static io.qdrant.client.ConditionFactory.isEmpty;

isEmpty("reports");

```

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

IsEmpty("reports");

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewIsEmpty("reports")

```

This condition will match all records where the field `reports` either does not exist, or has `null` or `[]` value.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#is-null) Is Null

It is not possible to test for `NULL` values with the **match** condition.
We have to use `IsNull` condition instead:

jsonpythontypescriptrustjavacsharpgo

```json
{
    "is_null": {
        "key": "reports"
    }
}

```

```python
models.IsNullCondition(
    is_null=models.PayloadField(key="reports"),
)

```

```typescript
{
  is_null: {
    key: "reports"
  }
}

```

```rust
use qdrant_client::qdrant::Condition;

Condition::is_null("reports")

```

```java
import static io.qdrant.client.ConditionFactory.isNull;

isNull("reports");

```

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

IsNull("reports");

```

```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewIsNull("reports")

```

This condition will match all records where the field `reports` exists and has `NULL` value.

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#has-id) Has id

This type of query is not related to payload, but can be very useful in some situations.
For example, the user could mark some specific search results as irrelevant, or we want to search only among the specified points.

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [\
            { "has_id": [1,3,5,7,9,11] }\
        ]
    }
    ...
}

```

```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[\
            models.HasIdCondition(has_id=[1, 3, 5, 7, 9, 11]),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [\
      {\
        has_id: [1, 3, 5, 7, 9, 11],\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}")
            .filter(Filter::must([Condition::has_id([1, 3, 5, 7, 9, 11])])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.hasId;
import static io.qdrant.client.PointIdFactory.id;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(hasId(List.of(id(1), id(3), id(5), id(7), id(9), id(11))))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(collectionName: "{collection_name}", filter: HasId([1, 3, 5, 7, 9, 11]));

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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewHasID(
				qdrant.NewIDNum(1),
				qdrant.NewIDNum(3),
				qdrant.NewIDNum(5),
				qdrant.NewIDNum(7),
				qdrant.NewIDNum(9),
				qdrant.NewIDNum(11),
			),
		},
	},
})

```

Filtered points would be:

```json
[\
  { "id": 1, "city": "London", "color": "green" },\
  { "id": 3, "city": "London", "color": "blue" },\
  { "id": 5, "city": "Moscow", "color": "green" }\
]

```

### [Anchor](https://qdrant.tech/documentation/concepts/filtering/\#has-vector) Has vector

_Available as of v1.13.0_

This condition enables filtering by the presence of a given named vector on a point.

For example, if we have two named vector in our collection.

```http
PUT /collections/{collection_name}
{
    "vectors": {
        "image": {
            "size": 4,
            "distance": "Dot"
        },
        "text": {
            "size": 8,
            "distance": "Cosine"
        }
    },
    "sparse_vectors": {
        "sparse-image": {},
        "sparse-text": {},
    },
}

```

Some points in the collection might have all vectors, some might have only a subset of them.

This is how you can search for points which have the dense `image` vector defined:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [\
            { "has_vector": "image" }\
        ]
    }
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[\
            models.HasVectorCondition(has_vector="image"),\
        ],
    ),
)

```

```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [\
      {\
        has_vector: "image",\
      },\
    ],
  },
});

```

```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}")
            .filter(Filter::must([Condition::has_vector("image")])),
    )
    .await?;

```

```java
import java.util.List;

import static io.qdrant.client.ConditionFactory.hasVector;
import static io.qdrant.client.PointIdFactory.id;

import io.qdrant.client.grpc.Points.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(hasVector("image"))
                    .build())
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(collectionName: "{collection_name}", filter: HasVector("image"));

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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewHasVector(
        "image",
			),
		},
	},
})

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/filtering.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/filtering.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575277847&cv=11&fst=1748575277847&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Ffiltering%2F&hn=www.googleadservices.com&frm=0&tiba=Filtering%20-%20Qdrant&npa=0&pscdl=noapi&auid=1251868725.1748575278&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575277750&cv=11&fst=1748575277750&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308615&ptag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Ffiltering%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Filtering%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1251868725.1748575278&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=25c1098e-5fd4-48eb-a1b2-ffbc45f07cf9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b0df10fc-6071-43d8-b712-e2fd0ba610a2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Ffiltering%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=25c1098e-5fd4-48eb-a1b2-ffbc45f07cf9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b0df10fc-6071-43d8-b712-e2fd0ba610a2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Ffiltering%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575278820&cv=11&fst=1748575278820&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Ffiltering%2F&hn=www.googleadservices.com&frm=0&tiba=Filtering%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1251868725.1748575278&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)