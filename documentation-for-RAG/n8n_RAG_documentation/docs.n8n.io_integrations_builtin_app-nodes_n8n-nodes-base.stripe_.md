---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe/"
title: "Stripe node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe/#stripe-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.stripe.md "Edit this page")

# Stripe node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe/\#stripe-node "Permanent link")

Use the Stripe node to automate work in Stripe, and integrate Stripe with other applications. n8n has built-in support for a wide range of Stripe features, including getting balance, creating charge, and deleting customers.

On this page, you'll find a list of operations the Stripe node supports and links to more resources.

Credentials

Refer to [Stripe credentials](https://docs.n8n.io/integrations/builtin/credentials/stripe/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe/\#operations "Permanent link")

- Balance
  - Get a balance
- Charge
  - Create a charge
  - Get a charge
  - Get all charges
  - Update a charge
- Coupon
  - Create a coupon
  - Get all coupons
- Customer
  - Create a customer
  - Delete a customer
  - Get a customer
  - Get all customers
  - Update a customer
- Customer Card
  - Add a customer card
  - Get a customer card
  - Remove a customer card
- Source
  - Create a source
  - Delete a source
  - Get a source
- Token
  - Create a token

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe/\#templates-and-examples "Permanent link")

**Update HubSpot when a new invoice is registered in Stripe**

by Jonathan

[View template details](https://n8n.io/workflows/1468-update-hubspot-when-a-new-invoice-is-registered-in-stripe/)

**Simplest way to create a Stripe Payment Link**

by Emmanuel Bernard

[View template details](https://n8n.io/workflows/2195-simplest-way-to-create-a-stripe-payment-link/)

**Streamline Your Zoom Meetings with Secure, Automated Stripe Payments**

by Emmanuel Bernard

[View template details](https://n8n.io/workflows/2192-streamline-your-zoom-meetings-with-secure-automated-stripe-payments/)

[Browse Stripe integration templates](https://n8n.io/integrations/stripe/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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