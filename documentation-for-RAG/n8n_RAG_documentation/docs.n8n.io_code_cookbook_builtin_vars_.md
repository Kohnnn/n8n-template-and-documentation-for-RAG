---
url: "https://docs.n8n.io/code/cookbook/builtin/vars/"
title: "vars | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/builtin/vars/#vars)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/builtin/vars.md "Edit this page")

# `vars` [\#](https://docs.n8n.io/code/cookbook/builtin/vars/\#vars "Permanent link")

Feature availability

- Available on Self-hosted Enterprise and Pro and Enterprise Cloud plans.
- You need access to the n8n instance owner account to create variables.

`vars` contains all [Variables](https://docs.n8n.io/code/variables/) for the active environment. It's read-only: you can access variables using `vars`, but must set them using the UI.

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/vars/#__tabbed_1_1)[Python](https://docs.n8n.io/code/cookbook/builtin/vars/#__tabbed_1_2)

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>// Access a variable<br>$vars.<variable-name><br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br># Access a variable<br>_vars.<variable-name><br>``` |

`vars` and `env`

`vars` gives access to user-created variables. It's part of the [Environments](https://docs.n8n.io/source-control-environments/) feature. `env` gives access to the [configuration environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/) for your n8n instance.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top