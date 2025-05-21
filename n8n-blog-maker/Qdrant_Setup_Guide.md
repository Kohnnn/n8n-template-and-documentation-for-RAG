# Qdrant Setup Guide for Blog Generator

This guide will help you set up and configure Qdrant, the vector database used by the Auto Blog Generator workflow.

## What is Qdrant?

Qdrant is a vector similarity search engine that enables you to search for content based on semantic meaning rather than just keywords. In the context of our blog generator workflow, it's used to:

1. Store embeddings (vector representations) of blog posts
2. Find similar posts for cross-referencing
3. Build a connected knowledge graph of your content
4. Enable powerful semantic search across your blog

## Quick Setup with Docker

The easiest way to set up Qdrant is using Docker:

```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage \
    qdrant/qdrant
```

For Windows PowerShell, use:

```powershell
docker run -p 6333:6333 -p 6334:6334 `
    -v ${PWD}/qdrant_storage:/qdrant/storage `
    qdrant/qdrant
```

This will:
- Start Qdrant on ports 6333 (API) and 6334 (Web UI)
- Store data persistently in a local directory

Once running, you can access:
- REST API at http://localhost:6333
- Web UI Dashboard at http://localhost:6334

## Manual Installation

If you prefer not to use Docker, you can:

1. Download the appropriate binary from [Qdrant Releases](https://github.com/qdrant/qdrant/releases)
2. Extract and run the binary
3. Configure using the `config.yaml` file

## Setting Up in n8n

### 1. Add Qdrant API Credentials

In n8n:
1. Go to **Settings** > **Credentials**
2. Click **Create New Credentials**
3. Select **Qdrant API**
4. Enter:
   - **Credential Name**: `QdrantApi account`
   - **API URL**: `http://localhost:6333`
   - **API Key**: Leave blank if not using authentication
5. Click **Save**

### 2. Test the Connection

The workflow includes a "Initialize Qdrant Collection" node that automatically creates the necessary collection. To test it manually:

1. Create a simple HTTP Request node in n8n
2. Configure it to:
   - **Method**: GET
   - **URL**: `http://localhost:6333/collections`
   - **Authentication**: Qdrant API (your credential)
3. Run the node and verify you get a response

## Collection Structure

The workflow creates a collection named `blog_posts` with:

- Vector dimension: 1536 (for OpenAI embeddings)
- Distance metric: Cosine (for similarity search)

Each point in the collection contains:
- **ID**: Unique identifier (based on date)
- **Vector**: Embedding of the blog content
- **Payload**:
  - `topic`: The blog post topic
  - `title`: The blog post title
  - `date`: Publication date
  - `content`: The full blog post content
  - `fileName`: Path to the file in GitHub

## Troubleshooting

### Common Issues

1. **Connection Refused**
   - Ensure Qdrant is running
   - Verify ports are correctly mapped in Docker
   - Check firewall settings

2. **Collection Creation Fails**
   - Collection might already exist (not an error)
   - Check logs for specific error messages

3. **Embedding Storage Fails**
   - Verify OpenAI API key is valid
   - Ensure vector dimensions match (1536 for ada-002)

### Viewing Data

To view your stored data:
1. Access the Web UI at http://localhost:6334
2. Navigate to the "Collections" tab
3. Select the "blog_posts" collection
4. Use the "Search" tab to explore your vectors

## Advanced Configuration

### Persistence

For production use, configure persistent storage:

```yaml
storage:
  # Storage persistence path
  storage_path: ./storage
```

### Authentication

To enable API key authentication:

```yaml
service:
  api_key: your-secret-api-key
```

Then update your n8n credential with this key.

### Memory Settings

Adjust memory usage for larger collections:

```yaml
storage:
  optimizers:
    # Default maximum segment size in KB
    default_segment_number: 2
    # Number of segments to store in RAM
    memmap_threshold_kb: 1024000
```

## Resources

- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [Vector Database Concepts](https://qdrant.tech/articles/what-is-a-vector-database/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)

## Next Steps

After setting up Qdrant, make sure to:
1. Test the workflow with a manual trigger
2. Check that vectors are being stored properly
3. Verify that related posts are being linked correctly

As your blog grows, the semantic connections between posts will become more valuable, creating a rich knowledge network. 