---
url: "https://docs.n8n.io/hosting/installation/npm/"
title: "npm | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/installation/npm/#npm)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/npm.md "Edit this page")

# npm [\#](https://docs.n8n.io/hosting/installation/npm/\#npm "Permanent link")

npm is a quick way to get started with n8n on your local machine. You must have [Node.js](https://nodejs.org/en/) installed. n8n requires Node.js 18 or above.

Latest and Next versions

n8n releases a new minor version most weeks. The `latest` version is for production use. `next` is the most recent release. You should treat `next` as a beta: it may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

Current `latest`: 1.94.1

Current `next`: 1.95.1

## Try n8n with npx [\#](https://docs.n8n.io/hosting/installation/npm/\#try-n8n-with-npx "Permanent link")

You can try n8n without installing it using npx.

From the terminal, run:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>npx n8n<br>``` |

This command will download everything that's needed to start n8n. You can then access n8n and start building workflows by opening [http://localhost:5678](http://localhost:5678/).

## Install globally with npm [\#](https://docs.n8n.io/hosting/installation/npm/\#install-globally-with-npm "Permanent link")

To install n8n globally, use npm:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>npm install n8n -g<br>``` |

To install or update to a specific version of n8n use the `@` syntax to specify the version. For example:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>npm install -g n8n@0.126.1<br>``` |

To install `next`:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>npm install -g n8n@next<br>``` |

After the installation, start n8n by running:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>n8n<br># or<br>n8n start<br>``` |

### Next steps [\#](https://docs.n8n.io/hosting/installation/npm/\#next-steps "Permanent link")

Try out n8n using the [Quickstarts](https://docs.n8n.io/try-it-out/).

## Updating [\#](https://docs.n8n.io/hosting/installation/npm/\#updating "Permanent link")

To update your n8n instance to the `latest` version, run:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>npm update -g n8n<br>``` |

To install the `next` version:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>npm install -g n8n@next<br>``` |

## n8n with tunnel [\#](https://docs.n8n.io/hosting/installation/npm/\#n8n-with-tunnel "Permanent link")

Danger

Use this for local development and testing. It isn't safe to use it in production.

To use webhooks for trigger nodes of external services like GitHub, n8n has to be reachable from the web. n8n runs a [tunnel service](https://github.com/localtunnel/localtunnel) that can redirect requests from n8n's servers to your local n8n instance.

Start n8n with `--tunnel` by running:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>n8n start --tunnel<br>``` |

## Reverting an upgrade [\#](https://docs.n8n.io/hosting/installation/npm/\#reverting-an-upgrade "Permanent link")

Install the older version that you want to go back to.

If the upgrade involved a database migration:

1. Check the feature documentation and release notes to see if there are any manual changes you need to make.
2. Run `n8n db:revert` on your current version to roll back the database. If you want to revert more than one database migration, you need to repeat this process.

## Windows troubleshooting [\#](https://docs.n8n.io/hosting/installation/npm/\#windows-troubleshooting "Permanent link")

If you are experiencing issues running n8n on Windows, make sure your Node.js environment is correctly set up. Follow Microsoft's guide to [Install NodeJS on Windows](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top