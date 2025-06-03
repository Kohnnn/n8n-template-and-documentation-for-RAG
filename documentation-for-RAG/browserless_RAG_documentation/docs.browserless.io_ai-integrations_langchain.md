---
url: "https://docs.browserless.io/ai-integrations/langchain"
title: "Langchain Integration | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/ai-integrations/langchain#__docusaurus_skipToContent_fallback)

On this page

[LangChain](https://www.langchain.com/) is a framework for developing applications powered by language models. By integrating Browserless with LangChain, you can provide your AI applications with powerful web scraping and content processing capabilities without managing browser infrastructure.

## Prerequisites [​](https://docs.browserless.io/ai-integrations/langchain\#prerequisites "Direct link to Prerequisites")

- Python 3.8 or higher
- An active Browserless API Token (available in your [account dashboard](https://account.browserless.io/))
- Basic understanding of LangChain concepts

## Step-by-Step Setup [​](https://docs.browserless.io/ai-integrations/langchain\#step-by-step-setup "Direct link to Step-by-Step Setup")

**1\. Get your API Key**

Go to your [Browserless Account Dashboard](https://account.browserless.io/) and copy your API token.

Then set the `BROWSERLESS_API_TOKEN` environment variable in your `.env` file:

- .env file
- Command line

```codeBlockLines_p187
BROWSERLESS_API_TOKEN=your-token-here

```

```codeBlockLines_p187
export BROWSERLESS_API_TOKEN=your-token-here

```

**2\. Create a virtual environment**

Set up a Python virtual environment to manage your dependencies:

- venv
- conda

```codeBlockLines_p187
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

```codeBlockLines_p187
conda create -n langchain-env python=3.8
conda activate langchain-env

```

**3\. Install required packages**

Install LangChain and other required packages:

- pip
- Poetry

```codeBlockLines_p187
pip install langchain-community python-dotenv

```

```codeBlockLines_p187
poetry add langchain-community python-dotenv

```

**4\. Create your first script**

Create a file named `scraper.py` with the following complete code:

```codeBlockLines_p187
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import BrowserlessLoader

def main():
    # Load environment variables
    load_dotenv()

    # Initialize the loader with your API token
    loader = BrowserlessLoader(
        api_token=os.getenv("BROWSERLESS_API_TOKEN"),
        urls=["https://example.com"],
        text_content=True  # Get text content instead of raw HTML
    )

    # Load and process the documents
    documents = loader.load()

    # Print the results
    for doc in documents:
        print(f"Source: {doc.metadata.get('source')}")
        print(f"Content: {doc.page_content[:200]}...")

if __name__ == "__main__":
    main()

```

**5\. Run your application**

Run your application with the following command:

```codeBlockLines_p187
python scraper.py

```

You should see output showing the scraped content from the example website.

## How It Works [​](https://docs.browserless.io/ai-integrations/langchain\#how-it-works "Direct link to How It Works")

**1\. Connection Setup**: BrowserlessLoader connects to Browserless using your API token
**2\. Content Loading**: The loader fetches and processes web content
**3\. Document Creation**: Content is converted into LangChain Documents
**4\. Processing**: Documents can be further processed with LangChain's tools

## Advanced Configuration [​](https://docs.browserless.io/ai-integrations/langchain\#advanced-configuration "Direct link to Advanced Configuration")

### Multiple URLs [​](https://docs.browserless.io/ai-integrations/langchain\#multiple-urls "Direct link to Multiple URLs")

Process multiple websites in a single operation:

```codeBlockLines_p187
loader = BrowserlessLoader(
    api_token=api_token,
    urls=[\
        "https://example1.com",\
        "https://example2.com",\
        "https://example3.com"\
    ]
)

```

### Raw HTML Mode [​](https://docs.browserless.io/ai-integrations/langchain\#raw-html-mode "Direct link to Raw HTML Mode")

Get raw HTML content instead of text:

```codeBlockLines_p187
loader = BrowserlessLoader(
    api_token=api_token,
    urls=["https://example.com"],
    text_content=False
)

```

## Performance Optimization [​](https://docs.browserless.io/ai-integrations/langchain\#performance-optimization "Direct link to Performance Optimization")

1. **Batch Processing**
   - Process multiple URLs in batches
   - Implement proper error handling
   - Use async/await for better performance
2. **Resource Management**
   - Monitor memory usage
   - Implement proper cleanup
   - Handle timeouts appropriately

## Security Best Practices [​](https://docs.browserless.io/ai-integrations/langchain\#security-best-practices "Direct link to Security Best Practices")

1. **API Token Management**
   - Never commit tokens to version control
   - Use environment variables
   - Rotate tokens regularly
2. **Input Validation**
   - Validate URLs before processing
   - Implement rate limiting
   - Handle sensitive data appropriately

## Common Use Cases [​](https://docs.browserless.io/ai-integrations/langchain\#common-use-cases "Direct link to Common Use Cases")

### News Aggregation [​](https://docs.browserless.io/ai-integrations/langchain\#news-aggregation "Direct link to News Aggregation")

```codeBlockLines_p187
def aggregate_news(api_token, news_sites):
    loader = BrowserlessLoader(
        api_token=api_token,
        urls=news_sites,
        text_content=True
    )
    documents = loader.load()

    # Process and analyze the news content
    for doc in documents:
        print(f"Source: {doc.metadata.get('source')}")
        print(f"Content: {doc.page_content[:200]}...")

```

### Content Analysis [​](https://docs.browserless.io/ai-integrations/langchain\#content-analysis "Direct link to Content Analysis")

```codeBlockLines_p187
from langchain.text_splitter import RecursiveCharacterTextSplitter

def analyze_content(api_token, url):
    # Load content
    loader = BrowserlessLoader(
        api_token=api_token,
        urls=[url],
        text_content=True
    )
    documents = loader.load()

    # Split content into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)

    # Process chunks
    for chunk in chunks:
        print(f"Chunk: {chunk.page_content[:100]}...")

```

For more advanced usage scenarios, please refer to:

- [LangChain Documentation](https://www.langchain.com/docs)
- [Browserless BaaS Documentation](https://docs.browserless.io/baas/start)
- [Integrating with other LLM providers](https://docs.browserless.io/ai-integrations/start)

- [Prerequisites](https://docs.browserless.io/ai-integrations/langchain#prerequisites)
- [Step-by-Step Setup](https://docs.browserless.io/ai-integrations/langchain#step-by-step-setup)
- [How It Works](https://docs.browserless.io/ai-integrations/langchain#how-it-works)
- [Advanced Configuration](https://docs.browserless.io/ai-integrations/langchain#advanced-configuration)
  - [Multiple URLs](https://docs.browserless.io/ai-integrations/langchain#multiple-urls)
  - [Raw HTML Mode](https://docs.browserless.io/ai-integrations/langchain#raw-html-mode)
- [Performance Optimization](https://docs.browserless.io/ai-integrations/langchain#performance-optimization)
- [Security Best Practices](https://docs.browserless.io/ai-integrations/langchain#security-best-practices)
- [Common Use Cases](https://docs.browserless.io/ai-integrations/langchain#common-use-cases)
  - [News Aggregation](https://docs.browserless.io/ai-integrations/langchain#news-aggregation)
  - [Content Analysis](https://docs.browserless.io/ai-integrations/langchain#content-analysis)