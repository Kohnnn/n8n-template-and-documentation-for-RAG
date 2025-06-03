---
url: "https://docs.browserless.io/baas/v1/libraries/selenium-dotnet"
title: ".NET Selenium (C#) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/selenium-dotnet#__docusaurus_skipToContent_fallback)

Version: v1

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

Browserless now supports the .NET Selenium library provided by OpenQA! Similar to all our selenium integrations, you can specify your authorization token by specifying an additional capability of `browserless:token`. Note that this is _not_ a capability that Chrome understands natively, and will throw an error, so you must specify `true` as your 3rd argument.

Here's a full example:

```codeBlockLines_p187
using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Remote;
using OpenQA.Selenium.Chrome;

namespace BrowserlessSelenium
{
    class Program
    {
        static void Main(string[] args)
        {
            IWebDriver driver;
            ChromeOptions options = new ChromeOptions();

            // Set launch args similar to puppeteer's for best performance
            options.AddArgument("--disable-background-timer-throttling");
            options.AddArgument("--disable-backgrounding-occluded-windows");
            options.AddArgument("--disable-breakpad");
            options.AddArgument("--disable-component-extensions-with-background-pages");
            options.AddArgument("--disable-dev-shm-usage");
            options.AddArgument("--disable-extensions");
            options.AddArgument("--disable-features=TranslateUI,BlinkGenPropertyTrees");
            options.AddArgument("--disable-ipc-flooding-protection");
            options.AddArgument("--disable-renderer-backgrounding");
            options.AddArgument("--enable-features=NetworkService,NetworkServiceInProcess");
            options.AddArgument("--force-color-profile=srgb");
            options.AddArgument("--hide-scrollbars");
            options.AddArgument("--metrics-recording-only");
            options.AddArgument("--mute-audio");
            options.AddArgument("--headless");
            options.AddArgument("--no-sandbox");

            options.AddAdditionalOption("browserless:token", "YOUR-API-TOKEN");
            options.AddAdditionalOption("browserless:timeout", 60000);//optional flag to set a different timeout value than the default
            options.AddAdditionalOption("browserless:stealth", True);//optional flag to enable Stealth
            options.AddAdditionalOption("browserless:blockAds", True);//optional flag to enable blockAds
            options.AddAdditionalOption("browserless:trackingId", "AwENCwMHDQoHBgwKBAUODQ");//optional flag to enable trackingId
            options.AddAdditionalOption("browserless:pauseOnConnect", True);//optional flag to enable pauseOnConnect

            driver = new RemoteWebDriver(
              new Uri("https://chrome.browserless.io/webdriver"), options.ToCapabilities()
            );

            driver.Navigate().GoToUrl("https://example.com");
            Console.WriteLine(driver.Title);

            // Always call `quit` to ensure your session cleans up properly and you're not charged for unused time
            driver.Quit();
        }
    }
}

```

This will simply log out the Title from the Example website, however it'll give you a great starting place for using .NET alongside browserless.

Be sure to [let us know if you have questions or issues](https://www.browserless.io/contact).