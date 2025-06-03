---
url: "https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/"
title: "LangChain concepts in n8n | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/#langchain-concepts-in-n8n)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/langchain/langchain-n8n.md "Edit this page")

# LangChain concepts in n8n [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#langchain-concepts-in-n8n "Permanent link")

This page explains how LangChain concepts and features map to n8n nodes.

This page includes lists of the LangChain-focused nodes in n8n. You can use any n8n node in a workflow where you interact with LangChain, to link LangChain to other services. The LangChain features uses n8n's [Cluster nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/).

n8n implements LangChain JS

This feature is n8n's implementation of [LangChain's JavaScript framework](https://js.langchain.com/docs/get_started/introduction).

## Trigger nodes [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#trigger-nodes "Permanent link")

[Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/)

## Cluster nodes [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#cluster-nodes "Permanent link")

[Cluster nodes](https://docs.n8n.io/glossary/#cluster-node-n8n) are node groups that work together to provide functionality in an n8n workflow. Instead of using a single node, you use a [root node](https://docs.n8n.io/glossary/#root-node-n8n) and one or more [sub-nodes](https://docs.n8n.io/glossary/#sub-node-n8n) that extend the functionality of the node.

[![Screenshot of a workflow with a root node and two sub-nodes](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)

### Root nodes [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#root-nodes "Permanent link")

Each cluster starts with one [root node](https://docs.n8n.io/glossary/#root-node-n8n).

#### Chains [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#chains "Permanent link")

A [chain](https://docs.n8n.io/glossary/#ai-chain) is a series of LLMs, and related tools, linked together to support functionality that can't be provided by a single LLM alone.

Available nodes:

- [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/)
- [Retrieval Q&A Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/)
- [Summarization Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization/)
- [Sentiment Analysis](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis/)
- [Text Classifier](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier/)

Learn more about [chaining in LangChain](https://js.langchain.com/docs/concepts/lcel).

#### Agents [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#agents "Permanent link")

> An [agent](https://docs.n8n.io/glossary/#ai-agent) has access to a suite of tools, and determines which ones to use depending on the user input. Agents can use multiple tools, and use the output of one tool as the input to the next. [Source](https://github.com/langchain-ai/langchainjs/blob/def3a26c054575e1ed40b9062087e8c0a8899633/docs/core_docs/docs/modules/agents/index.mdx)

Available nodes:

- [Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)

Learn more about [Agents in LangChain](https://js.langchain.com/docs/concepts/agents).

#### Vector stores [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#vector-stores "Permanent link")

[Vector stores](https://docs.n8n.io/glossary/#ai-vector-store) store embedded data, and perform vector searches on it.

- [Simple Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory/)
- [PGVector Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector/)
- [Pinecone Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone/)
- [Qdrant Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/)
- [Supabase Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase/)
- [Zep Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep/)

Learn more about [Vector stores in LangChain](https://js.langchain.com/docs/concepts/vectorstores/).

#### Miscellaneous [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#miscellaneous "Permanent link")

Utility nodes.

[LangChain Code](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code/): import LangChain. This means if there is functionality you need that n8n hasn't created a node for, you can still use it.

### Sub-nodes [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#sub-nodes "Permanent link")

Each root node can have one or more [sub-nodes](https://docs.n8n.io/glossary/#sub-node-n8n) attached to it.

#### Document loaders [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#document-loaders "Permanent link")

Document loaders add data to your chain as documents. The data source can be a file or web service.

Available nodes:

- [Default Document Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader/)
- [GitHub Document Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader/)

Learn more about [Document loaders in LangChain](https://js.langchain.com/docs/concepts/document_loaders).

#### Language models [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#language-models "Permanent link")

[LLMs (large language models)](https://docs.n8n.io/glossary/#large-language-model-llm) are programs that analyze datasets. They're the key element of working with AI.

Available nodes:

- [Anthropic Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic/)
- [AWS Bedrock Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock/)
- [Cohere Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere/)
- [Hugging Face Inference Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference/)
- [Mistral Cloud Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud/)
- [Ollama Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/)
- [Ollama Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/)
- [OpenAI Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/)

Learn more about [Language models in LangChain](https://js.langchain.com/docs/concepts/chat_models).

#### Memory [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#memory "Permanent link")

[Memory](https://docs.n8n.io/glossary/#ai-memory) retains information about previous queries in a series of queries. For example, when a user interacts with a chat model, it's useful if your application can remember and call on the full conversation, not just the most recent query entered by the user.

Available nodes:

- [Motorhead](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead/)
- [Redis Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat/)
- [Postgres Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat/)
- [Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/)
- [Xata](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata/)
- [Zep](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep/)

Learn more about [Memory in LangChain](https://langchain-ai.github.io/langgraphjs/concepts/memory/).

#### Output parsers [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#output-parsers "Permanent link")

Output parsers take the text generated by an LLM and format it to match the structure you require.

Available nodes:

- [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing/)
- [Item List Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist/)
- [Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/)

Learn more about [Output parsers in LangChain](https://js.langchain.com/docs/concepts/output_parsers/).

#### Retrievers [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#retrievers "Permanent link")

- [Contextual Compression Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression/)
- [MultiQuery Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery/)
- [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore/)
- [Workflow Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow/)

#### Text splitters [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#text-splitters "Permanent link")

Text splitters break down data (documents), making it easier for the LLM to process the information and return accurate results.

Available nodes:

- [Character Text Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter/)
- [Recursive Character Text Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter/)
- [Token Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter/)

n8n's text splitter nodes implements parts of [LangChain's text\_splitter API](https://js.langchain.com/docs/concepts/text_splitters/).

#### Tools [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#tools "Permanent link")

Utility [tools](https://docs.n8n.io/glossary/#ai-tool).

- [Calculator](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator/)
- [Code Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode/)
- [SerpAPI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi/)
- [Think Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink/)
- [Vector Store Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore/)
- [Wikipedia](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia/)
- [Wolfram\|Alpha](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha/)
- [Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/)

#### Embeddings [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#embeddings "Permanent link")

> [Embeddings](https://docs.n8n.io/glossary/#ai-embedding) capture the "relatedness" of text, images, video, or other types of information. ( [source](https://supabase.com/docs/guides/ai/concepts))

Available nodes:

- [Embeddings AWS Bedrock](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock/)
- [Embeddings Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere/)
- [Embeddings Google PaLM](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm/)
- [Embeddings Hugging Face Inference](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference/)
- [Embeddings Mistral Cloud](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud/)
- [Embeddings Ollama](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama/)
- [Embeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai/)

Learn more about [Text embeddings in LangChain](https://js.langchain.com/docs/concepts/embedding_models/).

#### Miscellaneous [\#](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/\#miscellaneous_1 "Permanent link")

- [Chat Memory Manager](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager/)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top