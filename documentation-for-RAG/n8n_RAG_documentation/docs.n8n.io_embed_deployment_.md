---
url: "https://docs.n8n.io/embed/deployment/"
title: "Deployment | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/embed/deployment/#deployment)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/embed/deployment.md "Edit this page")

# Deployment [\#](https://docs.n8n.io/embed/deployment/\#deployment "Permanent link")

Feature availability

Embed requires an embed license. For more information about when to use Embed, as well as costs and licensing processes, refer to [Embed](https://n8n.io/embed/) on the n8n website.

See the [hosting documentation](https://docs.n8n.io/reference/server-setup.html) for detailed setup options.

## User data [\#](https://docs.n8n.io/embed/deployment/\#user-data "Permanent link")

n8n recommends that you follow the same or similar practices used internally for n8n Cloud: Save user data using [Rook](https://rook.io/) and, if an n8n server goes down, a new instance starts on another machine using the same data.

Due to this, you don't need to use backups except in case of a catastrophic failure, or when a user wants to reactivate their account within your prescribed retention period (two weeks for n8n Cloud).

## Backups [\#](https://docs.n8n.io/embed/deployment/\#backups "Permanent link")

n8n recommends creating nightly backups by attaching another container, and copying all data to this second container. In this manner, RAM usage is negligible, and so doesn't impact the amount of users you can place on the server.

## Restarting [\#](https://docs.n8n.io/embed/deployment/\#restarting "Permanent link")

If your instance is down or restarting, missed executions (for example, Cron or Webhook nodes) during this time aren't recoverable. If it's important for you to maintain 100% uptime, you need to build another proxy in front of it which caches the data.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top