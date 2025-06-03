---
url: "https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/"
title: "Deployment Platforms - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Hybrid cloud](https://qdrant.tech/documentation/hybrid-cloud/)
- Deployment Platforms

# [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#qdrant-hybrid-cloud-hosting-platforms--deployment-options) Qdrant Hybrid Cloud: Hosting Platforms & Deployment Options

This page provides an overview of how to deploy Qdrant Hybrid Cloud on various managed Kubernetes platforms.

For a general list of prerequisites and installation steps, see our [Hybrid Cloud setup guide](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/). This platform specific documentation also applies to Qdrant Private Cloud.

![Akamai](https://qdrant.tech/documentation/cloud/cloud-providers/akamai.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#akamai-linode) Akamai (Linode)

[The Linode Kubernetes Engine (LKE)](https://www.linode.com/products/kubernetes/) is a managed container orchestration engine built on top of Kubernetes. LKE enables you to quickly deploy and manage your containerized applications without needing to build (and maintain) your own Kubernetes cluster. All LKE instances are equipped with a fully managed control plane at no additional cost.

First, consult Linode’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on LKE**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-linode-kubernetes-engine) More on Linode Kubernetes Engine

- [Getting Started with LKE](https://www.linode.com/docs/products/compute/kubernetes/get-started/)
- [LKE Guides](https://www.linode.com/docs/products/compute/kubernetes/guides/)
- [LKE API Reference](https://www.linode.com/docs/api/)

At the time of writing, Linode [does not support CSI Volume Snapshots](https://github.com/linode/linode-blockstorage-csi-driver/issues/107).

![AWS](https://qdrant.tech/documentation/cloud/cloud-providers/aws.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#amazon-web-services-aws) Amazon Web Services (AWS)

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) is a managed service to run Kubernetes in the AWS cloud and on-premises data centers which can then be paired with Qdrant’s hybrid cloud. With Amazon EKS, you can take advantage of all the performance, scale, reliability, and availability of AWS infrastructure, as well as integrations with AWS networking and security services.

First, consult AWS’ managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on AWS**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

For a good balance between peformance and cost, we recommend:

- Depending on your cluster resource configuration either general purpose (m6\*, m7\*, or m8\*), memory optimized (r6\*, r7\*, or r8\*) or cpu optimized (c6\*, c7\*, or c8\*) instance types. Qdrant Hybrid Cloud also supports AWS Graviton ARM64 instances.
- At least gp3 EBS volumes for storage

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-amazon-elastic-kubernetes-service) More on Amazon Elastic Kubernetes Service

- [Getting Started with Amazon EKS](https://docs.aws.amazon.com/eks/)
- [Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- [Amazon EKS API Reference](https://docs.aws.amazon.com/eks/latest/APIReference/Welcome.html)

Your EKS cluster needs the EKS EBS CSI driver or a similar storage driver:

- [Amazon EBS CSI Driver](https://docs.aws.amazon.com/eks/latest/userguide/managing-ebs-csi.html)

To allow vertical scaling, you need a StorageClass with volume expansion enabled:

- [Amazon EBS CSI Volume Resizing](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/examples/kubernetes/resizing/README.md)

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
  name: ebs-sc
provisioner: ebs.csi.aws.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true

```

To allow backups and restores, your EKS cluster needs the CSI snapshot controller:

- [Amazon EBS CSI Snapshot Controller](https://docs.aws.amazon.com/eks/latest/userguide/csi-snapshot-controller.html)

And you need to create a VolumeSnapshotClass:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-snapclass
deletionPolicy: Delete
driver: ebs.csi.aws.com

```

![Civo](https://qdrant.tech/documentation/cloud/cloud-providers/civo.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#civo) Civo

[Civo Kubernetes](https://www.civo.com/kubernetes) is a robust, scalable, and managed Kubernetes service. Civo supplies a CNCF-compliant Kubernetes cluster and makes it easy to provide standard Kubernetes applications and containerized workloads. User-defined Kubernetes clusters can be created as self-service without complications using the Civo Portal.

First, consult Civo’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on Civo**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-civo-kubernetes) More on Civo Kubernetes

- [Getting Started with Civo Kubernetes](https://www.civo.com/docs/kubernetes)
- [Civo Tutorials](https://www.civo.com/learn)
- [Frequently Asked Questions on Civo](https://www.civo.com/docs/faq)

To allow backups and restores, you need to create a VolumeSnapshotClass:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-snapclass
deletionPolicy: Delete
driver: csi.civo.com

```

![Digital Ocean](https://qdrant.tech/documentation/cloud/cloud-providers/digital-ocean.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#digital-ocean) Digital Ocean

[DigitalOcean Kubernetes (DOKS)](https://www.digitalocean.com/products/kubernetes) is a managed Kubernetes service that lets you deploy Kubernetes clusters without the complexities of handling the control plane and containerized infrastructure. Clusters are compatible with standard Kubernetes toolchains and integrate natively with DigitalOcean Load Balancers and volumes.

First, consult Digital Ocean’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on DigitalOcean**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-digitalocean-kubernetes) More on DigitalOcean Kubernetes

- [Getting Started with DOKS](https://docs.digitalocean.com/products/kubernetes/getting-started/quickstart/)
- [DOKS - How To Guides](https://docs.digitalocean.com/products/kubernetes/how-to/)
- [DOKS - Reference Manual](https://docs.digitalocean.com/products/kubernetes/reference/)

![Gcore](https://qdrant.tech/documentation/cloud/cloud-providers/gcore.svg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#gcore) Gcore

[Gcore Managed Kubernetes](https://gcore.com/cloud/managed-kubernetes) is a managed container orchestration engine built on top of Kubernetes. Gcore enables you to quickly deploy and manage your containerized applications without needing to build (and maintain) your own Kubernetes cluster. All Gcore instances are equipped with a fully managed control plane at no additional cost.

First, consult Gcore’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on Gcore**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-gcore-kubernetes-engine) More on Gcore Kubernetes Engine

- [Getting Started with Kubnetes on Gcore](https://gcore.com/docs/cloud/kubernetes/about-gcore-kubernetes)

![Google Cloud Platform](https://qdrant.tech/documentation/cloud/cloud-providers/gcp.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#google-cloud-platform-gcp) Google Cloud Platform (GCP)

[Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine) is a managed Kubernetes service that you can use to deploy and operate containerized applications at scale using Google’s infrastructure. GKE provides the operational power of Kubernetes while managing many of the underlying components, such as the control plane and nodes, for you.

First, consult GCP’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on GCP**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

For a good balance between peformance and cost, we recommend:

- Depending on your cluster resource configuration either general purpose (standard), memory optimized (highmem) or cpu optimized (highcpu) instance types of at least 2nd generation. Qdrant Hybrid Cloud also supports ARM64 instances.
- At least pd-balanced disks for storage

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-the-google-kubernetes-engine) More on the Google Kubernetes Engine

- [Getting Started with GKE](https://cloud.google.com/kubernetes-engine/docs/quickstart)
- [GKE Tutorials](https://cloud.google.com/kubernetes-engine/docs/tutorials)
- [GKE Documentation](https://cloud.google.com/kubernetes-engine/docs/)

To allow backups and restores, your GKE cluster needs the CSI VolumeSnapshot controller and class:

- [Google GKE Volume Snapshots](https://cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots)

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-snapclass
deletionPolicy: Delete
driver: pd.csi.storage.gke.io

```

![Microsoft Azure](https://qdrant.tech/documentation/cloud/cloud-providers/azure.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#mircrosoft-azure) Mircrosoft Azure

With [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-in/products/kubernetes-service), you can start developing and deploying cloud-native apps in Azure, data centres, or at the edge. Get unified management and governance for on-premises, edge, and multi-cloud Kubernetes clusters. Interoperate with Azure security, identity, cost management, and migration services.

First, consult Azure’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on Azure**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

For a good balance between peformance and cost, we recommend:

- Depending on your cluster resource configuration either general purpose (D-family), memory optimized (E-family) or cpu optimized (F-family) instance types. Qdrant Hybrid Cloud also supports Azure Cobalt ARM64 instances.
- At least Premium SSD v2 disks for storage

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-azure-kubernetes-service) More on Azure Kubernetes Service

- [Getting Started with AKS](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-start-here)
- [AKS Documentation](https://learn.microsoft.com/en-in/azure/aks/)
- [Best Practices with AKS](https://learn.microsoft.com/en-in/azure/aks/best-practices)

To allow backups and restores, your AKS cluster needs the CSI VolumeSnapshot controller and class:

- [Azure AKS Volume Snapshots](https://learn.microsoft.com/en-us/azure/aks/azure-disk-csi#create-a-volume-snapshot)

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-snapclass
deletionPolicy: Delete
driver: disk.csi.azure.com

```

![Oracle Cloud Infrastructure](https://qdrant.tech/documentation/cloud/cloud-providers/oracle.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#oracle-cloud-infrastructure) Oracle Cloud Infrastructure

[Oracle Cloud Infrastructure Container Engine for Kubernetes (OKE)](https://www.oracle.com/in/cloud/cloud-native/container-engine-kubernetes/) is a managed Kubernetes solution that enables you to deploy Kubernetes clusters while ensuring stable operations for both the control plane and the worker nodes through automatic scaling, upgrades, and security patching. Additionally, OKE offers a completely serverless Kubernetes experience with virtual nodes.

First, consult OCI’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on OCI**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-oci-container-engine) More on OCI Container Engine

- [Getting Started with OCI](https://docs.oracle.com/en-us/iaas/Content/ContEng/home.htm)
- [Frequently Asked Questions on OCI](https://www.oracle.com/in/cloud/cloud-native/container-engine-kubernetes/faq/)
- [OCI Product Updates](https://docs.oracle.com/en-us/iaas/releasenotes/services/conteng/)

To allow backups and restores, your OCI cluster needs the CSI VolumeSnapshot controller and class:

- [Prerequisites for Creating Volume Snapshots](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_volume-snapshot-prerequisites)

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-snapclass
deletionPolicy: Delete
driver: blockvolume.csi.oraclecloud.com

```

![OVHcloud](https://qdrant.tech/documentation/cloud/cloud-providers/ovh.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#ovhcloud) OVHcloud

[Service Managed Kubernetes](https://www.ovhcloud.com/en-in/public-cloud/kubernetes/), powered by OVH Public Cloud Instances, a leading European cloud provider. With OVHcloud Load Balancers and disks built in. OVHcloud Managed Kubernetes provides high availability, compliance, and CNCF conformance, allowing you to focus on your containerized software layers with total reversibility.

First, consult OVHcloud’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on OVHcloud**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-service-managed-kubernetes-by-ovhcloud) More on Service Managed Kubernetes by OVHcloud

- [Getting Started with OVH Managed Kubernetes](https://help.ovhcloud.com/csm/en-in-documentation-public-cloud-containers-orchestration-managed-kubernetes-k8s-getting-started)
- [OVH Managed Kubernetes Documentation](https://help.ovhcloud.com/csm/en-in-documentation-public-cloud-containers-orchestration-managed-kubernetes-k8s)
- [OVH Managed Kubernetes Tutorials](https://help.ovhcloud.com/csm/en-in-documentation-public-cloud-containers-orchestration-managed-kubernetes-k8s-tutorials)

![Red Hat](https://qdrant.tech/documentation/cloud/cloud-providers/redhat.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#red-hat-openshift) Red Hat OpenShift

[Red Hat OpenShift Kubernetes Engine](https://www.redhat.com/en/technologies/cloud-computing/openshift/kubernetes-engine) provides you with the basic functionality of Red Hat OpenShift. It offers a subset of the features that Red Hat OpenShift Container Platform offers, like full access to an enterprise-ready Kubernetes environment and an extensive compatibility test matrix with many of the software elements that you might use in your data centre.

First, consult Red Hat’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on Red Hat OpenShift**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-openshift-kubernetes-engine) More on OpenShift Kubernetes Engine

- [Getting Started with Red Hat OpenShift Kubernetes](https://docs.openshift.com/container-platform/4.15/getting_started/kubernetes-overview.html)
- [Red Hat OpenShift Kubernetes Documentation](https://docs.openshift.com/container-platform/4.15/welcome/index.html)
- [Installing on Container Platforms](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.5/html/installing/index)

Qdrant databases need a persistent storage solution. See [Openshift Storage Overview](https://docs.openshift.com/container-platform/4.15/storage/index.html).

To allow vertical scaling, you need a StorageClass with [volume expansion enabled](https://docs.openshift.com/container-platform/4.15/storage/expanding-persistent-volumes.html).

To allow backups and restores, your OpenShift cluster needs the [CSI snapshot controller](https://docs.openshift.com/container-platform/4.15/storage/container_storage_interface/persistent-storage-csi-snapshots.html), and you need to create a VolumeSnapshotClass.

![Scaleway](https://qdrant.tech/documentation/cloud/cloud-providers/scaleway.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#scaleway) Scaleway

[Scaleway Kapsule](https://www.scaleway.com/en/kubernetes-kapsule/) and [Kosmos](https://www.scaleway.com/en/kubernetes-kosmos/) are managed Kubernetes services from [Scaleway](https://www.scaleway.com/en/). They abstract away the complexities of managing and operating a Kubernetes cluster. The primary difference being, Kapsule clusters are composed solely of Scaleway Instances. Whereas, a Kosmos cluster is a managed multi-cloud Kubernetes engine that allows you to connect instances from any cloud provider to a single managed Control-Plane.

First, consult Scaleway’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on Scaleway**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-scaleway-kubernetes) More on Scaleway Kubernetes

- [Getting Started with Scaleway Kubernetes](https://www.scaleway.com/en/docs/containers/kubernetes/quickstart/#how-to-add-a-scaleway-pool-to-a-kubernetes-cluster)
- [Scaleway Kubernetes Documentation](https://www.scaleway.com/en/docs/containers/kubernetes/)
- [Frequently Asked Questions on Scaleway Kubernetes](https://www.scaleway.com/en/docs/faq/kubernetes/)

![STACKIT](https://qdrant.tech/documentation/cloud/cloud-providers/stackit.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#stackit) STACKIT

[STACKIT Kubernetes Engine (SKE)](https://www.stackit.de/en/product/kubernetes/) is a robust, scalable, and managed Kubernetes service. SKE supplies a CNCF-compliant Kubernetes cluster and makes it easy to provide standard Kubernetes applications and containerized workloads. User-defined Kubernetes clusters can be created as self-service without complications using the STACKIT Portal.

First, consult STACKIT’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on STACKIT**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-stackit-kubernetes-engine) More on STACKIT Kubernetes Engine

- [Getting Started with SKE](https://docs.stackit.cloud/stackit/en/getting-started-ske-10125565.html)
- [SKE Tutorials](https://docs.stackit.cloud/stackit/en/tutorials-ske-66683162.html)
- [Frequently Asked Questions on SKE](https://docs.stackit.cloud/stackit/en/faq-known-issues-of-ske-28476393.html)

To allow backups and restores, you need to create a VolumeSnapshotClass:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-snapclass
deletionPolicy: Delete
driver: cinder.csi.openstack.org

```

![Vultr](https://qdrant.tech/documentation/cloud/cloud-providers/vultr.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#vultr) Vultr

[Vultr Kubernetes Engine (VKE)](https://www.vultr.com/kubernetes/) is a fully-managed product offering with predictable pricing that makes Kubernetes easy to use. Vultr manages the control plane and worker nodes and provides integration with other managed services such as Load Balancers, Block Storage, and DNS.

First, consult Vultr’s managed Kubernetes instructions below. Then, **to set up Qdrant Hybrid Cloud on Vultr**, follow our [step-by-step documentation](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#more-on-vultr-kubernetes-engine) More on Vultr Kubernetes Engine

- [VKE Guide](https://docs.vultr.com/vultr-kubernetes-engine)
- [VKE Documentation](https://docs.vultr.com/)
- [Frequently Asked Questions on VKE](https://docs.vultr.com/vultr-kubernetes-engine#frequently-asked-questions)

At the time of writing, Vultr does not support CSI Volume Snapshots.

![Kubernetes](https://qdrant.tech/documentation/cloud/cloud-providers/kubernetes.jpg)

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#generic-kubernetes-support-on-premises-cloud-edge) Generic Kubernetes Support (on-premises, cloud, edge)

Qdrant Hybrid Cloud works with any Kubernetes cluster that meets the [standard compliance](https://www.cncf.io/training/certification/software-conformance/) requirements.

This includes for example:

- [VMWare Tanzu](https://tanzu.vmware.com/kubernetes-grid)
- [Red Hat OpenShift](https://www.openshift.com/)
- [SUSE Rancher](https://www.rancher.com/)
- [Canonical Kubernetes](https://ubuntu.com/kubernetes)
- [RKE](https://rancher.com/docs/rke/latest/en/)
- [RKE2](https://docs.rke2.io/)
- [K3s](https://k3s.io/)

Qdrant databases need persistent block storage. Most storage solutions provide a CSI driver that can be used with Kubernetes. See [CSI drivers](https://kubernetes-csi.github.io/docs/drivers.html) for more information.

To allow vertical scaling, you need a StorageClass with volume expansion enabled. See [Volume Expansion](https://kubernetes.io/docs/concepts/storage/storage-classes/#allow-volume-expansion) for more information.

To allow backups and restores, your CSI driver needs to support volume snapshots cluster needs the CSI VolumeSnapshot controller and class. See [CSI Volume Snapshots](https://kubernetes-csi.github.io/docs/snapshot-controller.html) for more information.

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/\#next-steps) Next Steps

Once you’ve got a Kubernetes cluster deployed on a platform of your choosing, you can begin setting up Qdrant Hybrid Cloud. Head to our Qdrant Hybrid Cloud [setup guide](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/) for instructions.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/platform-deployment-options.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/platform-deployment-options.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574863542&cv=11&fst=1748574863542&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Fplatform-deployment-options%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Deployment%20Platforms%20-%20Qdrant&npa=0&pscdl=noapi&auid=2116791980.1748574863&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574863523&cv=11&fst=1748574863523&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Fplatform-deployment-options%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Deployment%20Platforms%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2116791980.1748574863&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f121bae6-9d17-4e91-a570-3729cf969365&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8017f11e-4b85-4ed6-b0d1-b8ff76276e56&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Fplatform-deployment-options%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f121bae6-9d17-4e91-a570-3729cf969365&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8017f11e-4b85-4ed6-b0d1-b8ff76276e56&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Fplatform-deployment-options%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574864874&cv=11&fst=1748574864874&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Fplatform-deployment-options%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Deployment%20Platforms%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2116791980.1748574863&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)