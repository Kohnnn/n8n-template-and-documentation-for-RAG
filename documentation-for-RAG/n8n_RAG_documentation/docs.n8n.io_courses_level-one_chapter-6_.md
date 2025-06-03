---
url: "https://docs.n8n.io/courses/level-one/chapter-6/"
title: "Exporting and importing workflows | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-6/#exporting-and-importing-workflows)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-6.md "Edit this page")

# Exporting and importing workflows [\#](https://docs.n8n.io/courses/level-one/chapter-6/\#exporting-and-importing-workflows "Permanent link")

In this chapter, you will learn how to export and import workflows.

## Exporting and importing workflows [\#](https://docs.n8n.io/courses/level-one/chapter-6/\#exporting-and-importing-workflows_1 "Permanent link")

You can save n8n workflows locally as JSON files. This is useful if you want to share your workflow with someone else or import a workflow from someone else.

Sharing credentials

Exported workflow JSON files include [credential](https://docs.n8n.io/glossary/#credential-n8n) names and IDs. While IDs aren't sensitive, the names could be, depending on how you name your credentials. HTTP Request nodes may contain authentication headers when imported from cURL. Remove or anonymize this information from the JSON file before sharing to protect your credentials.

[![Import/Export menu](https://docs.n8n.io/_images/courses/level-one/chapter-six/l1-c6-import-export-menu.png)](https://docs.n8n.io/_images/courses/level-one/chapter-six/l1-c6-import-export-menu.png) _Import & Export workflows menu_

You can export and import workflows in three ways:

- From the **Editor UI** menu:
  - Export: From the top navigation bar, select the three dots in the upper right, then select **Download**. This will download your current workflow as a JSON file on your computer.
  - Import: From the top navigation bar, select the three dots in the upper right, then select **Import from URL** (to import a published workflow) or **Import from File** (to import a workflow as a JSON file).
- From the **Editor UI** canvas:
  - Export: Select all the nodes on the canvas and use `Ctrl` + `C` to copy the workflow JSON. You can paste this into a file or share it directly with other people.
  - Import: You can paste a copied workflow JSON directly into the canvas with `Ctrl` + `V`.
- From the command line:
  - Export: See the [full list of commands](https://docs.n8n.io/hosting/cli-commands/) for exporting workflows or credentials.
  - Import: See the [full list of commands](https://docs.n8n.io/hosting/cli-commands/#import-workflows-and-credentials) for importing workflows or credentials.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top