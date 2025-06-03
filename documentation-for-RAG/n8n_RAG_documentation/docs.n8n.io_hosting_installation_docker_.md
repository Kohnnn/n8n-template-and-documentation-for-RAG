---
url: "https://docs.n8n.io/hosting/installation/docker/"
title: "Docker | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/installation/docker/#docker-installation)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/docker.md "Edit this page")

# Docker Installation [\#](https://docs.n8n.io/hosting/installation/docker/\#docker-installation "Permanent link")

[Docker](https://www.docker.com/) offers the following advantages:

- Installs n8n in a clean environment.
- Easier setup for your preferred database.
- Can avoid issues due to different operating systems, as Docker provides a consistent system.
- Can avoid compatibility issues due to differences in operating systems and tools.
- Makes migrating to new hosts or environments more straightforward.

You can also use n8n in Docker with [Docker Compose](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/). You can find Docker Compose configurations for various architectures in the [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting).

Self-hosting knowledge prerequisites

Self-hosting n8n requires technical knowledge, including:

- Setting up and configuring servers and containers
- Managing application resources and scaling
- Securing servers and applications
- Configuring n8n

n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, n8n recommends [n8n Cloud](https://n8n.io/cloud/).

## Prerequisites [\#](https://docs.n8n.io/hosting/installation/docker/\#prerequisites "Permanent link")

Before proceeding, install [Docker Desktop](https://docs.docker.com/get-docker/).

Linux Users

Docker Desktop is available for Mac and Windows. Linux users must install [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) individually for your distribution.

Latest and Next versions

n8n releases a new minor version most weeks. The `latest` version is for production use. `next` is the most recent release. You should treat `next` as a beta: it may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

Current `latest`: 1.94.1

Current `next`: 1.95.1

## Starting n8n [\#](https://docs.n8n.io/hosting/installation/docker/\#starting-n8n "Permanent link")

From your terminal, run:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>docker volume create n8n_data<br>docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n<br>``` |

This command creates a volume to store persistent data, downloads the required n8n image, and starts your container, exposed on port `5678`. To save your work between container restarts, it also mounts a docker volume, `n8n_data`, to persist your data locally.

Once running, you can access n8n by opening:
[http://localhost:5678](http://localhost:5678/)

## Using with PostgreSQL [\#](https://docs.n8n.io/hosting/installation/docker/\#using-with-postgresql "Permanent link")

By default, n8n uses SQLite to save [credentials](https://docs.n8n.io/glossary/#credential-n8n), past executions, and workflows. n8n also supports PostgreSQL, configurable using environment variables as detailed below.

When using PostgreSQL, it's still important to persist the data stored in the `/home/node/.n8n` folder. This includes n8n user data and, even more importantly, the encryption key for credentials. It's also the name of the webhook when using the [n8n tunnel](https://docs.n8n.io/hosting/installation/docker/#n8n-with-tunnel).

If n8n can't find the `/home/node/.n8n` directory on startup, it automatically creates one. In this case, all existing credentials that n8n saved with a different encryption key will no longer work.

Keep in mind

While persisting the `/home/node/.n8n` directory with PostgreSQL is the recommended best practice, it's not explicitly required. You can provide the encryption key by passing the [`N8N_ENCRYPTION_KEY` environment variable](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) when starting your Docker container.

To use n8n with PostgreSQL, execute the following commands, replacing the placeholders (depicted within angled brackets, for example `<POSTGRES_USER>`) with your actual values:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>``` | ```<br>docker volume create n8n_data<br>docker run -it --rm \<br> --name n8n \<br> -p 5678:5678 \<br> -e DB_TYPE=postgresdb \<br> -e DB_POSTGRESDB_DATABASE=<POSTGRES_DATABASE> \<br> -e DB_POSTGRESDB_HOST=<POSTGRES_HOST> \<br> -e DB_POSTGRESDB_PORT=<POSTGRES_PORT> \<br> -e DB_POSTGRESDB_USER=<POSTGRES_USER> \<br> -e DB_POSTGRESDB_SCHEMA=<POSTGRES_SCHEMA> \<br> -e DB_POSTGRESDB_PASSWORD=<POSTGRES_PASSWORD> \<br> -v n8n_data:/home/node/.n8n \<br> docker.n8n.io/n8nio/n8n<br>``` |

You can find a complete `docker-compose` file for PostgreSQL in the [n8n hosting repository](https://github.com/n8n-io/n8n-hosting/tree/main/docker-compose/withPostgres).

## Setting timezone [\#](https://docs.n8n.io/hosting/installation/docker/\#setting-timezone "Permanent link")

To define the timezone n8n should use, you can set the [`GENERIC_TIMEZONE` environment variable](https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/). Schedule-oriented nodes, like the [Schedule Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/) use this to determine the correct timezone.

You can set the system timezone, which controls what some scripts and commands like `date` return, using the `TZ` environment variable.

This example sets the same timezone for both variables:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>docker volume create n8n_data<br>docker run -it --rm \<br> --name n8n \<br> -p 5678:5678 \<br> -e GENERIC_TIMEZONE="Europe/Berlin" \<br> -e TZ="Europe/Berlin" \<br> -v n8n_data:/home/node/.n8n \<br> docker.n8n.io/n8nio/n8n<br>``` |

## Updating [\#](https://docs.n8n.io/hosting/installation/docker/\#updating "Permanent link")

To update n8n, in Docker Desktop, navigate to the **Images** tab and select **Pull** from the context menu to download the latest n8n image:

[![Docker Desktop](https://docs.n8n.io/_images/hosting/installation/docker/docker_desktop.png)](https://docs.n8n.io/_images/hosting/installation/docker/docker_desktop.png)

You can also use the command line to pull the latest, or a specific version:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br># Pull latest (stable) version<br>docker pull docker.n8n.io/n8nio/n8n<br># Pull specific version<br>docker pull docker.n8n.io/n8nio/n8n:1.81.0<br># Pull next (unstable) version<br>docker pull docker.n8n.io/n8nio/n8n:next<br>``` |

After pulling the updated image, stop your n8n container and start it again. You can also use the command line. Replace `<container_id>` in the commands below with the container ID you find in the first command:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># Find your container ID<br>docker ps -a<br># Stop the container with the `<container_id>`<br>docker stop <container_id><br># Remove the container with the `<container_id>`<br>docker rm <container_id><br># Start the container<br>docker run --name=<container_name> [options] -d docker.n8n.io/n8nio/n8n<br>``` |

### Updating Docker Compose [\#](https://docs.n8n.io/hosting/installation/docker/\#updating-docker-compose "Permanent link")

If you run n8n using a Docker Compose file, follow these steps to update n8n:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br># Pull latest version<br>docker compose pull<br># Stop and remove older version<br>docker compose down<br># Start the container<br>docker compose up -d<br>``` |

## Further reading [\#](https://docs.n8n.io/hosting/installation/docker/\#further-reading "Permanent link")

You can find more information about Docker setup in the README file for the [Docker image](https://github.com/n8n-io/n8n/tree/master/docker/images/n8n).

## n8n with tunnel [\#](https://docs.n8n.io/hosting/installation/docker/\#n8n-with-tunnel "Permanent link")

Danger

Use this for local development and testing. It isn't safe to use it in production.

To use webhooks for trigger nodes of external services like GitHub, n8n has to be reachable from the web. n8n runs a [tunnel service](https://github.com/localtunnel/localtunnel) that can redirect requests from n8n's servers to your local n8n instance.

Start n8n with `--tunnel` by running:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br>docker volume create n8n_data<br>docker run -it --rm \<br> --name n8n \<br> -p 5678:5678 \<br> -v n8n_data:/home/node/.n8n \<br> docker.n8n.io/n8nio/n8n \<br> start --tunnel<br>``` |

## Next steps [\#](https://docs.n8n.io/hosting/installation/docker/\#next-steps "Permanent link")

- Learn more about [configuring](https://docs.n8n.io/hosting/configuration/environment-variables/) and [scaling](https://docs.n8n.io/hosting/scaling/overview/) n8n.
- Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/try-it-out/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top