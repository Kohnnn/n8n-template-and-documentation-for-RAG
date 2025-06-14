---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/"
title: "Timezone and localization environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/#timezone-and-localization-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/timezone-localization.md "Edit this page")

# Timezone and localization environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/\#timezone-and-localization-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `GENERIC_TIMEZONE` | \* | `America/New_York` | The n8n instance timezone. Important for schedule nodes (such as Cron). |
| `N8N_DEFAULT_LOCALE` | String | `en` | A locale identifier, compatible with the [Accept-Language header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language). n8n doesn't support regional identifiers, such as `de-AT`. When running in a locale other than the default, n8n displays UI strings in the selected locale, and falls back to `en` for any untranslated strings. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top