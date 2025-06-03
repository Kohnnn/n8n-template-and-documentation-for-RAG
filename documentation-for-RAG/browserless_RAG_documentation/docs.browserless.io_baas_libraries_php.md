---
url: "https://docs.browserless.io/baas/libraries/php"
title: "PHP (cURL) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/libraries/php#__docusaurus_skipToContent_fallback)

Version: v2

Browserless can run in PHP by using cURL.
Here's a small example:

```codeBlockLines_p187
<?php

$curl = curl_init();

curl_setopt_array($curl, [\
  CURLOPT_URL => "https://production-sfo.browserless.io/screenshot?token=YOUR_API_TOKEN_HERE",\
  CURLOPT_RETURNTRANSFER => true,\
  CURLOPT_ENCODING => "",\
  CURLOPT_MAXREDIRS => 10,\
  CURLOPT_TIMEOUT => 30,\
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,\
  CURLOPT_CUSTOMREQUEST => "POST",\
  CURLOPT_POSTFIELDS => "{\n  \"url\": \"https://example.com/\",\n\t\"options\": {\n\t\t\"fullPage\": true,\n\t\t\"encoding\": \"base64\"\n\t}\n}",\
  CURLOPT_HTTPHEADER => [\
    "Content-Type: application/json"\
  ],\
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}

```

This will simply take a screenshot of the Example website and return it encoded in base64 format, however it'll give you a great starting place for using our APIs through cURL in PHP.

Be sure to [let us know if you have questions or issues](https://www.browserless.io/contact).