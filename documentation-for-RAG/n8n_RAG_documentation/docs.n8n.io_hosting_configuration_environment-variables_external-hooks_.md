---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/external-hooks/"
title: "External hooks environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/external-hooks/#external-hooks-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/external-hooks.md "Edit this page")

# External hooks environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/external-hooks/\#external-hooks-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

You can define external hooks that n8n executes whenever a specific operation runs. Refer to [Backend hooks](https://docs.n8n.io/embed/configuration/#backend-hooks) for examples of available hooks and [Hook files](https://docs.n8n.io/embed/configuration/#backend-hook-files) for information on file formatting.

| Variable | Type | Description |
| --- | --- | --- |
| `EXTERNAL_HOOK_FILES` | String | Files containing backend external hooks. Provide multiple files as a colon-separated list (" `:`"). |
| `EXTERNAL_FRONTEND_HOOKS_URLS` | String | URLs to files containing frontend external hooks. Provide multiple URLs as a colon-separated list (" `:`"). |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top