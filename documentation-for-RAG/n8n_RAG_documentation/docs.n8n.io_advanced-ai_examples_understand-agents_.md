---
url: "https://docs.n8n.io/advanced-ai/examples/understand-agents/"
title: "What's an agent in AI? | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/examples/understand-agents/#whats-an-agent-in-ai)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/examples/understand-agents.md "Edit this page")

# What's an agent in AI? [\#](https://docs.n8n.io/advanced-ai/examples/understand-agents/\#whats-an-agent-in-ai "Permanent link")

One way to think of an [agent](https://docs.n8n.io/glossary/#ai-agent) is as a [chain](https://docs.n8n.io/advanced-ai/examples/understand-chains/) that knows how to make decisions. Where a chain follows a predetermined sequence of calls to different AI components, an agent uses a language model to determine which actions to take.

Agents are the part of AI that act as decision-makers. They can interact with other agents and [tools](https://docs.n8n.io/glossary/#ai-tool). When you send a query to an agent, it tries to choose the best tools to use to answer. Agents adapt to your specific queries, as well as the prompts that configure their behavior.

## Agents in n8n [\#](https://docs.n8n.io/advanced-ai/examples/understand-agents/\#agents-in-n8n "Permanent link")

n8n provides one Agent node, which can act as different types of agent depending on the settings you choose. Refer to the [Agent node documentation](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) for details on the available agent types.

When execute a workflow containing an agent, the agent runs multiple times. For example, it may do an initial setup, followed by a run to call a tool, then another run to evaluate the tool response and respond to the user.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top