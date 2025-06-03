---
url: "https://docs.n8n.io/advanced-ai/examples/api-workflow-tool/"
title: "Call an API to fetch data | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/examples/api-workflow-tool/#call-an-api-to-fetch-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/examples/api-workflow-tool.md "Edit this page")

# Call an API to fetch data [\#](https://docs.n8n.io/advanced-ai/examples/api-workflow-tool/\#call-an-api-to-fetch-data "Permanent link")

Use n8n to bring data from any [API](https://docs.n8n.io/glossary/#api) to your AI. This workflow uses the [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/) to provide the chat interface, and the [Call n8n Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/) to call a second workflow that calls the API. The second workflow uses AI functionality to refine the API request based on the user's query.

[View workflow file](https://docs.n8n.io/_workflows/advanced-ai/examples/let_your_ai_call_an_api.json)

## Key features [\#](https://docs.n8n.io/advanced-ai/examples/api-workflow-tool/\#key-features "Permanent link")

This workflow uses:

- [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/): start your workflow and respond to user chat interactions. The node provides a customizable chat interface.
- [Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/): the key piece of the AI workflow. The Agent interacts with other components of the workflow and makes decisions about what tools to use.
- [Call n8n Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/): plug in n8n workflows as custom tools. In AI, a tool is an interface the AI can use to interact with the world (in this case, the data provided by your workflow). The AI model uses the tool to access information beyond its built-in dataset.
- A [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/) with an [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing/) and [Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/) to read the user's query and set parameters for the API call based on the user input.

## Using the example [\#](https://docs.n8n.io/advanced-ai/examples/api-workflow-tool/\#using-the-example "Permanent link")

To load the template into your n8n instance:

1. Download the workflow JSON file.
2. Open a new workflow in your n8n instance.
3. Copy in the JSON, or select **Workflow menu**![Workflow menu icon](https://docs.n8n.io/_images/common-icons/three-dots-horizontal.png) \> **Import from file...**.

The example workflows use Sticky Notes to guide you:

- Yellow: notes and information.
- Green: instructions to run the workflow.
- Orange: you need to change something to make the workflow work.
- Blue: draws attention to a key feature of the example.