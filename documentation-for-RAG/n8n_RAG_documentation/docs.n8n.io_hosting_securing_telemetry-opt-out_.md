---
url: "https://docs.n8n.io/hosting/securing/telemetry-opt-out/"
title: "Opt out of data collection | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/securing/telemetry-opt-out/#data-collection)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/securing/telemetry-opt-out.md "Edit this page")

# Data collection [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#data-collection "Permanent link")

n8n collects some anonymous data from self-hosted n8n installations. Use the instructions below to opt out of data telemetry collection.

## Collected data [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#collected-data "Permanent link")

Refer to [Privacy \| Data collection in self-hosted n8n](https://docs.n8n.io/privacy-security/privacy/#data-collection-in-self-hosted-n8n) for details on the data n8n collects.

## How collection works [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#how-collection-works "Permanent link")

Your n8n instance sends most data to n8n as the events that generate it occur. Workflow execution counts and an instance pulse are sent periodically (every 6 hours). These data types mostly fall into n8n telemetry collection.

## Opting out of data collection [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#opting-out-of-data-collection "Permanent link")

n8n enables telemetry collection by default. To disable it, configure the following environment variables.

### Opt out of telemetry events [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#opt-out-of-telemetry-events "Permanent link")

To opt out of telemetry events, set the `N8N_DIAGNOSTICS_ENABLED` environment variable to false, for example:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_DIAGNOSTICS_ENABLED=false<br>``` |

### Opt out of checking for new versions of n8n [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#opt-out-of-checking-for-new-versions-of-n8n "Permanent link")

To opt out of checking for new versions of n8n, set the `N8N_VERSION_NOTIFICATIONS_ENABLED` environment variable to false, for example:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_VERSION_NOTIFICATIONS_ENABLED=false<br>``` |

## Disable all connection to n8n servers [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#disable-all-connection-to-n8n-servers "Permanent link")

If you want to fully prevent all communication with n8n's servers, refer to [Isolate n8n](https://docs.n8n.io/hosting/configuration/configuration-examples/isolation/).

## Related resources [\#](https://docs.n8n.io/hosting/securing/telemetry-opt-out/\#related-resources "Permanent link")

Refer to [Deployment environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) for more information on these environment variables.

Refer to [Configuration](https://docs.n8n.io/hosting/configuration/configuration-methods/) for more information on setting environment variables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top