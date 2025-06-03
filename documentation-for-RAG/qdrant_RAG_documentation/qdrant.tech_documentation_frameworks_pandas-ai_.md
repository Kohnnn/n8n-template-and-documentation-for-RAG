---
url: "https://qdrant.tech/documentation/frameworks/pandas-ai/"
title: "Pandas-AI - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Pandas-AI

# [Anchor](https://qdrant.tech/documentation/frameworks/pandas-ai/\#pandas-ai) Pandas-AI

Pandas-AI is a Python library that uses a generative AI model to interpret natural language queries and translate them into Python code to interact with pandas data frames and return the final results to the user.

## [Anchor](https://qdrant.tech/documentation/frameworks/pandas-ai/\#installation) Installation

```console
pip install pandasai[qdrant]

```

## [Anchor](https://qdrant.tech/documentation/frameworks/pandas-ai/\#usage) Usage

You can begin a conversation by instantiating an `Agent` instance based on your Pandas data frame. The default Pandas-AI LLM requires an [API key](https://pandabi.ai/).

You can find the list of all supported LLMs [here](https://docs.pandas-ai.com/en/latest/LLMs/llms/)

```python
import os
import pandas as pd
from pandasai import Agent

# Sample DataFrame
sales_by_country = pd.DataFrame(
    {
        "country": [\
            "United States",\
            "United Kingdom",\
            "France",\
            "Germany",\
            "Italy",\
            "Spain",\
            "Canada",\
            "Australia",\
            "Japan",\
            "China",\
        ],
        "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000],
    }
)

os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

agent = Agent(sales_by_country)
agent.chat("Which are the top 5 countries by sales?")
# OUTPUT: China, United States, Japan, Germany, Australia

```

## [Anchor](https://qdrant.tech/documentation/frameworks/pandas-ai/\#qdrant-support) Qdrant support

You can train Pandas-AI to understand your data better and improve the quality of the results.

Qdrant can be configured as a vector store to ingest training data and retrieve semantically relevant content.

```python
from pandasai.ee.vectorstores.qdrant import Qdrant

qdrant = Qdrant(
    collection_name="<SOME_COLLECTION>",
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    url="http://localhost:6333",
    grpc_port=6334,
    prefer_grpc=True
)

agent = Agent(df, vector_store=qdrant)

# Train with custom information
agent.train(docs="The fiscal year starts in April")

# Train the q/a pairs of code snippets
query = "What are the total sales for the current fiscal year?"
response = """
import pandas as pd

df = dfs[0]

# Calculate the total sales for the current fiscal year
total_sales = df[df['date'] >= pd.to_datetime('today').replace(month=4, day=1)]['sales'].sum()
result = { "type": "number", "value": total_sales }
"""
agent.train(queries=[query], codes=[response])

# # The model will use the information provided in the training to generate a response

```

## [Anchor](https://qdrant.tech/documentation/frameworks/pandas-ai/\#further-reading) Further reading

- [Getting Started with Pandas-AI](https://pandasai-docs.readthedocs.io/en/latest/getting-started/)
- [Pandas-AI Reference](https://pandasai-docs.readthedocs.io/en/latest/)
- [Source Code](https://github.com/sinaptik-ai/pandas-ai/tree/main/extensions/ee/vectorstores/qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/pandas-ai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/pandas-ai.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)

## Privacy Preference Center

Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.


[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)

Allow All

### Manage Consent Preferences

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574293329&cv=11&fst=1748574293329&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fpandas-ai%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Pandas-AI%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=565820610.1748574293&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574293437&cv=11&fst=1748574293437&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fpandas-ai%2F&hn=www.googleadservices.com&frm=0&tiba=Pandas-AI%20-%20Qdrant&npa=0&pscdl=noapi&auid=565820610.1748574293&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=56536625-4e65-4f41-b3c1-3904c329a262&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c1510775-62e7-4f47-a63e-59d3ec3bf8ab&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fpandas-ai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=56536625-4e65-4f41-b3c1-3904c329a262&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c1510775-62e7-4f47-a63e-59d3ec3bf8ab&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fpandas-ai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)