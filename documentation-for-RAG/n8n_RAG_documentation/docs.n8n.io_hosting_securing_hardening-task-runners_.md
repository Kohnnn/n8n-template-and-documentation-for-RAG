---
url: "https://docs.n8n.io/hosting/securing/hardening-task-runners/"
title: "Hardening task runners | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/securing/hardening-task-runners/#hardening-task-runners)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/securing/hardening-task-runners.md "Edit this page")

# Hardening task runners [\#](https://docs.n8n.io/hosting/securing/hardening-task-runners/\#hardening-task-runners "Permanent link")

[Task runners](https://docs.n8n.io/hosting/configuration/task-runners/) are responsible for executing code from the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/). While Code node executions are secure, you can follow these recommendations to further harden your task runners.

## Run task runners as sidecars in external mode [\#](https://docs.n8n.io/hosting/securing/hardening-task-runners/\#run-task-runners-as-sidecars-in-external-mode "Permanent link")

To increase the isolation between the core n8n process and code in the Code node, run task runners in [external mode](https://docs.n8n.io/hosting/configuration/task-runners/#setting-up-external-mode). External task runners launch as separate containers, providing a fully isolated environment to execute the JavaScript defined in the Code node.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top