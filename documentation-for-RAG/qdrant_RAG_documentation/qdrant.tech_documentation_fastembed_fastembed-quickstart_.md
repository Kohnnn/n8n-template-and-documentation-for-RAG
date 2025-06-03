---
url: "https://qdrant.tech/documentation/fastembed/fastembed-quickstart/"
title: "Quickstart - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Fastembed](https://qdrant.tech/documentation/fastembed/)
- Quickstart

# [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-quickstart/\#how-to-generate-text-embedings-with-fastembed) How to Generate Text Embedings with FastEmbed

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-quickstart/\#install-fastembed) Install FastEmbed

```python
pip install fastembed

```

Just for demo purposes, you will use Lists and NumPy to work with sample data.

```python
from typing import List
import numpy as np

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-quickstart/\#load-default-model) Load default model

In this example, you will use the default text embedding model, `BAAI/bge-small-en-v1.5`.

```python
from fastembed import TextEmbedding

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-quickstart/\#add-sample-data) Add sample data

Now, add two sample documents. Your documents must be in a list, and each document must be a string

```python
documents: List[str] = [\
    "FastEmbed is lighter than Transformers & Sentence-Transformers.",\
    "FastEmbed is supported by and maintained by Qdrant.",\
]

```

Download and initialize the model. Print a message to verify the process.

```python
embedding_model = TextEmbedding()
print("The model BAAI/bge-small-en-v1.5 is ready to use.")

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-quickstart/\#embed-data) Embed data

Generate embeddings for both documents.

```python
embeddings_generator = embedding_model.embed(documents)
embeddings_list = list(embeddings_generator)
len(embeddings_list[0])

```

Here is the sample document list. The default model creates vectors with 384 dimensions.

```bash
Document: This is built to be faster and lighter than other embedding libraries e.g. Transformers, Sentence-Transformers, etc.
Vector of type: <class 'numpy.ndarray'> with shape: (384,)
Document: fastembed is supported by and maintained by Qdrant.
Vector of type: <class 'numpy.ndarray'> with shape: (384,)

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-quickstart/\#visualize-embeddings) Visualize embeddings

```python
print("Embeddings:\n", embeddings_list)

```

The embeddings don’t look too interesting, but here is a visual.

```bash
Embeddings:
 [[-0.11154681  0.00976555  0.00524559  0.01951888 -0.01934952  0.02943449\
  -0.10519084 -0.00890122  0.01831438  0.01486796 -0.05642502  0.02561352\
  -0.00120165  0.00637456  0.02633459  0.0089221   0.05313658  0.03955453\
  -0.04400245 -0.02929407  0.04691846 -0.02515868  0.00778646 -0.05410657\
...\
  -0.00243012 -0.01820582  0.02938612  0.02108984 -0.02178085  0.02971899\
  -0.00790564  0.03561783  0.0652488  -0.04371546 -0.05550042  0.02651665\
  -0.01116153 -0.01682246 -0.05976734 -0.03143916  0.06522726  0.01801389\
  -0.02611006  0.01627177 -0.0368538   0.03968835  0.027597    0.03305927]]

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-quickstart.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-quickstart.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574296354&cv=11&fst=1748574296354&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-quickstart%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Quickstart%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=647848301.1748574296&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574296435&cv=11&fst=1748574296435&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-quickstart%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Quickstart%20-%20Qdrant&npa=0&pscdl=noapi&auid=647848301.1748574296&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=15d78aa9-4baa-42d7-8f78-8cb190e5cafd&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9359afd3-58bb-4ad5-b201-3e9956cd3e60&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-quickstart%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=15d78aa9-4baa-42d7-8f78-8cb190e5cafd&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9359afd3-58bb-4ad5-b201-3e9956cd3e60&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-quickstart%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574297497&cv=11&fst=1748574297497&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-quickstart%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Quickstart%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=647848301.1748574296&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)