---
url: "https://supabase.com/blog/semantic-image-search-amazon-bedrock"
title: "Implementing semantic image search with Amazon Titan and Supabase Vector"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Implementing semantic image search with Amazon Titan and Supabase Vector

26 Mar 2024

•

9 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Implementing semantic image search with Amazon Titan and Supabase Vector](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fgetting-started%2Famazon-bedrock%2Famazon-bedrock-supabase-vecs.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

[Amazon Titan](https://aws.amazon.com/bedrock/titan/) is a family of foundation models (FMs) for text and image generation, summarization, classification, open-ended Q&A, information extraction, and text or image search.

In this post we'll look at how we can get started with Amazon Bedrock and Supabase Vector in Python using the Amazon Titan multimodal model and the [vecs client](https://supabase.com/docs/guides/ai/vecs-python-client).

You can find the full application code as a Python Poetry project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/aws_bedrock_image_search).

## Create a new Python project with Poetry [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#create-a-new-python-project-with-poetry)

[Poetry](https://python-poetry.org/) provides packaging and dependency management for Python. If you haven't already, install poetry via pip:

`
pip install poetry
`

Then initialize a new project:

`
poetry new aws_bedrock_image_search
`

## Spin up a Postgres Database with pgvector [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#spin-up-a-postgres-database-with-pgvector)

If you haven't already, head over to [database.new](https://database.new/) and create a new project. Every Supabase project comes with a full Postgres database and the [pgvector extension](https://supabase.com/docs/guides/database/extensions/pgvector) preconfigured.

When creating your project, make sure to note down your database password as you will need it to construct the `DB_URL` in the next step.

You can find the database connection string in your Supabase Dashboard [project connect page](https://supabase.com/dashboard/project/_?showConnect=true). Select "Use connection pooling" with `Mode: Session` for a direct connection to your Postgres database. It will look something like this:

`
postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
`

## Install the dependencies [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#install-the-dependencies)

We will need to add the following dependencies to our project:

- [`vecs`](https://github.com/supabase/vecs#vecs): Supabase Vector Python Client.
- [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): AWS SDK for Python.
- [`matplotlib`](https://matplotlib.org/): for displaying our image result.

`
poetry add vecs boto3 matplotlib
`

## Import the necessary dependencies [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#import-the-necessary-dependencies)

At the top of your main python script, import the dependencies and store your `DB URL` from above in a variable:

`
import sys
import boto3
import vecs
import json
import base64
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from typing import Optional
DB_CONNECTION = "postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres"
`

Next, get the [credentials to your AWS account](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) and instantiate the `boto3` client:

`
bedrock_client = boto3.client(
    'bedrock-runtime',
    region_name='us-west-2',
    # Credentials from your AWS account
    aws_access_key_id='<replace_your_own_credentials>',
    aws_secret_access_key='<replace_your_own_credentials>',
    aws_session_token='<replace_your_own_credentials>',
)
`

## Create embeddings for your images [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#create-embeddings-for-your-images)

In the root of your project, create a new folder called `images` and add some images. You can use the images from the example project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/aws_bedrock_image_search/images) or you can find license free images on [unsplash](https://unsplash.com/).

To send images to the Amazon Bedrock API we need to need to encode them as `base64` strings. Create the following helper methods:

`
def readFileAsBase64(file_path):
    """Encode image as base64 string."""
    try:
        with open(file_path, "rb") as image_file:
            input_image = base64.b64encode(image_file.read()).decode("utf8")
        return input_image
    except:
        print("bad file name")
        sys.exit(0)
def construct_bedrock_image_body(base64_string):
    """Construct the request body.
    https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-mm.html
    """
    return json.dumps(
        {
            "inputImage": base64_string,
            "embeddingConfig": {"outputEmbeddingLength": 1024},
        }
    )
def get_embedding_from_titan_multimodal(body):
    """Invoke the Amazon Titan Model via API request."""
    response = bedrock_client.invoke_model(
        body=body,
        modelId="amazon.titan-embed-image-v1",
        accept="application/json",
        contentType="application/json",
    )
    response_body = json.loads(response.get("body").read())
    print(response_body)
    return response_body["embedding"]
def encode_image(file_path):
    """Generate embedding for the image at file_path."""
    base64_string = readFileAsBase64(file_path)
    body = construct_bedrock_image_body(base64_string)
    emb = get_embedding_from_titan_multimodal(body)
    return emb
`

Next, create a `seed` method, which will create a new Supabase Vector Collection, generate embeddings for your images, and upsert the embeddings into your database:

`
def seed():
    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)
    # get or create a collection of vectors with 1024 dimensions
    images = vx.get_or_create_collection(name="image_vectors", dimension=1024)
    # Generate image embeddings with Amazon Titan Model
    img_emb1 = encode_image('./images/one.jpg')
    img_emb2 = encode_image('./images/two.jpg')
    img_emb3 = encode_image('./images/three.jpg')
    img_emb4 = encode_image('./images/four.jpg')
    # add records to the *images* collection
    images.upsert(
        records=[\
            (\
                "one.jpg",       # the vector's identifier\
                img_emb1,        # the vector. list or np.array\
                {"type": "jpg"}  # associated  metadata\
            ), (\
                "two.jpg",\
                img_emb2,\
                {"type": "jpg"}\
            ), (\
                "three.jpg",\
                img_emb3,\
                {"type": "jpg"}\
            ), (\
                "four.jpg",\
                img_emb4,\
                {"type": "jpg"}\
            )\
        ]
    )
    print("Inserted images")
    # index the collection for fast search performance
    images.create_index()
    print("Created index")
`

Add this method as a script in your `pyproject.toml` file:

`
[tool.poetry.scripts]
seed = "image_search.main:seed"
search = "image_search.main:search"
`

After activating the virtual environtment with `poetry shell` you can now run your seed script via `poetry run seed`. You can inspect the generated embeddings in your Supabase Dashboard by visiting the [Table Editor](https://supabase.com/dashboard/project/_/editor), selecting the `vecs` schema, and the `image_vectors` table.

## Perform an image search from a text query [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#perform-an-image-search-from-a-text-query)

With Supabase Vector we can easily query our embeddings. We can use either an image as the search input or alternatively we can generate an embedding from a string input and use that as the query input:

`
def search(query_term: Optional[str] = None):
    if query_term is None:
        query_term = sys.argv[1]
    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)
    images = vx.get_or_create_collection(name="image_vectors", dimension=1024)
    # Encode text query
    text_emb = get_embedding_from_titan_multimodal(json.dumps(
        {
            "inputText": query_term,
            "embeddingConfig": {"outputEmbeddingLength": 1024},
        }
    ))
    # query the collection filtering metadata for "type" = "jpg"
    results = images.query(
        data=text_emb,                      # required
        limit=1,                            # number of records to return
        filters={"type": {"$eq": "jpg"}},   # metadata filters
    )
    result = results[0]
    print(result)
    plt.title(result)
    image = mpimg.imread('./images/' + result)
    plt.imshow(image)
    plt.show()
`

By limiting the query to one result, we can show the most relevant image to the user. Finally we use `matplotlib` to show the image result to the user.

That's it, go ahead and test it out by running `poetry run search` and you will be presented with an image of a "bike in front of a red brick wall".

## Conclusion [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#conclusion)

With just a couple of lines of Python you are able to implement image search as well as reverse image search using the Amazon Titan multimodal model and Supabase Vector.

## More Supabase [\#](https://supabase.com/blog/semantic-image-search-amazon-bedrock\#more-supabase)

- [Getting started with Amazon Bedrock and vecs](https://supabase.com/docs/guides/ai/integrations/amazon-bedrock)
- [Matryoshka embeddings: faster OpenAI vector search using Adaptive Retrieval](https://supabase.com/blog/matryoshka-embeddings)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&t=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)

[Last post\\
\\
**Announcing Data Preservation Service** \\
\\
1 April 2024](https://supabase.com/blog/pg-paper-dump)

[Next post\\
\\
**PostgREST Aggregate Functions** \\
\\
29 February 2024](https://supabase.com/blog/postgrest-aggregate-functions)

[postgres](https://supabase.com/blog/tags/postgres) [developers](https://supabase.com/blog/tags/developers) [AI](https://supabase.com/blog/tags/AI)

On this page

- [Create a new Python project with Poetry](https://supabase.com/blog/semantic-image-search-amazon-bedrock#create-a-new-python-project-with-poetry)
- [Spin up a Postgres Database with pgvector](https://supabase.com/blog/semantic-image-search-amazon-bedrock#spin-up-a-postgres-database-with-pgvector)
- [Install the dependencies](https://supabase.com/blog/semantic-image-search-amazon-bedrock#install-the-dependencies)
- [Import the necessary dependencies](https://supabase.com/blog/semantic-image-search-amazon-bedrock#import-the-necessary-dependencies)
- [Create embeddings for your images](https://supabase.com/blog/semantic-image-search-amazon-bedrock#create-embeddings-for-your-images)
- [Perform an image search from a text query](https://supabase.com/blog/semantic-image-search-amazon-bedrock#perform-an-image-search-from-a-text-query)
- [Conclusion](https://supabase.com/blog/semantic-image-search-amazon-bedrock#conclusion)
- [More Supabase](https://supabase.com/blog/semantic-image-search-amazon-bedrock#more-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&t=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)