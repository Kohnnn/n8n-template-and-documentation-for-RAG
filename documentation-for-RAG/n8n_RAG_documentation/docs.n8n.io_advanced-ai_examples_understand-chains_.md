---
url: "https://docs.n8n.io/advanced-ai/examples/understand-chains/"
title: "What's a chain in AI? | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/examples/understand-chains/#whats-a-chain-in-ai)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/examples/understand-chains.md "Edit this page")

# What's a chain in AI? [\#](https://docs.n8n.io/advanced-ai/examples/understand-chains/\#whats-a-chain-in-ai "Permanent link")

[Chains](https://docs.n8n.io/glossary/#ai-chain) bring together different components of AI to create a cohesive system. They set up a sequence of calls between the components. These components can include models and [memory](https://docs.n8n.io/glossary/#ai-memory) (though note that in n8n chains can't use memory).

## Chains in n8n [\#](https://docs.n8n.io/advanced-ai/examples/understand-chains/\#chains-in-n8n "Permanent link")

n8n provides three chain nodes:

- [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/): use to interact with an LLM, without any additional components.
- [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/): can connect to a [vector store](https://docs.n8n.io/glossary/#ai-vector-store) using a retriever, or to an n8n workflow using the Workflow Retriever node. Use this if you want to create a workflow that supports asking questions about specific documents.
- [Summarization Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization/): takes an input and returns a summary.

There's an important difference between chains in n8n and in other tools such as LangChain: none of the chain nodes support memory. This means they can't remember previous user queries. If you use LangChain to code an AI application, you can give your application memory. In n8n, if you need your workflow to support memory, use an agent. This is essential if you want users to be able to have a natural ongoing conversation with your app.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top