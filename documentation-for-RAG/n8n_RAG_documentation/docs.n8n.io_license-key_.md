---
url: "https://docs.n8n.io/license-key/"
title: "License key | n8n Docs "
---

[Skip to content](https://docs.n8n.io/license-key/#license-key)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/license-key.md "Edit this page")

# License Key [\#](https://docs.n8n.io/license-key/\#license-key "Permanent link")

To enable certain licensed features, you must first activate your license. You can do this either through the UI or by setting environment variables.

## Add a license key using the UI [\#](https://docs.n8n.io/license-key/\#add-a-license-key-using-the-ui "Permanent link")

In your n8n instance:

1. Log in as **Admin** or **Owner**.
2. Select **Settings** \> **Usage and plan**.
3. Select **Enter activation key**.
4. Paste in your license key.
5. Select **Activate**.

## Add a license key using an environment variables [\#](https://docs.n8n.io/license-key/\#add-a-license-key-using-an-environment-variables "Permanent link")

In your n8n configuration, set `N8N_LICENSE_ACTIVATION_KEY` to your license key. If the instance already has an activated license, this variable will have no effect.

Refer to [Environment variables](https://docs.n8n.io/hosting/configuration/configuration-methods/) to learn more about configuring n8n.

## Allowlist the license server IP addresses [\#](https://docs.n8n.io/license-key/\#allowlist-the-license-server-ip-addresses "Permanent link")

n8n uses Cloudflare to host the license server. As the specific IP addresses can change, you need to allowlist the [full range of Cloudflare IP addresses](https://www.cloudflare.com/ips/) to ensure n8n can always reach the license server.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top