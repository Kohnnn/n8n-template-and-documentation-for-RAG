---
url: "https://pptr.dev/next/api/puppeteer.configuration"
title: "Configuration interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.configuration#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.configuration)** (24.9.0).

Version: Next

On this page

Defines options to configure Puppeteer's behavior during installation and runtime.

See individual properties for more information.

### Signature [​](https://pptr.dev/next/api/puppeteer.configuration\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface Configuration

```

## Properties [​](https://pptr.dev/next/api/puppeteer.configuration\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| "chrome-headless-shell" | `optional` | [ChromeHeadlessShellSettings](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings) |  |  |
| cacheDirectory | `optional` | string | Defines the directory to be used by Puppeteer for caching.<br>Can be overridden by `PUPPETEER_CACHE_DIR`. | `path.join(os.homedir(), '.cache', 'puppeteer')` |
| chrome | `optional` | [ChromeSettings](https://pptr.dev/next/api/puppeteer.chromesettings) |  |  |
| defaultBrowser | `optional` | [SupportedBrowser](https://pptr.dev/next/api/puppeteer.supportedbrowser) | Specifies which browser you'd like Puppeteer to use.<br>Can be overridden by `PUPPETEER_BROWSER`. | `chrome` |
| executablePath | `optional` | string | Specifies an executable path to be used in [puppeteer.launch](https://pptr.dev/next/api/puppeteer.puppeteernode.launch).<br>Can be overridden by `PUPPETEER_EXECUTABLE_PATH`. | **Auto-computed.** |
| experiments | `optional` | [ExperimentsConfiguration](https://pptr.dev/next/api/puppeteer.experimentsconfiguration) | Defines experimental options for Puppeteer. |  |
| firefox | `optional` | [FirefoxSettings](https://pptr.dev/next/api/puppeteer.firefoxsettings) |  |  |
| logLevel | `optional` | 'silent' \| 'error' \| 'warn' | Tells Puppeteer to log at the given level. | `warn` |
| skipDownload | `optional` | boolean | Tells Puppeteer to not download during installation.<br>Can be overridden by `PUPPETEER_SKIP_DOWNLOAD`. |  |
| temporaryDirectory | `optional` | string | Defines the directory to be used by Puppeteer for creating temporary files.<br>Can be overridden by `PUPPETEER_TMP_DIR`. | `os.tmpdir()` |

- [Signature](https://pptr.dev/next/api/puppeteer.configuration#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.configuration#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!