---
url: "https://qdrant.tech/articles/metric-learning-tips/"
title: "Metric Learning Tips & Tricks - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Metric Learning Tips & Tricks

[Back to Machine Learning](https://qdrant.tech/articles/machine-learning/)

# Metric Learning Tips & Tricks

Andrei Vasnetsov

·

May 15, 2021

![Metric Learning Tips & Tricks](https://qdrant.tech/articles_data/metric-learning-tips/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#how-to-train-object-matching-model-with-no-labeled-data-and-use-it-in-production) How to train object matching model with no labeled data and use it in production

Currently, most machine-learning-related business cases are solved as a classification problems.
Classification algorithms are so well studied in practice that even if the original problem is not directly a classification task, it is usually decomposed or approximately converted into one.

However, despite its simplicity, the classification task has requirements that could complicate its production integration and scaling.
E.g. it requires a fixed number of classes, where each class should have a sufficient number of training samples.

In this article, I will describe how we overcome these limitations by switching to metric learning.
By the example of matching job positions and candidates, I will show how to train metric learning model with no manually labeled data, how to estimate prediction confidence, and how to serve metric learning in production.

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#what-is-metric-learning-and-why-using-it) What is metric learning and why using it?

According to Wikipedia, metric learning is the task of learning a distance function over objects.
In practice, it means that we can train a model that tells a number for any pair of given objects.
And this number should represent a degree or score of similarity between those given objects.
For example, objects with a score of 0.9 could be more similar than objects with a score of 0.5
Actual scores and their direction could vary among different implementations.

In practice, there are two main approaches to metric learning and two corresponding types of NN architectures.
The first is the interaction-based approach, which first builds local interactions (i.e., local matching signals) between two objects. Deep neural networks learn hierarchical interaction patterns for matching.
Examples of neural network architectures include MV-LSTM, ARC-II, and MatchPyramid.

![MV-LSTM, example of interaction-based model](https://gist.githubusercontent.com/generall/4821e3c6b5eee603d56729e7a156e461/raw/b0eb4ea5d088fe1095e529eb12708ac69f304ce3/mv_lstm.png)

> MV-LSTM, example of interaction-based model, [Shengxian Wan et al.](https://www.researchgate.net/figure/Illustration-of-MV-LSTM-S-X-and-S-Y-are-the-in_fig1_285271115) via Researchgate

The second is the representation-based approach.
In this case distance function is composed of 2 components:
the Encoder transforms an object into embedded representation - usually a large float point vector, and the Comparator takes embeddings of a pair of objects from the Encoder and calculates their similarity.
The most well-known example of this embedding representation is Word2Vec.

Examples of neural network architectures also include DSSM, C-DSSM, and ARC-I.

The Comparator is usually a very simple function that could be calculated very quickly.
It might be cosine similarity or even a dot production.
Two-stage schema allows performing complex calculations only once per object.
Once transformed, the Comparator can calculate object similarity independent of the Encoder much more quickly.
For more convenience, embeddings can be placed into specialized storages or vector search engines.
These search engines allow to manage embeddings using API, perform searches and other operations with vectors.

![C-DSSM, example of representation-based model](https://gist.githubusercontent.com/generall/4821e3c6b5eee603d56729e7a156e461/raw/b0eb4ea5d088fe1095e529eb12708ac69f304ce3/cdssm.png)

> C-DSSM, example of representation-based model, [Xue Li et al.](https://arxiv.org/abs/1901.10710v2) via arXiv

Pre-trained NNs can also be used. The output of the second-to-last layer could work as an embedded representation.
Further in this article, I would focus on the representation-based approach, as it proved to be more flexible and fast.

So what are the advantages of using metric learning comparing to classification?
Object Encoder does not assume the number of classes.
So if you can’t split your object into classes,
if the number of classes is too high, or you suspect that it could grow in the future - consider using metric learning.

In our case, business goal was to find suitable vacancies for candidates who specify the title of the desired position.
To solve this, we used to apply a classifier to determine the job category of the vacancy and the candidate.
But this solution was limited to only a few hundred categories.
Candidates were complaining that they couldn’t find the right category for them.
Training the classifier for new categories would be too long and require new training data for each new category.
Switching to metric learning allowed us to overcome these limitations, the resulting solution could compare any pair position descriptions, even if we don’t have this category reference yet.

![T-SNE with job samples](https://gist.githubusercontent.com/generall/4821e3c6b5eee603d56729e7a156e461/raw/b0eb4ea5d088fe1095e529eb12708ac69f304ce3/embeddings.png)

> T-SNE with job samples, Image by Author. Play with [Embedding Projector](https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/generall/7e712425e3b340c2c4dbc1a29f515d91/raw/b45b2b6f6c1d5ab3d3363c50805f3834a85c8879/config.json) yourself.

With metric learning, we learn not a concrete job type but how to match job descriptions from a candidate’s CV and a vacancy.
Secondly, with metric learning, it is easy to add more reference occupations without model retraining.
We can then add the reference to a vector search engine.
Next time we will match occupations - this new reference vector will be searchable.

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#data-for-metric-learning) Data for metric learning

Unlike classifiers, a metric learning training does not require specific class labels.
All that is required are examples of similar and dissimilar objects.
We would call them positive and negative samples.

At the same time, it could be a relative similarity between a pair of objects.
For example, twins look more alike to each other than a pair of random people.
And random people are more similar to each other than a man and a cat.
A model can use such relative examples for learning.

The good news is that the division into classes is only a special case of determining similarity.
To use such datasets, it is enough to declare samples from one class as positive and samples from another class as negative.
In this way, it is possible to combine several datasets with mismatched classes into one generalized dataset for metric learning.

But not only datasets with division into classes are suitable for extracting positive and negative examples.
If, for example, there are additional features in the description of the object, the value of these features can also be used as a similarity factor.
It may not be as explicit as class membership, but the relative similarity is also suitable for learning.

In the case of job descriptions, there are many ontologies of occupations, which were able to be combined into a single dataset thanks to this approach.
We even went a step further and used identical job titles to find similar descriptions.

As a result, we got a self-supervised universal dataset that did not require any manual labeling.

Unfortunately, universality does not allow some techniques to be applied in training.
Next, I will describe how to overcome this disadvantage.

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#training-the-model) Training the model

There are several ways to train a metric learning model.
Among the most popular is the use of Triplet or Contrastive loss functions, but I will not go deep into them in this article.
However, I will tell you about one interesting trick that helped us work with unified training examples.

One of the most important practices to efficiently train the metric learning model is hard negative mining.
This technique aims to include negative samples on which model gave worse predictions during the last training epoch.
Most articles that describe this technique assume that training data consists of many small classes (in most cases it is people’s faces).
With data like this, it is easy to find bad samples - if two samples from different classes have a high similarity score, we can use it as a negative sample.
But we had no such classes in our data, the only thing we have is occupation pairs assumed to be similar in some way.
We cannot guarantee that there is no better match for each job occupation among this pair.
That is why we can’t use hard negative mining for our model.

![Loss variations](https://gist.githubusercontent.com/generall/4821e3c6b5eee603d56729e7a156e461/raw/b0eb4ea5d088fe1095e529eb12708ac69f304ce3/losses.png)

> [Alfonso Medela et al.](https://arxiv.org/abs/1905.10675) via arXiv

To compensate for this limitation we can try to increase the number of random (weak) negative samples.
One way to achieve this is to train the model longer, so it will see more samples by the end of the training.
But we found a better solution in adjusting our loss function.
In a regular implementation of Triplet or Contractive loss, each positive pair is compared with some or a few negative samples.
What we did is we allow pair comparison amongst the whole batch.
That means that loss-function penalizes all pairs of random objects if its score exceeds any of the positive scores in a batch.
This extension gives `~ N * B^2` comparisons where `B` is a size of batch and `N` is a number of batches.
Much bigger than `~ N * B` in regular triplet loss.
This means that increasing the size of the batch significantly increases the number of negative comparisons, and therefore should improve the model performance.
We were able to observe this dependence in our experiments.
Similar idea we also found in the article [Supervised Contrastive Learning](https://arxiv.org/abs/2004.11362).

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#model-confidence) Model confidence

In real life it is often needed to know how confident the model was in the prediction.
Whether manual adjustment or validation of the result is required.

With conventional classification, it is easy to understand by scores how confident the model is in the result.
If the probability values of different classes are close to each other, the model is not confident.
If, on the contrary, the most probable class differs greatly, then the model is confident.

At first glance, this cannot be applied to metric learning.
Even if the predicted object similarity score is small it might only mean that the reference set has no proper objects to compare with.
Conversely, the model can group garbage objects with a large score.

Fortunately, we found a small modification to the embedding generator, which allows us to define confidence in the same way as it is done in conventional classifiers with a Softmax activation function.
The modification consists in building an embedding as a combination of feature groups.
Each feature group is presented as a one-hot encoded sub-vector in the embedding.
If the model can confidently predict the feature value - the corresponding sub-vector will have a high absolute value in some of its elements.
For a more intuitive understanding, I recommend thinking about embeddings not as points in space, but as a set of binary features.

To implement this modification and form proper feature groups we would need to change a regular linear output layer to a concatenation of several Softmax layers.
Each softmax component would represent an independent feature and force the neural network to learn them.

Let’s take for example that we have 4 softmax components with 128 elements each.
Every such component could be roughly imagined as a one-hot-encoded number in the range of 0 to 127.
Thus, the resulting vector will represent one of `128^4` possible combinations.
If the trained model is good enough, you can even try to interpret the values of singular features individually.

![Softmax feature embeddings](https://gist.githubusercontent.com/generall/4821e3c6b5eee603d56729e7a156e461/raw/b0eb4ea5d088fe1095e529eb12708ac69f304ce3/feature_embedding.png)

> Softmax feature embeddings, Image by Author.

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#neural-rules) Neural rules

Machine learning models rarely train to 100% accuracy.
In a conventional classifier, errors can only be eliminated by modifying and repeating the training process.
Metric training, however, is more flexible in this matter and allows you to introduce additional steps that allow you to correct the errors of an already trained model.

A common error of the metric learning model is erroneously declaring objects close although in reality they are not.
To correct this kind of error, we introduce exclusion rules.

Rules consist of 2 object anchors encoded into vector space.
If the target object falls into one of the anchors’ effects area - it triggers the rule. It will exclude all objects in the second anchor area from the prediction result.

![Exclusion rules](https://gist.githubusercontent.com/generall/4821e3c6b5eee603d56729e7a156e461/raw/b0eb4ea5d088fe1095e529eb12708ac69f304ce3/exclusion_rule.png)

> Neural exclusion rules, Image by Author.

The convenience of working with embeddings is that regardless of the number of rules,
you only need to perform the encoding once per object.
Then to find a suitable rule, it is enough to compare the target object’s embedding and the pre-calculated embeddings of the rule’s anchors.
Which, when implemented, translates into just one additional query to the vector search engine.

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#vector-search-in-production) Vector search in production

When implementing a metric learning model in production, the question arises about the storage and management of vectors.
It should be easy to add new vectors if new job descriptions appear in the service.

In our case, we also needed to apply additional conditions to the search.
We needed to filter, for example, the location of candidates and the level of language proficiency.

We did not find a ready-made tool for such vector management, so we created [Qdrant](https://github.com/qdrant/qdrant) \- open-source vector search engine.

It allows you to add and delete vectors with a simple API, independent of a programming language you are using.
You can also assign the payload to vectors.
This payload allows additional filtering during the search request.

Qdrant has a pre-built docker image and start working with it is just as simple as running

```bash
docker run -p 6333:6333 qdrant/qdrant

```

Documentation with examples could be found [here](https://api.qdrant.tech/api-reference).

## [Anchor](https://qdrant.tech/articles/metric-learning-tips/\#conclusion) Conclusion

In this article, I have shown how metric learning can be more scalable and flexible than the classification models.
I suggest trying similar approaches in your tasks - it might be matching similar texts, images, or audio data.
With the existing variety of pre-trained neural networks and a vector search engine, it is easy to build your metric learning-based application.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/metric-learning-tips.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/metric-learning-tips.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e51e1604-188d-4512-82a4-cc9558d22f2b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=349d0cb9-3ecc-4c57-8b84-ed7097698e29&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmetric-learning-tips%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573664809&cv=11&fst=1748573664809&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmetric-learning-tips%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Metric%20Learning%20Tips%20%26%20Tricks%20-%20Qdrant&npa=0&pscdl=noapi&auid=610929538.1748573664&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573664787&cv=11&fst=1748573664787&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmetric-learning-tips%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Metric%20Learning%20Tips%20%26%20Tricks%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=610929538.1748573664&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573665001&cv=11&fst=1748573665001&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmetric-learning-tips%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Metric%20Learning%20Tips%20%26%20Tricks%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=610929538.1748573664&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e51e1604-188d-4512-82a4-cc9558d22f2b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=349d0cb9-3ecc-4c57-8b84-ed7097698e29&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmetric-learning-tips%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)