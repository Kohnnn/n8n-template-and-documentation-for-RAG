# n8n RAG AI Agent Workflow Collection

## Overview

This repository contains a comprehensive collection of n8n workflows implementing Retrieval-Augmented Generation (RAG) for creating AI-powered workflow automation. The repository serves as both a reference implementation and ready-to-deploy solution for n8n workflow generation.

## Repository Structure

```
.
├── documentation-for-RAG/        # Documentation datasets for RAG systems
│   └── n8n_documentation_index/  # Indexed n8n documentation
├── n8n.io-templates/            # Reference workflow templates
├── n8n-blog-maker/              # Blog generation workflow system
├── Real Case Example/           # Production-ready workflow implementations
└── *.json                       # Individual workflow files
```

## Technical Components

### Workflow Documentation Corpus

The repository includes a complete n8n documentation corpus scraped using `crawl4ai`, providing:

- Node documentation with parameter specifications
- Workflow execution details
- Integration configuration requirements
- Error handling patterns and best practices

### RAG Implementation

The RAG system is implemented with the following components:

- **Vector Database Integration**: Compatible with Qdrant, Pinecone, and Supabase Vector
- **Embedding Models**: Supports OpenAI, Cohere, and Jina embeddings
- **Retrieval Mechanisms**: Implements semantic search with customizable relevance thresholds
- **Context Assembly**: Dynamic prompt construction with retrieved documentation fragments
- **Generation**: Compatible with various LLM providers (OpenAI, Anthropic, Google, etc.)

### API Integration Points

- Webhook endpoints for external triggers
- HTTP Request nodes for external service communication
- Database connectors (PostgreSQL, MongoDB, MySQL)
- File storage integrations (S3, Google Drive, Local)

### Workflow Categories

| Category | Count | Description |
|----------|-------|-------------|
| Content Generation | 35+ | Automated content creation workflows |
| Customer Interaction | 25+ | CRM and customer service automation |
| Data Processing | 20+ | ETL and data transformation pipelines |
| Media Production | 15+ | Video and image generation workflows |
| Miscellaneous | 5+ | Utility and specialized workflows |

## Implementation Requirements

### System Prerequisites

- n8n instance (v0.214.0+)
- Node.js (v16+)
- Docker (for containerized deployments)
- Vector database instance (Qdrant recommended)

### API Credentials

The following credentials are required for full functionality:

- OpenAI API key or equivalent LLM provider
- Vector database API credentials
- Service-specific API keys (YouTube, Twitter, etc. as needed)

### Memory Requirements

- Minimum 4GB RAM for basic workflows
- 8GB+ RAM recommended for complex RAG implementations
- 20GB+ storage for documentation corpus and embedding data

## Usage Instructions

### Installation

```bash
# Clone the repository
git clone https://github.com/username/n8n-rag-agent.git

# Navigate to repository
cd n8n-rag-agent

# Import workflows to n8n (using n8n CLI)
n8n import:workflow --input=*.json
```

### Configuration

1. Configure environment variables in your n8n instance:
   ```
   N8N_ENCRYPTION_KEY=your-encryption-key
   N8N_VECTOR_DB_URL=your-vector-db-url
   N8N_LLM_API_KEY=your-llm-api-key
   ```

2. Set up vector database collections:
   ```
   N8N_DOC_COLLECTION=n8n_documentation
   N8N_WORKFLOW_COLLECTION=workflow_examples
   ```

3. Install additional dependencies if required by specific workflows

### Execution

Workflows can be executed via:
- Webhook triggers
- Scheduled executions
- Manual activation
- API calls to n8n endpoints

## Performance Considerations

- RAG queries typically complete in 2-5 seconds depending on complexity
- Workflow generation may take 10-30 seconds for complex implementations
- Consider batch processing for high-volume operations

## Credits

- @imgroup: Real-world business implementations
- n8n community contributors

## License

[MIT License](LICENSE)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines. 