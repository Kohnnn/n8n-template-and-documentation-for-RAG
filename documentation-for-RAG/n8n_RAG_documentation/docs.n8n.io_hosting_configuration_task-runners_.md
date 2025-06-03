---
url: "https://docs.n8n.io/hosting/configuration/task-runners/"
title: "Task runners | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/task-runners/#task-runners)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/task-runners.md "Edit this page")

# Task runners [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#task-runners "Permanent link")

Task runners are a generic mechanism to execute tasks in a secure and performant way. They're used to execute user-provided JavaScript code in the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/).

This document describes how task runners work and how you can configure them.

## How it works [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#how-it-works "Permanent link")

The task runner feature consists of three components: a task runner, a task broker, and a task requester.

[![Task runner overview](https://docs.n8n.io/_images/hosting/configuration/task-runner-concept.png)](https://docs.n8n.io/_images/hosting/configuration/task-runner-concept.png)

Task runners connect to the task broker using a websocket connection. A task requester submits a task request to the broker where an available task runner can pick it up for execution.

The runner executes the task and submits the results to the task requester. The task broker coordinates communication between the runner and the requester.

The n8n instance (main and worker) acts as the broker. The Code node in this case is the task requester.

## Task runner modes [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#task-runner-modes "Permanent link")

You can use task runners in two different modes: internal and external.

### Internal mode [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#internal-mode "Permanent link")

In internal mode, the n8n instance launches the task runner as a child process. The n8n process monitors and manages the life cycle of the task runner. The task runner process shares the same `uid` and `gid` as n8n.

### External mode [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#external-mode "Permanent link")

In external mode, an external orchestrator (for example, Kubernetes) launches the task runner instead of n8n. Typically, this means you would configure the task runner to run as a side-car container next to n8n.

[![Task runner deployed as a side-car container](https://docs.n8n.io/_images/hosting/configuration/task-runner-external-mode.png)](https://docs.n8n.io/_images/hosting/configuration/task-runner-external-mode.png)

In this mode, the orchestrator monitors and manages the life cycle of the task runner container. The task runner is fully isolated from the n8n instance.

When using the [Queue mode](https://docs.n8n.io/hosting/scaling/queue-mode/), each n8n container (main and workers) needs to have its own task runner.

## Setting up external mode [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#setting-up-external-mode "Permanent link")

Use the following details to configure task runners in external mode

### Configuring n8n instance in external mode [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#configuring-n8n-instance-in-external-mode "Permanent link")

You can configure n8n to use external task runners by setting the following environment variables:

| Environment variables | Description |
| --- | --- |
| `N8N_RUNNERS_ENABLED=true` | Enables task runners. |
| `N8N_RUNNERS_MODE=external` | Use task runners in external mode. |
| `N8N_RUNNERS_AUTH_TOKEN=<random secure shared secret>` | A shared secret task runners use to connect to the broker. |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0` | By default, the task broker only listens to localhost. When using multiple containers (for example, with Docker Compose), it needs to be able to accept external connections. |

For full list of environment variables see [task runner environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/).

### Configuring task runners in external mode [\#](https://docs.n8n.io/hosting/configuration/task-runners/\#configuring-task-runners-in-external-mode "Permanent link")

The task runner comes bundled within the n8n Docker image. The Docker image also includes the task runner launcher.

The launcher can start the runner on-demand, which means lower memory usage when there's no work needed, but a short delay (few hundred ms) in cold-start. The launcher also monitors the runner and restarts it in case of infinite loops or other issues.

Run a task runner container from the n8n Docker image by setting the following properties:

| Configuration | Description |
| --- | --- |
| `command` | `["/usr/local/bin/task-runner-launcher", "javascript"]` |
| `livenessProbe` | `GET /healthz`, port `5680` |

Set the following environment variables for the container, adjusted to fit your needs:

| Environment variables | Description |
| --- | --- |
| `N8N_RUNNERS_AUTH_TOKEN=<random secure shared secret>` | The shared secret the task runner uses to connect to the broker. |
| `N8N_RUNNERS_MAX_CONCURRENCY=5` | The number of concurrent tasks the runner can execute. |
| `N8N_RUNNERS_TASK_BROKER_URI=localhost:5679` | The address of the task broker server within the n8n instance. |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT=15` | Number of seconds of inactivity to wait before shutting down the task runner process. The launcher will automatically start the runner again when there are new tasks to execute. Set to `0` to disable automatic shutdown. |
| `NODE_OPTIONS=--max-old-space-size=<limit>` | The memory limit for the task runner Node.js process. This should be lower than the limit for container so that the runner runs out of memory before the container. That way, the launcher is able to monitor the runner. |
| `GENERIC_TIMEZONE` | The [same default timezone as configured for the n8n instance](https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/). |

For full list of environment variables see [task runner environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top