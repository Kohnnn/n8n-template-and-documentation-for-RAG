---
url: "https://qdrant.tech/documentation/private-cloud/private-cloud-setup/"
title: "Setup Private Cloud - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Private cloud](https://qdrant.tech/documentation/private-cloud/)
- Setup Private Cloud

# [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#qdrant-private-cloud-setup) Qdrant Private Cloud Setup

## [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#requirements) Requirements

- **Kubernetes cluster:** To install Qdrant Private Cloud, you need a [standard compliant](https://www.cncf.io/training/certification/software-conformance/) Kubernetes cluster. You can run this cluster in any cloud, on-premise or edge environment, with distributions that range from AWS EKS to VMWare vSphere. See [Deployment Platforms](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/) for more information.
- **Storage:** For storage, you need to set up the Kubernetes cluster with a Container Storage Interface (CSI) driver that provides block storage. For vertical scaling, the CSI driver needs to support volume expansion. For backups and restores, the driver needs to support CSI snapshots and restores.

- **Permissions:** To install the Qdrant Kubernetes Operator you need to have `cluster-admin` access in your Kubernetes cluster.
- **Locations:** By default, the Qdrant Operator Helm charts and container images are served from `registry.cloud.qdrant.io`.

> **Note:** You can also mirror these images and charts into your own registry and pull them from there.

### [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#cli-tools) CLI tools

During the onboarding, you will need to deploy the Qdrant Kubernetes Operator using Helm. Make sure you have the following tools installed:

- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [helm](https://helm.sh/docs/intro/install/)

You will need to have access to the Kubernetes cluster with `kubectl` and `helm` configured to connect to it. Please refer the documentation of your Kubernetes distribution for more information.

### [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#required-artifacts) Required artifacts

Container images:

- `registry.cloud.qdrant.io/qdrant/qdrant`
- `registry.cloud.qdrant.io/qdrant/operator`
- `registry.cloud.qdrant.io/qdrant/cluster-manager`

Open Containers Initiative (OCI) Helm charts:

- `registry.cloud.qdrant.io/qdrant-charts/qdrant-private-cloud`
- `registry.cloud.qdrant.io/library/qdrant-kubernetes-api`

### [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#mirroring-images-and-charts) Mirroring images and charts

To mirror all necessary container images and Helm charts into your own registry, you can either use a replication feature that your registry provides, or you can manually sync the images with [Skopeo](https://github.com/containers/skopeo):

First login to the source registry:

```shell
skopeo login registry.cloud.qdrant.io

```

Then login to your own registry:

```shell
skopeo login your-registry.example.com

```

To sync all container images:

```shell
skopeo sync --all --src docker --dest docker registry.cloud.qdrant.io/qdrant/qdrant your-registry.example.com/qdrant/qdrant
skopeo sync --all --src docker --dest docker registry.cloud.qdrant.io/qdrant/cluster-manager your-registry.example.com/qdrant/cluster-manager
skopeo sync --all --src docker --dest docker registry.cloud.qdrant.io/qdrant/operator your-registry.example.com/qdrant/operator

```

To sync all helm charts:

```shell
skopeo sync --all --src docker --dest docker registry.cloud.qdrant.io/qdrant-charts/qdrant-private-cloud your-registry.example.com/qdrant-charts/qdrant-private-cloud
skopeo sync --all --src docker --dest docker registry.cloud.qdrant.io/qdrant-charts/qdrant-kubernetes-api your-registry.example.com/qdrant-charts/qdrant-kubernetes-api

```

During the installation or upgrade, you will need to adapt the repository information in the Helm chart values. See [Private Cloud Configuration](https://qdrant.tech/documentation/private-cloud/configuration/) for details.

## [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#installation-and-upgrades) Installation and Upgrades

Once you are onboarded to Qdrant Private Cloud, you will receive credentials to access the Qdrant Cloud Registry. You can use these credentials to install the Qdrant Private Cloud solution using the following commands. You can choose the Kubernetes namespace freely.

```bash
kubectl create namespace qdrant-private-cloud
kubectl create secret docker-registry qdrant-registry-creds --docker-server=registry.cloud.qdrant.io --docker-username='your-username' --docker-password='your-password' --namespace qdrant-private-cloud
helm registry login 'registry.cloud.qdrant.io' --username 'your-username' --password 'your-password'
helm upgrade --install qdrant-private-cloud-crds oci://registry.cloud.qdrant.io/qdrant-charts/qdrant-kubernetes-api --namespace qdrant-private-cloud --version v1.16.3 --wait
helm upgrade --install qdrant-private-cloud oci://registry.cloud.qdrant.io/qdrant-charts/qdrant-private-cloud --namespace qdrant-private-cloud --version 1.7.0

```

For a list of available versions consult the [Private Cloud Changelog](https://qdrant.tech/documentation/private-cloud/changelog/).

Current default versions are:

- qdrant-kubernetes-api v1.16.3
- qdrant-private-cloud 1.7.0

Especially ensure, that the default values to reference `StorageClasses` and the corresponding `VolumeSnapshotClass` are set correctly in your environment.

### [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#scope-of-the-operator) Scope of the operator

By default, the Qdrant Operator will only manage Qdrant clusters in the same Kubernetes namespace, where it is already deployed. The RoleBindings are also limited to this specific namespace. This default is chosen to limit the operator to the least amount of permissions necessary within a Kubernetes cluster.

If you want to manage Qdrant clusters in multiple namespaces with the same operator, you can either configure a list of namespaces that the operator should watch:

```yaml
operator:
  watch:
    # If true, watches only the namespace where the Qdrant operator is deployed, otherwise watches the namespaces in watch.namespaces
    onlyReleaseNamespace: false
    # an empty list watches all namespaces.
    namespaces:
      - qdrant-private-cloud
      - some-other-namespase
  limitRBAC: true

```

Or you can configure the operator to watch all namespaces:

```yaml
operator:
  watch:
    # If true, watches only the namespace where the Qdrant operator is deployed, otherwise watches the namespaces in watch.namespaces
    onlyReleaseNamespace: false
    # an empty list watches all namespaces.
    namespaces: []
  limitRBAC: false

```

## [Anchor](https://qdrant.tech/documentation/private-cloud/private-cloud-setup/\#uninstallation) Uninstallation

To uninstall the Qdrant Private Cloud solution, you can use the following command:

```bash
helm uninstall qdrant-private-cloud --namespace qdrant-private-cloud
helm uninstall qdrant-private-cloud-crds --namespace qdrant-private-cloud
kubectl delete namespace qdrant-private-cloud

```

Note that uninstalling the `qdrant-private-cloud-crds` Helm chart will remove all Custom Resource Definitions (CRDs) will also remove all Qdrant clusters that were managed by the operator.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/private-cloud-setup.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/private-cloud-setup.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574384272&cv=11&fst=1748574384272&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fprivate-cloud-setup%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Setup%20Private%20Cloud%20-%20Qdrant&npa=0&pscdl=noapi&auid=171225587.1748574384&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574384227&cv=11&fst=1748574384227&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fprivate-cloud-setup%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Setup%20Private%20Cloud%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=171225587.1748574384&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b7232a96-504f-4a43-a5f2-0d207d32ac44&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3c203c95-aa3b-4ba0-8aba-1758d6ec2643&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fprivate-cloud-setup%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b7232a96-504f-4a43-a5f2-0d207d32ac44&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3c203c95-aa3b-4ba0-8aba-1758d6ec2643&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fprivate-cloud-setup%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574385656&cv=11&fst=1748574385656&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fprivate-cloud-setup%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Setup%20Private%20Cloud%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=171225587.1748574384&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)