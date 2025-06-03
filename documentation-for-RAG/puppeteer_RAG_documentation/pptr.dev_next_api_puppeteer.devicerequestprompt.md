---
url: "https://pptr.dev/next/api/puppeteer.devicerequestprompt"
title: "DeviceRequestPrompt class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.devicerequestprompt#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.devicerequestprompt)** (24.9.0).

Version: Next

On this page

Device request prompts let you respond to the page requesting for a device through an API like WebBluetooth.

### Signature [​](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class DeviceRequestPrompt

```

## Remarks [​](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#remarks "Direct link to Remarks")

`DeviceRequestPrompt` instances are returned via the [Page.waitForDevicePrompt()](https://pptr.dev/next/api/puppeteer.page.waitfordeviceprompt) method.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `DeviceRequestPrompt` class.

## Example [​](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#example "Direct link to Example")

```codeBlockLines_RjmQ
const [devicePrompt] = Promise.all([\
  page.waitForDevicePrompt(),\
  page.click('#connect-bluetooth'),\
]);
await devicePrompt.select(
  await devicePrompt.waitForDevice(({name}) => name.includes('My Device')),
);

```

## Properties [​](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| devices |  | [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice)\[\] | Current list of selectable devices. |

## Methods [​](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [cancel()](https://pptr.dev/next/api/puppeteer.devicerequestprompt.cancel) |  | Cancel the prompt. |
| [select(device)](https://pptr.dev/next/api/puppeteer.devicerequestprompt.select) |  | Select a device in the prompt's list. |
| [waitForDevice(filter, options)](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice) |  | Resolve to the first device in the prompt matching a filter. |

- [Signature](https://pptr.dev/next/api/puppeteer.devicerequestprompt#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.devicerequestprompt#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.devicerequestprompt#example)
- [Properties](https://pptr.dev/next/api/puppeteer.devicerequestprompt#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.devicerequestprompt#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!