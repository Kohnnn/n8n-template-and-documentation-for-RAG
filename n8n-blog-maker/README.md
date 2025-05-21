# Automated Blog Generation and Publishing Workflow with Vector Database

This n8n workflow automatically generates blog posts using AI, stores them in a vector database for semantic search, and publishes them to your GitHub Pages site at [Kohnnn.github.io](https://github.com/Kohnnn/Kohnnn.github.io).

## Features

- Scheduled weekly blog post generation
- Style matching based on your reference documents
- Vector database storage using Qdrant for semantic search
- AI-powered content creation with GPT-4
- Automatic publishing to GitHub Pages
- Related post recommendations based on semantic similarity
- Manual triggering option via webhook

## Setup Instructions

### Prerequisites

1. An n8n instance (self-hosted or cloud)
2. OpenAI API key
3. GitHub personal access token with repo permissions
4. Qdrant vector database instance (can be run locally via Docker)

### Qdrant Setup

1. Install Qdrant using Docker:
   ```
   docker run -p 6333:6333 -p 6334:6334 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant
   ```

2. Ensure Qdrant is accessible at `http://localhost:6333`

### Credential Setup in n8n

1. **OpenAI API Key**
   - In n8n, go to Settings > Credentials
   - Add new credentials of type "HTTP Header Auth" named "OpenAI API Key"
   - Set the Name field to "Authorization"
   - Set the Value field to "Bearer YOUR_OPENAI_API_KEY"

2. **GitHub Token**
   - In n8n, add new credentials of type "GitHub API"
   - Enter your GitHub username and personal access token

3. **Qdrant API**
   - In n8n, add new credentials of type "Qdrant API"
   - Set the API URL to "http://localhost:6333"
   - Leave API Key blank if not using authentication

### Importing the Workflow

1. In n8n, go to Workflows > Import from File
2. Upload the `Auto_Blog_Generator_Workflow.json` file
3. Save the workflow

## Usage

### Automatic Execution

The workflow is scheduled to run weekly. It will:
1. Generate a blog post on the configured topic
2. Create embeddings of the content and store them in Qdrant
3. Search for semantically similar previous posts
4. Add related post references to the new post
5. Publish the post to GitHub Pages

### Manual Execution

To manually trigger the workflow:
1. Go to the workflow's webhook URL: `YOUR_N8N_BASE_URL/webhook/auto-blog-webhook`
2. Send a POST request with the following JSON body:
   ```json
   {
     "topic": "Your blog topic here",
     "styleReference": "path/to/your/reference/file.md"
   }
   ```

## Style References

For best results, upload style reference files that showcase your writing style. These files will be used by the AI to generate content that matches your voice and tone.

## Vector Database Features

This workflow utilizes Qdrant as a vector database to:

1. Store embeddings of all blog posts
2. Find semantically similar content across your blog
3. Create "Related Posts" sections automatically
4. Build a knowledge base of your writing over time

## Troubleshooting

- Ensure all API credentials are valid and have the necessary permissions
- Check that Qdrant is running and accessible
- Verify file paths for style references are correct
- Monitor the n8n execution logs for any errors 