---
url: "https://docs.browserless.io/baas/v1/libraries/java"
title: "Java (Selenium) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/java#__docusaurus_skipToContent_fallback)

Version: v1

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

Browserless now supports the Selenium library for Java, provided by OpenQA! Similar to all our selenium integrations you can specify your authorization token by specifying an additional capability of `browserless:token`. You'll also want to ensure `--headless` and `--no-sandbox` are set as well.

Here's a small example:

```codeBlockLines_p187
import java.net.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.remote.*;

public class Browserless {
  public static void main() throws MalformedURLException {

    final ChromeOptions chromeOptions = new ChromeOptions();

    chromeOptions.addArguments("--no-sandbox");
    chromeOptions.addArguments("--headless");
    chromeOptions.addArguments("--disable-dev-shm-usage");
    chromeOptions.setCapability("browserless:token", "YOUR-API-TOKEN");

    WebDriver driver = new RemoteWebDriver(
        new URL("https://chrome.browserless.io/webdriver"),
        chromeOptions
    );

    driver.get("https://www.example.com");
    driver.quit();
  }
}

```

This will simply navigate to the Example website, however it'll give you a great starting place for using Java Selenium alongside browserless.

Be sure to [let us know if you have questions or issues](https://www.browserless.io/contact).