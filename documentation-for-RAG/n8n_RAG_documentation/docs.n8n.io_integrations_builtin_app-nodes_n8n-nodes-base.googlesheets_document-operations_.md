---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations/"
title: "Google Sheets Document operations | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations/#google-sheets-document-operations)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md "Edit this page")

# Google Sheets Document operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations/\#google-sheets-document-operations "Permanent link")

Use this operation to create or delete a Google spreadsheet from Google Sheets. Refer to [Google Sheets](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/) for more information on the Google Sheets node itself.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Create a spreadsheet [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations/\#create-a-spreadsheet "Permanent link")

Use this operation to create a new spreadsheet.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Google Sheets credentials](https://docs.n8n.io/integrations/builtin/credentials/google/).
- **Resource**: Select **Document**.
- **Operation**: Select **Create**.
- **Title**: Enter the title of the new spreadsheet you want to create.
- **Sheets**: Add the **Title(s)** of the sheet(s) you want to create within the spreadsheet.

### Options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations/\#options "Permanent link")

- **Locale**: Enter the locale of the spreadsheet. This affects formatting details such as functions, dates, and currency. Use one of the following formats:
  - `en` (639-1)
  - `fil` (639-2 if no 639-1 format exists)
  - `en_US` (combination of ISO language and country).
  - Refer to [List of ISO 639 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) and [List of ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) for language and country codes. Note that Google doesn't support all locales/languages.
- **Recalculation Interval**: Enter the desired recalculation interval for the spreadsheet functions. This affects how often `NOW`, `TODAY`, `RAND`, and `RANDBETWEEN` are updated. Select **On Change** for recalculating whenever there is a change in the spreadsheet, **Minute** for recalculating every minute, or **Hour** for recalculating every hour. Refer to [Set a spreadsheet’s location & calculation settings](https://support.google.com/docs/answer/58515) for more information about these options.

Refer to the [Method: spreadsheets.create \| Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create) API documentation for more information.

## Delete a spreadsheet [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations/\#delete-a-spreadsheet "Permanent link")

Use this operation to delete an existing spreadsheet.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Google Sheets credentials](https://docs.n8n.io/integrations/builtin/credentials/google/).
- **Resource**: Select **Document**.
- **Operation**: Select **Delete**.
- **Document**: Choose a spreadsheet you want to delete.
  - Select **From list** to choose the title from the dropdown list, **By URL** to enter the url of the spreadsheet, or **By ID** to enter the `spreadsheetId`.
  - You can find the `spreadsheetId` in a Google Sheets URL: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`.

Refer to the [Method: files.delete \| Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete) API documentation for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top