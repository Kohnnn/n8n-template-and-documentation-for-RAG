---
url: "https://qdrant.tech/documentation/cloud-tools/terraform/"
title: "Terraform - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud tools](https://qdrant.tech/documentation/cloud-tools/)
- Terraform

![Terraform Logo](https://qdrant.tech/documentation/platforms/terraform/terraform.png)

HashiCorp Terraform is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle.

With the [Qdrant Terraform Provider](https://registry.terraform.io/providers/qdrant/qdrant-cloud/latest), you can manage the Qdrant cloud lifecycle leveraging all the goodness of Terraform.

## [Anchor](https://qdrant.tech/documentation/cloud-tools/terraform/\#pre-requisites) Pre-requisites

To use the Qdrant Terraform Provider, you’ll need:

1. A [Terraform installation](https://developer.hashicorp.com/terraform/install).
2. An [API key](https://qdrant.tech/documentation/qdrant-cloud-api/#authentication-connecting-to-cloud-api) to access the Qdrant cloud API.

## [Anchor](https://qdrant.tech/documentation/cloud-tools/terraform/\#example-usage) Example Usage

The following example creates a new Qdrant cluster in Google Cloud Platform (GCP) and returns the URL of the cluster.

```terraform
terraform {
  required_version = ">= 1.7.0"
  required_providers {
    qdrant-cloud = {
      source  = "qdrant/qdrant-cloud"
      version = ">=1.1.0"
    }
  }
}

provider "qdrant-cloud" {
  api_key    = "<QDRANT_CLOUD_API_KEY>"
  account_id = "QDRANT_ACCOUNT_ID>" // Account ID from cloud.qdrant.io/accounts/<QDRANT_ACCOUNT_ID>/ (can be overriden on resource level)
}

resource "qdrant-cloud_accounts_cluster" "example" {
  name           = "tf-example-cluster"
  cloud_provider = "gcp"
  cloud_region   = "us-east4"
  configuration {
    number_of_nodes = 1
    node_configuration {
       package_id = "7c939d96-d671-4051-aa16-3b8b7130fa42"
    }
  }
}

output "url" {
  value = qdrant-cloud_accounts_cluster.example.url
}

```

The provider includes the following resources and data-sources to work with:

## [Anchor](https://qdrant.tech/documentation/cloud-tools/terraform/\#resources) Resources

- `qdrant-cloud_accounts_cluster` \- Create clusters on Qdrant cloud - [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/resources/accounts_cluster.md)

- `qdrant-cloud_accounts_auth_key` \- Create API keys for Qdrant cloud clusters. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/resources/accounts_auth_key.md)


## [Anchor](https://qdrant.tech/documentation/cloud-tools/terraform/\#data-sources) Data Sources

- `qdrant-cloud_accounts_auth_keys` \- List API keys for Qdrant clusters. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/accounts_auth_keys.md)

- `qdrant-cloud_accounts_cluster` \- Get Cluster Information. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/accounts_cluster.md)

- `qdrant-cloud_accounts_clusters` \- List Qdrant clusters. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/accounts_clusters.md)

- `qdrant-cloud_booking_packages` \- Get detailed information about the packages/subscriptions available. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/booking_packages.md)


## [Anchor](https://qdrant.tech/documentation/cloud-tools/terraform/\#further-reading) Further Reading

- [Provider Documentation](https://registry.terraform.io/providers/qdrant/qdrant-cloud/latest/docs)
- [Terraform Quickstart](https://developer.hashicorp.com/terraform/tutorials)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-tools/terraform.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-tools/terraform.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575408898&cv=11&fst=1748575408898&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fterraform%2F&hn=www.googleadservices.com&frm=0&tiba=Terraform%20-%20Qdrant&npa=0&pscdl=noapi&auid=1336049556.1748575409&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575408875&cv=11&fst=1748575408875&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fterraform%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Terraform%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1336049556.1748575409&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=cf1f5ac5-ea81-43f4-842e-dbccadcf4ead&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=81a8984d-3548-48fc-820c-43824153f0be&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fterraform%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=cf1f5ac5-ea81-43f4-842e-dbccadcf4ead&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=81a8984d-3548-48fc-820c-43824153f0be&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fterraform%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575410116&cv=11&fst=1748575410116&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fterraform%2F&hn=www.googleadservices.com&frm=0&tiba=Terraform%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1336049556.1748575409&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)