---
url: "https://docs.n8n.io/hosting/architecture/database-structure/"
title: "Database structure | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/architecture/database-structure/#database-structure)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/architecture/database-structure.md "Edit this page")

# Database structure [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#database-structure "Permanent link")

This page describes the purpose of each table in the n8n database.

## Database and query technology [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#database-and-query-technology "Permanent link")

By default, n8n uses SQLite as the database. If you are using another database the structure will be similar, but the data-types may be different depending on the database.

n8n uses [TypeORM](https://github.com/typeorm/typeorm) for queries and migrations.

To inspect the n8n database, you can use [DBeaver](https://dbeaver.io/), which is an open-source universal database tool.

## Tables [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#tables "Permanent link")

These are the tables n8n creates during setup.

### auth\_identity [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#auth_identity "Permanent link")

Stores details of external authentication providers when using [SAML](https://docs.n8n.io/user-management/saml/).

### auth\_provider\_sync\_history [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#auth_provider_sync_history "Permanent link")

Stores the history of a SAML connection.

### credentials\_entity [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#credentials_entity "Permanent link")

Stores the [credentials](https://docs.n8n.io/glossary/#credential-n8n) used to authenticate with integrations.

### event\_destinations [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#event_destinations "Permanent link")

Contains the destination configurations for [Log streaming](https://docs.n8n.io/log-streaming/).

### execution\_data [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#execution_data "Permanent link")

Contains the workflow at time of running, and the execution data.

### execution\_entity [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#execution_entity "Permanent link")

Stores all saved workflow executions. Workflow settings can affect which executions n8n saves.

### execution\_metadata [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#execution_metadata "Permanent link")

Stores [Custom executions data](https://docs.n8n.io/workflows/executions/custom-executions-data/).

### installed\_nodes [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#installed_nodes "Permanent link")

Lists the [community nodes](https://docs.n8n.io/integrations/community-nodes/installation/) installed in your n8n instance.

### installed\_packages [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#installed_packages "Permanent link")

Details of npm community nodes packages installed in your n8n instance. [installed\_nodes](https://docs.n8n.io/hosting/architecture/database-structure/#installed_nodes) lists each individual node. `installed_packages` lists npm packages, which may contain more than one node.

### migrations [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#migrations "Permanent link")

A log of all database migrations. Read more about [Migrations](https://github.com/typeorm/typeorm/blob/master/docs/migrations.md) in TypeORM's documentation.

### project [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#project "Permanent link")

Lists the [projects](https://docs.n8n.io/user-management/rbac/projects/) in your instance.

### project\_relation [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#project_relation "Permanent link")

Describes the relationship between a user and a [project](https://docs.n8n.io/user-management/rbac/projects/), including the user's [role type](https://docs.n8n.io/user-management/rbac/role-types/).

### role [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#role "Permanent link")

Not currently used. Foruse in future work on custom roles.

### settings [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#settings "Permanent link")

Records custom instance settings. These are settings that you can't control using environment variables. They include:

- Whether the instance owner is set up
- Whether the user chose to skip owner and user management setup
- License key

### shared\_credentials [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#shared_credentials "Permanent link")

Maps credentials to users.

### shared\_workflow [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#shared_workflow "Permanent link")

Maps workflows to users.

### tag\_entity [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#tag_entity "Permanent link")

All workflow tags created in the n8n instance. This table lists the tags. [workflows\_tags](https://docs.n8n.io/hosting/architecture/database-structure/#workflows_tags) records which workflows have which tags.

### user [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#user "Permanent link")

Contains user data.

### variables [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#variables "Permanent link")

Store [variables](https://docs.n8n.io/code/variables/).

### webhook\_entity [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#webhook_entity "Permanent link")

Records the active webhooks in your n8n instance's workflows. This isn't just webhooks uses in the Webhook node. It includes all active webhooks used by any trigger node.

### workflow\_entity [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#workflow_entity "Permanent link")

Your n8n instance's saved workflows.

### workflow\_history [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#workflow_history "Permanent link")

Store previous versions of workflows.

### workflow\_statistics [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#workflow_statistics "Permanent link")

Counts workflow IDs and their status.

### workflows\_tags [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#workflows_tags "Permanent link")

Maps tags to workflows. [tag\_entity](https://docs.n8n.io/hosting/architecture/database-structure/#tag_entity) contains tag details.

## Entity Relationship Diagram (ERD) [\#](https://docs.n8n.io/hosting/architecture/database-structure/\#entity-relationship-diagram-erd "Permanent link")

[!["n8n ERD"](https://docs.n8n.io/_images/hosting/architecture/n8n-database-diagram.png)](https://docs.n8n.io/_images/hosting/architecture/n8n-database-diagram.png)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top