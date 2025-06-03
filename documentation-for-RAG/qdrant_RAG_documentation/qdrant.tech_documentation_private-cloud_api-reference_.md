---
url: "https://qdrant.tech/documentation/private-cloud/api-reference/"
title: "API Reference - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Private cloud](https://qdrant.tech/documentation/private-cloud/)
- API Reference

# [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#api-reference) API Reference

## [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#packages) Packages

- [qdrant.io/v1](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantiov1)

## [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantiov1) qdrant.io/v1

Package v1 contains API Schema definitions for the qdrant.io v1 API group

### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#resource-types) Resource Types

- [QdrantCloudRegion](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregion)
- [QdrantCloudRegionList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionlist)
- [QdrantCluster](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcluster)
- [QdrantClusterList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterlist)
- [QdrantClusterRestore](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestore)
- [QdrantClusterRestoreList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestorelist)
- [QdrantClusterScheduledSnapshot](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterscheduledsnapshot)
- [QdrantClusterScheduledSnapshotList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterscheduledsnapshotlist)
- [QdrantClusterSnapshot](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshot)
- [QdrantClusterSnapshotList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshotlist)
- [QdrantEntity](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentity)
- [QdrantEntityList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentitylist)
- [QdrantRelease](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantrelease)
- [QdrantReleaseList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantreleaselist)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#clusterphase) ClusterPhase

_Underlying type:_ _string_

_Appears in:_

