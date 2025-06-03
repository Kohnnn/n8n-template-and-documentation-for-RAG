---
url: "https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/"
title: "Managing a Cluster - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Private cloud](https://qdrant.tech/documentation/private-cloud/)
- Managing a Cluster

# [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#managing-a-qdrant-cluster) Managing a Qdrant Cluster

The most minimal QdrantCluster configuration is:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantCluster
metadata:
  name: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  version: "v1.11.3"
  size: 1
  resources:
    cpu: 100m
    memory: "1Gi"
    storage: "2Gi"

```

The `id` should be unique across all Qdrant clusters in the same namespace, the `name` must follow the above pattern and the `cluster-id` and `customer-id` labels are mandatory.

There are lots more configuration options to configure scheduling, security, networking, and more. For full details see the [Qdrant Private Cloud API Reference](https://qdrant.tech/documentation/private-cloud/api-reference/).

## [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#scaling-a-cluster) Scaling a Cluster

To scale a cluster, update the CPU, memory and storage resources in the QdrantCluster spec. The Qdrant operator will automatically adjust the cluster configuration. This operation is highly available on a multi-node cluster with replicated collections.

## [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#upgrading-the-qdrant-version) Upgrading the Qdrant version

To upgrade the Qdrant version of a database cluster, update the `version` field in the QdrantCluster spec. The Qdrant operator will automatically upgrade the cluster to the new version. The upgrade process is highly available on a multi-node cluster with replicated collections.

Note, that you should not skip minor versions when upgrading. For example, if you are running version `v1.11.3`, you can upgrade to `v1.11.5` or `v1.12.6`, but not directly to `v1.13.0`.

## [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#exposing-a-cluster) Exposing a Cluster

By default, a QdrantCluster will be exposed through an internal `ClusterIP` service. To expose the cluster to the outside world, you can create a `NodePort` service, a `LoadBalancer` service or an `Ingress` resource.

This is an example on how to create a QdrantCluster with a `LoadBalancer` service:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantCluster
metadata:
  name: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  version: "v1.11.3"
  size: 1
  resources:
    cpu: 100m
    memory: "1Gi"
    storage: "2Gi"
  service:
    type: LoadBalancer
    annotations:
      service.beta.kubernetes.io/aws-load-balancer-type: nlb

```

Especially if you create a LoadBalancer Service, you may need to provide annotations for the loadbalancer configration. Please refer to the documention of your cloud provider for more details.

Examples:

