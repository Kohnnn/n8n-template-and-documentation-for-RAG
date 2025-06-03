---
url: "https://qdrant.tech/documentation/frameworks/deepeval/"
title: "DeepEval - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- DeepEval

# [Anchor](https://qdrant.tech/documentation/frameworks/deepeval/\#deepeval) DeepEval

[DeepEval](https://deepeval.com/) by Confident AI is an open-source framework for testing large language model systems. Similar to Pytest but designed for LLM outputs, it evaluates metrics like G-Eval, hallucination, answer relevancy.

DeepEval can be integrated with Qdrant to evaluate RAG pipelines — ensuring your LLM applications return relevant, grounded, and faithful responses based on retrieved vector search context.

## [Anchor](https://qdrant.tech/documentation/frameworks/deepeval/\#how-it-works) How it works

A test case is a blueprint provided by DeepEval to unit test LLM outputs. There are two types of test cases in DeepEval:

`LLMTestCase`: Used to evaluate a single input-output pair, such as RAG responses or agent actions.

`ConversationalTestCase`: A sequence of `LLMTestCase` turns representing a back-and-forth interaction with an LLM system. This is especially useful for chatbot or assistant testing.

## [Anchor](https://qdrant.tech/documentation/frameworks/deepeval/\#metrics-overview) Metrics Overview

DeepEval offers a suite of metrics to evaluate various aspects of LLM outputs, including:

- **Answer Relevancy**: Measures how relevant the LLM’s output is to the given input query.
- **Faithfulness**: Assesses whether the LLM’s response is grounded in the provided context, ensuring factual accuracy.
- **Contextual Precision**: Determines whether the most relevant pieces of context are ranked higher than less relevant ones.
- **G-Eval**: A versatile metric that uses LLM-as-a-judge with chain-of-thought reasoning to evaluate outputs based on custom criteria.
- **Hallucination**: Detects instances where the LLM generates information not present in the source context.
- **Toxicity**: Assesses the presence of harmful or offensive content in the LLM’s output.
- **Bias**: Evaluates the output for any unintended biases.
- **Summarization**: Measures the quality and accuracy of generated summaries.

For a comprehensive list and detailed explanations of all available metrics, please refer to the [DeepEval metrics reference](https://deepeval.com/docs/metrics-introduction).

## [Anchor](https://qdrant.tech/documentation/frameworks/deepeval/\#using-qdrant-with-deepeval) Using Qdrant with DeepEval

Install the client libraries.

```bash
$ pip install deepeval qdrant-client

$ deepeval login

```

You can use Qdrant to power your RAG system by retrieving relevant documents for a query, feeding them into your prompt, and evaluating the generated output using DeepEval.

```python
from deepeval.test_case import LLMTestCase, ConversationalTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, ...

# 1. Query context from Qdrant
context = qdrant_client.query_points(...)

# 2. Construct prompt using query + retrieved context
prompt = build_prompt(query, context)

# 3. Generate response from your LLM
response = llm.generate(prompt)

# 4. Create a test case for evaluation
test_case = LLMTestCase(
    input=query,
    actual_output=response,
    expected_output=ground_truth_answer,
    retrieval_context=context
)

# 5. Evaluate the output using DeepEval
evaluate(
    test_cases=[test_case],
    metrics=[\
        AnswerRelevancyMetric(),\
        FaithfulnessMetric(),\
        ContextualPrecisionMetric(),\
        ...\
    ],
)

```

All evaluations performed using DeepEval can be viewed on the [Confident AI Dashboard](https://app.confident-ai.com/).

You can scale this process with a dataset (e.g. from Hugging Face) and evaluate multiple test cases at once by looping through question-answer pairs, querying Qdrant for context, and scoring with DeepEval metrics.

## [Anchor](https://qdrant.tech/documentation/frameworks/deepeval/\#further-reading) Further Reading

- [End-to-end Evalutation Example](https://github.com/qdrant/qdrant-rag-eval/blob/master/workshop-rag-eval-qdrant-deepeval/notebook/rag_eval_qdrant_deepeval.ipynb)
- [DeepEval documentation](https://deepeval.com/)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/deepeval.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/deepeval.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573638394&cv=11&fst=1748573638394&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdeepeval%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=DeepEval%20-%20Qdrant&npa=0&pscdl=noapi&auid=1327980695.1748573638&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573638373&cv=11&fst=1748573638373&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdeepeval%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=DeepEval%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1327980695.1748573638&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1d704050-f1a6-4f5e-9822-0a158f48b279&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=01f6f66f-2043-4cc5-9312-687b9dbe626d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdeepeval%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1d704050-f1a6-4f5e-9822-0a158f48b279&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=01f6f66f-2043-4cc5-9312-687b9dbe626d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdeepeval%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573639231&cv=11&fst=1748573639231&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdeepeval%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=DeepEval%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1327980695.1748573638&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)