- [QdrantClusterStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterstatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#componentphase) ComponentPhase

_Underlying type:_ _string_

_Appears in:_

- [ComponentStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#componentstatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#componentreference) ComponentReference

_Appears in:_

- [QdrantCloudRegionSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | APIVersion is the group and version of the component being referenced. |  |  |
| `kind` _string_ | Kind is the type of component being referenced |  |  |
| `name` _string_ | Name is the name of component being referenced |  |  |
| `namespace` _string_ | Namespace is the namespace of component being referenced. |  |  |
| `markedForDeletion` _boolean_ | MarkedForDeletion specifies whether the component is marked for deletion |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#componentstatus) ComponentStatus

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ | Name specifies the name of the component |  |  |
| `namespace` _string_ | Namespace specifies the namespace of the component |  |  |
| `version` _string_ | Version specifies the version of the component |  |  |
| `phase` _[ComponentPhase](https://qdrant.tech/documentation/private-cloud/api-reference/#componentphase)_ | Phase specifies the current phase of the component |  |  |
| `message` _string_ | Message specifies the info explaining the current phase of the component |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#entityphase) EntityPhase

_Underlying type:_ _string_

_Appears in:_

- [QdrantEntityStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentitystatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#entityresult) EntityResult

_Underlying type:_ _string_

EntityResult is the last result from the invocation to a manager

_Appears in:_

- [QdrantEntityStatusResult](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentitystatusresult)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#gpu) GPU

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `gpuType` _[GPUType](https://qdrant.tech/documentation/private-cloud/api-reference/#gputype)_ | GPUType specifies the type of the GPU to use. If set, GPU indexing is enabled. |  | Enum: \[nvidia amd\] |
| `forceHalfPrecision` _boolean_ | ForceHalfPrecision for `f32` values while indexing.<br>`f16` conversion will take place<br>only inside GPU memory and won’t affect storage type. | false |  |
| `deviceFilter` _string array_ | DeviceFilter for GPU devices by hardware name. Case-insensitive.<br>List of substrings to match against the gpu device name.<br>Example: \[- “nvidia”\]<br>If not specified, all devices are accepted. |  | MinItems: 1 |
| `devices` _string array_ | Devices is a List of explicit GPU devices to use.<br>If host has multiple GPUs, this option allows to select specific devices<br>by their index in the list of found devices.<br>If `deviceFilter` is set, indexes are applied after filtering.<br>If not specified, all devices are accepted. |  | MinItems: 1 |
| `parallelIndexes` _integer_ | ParallelIndexes is the number of parallel indexes to run on the GPU. | 1 | Minimum: 1 |
| `groupsCount` _integer_ | GroupsCount is the amount of used vulkan “groups” of GPU.<br>In other words, how many parallel points can be indexed by GPU.<br>Optimal value might depend on the GPU model.<br>Proportional, but doesn’t necessary equal to the physical number of warps.<br>Do not change this value unless you know what you are doing. |  | Minimum: 1 |
| `allowIntegrated` _boolean_ | AllowIntegrated specifies whether to allow integrated GPUs to be used. | false |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#gputype) GPUType

_Underlying type:_ _string_

_Appears in:_

- [GPU](https://qdrant.tech/documentation/private-cloud/api-reference/#gpu)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#helmrelease) HelmRelease

_Appears in:_

- [QdrantCloudRegionSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `markedForDeletionAt` _string_ | MarkedForDeletionAt specifies the time when the helm release was marked for deletion |  |  |
| `object` _[HelmRelease](https://qdrant.tech/documentation/private-cloud/api-reference/#helmrelease)_ | Object specifies the helm release object |  | EmbeddedResource: {} |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#helmrepository) HelmRepository

_Appears in:_

- [QdrantCloudRegionSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `markedForDeletionAt` _string_ | MarkedForDeletionAt specifies the time when the helm repository was marked for deletion |  |  |
| `object` _[HelmRepository](https://qdrant.tech/documentation/private-cloud/api-reference/#helmrepository)_ | Object specifies the helm repository object |  | EmbeddedResource: {} |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#inferenceconfig) InferenceConfig

_Appears in:_

- [QdrantConfiguration](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfiguration)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled specifies whether to enable inference for the cluster or not. | false |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#ingress) Ingress

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled specifies whether to enable ingress for the cluster or not. |  |  |
| `annotations` _object (keys:string, values:string)_ | Annotations specifies annotations for the ingress. |  |  |
| `ingressClassName` _string_ | IngressClassName specifies the name of the ingress class |  |  |
| `host` _string_ | Host specifies the host for the ingress. |  |  |
| `tls` _boolean_ | TLS specifies whether to enable tls for the ingress.<br>The default depends on the ingress provider:<br>\- KubernetesIngress: False<br>\- NginxIngress: False<br>\- QdrantCloudTraefik: Depending on the config.tls setting of the operator. |  |  |
| `tlsSecretName` _string_ | TLSSecretName specifies the name of the secret containing the tls certificate. |  |  |
| `nginx` _[NGINXConfig](https://qdrant.tech/documentation/private-cloud/api-reference/#nginxconfig)_ | NGINX specifies the nginx ingress specific configurations. |  |  |
| `traefik` _[TraefikConfig](https://qdrant.tech/documentation/private-cloud/api-reference/#traefikconfig)_ | Traefik specifies the traefik ingress specific configurations. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#kubernetesdistribution) KubernetesDistribution

_Underlying type:_ _string_

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#kubernetespod) KubernetesPod

_Appears in:_

- [KubernetesStatefulSet](https://qdrant.tech/documentation/private-cloud/api-reference/#kubernetesstatefulset)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `annotations` _object (keys:string, values:string)_ | Annotations specifies the annotations for the Pods. |  |  |
| `labels` _object (keys:string, values:string)_ | Labels specifies the labels for the Pods. |  |  |
| `extraEnv` _[EnvVar](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#envvar-v1-core) array_ | ExtraEnv specifies the extra environment variables for the Pods. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#kubernetesservice) KubernetesService

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `type` _[ServiceType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#servicetype-v1-core)_ | Type specifies the type of the Service: “ClusterIP”, “NodePort”, “LoadBalancer”. | ClusterIP |  |
| `annotations` _object (keys:string, values:string)_ | Annotations specifies the annotations for the Service. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#kubernetesstatefulset) KubernetesStatefulSet

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `annotations` _object (keys:string, values:string)_ | Annotations specifies the annotations for the StatefulSet. |  |  |
| `pods` _[KubernetesPod](https://qdrant.tech/documentation/private-cloud/api-reference/#kubernetespod)_ | Pods specifies the configuration of the Pods of the Qdrant StatefulSet. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#metricsource) MetricSource

_Underlying type:_ _string_

_Appears in:_

- [Monitoring](https://qdrant.tech/documentation/private-cloud/api-reference/#monitoring)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#monitoring) Monitoring

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `cAdvisorMetricSource` _[MetricSource](https://qdrant.tech/documentation/private-cloud/api-reference/#metricsource)_ | CAdvisorMetricSource specifies the cAdvisor metric source |  |  |
| `nodeMetricSource` _[MetricSource](https://qdrant.tech/documentation/private-cloud/api-reference/#metricsource)_ | NodeMetricSource specifies the node metric source |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#nginxconfig) NGINXConfig

_Appears in:_

- [Ingress](https://qdrant.tech/documentation/private-cloud/api-reference/#ingress)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `allowedSourceRanges` _string array_ | AllowedSourceRanges specifies the allowed CIDR source ranges for the ingress. |  |  |
| `grpcHost` _string_ | GRPCHost specifies the host name for the GRPC ingress. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#nodeinfo) NodeInfo

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ | Name specifies the name of the node |  |  |
| `region` _string_ | Region specifies the region of the node |  |  |
| `zone` _string_ | Zone specifies the zone of the node |  |  |
| `instanceType` _string_ | InstanceType specifies the instance type of the node |  |  |
| `arch` _string_ | Arch specifies the CPU architecture of the node |  |  |
| `capacity` _[NodeResourceInfo](https://qdrant.tech/documentation/private-cloud/api-reference/#noderesourceinfo)_ | Capacity specifies the capacity of the node |  |  |
| `allocatable` _[NodeResourceInfo](https://qdrant.tech/documentation/private-cloud/api-reference/#noderesourceinfo)_ | Allocatable specifies the allocatable resources of the node |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#noderesourceinfo) NodeResourceInfo

_Appears in:_

- [NodeInfo](https://qdrant.tech/documentation/private-cloud/api-reference/#nodeinfo)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `cpu` _string_ | CPU specifies the CPU resources of the node |  |  |
| `memory` _string_ | Memory specifies the memory resources of the node |  |  |
| `pods` _string_ | Pods specifies the pods resources of the node |  |  |
| `ephemeralStorage` _string_ | EphemeralStorage specifies the ephemeral storage resources of the node |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#nodestatus) NodeStatus

_Appears in:_

- [QdrantClusterStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ | Name specifies the name of the node |  |  |
| `started_at` _string_ | StartedAt specifies the time when the node started (in RFC3339 format) |  |  |
| `state` _object (keys: [PodConditionType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#podconditiontype-v1-core), values: [ConditionStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#conditionstatus-v1-core))_ | States specifies the condition states of the node |  |  |
| `version` _string_ | Version specifies the version of Qdrant running on the node |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#pause) Pause

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `owner` _string_ | Owner specifies the owner of the pause request. |  |  |
| `reason` _string_ | Reason specifies the reason for the pause request. |  |  |
| `creationTimestamp` _string_ | CreationTimestamp specifies the time when the pause request was created. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantcloudregion) QdrantCloudRegion

QdrantCloudRegion is the Schema for the qdrantcloudregions API

_Appears in:_

- [QdrantCloudRegionList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionlist)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantCloudRegion` |  |  |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[QdrantCloudRegionSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionspec)_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantcloudregionlist) QdrantCloudRegionList

QdrantCloudRegionList contains a list of QdrantCloudRegion

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantCloudRegionList` |  |  |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `items` _[QdrantCloudRegion](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregion) array_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantcloudregionspec) QdrantCloudRegionSpec

QdrantCloudRegionSpec defines the desired state of QdrantCloudRegion

_Appears in:_

- [QdrantCloudRegion](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregion)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `id` _string_ | Id specifies the unique identifier of the region |  |  |
| `components` _[ComponentReference](https://qdrant.tech/documentation/private-cloud/api-reference/#componentreference) array_ | Components specifies the list of components to be installed in the region |  |  |
| `helmRepositories` _[HelmRepository](https://qdrant.tech/documentation/private-cloud/api-reference/#helmrepository) array_ | HelmRepositories specifies the list of helm repositories to be created to the region<br>Deprecated: Use “Components” instead |  |  |
| `helmReleases` _[HelmRelease](https://qdrant.tech/documentation/private-cloud/api-reference/#helmrelease) array_ | HelmReleases specifies the list of helm releases to be created to the region<br>Deprecated: Use “Components” instead |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantcluster) QdrantCluster

QdrantCluster is the Schema for the qdrantclusters API

_Appears in:_

- [QdrantClusterList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterlist)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantCluster` |  |  |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterlist) QdrantClusterList

QdrantClusterList contains a list of QdrantCluster

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantClusterList` |  |  |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `items` _[QdrantCluster](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcluster) array_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterrestore) QdrantClusterRestore

QdrantClusterRestore is the Schema for the qdrantclusterrestores API

_Appears in:_

- [QdrantClusterRestoreList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestorelist)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantClusterRestore` |  |  |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[QdrantClusterRestoreSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestorespec)_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterrestorelist) QdrantClusterRestoreList

QdrantClusterRestoreList contains a list of QdrantClusterRestore objects

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantClusterRestoreList` |  |  |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `items` _[QdrantClusterRestore](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestore) array_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterrestorespec) QdrantClusterRestoreSpec

QdrantClusterRestoreSpec defines the desired state of QdrantClusterRestore

_Appears in:_

- [QdrantClusterRestore](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestore)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `source` _[RestoreSource](https://qdrant.tech/documentation/private-cloud/api-reference/#restoresource)_ | Source defines the source snapshot from which the restore will be done |  |  |
| `destination` _[RestoreDestination](https://qdrant.tech/documentation/private-cloud/api-reference/#restoredestination)_ | Destination defines the destination cluster where the source data will end up |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterscheduledsnapshot) QdrantClusterScheduledSnapshot

QdrantClusterScheduledSnapshot is the Schema for the qdrantclusterscheduledsnapshots API

_Appears in:_

- [QdrantClusterScheduledSnapshotList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterscheduledsnapshotlist)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantClusterScheduledSnapshot` |  |  |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[QdrantClusterScheduledSnapshotSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterscheduledsnapshotspec)_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterscheduledsnapshotlist) QdrantClusterScheduledSnapshotList

QdrantClusterScheduledSnapshotList contains a list of QdrantCluster

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantClusterScheduledSnapshotList` |  |  |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `items` _[QdrantClusterScheduledSnapshot](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterscheduledsnapshot) array_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterscheduledsnapshotspec) QdrantClusterScheduledSnapshotSpec

QdrantClusterScheduledSnapshotSpec defines the desired state of QdrantCluster

_Appears in:_

- [QdrantClusterScheduledSnapshot](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterscheduledsnapshot)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `cluster-id` _string_ | Id specifies the unique identifier of the cluster |  |  |
| `scheduleShortId` _string_ | Specifies short Id which identifies a schedule |  | MaxLength: 8 |
| `schedule` _string_ | Cron expression for frequency of creating snapshots, see [https://en.wikipedia.org/wiki/Cron](https://en.wikipedia.org/wiki/Cron).<br>The schedule is specified in UTC. |  | Pattern: \`^(@(annually |
| `retention` _string_ | Retention of schedule in hours |  | Pattern: `^[0-9]+h$` |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclustersnapshot) QdrantClusterSnapshot

QdrantClusterSnapshot is the Schema for the qdrantclustersnapshots API

_Appears in:_

- [QdrantClusterSnapshotList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshotlist)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantClusterSnapshot` |  |  |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[QdrantClusterSnapshotSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshotspec)_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclustersnapshotlist) QdrantClusterSnapshotList

QdrantClusterSnapshotList contains a list of QdrantClusterSnapshot

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantClusterSnapshotList` |  |  |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `items` _[QdrantClusterSnapshot](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshot) array_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclustersnapshotphase) QdrantClusterSnapshotPhase

_Underlying type:_ _string_

_Appears in:_

- [QdrantClusterSnapshotStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshotstatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclustersnapshotspec) QdrantClusterSnapshotSpec

_Appears in:_

- [QdrantClusterSnapshot](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshot)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `cluster-id` _string_ | The cluster ID for which a Snapshot need to be taken<br>The cluster should be in the same namespace as this QdrantClusterSnapshot is located |  |  |
| `creation-timestamp` _integer_ | The CreationTimestamp of the backup (expressed in Unix epoch format) |  |  |
| `scheduleShortId` _string_ | Specifies the short Id which identifies a schedule, if any.<br>This field should not be set if the backup is made manually. |  | MaxLength: 8 |
| `retention` _string_ | The retention period of this snapshot in hours, if any.<br>If not set, the backup doesn’t have a retention period, meaning it will not be removed. |  | Pattern: `^[0-9]+h$` |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantclusterspec) QdrantClusterSpec

QdrantClusterSpec defines the desired state of QdrantCluster

_Appears in:_

- [QdrantCluster](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcluster)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `id` _string_ | Id specifies the unique identifier of the cluster |  |  |
| `version` _string_ | Version specifies the version of Qdrant to deploy |  |  |
| `size` _integer_ | Size specifies the desired number of Qdrant nodes in the cluster |  | Maximum: 30<br>Minimum: 1 |
| `servicePerNode` _boolean_ | ServicePerNode specifies whether the cluster should start a dedicated service for each node. | true |  |
| `clusterManager` _boolean_ | ClusterManager specifies whether to use the cluster manager for this cluster.<br>The Python-operator will deploy a dedicated cluster manager instance.<br>The Go-operator will use a shared instance.<br>If not set, the default will be taken from the operator config. |  |  |
| `suspend` _boolean_ | Suspend specifies whether to suspend the cluster.<br>If enabled, the cluster will be suspended and all related resources will be removed except the PVCs. | false |  |
| `pauses` _[Pause](https://qdrant.tech/documentation/private-cloud/api-reference/#pause) array_ | Pauses specifies a list of pause request by developer for manual maintenance.<br>Operator will skip handling any changes in the CR if any pause request is present. |  |  |
| `image` _[QdrantImage](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantimage)_ | Image specifies the image to use for each Qdrant node. |  |  |
| `resources` _[Resources](https://qdrant.tech/documentation/private-cloud/api-reference/#resources)_ | Resources specifies the resources to allocate for each Qdrant node. |  |  |
| `security` _[QdrantSecurityContext](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantsecuritycontext)_ | Security specifies the security context for each Qdrant node. |  |  |
| `tolerations` _[Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#toleration-v1-core) array_ | Tolerations specifies the tolerations for each Qdrant node. |  |  |
| `nodeSelector` _object (keys:string, values:string)_ | NodeSelector specifies the node selector for each Qdrant node. |  |  |
| `config` _[QdrantConfiguration](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfiguration)_ | Config specifies the Qdrant configuration setttings for the clusters. |  |  |
| `ingress` _[Ingress](https://qdrant.tech/documentation/private-cloud/api-reference/#ingress)_ | Ingress specifies the ingress for the cluster. |  |  |
| `service` _[KubernetesService](https://qdrant.tech/documentation/private-cloud/api-reference/#kubernetesservice)_ | Service specifies the configuration of the Qdrant Kubernetes Service. |  |  |
| `gpu` _[GPU](https://qdrant.tech/documentation/private-cloud/api-reference/#gpu)_ | GPU specifies GPU configuration for the cluster. If this field is not set, no GPU will be used. |  |  |
| `statefulSet` _[KubernetesStatefulSet](https://qdrant.tech/documentation/private-cloud/api-reference/#kubernetesstatefulset)_ | StatefulSet specifies the configuration of the Qdrant Kubernetes StatefulSet. |  |  |
| `storageClassNames` _[StorageClassNames](https://qdrant.tech/documentation/private-cloud/api-reference/#storageclassnames)_ | StorageClassNames specifies the storage class names for db and snapshots. |  |  |
| `topologySpreadConstraints` _[TopologySpreadConstraint](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#topologyspreadconstraint-v1-core)_ | TopologySpreadConstraints specifies the topology spread constraints for the cluster. |  |  |
| `podDisruptionBudget` _[PodDisruptionBudgetSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#poddisruptionbudgetspec-v1-policy)_ | PodDisruptionBudget specifies the pod disruption budget for the cluster. |  |  |
| `restartAllPodsConcurrently` _boolean_ | RestartAllPodsConcurrently specifies whether to restart all pods concurrently (also called one-shot-restart).<br>If enabled, all the pods in the cluster will be restarted concurrently in situations where multiple pods<br>need to be restarted, like when RestartedAtAnnotationKey is added/updated or the Qdrant version needs to be upgraded.<br>This helps sharded but not replicated clusters to reduce downtime to a possible minimum during restart.<br>If unset, the operator is going to restart nodes concurrently if none of the collections if replicated. |  |  |
| `startupDelaySeconds` _integer_ | If StartupDelaySeconds is set (> 0), an additional ‘sleep ’ will be emitted to the pod startup.<br>The sleep will be added when a pod is restarted, it will not force any pod to restart.<br>This feature can be used for debugging the core, e.g. if a pod is in crash loop, it provided a way<br>to inspect the attached storage. |  |  |
| `rebalanceStrategy` _[RebalanceStrategy](https://qdrant.tech/documentation/private-cloud/api-reference/#rebalancestrategy)_ | RebalanceStrategy specifies the strategy to use for automaticially rebalancing shards the cluster.<br>Cluster-manager needs to be enabled for this feature to work. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantconfiguration) QdrantConfiguration

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `collection` _[QdrantConfigurationCollection](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfigurationcollection)_ | Collection specifies the default collection configuration for Qdrant. |  |  |
| `log_level` _string_ | LogLevel specifies the log level for Qdrant. |  |  |
| `service` _[QdrantConfigurationService](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfigurationservice)_ | Service specifies the service level configuration for Qdrant. |  |  |
| `tls` _[QdrantConfigurationTLS](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfigurationtls)_ | TLS specifies the TLS configuration for Qdrant. |  |  |
| `storage` _[StorageConfig](https://qdrant.tech/documentation/private-cloud/api-reference/#storageconfig)_ | Storage specifies the storage configuration for Qdrant. |  |  |
| `inference` _[InferenceConfig](https://qdrant.tech/documentation/private-cloud/api-reference/#inferenceconfig)_ | Inference configuration. This is used in Qdrant Managed Cloud only. If not set Inference is not available to this cluster. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantconfigurationcollection) QdrantConfigurationCollection

_Appears in:_

- [QdrantConfiguration](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfiguration)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `replication_factor` _integer_ | ReplicationFactor specifies the default number of replicas of each shard |  |  |
| `write_consistency_factor` _integer_ | WriteConsistencyFactor specifies how many replicas should apply the operation to consider it successful |  |  |
| `vectors` _[QdrantConfigurationCollectionVectors](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfigurationcollectionvectors)_ | Vectors specifies the default parameters for vectors |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantconfigurationcollectionvectors) QdrantConfigurationCollectionVectors

_Appears in:_

- [QdrantConfigurationCollection](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfigurationcollection)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `on_disk` _boolean_ | OnDisk specifies whether vectors should be stored in memory or on disk. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantconfigurationservice) QdrantConfigurationService

_Appears in:_

- [QdrantConfiguration](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfiguration)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `api_key` _[QdrantSecretKeyRef](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantsecretkeyref)_ | ApiKey for the qdrant instance |  |  |
| `read_only_api_key` _[QdrantSecretKeyRef](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantsecretkeyref)_ | ReadOnlyApiKey for the qdrant instance |  |  |
| `jwt_rbac` _boolean_ | JwtRbac specifies whether to enable jwt rbac for the qdrant instance<br>Default is false |  |  |
| `hide_jwt_dashboard` _boolean_ | HideJwtDashboard specifies whether to hide the JWT dashboard of the embedded UI<br>Default is false |  |  |
| `enable_tls` _boolean_ | EnableTLS specifies whether to enable tls for the qdrant instance<br>Default is false |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantconfigurationtls) QdrantConfigurationTLS

_Appears in:_

- [QdrantConfiguration](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfiguration)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `cert` _[QdrantSecretKeyRef](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantsecretkeyref)_ | Reference to the secret containing the server certificate chain file |  |  |
| `key` _[QdrantSecretKeyRef](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantsecretkeyref)_ | Reference to the secret containing the server private key file |  |  |
| `caCert` _[QdrantSecretKeyRef](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantsecretkeyref)_ | Reference to the secret containing the CA certificate file |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantentity) QdrantEntity

QdrantEntity is the Schema for the qdrantentities API

_Appears in:_

- [QdrantEntityList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentitylist)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantEntity` |  |  |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[QdrantEntitySpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentityspec)_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantentitylist) QdrantEntityList

QdrantEntityList contains a list of QdrantEntity objects

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantEntityList` |  |  |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `items` _[QdrantEntity](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentity) array_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantentityspec) QdrantEntitySpec

QdrantEntitySpec defines the desired state of QdrantEntity

_Appears in:_

- [QdrantEntity](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentity)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `id` _string_ | The unique identifier of the entity (in UUID format). |  |  |
| `entityType` _string_ | The type of the entity. |  |  |
| `clusterId` _string_ | The optional cluster identifier |  |  |
| `createdAt` _[MicroTime](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#microtime-v1-meta)_ | Timestamp when the entity was created. |  |  |
| `lastUpdatedAt` _[MicroTime](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#microtime-v1-meta)_ | Timestamp when the entity was last updated. |  |  |
| `deletedAt` _[MicroTime](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#microtime-v1-meta)_ | Timestamp when the entity was deleted (or is started to be deleting).<br>If not set the entity is not deleted |  |  |
| `payload` _[JSON](https://qdrant.tech/documentation/private-cloud/api-reference/#json)_ | Generic payload for this entity |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantentitystatusresult) QdrantEntityStatusResult

QdrantEntityStatusResult is the last result from the invocation to a manager

_Appears in:_

- [QdrantEntityStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantentitystatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `result` _[EntityResult](https://qdrant.tech/documentation/private-cloud/api-reference/#entityresult)_ | The result of last reconcile of the entity |  | Enum: \[Ok Pending Error\] |
| `reason` _string_ | The reason of the result (e.g. in case of an error) |  |  |
| `payload` _[JSON](https://qdrant.tech/documentation/private-cloud/api-reference/#json)_ | The optional payload of the status. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantimage) QdrantImage

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `repository` _string_ | Repository specifies the repository of the Qdrant image.<br>If not specified defaults the config of the operator (or qdrant/qdrant if not specified in operator). |  |  |
| `pullPolicy` _[PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#pullpolicy-v1-core)_ | PullPolicy specifies the image pull policy for the Qdrant image.<br>If not specified defaults the config of the operator (or IfNotPresent if not specified in operator). |  |  |
| `pullSecretName` _string_ | PullSecretName specifies the pull secret for the Qdrant image. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantrelease) QdrantRelease

QdrantRelease describes an available Qdrant release

_Appears in:_

- [QdrantReleaseList](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantreleaselist)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantRelease` |  |  |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[QdrantReleaseSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantreleasespec)_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantreleaselist) QdrantReleaseList

QdrantReleaseList contains a list of QdrantRelease

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `qdrant.io/v1` |  |  |
| `kind` _string_ | `QdrantReleaseList` |  |  |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `items` _[QdrantRelease](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantrelease) array_ |  |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantreleasespec) QdrantReleaseSpec

QdrantReleaseSpec defines the desired state of QdrantRelease

_Appears in:_

- [QdrantRelease](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantrelease)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `version` _string_ | Version number (should be semver compliant).<br>E.g. “v1.10.1” |  |  |
| `default` _boolean_ | If set, this version is default for new clusters on Cloud.<br>There should be only 1 Qdrant version in the platform set as default. | false |  |
| `image` _string_ | Full docker image to use for this version.<br>If empty, a default image will be derived from Version (and qdrant/qdrant is assumed). |  |  |
| `unavailable` _boolean_ | If set, this version cannot be used for new clusters. | false |  |
| `endOfLife` _boolean_ | If set, this version is no longer actively supported. | false |  |
| `accountIds` _string array_ | If set, this version can only be used by accounts with given IDs. |  |  |
| `accountPrivileges` _string array_ | If set, this version can only be used by accounts that have been given the listed privileges. |  |  |
| `remarks` _string_ | General remarks for human reading |  |  |
| `releaseNotesURL` _string_ | Release Notes URL for the specified version |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantsecretkeyref) QdrantSecretKeyRef

_Appears in:_

- [QdrantConfigurationService](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfigurationservice)
- [QdrantConfigurationTLS](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfigurationtls)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `secretKeyRef` _[SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#secretkeyselector-v1-core)_ | SecretKeyRef to the secret containing data to configure the qdrant instance |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#qdrantsecuritycontext) QdrantSecurityContext

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `user` _integer_ | User specifies the user to run the Qdrant process as. |  |  |
| `group` _integer_ | Group specifies the group to run the Qdrant process as. |  |  |
| `fsGroup` _integer_ | FsGroup specifies file system group to run the Qdrant process as. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#rebalancestrategy) RebalanceStrategy

_Underlying type:_ _string_

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#regioncapabilities) RegionCapabilities

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `volumeSnapshot` _boolean_ | VolumeSnapshot specifies whether the Kubernetes cluster supports volume snapshot |  |  |
| `volumeExpansion` _boolean_ | VolumeExpansion specifies whether the Kubernetes cluster supports volume expansion |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#regionphase) RegionPhase

_Underlying type:_ _string_

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#resourcerequests) ResourceRequests

_Appears in:_

- [Resources](https://qdrant.tech/documentation/private-cloud/api-reference/#resources)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `cpu` _string_ | CPU specifies the CPU request for each Qdrant node. |  |  |
| `memory` _string_ | Memory specifies the memory request for each Qdrant node. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#resources) Resources

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `cpu` _string_ | CPU specifies the CPU limit for each Qdrant node. |  |  |
| `memory` _string_ | Memory specifies the memory limit for each Qdrant node. |  |  |
| `storage` _string_ | Storage specifies the storage amount for each Qdrant node. |  |  |
| `requests` _[ResourceRequests](https://qdrant.tech/documentation/private-cloud/api-reference/#resourcerequests)_ | Requests specifies the resource requests for each Qdrant node. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#restoredestination) RestoreDestination

_Appears in:_

- [QdrantClusterRestoreSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestorespec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ | Name of the destination cluster |  |  |
| `namespace` _string_ | Namespace of the destination cluster |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#restorephase) RestorePhase

_Underlying type:_ _string_

_Appears in:_

- [QdrantClusterRestoreStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestorestatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#restoresource) RestoreSource

_Appears in:_

- [QdrantClusterRestoreSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterrestorespec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `snapshotName` _string_ | SnapshotName is the name of the snapshot from which we wish to restore |  |  |
| `namespace` _string_ | Namespace of the snapshot |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#scheduledsnapshotphase) ScheduledSnapshotPhase

_Underlying type:_ _string_

_Appears in:_

- [QdrantClusterScheduledSnapshotStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterscheduledsnapshotstatus)

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#storageclass) StorageClass

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ | Name specifies the name of the storage class |  |  |
| `default` _boolean_ | Default specifies whether the storage class is the default storage class |  |  |
| `provisioner` _string_ | Provisioner specifies the provisioner of the storage class |  |  |
| `allowVolumeExpansion` _boolean_ | AllowVolumeExpansion specifies whether the storage class allows volume expansion |  |  |
| `reclaimPolicy` _string_ | ReclaimPolicy specifies the reclaim policy of the storage class |  |  |
| `parameters` _object (keys:string, values:string)_ | Parameters specifies the parameters of the storage class |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#storageclassnames) StorageClassNames

_Appears in:_

- [QdrantClusterSpec](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `db` _string_ | DB specifies the storage class name for db volume. |  |  |
| `snapshots` _string_ | Snapshots specifies the storage class name for snapshots volume. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#storageconfig) StorageConfig

_Appears in:_

- [QdrantConfiguration](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantconfiguration)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `performance` _[StoragePerformanceConfig](https://qdrant.tech/documentation/private-cloud/api-reference/#storageperformanceconfig)_ | Performance configuration |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#storageperformanceconfig) StoragePerformanceConfig

_Appears in:_

- [StorageConfig](https://qdrant.tech/documentation/private-cloud/api-reference/#storageconfig)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `optimizer_cpu_budget` _integer_ | OptimizerCPUBudget defines the number of CPU allocation.<br>If 0 - auto selection, keep 1 or more CPUs unallocated depending on CPU size<br>If negative - subtract this number of CPUs from the available CPUs.<br>If positive - use this exact number of CPUs. |  |  |
| `async_scorer` _boolean_ | AsyncScorer enables io\_uring when rescoring |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#traefikconfig) TraefikConfig

_Appears in:_

- [Ingress](https://qdrant.tech/documentation/private-cloud/api-reference/#ingress)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `allowedSourceRanges` _string array_ | AllowedSourceRanges specifies the allowed CIDR source ranges for the ingress. |  |  |
| `entryPoints` _string array_ | EntryPoints is the list of traefik entry points to use for the ingress route.<br>If nothing is set, it will take the entryPoints configured in the operator config. |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#volumesnapshotclass) VolumeSnapshotClass

_Appears in:_

- [QdrantCloudRegionStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantcloudregionstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ | Name specifies the name of the volume snapshot class |  |  |
| `driver` _string_ | Driver specifies the driver of the volume snapshot class |  |  |

#### [Anchor](https://qdrant.tech/documentation/private-cloud/api-reference/\#volumesnapshotinfo) VolumeSnapshotInfo

_Appears in:_

- [QdrantClusterSnapshotStatus](https://qdrant.tech/documentation/private-cloud/api-reference/#qdrantclustersnapshotstatus)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `volumeSnapshotName` _string_ | VolumeSnapshotName is the name of the volume snapshot |  |  |
| `volumeName` _string_ | VolumeName is the name of the volume that was backed up |  |  |
| `readyToUse` _boolean_ | ReadyToUse indicates if the volume snapshot is ready to use |  |  |
| `snapshotHandle` _string_ | SnapshotHandle is the identifier of the volume snapshot in the respective cloud provider |  |  |

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/api-reference.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/api-reference.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574203595&cv=11&fst=1748574203595&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fapi-reference%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=API%20Reference%20-%20Qdrant&npa=0&pscdl=noapi&auid=1186269310.1748574203&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574203553&cv=11&fst=1748574203553&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fapi-reference%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=API%20Reference%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1186269310.1748574203&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ed3c7301-2d40-494e-814a-d38313cf4cc8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=dfef8635-355f-4440-9b24-153310b8914c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fapi-reference%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ed3c7301-2d40-494e-814a-d38313cf4cc8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=dfef8635-355f-4440-9b24-153310b8914c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fapi-reference%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574204719&cv=11&fst=1748574204719&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fapi-reference%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=API%20Reference%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1186269310.1748574203&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)