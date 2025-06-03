---
url: "https://docs.n8n.io/courses/level-two/chapter-5/chapter-5.1/"
title: "Workflow 1 | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-two/chapter-5/chapter-5.1/#workflow-1-merging-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-two/chapter-5/chapter-5.1.md "Edit this page")

# Workflow 1: Merging data [\#](https://docs.n8n.io/courses/level-two/chapter-5/chapter-5.1/\#workflow-1-merging-data "Permanent link")

Nathan's company stores its customer data in Airtable. This data contains information about the customers' ID, country, email, and join date, but lacks data about their respective region and subregion. You need to fill in these last two fields in order to create the reports for regional sales.

To accomplish this task, you first need to make a copy of this table in your Airtable account:

[iframe](https://airtable.com/embed/shrNX9tjPkVLABbNz?backgroundColor=orange&viewControls=on)

Next, build a small workflow that merges data from Airtable and a REST Countries API:

1. Use the [**Airtable node**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/) to list the data in the Airtable table named `customers`.
2. Use the [**HTTP Request node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to get data from the REST Countries API: `https://restcountries.com/v3.1/all`. This will return data about world countries, split out into separate items.
3. Use the [**Merge node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/) to merge data from Airtable and the Countries API by country name, represented as `customerCountry` in Airtable and `name.common` in the Countries API, respectively.
4. Use another Airtable node to update the fields `region` and `subregion` in Airtable with the data from the Countries API.

The workflow should look like this:

[![Workflow 1 for merging data from Airtable and the Countries API](https://docs.n8n.io/_images/courses/level-two/chapter-five/workflow1.png)](https://docs.n8n.io/_images/courses/level-two/chapter-five/workflow1.png) _Workflow 1 for merging data from Airtable and the Countries API_

Quiz questions

- How many items does the **HTTP Request node** return?
- How many items does the **Merge node** return?
- How many unique regions are assigned in the customers table?
- What's the subregion assigned to the customerID 10?

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top