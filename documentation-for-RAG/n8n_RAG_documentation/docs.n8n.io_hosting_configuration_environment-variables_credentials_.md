---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/credentials/"
title: "Credentials environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/credentials/#credentials-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/credentials.md "Edit this page")

# Credentials environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/credentials/\#credentials-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

Enable credential overwrites using the following environment variables. Refer to [Credential overwrites](https://docs.n8n.io/embed/configuration/#credential-overwrites) for details.

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `CREDENTIALS_OVERWRITE_DATA`<br>/ `_FILE` | \* | - | Overwrites for credentials. |
| `CREDENTIALS_OVERWRITE_ENDPOINT` | String | - | The API endpoint to fetch credentials. |
| `CREDENTIALS_DEFAULT_NAME` | String | `My credentials` | The default name for credentials. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top