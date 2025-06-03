---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/time-zone/"
title: "Set the self-hosted instance timezone | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/time-zone/#set-the-self-hosted-instance-timezone)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/time-zone.md "Edit this page")

# Set the self-hosted instance timezone [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/time-zone/\#set-the-self-hosted-instance-timezone "Permanent link")

The default timezone is America/New\_York. For instance, the Schedule node uses it to know at what time the workflow should start. To set a different default timezone, set `GENERIC_TIMEZONE` to the appropriate value. For example, if you want to set the timezone to Berlin (Germany):

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export GENERIC_TIMEZONE=Europe/Berlin<br>``` |

You can find the name of your timezone [here](https://momentjs.com/timezone/).

Refer to [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/) for more information on this variable.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top