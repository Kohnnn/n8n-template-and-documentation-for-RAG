---
url: "https://qdrant.tech/documentation/concepts/vectors/"
title: "Vectors - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Vectors

# [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#vectors) Vectors

Vectors (or embeddings) are the core concept of the Qdrant Vector Search engine.
Vectors define the similarity between objects in the vector space.

If a pair of vectors are similar in vector space, it means that the objects they represent are similar in some way.

For example, if you have a collection of images, you can represent each image as a vector.
If two images are similar, their vectors will be close to each other in the vector space.

In order to obtain a vector representation of an object, you need to apply a vectorization algorithm to the object.
Usually, this algorithm is a neural network that converts the object into a fixed-size vector.

The neural network is usually [trained](https://qdrant.tech/articles/metric-learning-tips/) on a pairs or [triplets](https://qdrant.tech/articles/triplet-loss/) of similar and dissimilar objects, so it learns to recognize a specific type of similarity.

By using this property of vectors, you can explore your data in a number of ways; e.g. by searching for similar objects, clustering objects, and more.

## [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#vector-types) Vector Types

Modern neural networks can output vectors in different shapes and sizes, and Qdrant supports most of them.
Let’s take a look at the most common types of vectors supported by Qdrant.

### [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#dense-vectors) Dense Vectors

This is the most common type of vector. It is a simple list of numbers, it has a fixed length and each element of the list is a floating-point number.

It looks like this:

```json

// A piece of a real-world dense vector
[\
    -0.013052909,\
    0.020387933,\
    -0.007869,\
    -0.11111383,\
    -0.030188112,\
    -0.0053388323,\
    0.0010654867,\
    0.072027855,\
    -0.04167721,\
    0.014839341,\
    -0.032948174,\
    -0.062975034,\
    -0.024837125,\
    ....\
]

```

The majority of neural networks create dense vectors, so you can use them with Qdrant without any additional processing.
Although compatible with most embedding models out there, Qdrant has been tested with the following [verified embedding providers](https://qdrant.tech/documentation/embeddings/).

### [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#sparse-vectors) Sparse Vectors

Sparse vectors are a special type of vectors.
Mathematically, they are the same as dense vectors, but they contain many zeros so they are stored in a special format.

Sparse vectors in Qdrant don’t have a fixed length, as it is dynamically allocated during vector insertion.
The amount of non-zero values in sparse vectors is currently limited to u32 datatype range (4294967295).

In order to define a sparse vector, you need to provide a list of non-zero elements and their indexes.

```json
// A sparse vector with 4 non-zero elements
{
    "indexes": [1, 3, 5, 7],
    "values": [0.1, 0.2, 0.3, 0.4]
}

```

Sparse vectors in Qdrant are kept in special storage and indexed in a separate index, so their configuration is different from dense vectors.

To create a collection with sparse vectors:

httpbashpythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}
{
    "sparse_vectors": {
        "text": { }
    }
}

```

```bash
curl -X PUT http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "sparse_vectors": {
        "text": { }
    }
  }'

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config={},
    sparse_vectors_config={
        "text": models.SparseVectorParams(),
    },
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  sparse_vectors: {
    text: { },
  },
});

```

```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateCollectionBuilder, SparseVectorParamsBuilder, SparseVectorsConfigBuilder,
};

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut sparse_vector_config = SparseVectorsConfigBuilder::default();

sparse_vector_config.add_named_vector_params("text", SparseVectorParamsBuilder::default());

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .sparse_vectors_config(sparse_vector_config),
    )
    .await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.SparseVectorConfig;
import io.qdrant.client.grpc.Collections.SparseVectorParams;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setSparseVectorsConfig(
                SparseVectorConfig.newBuilder()
                    .putMap("text", SparseVectorParams.getDefaultInstance()))
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
	collectionName: "{collection_name}",
	sparseVectorsConfig: ("text", new SparseVectorParams())
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
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"text": {},
		}),
})

