---
url: "https://docs.n8n.io/hosting/installation/server-setups/azure/"
title: "Azure | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/installation/server-setups/azure/#hosting-n8n-on-azure)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/server-setups/azure.md "Edit this page")

# Hosting n8n on Azure [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#hosting-n8n-on-azure "Permanent link")

This hosting guide shows you how to self-host n8n on Azure. It uses n8n with Postgres as a database backend using Kubernetes to manage the necessary resources and reverse proxy.

## Prerequisites [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#prerequisites "Permanent link")

You need [The Azure command line tool](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

Self-hosting knowledge prerequisites

Self-hosting n8n requires technical knowledge, including:

- Setting up and configuring servers and containers
- Managing application resources and scaling
- Securing servers and applications
- Configuring n8n

n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, n8n recommends [n8n Cloud](https://n8n.io/cloud/).

Latest and Next versions

n8n releases a new minor version most weeks. The `latest` version is for production use. `next` is the most recent release. You should treat `next` as a beta: it may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

Current `latest`: 1.94.1

Current `next`: 1.95.1

## Hosting options [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#hosting-options "Permanent link")

Azure offers several ways suitable for hosting n8n, including Azure Container Instances (optimized for running containers), Linux Virtual Machines, and Azure Kubernetes Service (containers running with Kubernetes).

This guide uses the Azure Kubernetes Service (AKS) as the hosting option. Using Kubernetes requires some additional complexity and configuration, but is the best method for scaling n8n as demand changes.

The steps in this guide use a mix of the Azure UI and command line tool, but you can use either to accomplish most tasks.

## Open the Azure Kubernetes Service [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#open-the-azure-kubernetes-service "Permanent link")

From [the Azure portal](https://portal.azure.com/) select **Kubernetes services**.

## Create a cluster [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#create-a-cluster "Permanent link")

From the Kubernetes services page, select **Create** \> **Create a Kubernetes cluster**.

You can select any of the configuration options that suit your needs, then select **Create** when done.

## Set Kubectl context [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#set-kubectl-context "Permanent link")

The remainder of the steps in this guide require you to set the Azure instance as the Kubectl context. You can find the connection details for a cluster instance by opening its details page and then the **Connect** button. The resulting code snippets shows the steps to paste and run into a terminal to change your local Kubernetes settings to use the new cluster.

## Clone configuration repository [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#clone-configuration-repository "Permanent link")

Kubernetes and n8n require a series of configuration files. You can clone these from [this repository](https://github.com/n8n-io/n8n-kubernetes-hosting/tree/azure). The following steps tell you which file configures what and what you need to change.

Clone the repository with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>git clone https://github.com/n8n-io/n8n-kubernetes-hosting.git -b azure<br>``` |

And change directory to the root of the repository you cloned:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>cd azure<br>``` |

## Configure Postgres [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#configure-postgres "Permanent link")

For larger scale n8n deployments, Postgres provides a more robust database backend than SQLite.

### Configure volume for persistent storage [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#configure-volume-for-persistent-storage "Permanent link")

To maintain data between pod restarts, the Postgres deployment needs a persistent volume. The default storage class is suitable for this purpose and is defined in the `postgres-claim0-persistentvolumeclaim.yaml` manifest.

Specialized storage classes

If you have specialised or higher requirements for storage classes, [read more on the options Azure offers in the documentation](https://learn.microsoft.com/en-us/azure/aks/concepts-storage#storage-classes).

### Postgres environment variables [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#postgres-environment-variables "Permanent link")

Postgres needs some environment variables set to pass to the application running in the containers.

The example `postgres-secret.yaml` file contains placeholders you need to replace with your own values. Postgres will use these details when creating the database..

The `postgres-deployment.yaml` manifest then uses the values from this manifest file to send to the application pods.

## Configure n8n [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#configure-n8n "Permanent link")

### Create a volume for file storage [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#create-a-volume-for-file-storage "Permanent link")

While not essential for running n8n, using persistent volumes is required for:

- Using nodes that interact with files, such as the binary data node.
- If you want to persist [manual n8n encryption keys](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) between restarts. This saves a file containing the key into file storage during startup.

The `n8n-claim0-persistentvolumeclaim.yaml` manifest creates this, and the n8n Deployment mounts that claim in the `volumes` section of the `n8n-deployment.yaml` manifest.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br>…<br>volumes:<br>  - name: n8n-claim0<br>    persistentVolumeClaim:<br>      claimName: n8n-claim0<br>…<br>``` |

### Pod resources [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#pod-resources "Permanent link")

[Kubernetes lets you](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) optionally specify the minimum resources application containers need and the limits they can run to. The example YAML files cloned above contain the following in the `resources` section of the `n8n-deployment.yaml` file:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>``` | ```<br>…<br>resources:<br>  requests:<br>    memory: "250Mi"<br>  limits:<br>    memory: "500Mi"<br>…    <br>``` |

This defines a minimum of 250mb per container, a maximum of 500mb, and lets Kubernetes handle CPU. You can change these values to match your own needs. As a guide, here are the resources values for the n8n cloud offerings:

- **Start**: 320mb RAM, 10 millicore CPU burstable
- **Pro (10k executions)**: 640mb RAM, 20 millicore CPU burstable
- **Pro (50k executions)**: 1280mb RAM, 80 millicore CPU burstable

### Optional: Environment variables [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#optional-environment-variables "Permanent link")

You can configure n8n settings and behaviors using environment variables.

Create an `n8n-secret.yaml` file. Refer to [Environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/) for n8n environment variables details.

## Deployments [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#deployments "Permanent link")

The two deployment manifests ( `n8n-deployment.yaml` and `postgres-deployment.yaml`) define the n8n and Postgres applications to Kubernetes.

The manifests define the following:

- Send the environment variables defined to each application pod
- Define the container image to use
- Set resource consumption limits with the `resources` object
- The `volumes` defined earlier and `volumeMounts` to define the path in the container to mount volumes.
- Scaling and restart policies. The example manifests define one instance of each pod. You should change this to meet your needs.

## Services [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#services "Permanent link")

The two service manifests ( `postgres-service.yaml` and `n8n-service.yaml`) expose the services to the outside world using the Kubernetes load balancer using ports 5432 and 5678 respectively.

## Send to Kubernetes cluster [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#send-to-kubernetes-cluster "Permanent link")

Send all the manifests to the cluster with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>kubectl apply -f .<br>``` |

Namespace error

You may see an error message about not finding an "n8n" namespace as that resources isn't ready yet. You can run the same command again, or apply the namespace manifest first with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>kubectl apply -f namespace.yaml<br>``` |

## Set up DNS [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#set-up-dns "Permanent link")

n8n typically operates on a subdomain. Create a DNS record with your provider for the subdomain and point it to the IP address of the n8n service. Find the IP address of the n8n service from the **Services & ingresses** menu item of the cluster you want to use under the **External IP** column. You need to add the n8n port, "5678" to the URL.

Static IP addresses with AKS

[Read this tutorial](https://learn.microsoft.com/en-us/azure/aks/static-ip) for more details on how to use a static IP address with AKS.

## Delete resources [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#delete-resources "Permanent link")

Remove the resources created by the manifests with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>kubectl delete -f .<br>``` |

## Next steps [\#](https://docs.n8n.io/hosting/installation/server-setups/azure/\#next-steps "Permanent link")

- Learn more about [configuring](https://docs.n8n.io/hosting/configuration/environment-variables/) and [scaling](https://docs.n8n.io/hosting/scaling/overview/) n8n.
- Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/try-it-out/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top