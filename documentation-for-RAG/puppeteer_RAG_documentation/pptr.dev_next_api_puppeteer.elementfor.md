---
url: "https://pptr.dev/next/api/puppeteer.elementfor"
title: "ElementFor type | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementfor#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementfor)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.elementfor\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type ElementFor<
  TagName extends keyof HTMLElementTagNameMap | keyof SVGElementTagNameMap,
> = TagName extends keyof HTMLElementTagNameMap
  ? HTMLElementTagNameMap[TagName]
  : TagName extends keyof SVGElementTagNameMap
    ? SVGElementTagNameMap[TagName]
    : never;

```

- [Signature](https://pptr.dev/next/api/puppeteer.elementfor#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!