---
url: "https://docs.browserless.io/enterprise/docker/extending"
title: "Extending the Docker Image | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/docker/extending#__docusaurus_skipToContent_fallback)

On this page

info

For hosted accounts, if you want to use a third-party module please [get in touch!](https://www.browserless.io/contact)

Browserless includes a few extra packages that make it easy to get going with most of the use-cases we've seen. However if you're using the `/function` API, or other API's wherein you want to load npm modules, then you'll need to extend our image so that you can install these dependencies. The process if fairly easy in docker to do so.

## 1\. Create your own Dockerfile [​](https://docs.browserless.io/enterprise/docker/extending\#1-create-your-own-dockerfile "Direct link to 1. Create your own Dockerfile")

First, you'll want to write your own `Dockerfile`. In the example below, we're going to add the `aws-sdk` module.

```codeBlockLines_p187
FROM ghcr.io/browserless/chromium:latest

# Install the AWS SDK
RUN npm install aws-sdk

```

Feel free to change the `FROM` value here. It's generally a good practice to "pin" this version to value that won't change. For instance, if we want to use version [1.15.0](https://github.com/browserless/browserless/blob/V1/CHANGELOG.md#1150) of Browserless, we'd have done:

```codeBlockLines_p187
FROM ghcr.io/browserless/chromium:2.2.0

# Install the AWS SDK
RUN npm install aws-sdk

```

In either case, save your file and let's proceed.

## 2\. Build the docker image [​](https://docs.browserless.io/enterprise/docker/extending\#2-build-the-docker-image "Direct link to 2. Build the docker image")

Once the you have the file saved, it's as simple as building the image.

```codeBlockLines_p187
$ docker build -t my/browserless:latest .

```

Here, we're using a "dumby" user of `my` and a repo of `browserless`, tagging it as the \`latest. Feel free to change these however you see fit, especially if you want to push this built image into docker's public cloud or your own private image registry.

It'll likely take a few minutes to pull all the dependencies locally and build, however subsequent builds will be much quicker since they'll have a local cache.

## 3\. Run the image [​](https://docs.browserless.io/enterprise/docker/extending\#3-run-the-image "Direct link to 3. Run the image")

Now that you have a custom-built version you can apply all the same arguments to your start command (all environment variables and so on apply), you'll simply change the image you're running when you startup (note that we're whitelisting this new module, allowing browserless to execute it for security purposes).

Here's an example of running the newly built image with the module whitelisted.

```codeBlockLines_p187
$ docker run -p 3000:3000 -e FUNCTION_EXTERNALS='["aws-sdk"]' my/browserless:latest

```

Now your calls to `/function` and others will have access to the `aws-sdk` module:

```codeBlockLines_p187
$ curl -X POST \
  http://localhost:3000/function \
  -H 'Content-Type: application/javascript' \
  -d 'const aws = require('\''aws-sdk'\'');

module.exports = async () => {
  const data = Object.keys(aws);

  return {
    data,
    type: '\''text/plain'\'',
  };
};'

```

That's it! If you need to add more simply install your modules in the `Dockerfile`, build the image, and run it!

- [1\. Create your own Dockerfile](https://docs.browserless.io/enterprise/docker/extending#1-create-your-own-dockerfile)
- [2\. Build the docker image](https://docs.browserless.io/enterprise/docker/extending#2-build-the-docker-image)
- [3\. Run the image](https://docs.browserless.io/enterprise/docker/extending#3-run-the-image)