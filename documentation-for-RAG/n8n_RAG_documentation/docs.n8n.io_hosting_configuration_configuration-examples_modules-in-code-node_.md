---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/modules-in-code-node/"
title: "Enable modules in Code node | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/modules-in-code-node/#enable-modules-in-code-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/modules-in-code-node.md "Edit this page")

# Enable modules in Code node [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/modules-in-code-node/\#enable-modules-in-code-node "Permanent link")

For security reasons, the Code node restricts importing modules. It's possible to lift that restriction for built-in and external modules by setting the following environment variables:

- `NODE_FUNCTION_ALLOW_BUILTIN`: For built-in modules
- `NODE_FUNCTION_ALLOW_EXTERNAL`: For external modules sourced from n8n/node\_modules directory. External module support is disabled when an environment variable isn't set.

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># Allows usage of all builtin modules<br>export NODE_FUNCTION_ALLOW_BUILTIN=*<br># Allows usage of only crypto<br>export NODE_FUNCTION_ALLOW_BUILTIN=crypto<br># Allows usage of only crypto and fs<br>export NODE_FUNCTION_ALLOW_BUILTIN=crypto,fs<br># Allow usage of external npm modules.<br>export NODE_FUNCTION_ALLOW_EXTERNAL=moment,lodash<br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/nodes/) for more information on these variables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top