---
url: "https://docs.n8n.io/hosting/installation/server-setups/docker-compose/"
title: "Docker Compose | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/#docker-compose)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/server-setups/docker-compose.md "Edit this page")

# Docker-Compose [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#docker-compose "Permanent link")

If you have already installed Docker and Docker-Compose, then you can start with [step 3](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/#3-dns-setup).

You can find Docker Compose configurations for various architectures in the [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting).

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

## 1\. Install Docker and Docker Compose [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#1-install-docker-and-docker-compose "Permanent link")

How you install Docker and Docker Compose can vary depending on the Linux distribution you use. You can find detailed instructions in both the [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installation documentation. The following example is for Ubuntu:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>``` | ```<br># Remove incompatible or out of date Docker implementations if they exist<br>for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done<br># Install prereq packages<br>sudo apt-get update<br>sudo apt-get install ca-certificates curl<br># Download the repo signing key<br>sudo install -m 0755 -d /etc/apt/keyrings<br>sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc<br>sudo chmod a+r /etc/apt/keyrings/docker.asc<br># Configure the repository<br>echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null<br># Update and install Docker and Docker Compose<br>sudo apt-get update<br>sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin<br>``` |

Verify that Docker and Docker Compose are available by typing:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>docker --version<br>docker compose version<br>``` |

## 2\. Optional: Non-root user access [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#2-optional-non-root-user-access "Permanent link")

You can optionally grant access to run Docker without the `sudo` command.

To grant access to the user that you're currently logged in with (assuming they have `sudo` access), run:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>sudo usermod -aG docker ${USER}<br># Register the `docker` group memebership with current session without changing your primary group<br>exec sg docker newgrp<br>``` |

To grant access to a different user, type the following, substituting `<USER_TO_RUN_DOCKER>` with the appropriate username:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo usermod -aG docker <USER_TO_RUN_DOCKER><br>``` |

You will need to run `exec sg docker newgrp` from any of that user's existing sessions for it to access the new group permissions.

You can verify that your current session recognizes the `docker` group by typing:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>groups<br>``` |

## 3\. DNS setup [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#3-dns-setup "Permanent link")

To host n8n online or on a network, create a dedicated subdomain pointed at your server.

Add an A record to route the subdomain accordingly:

- **Type**: A
- **Name**: `n8n` (or the desired subdomain)
- **IP address**: (your server's IP address)

## 4\. Create an `.env` file [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#4-create-an-env-file "Permanent link")

Create a project directory to store your n8n environment configuration and Docker Compose files and navigate inside:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>mkdir n8n-compose<br>cd n8n-compose<br>``` |

Inside the `n8n-compose` directory, create an `.env` file to customize your n8n instance's details. Change it to match your own information:

| .env file |
| --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>``` | ```<br># DOMAIN_NAME and SUBDOMAIN together determine where n8n will be reachable from<br># The top level domain to serve from<br>DOMAIN_NAME=example.com<br># The subdomain to serve from<br>SUBDOMAIN=n8n<br># The above example serve n8n at: https://n8n.example.com<br># Optional timezone to set which gets used by Cron and other scheduling nodes<br># New York is the default value if not set<br>GENERIC_TIMEZONE=Europe/Berlin<br># The email address to use for the TLS/SSL certificate creation<br>SSL_EMAIL=user@example.com<br>``` |

## 5\. Create local files directory [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#5-create-local-files-directory "Permanent link")

Inside your project directory, create a directory called `local-files` for sharing files between the n8n instance and the host system (for example, using the [Read/Write Files from Disk node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/)):

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>mkdir local-files<br>``` |

The Docker Compose file below can automatically create this directory, but doing it manually ensures that it's created with the right ownership and permissions.

## 6\. Create Docker Compose file [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#6-create-docker-compose-file "Permanent link")

Create a `compose.yaml` file. Paste the following in the file:

| compose.yaml file |
| --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>``` | ```<br>services:<br>  traefik:<br>    image: "traefik"<br>    restart: always<br>    command:<br>      - "--api.insecure=true"<br>      - "--providers.docker=true"<br>      - "--providers.docker.exposedbydefault=false"<br>      - "--entrypoints.web.address=:80"<br>      - "--entrypoints.web.http.redirections.entryPoint.to=websecure"<br>      - "--entrypoints.web.http.redirections.entrypoint.scheme=https"<br>      - "--entrypoints.websecure.address=:443"<br>      - "--certificatesresolvers.mytlschallenge.acme.tlschallenge=true"<br>      - "--certificatesresolvers.mytlschallenge.acme.email=${SSL_EMAIL}"<br>      - "--certificatesresolvers.mytlschallenge.acme.storage=/letsencrypt/acme.json"<br>    ports:<br>      - "80:80"<br>      - "443:443"<br>    volumes:<br>      - traefik_data:/letsencrypt<br>      - /var/run/docker.sock:/var/run/docker.sock:ro<br>  n8n:<br>    image: docker.n8n.io/n8nio/n8n<br>    restart: always<br>    ports:<br>      - "127.0.0.1:5678:5678"<br>    labels:<br>      - traefik.enable=true<br>      - traefik.http.routers.n8n.rule=Host(`${SUBDOMAIN}.${DOMAIN_NAME}`)<br>      - traefik.http.routers.n8n.tls=true<br>      - traefik.http.routers.n8n.entrypoints=web,websecure<br>      - traefik.http.routers.n8n.tls.certresolver=mytlschallenge<br>      - traefik.http.middlewares.n8n.headers.SSLRedirect=true<br>      - traefik.http.middlewares.n8n.headers.STSSeconds=315360000<br>      - traefik.http.middlewares.n8n.headers.browserXSSFilter=true<br>      - traefik.http.middlewares.n8n.headers.contentTypeNosniff=true<br>      - traefik.http.middlewares.n8n.headers.forceSTSHeader=true<br>      - traefik.http.middlewares.n8n.headers.SSLHost=${DOMAIN_NAME}<br>      - traefik.http.middlewares.n8n.headers.STSIncludeSubdomains=true<br>      - traefik.http.middlewares.n8n.headers.STSPreload=true<br>      - traefik.http.routers.n8n.middlewares=n8n@docker<br>    environment:<br>      - N8N_HOST=${SUBDOMAIN}.${DOMAIN_NAME}<br>      - N8N_PORT=5678<br>      - N8N_PROTOCOL=https<br>      - NODE_ENV=production<br>      - WEBHOOK_URL=https://${SUBDOMAIN}.${DOMAIN_NAME}/<br>      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}<br>    volumes:<br>      - n8n_data:/home/node/.n8n<br>      - ./local-files:/files<br>volumes:<br>  n8n_data:<br>  traefik_data:<br>``` |

The above Docker Compose file configures two containers: one for n8n, and one to run [traefik](https://github.com/traefik/traefik), an application proxy to manage TLS/SSL certificates and handle routing.

It also creates and mounts two [Docker Volumes](https://docs.docker.com/engine/storage/volumes/) and mounts the `local-files` directory you created earlier:

| Name | Type | Container mount | Description |
| --- | --- | --- | --- |
| `n8n_data` | [Volume](https://docs.docker.com/engine/storage/volumes/) | `/home/node/.n8n` | Where n8n saves its SQLite database file and encryption key. |
| `traefik_data` | [Volume](https://docs.docker.com/engine/storage/volumes/) | `/letsencrypt` | Where traefik saves the TLS/SSL certificate data. |
| `./local-files` | [Bind](https://docs.docker.com/engine/storage/bind-mounts/) | `/files` | A local directory shared between the n8n instance and host. In n8n, use the `/files` path to read from and write to this directory. |

## 7\. Start Docker Compose [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#7-start-docker-compose "Permanent link")

You can now start n8n by typing:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker compose up -d<br>``` |

To stop the container, type:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>sudo docker compose stop<br>``` |

## 8\. Done [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#8-done "Permanent link")

You can now reach n8n using the subdomain + domain combination you defined in your `.env` file configuration. The above example would result in `https://n8n.example.com`.

n8n is only accessible using secure HTTPS, not over plain HTTP.

## Next steps [\#](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/\#next-steps "Permanent link")

- Learn more about [configuring](https://docs.n8n.io/hosting/configuration/environment-variables/) and [scaling](https://docs.n8n.io/hosting/scaling/overview/) n8n.
- Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/try-it-out/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top