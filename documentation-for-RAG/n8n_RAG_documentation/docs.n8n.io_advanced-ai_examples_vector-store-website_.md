---
url: "https://docs.n8n.io/advanced-ai/examples/vector-store-website/"
title: "Populate a Pinecone vector database from a website | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/examples/vector-store-website/#populate-a-pinecone-vector-database-from-a-website)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/examples/vector-store-website.md "Edit this page")

# Populate a Pinecone vector database from a website [\#](https://docs.n8n.io/advanced-ai/examples/vector-store-website/\#populate-a-pinecone-vector-database-from-a-website "Permanent link")

Use n8n to scrape a website, load the data into Pinecone, then query it using a chat workflow. This workflow uses the [HTTP node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to get website data, extracts the relevant content using the [HTML node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html/), then uses the [Pinecone Vector Store node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone/) to send it to Pinecone.

[View workflow file](https://docs.n8n.io/_workflows/advanced-ai/examples/populate_a_pinecone_vector_database_from_a_website.json)

## Key features [\#](https://docs.n8n.io/advanced-ai/examples/vector-store-website/\#key-features "Permanent link")

This workflow uses:

- [HTTP node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/): fetches website data.
- [HTML node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html/): simplifies the data by extracting the main content from the page.
- [Pinecone Vector Store node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone/) and [Embeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai/): transform the data into vectors and store it in Pinecone.
- [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/) and [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/) to query the vector database.

## Using the example [\#](https://docs.n8n.io/advanced-ai/examples/vector-store-website/\#using-the-example "Permanent link")

To load the template into your n8n instance:

1. Download the workflow JSON file.
2. Open a new workflow in your n8n instance.
3. Copy in the JSON, or select **Workflow menu**![Workflow menu icon](https://docs.n8n.io/_images/common-icons/three-dots-horizontal.png) \> **Import from file...**.

The example workflows use Sticky Notes to guide you:

- Yellow: notes and information.
- Green: instructions to run the workflow.
- Orange: you need to change something to make the workflow work.
- Blue: draws attention to a key feature of the example.