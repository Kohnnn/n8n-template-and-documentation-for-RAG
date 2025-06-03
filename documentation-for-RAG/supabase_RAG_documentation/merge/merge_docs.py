import os
import re
import glob
from collections import defaultdict

# Paths
input_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.abspath(__file__).replace('merge_docs.py', '')

# Boilerplate patterns to remove
boilerplate_patterns = [
    r'\[Skip to content\]\(.*?\)\n*',
    r'\[Edit this page\]\(.*?\)\n*',
    r'Was this page helpful\?.*?Back to top',
    r'Version: .*?\n',
    r'On this page.*?\n',
]

# Compile regex patterns
compiled_patterns = [re.compile(pattern, re.DOTALL) for pattern in boilerplate_patterns]

def extract_frontmatter(content):
    """Extract title and URL from frontmatter"""
    frontmatter_match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        return None, None
    
    frontmatter = frontmatter_match.group(1)
    
    title_match = re.search(r'title:\s*"(.*?)"', frontmatter)
    url_match = re.search(r'url:\s*"(.*?)"', frontmatter)
    
    title = title_match.group(1) if title_match else "Untitled"
    url = url_match.group(1) if url_match else "#"
    
    return title, url

def remove_frontmatter(content):
    """Remove YAML frontmatter from content"""
    return re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

def remove_boilerplate(content):
    """Remove boilerplate text"""
    for pattern in compiled_patterns:
        content = pattern.sub('', content)
    return content

def categorize_files(md_files):
    """Group files by their directory structure"""
    categories = defaultdict(list)
    
    for md_file in md_files:
        # Skip the merged file if it exists
        if "merged_n8n_docs.md" in md_file:
            continue
            
        basename = os.path.basename(md_file)
        parts = basename.split('_')
        
        if len(parts) > 2:  # Has a category
            if 'integrations' in md_file and 'app-nodes' in md_file:
                category = "Integration App Nodes"
            elif 'integrations' in md_file:
                category = "Integrations"
            else:
                category = parts[1].capitalize()
        else:
            category = "General"
            
        categories[category].append(md_file)
    
    return categories

def process_files():
    """Process all markdown files and merge them"""
    # Get all markdown files
    md_files = glob.glob(os.path.join(input_dir, "*.md"))
    
    # Group files by category
    categorized_files = categorize_files(md_files)
    
    # Create output content
    output_content = "# n8n Documentation\n\n"
    
    # Process each category
    for category, files in sorted(categorized_files.items()):
        output_content += f"\n## {category}\n\n"
        
        # Process each file in the category
        for md_file in sorted(files):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract information from frontmatter
            title, url = extract_frontmatter(content)
            
            # Skip processing if no frontmatter found
            if not title:
                continue
            
            # Clean content
            content = remove_frontmatter(content)
            content = remove_boilerplate(content)
            
            # Add section header with original title and URL
            output_content += f"### {title}\n"
            output_content += f"Original URL: {url}\n\n"
            
            # Add the main content
            output_content += content.strip() + "\n\n"
            output_content += "---\n\n"  # Add a separator between sections
    
    # Write output to file
    output_file = os.path.join(output_dir, "merged_n8n_docs.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"Merged documentation written to {output_file}")

if __name__ == "__main__":
    process_files() 