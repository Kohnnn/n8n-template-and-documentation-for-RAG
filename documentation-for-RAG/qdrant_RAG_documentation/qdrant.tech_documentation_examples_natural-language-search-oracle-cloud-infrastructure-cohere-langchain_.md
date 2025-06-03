---
url: "https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/"
title: "RAG System for Employee Onboarding - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- RAG System for Employee Onboarding

# [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#rag-system-for-employee-onboarding) RAG System for Employee Onboarding

Public websites are a great way to share information with a wide audience. However, finding the right information can be
challenging, if you are not familiar with the website’s structure or the terminology used. That’s what the search bar is
for, but it is not always easy to formulate a query that will return the desired results, if you are not yet familiar
with the content. This is even more important in a corporate environment, and for the new employees, who are just
starting to learn the ropes, and don’t even know how to ask the right questions yet. You may have even the best intranet
pages, but onboarding is more than just reading the documentation, it is about understanding the processes. Semantic
search can help with finding right resources easier, but wouldn’t it be easier to just chat with the website, like you
would with a colleague?

Technological advancements have made it possible to interact with websites using natural language. This tutorial will
guide you through the process of integrating [Cohere](https://cohere.com/)’s language models with Qdrant to enable
natural language search on your documentation. We are going to use [LangChain](https://langchain.com/) as an
orchestrator. Everything will be hosted on [Oracle Cloud Infrastructure (OCI)](https://www.oracle.com/cloud/), so you
can scale your application as needed, and do not send your data to third parties. That is especially important when you
are working with confidential or sensitive data.

## [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#building-up-the-application) Building up the application

Our application will consist of two main processes: indexing and searching. Langchain will glue everything together,
as we will use a few components, including Cohere and Qdrant, as well as some OCI services. Here is a high-level
overview of the architecture:

![Architecture diagram of the target system](https://qdrant.tech/documentation/examples/faq-oci-cohere-langchain/architecture-diagram.png)

### [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#prerequisites) Prerequisites

Before we dive into the implementation, make sure to set up all the necessary accounts and tools.

#### [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#libraries) Libraries

We are going to use a few Python libraries. Of course, Langchain will be our main framework, but the Cohere models on
OCI are accessible via the [OCI SDK](https://docs.oracle.com/en-us/iaas/tools/python/2.125.1/). Let’s install all the
necessary libraries:

```shell
pip install langchain oci qdrant-client langchainhub

```

#### [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#oracle-cloud) Oracle Cloud

Our application will be fully running on Oracle Cloud Infrastructure (OCI). It’s up to you to choose how you want to
deploy your application. Qdrant Hybrid Cloud will be running in your [Kubernetes cluster running on Oracle Cloud\\
(OKE)](https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/), so all the processes might be also
deployed there. You can get started with signing up for an account on [Oracle Cloud](https://signup.cloud.oracle.com/).

Cohere models are available on OCI as a part of the [Generative AI\\
Service](https://www.oracle.com/artificial-intelligence/generative-ai/generative-ai-service/). We need both the
[Generation models](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-generate.htm) and the
[Embedding models](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm). Please follow the
linked tutorials to grasp the basics of using Cohere models there.

Accessing the models programmatically requires knowing the compartment OCID. Please refer to the [documentation that\\
describes how to find it](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/contactingsupport_topic-Locating_Oracle_Cloud_Infrastructure_IDs.htm#Finding_the_OCID_of_a_Compartment).
For the further reference, we will assume that the compartment OCID is stored in the environment variable:

shellpython

```shell
export COMPARTMENT_OCID="<your-compartment-ocid>"

```

```python
import os

os.environ["COMPARTMENT_OCID"] = "<your-compartment-ocid>"

```

#### [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#qdrant-hybrid-cloud) Qdrant Hybrid Cloud

Qdrant Hybrid Cloud running on Oracle Cloud helps you build a solution without sending your data to external services. Our documentation provides a step-by-step guide on how to [deploy Qdrant Hybrid Cloud on Oracle\\
Cloud](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/#oracle-cloud-infrastructure).

Qdrant will be running on a specific URL and access will be restricted by the API key. Make sure to store them both as environment variables as well:

```shell
export QDRANT_URL="https://qdrant.example.com"
export QDRANT_API_KEY="your-api-key"

```

_Optional:_ Whenever you use LangChain, you can also [configure LangSmith](https://docs.smith.langchain.com/), which will help us trace, monitor and debug LangChain applications. You can sign up for LangSmith [here](https://smith.langchain.com/).

```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY="your-api-key"
export LANGCHAIN_PROJECT="your-project"  # if not specified, defaults to "default"

```

Now you can get started:

```python
import os

os.environ["QDRANT_URL"] = "https://qdrant.example.com"
os.environ["QDRANT_API_KEY"] = "your-api-key"

```

Let’s create the collection that will store the indexed documents. We will use the `qdrant-client` library, and our
collection will be named `oracle-cloud-website`. Our embedding model, `cohere.embed-english-v3.0`, produces embeddings
of size 1024, and we have to specify that when creating the collection.

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    location=os.environ.get("QDRANT_URL"),
    api_key=os.environ.get("QDRANT_API_KEY"),
)
client.create_collection(
    collection_name="oracle-cloud-website",
    vectors_config=models.VectorParams(
        size=1024,
        distance=models.Distance.COSINE,
    ),
)

```

### [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#indexing-process) Indexing process

We have all the necessary tools set up, so let’s start with the indexing process. We will use the Cohere Embedding
models to convert the text into vectors, and then store them in Qdrant. Langchain is integrated with OCI Generative AI
Service, so we can easily access the models.

Our dataset will be fairly simple, as it will consist of the questions and answers from the [Oracle Cloud Free Tier\\
FAQ page](https://www.oracle.com/cloud/free/faq/).

![Some examples of the Oracle Cloud FAQ](https://qdrant.tech/documentation/examples/faq-oci-cohere-langchain/oracle-faq.png)

Questions and answers are presented in an HTML format, but we don’t want to manually extract the text and adapt it for
each subpage. Instead, we will use the `WebBaseLoader` that just loads the HTML content from given URL and converts it
to text.

```python
from langchain_community.document_loaders.web_base import WebBaseLoader

loader = WebBaseLoader("https://www.oracle.com/cloud/free/faq/")
documents = loader.load()

```

Our `documents` is a list with just a single element, which is the text of the whole page. We need to split it into
meaningful parts, so we will use the `RecursiveCharacterTextSplitter` component. It will try to keep all paragraphs (and
then sentences, and then words) together as long as possible, as those would generically seem to be the strongest
semantically related pieces of text. The chunk size and overlap are both parameters that can be adjusted to fit the
specific use case.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
split_documents = splitter.split_documents(documents)

```

Our documents might be now indexed, but we need to convert them into vectors. Let’s configure the embeddings so the
`cohere.embed-english-v3.0` is used. Not all the regions support the Generative AI Service, so we need to specify the
region where the models are stored. We will use the `us-chicago-1`, but please check the
[documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/overview.htm#regions) for the most up-to-date
list of supported regions.

```python
from langchain_community.embeddings.oci_generative_ai import OCIGenAIEmbeddings

embeddings = OCIGenAIEmbeddings(
    model_id="cohere.embed-english-v3.0",
    service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
    compartment_id=os.environ.get("COMPARTMENT_OCID"),
)

```

Now we can embed the documents and store them in Qdrant. We will create an instance of `Qdrant` and add the split
documents to the collection.

```python
from langchain.vectorstores.qdrant import Qdrant

qdrant = Qdrant(
    client=client,
    collection_name="oracle-cloud-website",
    embeddings=embeddings,
)

qdrant.add_documents(split_documents, batch_size=20)

```

Our documents should be now indexed and ready for searching. Let’s move to the next step.

### [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#speaking-to-the-website) Speaking to the website

The intended method of interaction with the website is through the chatbot. Large Language Model, in our case [Cohere\\
Command](https://cohere.com/command), will be answering user’s questions based on the relevant documents that Qdrant
will return using the question as a query. Our LLM is also hosted on OCI, so we can access it similarly to the embedding
model:

```python
from langchain_community.llms.oci_generative_ai import OCIGenAI

llm = OCIGenAI(
    model_id="cohere.command",
    service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
    compartment_id=os.environ.get("COMPARTMENT_OCID"),
)

```

Connection to Qdrant might be established in the same way as we did during the indexing process. We can use it to create
a retrieval chain, which implements the question-answering process. The retrieval chain also requires an additional
chain that will combine retrieved documents before sending them to an LLM.

```python
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub

retriever = qdrant.as_retriever()
combine_docs_chain = create_stuff_documents_chain(
    llm=llm,
    # Default prompt is loaded from the hub, but we can also modify it
    prompt=hub.pull("langchain-ai/retrieval-qa-chat"),
)
retrieval_qa_chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=combine_docs_chain,
)
response = retrieval_qa_chain.invoke({"input": "What is the Oracle Cloud Free Tier?"})

```

The output of the `.invoke` method is a dictionary-like structure with the query and answer, but we can also access the
source documents used to generate the response. This might be useful for debugging or for further processing.

```python
{
    'input': 'What is the Oracle Cloud Free Tier?',
    'context': [\
        Document(\
            page_content='* Free Tier is generally available in regions where commercial Oracle Cloud Infrastructure service is available. See the data regions page for detailed service availability (the exact regions available for Free Tier may differ during the sign-up process). The US$300 cloud credit is available in',\
            metadata={\
                'language': 'en-US',\
                'source': 'https://www.oracle.com/cloud/free/faq/',\
                'title': "FAQ on Oracle's Cloud Free Tier",\
                '_id': 'c8cf98e0-4b88-4750-be42-4157495fed2c',\
                '_collection_name': 'oracle-cloud-website'\
            }\
        ),\
        Document(\
            page_content='Oracle Cloud Free Tier allows you to sign up for an Oracle Cloud account which provides a number of Always Free services and a Free Trial with US$300 of free credit to use on all eligible Oracle Cloud Infrastructure services for up to 30 days. The Always Free services are available for an unlimited',\
            metadata={\
                'language': 'en-US',\
                'source': 'https://www.oracle.com/cloud/free/faq/',\
                'title': "FAQ on Oracle's Cloud Free Tier",\
                '_id': 'dc291430-ff7b-4181-944a-39f6e7a0de69',\
                '_collection_name': 'oracle-cloud-website'\
            }\
        ),\
        Document(\
            page_content='Oracle Cloud Free Tier does not include SLAs. Community support through our forums is available to all customers. Customers using only Always Free resources are not eligible for Oracle Support. Limited support is available for Oracle Cloud Free Tier with Free Trial credits. After you use all of',\
            metadata={\
                'language': 'en-US',\
                'source': 'https://www.oracle.com/cloud/free/faq/',\
                'title': "FAQ on Oracle's Cloud Free Tier",\
                '_id': '9e831039-7ccc-47f7-9301-20dbddd2fc07',\
                '_collection_name': 'oracle-cloud-website'\
            }\
        ),\
        Document(\
            page_content='looking to test things before moving to cloud, a student wanting to learn, or an academic developing curriculum in the cloud, Oracle Cloud Free Tier enables you to learn, explore, build and test for free.',\
            metadata={\
                'language': 'en-US',\
                'source': 'https://www.oracle.com/cloud/free/faq/',\
                'title': "FAQ on Oracle's Cloud Free Tier",\
                '_id': 'e2dc43e1-50ee-4678-8284-6df60a835cf5',\
                '_collection_name': 'oracle-cloud-website'\
            }\
        )\
    ],
    'answer': ' Oracle Cloud Free Tier is a subscription that gives you access to Always Free services and a Free Trial with $300 of credit that can be used on all eligible Oracle Cloud Infrastructure services for up to 30 days. \n\nThrough this Free Tier, you can learn, explore, build, and test for free. It is aimed at those who want to experiment with cloud services before making a commitment, as wellTheir use cases range from testing prior to cloud migration to learning and academic curriculum development. '
}

```

#### [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#other-experiments) Other experiments

Asking the basic questions is just the beginning. What you want to avoid is a hallucination, where the model generates
an answer that is not based on the actual content. The default prompt of Langchain should already prevent this, but you
might still want to check it. Let’s ask a question that is not directly answered on the FAQ page:

```python
response = retrieval_qa.invoke({
    "input": "Is Oracle Generative AI Service included in the free tier?"
})

```

Output:

> Oracle Generative AI Services are not specifically mentioned as being available in the free tier. As per the text, the
> $300 free credit can be used on all eligible services for up to 30 days. To confirm if Oracle Generative AI Services
> are included in the free credit offer, it is best to check the official Oracle Cloud website or contact their support.

It seems that Cohere Command model could not find the exact answer in the provided documents, but it tried to interpret
the context and provide a reasonable answer, without making up the information. This is a good sign that the model is
not hallucinating in that case.

## [Anchor](https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/\#wrapping-up) Wrapping up

This tutorial has shown how to integrate Cohere’s language models with Qdrant to enable natural language search on your
website. We have used Langchain as an orchestrator, and everything was hosted on Oracle Cloud Infrastructure (OCI).
Real world would require integrating this mechanism into your organization’s systems, but we built a solid foundation
that can be further developed.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575082527&cv=11&fst=1748575082527&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fnatural-language-search-oracle-cloud-infrastructure-cohere-langchain%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=RAG%20System%20for%20Employee%20Onboarding%20-%20Qdrant&npa=0&pscdl=noapi&auid=1035847869.1748575082&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575082473&cv=11&fst=1748575082473&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fnatural-language-search-oracle-cloud-infrastructure-cohere-langchain%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=RAG%20System%20for%20Employee%20Onboarding%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1035847869.1748575082&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8460478e-48cc-4137-8f70-ef7b270a3dd1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=24057c2d-14c4-436b-959d-5565d395c255&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fnatural-language-search-oracle-cloud-infrastructure-cohere-langchain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=8460478e-48cc-4137-8f70-ef7b270a3dd1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=24057c2d-14c4-436b-959d-5565d395c255&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fnatural-language-search-oracle-cloud-infrastructure-cohere-langchain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575083608&cv=11&fst=1748575083608&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fexamples%2Fnatural-language-search-oracle-cloud-infrastructure-cohere-langchain%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=RAG%20System%20for%20Employee%20Onboarding%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1035847869.1748575082&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)