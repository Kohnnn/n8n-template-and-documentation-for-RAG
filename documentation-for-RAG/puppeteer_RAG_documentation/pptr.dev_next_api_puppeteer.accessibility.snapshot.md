---
url: "https://pptr.dev/next/api/puppeteer.accessibility.snapshot"
title: "Accessibility.snapshot() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.accessibility.snapshot)** (24.9.0).

Version: Next

On this page

Captures the current state of the accessibility tree. The returned object represents the root accessible node of the page.

### Signature [​](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Accessibility {
  snapshot(options?: SnapshotOptions): Promise<SerializedAXNode | null>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [SnapshotOptions](https://pptr.dev/next/api/puppeteer.snapshotoptions) | _(Optional)_ |

**Returns:**

Promise< [SerializedAXNode](https://pptr.dev/next/api/puppeteer.serializedaxnode) \| null>

An AXNode object representing the snapshot.

## Remarks [​](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#remarks "Direct link to Remarks")

**NOTE** The Chrome accessibility tree contains nodes that go unused on most platforms and by most screen readers. Puppeteer will discard them as well for an easier to process tree, unless `interestingOnly` is set to `false`.

## Example 1 [​](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#example-1 "Direct link to Example 1")

An example of dumping the entire accessibility tree:

```codeBlockLines_RjmQ
const snapshot = await page.accessibility.snapshot();
console.log(snapshot);

```

## Example 2 [​](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#example-2 "Direct link to Example 2")

An example of logging the focused node's name:

```codeBlockLines_RjmQ
const snapshot = await page.accessibility.snapshot();
const node = findFocusedNode(snapshot);
console.log(node && node.name);

function findFocusedNode(node) {
  if (node.focused) return node;
  for (const child of node.children || []) {
    const foundNode = findFocusedNode(child);
    return foundNode;
  }
  return null;
}

```

- [Signature](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#remarks)
- [Example 1](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#example-1)
- [Example 2](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#example-2)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!