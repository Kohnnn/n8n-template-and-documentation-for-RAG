---
url: "https://pptr.dev/next/api/puppeteer.browsercontext"
title: "BrowserContext class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext)** (24.9.0).

Version: Next

On this page

[BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) represents individual user contexts within a [browser](https://pptr.dev/next/api/puppeteer.browser).

When a [browser](https://pptr.dev/next/api/puppeteer.browser) is launched, it has at least one default [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). Others can be created using [Browser.createBrowserContext()](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext). Each context has isolated storage (cookies/localStorage/etc.)

[BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) [emits](https://pptr.dev/next/api/puppeteer.eventemitter) various events which are documented in the [BrowserContextEvent](https://pptr.dev/next/api/puppeteer.browsercontextevent) enum.

If a [page](https://pptr.dev/next/api/puppeteer.page) opens another [page](https://pptr.dev/next/api/puppeteer.page), e.g. using `window.open`, the popup will belong to the parent [page's browser context](https://pptr.dev/next/api/puppeteer.page.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browsercontext\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class BrowserContext extends EventEmitter<BrowserContextEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [BrowserContextEvents](https://pptr.dev/next/api/puppeteer.browsercontextevents) >

## Remarks [​](https://pptr.dev/next/api/puppeteer.browsercontext\#remarks "Direct link to Remarks")

In Chrome all non-default contexts are incognito, and [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext) might be incognito if you provide the `--incognito` argument when launching the browser.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `BrowserContext` class.

## Example [​](https://pptr.dev/next/api/puppeteer.browsercontext\#example "Direct link to Example")

Creating a new [browser context](https://pptr.dev/next/api/puppeteer.browsercontext):

```codeBlockLines_RjmQ
// Create a new browser context
const context = await browser.createBrowserContext();
// Create a new page inside context.
const page = await context.newPage();
// ... do stuff with page ...
await page.goto('https://example.com');
// Dispose context once it's no longer needed.
await context.close();

```

## Properties [​](https://pptr.dev/next/api/puppeteer.browsercontext\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| closed | `readonly` | boolean | Whether this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) is closed. |
| id | `readonly` | string \| undefined | Identifier for this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |

## Methods [​](https://pptr.dev/next/api/puppeteer.browsercontext\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [browser()](https://pptr.dev/next/api/puppeteer.browsercontext.browser) |  | Gets the [browser](https://pptr.dev/next/api/puppeteer.browser) associated with this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [clearPermissionOverrides()](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides) |  | Clears all permission overrides for this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [close()](https://pptr.dev/next/api/puppeteer.browsercontext.close) |  | Closes this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) and all associated [pages](https://pptr.dev/next/api/puppeteer.page).<br>**Remarks:**<br>The [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext) cannot be closed. |
| [cookies()](https://pptr.dev/next/api/puppeteer.browsercontext.cookies) |  | Gets all cookies in the browser context. |
| [deleteCookie(cookies)](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie) |  | Removes cookie in the browser context |
| [newPage()](https://pptr.dev/next/api/puppeteer.browsercontext.newpage) |  | Creates a new [page](https://pptr.dev/next/api/puppeteer.page) in this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [overridePermissions(origin, permissions)](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions) |  | Grants this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) the given `permissions` within the given `origin`. |
| [pages()](https://pptr.dev/next/api/puppeteer.browsercontext.pages) |  | Gets a list of all open [pages](https://pptr.dev/next/api/puppeteer.page) inside this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).<br>**Remarks:**<br>Non-visible [pages](https://pptr.dev/next/api/puppeteer.page), such as `"background_page"`, will not be listed here. You can find them using [Target.page()](https://pptr.dev/next/api/puppeteer.target.page). |
| [setCookie(cookies)](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie) |  | Sets a cookie in the browser context. |
| [targets()](https://pptr.dev/next/api/puppeteer.browsercontext.targets) |  | Gets all active [targets](https://pptr.dev/next/api/puppeteer.target) inside this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [waitForTarget(predicate, options)](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget) |  | Waits until a [target](https://pptr.dev/next/api/puppeteer.target) matching the given `predicate` appears and returns it.<br>This will look all open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext). |

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browsercontext#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext#example)
- [Properties](https://pptr.dev/next/api/puppeteer.browsercontext#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.browsercontext#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!