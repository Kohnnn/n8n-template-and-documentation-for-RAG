import os
import asyncio
import json
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import LLMExtractionStrategy
import re
import re

import re

def extract_url(md_string):
    # Find whatever is inside (...) in a Markdown link [text](...)
    match = re.search(r'\[[^\]]*\]\(([^)]*)\)', md_string)
    if match:
        raw_url = match.group(1).strip()
        # Remove any trailing "description"
        raw_url = re.sub(r'\s*".*"$', '', raw_url)
        # Remove invalid fragments like </...>
        cleaned_url = re.sub(r'</[^>]*>', '', raw_url)
        return cleaned_url
    return md_string


async def crawl_and_extract(url, prompt, browser_cfg):
    """
    Generic function to crawl a URL and extract information based on a prompt.
    """
    url = extract_url(url)

    print("Crawling URL:", url)

    # Define the LLM extraction strategy
    llm_strategy = LLMExtractionStrategy(
        # provider="ollama/deepseek-r1:32b",
        api_token=os.getenv("OPENAI_API_KEY"),
        provider="openai/gpt-4o",
        extraction_type="block",
        instruction=prompt,  
        chunk_token_threshold=800,  
        overlap_rate=0.1, 
        apply_chunking=True,  
        input_format="markdown",
        extra_args={"temperature": 0.0, "max_tokens": 1000},
        verbose=True,
    )

    # Configure the crawler
    crawl_config = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASS,
        process_iframes=False,
        remove_overlay_elements=True,
        excluded_tags=["form", "header", "footer"],
    )


    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # Crawl the URL and extract information based on the prompt
        result = await crawler.arun(url=url, config=crawl_config)

        if result.success:
            # Extract the result from the LLM output
            try:
                print("EXTRACTED CONTENT: ", result.extracted_content)
                # Parse the JSON response
                response_json = json.loads(result.extracted_content)
                # Extract the content from the JSON structure
                extracted_content = str(response_json[0]["content"][0].strip())

                llm_strategy.show_usage()

                return extracted_content
            except (json.JSONDecodeError, KeyError, IndexError) as e:
                print(f"Error parsing extracted content: {e}")
                return None
        else:
            print("Error:", result.error_message)
            return None


async def main():
    website_url = "https://crawl4ai.com/"

    # Define the commands as an array of prompts
    commands = [
        "Find the link to the GitHub repository in the content. When the URL is found format it as a actual link, not a markdown link. Should be in the form of 'https://example.com. (\"https://github.com/example/</example/blah/bleh/blih...\" should become: https://github.com/example/blah/bleh/blih...). Return only the URL.",
        "Find the CONTRIBUTORS.md.  When the URL is found format it as a actual link, not a markdown link. Should be in the form of 'https://example.com (\"https://github.com/example/</example/blah/bleh/blih...\" should become: https://github.com/example/blah/bleh/blih...) Return only the URL.",
        "Extract the names of all contributors from the content. Return only the names in a comma-separated list.",
    ]

    # Initialize the URL to start with
    current_url = website_url

    # Create a browser config
    browser_cfg = BrowserConfig(headless=True)

    # Process each command sequentially
    for i, prompt in enumerate(commands):
        print(f"Processing command {i + 1}: {prompt}")

        # Crawl and extract based on the current URL and prompt
        result = await crawl_and_extract(current_url, prompt, browser_cfg)

        if result:
            # Update the current URL for the next command
            current_url = result
        else:
            print("Failed to process the command.")
            break


if __name__ == "__main__":
    asyncio.run(main())
