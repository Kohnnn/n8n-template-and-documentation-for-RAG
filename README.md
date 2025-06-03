# n8n RAG AI Agent Workflow Collection

## Overview

This repository contains a comprehensive collection of n8n workflows implementing Retrieval-Augmented Generation (RAG) for creating AI-powered workflow automation. The repository serves as both a reference implementation and ready-to-deploy solution for n8n workflow generation.

## Repository Structure

```
.
├── documentation-for-RAG/        # Documentation datasets for RAG systems
│   └── n8n_documentation_index/  # Indexed n8n documentation
├── n8n.io-templates (Credit to @enescingoz)/ # Reference workflow templates
├── n8n-blog-maker/              # Blog generation workflow system
├── Real Case Example (Credit to @imgroup)/ # Production-ready workflow implementations
├── Categorized/                 # Categorized workflow examples
├── *.json                       # Individual workflow files
└── *.pdf, *.py                  # Utility files and guides
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

### API Credentials

The following credentials are required for full functionality:

- OpenAI API key or equivalent LLM provider
- Vector database API credentials
- Service-specific API keys (YouTube, Twitter, etc. as needed)


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

## Here some sources to learn more about n8n

[Full basic - No prerequisites](https://youtu.be/c0Dqnd4HU8w)<br>
[Overall guide - No prerequisites](https://youtu.be/ZHH3sr234zY)<br>
[Webhook guide if you want to self host](https://youtu.be/kq5bmrjPPAY)<br>
[Neat tricks](https://youtu.be/NBhARSnjvwg)<br>
[MOST IMPORTANT](https://cdn11.bigcommerce.com/s-v7bssafn/images/stencil/760x600/products/1022/5529/20240624-DSC_3994-Edit__76162.1719226837.jpg?c=2)<br>

## Credits

- @imgroup: Real-world business implementations
- n8n.io community contributors

## License

[MIT License](LICENSE)