```

Insert a point with a sparse vector into the created collection:

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}/points
{
    "points": [\
        {\
            "id": 1,\
            "vector": {\
                "text": {\
                    "indices": [1, 3, 5, 7],\
                    "values": [0.1, 0.2, 0.3, 0.4]\
                }\
            }\
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
            payload={},  # Add any additional payload if necessary\
            vector={\
                "text": models.SparseVector(\
                    indices=[1, 3, 5, 7],\
                    values=[0.1, 0.2, 0.3, 0.4]\
                )\
            },\
        )\
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
      vector: {\
        text: {\
          indices: [1, 3, 5, 7],\
          values: [0.1, 0.2, 0.3, 0.4]\
        },\
      },\
    }\
  ]
});

```

```rust
use qdrant_client::qdrant::{NamedVectors, PointStruct, UpsertPointsBuilder, Vector};

use qdrant_client::{Payload, Qdrant};

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![PointStruct::new(\
    1,\
    NamedVectors::default().add_vector(\
        "text",\
        Vector::new_sparse(vec![1, 3, 5, 7], vec![0.1, 0.2, 0.3, 0.4]),\
    ),\
    Payload::new(),\
)];

client
    .upsert_points(UpsertPointsBuilder::new("{collection_name}", points))
    .await?;

```

```java
import java.util.List;
import java.util.Map;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

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
      .setVectors(
        namedVectors(Map.of(
          "text", vector(List.of(1.0f, 2.0f), List.of(6, 7))))
      )
      .build()))
  .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
  collectionName: "{collection_name}",
  points: new List < PointStruct > {
    new() {
      Id = 1,
        Vectors = new Dictionary <string, Vector> {
          ["text"] = ([0.1f, 0.2f, 0.3f, 0.4f], [1, 3, 5, 7])
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
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(
				map[string]*qdrant.Vector{
					"text": qdrant.NewVectorSparse(
						[]uint32{1, 3, 5, 7},
						[]float32{0.1, 0.2, 0.3, 0.4}),
				}),
		},
	},
})

```

Now you can run a search with sparse vectors:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/query
{
    "query": {
        "indices": [1, 3, 5, 7],
        "values": [0.1, 0.2, 0.3, 0.4]
    },
    "using": "text"
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

result = client.query_points(
    collection_name="{collection_name}",
    query=models.SparseVector(indices=[1, 3, 5, 7], values=[0.1, 0.2, 0.3, 0.4]),
    using="text",
).points

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    query: {
        indices: [1, 3, 5, 7],
        values: [0.1, 0.2, 0.3, 0.4]
    },
    using: "text",
    limit: 3,
});

```

```rust
use qdrant_client::qdrant::QueryPointsBuilder;
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(vec![(1, 0.2), (3, 0.1), (5, 0.9), (7, 0.7)])
            .limit(10)
            .using("text"),
    )
    .await?;

```

```java
import java.util.List;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.QueryPoints;

import static io.qdrant.client.QueryFactory.nearest;

QdrantClient client =
  new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(
        QueryPoints.newBuilder()
                .setCollectionName("{collection_name}")
                .setUsing("text")
                .setQuery(nearest(List.of(0.1f, 0.2f, 0.3f, 0.4f), List.of(1, 3, 5, 7)))
                .setLimit(3)
                .build())
        .get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
  collectionName: "{collection_name}",
  query: new (float, uint)[] {(0.1f, 1), (0.2f, 3), (0.3f, 5), (0.4f, 7)},
  usingVector: "text",
  limit: 3
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

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Query: qdrant.NewQuerySparse(
		[]uint32{1, 3, 5, 7},
		[]float32{0.1, 0.2, 0.3, 0.4}),
	Using: qdrant.PtrOf("text"),
})

```

### [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#multivectors) Multivectors

**Available as of v1.10.0**

Qdrant supports the storing of a variable amount of same-shaped dense vectors in a single point.
This means that instead of a single dense vector, you can upload a matrix of dense vectors.

The length of the matrix is fixed, but the number of vectors in the matrix can be different for each point.

Multivectors look like this:

```json
// A multivector of size 4
"vector": [\
    [-0.013,  0.020, -0.007, -0.111],\
    [-0.030, -0.055,  0.001,  0.072],\
    [-0.041,  0.014, -0.032, -0.062],\
    ....\
]

