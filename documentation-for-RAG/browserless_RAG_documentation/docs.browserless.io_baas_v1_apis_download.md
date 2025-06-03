---
url: "https://docs.browserless.io/baas/v1/apis/download"
title: "/download API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/download#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/download) or [BrowserQL](https://docs.browserless.io/browserql/start).

Much like the `/function` API, the `/download` API allows you to `POST` code for browserless to execute. The only difference with /download is that, instead of returning the result of your function, we instead return a file that the browser downloads.

Check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_download).

> If your download request doesn't result in a file being downloaded, browserless will likely time out the function.

## Basic Usage [​](https://docs.browserless.io/baas/v1/apis/download\#basic-usage "Direct link to Basic Usage")

Here's an example of downloading a file created in the browser (a CSV file):

```codeBlockLines_p187
const puppeteer = require('puppeteer');

async function run() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Here we generate a CSV file and have the browser download it
  await page.evaluate(() => {
    const rows = [\
      ['name1', 'city1', 'some other info'],\
      ['name2', 'city2', 'more info'],\
    ];
    let csvContent = 'data:text/csv;charset=utf-8,';
    rows.forEach(function (rowArray) {
      let row = rowArray.join(',');
      csvContent += row + '\r\n';
    });
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'data.csv');
    document.body.appendChild(link);

    return link.click();
  });
}

run();

```

This might come as a surprise, but unfortunately in puppeteer there's no way to know if the file was downloaded, or an API to even get it. You'll have to _know_ ahead of time where files are kept, and watch the file system for it to complete. Instead of wiring up all that code you can send browserless an HTTP request and it takes care of all the underlying file-system calls:

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/download?token=YOUR-API-TOKEN \
  -H 'Content-Type: application/javascript' \
  -d 'module.exports = async ({ page }) => {
    await page.evaluate(() => {
        const rows = [\
            ["name1", "city1", "some other info"],\
            ["name2", "city2", "more info"]\
        ];
        let csvContent = "data:text/csv;charset=utf-8,";
        rows.forEach(function(rowArray){
            let row = rowArray.join(",");
            csvContent += row + "\r\n";
        });
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "data.csv");
        document.body.appendChild(link);

        return link.click();
    });
};'

```

This API is sensitive to the downloaded file and will return an appropriate `Content-Type` with the response.

## Parameterizing your /download call [​](https://docs.browserless.io/baas/v1/apis/download\#parameterizing-your-download-call "Direct link to Parameterizing your /download call")

You can also post an `application/json` body, as opposed to an `application/javascript` one, if you'd like to re-use your function with new parameters. In this case, let's change our CSV file to be dynamic (note that our script is now minified for portability):

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/download?token=YOUR-API-TOKEN \
  -H 'Content-Type: application/json' \
  -d '{
  "code": "module.exports=async({page:a,context:b})=>{const{rows:c}=b;await a.evaluate(()=>{let d='\''data:text/csv;charset=utf-8,'\'';c.forEach(function(g){let h=g.join('\'','\'');d+=h+'\''\r\n'\''});const e=encodeURI(d),f=document.createElement('\''a'\'');return f.setAttribute('\''href'\'',e),f.setAttribute('\''download'\'','\''data.csv'\''),document.body.appendChild(f),f.click()})};",
  "context": {
    "rows": [\
      ["Some", "Cool", "CSV"],\
            ["With", "Rows", "And Stuff"]\
        ]
  }
}'

```

This lets you define re-usable functions and invoke them over HTTP in a more flexible way.

- [Basic Usage](https://docs.browserless.io/baas/v1/apis/download#basic-usage)
- [Parameterizing your /download call](https://docs.browserless.io/baas/v1/apis/download#parameterizing-your-download-call)