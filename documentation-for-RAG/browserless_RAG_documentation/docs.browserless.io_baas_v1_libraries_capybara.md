---
url: "https://docs.browserless.io/baas/v1/libraries/capybara"
title: "Capybara | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/capybara#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

You can now use the `Capybara` library with browserless! Similar to most libraries based on the webdriver protocol, you simply need to tell `Capybara` _where_ to talk with Chrome. This is a pretty quick change to make:

```codeBlockLines_p187
require 'capybara'
require 'selenium-webdriver'

# Done for demo purposes here!
Capybara.server = :puma, { Silent: true }

Capybara.register_driver :remote_chrome do |app|
  Capybara::Selenium::Driver.new(app,
    :browser              => :remote,
    :url                  => 'https://YOUR_API_TOKEN_HERE@chrome.browserless.io/webdriver',
    :options => Selenium::WebDriver::Remote::Capabilities.chrome("goog:chromeOptions" => {
      "args" => [\
        "--headless",\
        "--no-sandbox"\
      ]
    }),
  )
end

Capybara.default_driver = :remote_chrome

browser = Capybara.current_session
browser.visit 'https://browserless.io/'
puts browser.html
browser.driver.quit

```

This will simply log out the HTML from the Example demo, however it'll give you a great starting place for using Capybara alongside browserless.

Be sure to [let us know if you have questions or issues](https://www.browserless.io/contact).

## Pausing for the debugger [​](https://docs.browserless.io/baas/v1/libraries/capybara\#pausing-for-the-debugger "Direct link to Pausing for the debugger")

You can use the built-in `desired_capabilities` parameter in Selenium's API to tell browserless to pause your script on startup, allowing you to visit the account page and click the Session link to view it as it runs. This is helpful if your script executes extremely quickly, making debugging harder to do.

```codeBlockLines_p187
# Tell browserless to pause on startup:
Capybara.register_driver :remote_chrome do |app|
  Capybara::Selenium::Driver.new(app, {
    :browser              => :remote,
    :url                  => 'https://YOUR_API_TOKEN_HERE@chrome.browserless.io/webdriver',
    :desired_capabilities => Selenium::WebDriver::Remote::Capabilities.chrome(
      "goog:chromeOptions" => { "args" => [ "--headless", "--no-sandbox" ] },
      # PAUSE!
      "browserless.pause": true
    ),
  })
end

```

## Specifying a different timeout [​](https://docs.browserless.io/baas/v1/libraries/capybara\#specifying-a-different-timeout "Direct link to Specifying a different timeout")

You can also override the global timeout for sessions by specifying a `browserless.timeout` capability as well:

```codeBlockLines_p187
# Set timeout to 30 seconds
Capybara.register_driver :remote_chrome do |app|
  Capybara::Selenium::Driver.new(app, {
    :browser              => :remote,
    :url                  => 'https://YOUR_API_TOKEN_HERE@chrome.browserless.io/webdriver',
    :desired_capabilities => Selenium::WebDriver::Remote::Capabilities.chrome(
      "goog:chromeOptions" => { "args" => [ "--headless", "--no-sandbox" ] },
      # 30 seconds in milliseconds
      "browserless.timeout": 30000
    ),
  })
end

```

- [Pausing for the debugger](https://docs.browserless.io/baas/v1/libraries/capybara#pausing-for-the-debugger)
- [Specifying a different timeout](https://docs.browserless.io/baas/v1/libraries/capybara#specifying-a-different-timeout)