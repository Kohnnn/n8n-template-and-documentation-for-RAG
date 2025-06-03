---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/user-folder/"
title: "Specify user folder path | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/user-folder/#specify-user-folder-path)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/user-folder.md "Edit this page")

# Specify user folder path [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/user-folder/\#specify-user-folder-path "Permanent link")

n8n saves user-specific data like the encryption key, SQLite database file, and
the ID of the tunnel (if used) in the subfolder `.n8n` of the user who started n8n. It's possible to overwrite the user-folder using an environment variable.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_USER_FOLDER=/home/jim/n8n<br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) for more information on this variable.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top