```

There are two scenarios where multivectors are useful:

- **Multiple representation of the same object** \- For example, you can store multiple embeddings for pictures of the same object, taken from different angles. This approach assumes that the payload is same for all vectors.
- **Late interaction embeddings** \- Some text embedding models can output multiple vectors for a single text.
For example, a family of models such as ColBERT output a relatively small vector for each token in the text.

In order to use multivectors, we need to specify a function that will be used to compare between matrices of vectors

Currently, Qdrant supports `max_sim` function, which is defined as a sum of maximum similarities between each pair of vectors in the matrices.

score=∑i=1Nmaxj=1MSim(vectorAi,vectorBj)

Where N is the number of vectors in the first matrix, M is the number of vectors in the second matrix, and Sim is a similarity function, for example, cosine similarity.

To use multivectors, create a collection with the following configuration:

httppythontypescriptrustjavacsharpgo

```http
PUT collections/{collection_name}
{
  "vectors": {
    "size": 128,
    "distance": "Cosine",
    "multivector_config": {
      "comparator": "max_sim"
    }
  }
}

```

```python

from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(
        size=128,
        distance=models.Distance.COSINE,
        multivector_config=models.MultiVectorConfig(
            comparator=models.MultiVectorComparator.MAX_SIM
        ),
    ),
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 128,
    distance: "Cosine",
    multivector_config: {
      comparator: "max_sim"
    }
  },
});

```

```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, VectorParamsBuilder,
    MultiVectorComparator, MultiVectorConfigBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(
                VectorParamsBuilder::new(100, Distance::Cosine)
                    .multivector_config(
                        MultiVectorConfigBuilder::new(MultiVectorComparator::MaxSim)
                    ),
            ),
    )
    .await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.MultiVectorComparator;
import io.qdrant.client.grpc.Collections.MultiVectorConfig;
import io.qdrant.client.grpc.Collections.VectorParams;

QdrantClient client =
  new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.createCollectionAsync("{collection_name}",
  VectorParams.newBuilder().setSize(128)
  .setDistance(Distance.Cosine)
  .setMultivectorConfig(MultiVectorConfig.newBuilder()
    .setComparator(MultiVectorComparator.MaxSim)
    .build())
  .build()).get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParams {
    Size = 128,
      Distance = Distance.Cosine,
      MultivectorConfig = new() {
        Comparator = MultiVectorComparator.MaxSim
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

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     128,
		Distance: qdrant.Distance_Cosine,
		MultivectorConfig: &qdrant.MultiVectorConfig{
			Comparator: qdrant.MultiVectorComparator_MaxSim,
		},
	}),
})

```

To insert a point with multivector:

httppythontypescriptrustjavacsharpgo

```http
PUT collections/{collection_name}/points
{
  "points": [\
    {\
      "id": 1,\
      "vector": [\
        [-0.013,  0.020, -0.007, -0.111, ...],\
        [-0.030, -0.055,  0.001,  0.072, ...],\
        [-0.041,  0.014, -0.032, -0.062, ...]\
      ]\
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
            vector=[\
                [-0.013,  0.020, -0.007, -0.111],\
                [-0.030, -0.055,  0.001,  0.072],\
                [-0.041,  0.014, -0.032, -0.062]\
            ],\
        )\
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
      vector: [\
        [-0.013,  0.020, -0.007, -0.111, ...],\
        [-0.030, -0.055,  0.001,  0.072, ...],\
        [-0.041,  0.014, -0.032, -0.062, ...]\
      ],\
    }\
  ]
});

```

```rust
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder, Vector};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![\
    PointStruct::new(\
        1,\
        Vector::new_multi(vec![\
            vec![-0.013, 0.020, -0.007, -0.111],\
            vec![-0.030, -0.055, 0.001, 0.072],\
            vec![-0.041, 0.014, -0.032, -0.062],\
        ]),\
        Payload::new()\
    )\
];

client
    .upsert_points(
        UpsertPointsBuilder::new("{collection_name}", points)
    ).await?;

