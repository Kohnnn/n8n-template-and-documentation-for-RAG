---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/"
title: "TimescaleDB node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/#timescaledb-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md "Edit this page")

# TimescaleDB node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/\#timescaledb-node "Permanent link")

Use the TimescaleDB node to automate work in TimescaleDB, and integrate TimescaleDB with other applications. n8n has built-in support for a wide range of TimescaleDB features, including executing an SQL query, as well as inserting and updating rows in a database.

On this page, you'll find a list of operations the TimescaleDB node supports and links to more resources.

Credentials

Refer to [TimescaleDB credentials](https://docs.n8n.io/integrations/builtin/credentials/timescaledb/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/\#operations "Permanent link")

- Execute an SQL query
- Insert rows in database
- Update rows in database

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/\#templates-and-examples "Permanent link")

[Browse TimescaleDB integration templates](https://n8n.io/integrations/timescaledb/), or [search all templates](https://n8n.io/workflows/)

## Specify a column's data type [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/\#specify-a-columns-data-type "Permanent link")

To specify a column's data type, append the column name with `:type`, where `type` is the data type you want for the column. For example, if you want to specify the type `int` for the column **id** and type `text` for the column **name**, you can use the following snippet in the **Columns** field: `id:int,name:text`.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top