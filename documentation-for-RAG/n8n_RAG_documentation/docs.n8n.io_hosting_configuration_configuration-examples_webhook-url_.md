---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/webhook-url/"
title: "Configure webhook URLs with reverse proxy | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/webhook-url/#configure-n8n-webhooks-with-reverse-proxy)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/webhook-url.md "Edit this page")

# Configure n8n webhooks with reverse proxy [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/webhook-url/\#configure-n8n-webhooks-with-reverse-proxy "Permanent link")

n8n creates the webhook URL by combining `N8N_PROTOCOL`, `N8N_HOST` and `N8N_PORT`. If n8n runs behind a reverse proxy, that won't work. That's because n8n runs internally on port 5678 but the reverse proxy exposes it to the web on port 443. In that case, it's important to set the webhook URL manually so that n8n can display it in the Editor UI and register the correct webhook URLs with external services.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export WEBHOOK_URL=https://n8n.example.com/<br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/endpoints/) for more information on this variable.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top