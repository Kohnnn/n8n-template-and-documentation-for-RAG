---
url: "https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage"
title: "Coverage.stopJSCoverage() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage.stopjscoverage)** (24.9.0).

Version: Next

On this page

Promise that resolves to the array of coverage reports for all scripts.

### Signature [​](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Coverage {
  stopJSCoverage(): Promise<JSCoverageEntry[]>;
}

```

**Returns:**

Promise< [JSCoverageEntry](https://pptr.dev/next/api/puppeteer.jscoverageentry)\[\]>

## Remarks [​](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage\#remarks "Direct link to Remarks")

JavaScript Coverage doesn't include anonymous scripts by default. However, scripts with sourceURLs are reported.

- [Signature](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!