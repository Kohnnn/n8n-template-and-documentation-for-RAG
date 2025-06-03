---
url: "https://docs.n8n.io/hosting/logging-monitoring/monitoring/"
title: "Monitoring | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/logging-monitoring/monitoring/#monitoring)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/logging-monitoring/monitoring.md "Edit this page")

# Monitoring [\#](https://docs.n8n.io/hosting/logging-monitoring/monitoring/\#monitoring "Permanent link")

There are three API endpoints you can call to check the status of your instance: `/healthz`, `healthz/readiness`, and `/metrics`.

## healthz and healthz/readiness [\#](https://docs.n8n.io/hosting/logging-monitoring/monitoring/\#healthz-and-healthzreadiness "Permanent link")

The `/healthz` endpoint returns a standard HTTP status code. 200 indicates the instance is reachable. It doesn't indicate DB status. It's available for both self-hosted and Cloud users.

Access the endpoint:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br><your-instance-url>/healthz<br>``` |

The `/healthz/readiness` endpoint is similar to the `/healthz` endpoint, but it returns a HTTP status code of 200 if the DB is connected and migrated and therefore the instance is ready to accept traffic.

Access the endpoint:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br><your-instance-url>/healthz/readiness<br>``` |

## metrics [\#](https://docs.n8n.io/hosting/logging-monitoring/monitoring/\#metrics "Permanent link")

The `/metrics` endpoint provides more detailed information about the current status of the instance.

Access the endpoint:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br><your-instance-url>/metrics<br>``` |

Feature availability

The `/metrics` endpoint isn't available on n8n Cloud.

## Enable metrics and healthz for self-hosted n8n [\#](https://docs.n8n.io/hosting/logging-monitoring/monitoring/\#enable-metrics-and-healthz-for-self-hosted-n8n "Permanent link")

The `/metrics` and `/healthz` endpoints are disabled by default. To enable them, configure your n8n instance:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br># metrics<br>N8N_METRICS=true<br># healthz<br>QUEUE_HEALTH_CHECK_ACTIVE=true<br>``` |

Refer to [Configuration methods](https://docs.n8n.io/hosting/configuration/configuration-methods/) for more information on how to configure your instance using environment variables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top