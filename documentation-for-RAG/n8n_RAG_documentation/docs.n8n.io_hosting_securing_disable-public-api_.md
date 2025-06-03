---
url: "https://docs.n8n.io/hosting/securing/disable-public-api/"
title: "Disable the public REST API | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/securing/disable-public-api/#disable-the-public-rest-api)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/securing/disable-public-api.md "Edit this page")

# Disable the public REST API [\#](https://docs.n8n.io/hosting/securing/disable-public-api/\#disable-the-public-rest-api "Permanent link")

The [n8n public REST API](https://docs.n8n.io/api/) allows you to programmatically perform many of the same tasks as you can in the n8n GUI.

If you don't plan on using this API, n8n recommends disabling it to improve the security of your n8n installation.

To disable the [public REST API](https://docs.n8n.io/api/), set the `N8N_PUBLIC_API_DISABLED` environment variable to `true`, for example:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_PUBLIC_API_DISABLED=true<br>``` |

## Disable the API playground [\#](https://docs.n8n.io/hosting/securing/disable-public-api/\#disable-the-api-playground "Permanent link")

To disable the [API playground](https://docs.n8n.io/api/using-api-playground/), set the `N8N_PUBLIC_API_SWAGGERUI_DISABLED` environment variable to `true`, for example:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_PUBLIC_API_SWAGGERUI_DISABLED=true<br>``` |

## Related resources [\#](https://docs.n8n.io/hosting/securing/disable-public-api/\#related-resources "Permanent link")

Refer to [Deployment environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) for more information on these environment variables.

Refer to [Configuration](https://docs.n8n.io/hosting/configuration/configuration-methods/) for more information on setting environment variables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top