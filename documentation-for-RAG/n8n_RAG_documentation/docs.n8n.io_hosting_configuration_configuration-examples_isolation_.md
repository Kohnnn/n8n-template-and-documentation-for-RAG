---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/isolation/"
title: "Isolate n8n | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/isolation/#isolate-n8n)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/isolation.md "Edit this page")

# Isolate n8n [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/isolation/\#isolate-n8n "Permanent link")

By default, a self-hosted n8n instance sends data to n8n's servers. It notifies users about available updates, workflow templates, and diagnostics.

To prevent your n8n instance from connecting to n8n's servers, set these environment variables to false:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>N8N_DIAGNOSTICS_ENABLED=false<br>N8N_VERSION_NOTIFICATIONS_ENABLED=false<br>N8N_TEMPLATES_ENABLED=false<br>``` |

Unset n8n's diagnostics configuration:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>EXTERNAL_FRONTEND_HOOKS_URLS=<br>N8N_DIAGNOSTICS_CONFIG_FRONTEND=<br>N8N_DIAGNOSTICS_CONFIG_BACKEND=<br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) for more information on these variables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top