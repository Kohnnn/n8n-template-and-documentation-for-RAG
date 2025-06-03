---
url: "https://docs.n8n.io/log-streaming/"
title: "Log streaming | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/log-streaming/#log-streaming)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/log-streaming.md "Edit this page")

# Log streaming [\#](https://docs.n8n.io/log-streaming/\#log-streaming "Permanent link")

Feature availability

Log streaming is available on Enterprise Self-hosted and Cloud plans.

Log streaming allows you to send events from n8n to your own logging tools. This allows you to manage your n8n monitoring in your own alerting and logging processes.

## Set up log streaming [\#](https://docs.n8n.io/log-streaming/\#set-up-log-streaming "Permanent link")

To use log streaming, you have to add a streaming destination.

1. Navigate to **Settings** \> **Log Streaming**.
2. Select **Add new destination**.
3. Choose your destination type. n8n opens the **New Event Destination** modal.
4. In the **New Event Destination** modal, enter the configuration information for your event destination. These depend on the type of destination you're using.
5. Select **Events** to choose which events to stream.
6. Select **Save**.

Self-hosted users

If you self-host n8n, you can configure additional log streaming behavior using [Environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/logs/#log-streaming).

## Events [\#](https://docs.n8n.io/log-streaming/\#events "Permanent link")

The following events are available. You can choose which events to stream in **Settings** \> **Log Streaming** \> **Events**.

- Workflow
  - Started
  - Success
  - Failed
- Node executions
  - Started
  - Finished
- Audit
  - User signed up
  - User updated
  - User deleted
  - User invited
  - User invitation accepted
  - User re-invited
  - User email failed
  - User reset requested
  - User reset
  - User credentials created
  - User credentials shared
  - User credentials updated
  - User credentials deleted
  - User API created
  - User API deleted
  - Package installed
  - Package updated
  - Package deleted
  - Workflow created
  - Workflow deleted
  - Workflow updated
- AI node logs
  - Memory get messages
  - Memory added message
  - Output parser get instructions
  - Output parser parsed
  - Retriever get relevant documents
  - Embeddings embedded document
  - Embeddings embedded query
  - Document processed
  - Text splitter split
  - Tool called
  - Vector store searched
  - LLM generated
  - Vector store populated

## Destinations [\#](https://docs.n8n.io/log-streaming/\#destinations "Permanent link")

n8n supports three destination types:

- A syslog server
- A generic webhook
- A Sentry client

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top