```

```java
import java.util.List;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorsFactory.vectors;
import static io.qdrant.client.VectorFactory.multiVector;

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
            .setVectors(vectors(multiVector(new float[][] {
                {-0.013f,  0.020f, -0.007f, -0.111f},
                {-0.030f, -0.055f,  0.001f,  0.072f},
                {-0.041f,  0.014f, -0.032f, -0.062f}
            })))
            .build()
    ))
.get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
  collectionName: "{collection_name}",
  points: new List <PointStruct> {
    new() {
      Id = 1,
        Vectors = new float[][] {
          [-0.013f, 0.020f, -0.007f, -0.111f],
          [-0.030f, -0.05f, 0.001f, 0.072f],
          [-0.041f, 0.014f, -0.032f, -0.062f ],
        },
    },
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
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMulti(
				[][]float32{
					{-0.013, 0.020, -0.007, -0.111},
					{-0.030, -0.055, 0.001, 0.072},
					{-0.041, 0.014, -0.032, -0.062}}),
		},
	},
})

```

To search with multivector (available in `query` API):

httppythontypescriptrustjavacsharpgo

```http
POST collections/{collection_name}/points/query
{
  "query": [\
    [-0.013,  0.020, -0.007, -0.111, ...],\
    [-0.030, -0.055,  0.001,  0.072, ...],\
    [-0.041,  0.014, -0.032, -0.062, ...]\
  ]
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=[\
        [-0.013,  0.020, -0.007, -0.111],\
        [-0.030, -0.055,  0.001,  0.072],\
        [-0.041,  0.014, -0.032, -0.062]\
    ],
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
  "query": [\
    [-0.013, 0.020, -0.007, -0.111],\
    [-0.030, -0.055, 0.001, 0.072],\
    [-0.041, 0.014, -0.032, -0.062]\
  ]
});

```

```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{ QueryPointsBuilder, VectorInput };

let client = Qdrant::from_url("http://localhost:6334").build()?;

let res = client.query(
    QueryPointsBuilder::new("{collection_name}")
        .query(VectorInput::new_multi(
            vec![\
                vec![-0.013,  0.020, -0.007, -0.111],\
                vec![-0.030, -0.055,  0.001,  0.072],\
                vec![-0.041,  0.014, -0.032, -0.062],\
            ]
        ))
).await?;

```

```java
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.QueryPoints;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(QueryPoints.newBuilder()
    .setCollectionName("{collection_name}")
    .setQuery(nearest(new float[][] {
        {-0.013f, 0.020f, -0.007f, -0.111f},
        {-0.030f, -0.055f, 0.001f, 0.072f},
        {-0.041f, 0.014f, -0.032f, -0.062f}
    }))
    .build()).get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
  collectionName: "{collection_name}",
  query: new float[][] {
    [-0.013f, 0.020f, -0.007f, -0.111f],
    [-0.030f, -0.055f, 0.001 , 0.072f],
    [-0.041f, 0.014f, -0.032f, -0.062f],
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

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Query: qdrant.NewQueryMulti(
		[][]float32{
			{-0.013, 0.020, -0.007, -0.111},
			{-0.030, -0.055, 0.001, 0.072},
			{-0.041, 0.014, -0.032, -0.062},
		}),
})

```

## [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#named-vectors) Named Vectors

In Qdrant, you can store multiple vectors of different sizes and [types](https://qdrant.tech/documentation/concepts/vectors/#vector-types) in the same data [point](https://qdrant.tech/documentation/concepts/points/). This is useful when you need to define your data with multiple embeddings to represent different features or modalities (e.g., image, text or video).

To store different vectors for each point, you need to create separate named vector spaces in the [collection](https://qdrant.tech/documentation/concepts/collections/). You can define these vector spaces during collection creation and manage them independently.

To create a collection with named vectors, you need to specify a configuration for each vector:

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}
{
  "vectors": {
    "image": {
      "size": 4,
      "distance": "Dot"
    },
    "text": {
      "size": 5,
      "distance": "Cosine"
    }
  },
  "sparse_vectors": {
    "text-sparse": {}
  }
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config={
        "image": models.VectorParams(size=4, distance=models.Distance.DOT),
        "text": models.VectorParams(size=5, distance=models.Distance.COSINE),
    },
    sparse_vectors_config={"text-sparse": models.SparseVectorParams()},
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
    vectors: {
        image: { size: 4, distance: "Dot" },
        text: { size: 5, distance: "Cosine" },
    },
    sparse_vectors: {
        text_sparse: {}
    }
});

```

