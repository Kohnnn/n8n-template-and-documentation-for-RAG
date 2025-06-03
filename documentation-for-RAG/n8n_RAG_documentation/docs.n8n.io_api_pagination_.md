---
url: "https://docs.n8n.io/api/pagination/"
title: "Pagination | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/api/pagination/#api-pagination)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/api/pagination.md "Edit this page")

# API pagination [\#](https://docs.n8n.io/api/pagination/\#api-pagination "Permanent link")

The default page size is 100 results. You can change the page size limit. The maximum permitted size is 250.

When a response contains more than one page, it includes a cursor, which you can use to request the next pages.

For example, say you want to get all active workflows, 150 at a time.

Get the first page:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># For a self-hosted n8n instance<br>curl -X 'GET' \<br>  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150' \<br>  -H 'accept: application/json' \<br>  -H 'X-N8N-API-KEY: <your-api-key>'<br># For n8n Cloud<br>curl -X 'GET' \<br>  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150' \<br>  -H 'accept: application/json' \<br>  -H 'X-N8N-API-KEY: <your-api-key>'<br>``` |

The response is in JSON format, and includes a `nextCursor` value. This is an example response.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>{<br>  "data": [<br>    // The response contains an object for each workflow<br>    {<br>      // Workflow data<br>    }<br>  ],<br>  "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"<br>}<br>``` |

Then to request the next page:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br># For a self-hosted n8n instance<br>curl -X 'GET' \<br>  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \<br>  -H 'accept: application/json'<br># For n8n Cloud<br>curl -X 'GET' \<br>  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \<br>  -H 'accept: application/json'<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top