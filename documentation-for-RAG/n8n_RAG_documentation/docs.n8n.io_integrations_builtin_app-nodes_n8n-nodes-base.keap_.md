---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap/"
title: "Keap node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap/#keap-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.keap.md "Edit this page")

# Keap node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap/\#keap-node "Permanent link")

Use the Keap node to automate work in Keap, and integrate Keap with other applications. n8n has built-in support for a wide range of Keap features, including creating, updating, deleting, and getting companies, products, ecommerce orders, emails, and files.

On this page, you'll find a list of operations the Keap node supports and links to more resources.

Credentials

Refer to [Keap credentials](https://docs.n8n.io/integrations/builtin/credentials/keap/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap/\#operations "Permanent link")

- Company
  - Create a company
  - Retrieve all companies
- Contact
  - Create/update a contact
  - Delete an contact
  - Retrieve an contact
  - Retrieve all contacts
- Contact Note
  - Create a note
  - Delete a note
  - Get a notes
  - Retrieve all notes
  - Update a note
- Contact Tag
  - Add a list of tags to a contact
  - Delete a contact's tag
  - Retrieve all contact's tags
- Ecommerce Order
  - Create an ecommerce order
  - Get an ecommerce order
  - Delete an ecommerce order
  - Retrieve all ecommerce orders
- Ecommerce Product
  - Create an ecommerce product
  - Delete an ecommerce product
  - Get an ecommerce product
  - Retrieve all ecommerce product
- Email
  - Create a record of an email sent to a contact
  - Retrieve all sent emails
  - Send Email
- File
  - Delete a file
  - Retrieve all files
  - Upload a file

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap/\#templates-and-examples "Permanent link")

**Verify mailing address deliverability of contacts in Keap/Infusionsoft Using Lob**

by Belmont Digital

[View template details](https://n8n.io/workflows/2251-verify-mailing-address-deliverability-of-contacts-in-keapinfusionsoft-using-lob/)

**Get all contacts from Keap**

by amudhan

[View template details](https://n8n.io/workflows/553-get-all-contacts-from-keap/)

**Receive updates when a new contact is added in Keap**

by amudhan

[View template details](https://n8n.io/workflows/554-receive-updates-when-a-new-contact-is-added-in-keap/)

[Browse Keap integration templates](https://n8n.io/integrations/keap/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top