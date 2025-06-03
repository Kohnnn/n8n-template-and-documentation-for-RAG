---
url: "https://qdrant.tech/articles/detecting-coffee-anomalies/"
title: "Metric Learning for Anomaly Detection - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Metric Learning for Anomaly Detection

[Back to Machine Learning](https://qdrant.tech/articles/machine-learning/)

# Metric Learning for Anomaly Detection

Yusuf Sarıgöz

·

May 04, 2022

![Metric Learning for Anomaly Detection](https://qdrant.tech/articles_data/detecting-coffee-anomalies/preview/title.jpg)

Anomaly detection is a thirsting yet challenging task that has numerous use cases across various industries.
The complexity results mainly from the fact that the task is data-scarce by definition.

Similarly, anomalies are, again by definition, subject to frequent change, and they may take unexpected forms.
For that reason, supervised classification-based approaches are:

- Data-hungry - requiring quite a number of labeled data;
- Expensive - data labeling is an expensive task itself;
- Time-consuming - you would try to obtain what is necessarily scarce;
- Hard to maintain - you would need to re-train the model repeatedly in response to changes in the data distribution.

These are not desirable features if you want to put your model into production in a rapidly-changing environment.
And, despite all the mentioned difficulties, they do not necessarily offer superior performance compared to the alternatives.
In this post, we will detail the lessons learned from such a use case.

## [Anchor](https://qdrant.tech/articles/detecting-coffee-anomalies/\#coffee-beans) Coffee Beans

[Agrivero.ai](https://agrivero.ai/) \- is a company making AI-enabled solution for quality control & traceability of green coffee for producers, traders, and roasters.
They have collected and labeled more than **30 thousand** images of coffee beans with various defects - wet, broken, chipped, or bug-infested samples.
This data is used to train a classifier that evaluates crop quality and highlights possible problems.

![Anomalies in coffee](https://qdrant.tech/articles_data/detecting-coffee-anomalies/detection.gif)

Anomalies in coffee

We should note that anomalies are very diverse, so the enumeration of all possible anomalies is a challenging task on it’s own.
In the course of work, new types of defects appear, and shooting conditions change. Thus, a one-time labeled dataset becomes insufficient.

Let’s find out how metric learning might help to address this challenge.

## [Anchor](https://qdrant.tech/articles/detecting-coffee-anomalies/\#metric-learning-approach) Metric Learning Approach

In this approach, we aimed to encode images in an n-dimensional vector space and then use learned similarities to label images during the inference.

The simplest way to do this is KNN classification.
The algorithm retrieves K-nearest neighbors to a given query vector and assigns a label based on the majority vote.

In production environment kNN classifier could be easily replaced with [Qdrant](https://github.com/qdrant/qdrant) vector search engine.

![Production deployment](https://qdrant.tech/articles_data/detecting-coffee-anomalies/anomalies_detection.png)

Production deployment

This approach has the following advantages:

- We can benefit from unlabeled data, considering labeling is time-consuming and expensive.
- The relevant metric, e.g., precision or recall, can be tuned according to changing requirements during the inference without re-training.
- Queries labeled with a high score can be added to the KNN classifier on the fly as new data points.

To apply metric learning, we need to have a neural encoder, a model capable of transforming an image into a vector.

Training such an encoder from scratch may require a significant amount of data we might not have. Therefore, we will divide the training into two steps:

- The first step is to train the autoencoder, with which we will prepare a model capable of representing the target domain.

- The second step is finetuning. Its purpose is to train the model to distinguish the required types of anomalies.


![Model training architecture](https://qdrant.tech/articles_data/detecting-coffee-anomalies/anomaly_detection_training.png)

Model training architecture

### [Anchor](https://qdrant.tech/articles/detecting-coffee-anomalies/\#step-1---autoencoder-for-unlabeled-data) Step 1 - Autoencoder for Unlabeled Data

First, we pretrained a Resnet18-like model in a vanilla autoencoder architecture by leaving the labels aside.
Autoencoder is a model architecture composed of an encoder and a decoder, with the latter trying to recreate the original input from the low-dimensional bottleneck output of the former.

There is no intuitive evaluation metric to indicate the performance in this setup, but we can evaluate the success by examining the recreated samples visually.

![Example of image reconstruction with Autoencoder](https://qdrant.tech/articles_data/detecting-coffee-anomalies/image_reconstruction.png)

Example of image reconstruction with Autoencoder

Then we encoded a subset of the data into 128-dimensional vectors by using the encoder,
and created a KNN classifier on top of these embeddings and associated labels.

Although the results are promising, we can do even better by finetuning with metric learning.

### [Anchor](https://qdrant.tech/articles/detecting-coffee-anomalies/\#step-2---finetuning-with-metric-learning) Step 2 - Finetuning with Metric Learning

We started by selecting 200 labeled samples randomly without replacement.

In this step, The model was composed of the encoder part of the autoencoder with a randomly initialized projection layer stacked on top of it.
We applied transfer learning from the frozen encoder and trained only the projection layer with Triplet Loss and an online batch-all triplet mining strategy.

Unfortunately, the model overfitted quickly in this attempt.
In the next experiment, we used an online batch-hard strategy with a trick to prevent vector space from collapsing.
We will describe our approach in the further articles.

This time it converged smoothly, and our evaluation metrics also improved considerably to match the supervised classification approach.

![Metrics for the autoencoder model with KNN classifier](https://qdrant.tech/articles_data/detecting-coffee-anomalies/ae_report_knn.png)

Metrics for the autoencoder model with KNN classifier

![Metrics for the finetuned model with KNN classifier](https://qdrant.tech/articles_data/detecting-coffee-anomalies/ft_report_knn.png)

Metrics for the finetuned model with KNN classifier

We repeated this experiment with 500 and 2000 samples, but it showed only a slight improvement.
Thus we decided to stick to 200 samples - see below for why.

## [Anchor](https://qdrant.tech/articles/detecting-coffee-anomalies/\#supervised-classification-approach) Supervised Classification Approach

We also wanted to compare our results with the metrics of a traditional supervised classification model.
For this purpose, a Resnet50 model was finetuned with ~30k labeled images, made available for training.
Surprisingly, the F1 score was around ~0.86.

Please note that we used only 200 labeled samples in the metric learning approach instead of ~30k in the supervised classification approach.
These numbers indicate a huge saving with no considerable compromise in the performance.

## [Anchor](https://qdrant.tech/articles/detecting-coffee-anomalies/\#conclusion) Conclusion

We obtained results comparable to those of the supervised classification method by using **only 0.66%** of the labeled data with metric learning.
This approach is time-saving and resource-efficient, and that may be improved further. Possible next steps might be:

- Collect more unlabeled data and pretrain a larger autoencoder.
- Obtain high-quality labels for a small number of images instead of tens of thousands for finetuning.
- Use hyperparameter optimization and possibly gradual unfreezing in the finetuning step.
- Use [vector search engine](https://github.com/qdrant/qdrant) to serve Metric Learning in production.

We are actively looking into these, and we will continue to publish our findings in this challenge and other use cases of metric learning.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/detecting-coffee-anomalies.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/detecting-coffee-anomalies.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574551441&cv=11&fst=1748574551441&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdetecting-coffee-anomalies%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Metric%20Learning%20for%20Anomaly%20Detection%20-%20Qdrant&npa=0&pscdl=noapi&auid=487084425.1748574551&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574551422&cv=11&fst=1748574551422&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdetecting-coffee-anomalies%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Metric%20Learning%20for%20Anomaly%20Detection%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=487084425.1748574551&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=772f3328-713d-42dd-9c63-7911b37cf812&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1b3f6aae-562a-4977-96a8-592a33f61927&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdetecting-coffee-anomalies%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=772f3328-713d-42dd-9c63-7911b37cf812&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1b3f6aae-562a-4977-96a8-592a33f61927&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdetecting-coffee-anomalies%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574552569&cv=11&fst=1748574552569&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdetecting-coffee-anomalies%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Metric%20Learning%20for%20Anomaly%20Detection%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=487084425.1748574551&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)