---
url: "https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/"
title: "How to Build Intelligent Agentic RAG with CrewAI and Qdrant - Qdrant"
---

0

# How to Build Intelligent Agentic RAG with CrewAI and Qdrant

Kacper Łukawski

·

January 24, 2025

![How to Build Intelligent Agentic RAG with CrewAI and Qdrant](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fwebinar-crewai-qdrant-obsidian%2F&text=How%20to%20Build%20Intelligent%20Agentic%20RAG%20with%20CrewAI%20and%20Qdrant "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fwebinar-crewai-qdrant-obsidian%2F "LinkedIn")

In a recent live session, we teamed up with [CrewAI](https://crewai.com/), a framework for building intelligent,
multi-agent applications. If you missed it, [Kacper Łukawski](https://www.linkedin.com/in/kacperlukawski/) from Qdrant
and [Tony Kipkemboi](https://www.linkedin.com/in/tonykipkemboi) from [CrewAI](https://crewai.com/) gave an insightful
overview of CrewAI’s capabilities and demonstrated how to leverage Qdrant for creating an agentic RAG
(Retrieval-Augmented Generation) system. The focus was on semi-automating email communication, using
[Obsidian](https://obsidian.md/) as the knowledge base.

In this article, we’ll guide you through the process of setting up an AI-powered system that connects directly to your
email inbox and knowledge base, enabling it to analyze incoming messages and existing content to generate contextually
relevant response suggestions.

## [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#background-agents) Background agents

Although we got used to LLM-based apps that usually have a chat-like interface, even if it’s not a real UI but a CLI
tool, plenty of day-to-day tasks can be automated in the background without explicit human action firing the process.
This concept is also known as **ambient agents**, where the agent is always there, waiting for a trigger to act.

### [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#the-basic-concepts-of-crewai) The basic concepts of CrewAI

Thanks for Tony’s participation, we could learn more about CrewAI, and understand the basic concepts of the framework.
He introduced the concepts of agents and crews, and how they can be used to build intelligent multi-agent applications.
Moreover, Tony described different types of memory that CrewAI applications can use.

When it comes to Qdrant role in CrewAI applications, it can be used as short-term, or entity memory, as both components
are based on RAG and vector embeddings. If you’d like to know more about memory in CrewAI, please visit the [CrewAI\\
concepts](https://docs.crewai.com/concepts/memory).

Tony made an interesting analogy. He compared crews to different departments in a company, where each department has its
own responsibilities, but they all work together to achieve the company’s goals.

### [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#email-automation-with-crewai-qdrant-and-obsidian-notes) Email automation with CrewAI, Qdrant, and Obsidian notes

Our webinar focused on building an agentic RAG system that would semi-automate email communication. RAG is an essential
component of such a system, as you don’t want to take responsibility for responses that cannot be grounded. The system
would monitor your Gmail inbox, analyze the incoming emails, and prepare response drafts if it detects that the email is
not spam, newsletter, or notification.

On the other hand, the system would also monitor the Obsidian notes, by watching any changes in the local file system.
When a file is created, modified, or deleted, the system would automatically move these changes to the Qdrant
collection, so the knowledge base is always up-to-date. Obsidian uses Markdown files to store notes, so complex parsing
is not required.

Here is a simplified diagram presenting the target architecture of the system:

![Project architecture](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/project-architecture.png)

Qdrant acts as a knowledge base, storing the embeddings of the Obsidian notes.

## [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#implementing-the-system) Implementing the system

Since our system integrates with two external APIs - Gmail and filesystem. **We won’t go into details of how to work**
**with these APIs**, as it’s out of the scope of this webinar. Instead, we will focus on the CrewAI and Qdrant
integration, and CrewAI agents’ implementation.

### [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#crewai--qdrant-integration) CrewAI <> Qdrant integration

Since there is no official integration between CrewAI and Qdrant yet, we created a custom implementation of the
`RAGStorage` class, which has a pretty straightforward interface.

```python
from typing import Optional
from crewai.memory.storage.rag_storage import RAGStorage

class QdrantStorage(RAGStorage):
    """
    Extends Storage to handle embeddings for memory entries
    using Qdrant.
    """

    ...

    def search(self,
        query: str,
        limit: int = 3,
        filter: Optional[dict] = None,
        score_threshold: float = 0,
    ) -> list[dict]:
        ...

    def reset(self) -> None:
        ...

```

Full implementation might be found in the [GitHub\\
repository](https://github.com/qdrant/webinar-crewai-qdrant-obsidian/blob/main/src/email_assistant/storage.py). You can
use it for your own projects, or as a reference for your custom implementation. If you want to set up a crew that uses
Qdrant as both entity and short memory layers, you can do it like this:

```python
from crewai import Crew, Process
from crewai.memory import EntityMemory, ShortTermMemory
from email_assistant.storage import QdrantStorage

qdrant_location= "http://localhost:6333"
qdrant_api_key = "your-secret-api-key"
embedder_config = {...}

crew = Crew(
    agents=[...],
    tasks=[...],  # Automatically created by the @task decorator
    process=Process.sequential,
    memory=True,
    entity_memory=EntityMemory(
        storage=QdrantStorage(
            type="entity-memory",
            embedder_config=embedder_config,
            qdrant_location=qdrant_location,
            qdrant_api_key=qdrant_api_key,
        ),
    ),
    short_term_memory=ShortTermMemory(
        storage=QdrantStorage(
            type="short-term-memory",
            embedder_config=embedder_config,
            qdrant_location=qdrant_location,
            qdrant_api_key=qdrant_api_key,
        ),
    ),
    embedder=embedder_config,
    verbose=True,
)

```

Both types of memory will use different collection names in Qdrant, so you can easily distinguish between them, and the
data won’t be mixed up.

**We are planning to release a CrewAI tool for Qdrant integration in the near future**, so stay tuned!

### [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#loading-the-obsidian-notes-to-qdrant) Loading the Obsidian notes to Qdrant

For the sake of the demo, we decided to simply scrape the documentation of both CrewAI and Qdrant, and store it in the
Obsidian notes. That’s easy with Obsidian Web Clipper, as it allows you to save the web page as a Markdown file.

![Obsidian notes](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/obsidian.png)

Assuming we detected a change in the Obsidian notes, such as new note creation or modification, we would like to load
the changes to Qdrant. We could possibly use some chunking methods, starting from basic fixed-size chunks, or go
straight to semantic chunking. However, LLMs are also well-known for their ability to divide the text into meaningful
parts, so we decided to try them out. Moreover, standard chunking is enough in many cases, but we also wanted to test
the [Contextual Retrieval concept introduced by Anthropic](https://www.anthropic.com/news/contextual-retrieval). In a
nutshell, the idea is to use LLMs to generate a short context for each chunk, so it situates the chunk in the context of
the whole document.

It turns out, implementing such a crew in CrewAI is quite straightforward. There are two actors in the crew - one
chunking the text and the other one generating the context. Both might be defined in YAML files like this:

```yaml
chunks_extractor:
  role: >
    Semantic chunks extractor
  goal: >
    Parse Markdown to extract digestible pieces of information which are
    semantically meaningful and can be easily understood by a human.
  backstory: >
    You are a search expert building a search engine for Markdown files.
    Once you receive a Markdown file, you divide it into meaningful semantic
    chunks, so each chunk is about a certain topic or concept. You're known
    for your ability to extract relevant information from large documents and
    present it in a structured and easy-to-understand format, that increases
    the searchability of the content and results quality.

contextualizer:
  role: >
    Bringing context to the extracted chunks
  goal: >
    Add context to the extracted chunks to make them more meaningful and
    understandable. This context should help the reader understand the
    significance of the information and how it relates to the broader topic.
  backstory: >
    You are a knowledge curator who specializes in making information more
    accessible and understandable. You take the extracted chunks and provide
    additional context to make them more meaningful by bringing in relevant
    information about the whole document or the topic at hand.

```

CrewAI makes it very easy to define such agents, and even a non-tech person can understand and modify the YAML files.

Another YAML file defines the tasks that the agents should perform:

```yaml
extract_chunks:
  description: >
    Review the document you got and extract the chunks from it. Each
    chunk should be a separate piece of information that can be easily understood
    by a human and is semantically meaningful. If there are two or more chunks that
    are closely related, but not put next to each other, you can merge them into
    a single chunk. It is important to cover all the important information in the
    document and make sure that the chunks are logically structured and coherent.

    <document>{document}</document>
  expected_output: >
    A list of semantic chunks with succinct context of information extracted from
    the document.
  agent: chunks_extractor

contextualize_chunks:
  description: >
    You have the chunks we want to situate within the whole document.
    Please give a short succinct context to situate this chunk within the overall
    document for the purposes of improving search retrieval of the chunk. Answer
    only with the succinct context and nothing else.
  expected_output: >
    A short succinct context to situate the chunk within the overall document, along
    with the chunk itself.
  agent: contextualizer

```

YAML is not enough to make the agents work, so we need to implement them in Python. The role, goal, and backstory
of the agent, as well as the task description and expected output, are used to build a prompt sent to the LLM. However,
the code defines which LLM to use, and some other parameters of the interaction, like structured output. We heavily rely
on Pydantic models to define the output of the task, so the responses might be easily processed by the application,
for example, to store them in Qdrant.

```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from email_assistant import models

...

@CrewBase
class KnowledgeOrganizingCrew(BaseCrew):
    """
    A crew responsible for processing raw text data and converting it into structured knowledge.
    """

    agents_config = "config/knowledge/agents.yaml"
    tasks_config = "config/knowledge/tasks.yaml"

    @agent
    def chunks_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config["chunks_extractor"],
            verbose=True,
            llm="anthropic/claude-3-5-sonnet-20241022",
        )

    ...

    @task
    def contextualize_chunks(self) -> Task:
        # The task description is borrowed from the Anthropic Contextual Retrieval
        # See: https://www.anthropic.com/news/contextual-retrieval/
        return Task(
            config=self.tasks_config["contextualize_chunks"],
            output_pydantic=models.ContextualizedChunks,
        )

    ...

    @crew
    def crew(self) -> Crew:
        """Creates the KnowledgeOrganizingCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True,
            entity_memory=self.entity_memory(),
            short_term_memory=self.short_term_memory(),
            embedder=self.embedder_config,
            verbose=True,
        )

```

Full implementation might again be found in the [GitHub\\
repository](https://github.com/qdrant/webinar-crewai-qdrant-obsidian/blob/main/src/email_assistant/crew.py).

### [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#drafting-emails-in-gmail-inbox) Drafting emails in Gmail Inbox

At this point we already have our notes stored in Qdrant, and we can write emails in Gmail Inbox using the notes as a
ground truth. The system would monitor the Gmail inbox, and if it detects an email that is not spam, newsletter, or
notification, it would draft a response based on the knowledge base stored in Qdrant. Again, that means we need to use
two agents - one for detecting the kind of the incoming email, and the other one for drafting the response.

The YAML files for these agents might look like this:

```yaml
categorizer:
  role: >
    Email threads categorizer
  goal: >
    Automatically categorize email threads based on their content.
  backstory: >
    You're a virtual assistant with a knack for organizing information.
    You're known for your ability to quickly and accurately categorize email
    threads, so that your clients know which ones are important to answer
    and which ones are spam, newsletters, or other types of messages that
    do not require attention.
    Available categories: QUESTION, NOTIFICATION, NEWSLETTER, SPAM. Do not make
    up new categories.

response_writer:
  role: >
    Email response writer
  goal: >
    Write clear and concise responses to an email thread. Try to help the
    sender. Use the external knowledge base to provide relevant information.
  backstory: >
    You are a professional writer with a talent for crafting concise and
    informative responses. You're known for your ability to quickly understand
    the context of an email thread and provide a helpful and relevant response
    that addresses the sender's needs. You always rely on your knowledge base
    to provide accurate and up-to-date information.

```

The set of categories is predefined, so the categorizer should not invent new categories. The task definitions are as
follows:

```yaml
categorization_task:
  description: >
    Review the content of the following email thread and categorize it
    into the appropriate category. There might be multiple categories that
    apply to the email thread.

    <messages>{messages}</messages>
  expected_output: >
    A list of all the categories that the email threads can be classified into.
  agent: categorizer

response_writing_task:
  description: >
    Write a response to the following email thread. The response should be
    clear, concise, and helpful to the sender. Always rely on the Qdrant search
    tool, so you can get the most relevant information to craft your response.
    Please try to include the source URLs of the information you provide.

    Only focus on the real question asked by the sender and do not try to
    address any other issues that are not directly related to the sender's needs.
    Do not try to provide a response if the context is not clear enough.

    <messages>{messages}</messages>
  expected_output: >
    A well-crafted response to the email thread that addresses the sender's needs.
    Please use simple HTML formatting to make the response more readable.
    Do not include greetings or signatures in your response, but provide the footnotes
    with the source URLs of the information you used, if possible.

    If the provided context does not give you enough information to write a response,
    you must admit that you cannot provide a response and write "I cannot provide a response.".
  agent: response_writer

```

We specifically asked the agents to include the source URLs of the information they provide, so both the sender and the
recipient can verify the information.

### [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#working-system) Working system

We have both crews defined, and the application is ready to run. The only thing left is to monitor the Gmail inbox and
the Obsidian notes for changes. We use the `watchdog` library to monitor the filesystem, and the `google-api-python-client`
to monitor the Gmail inbox, but we won’t go into details of how to use these libraries, as the integration code would
make this blog post too long.

If you open the [main file of the\\
application](https://github.com/qdrant/webinar-crewai-qdrant-obsidian/blob/main/main.py), you will see that it is quite
simple. It runs two separate threads, one for monitoring the Gmail inbox, and the other one for monitoring the Obsidian
notes. If there is any event detected, the application will run the appropriate crew to process the data, and the
resulting response will be sent back to the email thread, or Qdrant collection, respectively. No UI is required, as your
ambient agents are working in the background.

## [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#results) Results

The system is now ready to run, and it can semi-automate email communication, and keep the knowledge base up-to-date.
If you set it up properly, you can expect the system to draft responses to emails that are not spam, newsletter, or
notification, so your email inbox may look like this, even when you sleep:

![Drafted emails](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/gmail-inbox.png)

## [Anchor](https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/\#materials) Materials

As usual, we prepared a video recording of the webinar, so you can watch it at your convenience:

How to Build Intelligent Agentic RAG with CrewAI and Qdrant - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[How to Build Intelligent Agentic RAG with CrewAI and Qdrant](https://www.youtube.com/watch?v=soGB3UowTZ0)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=soGB3UowTZ0&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 1:04:55
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=soGB3UowTZ0 "Watch on YouTube")

The source code of the demo is available on [GitHub](https://github.com/qdrant/webinar-crewai-qdrant-obsidian/), so if
you would like to try it out yourself, feel free to clone or fork the repository and follow the instructions in the
[README](https://github.com/qdrant/webinar-crewai-qdrant-obsidian/blob/main/README.md) file.

Are you building agentic RAG applications using CrewAI and Qdrant? Please join [our Discord\\
community](https://github.com/qdrant/webinar-crewai-qdrant-obsidian/blob/main/README.md) and share your experience!

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=0b1e5b5e-e8e6-4a27-8d16-bddeb1f40393)

![](https://qdrant.tech/img/rocket.svg)

Up!

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=902fae1d-88a5-49af-be99-c78fb9bbe3b8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ffacde58-6e89-47b6-b5dc-756300cda9b4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fwebinar-crewai-qdrant-obsidian%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=902fae1d-88a5-49af-be99-c78fb9bbe3b8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ffacde58-6e89-47b6-b5dc-756300cda9b4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fwebinar-crewai-qdrant-obsidian%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fwebinar-crewai-qdrant-obsidian%2F&portalId=139603372&pageTitle=How+to+Build+Intelligent+Agentic+RAG+with+CrewAI+and+Qdrant+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=1fdef99d2b6556fb6b2a0f0741ac0a7e&hssc=265983056.1.1748574446088&hstc=265983056.1fdef99d2b6556fb6b2a0f0741ac0a7e.1748574446088.1748574446088.1748574446088.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fwebinar-crewai-qdrant-obsidian%2F&pageTitle=How+to+Build+Intelligent+Agentic+RAG+with+CrewAI+and+Qdrant+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=1fdef99d2b6556fb6b2a0f0741ac0a7e&hssc=265983056.1.1748574446088&hstc=265983056.1fdef99d2b6556fb6b2a0f0741ac0a7e.1748574446088.1748574446088.1748574446088.1&hsfp=3707738794).