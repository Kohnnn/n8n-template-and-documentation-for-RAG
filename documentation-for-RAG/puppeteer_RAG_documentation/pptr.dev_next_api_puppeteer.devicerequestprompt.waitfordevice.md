---
url: "https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice"
title: "DeviceRequestPrompt.waitForDevice() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.devicerequestprompt.waitfordevice)** (24.9.0).

Version: Next

On this page

Resolve to the first device in the prompt matching a filter.

### Signature [​](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class DeviceRequestPrompt {
  waitForDevice(
    filter: (device: DeviceRequestPromptDevice) => boolean,
    options?: WaitTimeoutOptions,
  ): Promise<DeviceRequestPromptDevice>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| filter | (device: [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice)) =\> boolean |  |
| options | [WaitTimeoutOptions](https://pptr.dev/next/api/puppeteer.waittimeoutoptions) | _(Optional)_ |

**Returns:**

Promise< [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice) >

- [Signature](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!