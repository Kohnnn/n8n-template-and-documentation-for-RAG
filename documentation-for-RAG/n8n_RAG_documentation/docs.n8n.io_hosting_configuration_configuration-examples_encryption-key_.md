---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/encryption-key/"
title: "Set a custom encryption key | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/encryption-key/#set-a-custom-encryption-key)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/encryption-key.md "Edit this page")

# Set a custom encryption key [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/encryption-key/\#set-a-custom-encryption-key "Permanent link")

n8n creates a random encryption key automatically on the first launch and saves
it in the `~/.n8n` folder. n8n uses that key to encrypt the credentials before
they get saved to the database. If the key isn't yet in the settings file,
you can set it using an environment variable, so that n8n
uses your custom key instead of generating a new one.

In [queue mode](https://docs.n8n.io/hosting/scaling/queue-mode/), you must specify the encryption key environment variable for all workers.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export N8N_ENCRYPTION_KEY=<SOME RANDOM STRING><br>``` |

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) for more information on this variable.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top