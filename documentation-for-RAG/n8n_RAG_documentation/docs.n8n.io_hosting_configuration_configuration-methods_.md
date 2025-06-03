---
url: "https://docs.n8n.io/hosting/configuration/configuration-methods/"
title: "Configuration methods | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-methods/#configuration)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-methods.md "Edit this page")

# Configuration [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#configuration "Permanent link")

You can change n8n's settings using environment variables. For a full list of available configurations see [Environment Variables](https://docs.n8n.io/hosting/configuration/environment-variables/).

## Set environment variables by command line [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#set-environment-variables-by-command-line "Permanent link")

### npm [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#npm "Permanent link")

For npm, set your desired environment variables in terminal using the `export` command as shown below:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export <variable>=<value><br>``` |

### Docker [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#docker "Permanent link")

In Docker you can use the `-e` flag from the command line:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>docker run -it --rm \<br> --name n8n \<br> -p 5678:5678 \<br> -e N8N_TEMPLATES_ENABLED="false" \<br> docker.n8n.io/n8nio/n8n<br>``` |

## Set environment variables using a file [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#set-environment-variables-using-a-file "Permanent link")

You can also configure n8n using a configuration file.

Only define the values that need to be different from the default in your configuration file. You can use multiple files. For example, you can have a file with generic base settings, and files with specific values for different environments.

### npm [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#npm_1 "Permanent link")

Set the path to the JSON configuration file using the environment variable `N8N_CONFIG_FILES`:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br># Bash - Single file<br>export N8N_CONFIG_FILES=/<path-to-config>/my-config.json<br># Bash - Multiple files are comma-separated<br>export N8N_CONFIG_FILES=/<path-to-config>/my-config.json,/<path-to-config>/production.json<br># PowerShell - Single file, persist for current user<br># Note that setting scope (Process, User, Machine) has no effect on Unix systems<br>[Environment]::SetEnvironmentVariable('N8N_CONFIG_FILES', '<path-to-config>\config.json', 'User')<br>``` |

Example file:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>{<br> "executions": {<br>  "saveDataOnSuccess": "none"<br> },<br> "generic": {<br>  "timezone": "Europe/Berlin"<br> },<br> "nodes": {<br>  "exclude": "[\"n8n-nodes-base.executeCommand\",\"n8n-nodes-base.writeBinaryFile\"]"<br> }<br>}<br>``` |

Formatting as JSON

You can't always work out the correct JSON from the [Environment variables reference](https://docs.n8n.io/hosting/configuration/environment-variables/). For example, to set `N8N_METRICS` to `true`, you need to do:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>``` | ```<br>{<br>	"endpoints": {<br>		"metrics": {<br>			"enable": true<br>		}<br>	}<br>}<br>``` |

Refer to the [Schema file in the source code](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/config/schema.ts) for full details of the expected settings.

### Docker [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#docker_1 "Permanent link")

In Docker, you can set your environment variables in the `n8n: environment:` element of your `docker-compose.yaml` file.

For example:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>n8n:<br>    environment:<br>      - N8N_TEMPLATES_ENABLED=false<br>``` |

### Keeping sensitive data in separate files [\#](https://docs.n8n.io/hosting/configuration/configuration-methods/\#keeping-sensitive-data-in-separate-files "Permanent link")

You can append `_FILE` to individual environment variables to provide their configuration in a separate file, enabling you to avoid passing sensitive details using environment variables. n8n loads the data from the file with the given name, making it possible to load data from [Docker-Secrets](https://docs.docker.com/engine/swarm/secrets/) and [Kubernetes-Secrets](https://kubernetes.io/docs/concepts/configuration/secret/).

Refer to [Environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/) for details on each variable.

While most environment variables can use the `_FILE` suffix, it's more beneficial for sensitive data such as [credentials](https://docs.n8n.io/glossary/#credential-n8n) and database configuration. Here are some examples:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>``` | ```<br>CREDENTIALS_OVERWRITE_DATA_FILE=/path/to/credentials_data<br>DB_TYPE_FILE=/path/to/db_type<br>DB_POSTGRESDB_DATABASE_FILE=/path/to/database_name<br>DB_POSTGRESDB_HOST_FILE=/path/to/database_host<br>DB_POSTGRESDB_PORT_FILE=/path/to/database_port<br>DB_POSTGRESDB_USER_FILE=/path/to/database_user<br>DB_POSTGRESDB_PASSWORD_FILE=/path/to/database_password<br>DB_POSTGRESDB_SCHEMA_FILE=/path/to/database_schema<br>DB_POSTGRESDB_SSL_CA_FILE=/path/to/ssl_ca<br>DB_POSTGRESDB_SSL_CERT_FILE=/path/to/ssl_cert<br>DB_POSTGRESDB_SSL_KEY_FILE=/path/to/ssl_key<br>DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED_FILE=/path/to/ssl_reject_unauth<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top