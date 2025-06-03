---
url: "https://docs.browserless.io/baas/v1/recipes/downloading-files"
title: "Dealing with file downloads in puppeteer | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/recipes/downloading-files#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

Because of the tight coupling between Chrome and the local file-system it can be hard to determine _where_ files are being downloaded, and subsequently process/remove them. Because of this complex nature we offer two mechanisms in which to deal with file downloads in browserless: using our `/download` API, or manage the downloads via the `/workspace` API.

## Using the /download API [​](https://docs.browserless.io/baas/v1/recipes/downloading-files\#using-the-download-api "Direct link to Using the /download API")

Much like the `/function` API, the `/download` API allows you to `POST` a module to run that will return the file the browser downloads. Here's an example of a puppeteer script that will return a CSV file:

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

This might come as a surprise, but unfortunately in puppeteer there's no way to know if the file downloaded, or an API to even get it. You'll have to _know_ ahead of time where files are kept, and watch the file-system for it to complete!

browserless can save you all of that pain by using the simple `/download` API. Here's that same example:

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

This will process your code, create a new temporary directory, execute your script, watch for the download to complete and return it with an appropriate Content-Type (plus delete it from within the container). If there's an issue in the process, browserless will return semantic HTTP codes, and messages relaying what exactly happened to help with debugging.

This can save you numerous hassles as it takes care of all the low-level work involved in dealing with file-downloads, but if you're curious on how to accomplish this without this API read below!

## Using the `/workspace` API [​](https://docs.browserless.io/baas/v1/recipes/downloading-files\#using-the-workspace-api "Direct link to using-the-workspace-api")

The /workspace API allows for users to manually upload and download files that browserless (and thus Chrome) can access. In our prior example, we didn't care about the file-system in any capacity, however that changes if you wish to continue to use puppeteer in your code-base and call it programatically.

### 1\. Mount the `WORKSPACE_DIR` someplace [​](https://docs.browserless.io/baas/v1/recipes/downloading-files\#1-mount-the-workspace_dir-someplace "Direct link to 1-mount-the-workspace_dir-someplace")

By default, the internal `WORKSPACE_DIR` in browserless is set to the operating-system's temporary directory. It's best if you can mount it in an ephemeral location, but any directory with write-privileges is fine:

```codeBlockLines_p187
docker run -e "WORKSPACE_DIR=/home/browserless" -p 3000:3000 --restart always -d --name browserless browserless/chrome:latest

```

Now that is done we can instrument puppeteer to use it as the directory to download files.

### 2\. Tell puppeteer where to download files [​](https://docs.browserless.io/baas/v1/recipes/downloading-files\#2-tell-puppeteer-where-to-download-files "Direct link to 2. Tell puppeteer where to download files")

Chrome defaults to downloading files in various places, depending on the operating system. In our case, we want to tell it where since it provides greater flexibility on sharing files and processing them in an expedited manner.

In order to tell puppeteer where to store files you'll have to reach into some internals so that things work appropriately:

```codeBlockLines_p187
await page._client.send('Page.setDownloadBehavior', {
  behavior: 'allow',
  // This path must match the WORKSPACE_DIR in Step 1
  downloadPath: '/home/browserless',
});

```

Unfortunately you can't use the the [CDP Session](https://pptr.dev/#?product=Puppeteer&version=v1.11.0&show=api-class-cdpsession) manager to do this as it'll only apply to _that_ newly created CDP session, hence why it's required to to talk directly with the `_client` module on the `page` object.

Once this is set you can now emit whatever action to download the file!

### 3\. Download the file in the page [​](https://docs.browserless.io/baas/v1/recipes/downloading-files\#3-download-the-file-in-the-page "Direct link to 3. Download the file in the page")

By whatever means, this is the step where you'll download the file in the browser. Using our prior example we'll set this to generate a file for illustration purposes:

```codeBlockLines_p187
await page._client.send('Page.setDownloadBehavior', {
  behavior: 'allow',
  // This path must match the WORKSPACE_DIR in Step 1
  downloadPath: '/home/browserless',
});
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

```

This will trigger the file to download to the file-system _inside of browserless_.

### 4\. Download the file [​](https://docs.browserless.io/baas/v1/recipes/downloading-files\#4-download-the-file "Direct link to 4. Download the file")

Unfortunately you'll have to know the file's name in order to deal with it appropriately, but since browserless ships with a `/workspace` API we can use a simple `GET` request to see what's on the disk!

**Get downloads on browserless**

```codeBlockLines_p187
# Curl browserless and see what files it has
curl -X GET \
  https://chrome.browserless.io/workspace?token=MY_API_TOKEN

```

This will return a list of files, which we can then use a subsequent `GET` call to download.

```codeBlockLines_p187
[\
  {\
    "isDirectory": false,\
    "name": "data.csv",\
    "size": 2649\
  }\
]

```

Now that we know the file is there, and the name of it, we can issue our `GET` call to download it:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/workspace/data.csv?token=MY_API_TOKEN

```

Once we have it in our possession, a simple `DELETE` call will remove it from browserless' file-system:

```codeBlockLines_p187
curl -X DELETE \
  https://chrome.browserless.io/workspace/data.csv?token=MY_API_TOKEN

```

As you can see there's a lot involved in dealing with file-downloads: managing the directory where they reside, telling puppeteer _where_ to download them, and interacting with the file-system to get/delete them once we're done. If this seems like too much of a task then we highly recommend using the `/download` API and letting browserless deal with all the low-level internals.

- [Using the /download API](https://docs.browserless.io/baas/v1/recipes/downloading-files#using-the-download-api)
- [Using the `/workspace` API](https://docs.browserless.io/baas/v1/recipes/downloading-files#using-the-workspace-api)
  - [1\. Mount the `WORKSPACE_DIR` someplace](https://docs.browserless.io/baas/v1/recipes/downloading-files#1-mount-the-workspace_dir-someplace)
  - [2\. Tell puppeteer where to download files](https://docs.browserless.io/baas/v1/recipes/downloading-files#2-tell-puppeteer-where-to-download-files)
  - [3\. Download the file in the page](https://docs.browserless.io/baas/v1/recipes/downloading-files#3-download-the-file-in-the-page)
  - [4\. Download the file](https://docs.browserless.io/baas/v1/recipes/downloading-files#4-download-the-file)