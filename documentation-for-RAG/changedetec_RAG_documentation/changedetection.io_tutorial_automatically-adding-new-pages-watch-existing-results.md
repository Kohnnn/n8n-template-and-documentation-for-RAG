---
url: "https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results"
title: "Automatically adding new pages to watch from existing results | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results#main-content)

# Automatically adding new pages to watch from existing results

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 3 January, 2024



Topic

[How-To](https://changedetection.io/topic/how)

Think of the situation where you are watching your favourite ecommerce website, and you want to start automatically watching any NEW pages for changes.

For example, you might be interested in a list of search results for a product, but then you also want to follow/watch those product pages for changes (maybe price changes, availability etc)

Since version `0.45.11` it is possible to use the built in API to ask changedetection.io to insert a new link into its database, as a plaintext list of links (with a tag/group as an optional argument), we can use the 'notifications' tab to tell changedetection.io to notify itself to add a new link :)

Here's how! In this example we will use CashConverters as our example.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_59.png)

## Step 1 - Add the website URL and configure the filters

Using the current URL, copied and paste from your browser, as the URL in changedetection to watch.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_53.png)

Now in this case, the VisualSelector is not quite what we want, because we are only interested in _all_ of the links to the products, additionally we are interested in the "HREF" part of the "A HREF" part of the link so that we can see what the products link is.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_55.png)

Fortunately, they make it super easy for us, the link is clearly marked with the CSS class name  `product-item__price`

So then to get a list of URLs for products, we can use xPath to ask it to extract the "href" part for us, and only return that list.

We " _simply_" use the Filter Rule  `//a[@class="product-item__title"]/@href`

_**Ah but wait!** We need to be sure we have the full link, including https:// and the domain name/website URL._

Change to use the Filter Rule  `xpath:for-each(//a[@class="product-item__title"]/@href, function($a) { concat("https://cashconverters.co.uk", $a) })`

( We will make this easier in the future with some plugins that will support easily appending text to each line of results )

![Showing how the filter looks for adding the domain to automatically discovered links](https://changedetection.io/sites/changedetection.io/files/inline-images/image_56.png)

Now we check out the **Preview** or **Difference Page** output, and we can see a nice list of links

![List of links discovered for automatic following](https://changedetection.io/sites/changedetection.io/files/inline-images/image_57.png)

## Step 2 - Automatically importing the URLs via the API

The built-in [API supports importing a list (plain-text) of URLs with an option organisational tag/group](https://changedetection.io/docs/api_v1/index.html#api-Watch-Import)

Using that, we will make changedetection.io "notify" its own API of any changes to that URL list

Make sure your API access is turned on, and you have the key ready (Visit  Settings > API )

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_58.png)

We will use that [API key in our notification URL](https://github.com/dgtlmoon/changedetection.io/wiki/Notification-configuration-notes#postposts), So the URL to notify (to automatically import the list of URLS) would be (careful to include the + at the start, this signifies that it should be a "http header")

`post://localhost:5000/api/v1/import?tag=CashConverters&+x-api-key=dfb4d69efdec620e30edcd916c545efc`

or in the case that you're using [our beloved subscription service](https://changedetection.io/#subscription)

`posts://lemonade.changedetection.io/your-loginURL/api/v1/import?tag=CashConverters&+x-api-key=dfb4d69efdec620e30edcd916c545efc`

Use " **post://**" for non-SSL and " **posts://**" if your installation lives on a HTTPS protected address.

And set the **Notification Body** to only " `{{current_snapshot}}`" then you can press **Send test notification**, this will send all of those URLs for population in changedetection.io

![Showing how to configure the API to automatically add links](https://changedetection.io/sites/changedetection.io/files/inline-images/image_61.png)

Once you click **"send test notifcation"** with **{{current\_snapshot}}**, you should then see all those links in  your watch list

![List of automatically added links from website](https://changedetection.io/sites/changedetection.io/files/inline-images/image_68.png)

By default, it will only add "new" links

Have fun, and experiment! Happy change detecting :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.