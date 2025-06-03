---
url: "https://qdrant.tech/documentation/advanced-tutorials/code-search/"
title: "Search Through Your Codebase - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Advanced tutorials](https://qdrant.tech/documentation/advanced-tutorials/)
- Search Through Your Codebase

# [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#navigate-your-codebase-with-semantic-search-and-qdrant) Navigate Your Codebase with Semantic Search and Qdrant

| Time: 45 min | Level: Intermediate | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qdrant/examples/blob/master/code-search/code-search.ipynb) |  |
| --- | --- | --- | --- |

You too can enrich your applications with Qdrant semantic search. In this
tutorial, we describe how you can use Qdrant to navigate a codebase, to help
you find relevant code snippets. As an example, we will use the [Qdrant](https://github.com/qdrant/qdrant)
source code itself, which is mostly written in Rust.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#the-approach) The approach

We want to search codebases using natural semantic queries, and searching for code based on similar logic. You can set up these tasks with embeddings:

1. General usage neural encoder for Natural Language Processing (NLP), in our case
`sentence-transformers/all-MiniLM-L6-v2`.
2. Specialized embeddings for code-to-code similarity search. We use the
`jina-embeddings-v2-base-code` model.

To prepare our code for `all-MiniLM-L6-v2`, we preprocess the code to text that
more closely resembles natural language. The Jina embeddings model supports a
variety of standard programming languages, so there is no need to preprocess the
snippets. We can use the code as is.

NLP-based search is based on function signatures, but code search may return
smaller pieces, such as loops. So, if we receive a particular function signature
from the NLP model and part of its implementation from the code model, we merge
the results and highlight the overlap.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#data-preparation) Data preparation

Chunking the application sources into smaller parts is a non-trivial task. In
general, functions, class methods, structs, enums, and all the other language-specific
constructs are good candidates for chunks. They are big enough to
contain some meaningful information, but small enough to be processed by
embedding models with a limited context window. You can also use docstrings,
comments, and other metadata can be used to enrich the chunks with additional
information.

![Code chunking strategy](https://qdrant.tech/documentation/tutorials/code-search/data-chunking.png)

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#parsing-the-codebase) Parsing the codebase

While our example uses Rust, you can use our approach with any other language.
You can parse code with a [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) ( **LSP**)
compatible tool. You can use an LSP to build a graph of the codebase, and then extract chunks.
We did our work with the [rust-analyzer](https://rust-analyzer.github.io/).
We exported the parsed codebase into the [LSIF](https://microsoft.github.io/language-server-protocol/specifications/lsif/0.4.0/specification/)
format, a standard for code intelligence data. Next, we used the LSIF data to
navigate the codebase and extract the chunks. For details, see our [code search\\
demo](https://github.com/qdrant/demo-code-search).

We then exported the chunks into JSON documents with not only the code itself,
but also context with the location of the code in the project. For example, see
the description of the `await_ready_for_timeout` function from the `IsReady`
struct in the `common` module:

```json
{
   "name":"await_ready_for_timeout",
   "signature":"fn await_ready_for_timeout (& self , timeout : Duration) -> bool",
   "code_type":"Function",
   "docstring":"= \" Return `true` if ready, `false` if timed out.\"",
   "line":44,
   "line_from":43,
   "line_to":51,
   "context":{
      "module":"common",
      "file_path":"lib/collection/src/common/is_ready.rs",
      "file_name":"is_ready.rs",
      "struct_name":"IsReady",
      "snippet":"    /// Return `true` if ready, `false` if timed out.\n    pub fn await_ready_for_timeout(&self, timeout: Duration) -> bool {\n        let mut is_ready = self.value.lock();\n        if !*is_ready {\n            !self.condvar.wait_for(&mut is_ready, timeout).timed_out()\n        } else {\n            true\n        }\n    }\n"
   }
}

```

You can examine the Qdrant structures, parsed in JSON, in the [`structures.jsonl`\\
file](https://storage.googleapis.com/tutorial-attachments/code-search/structures.jsonl)
in our Google Cloud Storage bucket. Download it and use it as a source of data for our code search.

```shell
wget https://storage.googleapis.com/tutorial-attachments/code-search/structures.jsonl

```

Next, load the file and parse the lines into a list of dictionaries:

```python
import json

structures = []
with open("structures.jsonl", "r") as fp:
    for i, row in enumerate(fp):
        entry = json.loads(row)
        structures.append(entry)

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#code-to-natural-language-conversion) Code to _natural language_ conversion

Each programming language has its own syntax which is not a part of the natural
language. Thus, a general-purpose model probably does not understand the code
as is. We can, however, normalize the data by removing code specifics and
including additional context, such as module, class, function, and file name.
We took the following steps:

1. Extract the signature of the function, method, or other code construct.
2. Divide camel case and snake case names into separate words.
3. Take the docstring, comments, and other important metadata.
4. Build a sentence from the extracted data using a predefined template.
5. Remove the special characters and replace them with spaces.

As input, expect dictionaries with the same structure. Define a `textify`
function to do the conversion. We’ll use an `inflection` library to convert
with different naming conventions.

```shell
pip install inflection

```

Once all dependencies are installed, we define the `textify` function:

```python
import inflection
import re

from typing import Dict, Any

def textify(chunk: Dict[str, Any]) -> str:
    # Get rid of all the camel case / snake case
    # - inflection.underscore changes the camel case to snake case
    # - inflection.humanize converts the snake case to human readable form
    name = inflection.humanize(inflection.underscore(chunk["name"]))
    signature = inflection.humanize(inflection.underscore(chunk["signature"]))

    # Check if docstring is provided
    docstring = ""
    if chunk["docstring"]:
        docstring = f"that does {chunk['docstring']} "

    # Extract the location of that snippet of code
    context = (
        f"module {chunk['context']['module']} "
        f"file {chunk['context']['file_name']}"
    )
    if chunk["context"]["struct_name"]:
        struct_name = inflection.humanize(
            inflection.underscore(chunk["context"]["struct_name"])
        )
        context = f"defined in struct {struct_name} {context}"

    # Combine all the bits and pieces together
    text_representation = (
        f"{chunk['code_type']} {name} "
        f"{docstring}"
        f"defined as {signature} "
        f"{context}"
    )

    # Remove any special characters and concatenate the tokens
    tokens = re.split(r"\W", text_representation)
    tokens = filter(lambda x: x, tokens)
    return " ".join(tokens)

```

Now we can use `textify` to convert all chunks into text representations:

```python
text_representations = list(map(textify, structures))

```

This is how the `await_ready_for_timeout` function description appears:

```text
Function Await ready for timeout that does Return true if ready false if timed out defined as Fn await ready for timeout self timeout duration bool defined in struct Is ready module common file is_ready rs

```

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#ingestion-pipeline) Ingestion pipeline

Next, we’ll build a pipeline for vectorizing the data and set up a semantic search mechanism for both embedding models.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#building-qdrant-collection) Building Qdrant collection

We use the `qdrant-client` library with the `fastembed` extra to interact with the Qdrant server and generate vector embeddings locally. Let’s install it:

```shell
pip install "qdrant-client[fastembed]"

```

Of course, we need a running Qdrant server for vector search. If you need one,
you can [use a local Docker container](https://qdrant.tech/documentation/quick-start/)
or deploy it using the [Qdrant Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=26c4ec66-4581-4da0-a87a-0b0e7371cce1).
You can use either to follow this tutorial. Configure the connection parameters:

```python
QDRANT_URL = "https://my-cluster.cloud.qdrant.io:6333" # http://localhost:6333 for local instance
QDRANT_API_KEY = "THIS_IS_YOUR_API_KEY" # None for local instance

```

Then use the library to create a collection:

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(QDRANT_URL, api_key=QDRANT_API_KEY)
client.create_collection(
    "qdrant-sources",
    vectors_config={
        "text": models.VectorParams(
            size=client.get_embedding_size(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            ),
            distance=models.Distance.COSINE,
        ),
        "code": models.VectorParams(
            size=client.get_embedding_size(
                model_name="jinaai/jina-embeddings-v2-base-code"
            ),
            distance=models.Distance.COSINE,
        ),
    },
)

```

Our newly created collection is ready to accept the data. Let’s upload the embeddings:

```python
import uuid

# Extract the code snippets from the structures to a separate list
code_snippets = [\
    structure["context"]["snippet"] for structure in structures\
]

points = [\
    models.PointStruct(\
        id=uuid.uuid4().hex,\
        vector={\
            "text": models.Document(\
                text=text, model="sentence-transformers/all-MiniLM-L6-v2"\
            ),\
            "code": models.Document(\
                text=code, model="jinaai/jina-embeddings-v2-base-code"\
            ),\
        },\
        payload=structure,\
    )\
    for text, code, structure in zip(text_representations, code_snippets, structures)\
]

# Note: This might take a while since inference happens implicitly.
# Parallel processing can help.
# But too many processes may trigger swap memory and hurt performance.
client.upload_points("qdrant-sources", points=points, batch_size=64)

```

Internally, `qdrant-client` uses [FastEmbed](https://github.com/qdrant/fastembed) to implicitly convert our documents into their vector representations.
The uploaded points are immediately available for search. Next, query the
collection to find relevant code snippets.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#querying-the-codebase) Querying the codebase

We use one of the models to search the collection. Start with text embeddings.
Run the following query “ _How do I count points in a collection?_”. Review the
results.

```python
query = "How do I count points in a collection?"

hits = client.query_points(
    "qdrant-sources",
    query=models.Document(text=query, model="sentence-transformers/all-MiniLM-L6-v2"),
    using="text",
    limit=5,
).points

```

Now, review the results. The following table lists the module, the file name
and score. Each line includes a link to the signature, as a code block from
the file.

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| toc | point\_ops.rs | 0.59448624 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/storage/src/content_manager/toc/point_ops.rs#L120) |
| operations | types.rs | 0.5493385 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub struct CountRequestInternal`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/operations/types.rs#L831) |
| collection\_manager | segments\_updater.rs | 0.5121002 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub(crate) fn upsert_points<'a, T>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection_manager/segments_updater.rs#L339) |
| collection | point\_ops.rs | 0.5063539 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection/point_ops.rs#L213) |
| map\_index | mod.rs | 0.49973983 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn get_points_with_value_count<Q>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/map_index/mod.rs#L88) |

It seems we were able to find some relevant code structures. Let’s try the same with the code embeddings:

```python
hits = client.query_points(
    "qdrant-sources",
    query=models.Document(text=query, model="jinaai/jina-embeddings-v2-base-code"),
    using="code",
    limit=5,
).points

```

Output:

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| field\_index | geo\_index.rs | 0.73278356 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/geo_index.rs#L612) |
| numeric\_index | mod.rs | 0.7254976 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/numeric_index/mod.rs#L322) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L315) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L429) |
| fixtures | payload\_context\_fixture.rs | 0.706204 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn total_point_count`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/fixtures/payload_context_fixture.rs#L122) |

While the scores retrieved by different models are not comparable, but we can
see that the results are different. Code and text embeddings can capture
different aspects of the codebase. We can use both models to query the collection
and then combine the results to get the most relevant code snippets, from a single batch request.

```python
responses = client.query_batch_points(
    collection_name="qdrant-sources",
    requests=[\
        models.QueryRequest(\
            query=models.Document(\
                text=query, model="sentence-transformers/all-MiniLM-L6-v2"\
            ),\
            using="text",\
            with_payload=True,\
            limit=5,\
        ),\
        models.QueryRequest(\
            query=models.Document(\
                text=query, model="jinaai/jina-embeddings-v2-base-code"\
            ),\
            using="code",\
            with_payload=True,\
            limit=5,\
        ),\
    ],
)

results = [response.points for response in responses]

```

Output:

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| toc | point\_ops.rs | 0.59448624 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/storage/src/content_manager/toc/point_ops.rs#L120) |
| operations | types.rs | 0.5493385 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub struct CountRequestInternal`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/operations/types.rs#L831) |
| collection\_manager | segments\_updater.rs | 0.5121002 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub(crate) fn upsert_points<'a, T>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection_manager/segments_updater.rs#L339) |
| collection | point\_ops.rs | 0.5063539 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection/point_ops.rs#L213) |
| map\_index | mod.rs | 0.49973983 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn get_points_with_value_count<Q>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/map_index/mod.rs#L88) |
| field\_index | geo\_index.rs | 0.73278356 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/geo_index.rs#L612) |
| numeric\_index | mod.rs | 0.7254976 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/numeric_index/mod.rs#L322) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L315) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L429) |
| fixtures | payload\_context\_fixture.rs | 0.706204 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn total_point_count`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/fixtures/payload_context_fixture.rs#L122) |

This is one example of how you can use different models and combine the results.
In a real-world scenario, you might run some reranking and deduplication, as
well as additional processing of the results.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#code-search-demo) Code search demo

Our [Code search demo](https://code-search.qdrant.tech/) uses the following process:

1. The user sends a query.
2. Both models vectorize that query simultaneously. We get two different
vectors.
3. Both vectors are used in parallel to find relevant snippets. We expect
5 examples from the NLP search and 20 examples from the code search.
4. Once we retrieve results for both vectors, we merge them in one of the
following scenarios:
1. If both methods return different results, we prefer the results from
      the general usage model (NLP).
2. If there is an overlap between the search results, we merge overlapping
      snippets.

In the screenshot, we search for `flush of wal`. The result
shows relevant code, merged from both models. Note the highlighted
code in lines 621-629. It’s where both models agree.

![Results from both models, with overlap](https://qdrant.tech/documentation/tutorials/code-search/code-search-demo-example.png)

Now you see semantic code intelligence, in action.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#grouping-the-results) Grouping the results

You can improve the search results, by grouping them by payload properties.
In our case, we can group the results by the module. If we use code embeddings,
we can see multiple results from the `map_index` module. Let’s group the
results and assume a single result per module:

```python
results = client.query_points_groups(
    collection_name="qdrant-sources",
    using="code",
    query=models.Document(text=query, model="jinaai/jina-embeddings-v2-base-code"),
    group_by="context.module",
    limit=5,
    group_size=1,
)

```

Output:

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| field\_index | geo\_index.rs | 0.73278356 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/geo_index.rs#L612) |
| numeric\_index | mod.rs | 0.7254976 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/numeric_index/mod.rs#L322) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L315) |
| fixtures | payload\_context\_fixture.rs | 0.706204 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn total_point_count`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/fixtures/payload_context_fixture.rs#L122) |
| hnsw\_index | graph\_links.rs | 0.6998417 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn num_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/hnsw_index/graph_links.rs#L477) |

With the grouping feature, we get more diverse results.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#summary) Summary

This tutorial demonstrates how to use Qdrant to navigate a codebase. For an
end-to-end implementation, review the [code search\\
notebook](https://colab.research.google.com/github/qdrant/examples/blob/master/code-search/code-search.ipynb) and the
[code-search-demo](https://github.com/qdrant/demo-code-search). You can also check out [a running version of the code\\
search demo](https://code-search.qdrant.tech/) which exposes Qdrant codebase for search with a web interface.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/code-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/code-search.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573976804&cv=11&fst=1748573976804&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Fcode-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Search%20Through%20Your%20Codebase%20-%20Qdrant&npa=0&pscdl=noapi&auid=1263177589.1748573977&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573976776&cv=11&fst=1748573976776&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Fcode-search%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Search%20Through%20Your%20Codebase%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1263177589.1748573977&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=eb4ee9a9-24a9-4f0b-b67b-1135eed6bbe0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b8080911-df56-45f1-bad7-509912771e34&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Fcode-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=eb4ee9a9-24a9-4f0b-b67b-1135eed6bbe0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b8080911-df56-45f1-bad7-509912771e34&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Fcode-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573977959&cv=11&fst=1748573977959&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Fcode-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Search%20Through%20Your%20Codebase%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1263177589.1748573977&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)