```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, SparseVectorParamsBuilder, SparseVectorsConfigBuilder,
    VectorParamsBuilder, VectorsConfigBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut vector_config = VectorsConfigBuilder::default();
vector_config.add_named_vector_params("text", VectorParamsBuilder::new(5, Distance::Dot));
vector_config.add_named_vector_params("image", VectorParamsBuilder::new(4, Distance::Cosine));

let mut sparse_vectors_config = SparseVectorsConfigBuilder::default();
sparse_vectors_config
    .add_named_vector_params("text-sparse", SparseVectorParamsBuilder::default());

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(vector_config)
            .sparse_vectors_config(sparse_vectors_config),
    )
    .await?;

```

```java
import java.util.Map;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.SparseVectorConfig;
import io.qdrant.client.grpc.Collections.SparseVectorParams;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorParamsMap;
import io.qdrant.client.grpc.Collections.VectorsConfig;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(VectorsConfig.newBuilder().setParamsMap(
                VectorParamsMap.newBuilder().putAllMap(Map.of("image",
                    VectorParams.newBuilder()
                        .setSize(4)
                        .setDistance(Distance.Dot)
                        .build(),
                    "text",
                    VectorParams.newBuilder()
                        .setSize(5)
                        .setDistance(Distance.Cosine)
                        .build()))))
            .setSparseVectorsConfig(SparseVectorConfig.newBuilder().putMap(
                "text-sparse", SparseVectorParams.getDefaultInstance()))
            .build())
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParamsMap
  {
      Map = {
      ["image"] = new VectorParams {
        Size = 4, Distance = Distance.Dot
      },
      ["text"] = new VectorParams {
        Size = 5, Distance = Distance.Cosine
      },
    }
  },
  sparseVectorsConfig: new SparseVectorConfig
  {
      Map = {
        ["text-sparse"] = new()
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

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfigMap(
		map[string]*qdrant.VectorParams{
			"image": {
				Size:     4,
				Distance: qdrant.Distance_Dot,
			},
			"text": {
				Size:     5,
				Distance: qdrant.Distance_Cosine,
			},
		}),
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"text-sparse": {},
		},
	),
})

```

To insert a point with named vectors:

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}/points?wait=true
{
    "points": [\
        {\
            "id": 1,\
            "vector": {\
                "image": [0.9, 0.1, 0.1, 0.2],\
                "text": [0.4, 0.7, 0.1, 0.8, 0.1],\
                "text-sparse": {\
                  "indices": [1, 3, 5, 7],\
                  "values": [0.1, 0.2, 0.3, 0.4]\
                }\
            }\
        }\
    ]
}

```

```python
client.upsert(
    collection_name="{collection_name}",
    points=[\
        models.PointStruct(\
            id=1,\
            vector={\
                "image": [0.9, 0.1, 0.1, 0.2],\
                "text": [0.4, 0.7, 0.1, 0.8, 0.1],\
                "text-sparse": {\
                    "indices": [1, 3, 5, 7],\
                    "values": [0.1, 0.2, 0.3, 0.4],\
                },\
            },\
        ),\
    ],
)

```

```typescript
client.upsert("{collection_name}", {
    points: [\
        {\
            id: 1,\
            vector: {\
                image: [0.9, 0.1, 0.1, 0.2],\
                text: [0.4, 0.7, 0.1, 0.8, 0.1],\
                text_sparse: {\
                    indices: [1, 3, 5, 7],\
                    values: [0.1, 0.2, 0.3, 0.4]\
                }\
            },\
        },\
    ],
});

```

```rust

