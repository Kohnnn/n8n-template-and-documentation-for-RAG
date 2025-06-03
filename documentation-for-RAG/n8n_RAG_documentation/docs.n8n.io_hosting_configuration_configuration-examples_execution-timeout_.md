---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/execution-timeout/"
title: "Configure workflow timeout settings | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/execution-timeout/#configure-workflow-timeout-settings)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/execution-timeout.md "Edit this page")

# Configure workflow timeout settings [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/execution-timeout/\#configure-workflow-timeout-settings "Permanent link")

A workflow times out and gets canceled after this time (in seconds). If the workflow runs in the main process, a soft timeout happens (takes effect after the current node finishes). If a workflow runs in its own process, n8n attempts a soft timeout first, then kills the process after waiting for a fifth of the given timeout duration.

`EXECUTIONS_TIMEOUT` default is `-1`. For example, if you want to set the timeout to one hour:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export EXECUTIONS_TIMEOUT=3600<br>``` |

You can also set maximum execution time (in seconds) for each workflow individually. For example, if you want to set maximum execution time to two hours:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export EXECUTIONS_TIMEOUT_MAX=7200<br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/executions/) for more information on these variables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top