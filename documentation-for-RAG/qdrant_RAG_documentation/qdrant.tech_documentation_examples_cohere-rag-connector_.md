---
url: "https://qdrant.tech/documentation/examples/cohere-rag-connector/"
title: "Implement Cohere RAG connector - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Implement Cohere RAG connector

# [Anchor](https://qdrant.tech/documentation/examples/cohere-rag-connector/\#implement-custom-connector-for-cohere-rag) Implement custom connector for Cohere RAG

| Time: 45 min | Level: Intermediate |  |  |
| --- | --- | --- | --- |

The usual approach to implementing Retrieval Augmented Generation requires users to build their prompts with the
relevant context the LLM may rely on, and manually sending them to the model. Cohere is quite unique here, as their
models can now speak to the external tools and extract meaningful data on their own. You can virtually connect any data
source and let the Cohere LLM know how to access it. Obviously, vector search goes well with LLMs, and enabling semantic
search over your data is a typical case.

Cohere RAG has lots of interesting features, such as inline citations, which help you to refer to the specific parts of
the documents used to generate the response.

![Cohere RAG citations](https://qdrant.tech/documentation/tutorials/cohere-rag-connector/cohere-rag-citations.png)

_Source: [https://docs.cohere.com/docs/retrieval-augmented-generation-rag](https://docs.cohere.com/docs/retrieval-augmented-generation-rag)_

The connectors have to implement a specific interface and expose the data source as HTTP REST API. Cohere documentation
[describes a general process of creating a connector](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector).
This tutorial guides you step by step on building such a service around Qdrant.

## [Anchor](https://qdrant.tech/documentation/examples/cohere-rag-connector/\#qdrant-connector) Qdrant connector

You probably already have some collections you would like to bring to the LLM. Maybe your pipeline was set up using some
of the popular libraries such as Langchain, Llama Index, or Haystack. Cohere connectors may implement even more complex
logic, e.g. hybrid search. In our case, we are going to start with a fresh Qdrant collection, index data using Cohere
Embed v3, build the connector, and finally connect it with the [Command-R model](https://txt.cohere.com/command-r/).

### [Anchor](https://qdrant.tech/documentation/examples/cohere-rag-connector/\#building-the-collection) Building the collection

First things first, let’s build a collection and configure it for the Cohere `embed-multilingual-v3.0` model. It
produces 1024-dimensional embeddings, and we can choose any of the distance metrics available in Qdrant. Our connector
will act as a personal assistant of a software engineer, and it will expose our notes to suggest the priorities or
actions to perform.

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    "https://my-cluster.cloud.qdrant.io:6333",
    api_key="my-api-key",
)
client.create_collection(
    collection_name="personal-notes",
    vectors_config=models.VectorParams(
        size=1024,
        distance=models.Distance.DOT,
    ),
)

```

Our notes will be represented as simple JSON objects with a `title` and `text` of the specific note. The embeddings will
be created from the `text` field only.

```python
notes = [\
    {\
        "title": "Project Alpha Review",\
        "text": "Review the current progress of Project Alpha, focusing on the integration of the new API. Check for any compatibility issues with the existing system and document the steps needed to resolve them. Schedule a meeting with the development team to discuss the timeline and any potential roadblocks."\
    },\
    {\
        "title": "Learning Path Update",\
        "text": "Update the learning path document with the latest courses on React and Node.js from Pluralsight. Schedule at least 2 hours weekly to dedicate to these courses. Aim to complete the React course by the end of the month and the Node.js course by mid-next month."\
    },\
    {\
        "title": "Weekly Team Meeting Agenda",\
        "text": "Prepare the agenda for the weekly team meeting. Include the following topics: project updates, review of the sprint backlog, discussion on the new feature requests, and a brainstorming session for improving remote work practices. Send out the agenda and the Zoom link by Thursday afternoon."\
    },\
    {\
        "title": "Code Review Process Improvement",\
        "text": "Analyze the current code review process to identify inefficiencies. Consider adopting a new tool that integrates with our version control system. Explore options such as GitHub Actions for automating parts of the process. Draft a proposal with recommendations and share it with the team for feedback."\
    },\
    {\
        "title": "Cloud Migration Strategy",\
        "text": "Draft a plan for migrating our current on-premise infrastructure to the cloud. The plan should cover the selection of a cloud provider, cost analysis, and a phased migration approach. Identify critical applications for the first phase and any potential risks or challenges. Schedule a meeting with the IT department to discuss the plan."\
    },\
    {\
        "title": "Quarterly Goals Review",\
        "text": "Review the progress towards the quarterly goals. Update the documentation to reflect any completed objectives and outline steps for any remaining goals. Schedule individual meetings with team members to discuss their contributions and any support they might need to achieve their targets."\
    },\
    {\
        "title": "Personal Development Plan",\
        "text": "Reflect on the past quarter's achievements and areas for improvement. Update the personal development plan to include new technical skills to learn, certifications to pursue, and networking events to attend. Set realistic timelines and check-in points to monitor progress."\
    },\
    {\
        "title": "End-of-Year Performance Reviews",\
        "text": "Start preparing for the end-of-year performance reviews. Collect feedback from peers and managers, review project contributions, and document achievements. Consider areas for improvement and set goals for the next year. Schedule preliminary discussions with each team member to gather their self-assessments."\
    },\
    {\
        "title": "Technology Stack Evaluation",\
        "text": "Conduct an evaluation of our current technology stack to identify any outdated technologies or tools that could be replaced for better performance and productivity. Research emerging technologies that might benefit our projects. Prepare a report with findings and recommendations to present to the management team."\
    },\
    {\
        "title": "Team Building Event Planning",\
        "text": "Plan a team-building event for the next quarter. Consider activities that can be done remotely, such as virtual escape rooms or online game nights. Survey the team for their preferences and availability. Draft a budget proposal for the event and submit it for approval."\
    }\
]

```

Storing the embeddings along with the metadata is fairly simple.

```python
import cohere
import uuid

cohere_client = cohere.Client(api_key="my-cohere-api-key")

response = cohere_client.embed(
    texts=[\
        note.get("text")\
        for note in notes\
    ],
    model="embed-multilingual-v3.0",
    input_type="search_document",
)

client.upload_points(
    collection_name="personal-notes",
    points=[\
        models.PointStruct(\
            id=uuid.uuid4().hex,\
            vector=embedding,\
            payload=note,\
        )\
        for note, embedding in zip(notes, response.embeddings)\
    ]
)

```

Our collection is now ready to be searched over. In the real world, the set of notes would be changing over time, so the
ingestion process won’t be as straightforward. This data is not yet exposed to the LLM, but we will build the connector
in the next step.

### [Anchor](https://qdrant.tech/documentation/examples/cohere-rag-connector/\#connector-web-service) Connector web service

[FastAPI](https://fastapi.tiangolo.com/) is a modern web framework and perfect a choice for a simple HTTP API. We are
going to use it for the purposes of our connector. There will be just one endpoint, as required by the model. It will
accept POST requests at the `/search` path. There is a single `query` parameter required. Let’s define a corresponding
model.

```python
from pydantic import BaseModel

class SearchQuery(BaseModel):
    query: str

```

RAG connector does not have to return the documents in any specific format. There are [some good practices to follow](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector#configure-the-connection-between-the-connector-and-the-chat-api),
but Cohere models are quite flexible here. Results just have to be returned as JSON, with a list of objects in a
`results` property of the output. We will use the same document structure as we did for the Qdrant payloads, so there
is no conversion required. That requires two additional models to be created.

```python
from typing import List

class Document(BaseModel):
    title: str
    text: str

class SearchResults(BaseModel):
    results: List[Document]

```

Once our model classes are ready, we can implement the logic that will get the query and provide the notes that are
relevant to it. Please note the LLM is not going to define the number of documents to be returned. That’s completely
up to you how many of them you want to bring to the context.

There are two services we need to interact with - Qdrant server and Cohere API. FastAPI has a concept of a [dependency\\
injection](https://fastapi.tiangolo.com/tutorial/dependencies/#dependencies), and we will use it to provide both
clients into the implementation.

In case of queries, we need to set the `input_type` to `search_query` in the calls to Cohere API.

```python
from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

def client() -> QdrantClient:
    return QdrantClient(config.QDRANT_URL, api_key=config.QDRANT_API_KEY)

def cohere_client() -> cohere.Client:
    return cohere.Client(api_key=config.COHERE_API_KEY)

@app.post("/search")
def search(
    query: SearchQuery,
    client: Annotated[QdrantClient, Depends(client)],
    cohere_client: Annotated[cohere.Client, Depends(cohere_client)],
) -> SearchResults:
    response = cohere_client.embed(
        texts=[query.query],
        model="embed-multilingual-v3.0",
        input_type="search_query",
    )
    results = client.query_points(
        collection_name="personal-notes",
        query=response.embeddings[0],
        limit=2,
    ).points
    return SearchResults(
        results=[\
            Document(**point.payload)\
            for point in results\
        ]
    )

```

Our app might be launched locally for the development purposes, given we have the `uvicorn` server installed:

```shell
uvicorn main:app

```

FastAPI exposes an interactive documentation at `http://localhost:8000/docs`, where we can test our endpoint. The
`/search` endpoint is available there.

![FastAPI documentation](https://qdrant.tech/documentation/tutorials/cohere-rag-connector/fastapi-openapi.png)

We can interact with it and check the documents that will be returned for a specific query. For example, we want to know
recall what we are supposed to do regarding the infrastructure for your projects.

```shell
curl -X "POST" \
    -H "Content-type: application/json" \
    -d '{"query": "Is there anything I have to do regarding the project infrastructure?"}' \
    "http://localhost:8000/search"

```

The output should look like following:

```json
{
  "results": [\
    {\
      "title": "Cloud Migration Strategy",\
      "text": "Draft a plan for migrating our current on-premise infrastructure to the cloud. The plan should cover the selection of a cloud provider, cost analysis, and a phased migration approach. Identify critical applications for the first phase and any potential risks or challenges. Schedule a meeting with the IT department to discuss the plan."\
    },\
    {\
      "title": "Project Alpha Review",\
      "text": "Review the current progress of Project Alpha, focusing on the integration of the new API. Check for any compatibility issues with the existing system and document the steps needed to resolve them. Schedule a meeting with the development team to discuss the timeline and any potential roadblocks."\
    }\
  ]
}

```

### [Anchor](https://qdrant.tech/documentation/examples/cohere-rag-connector/\#connecting-to-command-r) Connecting to Command-R

Our web service is implemented, yet running only on our local machine. It has to be exposed to the public before
Command-R can interact with it. For a quick experiment, it might be enough to set up tunneling using services such as
[ngrok](https://ngrok.com/). We won’t cover all the details in the tutorial, but their
[Quickstart](https://ngrok.com/docs/guides/getting-started/) is a great resource describing the process step-by-step.
Alternatively, you can also deploy the service with a public URL.

Once it’s done, we can create the connector first, and then tell the model to use it, while interacting through the chat
API. Creating a connector is a single call to Cohere client:

```python
connector_response = cohere_client.connectors.create(
    name="personal-notes",
    url="https:/this-is-my-domain.app/search",
)

```

The `connector_response.connector` will be a descriptor, with `id` being one of the attributes. We’ll use this
identifier for our interactions like this:

```python
response = cohere_client.chat(
    message=(
        "Is there anything I have to do regarding the project infrastructure? "
        "Please mention the tasks briefly."
    ),
    connectors=[\
        cohere.ChatConnector(id=connector_response.connector.id)\
    ],
    model="command-r",
)

```

We changed the `model` to `command-r`, as this is currently the best Cohere model available to public. The
`response.text` is the output of the model:

```text
Here are some of the tasks related to project infrastructure that you might have to perform:
- You need to draft a plan for migrating your on-premise infrastructure to the cloud and come up with a plan for the selection of a cloud provider, cost analysis, and a gradual migration approach.
- It's important to evaluate your current technology stack to identify any outdated technologies. You should also research emerging technologies and the benefits they could bring to your projects.

```

You only need to create a specific connector once! Please do not call `cohere_client.connectors.create` for every single
message you send to the `chat` method.

## [Anchor](https://qdrant.tech/documentation/examples/cohere-rag-connector/\#wrapping-up) Wrapping up

We have built a Cohere RAG connector that integrates with your existing knowledge base stored in Qdrant. We covered just
the basic flow, but in real world scenarios, you should also consider e.g. [building the authentication\\
system](https://docs.cohere.com/docs/connector-authentication) to prevent unauthorized access.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/cohere-rag-connector.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/cohere-rag-connector.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=84b16951-35e9-48e4-a98b-8f4943ea7f70&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7f60cfc0-cdeb-4d0d-98df-96ed8368eec7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fcohere-rag-connector%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574413117&cv=11&fst=1748574413117&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fcohere-rag-connector%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Implement%20Cohere%20RAG%20connector%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1856528216.1748574413&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574413178&cv=11&fst=1748574413178&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fcohere-rag-connector%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Implement%20Cohere%20RAG%20connector%20-%20Qdrant&npa=0&pscdl=noapi&auid=1856528216.1748574413&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=84b16951-35e9-48e4-a98b-8f4943ea7f70&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7f60cfc0-cdeb-4d0d-98df-96ed8368eec7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fcohere-rag-connector%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574414383&cv=11&fst=1748574414383&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fcohere-rag-connector%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Implement%20Cohere%20RAG%20connector%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1856528216.1748574413&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)