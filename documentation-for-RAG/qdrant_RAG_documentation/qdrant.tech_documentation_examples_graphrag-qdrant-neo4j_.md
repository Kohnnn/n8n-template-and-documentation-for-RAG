---
url: "https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/"
title: "GraphRAG with Qdrant and Neo4j - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- GraphRAG with Qdrant and Neo4j

# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#build-a-graphrag-agent-with-neo4j-and-qdrant) Build a GraphRAG Agent with Neo4j and Qdrant

![image0](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image0.png)

| Time: 30 min | Level: Intermediate | Output: [GitHub](https://github.com/qdrant/examples/blob/master/graphrag_neo4j/graphrag.py) |
| --- | --- | --- |

To make Artificial Intelligence (AI) systems more intelligent and reliable, we face a paradox: Large Language Models (LLMs) possess remarkable reasoning capabilities, yet they struggle to connect information in ways humans find intuitive. While groundbreaking, Retrieval-Augmented Generation (RAG) approaches often fall short when tasked with complex information synthesis. When asked to connect disparate pieces of information or understand holistic concepts across large documents, these systems frequently miss crucial connections that would be obvious to human experts.

To solve these problems, Microsoft introduced **GraphRAG,** which uses Knowledge Graphs (KGs) instead of vectors as a context for LLMs. GraphRAG depends mainly on LLMs for creating KGs and querying them. However, this reliance on LLMs can lead to many problems. We will address these challenges by combining vector databases with graph-based databases.

This tutorial will demonstrate how to build a GraphRAG system with vector search using Neo4j and Qdrant.

| Additional Materials |
| --- |
| This advanced tutorial is based on our original integration doc: [**Neo4j - Qdrant Integration**](https://qdrant.tech/documentation/frameworks/neo4j-graphrag/) |
| The output for this tutorial is in our GitHub Examples repo: [**Neo4j - Qdrant Agent in Python**](https://github.com/qdrant/examples/blob/master/graphrag_neo4j/graphrag.py) |

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#watch-the-video) Watch the Video

GraphRAG with Qdrant & Neo4j: Combining Vector Search and Knowledge Graphs - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[GraphRAG with Qdrant & Neo4j: Combining Vector Search and Knowledge Graphs](https://www.youtube.com/watch?v=o9pszzRuyjo)

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

[Watch on](https://www.youtube.com/watch?v=o9pszzRuyjo&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 11:11
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=o9pszzRuyjo "Watch on YouTube")

# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#rag--its-challenges) RAG & Its Challenges

[RAG](https://qdrant.tech/rag/) combines retrieval-based and generative AI to enhance LLMs with relevant, up-to-date information from a knowledge base, like a vector database. However, RAG faces several challenges:

1. **Understanding Context:** Models may misinterpret queries, particularly when the context is complex or ambiguous, leading to incorrect or irrelevant answers.
2. **Balancing Similarity vs. Relevance:** RAG systems can struggle to ensure that retrieved information is similar and contextually relevant.
3. **Answer Completeness:** Traditional RAGs might not be able to capture all relevant details for complex queries that require LLMs to find relationships in the context that are not explicitly present.

# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#introduction-to-graphrag) Introduction to GraphRAG

Unlike RAG, which typically relies on document retrieval, GraphRAG builds knowledge graphs (KGs) to capture entities and their relationships. For datasets or use cases that demand human-level intelligence from an AI system, GraphRAG offers a promising solution:

- It can follow chains of relationships to answer complex queries, making it suitable for better reasoning beyond simple document retrieval.
- The graph structure allows a deeper understanding of the context, leading to more accurate and relevant responses.

The workflow of GraphRAG is as follows:

1. The LLM analyzes the dataset to identify entities (people, places, organizations) and their relationships, creating a comprehensive knowledge graph where entities are nodes and their connections form edges.
2. A bottom-up clustering algorithm organizes the KG into hierarchical semantic groups. This creates meaningful segments of related information, enabling understanding at different levels of abstraction.
3. GraphRAG uses both the KG and semantic clusters to select a relevant context for the LLM when answering queries.

![image2](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image2.png)

[Fig](https://arxiv.org/pdf/2404.16130) 1: A Complete Picture of GraphRAG Ingestion and Retrieval

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#challenges-of-graphrag) Challenges of GraphRAG

Despite its advantages, the LLM-centric GraphRAG approach faces several challenges:

- **KG Construction with LLMs:** Since the LLM is responsible for constructing the knowledge graph, there are risks such as inconsistencies, propagation of biases or errors, and lack of control over the ontology used. However, we used a LLM to extract the ontology in our implementation.
- **Querying KG with LLMs:** Once the graph is constructed, an LLM translates the human query into Cypher (Neo4j’s declarative query language). However, crafting complex queries in Cypher may result in inaccurate outcomes.
- **Scalability & Cost Consideration:** To be practical, applications must be both scalable and cost-effective. Relying on LLMs increases costs and decreases scalability, as they are used every time data is added, queried, or generated.

To address these challenges, a more controlled and structured knowledge representation system may be required for GraphRAG to function optimally at scale.

# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#architecture-overview) Architecture Overview

The architecture has two main components: **Ingestion** and **Retrieval & Generation**. Ingestion processes raw data into structured knowledge and vector representations, while Retrieval and Generation enable efficient querying and response generation.

This process is divided into two steps: **Ingestion**, where data is prepared and stored, and **Retrieval and Generation**, where the prepared data is queried and utilized. Let’s start with Ingestion.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingestion) Ingestion

The GraphRAG ingestion pipeline combines a **Graph Database** and a **Vector Database** to improve RAG workflows.

![image1](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image1.png)

Fig 2: Overview of Ingestion Pipeline

Let’s break it down:

1. **Raw Data:** Serves as the foundation, comprising unstructured or structured content.
2. **Ontology Creation:** An **LLM** processes the raw data into an **ontology**, structuring entities, relationships, and hierarchies. Better approaches exist to extracting more structured information from raw data, like using NER to identify the names of people, organizations, and places. Unlike LLMs, this method creates.
3. **Graph Database:** The ontology is stored in a **Graph database** to capture complex relationships.
4. **Vector Embeddings:** An **Embedding model** converts the raw data into high-dimensional vectors capturing semantic similarities.
5. **Vector Database:** These embeddings are stored in a **Vector database** for similarity-based retrieval.
6. **Database Interlinking:** The **Graph database** (e.g., Neo4j) and **Vector database** (e.g., Qdrant) share unique IDs, enabling cross-referencing between ontology-based and vector-based results.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#retrieval--generation) Retrieval & Generation

The **Retrieval and Generation** process is designed to handle user queries by leveraging both semantic search and graph-based context extraction.

![image3](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image3.png)

Fig 3: Overview of Retrieval and Generation Pipeline

The architecture can be broken down into the following steps:

1. **Query Vectorization:** An embedding model converts The user query into a high-dimensional vector.
2. **Semantic Search:** The vector performs a similarity-based search in the **Vector database**, retrieving relevant documents or entries.
3. **ID Extraction:** Extracted IDs from the semantic search results are used to query the **Graph database**.
4. **Graph Context Retrieval:** The **Graph database** provides contextual information, including relationships and entities linked to the extracted IDs.
5. **Response Generation:** The context retrieved from the graph is passed to an LLM to generate a final response.
6. **Results:** The generated response is returned to the user.

This architecture combines the strengths of both databases:

1. **Semantic Search with Vector Database:** The user query is first processed semantically to identify the most relevant data points without needing explicit keyword matches.
2. **Contextual Expansion with Graph Database:** IDs or entities retrieved from the vector database query the graph database for detailed relationships, enriching the retrieved data with structured context.
3. **Enhanced Generation:** The architecture combines semantic relevance (from the vector database) and graph-based context to enable the LLM to generate more informed, accurate, and contextually rich responses.

# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#implementation) Implementation

We’ll walk through a complete pipeline that ingests data into Neo4j and Qdrant, retrieves relevant data, and generates responses using an LLM based on the retrieved graph context.

The main components of this pipeline include data ingestion (to Neo4j and Qdrant), retrieval, and generation steps.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#prerequisites) Prerequisites

These are the tutorial prerequisites, which are divided into setup, imports, and initialization of the two DBs.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#setup) Setup

Let’s start with setting up instances with Qdrant and Neo4j.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#qdrant-setup) Qdrant Setup

To create a Qdrant instance, you can use their **managed service** (Qdrant Cloud) or set up a self-hosted cluster. For simplicity, we will use Qdrant cloud:

- Go to [Qdrant Cloud](https://qdrant.tech/) and sign up or log in.
- Once logged in, click on **Create New Cluster**.
- Follow the on-screen instructions to create your cluster.
- Once your cluster is created, you’ll be given a **Cluster URL** and **API Key**, which you will use in the client to interact with Qdrant.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#neo4j-setup) Neo4j Setup

To set up a Neo4j instance, you can use **Neo4j Aura** (cloud service) or host it yourself. We will use Neo4j Aura:

- Go to Neo4j Aura and sign up/log in.
- After setting up, an instance will be created if it is the first time.
- After the database is set up, you’ll receive a **connection URI**, **username**, and **password**.

We can add the following in the .env file for security purposes.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#imports) Imports

First, we import the required libraries for working with Neo4j, Qdrant, OpenAI, and other utility functions.

```python
from neo4j import GraphDatabase
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI
from collections import defaultdict
from neo4j_graphrag.retrievers import QdrantNeo4jRetriever
import uuid
import os

```

* * *

- **Neo4j:** Used to store and query the graph database.
- **Qdrant:** A vector database used for semantic similarity search.
- **dotenv:** Loads environment variables for credentials and API keys.
- **Pydantic:** Ensures data is structured properly when interacting with the graph data.
- **OpenAI:** Interfaces with the OpenAI API to generate responses and embeddings.
- **neo4j\_graphrag:** A helper package to retrieve data from both Qdrant and Neo4j.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#setting-up-environment-variables) Setting Up Environment Variables

Before initializing the clients, we load the necessary credentials from environment variables.

```python
# Load environment variables
load_dotenv()

# Get credentials from environment variables
qdrant_key = os.getenv("QDRANT_KEY")
qdrant_url = os.getenv("QDRANT_URL")
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_username = os.getenv("NEO4J_USERNAME")
neo4j_password = os.getenv("NEO4J_PASSWORD")
openai_key = os.getenv("OPENAI_API_KEY")

```

* * *

This ensures that sensitive information (like API keys and database credentials) is securely stored in environment variables.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#initializing-neo4j-and-qdrant-clients) Initializing Neo4j and Qdrant Clients

Now, we initialize the Neo4j and Qdrant clients using the credentials.

```python
# Initialize Neo4j driver
neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))

# Initialize Qdrant client
qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_key
)

```

* * *

- **Neo4j:** We set up a connection to the Neo4j graph database.
- **Qdrant:** We initialize the connection to the Qdrant vector store.

This will connect with Neo4j and Qdrant, and we can now start with Ingestion.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingestion-1) Ingestion

We will follow the workflow of the ingestion pipeline presented in the architecture section. Let’s examine it implementation-wise.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#defining-output-parser) Defining Output Parser

The single and GraphComponents classes structure the LLM’s responses into a usable format.

```python
class single(BaseModel):
    node: str
    target_node: str
    relationship: str

class GraphComponents(BaseModel):
    graph: list[single]

```

* * *

These classes help ensure that data from the OpenAI LLM is parsed correctly into the graph components (nodes and relationships).

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#defining-openai-client-and-llm-parser-function) Defining OpenAI Client and LLM Parser Function

We now initialize the OpenAI client and define a function to send prompts to the LLM and parse its responses.

```python
client = OpenAI()

def openai_llm_parser(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        response_format={"type": "json_object"},
        messages=[\
            {\
                "role": "system",\
                "content":\
\
                """ You are a precise graph relationship extractor. Extract all\
                    relationships from the text and format them as a JSON object\
                    with this exact structure:\
                    {\
                        "graph": [\
                            {"node": "Person/Entity",\
                             "target_node": "Related Entity",\
                             "relationship": "Type of Relationship"},\
                            ...more relationships...\
                        ]\
                    }\
                    Include ALL relationships mentioned in the text, including\
                    implicit ones. Be thorough and precise. """\
\
            },\
            {\
                "role": "user",\
                "content": prompt\
            }\
        ]
    )

    return GraphComponents.model_validate_json(completion.choices[0].message.content)


```

* * *

This function sends a prompt to the LLM, asking it to extract graph components (nodes and relationships) from the provided text. The response is parsed into structured graph data.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#extracting-graph-components) Extracting Graph Components

The function extract\_graph\_components processes raw data, extracting the nodes and relationships as graph components.

```python
def extract_graph_components(raw_data):
    prompt = f"Extract nodes and relationships from the following text:\n{raw_data}"

    parsed_response = openai_llm_parser(prompt)  # Assuming this returns a list of dictionaries
    parsed_response = parsed_response.graph  # Assuming the 'graph' structure is a key in the parsed response

    nodes = {}
    relationships = []

    for entry in parsed_response:
        node = entry.node
        target_node = entry.target_node  # Get target node if available
        relationship = entry.relationship  # Get relationship if available

        # Add nodes to the dictionary with a unique ID
        if node not in nodes:
            nodes[node] = str(uuid.uuid4())

        if target_node and target_node not in nodes:
            nodes[target_node] = str(uuid.uuid4())

        # Add relationship to the relationships list with node IDs
        if target_node and relationship:
            relationships.append({
                "source": nodes[node],
                "target": nodes[target_node],
                "type": relationship
            })

    return nodes, relationships

```

* * *

This function takes raw data, uses the LLM to parse it into graph components, and then assigns unique IDs to nodes and relationships.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingesting-data-to-neo4j) Ingesting Data to Neo4j

The function ingest\_to\_neo4j ingests the extracted graph data (nodes and relationships) into Neo4j.

```python
def ingest_to_neo4j(nodes, relationships):
    """
    Ingest nodes and relationships into Neo4j.
    """

    with neo4j_driver.session() as session:
        # Create nodes in Neo4j
        for name, node_id in nodes.items():
            session.run(
                "CREATE (n:Entity {id: $id, name: $name})",
                id=node_id,
                name=name
            )

        # Create relationships in Neo4j
        for relationship in relationships:
            session.run(
                "MATCH (a:Entity {id: $source_id}), (b:Entity {id: $target_id}) "
                "CREATE (a)-[:RELATIONSHIP {type: $type}]->(b)",
                source_id=relationship["source"],
                target_id=relationship["target"],
                type=relationship["type"]
            )

    return nodes

```

* * *

Here, we create nodes and relationships in the Neo4j graph database. Nodes are entities, and relationships link these entities.

This will ingest the data into Neo4j and on a sample dataset it looks something like this:

![image4](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image4.png)

Fig 4: Visualization of the Knowledge Graph

Let’s explore how to map nodes with their IDs and integrate this information, along with vectors, into Qdrant. First, let’s create a Qdrant collection.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#creating-qdrant-collection) Creating Qdrant Collection

You can create a collection once you have set up your Qdrant instance. A collection in Qdrant holds vectors for search and retrieval.

```python
def create_collection(client, collection_name, vector_dimension):

```

try:

```python
# Try to fetch the collection status
try:
    collection_info = client.get_collection(collection_name)
    print(f"Skipping creating collection; '{collection_name}' already exists.")
except Exception as e:
    # If collection does not exist, an error will be thrown, so we create the collection
    if 'Not found: Collection' in str(e):
        print(f"Collection '{collection_name}' not found. Creating it now...")

        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_dimension, distance=models.Distance.COSINE)
        )

        print(f"Collection '{collection_name}' created successfully.")
    else:
        print(f"Error while checking collection: {e}")

```

* * *

- **Qdrant Client:** The QdrantClient is used to connect to the Qdrant instance.
- **Creating Collection:** The create\_collection function checks if a collection exists. If not, it creates one with a specified vector dimension and distance metric (cosine similarity in this case).

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#generating-embeddings) Generating Embeddings

Next, we define a function that generates embeddings for text using OpenAI’s API.

```python
def openai_embeddings(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    return response.data[0].embedding

```

* * *

This function uses OpenAI’s embedding model to transform input text into vector representations.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingesting-into-qdrant) Ingesting into Qdrant

Let’s ingest the data into the vector database.

```python
def ingest_to_qdrant(collection_name, raw_data, node_id_mapping):
    embeddings = [openai_embeddings(paragraph) for paragraph in raw_data.split("\n")]

    qdrant_client.upsert(
        collection_name=collection_name,
        points=[\
            {\
                "id": str(uuid.uuid4()),\
                "vector": embedding,\
                "payload": {"id": node_id}\
            }\
            for node_id, embedding in zip(node_id_mapping.values(), embeddings)\
        ]
    )

```

* * *

The ingest\_to\_qdrant function generates embeddings for each paragraph in the raw data and stores them in a Qdrant collection. It associates each embedding with a unique ID and its corresponding node ID from the node\_id\_mapping dictionary, ensuring proper linkage for later retrieval.

* * *

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#retrieval--generation-1) Retrieval & Generation

In this section, we will create the retrieval and generation engine for the system.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#building-a-retriever) Building a Retriever

The retriever integrates vector search and graph data, enabling semantic similarity searches with Qdrant and fetching relevant graph data from Neo4j. This enriches the RAG process and allows for more informed responses.

```python
def retriever_search(neo4j_driver, qdrant_client, collection_name, query):
    retriever = QdrantNeo4jRetriever(
        driver=neo4j_driver,
        client=qdrant_client,
        collection_name=collection_name,
        id_property_external="id",
        id_property_neo4j="id",
    )

    results = retriever.search(query_vector=openai_embeddings(query), top_k=5)

    return results

```

* * *

The [QdrantNeo4jRetriever](https://qdrant.tech/documentation/frameworks/neo4j-graphrag/) handles both vector search and graph data fetching, combining Qdrant for vector-based retrieval and Neo4j for graph-based queries.

**Vector Search:**

- **`qdrant_client`** connects to Qdrant for efficient vector similarity search.
- **`collection_name`** specifies where vectors are stored.
- **`id_property_external="id"`** maps the external entity’s ID for retrieval.

**Graph Fetching:**

- **`neo4j_driver`** connects to Neo4j for querying graph data.
- **`id_property_neo4j="id"`** ensures the entity IDs from Qdrant match the graph nodes in Neo4j.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#querying-neo4j-for-related-graph-data) Querying Neo4j for Related Graph Data

We need to fetch subgraph data from a Neo4j database based on specific entity IDs after the retriever has provided the relevant IDs.

```python
def fetch_related_graph(neo4j_client, entity_ids):
    query = """
    MATCH (e:Entity)-[r1]-(n1)-[r2]-(n2)
    WHERE e.id IN $entity_ids
    RETURN e, r1 as r, n1 as related, r2, n2
    UNION
    MATCH (e:Entity)-[r]-(related)
    WHERE e.id IN $entity_ids
    RETURN e, r, related, null as r2, null as n2
    """
    with neo4j_client.session() as session:
        result = session.run(query, entity_ids=entity_ids)
        subgraph = []
        for record in result:
            subgraph.append({
                "entity": record["e"],
                "relationship": record["r"],
                "related_node": record["related"]
            })
            if record["r2"] and record["n2"]:
                subgraph.append({
                    "entity": record["related"],
                    "relationship": record["r2"],
                    "related_node": record["n2"]
                })
    return subgraph

```

* * *

The function fetch\_related\_graph takes in a Neo4j client and a list of entity\_ids. It runs a Cypher query to find related nodes (entities) and their relationships based on the given entity IDs. The query matches entities (e:Entity) and finds related nodes through any relationship \[r\]. The function returns a list of subgraph data, where each record contains the entity, relationship, and related\_node.

This subgraph is essential for generating context to answer user queries.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#setting-up-the-graph-context) Setting up the Graph Context

The second part of the implementation involves preparing a graph context. We’ll fetch relevant subgraph data from a Neo4j database and format it for the model. Let’s break it down.

```python
def format_graph_context(subgraph):
    nodes = set()
    edges = []

    for entry in subgraph:
        entity = entry["entity"]
        related = entry["related_node"]
        relationship = entry["relationship"]

        nodes.add(entity["name"])
        nodes.add(related["name"])

        edges.append(f"{entity['name']} {relationship['type']} {related['name']}")

    return {"nodes": list(nodes), "edges": edges}

```

* * *

The function format\_graph\_context processes a subgraph returned by a Neo4j query. It extracts the graph’s entities (nodes) and relationships (edges). The nodes set ensures each entity is added only once. The edges list captures the relationships in a readable format: _Entity1 relationship Entity2_.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#integrating-with-the-llm) Integrating with the LLM

Now that we have the graph context, we need to generate a prompt for a language model like GPT-4. This is where the core of the Retrieval-Augmented Generation (RAG) happens — we combine the graph data and the user query into a comprehensive prompt for the model.

```python
def graphRAG_run(graph_context, user_query):
    nodes_str = ", ".join(graph_context["nodes"])
    edges_str = "; ".join(graph_context["edges"])
    prompt = f"""
    You are an intelligent assistant with access to the following knowledge graph:

    Nodes: {nodes_str}

    Edges: {edges_str}

    Using this graph, Answer the following question:

    User Query: "{user_query}"
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[\
                {"role": "system", "content": "Provide the answer for the following question:"},\
                {"role": "user", "content": prompt}\
            ]
        )
        return response.choices[0].message

    except Exception as e:
        return f"Error querying LLM: {str(e)}"

```

* * *

The function graphRAG\_run takes the graph context (nodes and edges) and the user query, combining them into a structured prompt for the LLM. The nodes and edges are formatted as readable strings to form part of the LLM input. The LLM is then queried with the generated prompt, asking it to refine the user query using the graph context and provide an answer. If the model successfully generates a response, it returns the answer.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#end-to-end-pipeline) End-to-End Pipeline

Finally, let’s integrate everything into an end-to-end pipeline where we ingest some sample data, run the retrieval process, and query the language model.

```python
if __name__ == "__main__":
    print("Script started")
    print("Loading environment variables...")
    load_dotenv('.env.local')
    print("Environment variables loaded")

    print("Initializing clients...")
    neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
    qdrant_client = QdrantClient(
        url=qdrant_url,
        api_key=qdrant_key
    )
    print("Clients initialized")

    print("Creating collection...")
    collection_name = "graphRAGstoreds"
    vector_dimension = 1536
    create_collection(qdrant_client, collection_name, vector_dimension)
    print("Collection created/verified")

    print("Extracting graph components...")

    raw_data = """Alice is a data scientist at TechCorp's Seattle office.
    Bob and Carol collaborate on the Alpha project.
    Carol transferred to the New York office last year.
    Dave mentors both Alice and Bob.
    TechCorp's headquarters is in Seattle.
    Carol leads the East Coast team.
    Dave started his career in Seattle.
    The Alpha project is managed from New York.
    Alice previously worked with Carol at DataCo.
    Bob joined the team after Dave's recommendation.
    Eve runs the West Coast operations from Seattle.
    Frank works with Carol on client relations.
    The New York office expanded under Carol's leadership.
    Dave's team spans multiple locations.
    Alice visits Seattle monthly for team meetings.
    Bob's expertise is crucial for the Alpha project.
    Carol implemented new processes in New York.
    Eve and Dave collaborated on previous projects.
    Frank reports to the New York office.
    TechCorp's main AI research is in Seattle.
    The Alpha project revolutionized East Coast operations.
    Dave oversees projects in both offices.
    Bob's contributions are mainly remote.
    Carol's team grew significantly after moving to New York.
    Seattle remains the technology hub for TechCorp."""

    nodes, relationships = extract_graph_components(raw_data)
    print("Nodes:", nodes)
    print("Relationships:", relationships)

    print("Ingesting to Neo4j...")
    node_id_mapping = ingest_to_neo4j(nodes, relationships)
    print("Neo4j ingestion complete")

    print("Ingesting to Qdrant...")
    ingest_to_qdrant(collection_name, raw_data, node_id_mapping)
    print("Qdrant ingestion complete")

    query = "How is Bob connected to New York?"
    print("Starting retriever search...")
    retriever_result = retriever_search(neo4j_driver, qdrant_client, collection_name, query)
    print("Retriever results:", retriever_result)

    print("Extracting entity IDs...")
    entity_ids = [item.content.split("'id': '")[1].split("'")[0] for item in retriever_result.items]
    print("Entity IDs:", entity_ids)

    print("Fetching related graph...")
    subgraph = fetch_related_graph(neo4j_driver, entity_ids)
    print("Subgraph:", subgraph)

    print("Formatting graph context...")
    graph_context = format_graph_context(subgraph)
    print("Graph context:", graph_context)

    print("Running GraphRAG...")
    answer = graphRAG_run(graph_context, query)
    print("Final Answer:", answer)

```

* * *

Here’s what’s happening:

- First, the user query is defined (“How is Bob connected to New York?”).
- The QdrantNeo4jRetriever searches for related entities in the Qdrant vector database based on the user query’s embedding. It retrieves the top 5 results (top\_k=5).
- The entity\_ids are extracted from the retriever result.
- The fetch\_related\_graph function retrieves related entities and their relationships from the Neo4j database.
- The format\_graph\_context function prepares the graph data in a format the LLM can understand.
- Finally, the graphRAG\_run function is called to generate and query the language model, producing an answer based on the retrieved graph context.

With this, we have successfully created GraphRAG, a system capable of capturing complex relationships and delivering improved performance compared to the baseline RAG approach.

# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#advantages-of-qdrant--neo4j-graphrag) Advantages of Qdrant + Neo4j GraphRAG

Combining Qdrant with Neo4j in a GraphRAG architecture offers several compelling advantages, particularly regarding recall and precision combo, contextual understanding, adaptability to complex queries, and better cost and scalability.

1. **Improved Recall and Precision:** By leveraging Qdrant, a highly efficient vector search engine, alongside Neo4j’s robust graph database, the system benefits from both semantic search and relationship-based retrieval. Qdrant identifies relevant vectors and captures the similarity between queries and stored data. At the same time, Neo4j adds a layer of connectivity through its graph structure, ensuring that relevant and contextually linked information is retrieved. This combination improves recall (retrieving a broader set of relevant results) and precision (delivering more accurate and contextually relevant results), addressing a common challenge in traditional retrieval-based AI systems.
2. **Enhanced Contextual Understanding:** Neo4j enhances contextual understanding by representing information as a graph, where entities and their relationships are naturally modeled. When integrated with Qdrant, the system can retrieve similar items based on vector embeddings and those that fit within the desired relational context, leading to more nuanced and meaningful responses.
3. **Adaptability to Complex Queries:** Combining Qdrant and Neo4j makes the system highly adaptable to complex queries. While Qdrant handles the vector search for relevant data, Neo4j’s graph capabilities enable sophisticated querying through relationships. This allows for multi-hop reasoning and handling complex, structured queries that would be challenging for traditional search engines.
4. **Better Cost & Scalability:** GraphRAG, on its own, demands significant resources, as it relies on LLMs to construct and query knowledge graphs. It also employs clustering algorithms to create semantic clusters for local searches. These can hinder scalability and increase costs. Qdrant addresses the issue of local search through vector search, while Neo4j’s knowledge graph is queried for more precise answers, enhancing both efficiency and accuracy. Furthermore, instead of using an LLM, Named Entity Recognition (NER)-based techniques can reduce the cost further, but it depends mainly on the dataset.

# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#conclusion) Conclusion

GraphRAG with Neo4j and Qdrant marks an important step forward in retrieval-augmented generation. This hybrid approach delivers significant advantages by combining vector search and graph databases. Qdrant’s semantic search capabilities enhance recall accuracy, while Neo4j’s relationship modeling provides deeper context understanding.

The implementation template we’ve explored offers a foundation for your projects. You can adapt and customize it based on your specific needs, whether for document analysis, knowledge management, or other information retrieval tasks.

As AI systems evolve, this combination of technologies shows how we can build smarter, more efficient solutions. We encourage you to experiment with this approach and discover how it can enhance your applications.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/graphrag-qdrant-neo4j.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/graphrag-qdrant-neo4j.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=141d333d-d8f0-4797-9a5a-73bd05f7bbbe&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b4b1a253-c09a-43f6-8832-01e3c68d4ec1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fgraphrag-qdrant-neo4j%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=141d333d-d8f0-4797-9a5a-73bd05f7bbbe&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b4b1a253-c09a-43f6-8832-01e3c68d4ec1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fgraphrag-qdrant-neo4j%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)