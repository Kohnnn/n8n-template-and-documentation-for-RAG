---
url: "https://qdrant.tech/documentation/frameworks/honeyhive/"
title: "HoneyHive - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- HoneyHive

# [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#honeyhive) HoneyHive

[HoneyHive](https://www.honeyhive.ai/) is an AI evaluation and observability platform for Generative AI applications. HoneyHive’s platform gives developers enterprise-grade tools to debug complex retrieval pipelines, evaluate performance over large test suites, monitor usage in real-time, and manage prompts within a shared workspace. Teams use HoneyHive to iterate faster, detect failures at scale, and deliver exceptional AI products.

By integrating Qdrant with HoneyHive, you can:

- Trace vector database operations
- Monitor latency, embedding quality, and context relevance
- Evaluate retrieval performance in your RAG pipelines
- Optimize paramaters such as `chunk_size` or `chunk_overlap`

## [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#prerequisites) Prerequisites

- A HoneyHive account and API key
- Python 3.8+

## [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#installation) Installation

Install the required packages:

```bash
pip install qdrant-client openai honeyhive

```

## [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#basic-integration-example) Basic Integration Example

The following example demonstrates a complete RAG pipeline with HoneyHive tracing for Qdrant operations. We’ll break down each component step by step.

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#initialize-clients-and-setup) Initialize Clients and Setup

First, set up the necessary clients and configuration for HoneyHive, OpenAI, and Qdrant:

```python
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance
import openai
import os
from honeyhive.tracer import HoneyHiveTracer
from honeyhive.tracer.custom import trace
from openai import OpenAI

# Set API Keys
openai.api_key = os.getenv("OPENAI_API_KEY")
honeyhive_api_key = os.getenv("HONEYHIVE_API_KEY")

# Initialize HoneyHive Tracer
HoneyHiveTracer.init(
    api_key=honeyhive_api_key,
    project="qdrant-rag-example",
    session_name="qdrant-integration-demo"
)

# Initialize OpenAI client
openai_client = OpenAI(api_key=openai.api_key)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#connect-to-qdrant) Connect to Qdrant

You can connect to Qdrant in two ways: self-hosted (local) or cloud-hosted (Qdrant Cloud):

#### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#option-1-self-hosted-qdrant-local) Option 1: Self-Hosted Qdrant (Local)

To run Qdrant locally, you need to have Docker installed and run the following command:

```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 -p 6334:6334 -v "$(pwd)/qdrant_storage:/qdrant/storage" qdrant/qdrant

```

Then connect to the local Qdrant instance:

```python
# Connect to local Qdrant
client = QdrantClient(url="http://localhost:6333")
print("Connected to local Qdrant instance")

```

#### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#option-2-qdrant-cloud) Option 2: Qdrant Cloud

For Qdrant Cloud, you’ll need your cluster host and API key:

```python
# Qdrant Cloud configuration
QDRANT_HOST = os.getenv("QDRANT_HOST")  # e.g., "your-cluster-id.eu-central.aws.cloud.qdrant.io"
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Connect to Qdrant Cloud
client = QdrantClient(url=QDRANT_HOST, api_key=QDRANT_API_KEY)
print("Connected to Qdrant Cloud")

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#create-a-collection) Create a Collection

Create a collection to store document embeddings:

```python
collection_name = "documents"
vector_size = 1536  # For text-embedding-3-small
vector_distance = Distance.COSINE

# Create collection if it doesn't exist
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=vector_distance)
    )

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#define-embedding-function-with-tracing) Define Embedding Function with Tracing

Create a function to generate embeddings with HoneyHive tracing:

```python
@trace()
def embed_text(text: str) -> list:
    """Generate embeddings for a text using OpenAI's API."""
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#insert-documents-with-tracing) Insert Documents with Tracing

Create a function to insert documents into Qdrant with tracing:

```python
@trace()
def insert_documents(docs):
    """Insert documents into Qdrant collection."""
    points = []
    for idx, doc in enumerate(docs):
        vector = embed_text(doc)
        points.append(PointStruct(
            id=idx + 1,
            vector=vector,
            payload={"text": doc}
        ))

    client.upsert(
        collection_name=collection_name,
        points=points
    )
    return len(points)

# Sample documents
documents = [\
    "Qdrant is a vector database optimized for storing and searching high-dimensional vectors.",\
    "HoneyHive provides observability for AI applications, including RAG pipelines.",\
    "Retrieval-Augmented Generation (RAG) combines retrieval systems with generative models.",\
    "Vector databases like Qdrant are essential for efficient similarity search in RAG systems.",\
    "OpenAI's embedding models convert text into high-dimensional vectors for semantic search."\
]

# Insert documents
num_inserted = insert_documents(documents)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#retrieve-documents-with-tracing) Retrieve Documents with Tracing

Create a function to retrieve relevant documents from Qdrant with tracing:

```python
@trace()
def get_relevant_docs(query: str, top_k: int = 3) -> list:
    """Retrieve relevant documents for a query."""
    # Embed the query
    q_vector = embed_text(query)

    # Search in Qdrant
    search_response = client.query_points(
        collection_name=collection_name,
        query=q_vector,
        limit=top_k,
        with_payload=True
    )

    # Extract results
    docs = []
    for point in search_response.points:
        docs.append({
            "id": point.id,
            "text": point.payload.get("text"),
            "score": point.score
        })

    return docs

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#generate-response-with-tracing) Generate Response with Tracing

Create a function to generate a response using OpenAI with tracing:

```python
@trace()
def answer_query(query: str, relevant_docs: list) -> str:
    """Generate an answer for a query using retrieved documents."""
    if not relevant_docs:
        return "Could not retrieve relevant documents to answer the query."

    # Format context from retrieved documents
    context_parts = []
    for i, doc in enumerate(relevant_docs):
        context_parts.append(f"Document {i+1} (ID: {doc['id']}, Score: {doc['score']:.4f}):\n{doc['text']}")
    context = "\n\n".join(context_parts)

    # Create prompt
    prompt = f"""Answer the question based ONLY on the following context:

Context:
{context}

Question: {query}

Answer:"""

    # Generate answer
    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[\
            {"role": "system", "content": "You are a helpful assistant that answers questions based strictly on the provided context. If the answer is not in the context, say so clearly."},\
            {"role": "user", "content": prompt}\
        ],
        temperature=0.2
    )

    return completion.choices[0].message.content.strip()

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#complete-rag-pipeline) Complete RAG Pipeline

Create a function to run the complete RAG pipeline with tracing:

```python
@trace()
def rag_pipeline(query: str) -> dict:
    """End-to-end RAG pipeline."""
    # Get relevant documents
    relevant_docs = get_relevant_docs(query)

    # Generate answer
    answer = answer_query(query, relevant_docs)

    return {
        "query": query,
        "answer": answer,
        "retrieved_documents": relevant_docs
    }

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#batch-processing) Batch Processing

For larger document sets, you can use batch processing to improve performance:

```python
@trace()
def batch_insert_documents(documents_to_insert, batch_size=10, start_id_offset=0):
    """Insert documents in batches."""
    total_inserted = 0

    for i in range(0, len(documents_to_insert), batch_size):
        batch_docs = documents_to_insert[i:i+batch_size]
        points = []

        for local_idx, doc in enumerate(batch_docs):
            relative_idx = i + local_idx
            vector = embed_text(doc)
            point_id = relative_idx + start_id_offset + 1
            points.append(PointStruct(
                id=point_id,
                vector=vector,
                payload={"text": doc}
            ))

        if points:
            client.upsert(
                collection_name=collection_name,
                points=points
            )
            total_inserted += len(points)

    return total_inserted

```

### [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#test-the-rag-pipeline) Test the RAG Pipeline

Here’s how to test the complete RAG pipeline:

```python
# Test query
test_query = "What is Qdrant used for?"
result = rag_pipeline(test_query)

print(f"Query: {result['query']}")
print(f"Answer: {result['answer']}")
print("\nRetrieved Documents:")
for i, doc in enumerate(result['retrieved_documents']):
    print(f"Document {i+1} (ID: {doc['id']}, Score: {doc['score']:.4f}): {doc['text']}")

```

## [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#viewing-traces-in-honeyhive) Viewing Traces in HoneyHive

After running your RAG pipeline with Qdrant, you can view the traces in the HoneyHive UI:

1. Navigate to your project in the HoneyHive dashboard
2. Click on the “Traces” tab to see all the traces from your RAG pipeline
3. Click on a specific trace to see detailed information about each step in the pipeline
4. Analyze the performance of your vector operations, embeddings, and retrieval processes

With HoneyHive, you can easily monitor and optimize your Qdrant-powered RAG pipeline, ensuring that it delivers the best possible results for your users.

## [Anchor](https://qdrant.tech/documentation/frameworks/honeyhive/\#further-reading) Further Reading

- [HoneyHive Documentation](https://docs.honeyhive.ai/introduction/what-is-hhai)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/honeyhive.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/honeyhive.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574327068&cv=11&fst=1748574327068&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fhoneyhive%2F&hn=www.googleadservices.com&frm=0&tiba=HoneyHive%20-%20Qdrant&npa=0&pscdl=noapi&auid=858353863.1748574327&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574327049&cv=11&fst=1748574327049&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fhoneyhive%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=HoneyHive%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=858353863.1748574327&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4677af81-1ab6-4cf2-8f86-b9fc310520e6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=fcc58405-e98a-4a8e-82a3-160a1a298e0c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fhoneyhive%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4677af81-1ab6-4cf2-8f86-b9fc310520e6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=fcc58405-e98a-4a8e-82a3-160a1a298e0c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fhoneyhive%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574328224&cv=11&fst=1748574328224&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fhoneyhive%2F&hn=www.googleadservices.com&frm=0&tiba=HoneyHive%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=858353863.1748574327&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)