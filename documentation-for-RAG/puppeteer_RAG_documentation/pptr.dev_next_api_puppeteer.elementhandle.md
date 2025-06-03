---
url: "https://pptr.dev/next/api/puppeteer.elementhandle"
title: "ElementHandle class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle)** (24.9.0).

Version: Next

On this page

ElementHandle represents an in-page DOM element.

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class ElementHandle<ElementType extends Node = Element> extends JSHandle<ElementType>

```

**Extends:** [JSHandle](https://pptr.dev/next/api/puppeteer.jshandle) <ElementType>

## Remarks [​](https://pptr.dev/next/api/puppeteer.elementhandle\#remarks "Direct link to Remarks")

ElementHandles can be created with the [Page.$()](https://pptr.dev/next/api/puppeteer.page._) method.

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  const hrefElement = await page.$('a');
  await hrefElement.click();
  // ...
})();

```

ElementHandle prevents the DOM element from being garbage-collected unless the handle is [disposed](https://pptr.dev/next/api/puppeteer.jshandle.dispose). ElementHandles are auto-disposed when their origin frame gets navigated.

ElementHandle instances can be used as arguments in [Page.$eval()](https://pptr.dev/next/api/puppeteer.page._eval) and [Page.evaluate()](https://pptr.dev/next/api/puppeteer.page.evaluate) methods.

If you're using TypeScript, ElementHandle takes a generic argument that denotes the type of element the handle is holding within. For example, if you have a handle to a `<select>` element, you can type it as `ElementHandle<HTMLSelectElement>` and you get some nicer type checks.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ElementHandle` class.

## Properties [​](https://pptr.dev/next/api/puppeteer.elementhandle\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| frame | `readonly` | [Frame](https://pptr.dev/next/api/puppeteer.frame) | Frame corresponding to the current handle. |

## Methods [​](https://pptr.dev/next/api/puppeteer.elementhandle\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [$(selector)](https://pptr.dev/next/api/puppeteer.elementhandle._) |  | Queries the current element for an element matching the given selector. |
| [$$(selector, options)](https://pptr.dev/next/api/puppeteer.elementhandle.__) |  | Queries the current element for all elements matching the given selector. |
| [$$eval(selector, pageFunction, args)](https://pptr.dev/next/api/puppeteer.elementhandle.__eval) |  | Runs the given function on an array of elements matching the given selector in the current element.<br>If the given function returns a promise, then this method will wait till the promise resolves. |
| [$eval(selector, pageFunction, args)](https://pptr.dev/next/api/puppeteer.elementhandle._eval) |  | Runs the given function on the first element matching the given selector in the current element.<br>If the given function returns a promise, then this method will wait till the promise resolves. |
| [autofill(data)](https://pptr.dev/next/api/puppeteer.elementhandle.autofill) |  | If the element is a form input, you can use [ElementHandle.autofill()](https://pptr.dev/next/api/puppeteer.elementhandle.autofill) to test if the form is compatible with the browser's autofill implementation. Throws an error if the form cannot be autofilled.<br>**Remarks:**<br>Currently, Puppeteer supports auto-filling credit card information only and in Chrome in the new headless and headful modes only.<br>```codeBlockLines_RjmQ<br>// Select an input on the credit card form.<br>const name = await page.waitForSelector('form #name');<br>// Trigger autofill with the desired data.<br>await name.autofill({<br>  creditCard: {<br>    number: '4444444444444444',<br>    name: 'John Smith',<br>    expiryMonth: '01',<br>    expiryYear: '2030',<br>    cvc: '123',<br>  },<br>});<br>``` |
| [backendNodeId()](https://pptr.dev/next/api/puppeteer.elementhandle.backendnodeid) |  | When connected using Chrome DevTools Protocol, it returns a DOM.BackendNodeId for the element. |
| [boundingBox()](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox) |  | This method returns the bounding box of the element (relative to the main frame), or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`). |
| [boxModel()](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel) |  | This method returns boxes of the element, or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`).<br>**Remarks:**<br>Boxes are represented as an array of points; Each Point is an object `{x, y}`. Box points are sorted clock-wise. |
| [click(this, options)](https://pptr.dev/next/api/puppeteer.elementhandle.click) |  | This method scrolls element into view if needed, and then uses [Page.mouse](https://pptr.dev/next/api/puppeteer.page#mouse) to click in the center of the element. If the element is detached from DOM, the method throws an error. |
| [clickablePoint(offset)](https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint) |  | Returns the middle point within an element unless a specific offset is provided. |
| [contentFrame(this)](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe) |  | Resolves the frame associated with the element, if any. Always exists for HTMLIFrameElements. |
| [contentFrame()](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe) |  |  |
| [drag(this, target)](https://pptr.dev/next/api/puppeteer.elementhandle.drag) |  | Drags an element over the given element or point. |
| [dragAndDrop(this, target, options)](https://pptr.dev/next/api/puppeteer.elementhandle.draganddrop) | `deprecated` | **Deprecated:**<br>Use `ElementHandle.drop` instead. |
| [dragEnter(this, data)](https://pptr.dev/next/api/puppeteer.elementhandle.dragenter) | `deprecated` | **Deprecated:**<br>Do not use. `dragenter` will automatically be performed during dragging. |
| [dragOver(this, data)](https://pptr.dev/next/api/puppeteer.elementhandle.dragover) | `deprecated` | **Deprecated:**<br>Do not use. `dragover` will automatically be performed during dragging. |
| [drop(this, element)](https://pptr.dev/next/api/puppeteer.elementhandle.drop) |  | Drops the given element onto the current one. |
| [drop(this, data)](https://pptr.dev/next/api/puppeteer.elementhandle.drop) | `deprecated` | **Deprecated:**<br>No longer supported. |
| [focus()](https://pptr.dev/next/api/puppeteer.elementhandle.focus) |  | Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element. |
| [hover(this)](https://pptr.dev/next/api/puppeteer.elementhandle.hover) |  | This method scrolls element into view if needed, and then uses [Page.mouse](https://pptr.dev/next/api/puppeteer.page#mouse) to hover over the center of the element. If the element is detached from DOM, the method throws an error. |
| [isHidden()](https://pptr.dev/next/api/puppeteer.elementhandle.ishidden) |  | An element is considered to be hidden if at least one of the following is true:<br>- the element has no [computed styles](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle).<br>  <br>- the element has an empty [bounding client rect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).<br>  <br>- the element's [visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility) is `hidden` or `collapse`. |
| [isIntersectingViewport(this, options)](https://pptr.dev/next/api/puppeteer.elementhandle.isintersectingviewport) |  | Resolves to true if the element is visible in the current viewport. If an element is an SVG, we check if the svg owner element is in the viewport instead. See [https://crbug.com/963246](https://crbug.com/963246). |
| [isVisible()](https://pptr.dev/next/api/puppeteer.elementhandle.isvisible) |  | An element is considered to be visible if all of the following is true:<br>- the element has [computed styles](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle).<br>  <br>- the element has a non-empty [bounding client rect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).<br>  <br>- the element's [visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility) is not `hidden` or `collapse`. |
| [press(key, options)](https://pptr.dev/next/api/puppeteer.elementhandle.press) |  | Focuses the element, and then uses [Keyboard.down()](https://pptr.dev/next/api/puppeteer.keyboard.down) and [Keyboard.up()](https://pptr.dev/next/api/puppeteer.keyboard.up).<br>**Remarks:**<br>If `key` is a single character and no modifier keys besides `Shift` are being held down, a `keypress`/ `input` event will also be generated. The `text` option can be specified to force an input event to be generated.<br>**NOTE** Modifier keys DO affect `elementHandle.press`. Holding down `Shift` will type the text in upper case. |
| [screenshot(options)](https://pptr.dev/next/api/puppeteer.elementhandle.screenshot) |  | This method scrolls element into view if needed, and then uses [Page.screenshot()](https://pptr.dev/next/api/puppeteer.page.screenshot) to take a screenshot of the element. If the element is detached from DOM, the method throws an error. |
| [screenshot(options)](https://pptr.dev/next/api/puppeteer.elementhandle.screenshot) |  |  |
| [scrollIntoView(this)](https://pptr.dev/next/api/puppeteer.elementhandle.scrollintoview) |  | Scrolls the element into view using either the automation protocol client or by calling element.scrollIntoView. |
| [select(values)](https://pptr.dev/next/api/puppeteer.elementhandle.select) |  | Triggers a `change` and `input` event once all the provided options have been selected. If there's no `<select>` element matching `selector`, the method throws an error. |
| [tap(this)](https://pptr.dev/next/api/puppeteer.elementhandle.tap) |  | This method scrolls element into view if needed, and then uses [Touchscreen.tap()](https://pptr.dev/next/api/puppeteer.touchscreen.tap) to tap in the center of the element. If the element is detached from DOM, the method throws an error. |
| [toElement(tagName)](https://pptr.dev/next/api/puppeteer.elementhandle.toelement) |  | Converts the current handle to the given element type. |
| [touchEnd(this)](https://pptr.dev/next/api/puppeteer.elementhandle.touchend) |  |  |
| [touchMove(this, touch)](https://pptr.dev/next/api/puppeteer.elementhandle.touchmove) |  | This method scrolls the element into view if needed, and then moves the touch to the center of the element. |
| [touchStart(this)](https://pptr.dev/next/api/puppeteer.elementhandle.touchstart) |  | This method scrolls the element into view if needed, and then starts a touch in the center of the element. |
| [type(text, options)](https://pptr.dev/next/api/puppeteer.elementhandle.type) |  | Focuses the element, and then sends a `keydown`, `keypress`/ `input`, and `keyup` event for each character in the text.<br>To press a special key, like `Control` or `ArrowDown`, use [ElementHandle.press()](https://pptr.dev/next/api/puppeteer.elementhandle.press). |
| [uploadFile(this, paths)](https://pptr.dev/next/api/puppeteer.elementhandle.uploadfile) |  | Sets the value of an [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) to the given file paths.<br>**Remarks:**<br>This will not validate whether the file paths exists. Also, if a path is relative, then it is resolved against the [current working directory](https://nodejs.org/api/process.html#process_process_cwd). For locals script connecting to remote chrome environments, paths must be absolute. |
| [waitForSelector(selector, options)](https://pptr.dev/next/api/puppeteer.elementhandle.waitforselector) |  | Wait for an element matching the given selector to appear in the current element.<br>Unlike [Frame.waitForSelector()](https://pptr.dev/next/api/puppeteer.frame.waitforselector), this method does not work across navigations or if the element is detached from DOM. |

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.elementhandle#remarks)
- [Properties](https://pptr.dev/next/api/puppeteer.elementhandle#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.elementhandle#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!