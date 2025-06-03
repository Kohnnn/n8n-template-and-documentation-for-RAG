---
url: "https://docs.browserless.io/bql-schema/operations/mutations/screenshot"
title: "screenshot | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/screenshot#__docusaurus_skipToContent_fallback)

On this page

Screenshots the page or a specific selector

Example:

```codeBlockLines_p187
mutation Screenshot {
  goto(url: "https://example.com") {
    status
  }

  screenshot {
    base64
  }
}

```

```codeBlockLines_p187
screenshot(
  captureBeyondViewport: Boolean
  clip: ScreenshotClip
  fromSurface: Boolean
  fullPage: Boolean
  omitBackground: Boolean
  optimizeForSpeed: Boolean
  quality: Float
  selector: String
  type: ScreenshotType
  timeout: Float
): ScreenshotResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#arguments "Direct link to Arguments")

#### [`screenshot.captureBeyondViewport`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotcapturebeyondviewportboolean- "Direct link to screenshotcapturebeyondviewportboolean-")

Capture the screenshot beyond the viewport.
Default: False if there is no clip. True otherwise

#### [`screenshot.clip`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`ScreenshotClip`](https://docs.browserless.io/bql-schema/types/inputs/screenshot-clip) input [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotclipscreenshotclip- "Direct link to screenshotclipscreenshotclip-")

Specifies the region of the page/element to clip

#### [`screenshot.fromSurface`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotfromsurfaceboolean- "Direct link to screenshotfromsurfaceboolean-")

Capture the screenshot from the surface, rather than the view.
Default: True

#### [`screenshot.fullPage`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotfullpageboolean- "Direct link to screenshotfullpageboolean-")

When True, takes a screenshot of the full page.
Default: False

#### [`screenshot.omitBackground`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotomitbackgroundboolean- "Direct link to screenshotomitbackgroundboolean-")

Hides default white background and allows capturing screenshots with transparency.
Default: False

#### [`screenshot.optimizeForSpeed`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotoptimizeforspeedboolean- "Direct link to screenshotoptimizeforspeedboolean-")

Optimize image encoding for speed, not for resulting size.
Default: False

#### [`screenshot.quality`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotqualityfloat- "Direct link to screenshotqualityfloat-")

Quality of the image, between 0-100. Not applicable to png images.

#### [`screenshot.selector`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotselectorstring- "Direct link to screenshotselectorstring-")

The CSS selector of the element on the page you want to screenshot

#### [`screenshot.type`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`ScreenshotType`](https://docs.browserless.io/bql-schema/types/enums/screenshot-type) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshottypescreenshottype- "Direct link to screenshottypescreenshottype-")

The final format of the screenshot

#### [`screenshot.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshottimeoutfloat- "Direct link to screenshottimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the screenshot to be taken. Default timeout is 30 seconds, or 30000.

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#type "Direct link to Type")

#### [`ScreenshotResponse`](https://docs.browserless.io/bql-schema/types/objects/screenshot-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/screenshot\#screenshotresponse- "Direct link to screenshotresponse-")

The response returned after generating a Screenshot

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/screenshot#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/screenshot#type)