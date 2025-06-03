---
url: "https://pptr.dev/next/api/puppeteer.coverage.startjscoverage"
title: "Coverage.startJSCoverage() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage.startjscoverage)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Coverage {
  startJSCoverage(options?: JSCoverageOptions): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [JSCoverageOptions](https://pptr.dev/next/api/puppeteer.jscoverageoptions) | _(Optional)_ Set of configurable options for coverage defaults to `resetOnNavigation : true, reportAnonymousScripts : false,` `includeRawScriptCoverage : false, useBlockCoverage : true` |

**Returns:**

Promise<void>

Promise that resolves when coverage is started.

## Remarks [​](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage\#remarks "Direct link to Remarks")

Anonymous scripts are ones that don't have an associated url. These are scripts that are dynamically created on the page using `eval` or `new Function`. If `reportAnonymousScripts` is set to `true`, anonymous scripts URL will start with `debugger://VM` (unless a magic //# sourceURL comment is present, in which case that will the be URL).

- [Signature](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!