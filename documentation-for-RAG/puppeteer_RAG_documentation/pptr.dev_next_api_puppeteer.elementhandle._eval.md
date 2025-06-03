---
url: "https://pptr.dev/next/api/puppeteer.elementhandle._eval"
title: "ElementHandle.$eval() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle._eval#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle._eval)** (24.9.0).

Version: Next

On this page

Runs the given function on the first element matching the given selector in the current element.

If the given function returns a promise, then this method will wait till the promise resolves.

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle._eval\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  $eval<
    Selector extends string,
    Params extends unknown[],
    Func extends EvaluateFuncWith<NodeFor<Selector>, Params> = EvaluateFuncWith<
      NodeFor<Selector>,
      Params
    >,
  >(
    selector: Selector,
    pageFunction: Func | string,
    ...args: Params
  ): Promise<Awaited<ReturnType<Func>>>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.elementhandle._eval\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| selector | Selector | [selector](https://pptr.dev/guides/page-interactions#selectors) to query the page for. [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) can be passed as-is and a [Puppeteer-specific selector syntax](https://pptr.dev/guides/page-interactions#non-css-selectors) allows querying by [text](https://pptr.dev/guides/page-interactions#text-selectors--p-text), [a11y role and name](https://pptr.dev/guides/page-interactions#aria-selectors--p-aria), and [xpath](https://pptr.dev/guides/page-interactions#xpath-selectors--p-xpath) and [combining these queries across shadow roots](https://pptr.dev/guides/page-interactions#querying-elements-in-shadow-dom). Alternatively, you can specify the selector type using a [prefix](https://pptr.dev/guides/page-interactions#prefixed-selector-syntax). |
| pageFunction | Func \| string | The function to be evaluated in this element's page's context. The first element matching the selector will be passed in as the first argument. |
| args | Params | Additional arguments to pass to `pageFunction`. |

**Returns:**

Promise<Awaited<ReturnType<Func>>>

A promise to the result of the function.

## Example [​](https://pptr.dev/next/api/puppeteer.elementhandle._eval\#example "Direct link to Example")

```codeBlockLines_RjmQ
const tweetHandle = await page.$('.tweet');
expect(await tweetHandle.$eval('.like', node => node.innerText)).toBe('100');
expect(await tweetHandle.$eval('.retweets', node => node.innerText)).toBe('10');

```

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle._eval#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle._eval#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.elementhandle._eval#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!