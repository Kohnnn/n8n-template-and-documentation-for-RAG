---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/"
title: "Task runner environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/#task-runner-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/task-runners.md "Edit this page")

# Task runner environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/\#task-runner-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

[Task runners](https://docs.n8n.io/hosting/configuration/task-runners/) execute code defined by the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/).

## n8n instance environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/\#n8n-instance-environment-variables "Permanent link")

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_RUNNERS_ENABLED` | Boolean | `false` | Are task runners enabled. |
| `N8N_RUNNERS_MODE` | Enum string: `internal`, `external` | `internal` | How to launch and run the task runner. `internal` means n8n will launch a task runner as child process. `external` means an external orchestrator will launch the task runner. |
| `N8N_RUNNERS_AUTH_TOKEN` | String | Random string | Shared secret used by a task runner to authenticate to n8n. Required when using `external` mode. |
| `N8N_RUNNERS_BROKER_PORT` | Number | `5679` | Port the task broker listens on for task runner connections. |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS` | String | `127.0.0.1` | Address the task broker listens on. |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | Maximum payload size in bytes for communication between a task broker and a task runner. |
| `N8N_RUNNERS_MAX_OLD_SPACE_SIZE` | String |  | The `--max-old-space-size` option to use for a task runner (in MB). By default, Node.js will set this based on available memory. |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | The number of concurrent tasks a task runner can execute at a time. |
| `N8N_RUNNERS_TASK_TIMEOUT` | Number | `60` | How long (in seconds) a task can take to complete before the task aborts and the runner restarts. Must be greater than 0. |
| `N8N_RUNNERS_HEARTBEAT_INTERVAL` | Number | `30` | How often (in seconds) the runner must send a heartbeat to the broker, else the task aborts and the runner restarts. Must be greater than 0. |

## Task runner launcher environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/\#task-runner-launcher-environment-variables "Permanent link")

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_RUNNERS_LAUNCHER_LOG_LEVEL` | Enum string: `debug`, `info`, `warn`, `error` | `info` | Which log messages to show. |
| `N8N_RUNNERS_AUTH_TOKEN` | String | - | Shared secret used to authenticate to n8n. |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | The number of seconds to wait before shutting down an idle runner. |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | The URI of the task broker server (n8n instance). |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | Port for the launcher's health check server. |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | Maximum payload size in bytes for communication between a task broker and a task runner. |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | The number of concurrent tasks a task runner can execute at a time. |
| `NODE_OPTIONS` | String | - | [Options](https://nodejs.org/api/cli.html#node_optionsoptions) for Node.js. |

## Task runner environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/task-runners/\#task-runner-environment-variables_1 "Permanent link")

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_RUNNERS_GRANT_TOKEN` | String | Random string | Token the runner uses to authenticate with the task broker. This is automatically provided by the launcher. |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | The number of seconds to wait before shutting down an idle runner. |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | The URI of the task broker server (n8n instance). |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | Port for the launcher's health check server. |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | Maximum payload size in bytes for communication between a task broker and a task runner. |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | The number of concurrent tasks a task runner can execute at a time. |
| `NODE_FUNCTION_ALLOW_BUILTIN` | String | - | Permit users to import specific built-in modules in the Code node. Use \* to allow all. n8n disables importing modules by default. |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | String | - | Permit users to import specific external modules (from `n8n/node_modules`) in the Code node. n8n disables importing modules by default. |
| `N8N_RUNNERS_ALLOW_PROTOTYPE_MUTATION` | Boolean | `false` | Whether to allow prototype mutation for external libraries. Set to `true` to allow modules that rely on runtime prototype mutation (for example, [`puppeteer`](https://pptr.dev/)) at the cost of relaxing security. |
| `GENERIC_TIMEZONE` | \* | `America/New_York` | The [same default timezone as configured for the n8n instance](https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/). |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top