---
url: "https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/"
title: "Digital Ocean | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/#hosting-n8n-on-digitalocean)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/server-setups/digital-ocean.md "Edit this page")

# Hosting n8n on DigitalOcean [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#hosting-n8n-on-digitalocean "Permanent link")

This hosting guide shows you how to self-host n8n on a DigitalOcean droplet. It uses:

- [Caddy](https://caddyserver.com/) (a reverse proxy) to allow access to the Droplet from the internet. Caddy will also automatically create and manage SSL / TLS certificates for your n8n instance.
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

## Create a Droplet [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#create-a-droplet "Permanent link")

1. [Log in](https://cloud.digitalocean.com/login) to DigitalOcean.
2. Select the project to host the Droplet, or [create a new project](https://docs.digitalocean.com/products/projects/how-to/create/).
3. In your project, select **Droplets** from the **Manage** menu.
4. [Create a new Droplet](https://docs.digitalocean.com/products/droplets/how-to/create/) using the [Docker image](https://marketplace.digitalocean.com/apps/docker) available on the **Marketplace** tab.

Droplet resources

When creating the Droplet, DigitalOcean asks you to choose a plan. For most usage levels, a basic shared CPU plan is enough.

SSH key or Password

DigitalOcean lets you choose between SSH key and password-based authentication. SSH keys are considered more secure.

## Log in to your Droplet and create new user [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#log-in-to-your-droplet-and-create-new-user "Permanent link")

The rest of this guide requires you to log in to the Droplet using a terminal with SSH. Refer to [How to Connect to Droplets with SSH](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/) for more information.

You should create a new user, to avoid working as the root user:

1. Log in as root.
2. Create a new user:



|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>adduser <username><br>``` |

3. Follow the prompts in the CLI to finish creating the user.
4. Grant the new user administrative privileges:



|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>usermod -aG sudo <username><br>``` |



    You can now run commands with superuser privileges by using `sudo` before the command.
5. Follow the steps to set up SSH for the new user: [Add Public Key Authentication](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04#step-four-add-public-key-authentication-recommended).
6. Log out of the droplet.
7. Log in using SSH as the new user.

## Clone configuration repository [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#clone-configuration-repository "Permanent link")

Docker Compose, n8n, and Caddy require a series of folders and configuration files. You can clone these from [this repository](https://github.com/n8n-io/n8n-docker-caddy) into the home folder of the logged-in user on your Droplet. The following steps will tell you which file to change and what changes to make.

Clone the repository with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>git clone https://github.com/n8n-io/n8n-docker-caddy.git<br>``` |

And change directory to the root of the repository you cloned:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>cd n8n-docker-caddy<br>``` |

## Default folders and files [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#default-folders-and-files "Permanent link")

The host operating system (the DigitalOcean Droplet) copies the two folders you created to Docker containers to make them available to Docker. The two folders are:

- `caddy_config`: Holds the Caddy configuration files.
- `local_files`: A folder for files you upload or add using n8n.

### Create Docker volumes [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#create-docker-volumes "Permanent link")

To persist the Caddy cache between restarts and speed up start times, create [a Docker volume](https://docs.docker.com/storage/volumes/) that Docker reuses between restarts:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker volume create caddy_data<br>``` |

Create a Docker volume for the n8n data:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker volume create n8n_data<br>``` |

## Set up DNS [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#set-up-dns "Permanent link")

n8n typically operates on a subdomain. Create a DNS record with your provider for the subdomain and point it to the IP address of the Droplet. The exact steps for this depend on your DNS provider, but typically you need to create a new "A" record for the n8n subdomain. DigitalOcean provide [An Introduction to DNS Terminology, Components, and Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-dns-terminology-components-and-concepts).

## Open ports [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#open-ports "Permanent link")

n8n runs as a web application, so the Droplet needs to allow incoming access to traffic on port 80 for non-secure traffic, and port 443 for secure traffic.

Open the following ports in the Droplet's firewall by running the following two commands:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>sudo ufw allow 80<br>sudo ufw allow 443<br>``` |

## Configure n8n [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#configure-n8n "Permanent link")

n8n needs some environment variables set to pass to the application running in the Docker container. The example `.env` file contains placeholders you need to replace with values of your own.

Open the file with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>nano .env<br>``` |

The file contains inline comments to help you know what to change.

Refer to [Environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/) for n8n environment variables details.

## The Docker Compose file [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#the-docker-compose-file "Permanent link")

The Docker Compose file ( `docker-compose.yml`) defines the services the application needs, in this case Caddy and n8n.

- The Caddy service definition defines the ports it uses and the local volumes to copy to the containers.
- The n8n service definition defines the ports it uses, the environment variables n8n needs to run (some defined in the `.env` file), and the volumes it needs to copy to the containers.

The Docker Compose file uses the environment variables set in the `.env` file, so you shouldn't need to change it's content, but to take a look, run the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>nano docker-compose.yml<br>``` |

## Configure Caddy [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#configure-caddy "Permanent link")

Caddy needs to know which domains it should serve, and which port to expose to the outside world. Edit the `Caddyfile` file in the `caddy_config` folder.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>nano caddy_config/Caddyfile<br>``` |

Change the placeholder domain to yours. If you followed the steps to name the subdomain n8n, your full domain is similar to `n8n.example.com`. The `n8n` in the `reverse_proxy` setting tells Caddy to use the service definition defined in the `docker-compose.yml` file:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>n8n.<domain>.<suffix> {<br>    reverse_proxy n8n:5678 {<br>      flush_interval -1<br>    }<br>}<br>``` |

If you were to use `automate.example.com`, your `Caddyfile` may look something like:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>automate.example.com {<br>    reverse_proxy n8n:5678 {<br>      flush_interval -1<br>    }<br>}<br>``` |

## Start Docker Compose [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#start-docker-compose "Permanent link")

Start n8n and Caddy with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker compose up -d<br>``` |

This may take a few minutes.

## Test your setup [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#test-your-setup "Permanent link")

In your browser, open the URL formed of the subdomain and domain name defined earlier. Enter the user name and password defined earlier, and you should be able to access n8n.

## Stop n8n and Caddy [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#stop-n8n-and-caddy "Permanent link")

You can stop n8n and Caddy with the following command:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker compose stop<br>``` |

## Updating [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#updating "Permanent link")

If you run n8n using a Docker Compose file, follow these steps to update n8n:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br># Pull latest version<br>docker compose pull<br># Stop and remove older version<br>docker compose down<br># Start the container<br>docker compose up -d<br>``` |

## Next steps [\#](https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/\#next-steps "Permanent link")

- Learn more about [configuring](https://docs.n8n.io/hosting/configuration/environment-variables/) and [scaling](https://docs.n8n.io/hosting/scaling/overview/) n8n.
- Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/try-it-out/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top