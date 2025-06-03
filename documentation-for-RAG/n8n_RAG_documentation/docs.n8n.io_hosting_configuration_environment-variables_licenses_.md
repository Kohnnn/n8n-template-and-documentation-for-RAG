---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/licenses/"
title: "License environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/licenses/#license-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/licenses.md "Edit this page")

# License environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/licenses/\#license-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

To enable certain licensed features, you must first activate your license. You can do this either through the UI or by setting environment variables. For more information, see [license key](https://docs.n8n.io/license-key/).

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_HIDE_USAGE_PAGE` | boolean | `false` | Hide the usage and plans page in the app. |
| `N8N_LICENSE_ACTIVATION_KEY` | String | `''` | Activation key to initialize license. Not applicable if the n8n instance was already activated. |
| `N8N_LICENSE_AUTO_RENEW_ENABLED` | Boolean | `true` | Enables (true) or disables (false) autorenewal for licenses. <br>If disabled, you need to manually renew the license every 10 days by navigating to **Settings** \> **Usage and plan**, and pressing `F5`. Failure to renew the license will disable all licensed features. |
| `N8N_LICENSE_DETACH_FLOATING_ON_SHUTDOWN` | Boolean | `true` | Controls whether the instance releases [floating entitlements](https://docs.n8n.io/glossary/#entitlement-n8n) back to the pool upon shutdown. Set to `true` to allow other instances to reuse the entitlements, or `false` to retain them. <br> For production instances that must always keep their licensed features, set this to `false`. |
| `N8N_LICENSE_SERVER_URL` | String | `http://license.n8n.io/v1` | Server URL to retrieve license. |
| `N8N_LICENSE_TENANT_ID` | Number | `1` | Tenant ID associated with the license. Only set this variable if explicitly instructed by n8n. |
| `https_proxy_license_server` | String | `https://user:pass@proxy:port` | Proxy server URL for HTTPS requests to retrieve license. This variable name needs to be lowercase. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top