- [AWS EKS LoadBalancer annotations](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/annotations/)
- [Azure AKS Public LoadBalancer annotations](https://learn.microsoft.com/en-us/azure/aks/load-balancer-standard)
- [Azure AKS Internal LoadBalancer annotations](https://learn.microsoft.com/en-us/azure/aks/internal-lb)
- [GCP GKE LoadBalancer annotations](https://cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters)

## [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#authentication-and-authorization) Authentication and Authorization

Authentication information is provided by Kubernetes secrets.

One way to create a secret is with kubectl:

```shell
kubectl create secret generic qdrant-api-key --from-literal=api-key=your-secret-api-key --from-literal=read-only-api-key=your-secret-read-only-api-key --namespace qdrant-private-cloud

```

The resulting secret will look like this:

```yaml
apiVersion: v1
data:
  api-key: ...
  read-only-api-key: ...
kind: Secret
metadata:
  name: qdrant-api-key
  namespace: qdrant-private-cloud
type: kubernetes.io/generic

```

You can reference the secret in the QdrantCluster spec:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantCluster
metadata:
  name: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  version: "v1.11.3"
  size: 1
  resources:
    cpu: 100m
    memory: "1Gi"
    storage: "2Gi"
  config:
    service:
      api_key:
        secretKeyRef:
          name: qdrant-api-key
          key: api-key
      read_only_api_key:
        secretKeyRef:
          name: qdrant-api-key
          key: read-only-api-key
      jwt_rbac: true

```

If you set the `jwt_rbac` flag, you will also be able to create granular [JWT tokens for role based access control](https://qdrant.tech/documentation/guides/security/#granular-access-control-with-jwt).

### [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#configuring-tls-for-database-access) Configuring TLS for Database Access

If you want to configure TLS for accessing your Qdrant database, there are two options:

- You can offload TLS at the ingress or loadbalancer level.
- You can configure TLS directly in the Qdrant database.

If you want to configure TLS directly in the Qdrant database, you can provide this as a secret.

To create such a secret, you can use `kubectl`:

```shell
 kubectl create secret tls qdrant-tls --cert=mydomain.com.crt --key=mydomain.com.key --namespace the-qdrant-namespace

```

The resulting secret will look like this:

```yaml
apiVersion: v1
data:
  tls.crt: ...
  tls.key: ...
kind: Secret
metadata:
  name: qdrant-tls
  namespace: the-qdrant-namespace
type: kubernetes.io/tls

```

You can reference the secret in the QdrantCluster spec:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantCluster
metadata:
  name: test-cluster
spec:
  id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  version: "v1.11.3"
  size: 1
  resources:
    cpu: 100m
    memory: "1Gi"
    storage: "2Gi"
  config:
    service:
      enable_tls: true
    tls:
      cert:
        secretKeyRef:
          name: qdrant-tls
          key: tls.crt
      key:
        secretKeyRef:
          name: qdrant-tls
          key: tls.key

```

### [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#configuring-tls-for-inter-cluster-communication) Configuring TLS for Inter-cluster Communication

_Available as of Operator v2.2.0_

If you want to encrypt communication between Qdrant nodes, you need to enable TLS by providing
certificate, key, and root CA certificate used for generating the former.

Similar to the instruction stated in the previous section, you need to create a secret:

```shell
 kubectl create secret generic qdrant-p2p-tls \
        --from-file=tls.crt=qdrant-nodes.crt \
        --from-file=tls.key=qdrant-nodes.key \
        --from-file=ca.crt=root-ca.crt
        --namespace the-qdrant-namespace

```

The resulting secret will look like this:

```yaml
apiVersion: v1
data:
  tls.crt: ...
  tls.key: ...
  ca.crt: ...
kind: Secret
metadata:
  name: qdrant-p2p-tls
  namespace: the-qdrant-namespace
type: Opaque

```

You can reference the secret in the QdrantCluster spec:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantCluster
metadata:
  name: test-cluster
  labels:
    cluster-id: "my-cluster"
    customer-id: "acme-industries"
spec:
  id: "my-cluster"
  version: "v1.13.3"
  size: 2
  resources:
    cpu: 100m
    memory: "1Gi"
    storage: "2Gi"
  config:
    service:
      enable_tls: true
    tls:
      caCert:
        secretKeyRef:
          name: qdrant-p2p-tls
          key: ca.crt
      cert:
        secretKeyRef:
          name: qdrant-p2p-tls
          key: tls.crt
      key:
        secretKeyRef:
          name: qdrant-p2p-tls
          key: tls.key

```

## [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#gpu-support) GPU support

Starting with Qdrant 1.13 and private-cloud version 1.6.1 you can create a cluster that uses GPUs to accelarate indexing.

As a prerequisite, you need to have a Kubernetes cluster with GPU support. You can check the [Kubernetes documentation](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) for generic information on GPUs and Kubernetes, or the documentation of your specific Kubernetes distribution.

Examples:

- [AWS EKS GPU support](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/amazon-eks.html)
- [Azure AKS GPU support](https://docs.microsoft.com/en-us/azure/aks/gpu-cluster)
- [GCP GKE GPU support](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus)
- [Vultr Kubernetes GPU support](https://blogs.vultr.com/whats-new-vultr-q2-2023)

Once you have a Kubernetes cluster with GPU support, you can create a QdrantCluster with GPU support:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantCluster
metadata:
  name: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  version: "v1.13.4"
  size: 1
  resources:
    cpu: 2
    memory: "8Gi"
    storage: "40Gi"
  gpu:
    gpuType: "nvidia"

```

Once the cluster Pod has started, you can check in the logs if the GPU is detected:

```shell
$ kubectl logs qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-0

Starting initializing for pod 0
           _                 _
  __ _  __| |_ __ __ _ _ __ | |_
 / _` |/ _` | '__/ _` | '_ \| __|
| (_| | (_| | | | (_| | | | | |_
 \__, |\__,_|_|  \__,_|_| |_|\__|
    |_|

Version: 1.13.4, build: 7abc6843
Access web UI at http://localhost:6333/dashboard

2025-03-14T10:25:30.509636Z  INFO gpu::instance: Found GPU device: NVIDIA A16-2Q
2025-03-14T10:25:30.509679Z  INFO gpu::instance: Found GPU device: llvmpipe (LLVM 15.0.7, 256 bits)
2025-03-14T10:25:30.509734Z  INFO gpu::device: Create GPU device NVIDIA A16-2Q
...

```

For more GPU configuration options, see the [Qdrant Private Cloud API Reference](https://qdrant.tech/documentation/private-cloud/api-reference/).

## [Anchor](https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/\#ephemeral-snapshot-volumes) Ephemeral Snapshot Volumes

If you do not [create snapshots](https://api.qdrant.tech/api-reference/snapshots/create-snapshot), or there is no need
to keep them available after cluster restart, the snapshot storage classname can be set to `emptyDir`:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantCluster
metadata:
  name: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  version: "v1.13.4"
  size: 1
  resources:
    cpu: 2
    memory: "8Gi"
    storage: "40Gi"
  storageClassNames:
    snapshots: emptyDir

```

See [Kubernetes docs on emptyDir volumes](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) for more details,
on how k8s node ephemeral storage is allocated and used.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/qdrant-cluster-management.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/qdrant-cluster-management.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0d5c91da-d916-468d-94b3-a6df4b6d7f2c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=462276a5-3275-4ed3-9e08-1d8600360cc9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fqdrant-cluster-management%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573943524&cv=11&fst=1748573943524&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103158~103103160~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fqdrant-cluster-management%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Managing%20a%20Cluster%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=468434258.1748573941&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573943561&cv=11&fst=1748573943561&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103158~103103160~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fqdrant-cluster-management%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Managing%20a%20Cluster%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=468434258.1748573941&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573943465&cv=11&fst=1748573943465&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103103158~103103160~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fqdrant-cluster-management%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Managing%20a%20Cluster%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=468434258.1748573941&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0d5c91da-d916-468d-94b3-a6df4b6d7f2c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=462276a5-3275-4ed3-9e08-1d8600360cc9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fqdrant-cluster-management%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)