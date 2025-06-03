---
url: "https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage"
title: "Coverage.stopCSSCoverage() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage.stopcsscoverage)** (24.9.0).

Version: Next

On this page

Promise that resolves to the array of coverage reports for all stylesheets.

### Signature [​](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Coverage {
  stopCSSCoverage(): Promise<CoverageEntry[]>;
}

```

**Returns:**

Promise< [CoverageEntry](https://pptr.dev/next/api/puppeteer.coverageentry)\[\]>

## Remarks [​](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage\#remarks "Direct link to Remarks")

CSS Coverage doesn't include dynamically injected style tags without sourceURLs.

- [Signature](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!