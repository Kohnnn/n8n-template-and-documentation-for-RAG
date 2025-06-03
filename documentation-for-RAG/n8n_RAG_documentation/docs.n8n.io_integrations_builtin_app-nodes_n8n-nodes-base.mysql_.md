---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/"
title: "MySQL node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/#mysql-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.mysql/index.md "Edit this page")

# MySQL node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/\#mysql-node "Permanent link")

Use the MySQL node to automate work in MySQL, and integrate MySQL with other applications. n8n has built-in support for a wide range of MySQL features, including executing an SQL query, as well as inserting, and updating rows in a database.

On this page, you'll find a list of operations the MySQL node supports and links to more resources.

Credentials

Refer to [MySQL credentials](https://docs.n8n.io/integrations/builtin/credentials/mysql/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/\#operations "Permanent link")

- Delete
- Execute SQL
- Insert
- Insert or Update
- Select
- Update

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/\#templates-and-examples "Permanent link")

**Generate SQL queries from schema only - AI-powered**

by Yulia

[View template details](https://n8n.io/workflows/2508-generate-sql-queries-from-schema-only-ai-powered/)

**Import CSV into MySQL**

by Eduard

[View template details](https://n8n.io/workflows/1839-import-csv-into-mysql/)

**Build an AI-Powered Tech Radar Advisor with SQL DB, RAG, and Routing Agents**

by Sean Lon

[View template details](https://n8n.io/workflows/3151-build-an-ai-powered-tech-radar-advisor-with-sql-db-rag-and-routing-agents/)

[Browse MySQL integration templates](https://n8n.io/integrations/mysql/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/\#related-resources "Permanent link")

Refer to [MySQL's Connectors and APIs documentation](https://dev.mysql.com/doc/index-connectors.html) for more information about the service.

Refer to MySQL's [SELECT statement documentation](https://dev.mysql.com/doc/refman/8.4/en/select.html) for more information on writing SQL queries.

## Use query parameters [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/\#use-query-parameters "Permanent link")

When creating a query to run on a MySQL database, you can use the **Query Parameters** field in the **Options** section to load data into the query. n8n sanitizes data in query parameters, which prevents SQL injection.

For example, you want to find a person by their email address. Given the following input data:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>``` | ```<br>[<br>    {<br>        "email": "alex@example.com",<br>        "name": "Alex",<br>        "age": 21 <br>    },<br>    {<br>        "email": "jamie@example.com",<br>        "name": "Jamie",<br>        "age": 33 <br>    }<br>]<br>``` |

You can write a query like:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>SELECT * FROM $1:name WHERE email = $2;<br>``` |

Then in **Query Parameters**, provide the field values to use. You can provide fixed values or expressions. For this example, use expressions so the node can pull the email address from each input item in turn:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>// users is an example table name<br>users, {{ $json.email }} <br>``` |

## Common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/\#common-issues "Permanent link")

For common errors or issues and suggested resolution steps, refer to [Common issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top