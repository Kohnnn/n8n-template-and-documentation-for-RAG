---
url: "https://docs.n8n.io/hosting/installation/server-setups/heroku/"
title: "Heroku | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/installation/server-setups/heroku/#hosting-n8n-on-heroku)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/server-setups/heroku.md "Edit this page")

# Hosting n8n on Heroku [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#hosting-n8n-on-heroku "Permanent link")

This hosting guide shows you how to self-host n8n on Heroku. It uses:

- [Docker Compose](https://docs.docker.com/compose/) to create and define the application components and how they work together.
- [Heroku's PostgreSQL service](https://devcenter.heroku.com/categories/heroku-postgres) to host n8n's data storage.
- A **Deploy to Heroku** button offering a one click, with minor configuration, deployment.

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

## Use the deployment template to create a Heroku project [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#use-the-deployment-template-to-create-a-heroku-project "Permanent link")

The quickest way to get started with deploying n8n to Heroku is using the **Deploy to Heroku** button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/n8n-io/n8n-heroku/tree/main)

This opens the **Create New App** page on Heroku. Set a name for the project, and choose the region to deploy the project to.

### Configure environment variables [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#configure-environment-variables "Permanent link")

Heroku pre-fills the configuration options defined in the `env` section of the `app.json` file, which also sets default values for the environment variables n8n uses.

You can change any of these values to suit your needs. You must change the following values:

- **N8N\_ENCRYPTION\_KEY**, which n8n uses to [encrypt user account details](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/) before saving to the database.
- **WEBHOOK\_URL** should match the application name you create to ensure that webhooks have the correct URL.

### Deploy n8n [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#deploy-n8n "Permanent link")

Select **Deploy app**.

After Heroku builds and deploys the app it provides links to **Manage App** or **View** the application.

Heroku and DNS

Refer to the [Heroku documentation](https://devcenter.heroku.com/categories/networking-dns) to find out how to connect your domain to a Heroku application.

## Changing the deployment template [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#changing-the-deployment-template "Permanent link")

You can make changes to the deployment template by forking the [repository](https://github.com/n8n-io/n8n-heroku) and deploying from you fork.

### The Dockerfile [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#the-dockerfile "Permanent link")

By default the Dockerfile pulls the latest n8n image, if you want to use a different or fixed version, then update the image tag on the top line of the `Dockerfile`.

### Heroku and exposing ports [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#heroku-and-exposing-ports "Permanent link")

Heroku doesn't allow Docker-based applications to define an exposed port with the `EXPOSE` command. Instead, Heroku provides a `PORT` environment variable that it dynamically populates at application runtime. The `entrypoint.sh` file overrides the default Docker image command to instead set the port variable that Heroku provides. You can then access n8n on port 80 in a web browser.

Docker limitations with Heroku

[Read this guide](https://devcenter.heroku.com/articles/container-registry-and-runtime#unsupported-dockerfile-commands) for more details on the limitations of using Docker with Heroku.

### Configuring Heroku [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#configuring-heroku "Permanent link")

The `heroku.yml` file defines the application you want to create on Heroku. It consists of two sections:

- `setup` \> `addons` defines the Heroku addons to use. In this case, the PostgreSQL database addon.
- The `build` section defines how Heroku builds the application. In this case it uses the Docker buildpack to build a `web` service based on the supplied `Dockerfile`.

## Next steps [\#](https://docs.n8n.io/hosting/installation/server-setups/heroku/\#next-steps "Permanent link")

- Learn more about [configuring](https://docs.n8n.io/hosting/configuration/environment-variables/) and [scaling](https://docs.n8n.io/hosting/scaling/overview/) n8n.
- Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/try-it-out/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top