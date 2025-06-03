---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel/"
title: "Microsoft Excel 365 node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel/#microsoft-excel-365-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel.md "Edit this page")

# Microsoft Excel 365 node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel/\#microsoft-excel-365-node "Permanent link")

Use the Microsoft Excel node to automate work in Microsoft Excel, and integrate Microsoft Excel with other applications. n8n has built-in support for a wide range of Microsoft Excel features, including adding and retrieving lists of table data, and workbooks, as well as getting worksheets.

On this page, you'll find a list of operations the Microsoft Excel node supports and links to more resources.

Credentials

Refer to [Microsoft credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoft/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel/\#operations "Permanent link")

- Table
  - Adds rows to the end of the table
  - Retrieve a list of table columns
  - Retrieve a list of table rows
  - Looks for a specific column value and then returns the matching row
- Workbook
  - Adds a new worksheet to the workbook.
  - Get data of all workbooks
- Worksheet
  - Get all worksheets
  - Get worksheet content

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel/\#templates-and-examples "Permanent link")

**Automated Web Scraping: email a CSV, save to Google Sheets & Microsoft Excel**

by Mihai Farcas

[View template details](https://n8n.io/workflows/2275-automated-web-scraping-email-a-csv-save-to-google-sheets-and-microsoft-excel/)

**Get all Excel workbooks**

by amudhan

[View template details](https://n8n.io/workflows/566-get-all-excel-workbooks/)

**Daily Newsletter Service using Excel, Outlook and AI**

by Jimleuk

[View template details](https://n8n.io/workflows/3446-daily-newsletter-service-using-excel-outlook-and-ai/)

[Browse Microsoft Excel 365 integration templates](https://n8n.io/integrations/microsoft-excel/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top