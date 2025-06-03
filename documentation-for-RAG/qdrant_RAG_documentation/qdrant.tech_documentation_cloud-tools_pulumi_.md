---
url: "https://qdrant.tech/documentation/cloud-tools/pulumi/"
title: "Pulumi - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud tools](https://qdrant.tech/documentation/cloud-tools/)
- Pulumi

![Pulumi Logo](https://qdrant.tech/documentation/platforms/pulumi/pulumi-logo.png)

Pulumi is an open source infrastructure as code tool for creating, deploying, and managing cloud infrastructure.

A Qdrant SDK in any of Pulumi’s supported languages can be generated based on the [Qdrant Terraform Provider](https://registry.terraform.io/providers/qdrant/qdrant-cloud/latest).

## [Anchor](https://qdrant.tech/documentation/cloud-tools/pulumi/\#pre-requisites) Pre-requisites

1. A [Pulumi Installation](https://www.pulumi.com/docs/install/).
2. An [API key](https://qdrant.tech/documentation/qdrant-cloud-api/#authentication-connecting-to-cloud-api) to access the Qdrant cloud API.

## [Anchor](https://qdrant.tech/documentation/cloud-tools/pulumi/\#setup) Setup

- Create a Pulumi project in any of the [supported languages](https://www.pulumi.com/docs/languages-sdks/) by running

```bash
mkdir qdrant-pulumi && cd qdrant-pulumi
pulumi new "<LANGUAGE>" -y

```

- Generate a Pulumi SDK for Qdrant by running the following in your Pulumi project directory.

```bash
pulumi package add terraform-provider registry.terraform.io/qdrant/qdrant-cloud

```

- Set the Qdrant cloud API as a config value.

```bash
pulumi config set qdrant-cloud:apiKey "<QDRANT_CLOUD_API_KEY>" --secret

```

- You can now import the SDK as:

pythontypescriptjava

```python
import pulumi_qdrant_cloud as qdrant_cloud

```

```typescript
import * as qdrantCloud from "qdrant-cloud";

```

```java
import com.pulumi.qdrantcloud.*;

```

## [Anchor](https://qdrant.tech/documentation/cloud-tools/pulumi/\#usage) Usage

The provider includes the following data-sources and resources to work with:

### [Anchor](https://qdrant.tech/documentation/cloud-tools/pulumi/\#data-sources) Data Sources

- `qdrant-cloud_booking_packages` \- Get IDs and detailed information about the packages/subscriptions available. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/booking_packages.md)

pythontypescriptjava

```python
qdrant_cloud.get_booking_packages(cloud_provider="aws", cloud_region="us-west-2")

```

```typescript
qdrantCloud.getBookingPackages({
    cloudProvider: "aws",
    cloudRegion: "us-west-2"
})

```

```java
import com.pulumi.qdrantcloud.inputs.GetBookingPackagesArgs;

QdrantcloudFunctions.getBookingPackages(GetBookingPackagesArgs.builder()
        .cloudProvider("aws")
        .cloudRegion("us-west-2")
        .build());

```

- `qdrant-cloud_accounts_auth_keys` \- List API keys for Qdrant clusters. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/accounts_auth_keys.md)

pythontypescriptjava

```python
qdrant_cloud.get_accounts_auth_keys(account_id="<ACCOUNT_ID>")

```

```typescript
qdrantCloud.getAccountsAuthKeys({
    accountId: "<ACCOUNT_ID>"
})

```

```java
import com.pulumi.qdrantcloud.inputs.GetAccountsAuthKeysArgs;

QdrantcloudFunctions.getAccountsAuthKeys(GetAccountsAuthKeysArgs.builder()
        .accountId("<ACCOUNT_ID>")
        .build());

```

- `qdrant-cloud_accounts_cluster` \- Get Cluster Information. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/accounts_cluster.md)

pythontypescriptjava

```python
qdrant_cloud.get_accounts_cluster(
    account_id="<ACCOUNT_ID>",
    id="<CLUSTER_ID>",
)

```

```typescript
qdrantCloud.getAccountsCluster({
    accountId: "<ACCOUNT_ID>",
    id: "<CLUSTER_ID>"
})

```

```java
import com.pulumi.qdrantcloud.inputs.GetAccountsClusterArgs;

QdrantcloudFunctions.getAccountsCluster(GetAccountsClusterArgs
        .builder()
        .accountId("<ACCOUNT_ID>")
        .id("<CLUSTER_ID>")
        .build());

```

- `qdrant-cloud_accounts_clusters` \- List Qdrant clusters. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/data-sources/accounts_clusters.md)

pythontypescriptjava

```python
qdrant_cloud.get_accounts_clusters(account_id="<ACCOUNT_ID>")

```

```typescript
qdrantCloud.getAccountsClusters({
    accountId: "<ACCOUNT_ID>"
})

```

```java
import com.pulumi.qdrantcloud.inputs.GetAccountsClustersArgs;

QdrantcloudFunctions.getAccountsClusters(
        GetAccountsClustersArgs.builder().accountId("<ACCOUNT_ID>").build());

```

### [Anchor](https://qdrant.tech/documentation/cloud-tools/pulumi/\#resources) Resources

- `qdrant-cloud_accounts_cluster` \- Create clusters on Qdrant cloud - [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/resources/accounts_cluster.md)

pythontypescriptjava

```python
qdrant_cloud.AccountsCluster(
    resource_name="pl-example-cluster-resource",
    name="pl-example-cluster",
    cloud_provider="gcp",
    cloud_region="us-east4",
    configuration=qdrant_cloud.AccountsClusterConfigurationArgs(
        number_of_nodes=1,
        node_configuration=qdrant_cloud.AccountsClusterConfigurationNodeConfigurationArgs(
            package_id="3920d1eb-d3eb-4117-9578-b12d89bb1c5d"
        ),
    ),
    account_id="<ACCOUNT_ID>",
)

```

```typescript
new qdrantCloud.AccountsCluster("pl-example-cluster-resource", {
    cloudProvider: "gcp",
    cloudRegion: "us-east4",
    configuration: {
        numberOfNodes: 1,
        nodeConfiguration: {
            packageId: "3920d1eb-d3eb-4117-9578-b12d89bb1c5d"
        }
    },
    accountId: "<ACCOUNT_ID>"
})

```

```java
import com.pulumi.qdrantcloud.AccountsClusterArgs;
import com.pulumi.qdrantcloud.inputs.AccountsClusterConfigurationArgs;
import com.pulumi.qdrantcloud.inputs.AccountsClusterConfigurationNodeConfigurationArgs;

new AccountsCluster("pl-example-cluster-resource", AccountsClusterArgs.builder()
        .name("pl-example-cluster")
        .cloudProvider("gcp")
        .cloudRegion("us-east4")
        .configuration(AccountsClusterConfigurationArgs.builder()
                .numberOfNodes(1.0)
                .nodeConfiguration(AccountsClusterConfigurationNodeConfigurationArgs.builder()
                        .packageId("3920d1eb-d3eb-4117-9578-b12d89bb1c5d")
                        .build())
                .build())
        .accountId("<ACCOUNT_ID>")
        .build());

```

- `qdrant-cloud_accounts_auth_key` \- Create API keys for Qdrant cloud clusters. [Reference](https://github.com/qdrant/terraform-provider-qdrant-cloud/blob/main/docs/resources/accounts_auth_key.md)

pythontypescriptjava

```python
qdrant_cloud.AccountsAuthKey(
    resource_name="pl-example-key-resource",
    cluster_ids=["<CLUSTER_ID>"],
)

```

```typescript
new qdrantCloud.AccountsAuthKey("pl-example-cluster-resource", {
    clusterIds: ["<CLUSTER_ID>", "<CLUSTER_ID_2>"]
})

```

```java
import com.pulumi.qdrantcloud.AccountsAuthKey;
import com.pulumi.qdrantcloud.AccountsAuthKeyArgs;

new AccountsAuthKey("pl-example-key-resource", AccountsAuthKeyArgs.builder()
        .clusterIds("<CLUSTER_ID>", "<CLUSTER_ID_2>")
        .build());

```

## [Anchor](https://qdrant.tech/documentation/cloud-tools/pulumi/\#further-reading) Further Reading

- [Provider Documentation](https://registry.terraform.io/providers/qdrant/qdrant-cloud/latest/docs)
- [Pulumi Quickstart](https://www.pulumi.com/docs/get-started/)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-tools/pulumi.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-tools/pulumi.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574691153&cv=11&fst=1748574691153&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fpulumi%2F&hn=www.googleadservices.com&frm=0&tiba=Pulumi%20-%20Qdrant&npa=0&pscdl=noapi&auid=1315860486.1748574691&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574691130&cv=11&fst=1748574691130&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fpulumi%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Pulumi%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1315860486.1748574691&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d4c0fe16-506a-41c7-934c-668702ffef6b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=646dd381-0f6c-4450-a666-897fd6bf1a9b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fpulumi%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d4c0fe16-506a-41c7-934c-668702ffef6b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=646dd381-0f6c-4450-a666-897fd6bf1a9b&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fpulumi%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574692333&cv=11&fst=1748574692333&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103155~103103157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-tools%2Fpulumi%2F&hn=www.googleadservices.com&frm=0&tiba=Pulumi%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1315860486.1748574691&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)