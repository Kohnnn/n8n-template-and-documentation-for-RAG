---
url: "https://docs.n8n.io/hosting/installation/server-setups/hetzner/"
title: "Hetzner | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/installation/server-setups/hetzner/#hosting-n8n-on-hetzner-cloud)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/server-setups/hetzner.md "Edit this page")

# Hosting n8n on Hetzner cloud [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#hosting-n8n-on-hetzner-cloud "Permanent link")

This hosting guide shows you how to self-host n8n on a Hetzner cloud server. It uses:

- [Caddy](https://caddyserver.com/) (a reverse proxy) to allow access to the Server from the internet.
- [Docker Compose](https://docs.docker.com/compose/) to create and define the application components and how they work together.

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

## Create a server [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#create-a-server "Permanent link")

1. [Log in](https://console.hetzner.cloud/) to the Hetzner Cloud Console.
2. Select the project to host the server, or create a new project by selecting **\+ NEW PROJECT**.
3. Select **\+ CREATE SERVER** on the project tile you want to add it to.

You can change most of the settings to suit your needs, but as this guide uses Docker to run the application, under the **Image** section, select "Docker CE" from the **APPS** tab.

Type

When creating the server, Hetzner asks you to choose a plan. For most usage levels, the CPX11 type is enough.

SSH keys

Hetzner lets you choose between SSH and password-based authentication. SSH is more secure. The rest of this guide assumes you are using SSH.

## Log in to your server [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#log-in-to-your-server "Permanent link")

The rest of this guide requires you to log in to the server using a terminal with SSH. Refer to [Access with SSH/rsync/BorgBackup](https://docs.hetzner.com/robot/storage-box/access/access-ssh-rsync-borg) for more information. You can find the public IP in the listing of the servers in your project.

## Install Docker Compose [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#install-docker-compose "Permanent link")

The Hetzner Docker app image doesn't have Docker compose installed. Install it with the following commands:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>apt update && apt -y upgrade<br>apt install docker-compose-plugin<br>``` |

## Clone configuration repository [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#clone-configuration-repository "Permanent link")

Docker Compose, n8n, and Caddy require a series of folders and configuration files. You can clone these from [this repository](https://github.com/n8n-io/n8n-docker-caddy) into the root user folder of the server. The following steps will tell you which file to change and what changes to make.

Clone the repository with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>git clone https://github.com/n8n-io/n8n-docker-caddy.git<br>``` |

And change directory to the root of the repository you cloned:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>cd n8n-docker-caddy<br>``` |

## Default folders and files [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#default-folders-and-files "Permanent link")

The host operating system (the server) copies the two folders you created to Docker containers to make them available to Docker. The two folders are:

- `caddy_config`: Holds the Caddy configuration files.
- `local_files`: A folder for files you upload or add using n8n.

### Create Docker volume [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#create-docker-volume "Permanent link")

To persist the Caddy cache between restarts and speed up start times, create [a Docker volume](https://docs.docker.com/storage/volumes/) that Docker reuses between restarts:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>docker volume create caddy_data<br>``` |

Create a Docker volume for the n8n data:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker volume create n8n_data<br>``` |

## Set up DNS [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#set-up-dns "Permanent link")

n8n typically operates on a subdomain. Create a DNS record with your provider for the subdomain and point it to the IP address of the server. The exact steps for this depend on your DNS provider, but typically you need to create a new "A" record for the n8n subdomain. DigitalOcean provide [An Introduction to DNS Terminology, Components, and Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-dns-terminology-components-and-concepts).

## Open ports [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#open-ports "Permanent link")

n8n runs as a web application, so the server needs to allow incoming access to traffic on port 80 for non-secure traffic, and port 443 for secure traffic.

Open the following ports in the server's firewall by running the following two commands:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>sudo ufw allow 80<br>sudo ufw allow 443<br>``` |

## Configure n8n [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#configure-n8n "Permanent link")

n8n needs some environment variables set to pass to the application running in the Docker container. The example `.env` file contains placeholders you need to replace with values of your own.

Open the file with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>nano .env<br>``` |

The file contains inline comments to help you know what to change.

Refer to [Environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/) for n8n environment variables details.

## The Docker Compose file [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#the-docker-compose-file "Permanent link")

The Docker Compose file ( `docker-compose.yml`) defines the services the application needs, in this case Caddy and n8n.

- The Caddy service definition defines the ports it uses and the local volumes to copy to the containers.
- The n8n service definition defines the ports it uses, the environment variables n8n needs to run (some defined in the `.env` file), and the volumes it needs to copy to the containers.

The Docker Compose file uses the environment variables set in the `.env` file, so you shouldn't need to change it's content, but to take a look, run the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>nano docker-compose.yml<br>``` |

## Configure Caddy [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#configure-caddy "Permanent link")

Caddy needs to know which domains it should serve, and which port to expose to the outside world. Edit the `Caddyfile` file in the `caddy_config` folder.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>nano caddy_config/Caddyfile<br>``` |

Change the placeholder subdomain to yours. If you followed the steps to name the subdomain n8n, your full domain is similar to `n8n.example.com`. The `n8n` in the `reverse_proxy` setting tells Caddy to use the service definition defined in the `docker-compose.yml` file:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>n8n.<domain>.<suffix> {<br>    reverse_proxy n8n:5678 {<br>      flush_interval -1<br>    }<br>}<br>``` |

## Start Docker Compose [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#start-docker-compose "Permanent link")

Start n8n and Caddy with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>docker compose up -d<br>``` |

This may take a few minutes.

## Test your setup [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#test-your-setup "Permanent link")

In your browser, open the URL formed of the subdomain and domain name defined earlier. Enter the user name and password defined earlier, and you should be able to access n8n.

## Stop n8n and Caddy [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#stop-n8n-and-caddy "Permanent link")

You can stop n8n and Caddy with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker compose stop<br>``` |

## Updating [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#updating "Permanent link")

If you run n8n using a Docker Compose file, follow these steps to update n8n:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br># Pull latest version<br>docker compose pull<br># Stop and remove older version<br>docker compose down<br># Start the container<br>docker compose up -d<br>``` |

## Next steps [\#](https://docs.n8n.io/hosting/installation/server-setups/hetzner/\#next-steps "Permanent link")

- Learn more about [configuring](https://docs.n8n.io/hosting/configuration/environment-variables/) and [scaling](https://docs.n8n.io/hosting/scaling/overview/) n8n.
- Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/try-it-out/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top