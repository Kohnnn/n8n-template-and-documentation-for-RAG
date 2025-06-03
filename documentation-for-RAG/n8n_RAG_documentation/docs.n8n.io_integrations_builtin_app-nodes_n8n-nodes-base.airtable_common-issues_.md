---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues/"
title: "Airtable node common issues | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues/#airtable-node-common-issues)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md "Edit this page")

# Airtable node common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues/\#airtable-node-common-issues "Permanent link")

Here are some common errors and issues with the [Airtable node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/) and steps to resolve or troubleshoot them.

## Forbidden - perhaps check your credentials [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues/\#forbidden-perhaps-check-your-credentials "Permanent link")

This error displays when trying to perform actions not permitted by your current level of access. The full text looks something like this:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"<br>``` |

The error most often displays when the credential you're using doesn't have the scopes it requires on the resources you're attempting to manage.

Refer to the [Airtable credentials](https://docs.n8n.io/integrations/builtin/credentials/airtable/) and [Airtables scopes documentation](https://airtable.com/developers/web/api/scopes) for more information.

## Service is receiving too many requests from you [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues/\#service-is-receiving-too-many-requests-from-you "Permanent link")

Airtable has a hard API limit on the number of requests generated using personal access tokens.

If you send more than five requests per second per base, you will receive a 429 error, indicating that you have sent too many requests. You will have to wait 30 seconds before resuming requests. This same limit applies for sending more than 50 requests across all bases per access token.

You can find out more in the [Airtable's rate limits documentation](https://airtable.com/developers/web/api/rate-limits). If you find yourself running into rate limits with the Airtable node, consider implementing one of the suggestions on the [handling rate limits](https://docs.n8n.io/integrations/builtin/rate-limits/) page.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top