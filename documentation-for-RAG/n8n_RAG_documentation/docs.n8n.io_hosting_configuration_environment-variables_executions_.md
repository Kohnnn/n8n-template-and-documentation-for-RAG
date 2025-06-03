---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/executions/"
title: "Executions environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/executions/#executions-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/executions.md "Edit this page")

# Executions environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/executions/\#executions-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

This page lists environment variables to configure workflow execution settings.

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `EXECUTIONS_MODE` | Enum string: `regular`, `queue` | `regular` | Whether executions should run directly or using queue.<br>Refer to [Queue mode](https://docs.n8n.io/hosting/scaling/queue-mode/) for more details. |
| `EXECUTIONS_TIMEOUT` | Number | `-1` | Sets a default timeout (in seconds) to all workflows after which n8n stops their execution. Users can override this for individual workflows up to the duration set in `EXECUTIONS_TIMEOUT_MAX`. Set `EXECUTIONS_TIMEOUT` to `-1` to disable. |
| `EXECUTIONS_TIMEOUT_MAX` | Number | `3600` | The maximum execution time (in seconds) that users can set for an individual workflow. |
| `EXECUTIONS_DATA_SAVE_ON_ERROR` | Enum string: `all`, `none` | `all` | Whether n8n saves execution data on error. |
| `EXECUTIONS_DATA_SAVE_ON_SUCCESS` | Enum string: `all`, `none` | `all` | Whether n8n saves execution data on success. |
| `EXECUTIONS_DATA_SAVE_ON_PROGRESS` | Boolean | `false` | Whether to save progress for each node executed (true) or not (false). |
| `EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS` | Boolean | `true` | Whether to save data of executions when started manually. |
| `EXECUTIONS_DATA_PRUNE` | Boolean | `true` | Whether to delete data of past executions on a rolling basis. |
| `EXECUTIONS_DATA_MAX_AGE` | Number | `336` | The execution age (in hours) before it's deleted. |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | Number | `10000` | Maximum number of executions to keep in the database. 0 = no limit |
| `EXECUTIONS_DATA_HARD_DELETE_BUFFER` | Number | `1` | How old (hours) the finished execution data has to be to get hard-deleted. By default, this buffer excludes recent executions as the user may need them while building a workflow. |
| `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL` | Number | `15` | How often (minutes) execution data should be hard-deleted. |
| `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL` | Number | `60` | How often (minutes) execution data should be soft-deleted. |
| `N8N_CONCURRENCY_PRODUCTION_LIMIT` | Number | `-1` | Max production executions allowed to run concurrently, in both regular and scaling modes. `-1` to disable in regular mode. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top