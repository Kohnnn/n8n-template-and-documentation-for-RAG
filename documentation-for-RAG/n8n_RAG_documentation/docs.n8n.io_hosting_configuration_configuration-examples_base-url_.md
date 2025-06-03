---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/base-url/"
title: "Configure the Base URL for n8n's front end access | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/base-url/#configure-the-base-url-for-n8ns-front-end-access)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/base-url.md "Edit this page")

# Configure the Base URL for n8n's front end access [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/base-url/\#configure-the-base-url-for-n8ns-front-end-access "Permanent link")

Requires manual UI build

This use case involves configuring the `VUE_APP_URL_BASE_API` environmental variable which requires a manual build of the `n8n-editor-ui` package. You can't use it with the default n8n Docker image where the default setting for this variable is `/`, meaning that it uses the root-domain.

You can configure the Base URL that the front end uses to connect to the back end's REST API. This is relevant when you want to host n8n's front end and back end separately.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export VUE_APP_URL_BASE_API=https://n8n.example.com/<br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) for more information on this variable.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top