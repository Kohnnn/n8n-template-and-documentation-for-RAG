---
url: "https://docs.browserless.io/baas/v1/libraries/selenium-python"
title: "Python (Selenium) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/selenium-python#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

You can use your existing python infrastructure today with browserless by using the selenium webdriver library.

As with most selenium libraries, you'll need to install the webdriver dependency, and set browserless as your remote webdriver. You'll also use `set_capability` to specify your browserless.io token when making requests to the hosted service.

Below there are some small examples of getting started:

## Selenium 4 [​](https://docs.browserless.io/baas/v1/libraries/selenium-python\#selenium-4 "Direct link to Selenium 4")

```codeBlockLines_p187
# Selenium 4
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserless:token', 'YOUR-API-TOKEN')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor='https://chrome.browserless.io/webdriver',
    options=chrome_options
)

driver.get("https://www.example.com")
print(driver.title)
driver.quit()

```

## Selenium 3 [​](https://docs.browserless.io/baas/v1/libraries/selenium-python\#selenium-3 "Direct link to Selenium 3")

```codeBlockLines_p187
# Selenium 3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserless:token', 'YOUR-API-TOKEN')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
  command_executor='https://chrome.browserless.io/webdriver',
  desired_capabilities=chrome_options.to_capabilities()
)

driver.get("https://www.example.com")
print(driver.title)
driver.quit()

```

This will simply navigate to the Example website and print the title, however it'll give you a great starting place for using Java Selenium alongside browserless.

Be sure to [let us know if you have questions or issues](https://www.browserless.io/contact).

- [Selenium 4](https://docs.browserless.io/baas/v1/libraries/selenium-python#selenium-4)
- [Selenium 3](https://docs.browserless.io/baas/v1/libraries/selenium-python#selenium-3)