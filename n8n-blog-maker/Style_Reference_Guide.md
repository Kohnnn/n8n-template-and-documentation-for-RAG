# Style Reference Guide for Blog Generator

This guide helps you prepare effective style reference documents for your automated blog generation workflow with vector database integration.

## What Are Style References?

Style references are examples of your writing that showcase your personal voice, tone, and formatting preferences. The AI analyzes these references to generate new content that matches your unique style while maintaining semantic coherence through vector database storage.

## How to Create Effective Style References

### 1. Choose Representative Samples

Select blog posts or articles that:
- Accurately represent your writing style
- Cover similar topics to your automated blog
- Include your typical formatting patterns
- Are recent enough to reflect your current style

### 2. Format Requirements

Each style reference document should be:
- Saved as a Markdown (.md) file
- Between 500-3000 words (enough to capture style patterns)
- Well-structured with proper headers, paragraphs, and formatting
- Free of sensitive or private information you don't want referenced

### 3. Include Typical Elements

For best results, include examples of:
- Headers (different levels)
- Bulleted and numbered lists
- Text emphasis (bold, italic)
- Links and citations
- Code blocks (if relevant)
- Quotes or blockquotes
- Image references (if applicable)

### 4. Showcase Your Voice

Make sure your references demonstrate:
- Your typical sentence structure and length
- Vocabulary and terminology you commonly use
- Tone (formal, casual, technical, conversational)
- Transition phrases you prefer
- Opening and closing patterns

## Example Style Reference Structure

```markdown
# Main Topic Title

## Introduction Section

This is where you would introduce your topic in your characteristic style. Write a few 
paragraphs that showcase how you typically begin articles. Include your usual 
level of detail and any signature phrases or approaches.

## Key Point One

Elaborate on your first key point. Show how you typically develop ideas and 
provide examples or evidence.

* Bullet point example
* Another bullet point
* A third bullet point with **emphasized text**

## Key Point Two

Continue with your second main point. Include your typical paragraph structure
and transition style between ideas.

> If you often use quotes or callouts, include examples here to show how you format them.

### A Subsection Example

Demonstrate how you organize subtopics. Include any recurring patterns in how you 
break down complex ideas.

## Conclusion

Show how you typically wrap up articles. Include your signature closing style,
calls to action, or how you summarize key takeaways.

## References

- [Example link reference](https://example.com)
- Another reference source
```

## Tips for Better Results

1. **Provide Multiple Examples**: Upload 2-3 different style references for more consistent results.
2. **Refresh Periodically**: Update your style references every few months if your writing style evolves.
3. **Topic Variety**: Include references covering different topics to help the AI generalize your style.
4. **Clean Formatting**: Make sure your reference files have clean, consistent Markdown formatting.
5. **Highlight Uniqueness**: If you have unique style elements (e.g., a specific sign-off phrase), include examples.

## How the Vector Database Uses Style References

When you upload style references, the workflow:
1. Creates vector embeddings of your reference content
2. Analyzes semantic patterns in your writing
3. Stores these patterns in the Qdrant vector database
4. Uses them to inform content generation
5. Finds semantic similarities between new and existing content
6. Creates connections between related posts

By providing high-quality style references, you'll get better blog posts with more cohesive interrelationships across your content ecosystem. 