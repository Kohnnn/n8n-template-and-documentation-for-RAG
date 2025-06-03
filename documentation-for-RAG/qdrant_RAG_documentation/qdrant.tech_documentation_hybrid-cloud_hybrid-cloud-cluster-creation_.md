---
url: "https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/"
title: "Create a Cluster - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Hybrid cloud](https://qdrant.tech/documentation/hybrid-cloud/)
- Create a Cluster

# [Anchor](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/\#creating-a-qdrant-cluster-in-hybrid-cloud) Creating a Qdrant Cluster in Hybrid Cloud

Once you have created a Hybrid Cloud Environment, you can create a Qdrant cluster in that enviroment. Use the same process to [Create a cluster](https://qdrant.tech/documentation/cloud/create-cluster/). Make sure to select your Hybrid Cloud Environment as the target.

![Create Hybrid Cloud Cluster](https://qdrant.tech/documentation/cloud/hybrid_cloud_create_cluster.png)

Note that in the “Kubernetes Configuration” section you can additionally configure:

- Node selectors for the Qdrant database pods
- Toleration for the Qdrant database pods
- Additional labels for the Qdrant database pods
- A service type and annotations for the Qdrant database service

These settings can also be changed after the cluster is created on the cluster detail page.

![Create Hybrid Cloud Cluster - Kubernetes Configuration](https://qdrant.tech/documentation/cloud/hybrid_cloud_kubernetes_configuration.png)

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/\#scheduling-configuration) Scheduling Configuration

When creating or editing a cluster, you can configure how the database Pods get scheduled in your Kubernetes cluster. This can be useful to ensure that the Qdrant databases will run on dedicated nodes. You can configure the necessary node selectors and tolerations in the “Kubernetes Configuration” section during cluster creation, or on the cluster detail page.

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/\#authentication-to-your-qdrant-clusters) Authentication to your Qdrant Clusters

In Hybrid Cloud the authentication information is provided by Kubernetes secrets.

You can configure authentication for your Qdrant clusters in the “Configuration” section of the Qdrant Cluster detail page. There you can configure the Kubernetes secret name and key to be used as an API key and/or read-only API key.

![Hybrid Cloud API Key configuration](https://qdrant.tech/documentation/cloud/hybrid_cloud_api_key.png)

One way to create a secret is with kubectl:

```shell
kubectl create secret generic qdrant-api-key --from-literal=api-key=your-secret-api-key --namespace the-qdrant-namespace

```

The resulting secret will look like this:

```yaml
apiVersion: v1
data:
  api-key: ...
kind: Secret
metadata:
  name: qdrant-api-key
  namespace: the-qdrant-namespace
type: kubernetes.io/generic

```

With this command the secret name would be `qdrant-api-key` and the key would be `api-key`.

If you want to retrieve the secret again, you can also use `kubectl`:

```shell
kubectl get secret qdrant-api-key -o jsonpath="{.data.api-key}" --namespace the-qdrant-namespace | base64 --decode

```

#### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/\#watch-the-video) Watch the Video

In this tutorial, we walk you through the steps to expose your Qdrant database cluster running on Qdrant Hybrid Cloud to external applications or users outside your Kubernetes cluster. Learn how to configure TLS certificates for secure communication, set up authentication, and explore different methods like load balancers, ingress, and port configurations.

How to Securely Expose Qdrant on Hybrid Cloud to External Applications - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[How to Securely Expose Qdrant on Hybrid Cloud to External Applications](https://www.youtube.com/watch?v=ikofKaUc4x0)

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

[Watch on](https://www.youtube.com/watch?v=ikofKaUc4x0&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 9:40
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=ikofKaUc4x0 "Watch on YouTube")

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/\#exposing-qdrant-clusters-to-your-client-applications) Exposing Qdrant clusters to your client applications

You can expose your Qdrant clusters to your client applications using Kubernetes services and ingresses. By default, a `ClusterIP` service is created for each Qdrant cluster.

Within your Kubernetes cluster, you can access the Qdrant cluster using the service name and port:

```
http://qdrant-9a9f48c7-bb90-4fb2-816f-418a46a74b24.qdrant-namespace.svc:6333

```

This endpoint is also visible on the cluster detail page.

If you want to access the database from your local developer machine, you can use `kubectl port-forward` to forward the service port to your local machine:

```
kubectl --namespace your-qdrant-namespace port-forward service/qdrant-9a9f48c7-bb90-4fb2-816f-418a46a74b24 6333:6333

```

You can also expose the database outside the Kubernetes cluster with a `LoadBalancer` (if supported in your Kubernetes environment) or `NodePort` service or an ingress.

The service type and necessary annotations can be configured in the “Kubernetes Configuration” section during cluster creation, or on the cluster detail page.

![Hybrid Cloud API Key configuration](https://qdrant.tech/documentation/cloud/hybrid_cloud_service.png)

Especially if you create a LoadBalancer Service, you may need to provide annotations for the loadbalancer configration. Please refer to the documention of your cloud provider for more details.

Examples:

- [AWS EKS LoadBalancer annotations](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/annotations/)
- [Azure AKS Public LoadBalancer annotations](https://learn.microsoft.com/en-us/azure/aks/load-balancer-standard)
- [Azure AKS Internal LoadBalancer annotations](https://learn.microsoft.com/en-us/azure/aks/internal-lb)
- [GCP GKE LoadBalancer annotations](https://cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters)

You could also create a Loadbalancer service manually like this:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: qdrant-9a9f48c7-bb90-4fb2-816f-418a46a74b24-lb
  namespace: qdrant-namespace
spec:
  type: LoadBalancer
  ports:
  - name: http
    port: 6333
  - name: grpc
    port: 6334
  selector:
    app: qdrant
    cluster-id: 9a9f48c7-bb90-4fb2-816f-418a46a74b24

```

An ingress could look like this:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: qdrant-9a9f48c7-bb90-4fb2-816f-418a46a74b24
  namespace: qdrant-namespace
spec:
    rules:
    - host: qdrant-9a9f48c7-bb90-4fb2-816f-418a46a74b24.your-domain.com
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: qdrant-9a9f48c7-bb90-4fb2-816f-418a46a74b24
              port:
                number: 6333

```

Please refer to the Kubernetes, ingress controller and cloud provider documentation for more details.

If you expose the database like this, you will be able to see this also reflected as an endpoint on the cluster detail page. And will see the Qdrant database dashboard link pointing to it.

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/\#configuring-tls) Configuring TLS

If you want to configure TLS for accessing your Qdrant database in Hybrid Cloud, there are two options:

- You can offload TLS at the ingress or loadbalancer level.
- You can configure TLS directly in the Qdrant database.

If you want to offload TLS at the ingress or loadbancer level, please refer to their respective documents.

If you want to configure TLS directly in the Qdrant database, you can reference a secret containing the TLS certificate and key in the “Configuration” section of the Qdrant Cluster detail page.

![Hybrid Cloud API Key configuration](https://qdrant.tech/documentation/cloud/hybrid_cloud_tls.png)

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

With this command the secret name to enter into the UI would be `qdrant-tls` and the keys would be `tls.crt` and `tls.key`.

### [Anchor](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/\#configuring-cpu-and-memory-resource-reservations) Configuring CPU and memory resource reservations

When creating a Qdrant database cluster, Qdrant Cloud schedules Pods with specific CPU and memory requests and limits to ensure optimal performance. It will use equal requests and limits for stability. Ideally, Kubernetes nodes should match the Pod size, with one database Pod per VM.

By default, Qdrant Cloud will reserve 20% of available CPU and memory on each Pod. This is done to leave room for the operating system, Kubernetes, and system components. This conservative default may need adjustment depending on node size, whereby smaller nodes might require more, and larger nodes less resources reserved.

You can modify this reservation in the “Configuration” section of the Qdrant Cluster detail page.

If you want to check how much resources are availabe on an empty Kubernetes node, you can use the following command:

```shell
kubectl describe node <node-name>

```

This will give you a breakdown of the available resources to Kubernetes and how much is already reserved and used for system Pods.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/hybrid-cloud-cluster-creation.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/hybrid-cloud-cluster-creation.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=604d5182-4269-4ed0-88fe-1aef6c25024d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=053f1f0b-213e-484f-8602-7d3f61eaf98d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Fhybrid-cloud-cluster-creation%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=604d5182-4269-4ed0-88fe-1aef6c25024d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=053f1f0b-213e-484f-8602-7d3f61eaf98d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Fhybrid-cloud-cluster-creation%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)