---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/"
title: "Gmail node common issues | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/#gmail-node-common-issues)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md "Edit this page")

# Gmail node common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/\#gmail-node-common-issues "Permanent link")

Here are some common errors and issues with the [Gmail node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/) and steps to resolve or troubleshoot them.

## Remove the n8n attribution from sent messages [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/\#remove-the-n8n-attribution-from-sent-messages "Permanent link")

If you're using the node to [send a message](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/#send-a-message) or [reply to a message](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/#reply-to-a-message), the node appends this statement to the end of the email:

> This email was sent automatically with n8n

To remove this attribution:

1. In the node's **Options** section, select **Add option**.
2. Select **Append n8n attribution**.
3. Turn the toggle off.

Refer to [Send options](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/#send-options) and [Reply options](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/#reply-options) for more information.

## Forbidden - perhaps check your credentials [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/\#forbidden-perhaps-check-your-credentials "Permanent link")

This error displays next to certain dropdowns in the node, like the **Label Names or IDs** dropdown. The full text looks something like this:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"<br>``` |

The error most often displays when you're using a Google Service Account as the credential and the credential doesn't have **Impersonate a User** turned on.

Refer to [Google Service Account: Finish your n8n credential](https://docs.n8n.io/integrations/builtin/credentials/google/service-account/#finish-your-n8n-credential) for more information.

## 401 unauthorized error [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/\#401-unauthorized-error "Permanent link")

The full text of the error looks like this:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}<br>``` |

This error occurs when there's an issue with the credential you're using and its scopes or permissions.

To resolve:

1. For [OAuth2](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/) credentials, make sure you've enabled the Gmail API in **APIs & Services > Library**. Refer to [Google OAuth2 Single Service - Enable APIs](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/#enable-apis) for more information.
2. For [Service Account](https://docs.n8n.io/integrations/builtin/credentials/google/service-account/) credentials:
1. [Enable domain-wide delegation](https://docs.n8n.io/integrations/builtin/credentials/google/service-account/#enable-domain-wide-delegation).
2. Make sure you add the Gmail API as part of the domain-wide delegation configuration.

## Bad request - please check your parameters [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/\#bad-request-please-check-your-parameters "Permanent link")

This error most often occurs if you enter a Message ID, Thread ID, or Label ID that doesn't exist.

Try a **Get** operation with the ID to confirm it exists.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top