---
url: "https://docs.n8n.io/hosting/configuration/supported-databases-settings/"
title: "Supported databases and settings | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/supported-databases-settings/#supported-databases)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/supported-databases-settings.md "Edit this page")

# Supported databases [\#](https://docs.n8n.io/hosting/configuration/supported-databases-settings/\#supported-databases "Permanent link")

By default, n8n uses SQLite to save credentials, past executions, and workflows. n8n also supports PostgresDB.

## Shared settings [\#](https://docs.n8n.io/hosting/configuration/supported-databases-settings/\#shared-settings "Permanent link")

The following environment variables get used by all databases:

- `DB_TABLE_PREFIX` (default: -) - Prefix for table names

## PostgresDB [\#](https://docs.n8n.io/hosting/configuration/supported-databases-settings/\#postgresdb "Permanent link")

To use PostgresDB as the database, you can provide the following environment variables:

- `DB_TYPE=postgresdb`
- `DB_POSTGRESDB_DATABASE` (default: 'n8n')
- `DB_POSTGRESDB_HOST` (default: 'localhost')
- `DB_POSTGRESDB_PORT` (default: 5432)
- `DB_POSTGRESDB_USER` (default: 'postgres')
- `DB_POSTGRESDB_PASSWORD` (default: empty)
- `DB_POSTGRESDB_SCHEMA` (default: 'public')
- `DB_POSTGRESDB_SSL_CA` (default: undefined): Path to the server's CA certificate used to validate the connection (opportunistic encryption isn't supported)
- `DB_POSTGRESDB_SSL_CERT` (default: undefined): Path to the client's TLS certificate
- `DB_POSTGRESDB_SSL_KEY` (default: undefined): Path to the client's private key corresponding to the certificate
- `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED` (default: true): If TLS connections that fail validation should be rejected

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>``` | ```<br>export DB_TYPE=postgresdb<br>export DB_POSTGRESDB_DATABASE=n8n<br>export DB_POSTGRESDB_HOST=postgresdb<br>export DB_POSTGRESDB_PORT=5432<br>export DB_POSTGRESDB_USER=n8n<br>export DB_POSTGRESDB_PASSWORD=n8n<br>export DB_POSTGRESDB_SCHEMA=n8n<br># optional:<br>export DB_POSTGRESDB_SSL_CA=$(pwd)/ca.crt<br>export DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED=false<br>n8n start<br>``` |

### Required permissions [\#](https://docs.n8n.io/hosting/configuration/supported-databases-settings/\#required-permissions "Permanent link")

n8n needs to create and modify the schemas of the tables it uses.

Recommended permissions:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>CREATE DATABASE n8n-db;<br>CREATE USER n8n-user WITH PASSWORD 'random-password';<br>GRANT ALL PRIVILEGES ON DATABASE n8n-db TO n8n-user;<br>``` |

### TLS [\#](https://docs.n8n.io/hosting/configuration/supported-databases-settings/\#tls "Permanent link")

You can choose between these configurations:

- Not declaring (default): Connect with `SSL=off`
- Declaring only the CA and unauthorized flag: Connect with `SSL=on` and verify the server's signature
- Declaring `_{CERT,KEY}` and the above: Use the certificate and key for client TLS authentication

## SQLite [\#](https://docs.n8n.io/hosting/configuration/supported-databases-settings/\#sqlite "Permanent link")

This is the default database that gets used if nothing is defined.

The database file is located at:
`~/.n8n/database.sqlite`

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top