---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/source-control/"
title: "Source control environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/source-control/#source-control-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/source-control.md "Edit this page")

# Source control environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/source-control/\#source-control-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

n8n uses Git-based source control to support environments. Refer to [Source control and environments](https://docs.n8n.io/source-control-environments/setup/) for more information on how to link a Git repository to an n8n instance and configure your source control.

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_SOURCECONTROL_DEFAULT_SSH_KEY_TYPE` | String | `ed25519` | Set to `rsa` to make RSA the default SSH key type for [Source control setup](https://docs.n8n.io/source-control-environments/setup/). |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top