---
url: "https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/"
title: "Automate filtering with LLMs - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Search precision](https://qdrant.tech/documentation/search-precision/)
- Automate filtering with LLMs

# [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#automate-filtering-with-llms) Automate filtering with LLMs

Our [complete guide to filtering in vector search](https://qdrant.tech/articles/vector-search-filtering/) describes why filtering is
important, and how to implement it with Qdrant. However, applying filters is easier when you build an application
with a traditional interface. Your UI may contain a form with checkboxes, sliders, and other elements that users can
use to set their criteria. But what if you want to build a RAG-powered application with just the conversational
interface, or even voice commands? In this case, you need to automate the filtering process!

LLMs seem to be particularly good at this task. They can understand natural language and generate structured output
based on it. In this tutorial, we’ll show you how to use LLMs to automate filtering in your vector search application.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#few-notes-on-qdrant-filters) Few notes on Qdrant filters

Qdrant Python SDK defines the models using [Pydantic](https://docs.pydantic.dev/latest/). This library is de facto
standard for data validation and serialization in Python. It allows you to define the structure of your data using
Python type hints. For example, our `Filter` model is defined as follows:

```python
class Filter(BaseModel, extra="forbid"):
    should: Optional[Union[List["Condition"], "Condition"]] = Field(
        default=None, description="At least one of those conditions should match"
    )
    min_should: Optional["MinShould"] = Field(
        default=None, description="At least minimum amount of given conditions should match"
    )
    must: Optional[Union[List["Condition"], "Condition"]] = Field(default=None, description="All conditions must match")
    must_not: Optional[Union[List["Condition"], "Condition"]] = Field(
        default=None, description="All conditions must NOT match"
    )

```

Qdrant filters may be nested, and you can express even the most complex conditions using the `must`, `should`, and
`must_not` notation.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#structured-output-from-llms) Structured output from LLMs

It isn’t an uncommon practice to use LLMs to generate structured output. It is primarily useful if their output is
intended for further processing by a different application. For example, you can use LLMs to generate SQL queries,
JSON objects, and most importantly, Qdrant filters. Pydantic got adopted by the LLM ecosystem quite well, so there is
plenty of libraries which uses Pydantic models to define the structure of the output for the Language Models.

One of the interesting projects in this area is [Instructor](https://python.useinstructor.com/) that allows you to
play with different LLM providers and restrict their output to a specific structure. Let’s install the library and
already choose a provider we’ll use in this tutorial:

```shell
pip install "instructor[anthropic]"

```

Anthropic is not the only option out there, as Instructor supports many other providers including OpenAI, Ollama,
Llama, Gemini, Vertex AI, Groq, Litellm and others. You can choose the one that fits your needs the best, or the one
you already use in your RAG.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#using-instructor-to-generate-qdrant-filters) Using Instructor to generate Qdrant filters

Instructor has some helper methods to decorate the LLM APIs, so you can interact with them as if you were using their
normal SDKs. In case of Anthropic, you just pass an instance of `Anthropic` class to the `from_anthropic` function:

```python
import instructor
from anthropic import Anthropic

anthropic_client = instructor.from_anthropic(
    client=Anthropic(
        api_key="YOUR_API_KEY",
    )
)

```

A decorated client slightly modifies the original API, so you can pass the `response_model` parameter to the
`.messages.create` method. This parameter should be a Pydantic model that defines the structure of the output. In case
of Qdrant filters, it should be a `Filter` model:

```python
from qdrant_client import models

qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": "red T-shirt"\
        }\
    ],
)

```

The output of this code will be a Pydantic model that represents a Qdrant filter. Surprisingly, there is no need to pass
additional instructions to already figure out that the user wants to filter by the color and the type of the product.
Here is how the output looks like:

```python
Filter(
    should=None,
    min_should=None,
    must=[\
        FieldCondition(\
            key="color",\
            match=MatchValue(value="red"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="type",\
            match=MatchValue(value="t-shirt"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        )\
    ],
    must_not=None
)

```

Obviously, giving the model complete freedom to generate the filter may lead to unexpected results, or no results at
all. Your collection probably has payloads with a specific structure, so it doesn’t make sense to use anything else.
Moreover, **it’s considered a good practice to filter by the fields that have been indexed**. That’s why it makes sense
to automatically determine the indexed fields and restrict the output to them.

### [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#restricting-the-available-fields) Restricting the available fields

Qdrant collection info contains a list of the indexes created on a particular collection. You can use this information
to automatically determine the fields that can be used for filtering. Here is how you can do it:

```python
from qdrant_client import QdrantClient

client = QdrantClient("http://localhost:6333")
collection_info = client.get_collection(collection_name="test_filter")
indexes = collection_info.payload_schema
print(indexes)

```

Output:

```python
{
    "city.location": PayloadIndexInfo(
        data_type=PayloadSchemaType.GEO,
        ...
    ),
    "city.name": PayloadIndexInfo(
        data_type=PayloadSchemaType.KEYWORD,
        ...
    ),
    "color": PayloadIndexInfo(
        data_type=PayloadSchemaType.KEYWORD,
        ...
    ),
    "fabric": PayloadIndexInfo(
        data_type=PayloadSchemaType.KEYWORD,
        ...
    ),
    "price": PayloadIndexInfo(
        data_type=PayloadSchemaType.FLOAT,
        ...
    ),
}

```

Our LLM should know the names of the fields it can use, but also their type, as e.g., range filtering only makes sense
for numerical fields, and geo filtering on non-geo fields won’t yield anything meaningful. You can pass this information
as a part of the prompt to the LLM, so let’s encode it as a string:

```python
formatted_indexes = "\n".join([\
    f"- {index_name} - {index.data_type.name}"\
    for index_name, index in indexes.items()\
])
print(formatted_indexes)

```

Output:

```text
- fabric - KEYWORD
- city.name - KEYWORD
- color - KEYWORD
- price - FLOAT
- city.location - GEO

```

**It’s a good idea to cache the list of the available fields and their types**, as they are not supposed to change
often. Our interactions with the LLM should be slightly different now:

```python
qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": (\
                "<query>color is red</query>"\
                f"<indexes>\n{formatted_indexes}\n</indexes>"\
            )\
        }\
    ],
)

```

Output:

```python
Filter(
    should=None,
    min_should=None,
    must=FieldCondition(
        key="color",
        match=MatchValue(value="red"),
        range=None,
        geo_bounding_box=None,
        geo_radius=None,
        geo_polygon=None,
        values_count=None
    ),
    must_not=None
)

```

The same query, restricted to the available fields, now generates better criteria, as it doesn’t try to filter by the
fields that don’t exist in the collection.

### [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#testing-the-llm-output) Testing the LLM output

Although the LLMs are quite powerful, they are not perfect. If you plan to automate filtering, it makes sense to run
some tests to see how well they perform. Especially edge cases, like queries that cannot be expressed as filters. Let’s
see how the LLM will handle the following query:

```python
qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": (\
                "<query>fruit salad with no more than 100 calories</query>"\
                f"<indexes>\n{formatted_indexes}\n</indexes>"\
            )\
        }\
    ],
)

```

Output:

```python
Filter(
    should=None,
    min_should=None,
    must=FieldCondition(
        key="price",
        match=None,
        range=Range(lt=None, gt=None, gte=None, lte=100.0),
        geo_bounding_box=None,
        geo_radius=None,
        geo_polygon=None,
        values_count=None
    ),
    must_not=None
)

```

Surprisingly, the LLM extracted the calorie information from the query and generated a filter based on the price field.
It somehow extracts any numerical information from the query and tries to match it with the available fields.

Generally, giving model some more guidance on how to interpret the query may lead to better results. Adding a system
prompt that defines the rules for the query interpretation may help the model to do a better job. Here is how you can
do it:

```python
SYSTEM_PROMPT = """
You are extracting filters from a text query. Please follow the following rules:
1. Query is provided in the form of a text enclosed in <query> tags.
2. Available indexes are put at the end of the text in the form of a list enclosed in <indexes> tags.
3. You cannot use any field that is not available in the indexes.
4. Generate a filter only if you are certain that user's intent matches the field name.
5. Prices are always in USD.
6. It's better not to generate a filter than to generate an incorrect one.
"""

qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": SYSTEM_PROMPT.strip(),\
        },\
        {\
            "role": "assistant",\
            "content": "Okay, I will follow all the rules."\
        },\
        {\
            "role": "user",\
            "content": (\
                "<query>fruit salad with no more than 100 calories</query>"\
                f"<indexes>\n{formatted_indexes}\n</indexes>"\
            )\
        }\
    ],
)

```

Current output:

```python
Filter(
    should=None,
    min_should=None,
    must=None,
    must_not=None
)

```

### [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#handling-complex-queries) Handling complex queries

We have a bunch of indexes created on the collection, and it is quite interesting to see how the LLM will handle more
complex queries. For example, let’s see how it will handle the following query:

```python
qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": SYSTEM_PROMPT.strip(),\
        },\
        {\
            "role": "assistant",\
            "content": "Okay, I will follow all the rules."\
        },\
        {\
            "role": "user",\
            "content": (\
                "<query>"\
                "white T-shirt available no more than 30 miles from London, "\
                "but not in the city itself, below $15.70, not made from polyester"\
                "</query>\n"\
                "<indexes>\n"\
                f"{formatted_indexes}\n"\
                "</indexes>"\
            )\
        },\
    ],
)

```

It might be surprising, but Anthropic Claude is able to generate even such complex filters. Here is the output:

```python
Filter(
    should=None,
    min_should=None,
    must=[\
        FieldCondition(\
            key="color",\
            match=MatchValue(value="white"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="city.location",\
            match=None,\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=GeoRadius(\
                center=GeoPoint(lon=-0.1276, lat=51.5074),\
                radius=48280.0\
            ),\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="price",\
            match=None,\
            range=Range(lt=15.7, gt=None, gte=None, lte=None),\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        )\
    ], must_not=[\
        FieldCondition(\
            key="city.name",\
            match=MatchValue(value="London"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="fabric",\
            match=MatchValue(value="polyester"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        )\
    ]
)

```

The model even knows the coordinates of London and uses them to generate the geo filter. It isn’t the best idea to
rely on the model to generate such complex filters, but it’s quite impressive that it can do it.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#further-steps) Further steps

Real production systems would rather require more testing and validation of the LLM output. Building a ground truth
dataset with the queries and the expected filters would be a good idea. You can use this dataset to evaluate the model
performance and to see how it behaves in different scenarios.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/search-precision/automate-filtering-with-llms.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/search-precision/automate-filtering-with-llms.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=48010331-3c29-4694-82c0-55f93d15ed1e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6df39a87-f303-4701-828a-b1f91e38ce71&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsearch-precision%2Fautomate-filtering-with-llms%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573680773&cv=11&fst=1748573680773&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsearch-precision%2Fautomate-filtering-with-llms%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Automate%20filtering%20with%20LLMs%20-%20Qdrant&npa=0&pscdl=noapi&auid=1291106324.1748573680&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573680758&cv=11&fst=1748573680758&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsearch-precision%2Fautomate-filtering-with-llms%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Automate%20filtering%20with%20LLMs%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1291106324.1748573680&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573680827&cv=11&fst=1748573680827&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsearch-precision%2Fautomate-filtering-with-llms%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Automate%20filtering%20with%20LLMs%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1291106324.1748573680&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=48010331-3c29-4694-82c0-55f93d15ed1e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6df39a87-f303-4701-828a-b1f91e38ce71&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fsearch-precision%2Fautomate-filtering-with-llms%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)