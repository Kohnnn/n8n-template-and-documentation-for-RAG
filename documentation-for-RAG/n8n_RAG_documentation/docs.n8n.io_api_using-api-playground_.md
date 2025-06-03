---
url: "https://docs.n8n.io/api/using-api-playground/"
title: "Using the API playground | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/api/using-api-playground/#using-the-api-playground)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/api/using-api-playground.md "Edit this page")

# Using the API playground [\#](https://docs.n8n.io/api/using-api-playground/\#using-the-api-playground "Permanent link")

Feature availability

The API playground isn't available on Cloud. It's available for all self-hosted pricing tiers.

The n8n API comes with a built-in Swagger UI playground in self-hosted versions. This provides interactive documentation, where you can try out requests. The path to access the playground depends on your hosting.

n8n constructs the path from values set in your environment variables:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/docs<br>``` |

The API version number is `1`. There may be multiple versions available in the future.

Real data

If you select **Authorize** and enter your API key in the API playground, you have access to your live data. This is useful for trying out requests. Be aware you can change or delete real data.

The API includes built-in documentation about credential formats. This is available using the `credentials` endpoint:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/credentials/schema/{credentialTypeName}<br>``` |

How to find `credentialTypeName`

To find the type, download your workflow as JSON and examine it. For example, for a Google Drive node the `{credentialTypeName}` is `googleDriveOAuth2Api`:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>{<br>    ...,<br>    "credentials": {<br>        "googleDriveOAuth2Api": {<br>        "id": "9",<br>        "name": "Google Drive"<br>        }<br>    }<br>}<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top