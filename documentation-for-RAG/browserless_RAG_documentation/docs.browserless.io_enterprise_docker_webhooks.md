---
url: "https://docs.browserless.io/enterprise/docker/webhooks"
title: "Docker Webhooks | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/docker/webhooks#__docusaurus_skipToContent_fallback)

On this page

When launching the docker image you can configure it to "callback" to a web-based URL when certain events occur. For instance, you can have it call an HTTP URI when sessions are queued or rejected.

For each URL, when the associated event happens, browserless will do a `GET` call on the provided URL. It doesn't listen to responses or failures, however it's a good idea to answer it back immediately to close any open connections.

Below is a list of all possible options. Be sure to check back often and see when more are added!

## Queuing [​](https://docs.browserless.io/enterprise/docker/webhooks\#queuing "Direct link to Queuing")

Setting a `QUEUE_ALERT_URL` will trigger the image to call a the specified URL when queuing begins to happen. You can set this to any HTTP URL as seen below:

```codeBlockLines_p187
$ docker run -d \
  --restart always \
  --name browserless \
  -e "QUEUE_ALERT_URL=https://my.website.com/queued" \
  -p 3000:3000
  ghcr.io/browserless/chromium

```

## Rejections [​](https://docs.browserless.io/enterprise/docker/webhooks\#rejections "Direct link to Rejections")

Setting a `REJECT_ALERT_URL` will trigger the image to call a the specified URL when rejections begins to happen. You can set this to any HTTP URL as seen below:

```codeBlockLines_p187
$ docker run -d \
  --restart always \
  --name browserless \
  -e "REJECT_ALERT_URL=https://my.website.com/rejected" \
  -p 3000:3000
  ghcr.io/browserless/chromium

```

## Timeouts [​](https://docs.browserless.io/enterprise/docker/webhooks\#timeouts "Direct link to Timeouts")

Setting a `TIMEOUT_ALERT_URL` will trigger the image to call a the specified URL when time-outs begins to happen. You can set this to any HTTP URL as seen below:

```codeBlockLines_p187
$ docker run -d \
  --restart always \
  --name browserless \
  -e "TIMEOUT_ALERT_URL=https://my.website.com/time-out" \
  -p 3000:3000
  ghcr.io/browserless/chromium

```

## Health Failure [​](https://docs.browserless.io/enterprise/docker/webhooks\#health-failure "Direct link to Health Failure")

Setting a `FAILED_HEALTH_URL` will trigger the image to call a the specified URL when the health of the instance is critical (over 99% on CPU and memory). You can use this event to potentially restart the image or replace it.

```codeBlockLines_p187
$ docker run -d \
  --restart always \
  --name browserless \
  -e "FAILED_HEALTH_URL=https://my.website.com/failed-health" \
  -p 3000:3000
  ghcr.io/browserless/chromium

```

## Need something else? [​](https://docs.browserless.io/enterprise/docker/webhooks\#need-something-else "Direct link to Need something else?")

If you're looking for hooks for other events, please [let us know](https://www.browserless.io/contact).

- [Queuing](https://docs.browserless.io/enterprise/docker/webhooks#queuing)
- [Rejections](https://docs.browserless.io/enterprise/docker/webhooks#rejections)
- [Timeouts](https://docs.browserless.io/enterprise/docker/webhooks#timeouts)
- [Health Failure](https://docs.browserless.io/enterprise/docker/webhooks#health-failure)
- [Need something else?](https://docs.browserless.io/enterprise/docker/webhooks#need-something-else)