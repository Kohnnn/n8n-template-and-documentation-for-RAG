---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/security/"
title: "Security environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/security/#security-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/security.md "Edit this page")

# Security environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/security/\#security-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_BLOCK_ENV_ACCESS_IN_NODE` | Boolean | `false` | Whether to allow users to access environment variables in expressions and the Code node (false) or not (true). |
| `N8N_RESTRICT_FILE_ACCESS_TO` | String |  | Limits access to files in these directories. Provide multiple files as a colon-separated list (" `:`"). |
| `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES` | Boolean | `true` | Set to `true` to block access to all files in the `.n8n` directory and user defined configuration files. |
| `N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW` | Number | 90 | Number of days to consider a workflow abandoned if it's not executed. |
| `N8N_SECURE_COOKIE` | Boolean | `true` | Ensures that cookies are only sent over HTTPS, enhancing security. |
| `N8N_SAMESITE_COOKIE` | Enum string: `strict`, `lax`, `none` | `lax` | Controls cross-site cookie behavior ( [learn more](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)):<br>- `strict`: Sent only for first-party requests.<br>- `lax` (default): Sent with top-level navigation requests.<br>- `none`: Sent in all contexts (requires HTTPS). |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top