use qdrant_client::qdrant::{
    NamedVectors, PointStruct, UpsertPointsBuilder, Vector,
};
use qdrant_client::Payload;

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![PointStruct::new(\
                1,\
                NamedVectors::default()\
                    .add_vector("text", Vector::new_dense(vec![0.4, 0.7, 0.1, 0.8, 0.1]))\
                    .add_vector("image", Vector::new_dense(vec![0.9, 0.1, 0.1, 0.2]))\
                    .add_vector(\
                        "text-sparse",\
                        Vector::new_sparse(vec![1, 3, 5, 7], vec![0.1, 0.2, 0.3, 0.4]),\
                    ),\
                Payload::default(),\
            )],
        )
        .wait(true),
    )
    .await?;

```

```java
import java.util.List;
import java.util.Map;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.grpc.Points.PointStruct;

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "image",
                            vector(List.of(0.9f, 0.1f, 0.1f, 0.2f)),
                            "text",
                            vector(List.of(0.4f, 0.7f, 0.1f, 0.8f, 0.1f)),
                            "text-sparse",
                            vector(List.of(0.1f, 0.2f, 0.3f, 0.4f), List.of(1, 3, 5, 7)))))
                .build()))
    .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new()
        {
            Id = 1,
            Vectors = new Dictionary<string, Vector>
            {
                ["image"] = new() {
                    Data = {0.9f, 0.1f, 0.1f, 0.2f}
                },
                ["text"] = new() {
                    Data = {0.4f, 0.7f, 0.1f, 0.8f, 0.1f}
                },
                ["text-sparse"] = ([0.1f, 0.2f, 0.3f, 0.4f], [1, 3, 5, 7]),
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"image": qdrant.NewVector(0.9, 0.1, 0.1, 0.2),
				"text":  qdrant.NewVector(0.4, 0.7, 0.1, 0.8, 0.1),
				"text-sparse": qdrant.NewVectorSparse(
					[]uint32{1, 3, 5, 7},
					[]float32{0.1, 0.2, 0.3, 0.4}),
			}),
		},
	},
})

```

To search with named vectors (available in `query` API):

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/points/query
{
    "query": [0.2, 0.1, 0.9, 0.7],
    "using": "image",
    "limit": 3
}

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=[0.2, 0.1, 0.9, 0.7],
    using="image",
    limit=3,
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
  query: [0.2, 0.1, 0.9, 0.7],
  using: "image",
  limit: 3,
});

```

```rust
use qdrant_client::qdrant::QueryPointsBuilder;
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(vec![0.2, 0.1, 0.9, 0.7])
            .limit(3)
            .using("image"),
    )
    .await?;

```

```java
import java.util.List;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.QueryPoints;

import static io.qdrant.client.QueryFactory.nearest;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(QueryPoints.newBuilder()
        .setCollectionName("{collection_name}")
        .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
        .setUsing("image")
        .setLimit(3)
        .build()).get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
	collectionName: "{collection_name}",
	query: new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
	usingVector: "image",
	limit: 3
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

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
	Using:          qdrant.PtrOf("image"),
})

```

## [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#datatypes) Datatypes

Newest versions of embeddings models generate vectors with very large dimentionalities.
With OpenAI’s `text-embedding-3-large` embedding model, the dimensionality can go up to 3072.

The amount of memory required to store such vectors grows linearly with the dimensionality,
so it is important to choose the right datatype for the vectors.

The choice between datatypes is a trade-off between memory consumption and precision of vectors.

Qdrant supports a number of datatypes for both dense and sparse vectors:

**Float32**

This is the default datatype for vectors in Qdrant. It is a 32-bit (4 bytes) floating-point number.
The standard OpenAI embedding of 1536 dimensionality will require 6KB of memory to store in Float32.

You don’t need to specify the datatype for vectors in Qdrant, as it is set to Float32 by default.

**Float16**

This is a 16-bit (2 bytes) floating-point number. It is also known as half-precision float.
Intuitively, it looks like this:

```text
float32 -> float16 delta (float32 - float16).abs

0.79701585 -> 0.796875   delta 0.00014084578
0.7850789  -> 0.78515625 delta 0.00007736683
0.7775044  -> 0.77734375 delta 0.00016063452
0.85776305 -> 0.85791016 delta 0.00014710426
0.6616839  -> 0.6616211  delta 0.000062823296

```

The main advantage of Float16 is that it requires half the memory of Float32, while having virtually no impact on the quality of vector search.

