---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus/"
title: "Enable Prometheus metrics | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus/#enable-prometheus-metrics)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/prometheus.md "Edit this page")

# Enable Prometheus metrics [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus/\#enable-prometheus-metrics "Permanent link")

To collect and expose metrics, n8n uses the [prom-client](https://www.npmjs.com/package/prom-client) library.

The `/metrics` endpoint is disabled by default, but it's possible to enable it using the `N8N_METRICS` environment variable.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_METRICS=true<br>``` |

Refer to the respective [Environment Variables](https://docs.n8n.io/hosting/configuration/environment-variables/endpoints/) ( `N8N_METRICS_INCLUDE_*`) for configuring which metrics and labels should get exposed.

Both `main` and `worker` instances are able to expose metrics.

## Queue metrics [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus/\#queue-metrics "Permanent link")

To enable queue metrics, set the `N8N_METRICS_INCLUDE_QUEUE_METRICS` env var to `true`. You can adjust the refresh rate with `N8N_METRICS_QUEUE_METRICS_INTERVAL`.

Queue metrics are only available for the `main` instance in single-main mode.

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>``` | ```<br># HELP n8n_scaling_mode_queue_jobs_active Current number of jobs being processed across all workers in scaling mode.<br># TYPE n8n_scaling_mode_queue_jobs_active gauge<br>n8n_scaling_mode_queue_jobs_active 0<br># HELP n8n_scaling_mode_queue_jobs_completed Total number of jobs completed across all workers in scaling mode since instance start.<br># TYPE n8n_scaling_mode_queue_jobs_completed counter<br>n8n_scaling_mode_queue_jobs_completed 0<br># HELP n8n_scaling_mode_queue_jobs_failed Total number of jobs failed across all workers in scaling mode since instance start.<br># TYPE n8n_scaling_mode_queue_jobs_failed counter<br>n8n_scaling_mode_queue_jobs_failed 0<br># HELP n8n_scaling_mode_queue_jobs_waiting Current number of enqueued jobs waiting for pickup in scaling mode.<br># TYPE n8n_scaling_mode_queue_jobs_waiting gauge<br>n8n_scaling_mode_queue_jobs_waiting 0<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top