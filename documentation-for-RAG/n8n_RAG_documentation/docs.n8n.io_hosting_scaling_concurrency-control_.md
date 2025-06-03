---
url: "https://docs.n8n.io/hosting/scaling/concurrency-control/"
title: "Concurrency control | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/scaling/concurrency-control/#self-hosted-concurrency-control)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/scaling/concurrency-control.md "Edit this page")

# Self-hosted concurrency control [\#](https://docs.n8n.io/hosting/scaling/concurrency-control/\#self-hosted-concurrency-control "Permanent link")

Only for self-hosted n8n

This document is for self-hosted concurrency control. Read [Cloud concurrency](https://docs.n8n.io/manage-cloud/concurrency/) to learn how concurrency works with n8n Cloud accounts.

In regular mode, n8n doesn't limit how many production executions may run at the same time. This can lead to a scenario where too many concurrent executions thrash the event loop, causing performance degradation and unresponsiveness.

To prevent this, you can set a concurrency limit for production executions in regular mode. Use this to control how many production executions run concurrently, and queue up any concurrent production executions over the limit. These executions remain in the queue until concurrency capacity frees up, and are then processed in FIFO order.

Concurrency control is disabled by default. To enable it:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_CONCURRENCY_PRODUCTION_LIMIT=20<br>``` |

Keep in mind:

- Concurrency control applies only to production executions: those started from a webhook or [trigger](https://docs.n8n.io/glossary/#trigger-node-n8n) node. It doesn't apply to any other kinds, such as manual executions, sub-workflow executions, error executions, or started from CLI.
- You can't retry queued executions. Cancelling or deleting a queued execution also removes it from the queue.
- On instance startup, n8n resumes queued executions up to the concurrency limit and re-enqueues the rest.

- To monitor concurrency control, watch logs for executions being added to the queue and released. In a future version, n8n will show concurrency control in the UI.

When you enable concurrency control, you can view the number of active executions and the configured limit at the top of a project's or workflow's executions tab.

## Comparison to queue mode [\#](https://docs.n8n.io/hosting/scaling/concurrency-control/\#comparison-to-queue-mode "Permanent link")

In queue mode, you can control how many jobs a worker may run concurrently using the [`--concurrency` flag](https://docs.n8n.io/hosting/scaling/queue-mode/#configure-worker-concurrency).

Concurrency control in queue mode is a separate mechanism from concurrency control in regular mode, but the environment variable `N8N_CONCURRENCY_PRODUCTION_LIMIT` controls both of them. In queue mode, n8n takes the limit from this variable if set to a value other than `-1`, falling back to the `--concurrency` flag or its default.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top