To use Float16, you need to specify the datatype for vectors in the collection configuration:

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}
{
  "vectors": {
    "size": 128,
    "distance": "Cosine",
    "datatype": "float16" // <-- For dense vectors
  },
  "sparse_vectors": {
    "text": {
      "index": {
        "datatype": "float16" // <-- And for sparse vectors
      }
    }
  }
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(
        size=128,
        distance=models.Distance.COSINE,
        datatype=models.Datatype.FLOAT16
    ),
    sparse_vectors_config={
        "text": models.SparseVectorParams(
            index=models.SparseIndexParams(datatype=models.Datatype.FLOAT16)
        ),
    },
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 128,
    distance: "Cosine",
    datatype: "float16"
  },
  sparse_vectors: {
    text: {
      index: {
        datatype: "float16"
      }
    }
  }
});

```

```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Datatype, Distance, SparseIndexConfigBuilder, SparseVectorParamsBuilder, SparseVectorsConfigBuilder, VectorParamsBuilder
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut sparse_vector_config = SparseVectorsConfigBuilder::default();
sparse_vector_config.add_named_vector_params(
    "text",
    SparseVectorParamsBuilder::default()
        .index(SparseIndexConfigBuilder::default().datatype(Datatype::Float32)),
);

let create_collection = CreateCollectionBuilder::new("{collection_name}")
    .sparse_vectors_config(sparse_vector_config)
    .vectors_config(
        VectorParamsBuilder::new(128, Distance::Cosine).datatype(Datatype::Float16),
    );

client.create_collection(create_collection).await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Datatype;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.SparseIndexConfig;
import io.qdrant.client.grpc.Collections.SparseVectorConfig;
import io.qdrant.client.grpc.Collections.SparseVectorParams;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorsConfig;

QdrantClient client = new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
  .createCollectionAsync(
    CreateCollection.newBuilder()
    .setCollectionName("{collection_name}")
    .setVectorsConfig(VectorsConfig.newBuilder()
      .setParams(VectorParams.newBuilder()
        .setSize(128)
        .setDistance(Distance.Cosine)
        .setDatatype(Datatype.Float16)
        .build())
      .build())
    .setSparseVectorsConfig(
      SparseVectorConfig.newBuilder()
      .putMap("text", SparseVectorParams.newBuilder()
        .setIndex(SparseIndexConfig.newBuilder()
          .setDatatype(Datatype.Float16)
          .build())
        .build()))
    .build())
  .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParams {
    Size = 128,
      Distance = Distance.Cosine,
      Datatype = Datatype.Float16
  },
  sparseVectorsConfig: (
    "text",
    new SparseVectorParams {
      Index = new SparseIndexConfig {
        Datatype = Datatype.Float16
      }
    }
  )
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
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     128,
		Distance: qdrant.Distance_Cosine,
		Datatype: qdrant.Datatype_Float16.Enum(),
	}),
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"text": {
				Index: &qdrant.SparseIndexConfig{
					Datatype: qdrant.Datatype_Float16.Enum(),
				},
			},
		}),
})

```

**Uint8**

Another step towards memory optimization is to use the Uint8 datatype for vectors.
Unlike Float16, Uint8 is not a floating-point number, but an integer number in the range from 0 to 255.

Not all embeddings models generate vectors in the range from 0 to 255, so you need to be careful when using Uint8 datatype.

In order to convert a number from float range to Uint8 range, you need to apply a process called quantization.

Some embedding providers may provide embeddings in a pre-quantized format.
One of the most notable examples is the [Cohere int8 & binary embeddings](https://cohere.com/blog/int8-binary-embeddings).

For other embeddings, you will need to apply quantization yourself.

httppythontypescriptrustjavacsharpgo

```http
PUT /collections/{collection_name}
{
  "vectors": {
    "size": 128,
    "distance": "Cosine",
    "datatype": "uint8" // <-- For dense vectors
  },
  "sparse_vectors": {
    "text": {
      "index": {
        "datatype": "uint8" // <-- For sparse vectors
      }
    }
  }
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(
        size=128, distance=models.Distance.COSINE, datatype=models.Datatype.UINT8
    ),
    sparse_vectors_config={
        "text": models.SparseVectorParams(
            index=models.SparseIndexParams(datatype=models.Datatype.UINT8)
        ),
    },
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 128,
    distance: "Cosine",
    datatype: "uint8"
  },
  sparse_vectors: {
    text: {
      index: {
        datatype: "uint8"
      }
    }
  }
});

