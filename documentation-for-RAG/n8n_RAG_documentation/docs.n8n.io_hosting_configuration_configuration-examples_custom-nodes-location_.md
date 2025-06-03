---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/custom-nodes-location/"
title: "Specify location for your custom nodes | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/custom-nodes-location/#specify-location-for-your-custom-nodes)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/custom-nodes-location.md "Edit this page")

# Specify location for your custom nodes [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/custom-nodes-location/\#specify-location-for-your-custom-nodes "Permanent link")

Every user can add custom nodes that get loaded by n8n on startup. The default
location is in the subfolder `.n8n/custom` of the user who started n8n.

You can define more folders with an environment variable:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_CUSTOM_EXTENSIONS="/home/jim/n8n/custom-nodes;/data/n8n/nodes"<br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/nodes/) for more information on this variable.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top