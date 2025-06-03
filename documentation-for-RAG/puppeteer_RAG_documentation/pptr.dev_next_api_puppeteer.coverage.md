---
url: "https://pptr.dev/next/api/puppeteer.coverage"
title: "Coverage class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage)** (24.9.0).

Version: Next

On this page

The Coverage class provides methods to gather information about parts of JavaScript and CSS that were used by the page.

### Signature [​](https://pptr.dev/next/api/puppeteer.coverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class Coverage

```

## Remarks [​](https://pptr.dev/next/api/puppeteer.coverage\#remarks "Direct link to Remarks")

To output coverage in a form consumable by [Istanbul](https://github.com/istanbuljs), see [puppeteer-to-istanbul](https://github.com/istanbuljs/puppeteer-to-istanbul).

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Coverage` class.

## Example [​](https://pptr.dev/next/api/puppeteer.coverage\#example "Direct link to Example")

An example of using JavaScript and CSS coverage to get percentage of initially executed code:

```codeBlockLines_RjmQ
// Enable both JavaScript and CSS coverage
await Promise.all([\
  page.coverage.startJSCoverage(),\
  page.coverage.startCSSCoverage(),\
]);
// Navigate to page
await page.goto('https://example.com');
// Disable both JavaScript and CSS coverage
const [jsCoverage, cssCoverage] = await Promise.all([\
  page.coverage.stopJSCoverage(),\
  page.coverage.stopCSSCoverage(),\
]);
let totalBytes = 0;
let usedBytes = 0;
const coverage = [...jsCoverage, ...cssCoverage];
for (const entry of coverage) {
  totalBytes += entry.text.length;
  for (const range of entry.ranges) usedBytes += range.end - range.start - 1;
}
console.log(`Bytes used: ${(usedBytes / totalBytes) * 100}%`);

```

## Methods [​](https://pptr.dev/next/api/puppeteer.coverage\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [startCSSCoverage(options)](https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage) |  |  |
| [startJSCoverage(options)](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage) |  | **Remarks:**<br>Anonymous scripts are ones that don't have an associated url. These are scripts that are dynamically created on the page using `eval` or `new Function`. If `reportAnonymousScripts` is set to `true`, anonymous scripts URL will start with `debugger://VM` (unless a magic //# sourceURL comment is present, in which case that will the be URL). |
| [stopCSSCoverage()](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage) |  | Promise that resolves to the array of coverage reports for all stylesheets.<br>**Remarks:**<br>CSS Coverage doesn't include dynamically injected style tags without sourceURLs. |
| [stopJSCoverage()](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage) |  | Promise that resolves to the array of coverage reports for all scripts.<br>**Remarks:**<br>JavaScript Coverage doesn't include anonymous scripts by default. However, scripts with sourceURLs are reported. |

- [Signature](https://pptr.dev/next/api/puppeteer.coverage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.coverage#example)
- [Methods](https://pptr.dev/next/api/puppeteer.coverage#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!