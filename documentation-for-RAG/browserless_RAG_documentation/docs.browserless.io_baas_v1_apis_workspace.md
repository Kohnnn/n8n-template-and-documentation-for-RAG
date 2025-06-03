---
url: "https://docs.browserless.io/baas/v1/apis/workspace"
title: "/workspace API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/workspace#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/intro) or [BrowserQL](https://docs.browserless.io/browserql/start).

info

If you're using the hosted service, please refer to our GraphQL "workspace" query for better documentation. We also collect workspace results across your entire fleet in GraphQL. See [https://api.browserless.io/graphql](https://api.browserless.io/graphql)

When dealing with both file downloads and uploads, Chrome needs access to the local file-system. In most docker-based environments this can be challenging since each container runs with its own file-system, unless you attach a network-mounted file system (and subsequently grant it access in your `docker run` command). Because of these challenges we've implemented a series of API's that make it easier to work with files on disk, under the `/workspace` route.

Check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Management%20API/post_workspace).

info

The workspace API is only available for dedicated and self-hosted accounts

## Listing your files [​](https://docs.browserless.io/baas/v1/apis/workspace\#listing-your-files "Direct link to Listing your files")

To get files on your running container, simply issue a `GET` request to `/workspace`:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/workspace?token=MY_API_TOKEN

```

The following cURL will result in an output like:

```codeBlockLines_p187
[\
  {\
    "created": "2019-07-15T22:11:40.157Z",\
    "isDirectory": false,\
    "name": "data.csv",\
    "path": "/workspace/data.csv",\
    "size": 52,\
    "workspaceId": null\
  }\
]

```

Please note that this _will_ print any files in the current directory, but won't recursively look into them. It will also show files that browserless itself hasn't had any interaction with (in cases where assign `WORKSPACE_DIR` to a non-empty directory in docker). Consequently, **browserless won't delete or remove any files automatically**, so take care that files are removed swiftly when no-longer needed.

With this information returned, we can now download a file from the system.

## Downloading files [​](https://docs.browserless.io/baas/v1/apis/workspace\#downloading-files "Direct link to Downloading files")

Once you know the name of the file, you can simply issue a `GET` request for that particular file. We currently don't support downloading of all files in an archived format, so you'll need to issue a download request for every file you want.

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/workspace/file-one.csv?token=MY_API_TOKEN

```

Depending on the file, and its extension, browserless will stream the file back. In this case since the file is a CSV file, it'll return a `text/csv; charset=UTF-8` Content-Type.

```codeBlockLines_p187
"Wednesday, October 10, 2018"
"Thursday, October 4, 2018"
"Monday, October 1, 2018"
"Wednesday, September 26, 2018"
"Monday, September 24, 2018"
"Wednesday, September 19, 2018"
"Monday, September 17, 2018"
"Wednesday, September 12, 2018"

```

## Saving files [​](https://docs.browserless.io/baas/v1/apis/workspace\#saving-files "Direct link to Saving files")

If you need to have a file locally for Chrome to reference, then you'll need to upload it into browserless for consumption. This is done by `POST` ing a requests to the `/workspace` API with a `multipart/form-data` Content-Type. This allows for uploading of _multiple_ files, and is more flexible to meet a variety of use-cases. Once uploaded, browserless will return an array of file information based upon the content.

Please refer to your language or libraries documentation on how to handle `multipart/form-data` uploads. cURL, for instance, adds these headers automatically, as does many other libraries.

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/workspace?token=MY_API_TOKEN \
  -F 'file=@/Users/browserless/Documents/file-one.csv'

```

Responses have the following output, and are always returned in an array:

```codeBlockLines_p187
[\
  {\
    "fieldname": "file",\
    "originalname": "file-one.csv",\
    "encoding": "7bit",\
    "mimetype": "text/csv",\
    "destination": "/Users/jgriffith/Downloads",\
    "filename": "file-one.csv",\
    "path": "/Users/jgriffith/Downloads/file-one.csv",\
    "size": 2649\
  }\
]

```

## Deleting files [​](https://docs.browserless.io/baas/v1/apis/workspace\#deleting-files "Direct link to Deleting files")

> Be careful when deleting files as the operation cannot be undone

When work is complete, or you simply want to cleanup the workspace, you can issue a `DELETE` request for the file(s) you want to remove. Following upon our previous examples, you'll need to tell browserless which file to delete:

```codeBlockLines_p187
curl -X DELETE \
  https://chrome.browserless.io/workspace/file-one.csv?token=MY_API_TOKEN

```

Once this is complete, browserless will either respond with a `404` if the file isn't available, or a `204` if the operation was successful.

By default our dedicated plans automatically get their workspace contents deleted seven (7) days after creation.

## Scoping downloads [​](https://docs.browserless.io/baas/v1/apis/workspace\#scoping-downloads "Direct link to Scoping downloads")

> Scoping downloads is available in version 1.11.0 of our docker images.

Often times workloads involve downloading the same files as previous sessions did, which can result in a filename conflict. You might also want to just extract _all_ the files that Chrome downloads in a particular session instead of a single file at a time. For instances such as these we recommend using a `trackingId` in your connect request.

`trackingID` treats the behavior of file downloads slightly differently. Instead of saving files in the default workspace directory, browserless will instead create a sub-directory with the name of the `trackingId` you provide. For instance, if you connect with the following, and run some work, the result of the /workspace GET call will include files in a sub-directory.

```codeBlockLines_p187
// Connect with a "trackingId" in the browserWSEndpoint:
puppeteer.connect({
  browserWSEndpoint:
    'wss://chrome.browserless.io?token=YOUR-API-TOKEN&trackingId=AwENCwMHDQoHBgwKBAUODQ',
});

// Do some work, download files, catch errors!
browser.close();

```

Now, with that session complete, a `GET /workspace` will reveal these contents:

```codeBlockLines_p187
[\
  {\
    // Date of file creation\
    created: "2019-07-15T22:11:40.157Z",\
\
    // If the download is a directory\
    isDirectory: false,\
\
    // The resulting files name\
    name: "data.csv",\
\
    // The path to retrieve the file\
    path: "/workspace/AwENCwMHDQoHBgwKBAUODQ/data.csv",\
\
    // The size of the file in bytes\
    size: 52,\
\
    // The tracking-id that this file belongs to\
    workspaceId: "AwENCwMHDQoHBgwKBAUODQ",\
  },\
];

```

Also, if you wish to get _all_ the files of a particular session, simply do a GET call with the sessions tracking ID in place. Following our previous example, that will look like:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/workspace/AwENCwMHDQoHBgwKBAUODQ?token=MY_API_TOKEN

```

This will return a ZIP archive of all the files downloaded from that particular session. Finally, you can do a DELETE call on that tracking-id to remove all files:

```codeBlockLines_p187
curl -X DELETE \
  https://chrome.browserless.io/workspace/AwENCwMHDQoHBgwKBAUODQ?token=MY_API_TOKEN

```

We strongly recommend using a `tracingId` that has a low chance of collision with another (like GUID or UUID). This prevents one session from overwriting another's request.

- [Listing your files](https://docs.browserless.io/baas/v1/apis/workspace#listing-your-files)
- [Downloading files](https://docs.browserless.io/baas/v1/apis/workspace#downloading-files)
- [Saving files](https://docs.browserless.io/baas/v1/apis/workspace#saving-files)
- [Deleting files](https://docs.browserless.io/baas/v1/apis/workspace#deleting-files)
- [Scoping downloads](https://docs.browserless.io/baas/v1/apis/workspace#scoping-downloads)