---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/insights/"
title: "Insights environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/insights/#insights-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/insights.md "Edit this page")

# Insights environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/insights/\#insights-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

Insights gives instance owners and admins visibility into how workflows perform over time. Refer to [Insights](https://docs.n8n.io/insights/) for details.

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_DISABLED_MODULES` | String | - | Set to `insights` to disable the feature and metrics collection for an instance. |
| `N8N_INSIGHTS_COMPACTION_BATCH_SIZE` | Number | 500 | The number of raw insights data to compact in a single batch. |
| `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` | Number | 180 | The maximum age (in days) of daily insights data to compact. |
| `N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` | Number | 90 | The maximum age (in days) of hourly insights data to compact. |
| `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES` | Number | 60 | Interval (in minutes) at which compaction should run. |
| `N8N_INSIGHTS_FLUSH_BATCH_SIZE` | Number | 1000 | The maximum number of insights data to keep in the buffer before flushing. |
| `N8N_INSIGHTS_FLUSH_INTERVAL_SECONDS` | Number | 30 | The interval (in seconds) at which the insights data should be flushed to the database. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top