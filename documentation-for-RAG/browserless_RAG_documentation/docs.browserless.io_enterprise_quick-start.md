---
url: "https://docs.browserless.io/enterprise/quick-start"
title: "Enterprise Quick Start | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/quick-start#__docusaurus_skipToContent_fallback)

On this page

Welcome to Browserless Enterprise! This guide will help you quickly get started with our Enterprise offerings and understand the key features available to you.

## What is Browserless Enterprise? [​](https://docs.browserless.io/enterprise/quick-start\#what-is-browserless-enterprise "Direct link to What is Browserless Enterprise?")

Browserless Enterprise provides advanced features and capabilities for organizations that need:

- Self-hosted browser automation infrastructure
- Private deployments with custom configurations
- Advanced monitoring and debugging tools
- High-volume browser automation at scale

## Getting Started [​](https://docs.browserless.io/enterprise/quick-start\#getting-started "Direct link to Getting Started")

### 1\. Choose Your Deployment Option [​](https://docs.browserless.io/enterprise/quick-start\#1-choose-your-deployment-option "Direct link to 1. Choose Your Deployment Option")

Browserless Enterprise can be deployed in several ways:

- **Docker**: Run Browserless in your own infrastructure using our Docker images
- **Private Deployment**: Custom-tailored deployments for your specific needs
- **Cloud Enterprise**: Managed enterprise-grade browser automation in our cloud

### 2\. Set Up Your Environment [​](https://docs.browserless.io/enterprise/quick-start\#2-set-up-your-environment "Direct link to 2. Set Up Your Environment")

#### Docker Quick Start [​](https://docs.browserless.io/enterprise/quick-start\#docker-quick-start "Direct link to Docker Quick Start")

The fastest way to get started with Browserless Enterprise is using our Docker image:

```codeBlockLines_p187
docker run \
  --rm \
  -p 3000:3000 \
  -e "CONCURRENT=10" \
  -e "TOKEN=YOUR_TOKEN" \
  ghcr.io/browserless/chromium

```

Visit [Docker Quick Start](https://docs.browserless.io/enterprise/docker/quickstart) for more detailed instructions.

#### Private Deployment [​](https://docs.browserless.io/enterprise/quick-start\#private-deployment "Direct link to Private Deployment")

For custom deployments, our team will work with you to set up Browserless in your environment according to your specific requirements. [Contact us](https://www.browserless.io/contact) to discuss your needs.

### 3\. Connect Your Application [​](https://docs.browserless.io/enterprise/quick-start\#3-connect-your-application "Direct link to 3. Connect Your Application")

Once your Browserless Enterprise instance is running, connect your application using Puppeteer, Playwright, or other supported libraries:

```codeBlockLines_p187
// Puppeteer example
const browser = await puppeteer.connect({
  browserWSEndpoint: "ws://localhost:3000?token=YOUR_TOKEN",
});

```

## Key Enterprise Features [​](https://docs.browserless.io/enterprise/quick-start\#key-enterprise-features "Direct link to Key Enterprise Features")

### User Data Directory [​](https://docs.browserless.io/enterprise/quick-start\#user-data-directory "Direct link to User Data Directory")

Persist browser sessions and cookies between runs with [User Data Directory](https://docs.browserless.io/enterprise/user-data-directory) support.

### Watching Sessions [​](https://docs.browserless.io/enterprise/quick-start\#watching-sessions "Direct link to Watching Sessions")

Monitor and debug browser sessions in real-time with the [Session Watching](https://docs.browserless.io/enterprise/watching-sessions) feature.

### Live Debugger [​](https://docs.browserless.io/enterprise/quick-start\#live-debugger "Direct link to Live Debugger")

Interactively debug your browser automation scripts with the [Live Debugger](https://docs.browserless.io/enterprise/live-debugger).

### Utility Functions [​](https://docs.browserless.io/enterprise/quick-start\#utility-functions "Direct link to Utility Functions")

Access powerful utility functions for [session management](https://docs.browserless.io/enterprise/utility-functions/sessions), [configuration](https://docs.browserless.io/enterprise/utility-functions/config), and [metrics](https://docs.browserless.io/enterprise/utility-functions/metrics).

## Next Steps [​](https://docs.browserless.io/enterprise/quick-start\#next-steps "Direct link to Next Steps")

- Learn about [Browserless Terminology](https://docs.browserless.io/enterprise/terminology)
- Explore [Docker Configuration](https://docs.browserless.io/enterprise/docker/configuration)
- Set up [Private Deployment](https://docs.browserless.io/enterprise/private-deployment/graphql-api)
- Understand [Worker Settings](https://docs.browserless.io/enterprise/private-deployment/worker-settings)

For any questions or assistance, [contact our support team](https://www.browserless.io/contact).

- [What is Browserless Enterprise?](https://docs.browserless.io/enterprise/quick-start#what-is-browserless-enterprise)
- [Getting Started](https://docs.browserless.io/enterprise/quick-start#getting-started)
  - [1\. Choose Your Deployment Option](https://docs.browserless.io/enterprise/quick-start#1-choose-your-deployment-option)
  - [2\. Set Up Your Environment](https://docs.browserless.io/enterprise/quick-start#2-set-up-your-environment)
  - [3\. Connect Your Application](https://docs.browserless.io/enterprise/quick-start#3-connect-your-application)
- [Key Enterprise Features](https://docs.browserless.io/enterprise/quick-start#key-enterprise-features)
  - [User Data Directory](https://docs.browserless.io/enterprise/quick-start#user-data-directory)
  - [Watching Sessions](https://docs.browserless.io/enterprise/quick-start#watching-sessions)
  - [Live Debugger](https://docs.browserless.io/enterprise/quick-start#live-debugger)
  - [Utility Functions](https://docs.browserless.io/enterprise/quick-start#utility-functions)
- [Next Steps](https://docs.browserless.io/enterprise/quick-start#next-steps)