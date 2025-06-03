---
url: "https://docs.n8n.io/advanced-ai/examples/understand-memory/"
title: "What's memory in AI? | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/examples/understand-memory/#whats-memory-in-ai)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/examples/understand-memory.md "Edit this page")

# What's memory in AI? [\#](https://docs.n8n.io/advanced-ai/examples/understand-memory/\#whats-memory-in-ai "Permanent link")

Memory is a key part of AI chat services. The [memory](https://docs.n8n.io/glossary/#ai-memory) keeps a history of previous messages, allowing for an ongoing conversation with the AI, rather than every interaction starting fresh.

## AI memory in n8n [\#](https://docs.n8n.io/advanced-ai/examples/understand-memory/\#ai-memory-in-n8n "Permanent link")

To add memory to your AI workflow you can use either:

- [Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/): stores a customizable length of chat history for the current session. This is the easiest to get started with.
- One of the memory services that n8n provides nodes for. These include:
  - [Motorhead](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead/)
  - [Redis Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat/)
  - [Postgres Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat/)
  - [Xata](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata/)
  - [Zep](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep/)

If you need to do advanced AI memory management in your workflows, use the [Chat Memory Manager](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager/) node.

This node is useful when you:

- Can't add a memory node directly.
- Need to do more complex memory management, beyond what the memory nodes offer. For example, you can add this node to check the memory size of the Agent node's response, and reduce it if needed.
- Want to inject messages to the AI that look like user messages, to give the AI more context.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top