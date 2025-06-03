---
url: "https://docs.n8n.io/advanced-ai/examples/agent-chain-comparison/"
title: "Agents vs chains | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/examples/agent-chain-comparison/#demonstration-of-key-differences-between-agents-and-chains)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/examples/agent-chain-comparison.md "Edit this page")

# Demonstration of key differences between agents and chains [\#](https://docs.n8n.io/advanced-ai/examples/agent-chain-comparison/\#demonstration-of-key-differences-between-agents-and-chains "Permanent link")

In this workflow you can choose whether your chat query goes to an [agent](https://docs.n8n.io/glossary/#ai-agent) or [chain](https://docs.n8n.io/glossary/#ai-chain). It shows some of the ways that agents are more powerful than chains.

[View workflow file](https://docs.n8n.io/_workflows/advanced-ai/examples/agents_vs_chains.json)

## Key features [\#](https://docs.n8n.io/advanced-ai/examples/agent-chain-comparison/\#key-features "Permanent link")

This workflow uses:

- [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/): start your workflow and respond to user chat interactions. The node provides a customizable chat interface.
- [Switch node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/): directs your query to either the agent or chain, depending on which you specify in your query. If you say "agent" it sends it to the agent. If you say "chain" it sends it to the chain.
- [Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/): the Agent node interacts with other components of the workflow and makes decisions about what [tools](https://docs.n8n.io/glossary/#ai-tool) to use.
- [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/): the Basic LLM Chain node supports chatting with a connected LLM, but doesn't support [memory](https://docs.n8n.io/glossary/#ai-memory) or tools.

## Using the example [\#](https://docs.n8n.io/advanced-ai/examples/agent-chain-comparison/\#using-the-example "Permanent link")

To load the template into your n8n instance:

1. Download the workflow JSON file.
2. Open a new workflow in your n8n instance.
3. Copy in the JSON, or select **Workflow menu**![Workflow menu icon](https://docs.n8n.io/_images/common-icons/three-dots-horizontal.png) \> **Import from file...**.

The example workflows use Sticky Notes to guide you:

- Yellow: notes and information.
- Green: instructions to run the workflow.
- Orange: you need to change something to make the workflow work.
- Blue: draws attention to a key feature of the example.