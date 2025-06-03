---
url: "https://qdrant.tech/documentation/hybrid-cloud/operator-configuration/"
title: "Configure the Qdrant Operator - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Hybrid cloud](https://qdrant.tech/documentation/hybrid-cloud/)
- Configure the Qdrant Operator

# [Anchor](https://qdrant.tech/documentation/hybrid-cloud/operator-configuration/\#configuring-qdrant-operator-advanced-options) Configuring Qdrant Operator: Advanced Options

The Qdrant Operator has several configuration options, which can be configured in the advanced section of your Hybrid Cloud Environment.

The following YAML shows all configuration options with their default values:

```yaml
# Additional pod annotations
podAnnotations: {}

# Configuration for the Qdrant operator service monitor to scrape metrics
serviceMonitor:
  enabled: false

# Resource requests and limits for the Qdrant operator
resources: {}

# Node selector for the Qdrant operator
nodeSelector: {}

# Tolerations for the Qdrant operator
tolerations: []

# Affinity configuration for the Qdrant operator
affinity: {}

# Configuration for the Qdrant operator (v2)
settings:
  # The log level for the operator
  # Available options: DEBUG | INFO | WARN | ERROR
  logLevel: INFO
  # Controller related settings
  controller:
    # The period a forced recync is done by the controller (if watches are missed / nothing happened)
    forceResyncPeriod: 10h
    # QPS indicates the maximum QPS to the master from this client.
    # Default is 200
    qps: 200
    # Maximum burst for throttle.
    # Default is 500.
    burst: 500
  # Features contains the settings for enabling / disabling the individual features of the operator
  features:
    # ClusterManagement contains the settings for qdrant (database) cluster management
    clusterManagement:
      # Whether or not the Qdrant cluster features are enabled.
      # If disabled, all other properties in this struct are disregarded. Otherwise, the individual features will be inspected.
      # Default is true.
      enable: true
      # The StorageClass used to make database and snapshot PVCs.
      # Default is nil, meaning the default storage class of Kubernetes.
      storageClass:
        # The StorageClass used to make database PVCs.
        # Default is nil, meaning the default storage class of Kubernetes.
        #database:
        # The StorageClass used to make snapshot PVCs.
        # Default is nil, meaning the default storage class of Kubernetes.
        #snapshot:
      # Qdrant config contains settings specific for the database
      qdrant:
        # The config where to find the image for qdrant
        image:
          # The repository where to find the image for qdrant
          # Default is "qdrant/qdrant"
          repository: qdrant/qdrant
          # Docker image pull policy
          # Default "IfNotPresent", unless the tag is dev, master or latest. Then "Always"
          #pullPolicy:
          # Docker image pull secret name
          # This secret should be available in the namespace where the cluster is running
          # Default not set
          #pullSecretName:
        # storage contains the settings for the storage of the Qdrant cluster
        storage:
          performance:
            # CPU budget, how many CPUs (threads) to allocate for an optimization job.
            # If 0 - auto selection, keep 1 or more CPUs unallocated depending on CPU size
            # If negative - subtract this number of CPUs from the available CPUs.
            # If positive - use this exact number of CPUs.
            optimizerCpuBudget: 0
            # Enable async scorer which uses io_uring when rescoring.
            # Only supported on Linux, must be enabled in your kernel.
            # See: <https://qdrant.tech/articles/io_uring/#and-what-about-qdrant>
            asyncScorer: false
        # Qdrant DB log level
        # Available options: DEBUG | INFO | WARN | ERROR
        # Default is "INFO"
        logLevel: INFO
        # Default Qdrant security context configuration
        securityContext:
          # Enable default security context
          # Default is false
          enabled: false
          # Default user for qdrant container
          # Default not set
          #user: 1000
          # Default fsGroup for qdrant container
          # Default not set
          #fsUser: 2000
          # Default group for qdrant container
          # Default not set
          #group: 3000
        # Network policies configuration for the Qdrant databases
        networkPolicies:
          ingress:
            - ports:
                - protocol: TCP
                  port: 6333
                - protocol: TCP
                  port: 6334
          # Allow DNS resolution from qdrant pods at Kubernetes internal DNS server
          egress:
            - ports:
                - protocol: UDP
                  port: 53
      # Scheduling config contains the settings specific for scheduling
      scheduling:
        # Default topology spread constraints (list from type corev1.TopologySpreadConstraint)
        topologySpreadConstraints:
          - maxSkew: 1
            topologyKey: "kubernetes.io/hostname"
            whenUnsatisfiable: "ScheduleAnyway"
        # Default pod disruption budget (object from type policyv1.PodDisruptionBudgetSpec)
        podDisruptionBudget:
          maxUnavailable: 1
      # ClusterManager config contains the settings specific for cluster manager
      clusterManager:
        # Whether or not the cluster manager (on operator level).
        # If disabled, all other properties in this struct are disregarded. Otherwise, the individual features will be inspected.
        # Default is false.
        enable: true
        # The endpoint address the cluster manager could be reached
        # If set, this should be a full URL like: http://cluster-manager.qdrant-cloud-ns.svc.cluster.local:7333
        endpointAddress: http://qdrant-cluster-manager:80
        # InvocationInterval is the interval between calls (started after the previous call is retured)
        # Default is 10 seconds
        invocationInterval: 10s
        # Timeout is the duration a single call to the cluster manager is allowed to take.
        # Default is 30 seconds
        timeout: 30s
        # Specifies overrides for the manage rules
        manageRulesOverrides:
          #dry_run:
          #max_transfers:
          #max_transfers_per_collection:
          #rebalance:
          #replicate:
      # Ingress config contains the settings specific for ingress
      ingress:
        # Whether or not the Ingress feature is enabled.
        # Default is true.
        enable: false
        # Which specific ingress provider should be used
        # Default is KubernetesIngress
        provider: KubernetesIngress
        # The specific settings when the Provider is QdrantCloudTraefik
        qdrantCloudTraefik:
          # Enable tls
          # Default is false
          tls: false
          # Secret with TLS certificate
          # Default is None
          secretName: ""
          # List of Traefik middlewares to apply
          # Default is an empty list
          middlewares: []
          # IP Allowlist Strategy for Traefik
          # Default is None
          ipAllowlistStrategy:
          # Enable body validator plugin and matching ingressroute rules
          # Default is false
          enableBodyValidatorPlugin: false
        # The specific settings when the Provider is KubernetesIngress
        kubernetesIngress:
          # Name of the ingress class
          # Default is None
          #ingressClassName:
      # TelemetryTimeout is the duration a single call to the cluster telemetry endpoint is allowed to take.
      # Default is 3 seconds
      telemetryTimeout: 3s
      # MaxConcurrentReconciles is the maximum number of concurrent Reconciles which can be run. Defaults to 20.
      maxConcurrentReconciles: 20
      # VolumeExpansionMode specifies the expansion mode, which can be online or offline (e.g. in case of Azure).
      # Available options: Online, Offline
      # Default is Online
      volumeExpansionMode: Online
    # BackupManagementConfig contains the settings for backup management
    backupManagement:
      # Whether or not the backup features are enabled.
      # If disabled, all other properties in this struct are disregarded. Otherwise, the individual features will be inspected.
      # Default is true.
      enable: true
      # Snapshots contains the settings for snapshots as part of backup management.
      snapshots:
        # Whether or not the Snapshot feature is enabled.
        # Default is true.
        enable: true
        # The VolumeSnapshotClass used to make VolumeSnapshots.
        # Default is "csi-snapclass".
        volumeSnapshotClass: "csi-snapclass"
        # The duration a snapshot is retained when the phase becomes Failed or Skipped
        # Default is 72h (3d).
        retainUnsuccessful: 72h
        # MaxConcurrentReconciles is the maximum number of concurrent Reconciles which can be run. Defaults to 1.
        maxConcurrentReconciles: 1
      # ScheduledSnapshots contains the settings for scheduled snapshot as part of backup management.
      scheduledSnapshots:
        # Whether or not the ScheduledSnapshot feature is enabled.
        # Default is true.
        enable: true
        # MaxConcurrentReconciles is the maximum number of concurrent Reconciles which can be run. Defaults to 1.
        maxConcurrentReconciles: 1
      # Restores contains the settings for restoring (a snapshot) as part of backup management.
      restores:
        # Whether or not the Restore feature is enabled.
        # Default is true.
        enable:  true
        # MaxConcurrentReconciles is the maximum number of concurrent Reconciles which can be run. Defaults to 1.
        maxConcurrentReconciles: 1

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/operator-configuration.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/operator-configuration.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b4bd9c4c-291b-48e6-88b5-e7862450b03f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9b56a70a-9ccb-4279-aea8-7efdfa9f6e19&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Foperator-configuration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575223678&cv=11&fst=1748575223678&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Foperator-configuration%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Configure%20the%20Qdrant%20Operator%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1349794651.1748575222&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575223700&cv=11&fst=1748575223700&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Foperator-configuration%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Configure%20the%20Qdrant%20Operator%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1349794651.1748575222&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575223652&cv=11&fst=1748575223652&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Foperator-configuration%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Configure%20the%20Qdrant%20Operator%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1349794651.1748575222&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b4bd9c4c-291b-48e6-88b5-e7862450b03f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9b56a70a-9ccb-4279-aea8-7efdfa9f6e19&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2Foperator-configuration%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)