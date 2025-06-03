---
url: "https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring"
title: "Using Bright Data's \"Scraping Browser\" to by-pass CAPTCHA's and other protection when monitoring pages | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring#main-content)

# Using Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pages

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 16 November, 2024



Topic

[How-To](https://changedetection.io/topic/how)

[Proxies](https://changedetection.io/topic/proxies)

For many websites - simply using a proxy is not enough, the website is using much more complex anti-robot software to detect the actual browser that is being used, not just the IP connection or headers (including common headers such as user-agent and others)

You need a better way to simulate a real browser - A scraping browser is different to a proxy, a proxy just tunnels your connection but the Browser still looks the same, with a scraping browsers you are also simulating a real browser hidden away in Bright Data's infrastructure.

As it turns out, many websites are probing much deeper into your browser - analysing the response from your 2D and 3D/GPU videocard is just one of the tactics they use.

Unfortunately for many headless Chrome sessions it means they stand out all too easy - their "fingerprint" is just too obvious, they dont have anything that resembles a real video card or other hardware attached.

The result is - you get pushed to enter a CAPTCHA or other similar anti-robot mechanism.

_**But there is a solution,**_ whilst not guaranteed - it definitely helps a lot!

The clever people over at Bright Data have added a "Scraping Browser" to their offers, which more precisely simulates a real browser than just about anything you can try to run yourself.

(note: this functionality in changedetection.io will be released late November 2023, but you can try it now under the current _master_ tag from our [GitHub](https://github.com/dgtlmoon/changedetection.io) or [dev tag from our Docker Hub](https://hub.docker.com/layers/dgtlmoon/changedetection.io/dev/images/sha256-2397ad50a81527514492e859da685dada3863659b1e233f8e8f020eb08af0da0?context=explore))

More information about [Bright Data's scraping browser can be found here.](https://brightdata.com/products/scraping-browser)

#### _**Here's how to setup Bright Data's "Scraping Browser" with changedetection.io**_

Head on over to your Bright Data _**control panel**_ \- When you sign up using this link -  [https://brightdata.grsm.io/n0r16zf7eivq](https://brightdata.grsm.io/n0r16zf7eivq) \- BrightData will match any first deposit up to $150.

Once logged in - click on _**"Scraping Browser"**_

![The Bright Data control panel - where to find the Scraping Browser link](https://changedetection.io/sites/changedetection.io/files/inline-images/image_28.png)

Now we will copy the special "Connection address" so changedetection.io knows how to find the Scraping Browser, click on **Check out code and integration examples o** n the bottom right.

It's also worth considering here that you can add on extra residential proxies , residential proxies also greatly increase your chance of skipping past any potential CAPTCHA issues, but for now we will continue with the default setup.

![The Bright Data control panel - where to find the Scraping Browser link](https://changedetection.io/sites/changedetection.io/files/inline-images/image_33.png)

Copy the text from the next page into your clipboard, it will start with **wss://**, be sure to not include any quotes or other text, copy the whole text which is marked in blue below.

![The Bright Data control panel - where to find the Scraping Browser wss:// link for changedetection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_34.png)

Now for the fun part, jump over to  your changedetection.io login and click on **Settings > CAPTCHA & Proxies,** scroll down to the _**"Extra Browsers"**_ section, give your browser a name (in this case just **BrightData Scraping Browser** and paste the **wss://...** type URL into the **Connection URL** box

![Adding a scraping browser to changedetection.io - step 1 adding the browser link](https://changedetection.io/sites/changedetection.io/files/inline-images/image_37.png)

Now to use your new Scraping Browser with any website you are watching for changes, simply click **Edit** in your overview list and select the new browser

![list of websites with changes overview](https://changedetection.io/sites/changedetection.io/files/inline-images/image_39.png)

Choose the new browser **Bright Data Scraping Browser** that we setup in the previous step.

![Setting a single website to use a particular scraping browsers](https://changedetection.io/sites/changedetection.io/files/inline-images/image_40.png)

And there you have it - _how to setup a scraping browser to get a much better success rate (say goodbye CAPTCHA!) when watching websites for changes._

_Some extra tips -_

When you setup additional Residential Proxies - Bright Data will present you with a new "wss://.." type connection URL, so you can then setup multiple proxy networks with multiple scraping browsers.

Sign up with Bright Data using [https://brightdata.grsm.io/n0r16zf7eivq](https://brightdata.grsm.io/n0r16zf7eivq) BrightData will match any first deposit up to $150

### Troubleshooting

If you see the error  " `Overriding accept-language, user-agent headers forbidden`" \-  You may need to enable " _Custom headers_" \- In your Brightdata dashboard - under the `Proxy Settings` \> `Configuration` \> `Advanced Settings` \> `Custom headers & cookies` this option needs to be activated. (changedetection.io may send its own custom User-Agent and other headers)

If you receive an error like `"WebSocket error: wss://brd-customer..... 403 wrong_auth"` then try whitelisting the IP of our server (or your local connection) from inside the BrightData control panel at the "Scraping Browser" settings - as an alternative to username+password (But still keep the username+password in the `wss://.. ` connection URL)

![Example of adding a white-list IP access in BrightData for the scraping browser](https://changedetection.io/sites/changedetection.io/files/inline-images/image_52.png)

Happy changedetecting!

**extra points!** You can now use the built-in proxy scanner to see which websites still give the 403 access denied error, check it out here [https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)

Your browser does not support the video tag.


- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.