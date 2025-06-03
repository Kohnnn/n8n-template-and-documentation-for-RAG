---
url: "https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner"
title: "Find the best proxy to beat \"403 access denied\" with our proxy scanner | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner#main-content)

# Find the best proxy to beat "403 access denied" with our proxy scanner

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 13 April, 2025



Topic

[How-To](https://changedetection.io/topic/how)

Using a proxy scanner to determine which proxies can bypass **403 Access Denied** errors is crucial when monitoring websites for product prices or other changes with tools like Changedetection.io. Some websites restrict access based on geographic location or traffic patterns, leading to blocked requests and incomplete monitoring. A proxy scanner helps identify working proxies that successfully retrieve pages without being denied, ensuring consistent access to accurate data.

Fortunately changedetection.io has a **proxy scanner** built in - so take for example this common situation where we have a few proxies configured but we get the error **403 access denied** on our default proxy

![403 access denied](https://changedetection.io/sites/changedetection.io/files/inline-images/image_119.png)

If we jump over to **Edit** \> then **Requests** tab we can then find the **Proxy Scanner tool** which will help us find the proxy (or location) that will let us by-pass the 403 Access Denied error.

**First you need to add your proxies**

Jump on over to **Settings** \> **CAPTCHA & Proxies** and add your "Extra proxies", in the hosted/subscription version we call these "locations" however they are the same thing. I recommend BrightData or Oxylabs here, they are both fantastic.

![Adding Proxies](https://changedetection.io/sites/changedetection.io/files/inline-images/image_124.png)

Then go back to your "watch", and click " **EDIT**" and " **Request**"

Then we click on **Check / Scan All** to activate the scanner on all proxy connections and find the one which will not give the 403 access denied message.

(other options like _request method_ removed here for the sake of brevity)

![403 access denied - start proxy scanner / check all](https://changedetection.io/sites/changedetection.io/files/inline-images/image_121.png)

Once we click on that **Check / Scan All** the proxy scanner will then get to work!

Your browser does not support the video tag.


Within a few seconds we can see the results, that 4 of our proxies gave Access Denied, but 4 were ready to rock!  As well as some basic timing information (seconds for the request), any non-200 errors (error 500, error 403 etc) will show here.

So here we simply selected **Europe / Frankfurt** and then clicked **Save**

And then we wait a few seconds and see that the 403 access denied message is now gone

![403 access denied solved](https://changedetection.io/sites/changedetection.io/files/inline-images/image_122.png)

So there you have it, just another great little tool in changedetection - the **proxy scanner** which helps you beat **403 access denied** errors by find the best proxy for you!

As always, happy change detecting!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.