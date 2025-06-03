---
url: "https://docs.browserless.io/browserql/scraping/performing-searches"
title: "Performing searches | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/scraping/performing-searches#__docusaurus_skipToContent_fallback)

If you need to interact with popups or search bars then use the `click` and `type` requests. They use level 4 CSS for the selectors while handling wait conditions automatically.

```codeBlockLines_p187
mutation searching_booking_com{
  goto(url: "https://www.booking.com", waitUntil: networkIdle) {
    status
  }

  closeModal: click(
    selector: "button[aria-label='Dismiss sign-in info.']",
    visible: true,
    timeout: 5000
  ) {
    time
  }

  type(
    text: "New York",
    selector: "input[name='ss'][placeholder='Where are you going?']",
  ) {
    selector
  }

  submitSearch: click(
    selector: "button[type='submit'][class*='a83ed08757']",
    visible: true
  ) {
    selector
    time
  }
}

```