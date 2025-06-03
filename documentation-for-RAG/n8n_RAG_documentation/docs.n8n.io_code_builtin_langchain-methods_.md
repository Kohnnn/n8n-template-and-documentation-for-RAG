---
url: "https://docs.n8n.io/code/builtin/langchain-methods/"
title: "LangChain Code node | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/builtin/langchain-methods/#langchain-code-node-methods)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/langchain-methods.md "Edit this page")

# LangChain Code node methods [\#](https://docs.n8n.io/code/builtin/langchain-methods/\#langchain-code-node-methods "Permanent link")

n8n provides these methods to make it easier to perform common tasks in the [LangChain Code node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code/).

LangChain Code node only

These variables are for use in expressions in the LangChain Code node. You can't use them in other nodes.

| Method | Description |
| --- | --- |
| `this.addInputData(inputName, data)` | Populate the data of a specified non-main input. Useful for mocking data.<br>- `inputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`<br>- `data` contains the data you want to add. Refer to [Data structure](https://docs.n8n.io/data/data-structure/) for information on the data structure expected by n8n. |
| `this.addOutputData(outputName, data)` | Populate the data of a specified non-main output. Useful for mocking data.<br>- `outputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`<br>- `data` contains the data you want to add. Refer to [Data structure](https://docs.n8n.io/data/data-structure/) for information on the data structure expected by n8n. |
| `this.getInputConnectionData(inputName, itemIndex, inputIndex?)` | Get data from a specified non-main input.<br>- `inputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`<br>- `itemIndex` should always be `0` (this parameter will be used in upcoming functionality)<br>- Use `inputIndex` if there is more than one node connected to the specified input. |
| `this.getInputData(inputIndex?, inputName?)` | Get data from the main input. |
| `this.getNode()` | Get the current node. |
| `this.getNodeOutputs()` | Get the outputs of the current node. |
| `this.getExecutionCancelSignal()` | Use this to stop the execution of a function when the workflow stops. In most cases n8n handles this, but you may need to use it if building your own chains or agents. It replaces the [Cancelling a running LLMChain](https://js.langchain.com/docs/modules/chains/foundational/llm_chain#cancelling-a-running-llmchain) code that you'd use if building a LangChain application normally. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top