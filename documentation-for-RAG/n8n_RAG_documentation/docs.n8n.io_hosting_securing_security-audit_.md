---
url: "https://docs.n8n.io/hosting/securing/security-audit/"
title: "Security audit | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/securing/security-audit/#security-audit)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/securing/security-audit.md "Edit this page")

# Security audit [\#](https://docs.n8n.io/hosting/securing/security-audit/\#security-audit "Permanent link")

You can run a security audit on your n8n instance, to detect common security issues.

## Run an audit [\#](https://docs.n8n.io/hosting/securing/security-audit/\#run-an-audit "Permanent link")

You can run an audit using the CLI, the public API, or the n8n node.

### CLI [\#](https://docs.n8n.io/hosting/securing/security-audit/\#cli "Permanent link")

Run `n8n audit`.

### API [\#](https://docs.n8n.io/hosting/securing/security-audit/\#api "Permanent link")

Make a `POST` call to the `/audit` endpoint. You must authenticate as the instance owner.

### n8n node [\#](https://docs.n8n.io/hosting/securing/security-audit/\#n8n-node "Permanent link")

Add the [n8n node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n/) to your workflow. Select **Resource** \> **Audit** and **Operation** \> **Generate**.

## Report contents [\#](https://docs.n8n.io/hosting/securing/security-audit/\#report-contents "Permanent link")

The audit generates five risk reports:

### Credentials [\#](https://docs.n8n.io/hosting/securing/security-audit/\#credentials "Permanent link")

This report shows:

- Credentials not used in a workflow.
- Credentials not used in an active workflow.
- Credentials not use in a recently active workflow.

### Database [\#](https://docs.n8n.io/hosting/securing/security-audit/\#database "Permanent link")

This report shows:

- Expressions used in **Execute Query** fields in SQL nodes.
- Expressions used in **Query Parameters** fields in SQL nodes.
- Unused **Query Parameters** fields in SQL nodes.

### File system [\#](https://docs.n8n.io/hosting/securing/security-audit/\#file-system "Permanent link")

This report lists nodes that interact with the file system.

### Nodes [\#](https://docs.n8n.io/hosting/securing/security-audit/\#nodes "Permanent link")

This report shows:

- Official risky nodes. These are n8n built in nodes. You can use them to fetch and run any code on the host system, which exposes the instance to exploits. You can view the list in [n8n code \| Audit constants](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/security-audit/constants.ts#L51), under `OFFICIAL_RISKY_NODE_TYPES`.
- Community nodes.
- Custom nodes.

### Instance [\#](https://docs.n8n.io/hosting/securing/security-audit/\#instance "Permanent link")

This report shows:

- Unprotected webhooks in the instance.
- Missing security settings
- If your instance is outdated.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top