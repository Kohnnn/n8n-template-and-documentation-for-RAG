---
url: "https://qdrant.tech/blog/enterprise-vector-search/"
title: "Introducing Qdrant Cloud’s New Enterprise-Ready Vector Search - Qdrant"
---

0

# Introducing Qdrant Cloud’s New Enterprise-Ready Vector Search

Daniel Azoulai

·

March 04, 2025

![Introducing Qdrant Cloud’s New Enterprise-Ready Vector Search](https://qdrant.tech/blog/enterprise-vector-search/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fenterprise-vector-search%2F&text=Introducing%20Qdrant%20Cloud%e2%80%99s%20New%20Enterprise-Ready%20Vector%20Search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fenterprise-vector-search%2F "LinkedIn")

At Qdrant, we enable developers to power AI workloads - not only securely, but at any scale. That’s why we are excited to introduce Qdrant Cloud’s new suite of enterprise-grade features. With **our Cloud API, Cloud RBAC**, **Single Sign-On (SSO)**, granular **Database API Keys**, and **Advanced Monitoring & Observability**, you now have the control and visibility needed to operate at scale.

## [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#securely-scale-your-ai-workloads) Securely Scale Your AI Workloads

Your enterprise-grade AI applications demand more than just a powerful vector database—they need to meet compliance, performance, and scalability requirements. To do that, you need simplified management, secure access & authentication, and real-time monitoring & observability. Now, Qdrant’s new enterprise-grade features address these needs, giving your team the tools to reduce operational overhead, simplify authentication, enforce access policies, and have deep visibility into performance.

## [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#our-new-qdrant-cloud-capabilities) Our New Qdrant Cloud Capabilities:

- **Cloud API for Simplified Management →** Automate and scale with **API-driven control** and **Terraform support**.
- **Secure Access & Authentication** → Control who gets in and what they can do with **Cloud RBAC**, **SSO**, and granular **Database API Keys**.
- **Advanced Monitoring & Observability** → Stay ahead of issues with **Prometheus/OpenMetrics**, **Datadog**, **Grafana**, and other third-party integrations.

## [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#ok-now-for-the-good-part) Ok, now for the good part…

### [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#cloud-api-for-simplified-management) Cloud API for Simplified Management

Skip the UI—manage Qdrant entirely through code. The [**Qdrant Cloud API**](https://qdrant.tech/documentation/qdrant-cloud-api/?) lets you automate cluster creation, updates, and scaling, ensuring repeatable, version-controlled deployments. You can also programmatically generate and revoke API keys, update configurations, and adapt infrastructure as workloads change.

You can manage the Qdrant Cloud lifecycle with Qdrant’s [**Terraform Provider**](https://qdrant.tech/documentation/cloud-tools/terraform/). With this support, you can define and automate cluster provisioning using Infrastructure-as-Code (IaC) best practices.

**Why it matters:** By automating cluster management and scaling, Qdrant helps you focus on building AI-powered applications, not maintaining infrastructure.

### [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#secure-access--authentication---control-the-who-and-what) Secure Access & Authentication - Control the Who and What

#### [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#cloud-rbac-role-based-access-control---the-who) Cloud RBAC (Role-Based Access Control) - The Who

With **Cloud RBAC**, you can define precise **role-based permissions** for team members managing clusters, billing, and hybrid cloud deployments in Qdrant Cloud. Instead of granting broad, unrestricted access, teams can **assign permissions based on roles**, ensuring tighter security and compliance.

#### [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#granular-database-api-keys---the-what) Granular Database API Keys - The What

**Database API Keys** let applications and services **directly interact with data inside Qdrant**. You can **grant API access at the cluster, collection, or even vector level**, specifying **read-only or read/write permissions** for each key.

Unlike **Cloud RBAC**, which governs **team permissions in the [Cloud Console](https://cloud.qdrant.io/login?ajs_anonymous_id=55ffe525-04b0-494e-901a-a11e9c33718b)**, **Database API Keys** control how external applications access stored data. You can define **fine-grained API key permissions**, apply **Time-to-Live (TTL) expiration policies**, and revoke keys instantly—without requiring a database restart ( **only available in Qdrant Cloud**).

To further refine access, **payload-based filters** allow you to restrict API keys to **only retrieve vectors that match specific metadata conditions**. Before finalizing an API key, you can **preview its access settings** to ensure it behaves as expected—reducing misconfigurations and improving security.

How to Use Qdrant's Database API Keys with Granular Access Control - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[How to Use Qdrant's Database API Keys with Granular Access Control](https://www.youtube.com/watch?v=3c-8tcBIVdQ)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=3c-8tcBIVdQ&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 3:00
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=3c-8tcBIVdQ "Watch on YouTube")

#### [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#read-more-about-database-api-keyshttpsqdranttechdocumentationcloudauthentication)[Read more about Database API keys](https://qdrant.tech/documentation/cloud/authentication/).

#### [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#single-sign-on-sso-for-simplified-authentication) Single Sign-On (SSO) for Simplified Authentication

**SSO** eliminates password sprawl by allowing users to log in through **Okta, Google Workspace, Azure AD (Entra ID), SAML, PingFederate, and more**—enforcing authentication policies while reducing IT overhead. Instead of managing separate credentials, users **simply enter their company email** and are redirected to their organization’s authentication system.

**SSO setup is fully supported**—to enable it for your company, **contact Qdrant support**, and our team will guide you through the setup process. SSO also works with **multi-factor authentication (MFA)** for additional security.

_SSO is only available for [Premium Tier](https://qdrant.tech/documentation/cloud/premium/) customers. [Learn more about SSO](https://qdrant.tech/documentation/cloud/qdrant-cloud-setup/#enterprise-single-sign-on-sso)._

How to Use Qdrant's Single Sign-On (SSO) Integration - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[How to Use Qdrant's Single Sign-On (SSO) Integration](https://www.youtube.com/watch?v=EtUcA-MCZJM)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=EtUcA-MCZJM&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 1:16
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=EtUcA-MCZJM "Watch on YouTube")

**Why it matters:** By integrating **Cloud RBAC**, granular **Database API Keys** and **SSO**, Qdrant Cloud helps your team have the right access at the right time—without unnecessary friction.

### [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#advanced-monitoring-and-observability-for-full-performance-insights) Advanced Monitoring and Observability for Full Performance Insights

Qdrant Cloud provides **real-time visibility into database performance** with built-in **Prometheus/OpenMetrics support**. You can monitor **CPU usage, memory usage, disk space, request volumes, and query latencies** directly in the **Qdrant Cloud Console**, giving you a **live overview of system health**.

For **deeper analytics**, Qdrant lets you **integrate with your existing monitoring stack**, including [Datadog](https://qdrant.tech/documentation/observability/datadog/) **,** [Grafana](https://qdrant.tech/documentation/cloud/cluster-monitoring/#grafana-dashboard) **,** and [other enterprise observability tools](https://qdrant.tech/documentation/observability/). Every Qdrant Cloud cluster includes a **metrics endpoint**, accessible via a **read-only API key**, providing **Prometheus and OpenTelemetry compatible data** for easy ingestion into Grafana Cloud or any other supported monitoring system.

Qdrant also provides a **ready-to-use [Grafana dashboard](https://github.com/qdrant/qdrant-cloud-grafana-dashboard)** to help you **visualize key database metrics**, including historical performance data, cluster uptime, request latencies, backup schedules, and network I/O.

You can set up **customizable alerts** in [Grafana](https://qdrant.tech/documentation/cloud/cluster-monitoring/#grafana-dashboard), Prometheus, or [Datadog](https://qdrant.tech/documentation/observability/datadog/) to **track key performance indicators** such as **memory**, **storage**, and **query** **latency** thresholds.

For **historical performance tracking**, third-party integrations allow you to **analyze trends over time**, providing deeper insights into system performance and long-term optimization strategies.

**Why it matters:** With **detailed telemetry, automated alerts, and deep observability integrations**, you can troubleshoot issues faster, optimize database performance, and scale AI applications.

Qdrant's Full Observability with Monitoring - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Qdrant's Full Observability with Monitoring](https://www.youtube.com/watch?v=pKPP-tL5_6w)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=pKPP-tL5_6w&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 2:31
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=pKPP-tL5_6w "Watch on YouTube")

[Read more about advanced monitoring](https://qdrant.tech/documentation/cloud/cluster-monitoring/).

## [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#simply-put-qdrant-is-enterprise-ready) Simply put, Qdrant is Enterprise-Ready

Our high-performance vector search engine already handles billion-scale use cases. Through Qdrant Cloud, you get our Cloud API, authentication & access tools, and monitoring & observability integrations.

With this combination, you can simplify infrastructure management, implement secure access & authentication, and stay ahead of performance challenges. That’s why Qdrant is the enterprise vector database of choice— **no matter the scale**.

## [Anchor](https://qdrant.tech/blog/enterprise-vector-search/\#come-build-with-us) Come Build with Us!

[Contact Sales](https://qdrant.tech/contact-us/) to enable enterprise features for your team, or [start prototyping with a free Qdrant cluster](https://login.cloud.qdrant.io/u/signup/identifier?state=hKFo2SAxeFNkY0JxeTMwUmpsRk15SFRUR2dFbmFYcjJUdnpHc6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFpOOTQ4S21uUEVlM3o1WUx1QnMzSUlrMmlIR1NtV1JCo2NpZNkgckkxd2NPUEhPTWRlSHVUeDR4MWtGMEtGZFE3d25lemc).

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=55ffe525-04b0-494e-901a-a11e9c33718b)

![](https://qdrant.tech/img/rocket.svg)

Up!

![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)

## Privacy Preference Center

Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.


[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)

Allow All

### Manage Consent Preferences

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5f66bc5e-bd8b-4a1d-bd41-53ff4995ad29&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=559663c7-938d-48d0-a276-9880cb4718be&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fenterprise-vector-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5f66bc5e-bd8b-4a1d-bd41-53ff4995ad29&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=559663c7-938d-48d0-a276-9880cb4718be&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fenterprise-vector-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372).