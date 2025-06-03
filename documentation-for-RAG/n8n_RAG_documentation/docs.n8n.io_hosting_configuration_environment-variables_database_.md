---
url: "https://docs.n8n.io/hosting/configuration/environment-variables/database/"
title: "Database environment variables | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/environment-variables/database/#database-environment-variables)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/database.md "Edit this page")

# Database environment variables [\#](https://docs.n8n.io/hosting/configuration/environment-variables/database/\#database-environment-variables "Permanent link")

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/hosting/configuration/configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

By default, n8n uses SQLite. n8n also supports PostgreSQL. n8n [removed support for MySQL and MariaDB](https://docs.n8n.io/1-0-migration-checklist/#mysql-and-mariadb) in v1.0.

This page outlines environment variables to configure your chosen database for your self-hosted n8n instance.

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `DB_TYPE`<br>/ `_FILE` | Enum string:<br>`sqlite`, `postgresdb` | `sqlite` | The database to use. |
| `DB_TABLE_PREFIX` | \* | - | Prefix to use for table names. |

## PostgreSQL [\#](https://docs.n8n.io/hosting/configuration/environment-variables/database/\#postgresql "Permanent link")

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `DB_POSTGRESDB_DATABASE`<br>/ `_FILE` | String | `n8n` | The name of the PostgreSQL database. |
| `DB_POSTGRESDB_HOST`<br>/ `_FILE` | String | `localhost` | The PostgreSQL host. |
| `DB_POSTGRESDB_PORT`<br>/ `_FILE` | Number | `5432` | The PostgreSQL port. |
| `DB_POSTGRESDB_USER`<br>/ `_FILE` | String | `postgres` | The PostgreSQL user. |
| `DB_POSTGRESDB_PASSWORD`<br>/ `_FILE` | String | - | The PostgreSQL password. |
| `DB_POSTGRESDB_POOL_SIZE`<br>/ `_FILE` | Number | `2` | Control how many parallel open Postgres connections n8n should have. Increasing it may help with resource utilization, but too many connections may degrade performance. |
| `DB_POSTGRESDB_CONNECTION_TIMEOUT`<br>/ `_FILE` | Number | `20000` | Postgres connection timeout (ms). |
| `DB_POSTGRESDB_SCHEMA`<br>/ `_FILE` | String | `public` | The PostgreSQL schema. |
| `DB_POSTGRESDB_SSL_ENABLED`<br>/ `_FILE` | Boolean | `false` | Whether to enable SSL. Automatically enabled if `DB_POSTGRESDB_SSL_CA`, `DB_POSTGRESDB_SSL_CERT` or `DB_POSTGRESDB_SSL_KEY` is defined. |
| `DB_POSTGRESDB_SSL_CA`<br>/ `_FILE` | String | - | The PostgreSQL SSL certificate authority. |
| `DB_POSTGRESDB_SSL_CERT`<br>/ `_FILE` | String | - | The PostgreSQL SSL certificate. |
| `DB_POSTGRESDB_SSL_KEY`<br>/ `_FILE` | String | - | The PostgreSQL SSL key. |
| `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED`<br>/ `_FILE` | Boolean | `true` | If n8n should reject unauthorized SSL connections (true) or not (false). |

## SQLite [\#](https://docs.n8n.io/hosting/configuration/environment-variables/database/\#sqlite "Permanent link")

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `DB_SQLITE_POOL_SIZE` | Number | `0` | Controls whether to open the SQLite file in [WAL mode](https://www.sqlite.org/wal.html) or [rollback journal mode](https://www.sqlite.org/lockingv3.html#rollback). Uses rollback journal mode when set to zero. When greater than zero, uses WAL mode with the value determining the number of parallel SQL read connections to configure. WAL mode is much more performant and reliable than the rollback journal mode. |
| `DB_SQLITE_VACUUM_ON_STARTUP` | Boolean | `false` | Runs [VACUUM](https://www.sqlite.org/lang_vacuum.html) operation on startup to rebuild the database. Reduces file size and optimizes indexes. This is a long running blocking operation and increases start-up time. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top