---
url: "https://docs.browserless.io/baas/load-balancers"
title: "Load Balancers | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/load-balancers#__docusaurus_skipToContent_fallback)

Version: v2

On this page

The Cloud Subscription plans and Dedicated plans have load balancing mechanisms built-in. This documentation will provide further information on how they work on each plan.

## Cloud subscriptions' load balancing [​](https://docs.browserless.io/baas/load-balancers\#cloud-subscriptions-load-balancing "Direct link to Cloud subscriptions' load balancing")

When you fire a request to our endpoints, it will go through our load balancers and will be sent to one of our instances to be handled. These are the cloud subscription endpoints available:

1. SFO endpoint: `https://production-sfo.browserless.io`
2. LON endpoint: `https://production-lon.browserless.io`
3. AMS endpoint: `https://production-ams.browserless.io`

We list our shared fleet's [IP addresses for whitelisting](https://docs.browserless.io/baas/troubleshooting/whitelisting-ips) purposes.

Our cloud-unit fleet is comprised of many machines running browserless, and our load-balancer will automatically determine which machine to handle the request. If, say, a machine is too overloaded to handle the inbound connection then our load-balancer routes the request to another. In very plain terms we use a modified least-connected algorithm to ensure your request is handled appropriately.

## Enterprise - Dedicated workers' load balancing [​](https://docs.browserless.io/baas/load-balancers\#enterprise---dedicated-workers-load-balancing "Direct link to Enterprise - Dedicated workers' load balancing")

Your worker can be located in 4 different sites: San Francisco, New York, Amsterdam, or London. If you request to `https://chrome.browserless.io`, it will redirect to one of the 4 regions.

In order to improve the latency by having a worker located closer to your client, you'll want to use the load balancer closest to your machine to reduce the distance data from requests must travel. These are the load balancers available for you to point your traffic to:

1. West load balancer (SFO): `https://chrome-us-west.browserless.io`
2. East load balancer (NYC): `https://chrome-us-east.browserless.io`
3. UK load balancer (LON): `https://chrome-eu-uk.browserless.io`
4. AMS load balancer (AMS): `https://chrome-eu-ams.browserless.io`

### Multiple worker load balancing [​](https://docs.browserless.io/baas/load-balancers\#multiple-worker-load-balancing "Direct link to Multiple worker load balancing")

When you have multiple instances, it'll automatically load-balance amongst them by least connections. If you want to handle load-balancing on your end, you can get the endpoint for every individual worker by clicking on the URL in the "Address" Column in the Production Workers table available in your [account dashboard](https://account.browserless.io/).

- [Cloud subscriptions' load balancing](https://docs.browserless.io/baas/load-balancers#cloud-subscriptions-load-balancing)
- [Enterprise - Dedicated workers' load balancing](https://docs.browserless.io/baas/load-balancers#enterprise---dedicated-workers-load-balancing)
  - [Multiple worker load balancing](https://docs.browserless.io/baas/load-balancers#multiple-worker-load-balancing)