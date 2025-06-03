---
url: "https://docs.n8n.io/api/authentication/"
title: "Authentication | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/api/authentication/#api-authentication)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/api/authentication.md "Edit this page")

# API authentication [\#](https://docs.n8n.io/api/authentication/\#api-authentication "Permanent link")

n8n uses API keys to authenticate API calls.

Feature availability

The n8n API isn't available during the free trial. Please upgrade to access this feature.

## API Scopes [\#](https://docs.n8n.io/api/authentication/\#api-scopes "Permanent link")

Users of [enterprise instances](https://n8n.io/enterprise/) can limit which resources and actions a key can access with scopes. API key scopes allow you specify the exact level of access a key needs for its intended purpose.

Non-enterprise API keys have full access to all the account's resources and capabilities.

## Create an API key [\#](https://docs.n8n.io/api/authentication/\#create-an-api-key "Permanent link")

1. Log in to n8n.
2. Go to **Settings** \> **n8n API**.
3. Select **Create an API key**.
4. Choose a **Label** and set an **Expiration** time for the key.
5. If on an enterprise plan, choose the **Scopes** to give the key.
6. Copy **My API Key** and use this key to authenticate your calls.

## Call the API using your key [\#](https://docs.n8n.io/api/authentication/\#call-the-api-using-your-key "Permanent link")

Send the API key in your API call as a header named `X-N8N-API-KEY`.

For example, say you want to get all active workflows. Your curl request will look like this:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># For a self-hosted n8n instance<br>curl -X 'GET' \<br>  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true' \<br>  -H 'accept: application/json' \<br>  -H 'X-N8N-API-KEY: <your-api-key>'<br># For n8n Cloud<br>curl -X 'GET' \<br>  '<your-cloud-instance>/api/v<version-number>/workflows?active=true' \<br>  -H 'accept: application/json' \<br>  -H 'X-N8N-API-KEY: <your-api-key>'<br>``` |

## Delete an API key [\#](https://docs.n8n.io/api/authentication/\#delete-an-api-key "Permanent link")

1. Log in to n8n.
2. Go to **Settings** \> **n8n API**.
3. Select **Delete** next to the key you want to delete.
4. Confirm the delete by selecting **Delete Forever**.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top