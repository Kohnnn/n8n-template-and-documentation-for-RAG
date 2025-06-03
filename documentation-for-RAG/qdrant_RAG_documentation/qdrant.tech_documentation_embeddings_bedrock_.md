---
url: "https://qdrant.tech/documentation/embeddings/bedrock/"
title: "AWS Bedrock - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- AWS Bedrock

# [Anchor](https://qdrant.tech/documentation/embeddings/bedrock/\#bedrock-embeddings) Bedrock Embeddings

You can use [AWS Bedrock](https://aws.amazon.com/bedrock/) with Qdrant. AWS Bedrock supports multiple [embedding model providers](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html).

You’ll need the following information from your AWS account:

- Region
- Access key ID
- Secret key

To configure your credentials, review the following AWS article: [How do I create an AWS access key](https://repost.aws/knowledge-center/create-access-key).

With the following code sample, you can generate embeddings using the [Titan Embeddings G1 - Text model](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) which produces sentence embeddings of size 1536.

pythonjavascript

```python
# Install the required dependencies
# pip install boto3 qdrant_client

import json
import boto3

from qdrant_client import QdrantClient, models

session = boto3.Session()

bedrock_client = session.client(
    "bedrock-runtime",
    region_name="<YOUR_AWS_REGION>",
    aws_access_key_id="<YOUR_AWS_ACCESS_KEY_ID>",
    aws_secret_access_key="<YOUR_AWS_SECRET_KEY>",
)

qdrant_client = QdrantClient(url="http://localhost:6333")

qdrant_client.create_collection(
    "{collection_name}",
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
)

body = json.dumps({"inputText": "Some text to generate embeddings for"})

response = bedrock_client.invoke_model(
    body=body,
    modelId="amazon.titan-embed-text-v1",
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())

qdrant_client.upsert(
    "{collection_name}",
    points=[models.PointStruct(id=1, vector=response_body["embedding"])],
)

```

```javascript
// Install the required dependencies
// npm install @aws-sdk/client-bedrock-runtime @qdrant/js-client-rest

import {
    BedrockRuntimeClient,
    InvokeModelCommand,
} from "@aws-sdk/client-bedrock-runtime";
import { QdrantClient } from '@qdrant/js-client-rest';

const main = async () => {
    const bedrockClient = new BedrockRuntimeClient({
        region: "<YOUR_AWS_REGION>",
        credentials: {
            accessKeyId: "<YOUR_AWS_ACCESS_KEY_ID>",,
            secretAccessKey: "<YOUR_AWS_SECRET_KEY>",
        },
    });

    const qdrantClient = new QdrantClient({ url: 'http://localhost:6333' });

    await qdrantClient.createCollection("{collection_name}", {
        vectors: {
            size: 1536,
            distance: 'Cosine',
        }
    });

    const response = await bedrockClient.send(
        new InvokeModelCommand({
            modelId: "amazon.titan-embed-text-v1",
            body: JSON.stringify({
                inputText: "Some text to generate embeddings for",
            }),
            contentType: "application/json",
            accept: "application/json",
        })
    );

    const body = new TextDecoder().decode(response.body);

    await qdrantClient.upsert("{collection_name}", {
        points: [\
            {\
                id: 1,\
                vector: JSON.parse(body).embedding,\
            },\
        ],
    });
}

main();

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/bedrock.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/bedrock.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574739505&cv=11&fst=1748574739505&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694~104611959~104611961&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fbedrock%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=AWS%20Bedrock%20-%20Qdrant&npa=0&pscdl=noapi&auid=1243944800.1748574739&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574739484&cv=11&fst=1748574739484&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694~104611959~104611961&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fbedrock%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=AWS%20Bedrock%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1243944800.1748574739&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1f3997fe-506e-4c05-b799-976f3c7dfc06&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3f413250-9d36-434c-9955-6b40c790ed28&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fbedrock%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1f3997fe-506e-4c05-b799-976f3c7dfc06&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3f413250-9d36-434c-9955-6b40c790ed28&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fbedrock%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574740528&cv=11&fst=1748574740528&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694~104611959~104611961&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fbedrock%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=AWS%20Bedrock%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1243944800.1748574739&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)