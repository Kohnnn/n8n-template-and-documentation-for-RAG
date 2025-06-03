---
url: "https://docs.browserless.io/baas/v1/apis/stats"
title: "/stats API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/stats#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/intro) or [BrowserQL](https://docs.browserless.io/browserql/start).

The stats API reveals key metrics about a site's accessibility, best practices, performance, PWA information, and SEO, from a performance standpoint. It includes useful metrics like latency, time-to-interaction, design contrast other recommendations. This API is powered by [Google's Lighthouse](https://github.com/GoogleChrome/lighthouse) project, and it's compatible with its CLI options.

In order to gather this data, send a `POST` request to `https://chrome.browserless.io/stats` if on a hosted plan, with a simple JSON payload containing a valid URL.

warning

Due to the number of checks gathered it can take anywhere from several seconds to minutes depending on the site and size of the worker.

If you want to see all the options check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_stats).

### Examples [​](https://docs.browserless.io/baas/v1/apis/stats\#examples "Direct link to Examples")

1. [Basic Usage](https://docs.browserless.io/baas/v1/apis/stats#basic-usage)
2. [Gathering metrics for a category](https://docs.browserless.io/baas/v1/apis/stats#gathering-metrics-for-a-category)
3. [Gathering metrics from a single audit](https://docs.browserless.io/baas/v1/apis/stats#gathering-metrics-from-a-single-audit)

## Basic Usage [​](https://docs.browserless.io/baas/v1/apis/stats\#basic-usage "Direct link to Basic Usage")

**JSON**

```codeBlockLines_p187
{
  "url": "https://example.com/"
}

```

**cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/stats?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '
{
  "url": "https://example.com/"
}'

```

By default, the `/stats` API will gather **all** the metrics. This will not only result in a **really** big JSON response (350kb to 800kb on average) and it **will** take some seconds (to minutes) to complete.

Each test has a score that indicates how well it performed, where 1 is the maximum and 0 is the lowest, generating a response like this:

```codeBlockLines_p187
  // ...
  "audits": {
    "is-on-https": {
      "title": "Uses HTTPS",
      "score": 1
      // ...
    },
    "viewport": {
      "title": "Has a `<meta name=\"viewport\">` tag with `width` or `initial-scale`",
      "score": 1
      // ...
    },
    "first-contentful-paint": {
      "score": 1,
      "displayValue": "0.8 s"
      // ...
    }
    // ...
  }

```

## Gathering metrics for a category [​](https://docs.browserless.io/baas/v1/apis/stats\#gathering-metrics-for-a-category "Direct link to Gathering metrics for a category")

You can get metrics from specific categories, using the `config` property. [Just like Lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/readme.md#cli-options), available categories are `accessibility`, `best practices`, `performance`, `pwa`, and `seo`

**JSON**

```codeBlockLines_p187
{
  "url": "https://example.com",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyCategories": ["accessibility"]
    }
  }
}

```

**cURL request**

```codeBlockLines_p187
curl --request POST \
  --url 'https://chrome.browserless.io/stats?token=MY_API_TOKEN' \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://browserless.io",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyCategories": ["accessibility"]
    }
  }
}'

```

This will gather the predefined metrics defined by Lighthouse for that category:

```codeBlockLines_p187
  // ...
  "audits": {
    "aria-command-name": {
      "title": "`button`, `link`, and `menuitem` elements have accessible names",
      "score": 1
      // ...
    },
    "aria-hidden-body": {
      "title": "`[aria-hidden=\"true\"]` is not present on the document `<body>`",
      "score": 1
      // ...
    },
    "aria-hidden-focus": {
      "title": "`[aria-hidden=\"true\"]` elements do not contain focusable descendents",
      "score": 1
      // ...
    },
    // ...
  }

```

## Gathering metrics from a single audit [​](https://docs.browserless.io/baas/v1/apis/stats\#gathering-metrics-from-a-single-audit "Direct link to Gathering metrics from a single audit")

You can get any specific metrics [valid in Lighthouse](https://github.com/GoogleChrome/lighthouse/tree/master/core/audits)

```codeBlockLines_p187
{
  "url": "https://browserless.io",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyAudits": ["unminified-css"]
    }
  }
}

```

**cURL request**

```codeBlockLines_p187
curl --request POST \
  --url 'https://chrome.browserless.io/stats?token=MY_API_TOKEN' \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://browserless.io",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyCategories": ["accessibility"]
    }
  }
}'

```

**Response example**

```codeBlockLines_p187
  // ...
  "audits": {
    "unminified-css": {
      "title": "Minify CSS",
      "score": 1
      // ...
    },
    // ...
  }

```

- [Examples](https://docs.browserless.io/baas/v1/apis/stats#examples)
- [Basic Usage](https://docs.browserless.io/baas/v1/apis/stats#basic-usage)
- [Gathering metrics for a category](https://docs.browserless.io/baas/v1/apis/stats#gathering-metrics-for-a-category)
- [Gathering metrics from a single audit](https://docs.browserless.io/baas/v1/apis/stats#gathering-metrics-from-a-single-audit)