```

```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Datatype, Distance, SparseIndexConfigBuilder,
    SparseVectorParamsBuilder, SparseVectorsConfigBuilder, VectorParamsBuilder,
};

use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut sparse_vector_config = SparseVectorsConfigBuilder::default();

sparse_vector_config.add_named_vector_params(
    "text",
    SparseVectorParamsBuilder::default()
        .index(SparseIndexConfigBuilder::default().datatype(Datatype::Uint8)),
);
let create_collection = CreateCollectionBuilder::new("{collection_name}")
    .sparse_vectors_config(sparse_vector_config)
    .vectors_config(
        VectorParamsBuilder::new(128, Distance::Cosine)
            .datatype(Datatype::Uint8)
    );

client.create_collection(create_collection).await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Datatype;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.SparseIndexConfig;
import io.qdrant.client.grpc.Collections.SparseVectorConfig;
import io.qdrant.client.grpc.Collections.SparseVectorParams;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorsConfig;

QdrantClient client = new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
  .createCollectionAsync(
    CreateCollection.newBuilder()
    .setCollectionName("{collection_name}")
    .setVectorsConfig(VectorsConfig.newBuilder()
      .setParams(VectorParams.newBuilder()
        .setSize(128)
        .setDistance(Distance.Cosine)
        .setDatatype(Datatype.Uint8)
        .build())
      .build())
    .setSparseVectorsConfig(
      SparseVectorConfig.newBuilder()
      .putMap("text", SparseVectorParams.newBuilder()
        .setIndex(SparseIndexConfig.newBuilder()
          .setDatatype(Datatype.Uint8)
          .build())
        .build()))
    .build())
  .get();

```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParams {
    Size = 128,
      Distance = Distance.Cosine,
      Datatype = Datatype.Uint8
  },
  sparseVectorsConfig: (
    "text",
    new SparseVectorParams {
      Index = new SparseIndexConfig {
        Datatype = Datatype.Uint8
      }
    }
  )
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
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     128,
		Distance: qdrant.Distance_Cosine,
		Datatype: qdrant.Datatype_Uint8.Enum(),
	}),
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"text": {
				Index: &qdrant.SparseIndexConfig{
					Datatype: qdrant.Datatype_Uint8.Enum(),
				},
			},
		}),
})

```

## [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#quantization) Quantization

Apart from changing the datatype of the original vectors, Qdrant can create quantized representations of vectors alongside the original ones.
This quantized representation can be used to quickly select candidates for rescoring with the original vectors or even used directly for search.

Quantization is applied in the background, during the optimization process.

More information about the quantization process can be found in the [Quantization](https://qdrant.tech/documentation/guides/quantization/) section.

## [Anchor](https://qdrant.tech/documentation/concepts/vectors/\#vector-storage) Vector Storage

Depending on the requirements of the application, Qdrant can use one of the data storage options.
Keep in mind that you will have to tradeoff between search speed and the size of RAM used.

More information about the storage options can be found in the [Storage](https://qdrant.tech/documentation/concepts/storage/#vector-storage) section.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/vectors.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/vectors.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e2af3bad-fd16-4152-9665-722925f6ca8b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1808a49d-6732-42a6-881d-6c43515707e1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fvectors%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574546513&cv=11&fst=1748574546513&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fvectors%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Vectors%20-%20Qdrant&npa=0&pscdl=noapi&auid=1064486708.1748574546&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574546476&cv=11&fst=1748574546476&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fvectors%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Vectors%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1064486708.1748574546&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574546745&cv=11&fst=1748574546745&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fvectors%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Vectors%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1064486708.1748574546&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e2af3bad-fd16-4152-9665-722925f6ca8b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1808a49d-6732-42a6-881d-6c43515707e1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fconcepts%2Fvectors%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)