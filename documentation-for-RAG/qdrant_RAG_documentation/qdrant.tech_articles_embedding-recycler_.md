---
url: "https://qdrant.tech/articles/embedding-recycler/"
title: "Layer Recycling and Fine-tuning Efficiency - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Layer Recycling and Fine-tuning Efficiency

[Back to Machine Learning](https://qdrant.tech/articles/machine-learning/)

# Layer Recycling and Fine-tuning Efficiency

Yusuf Sarıgöz

·

August 23, 2022

![Layer Recycling and Fine-tuning Efficiency](https://qdrant.tech/articles_data/embedding-recycling/preview/title.jpg)

A recent [paper](https://arxiv.org/abs/2207.04993)
by Allen AI has attracted attention in the NLP community as they cache the output of a certain intermediate layer
in the training and inference phases to achieve a speedup of ~83%
with a negligible loss in model performance.
This technique is quite similar to [the caching mechanism in Quaterion](https://quaterion.qdrant.tech/tutorials/cache_tutorial.html),
but the latter is intended for any data modalities while the former focuses only on language models
despite presenting important insights from their experiments.
In this post, I will share our findings combined with those,
hoping to provide the community with a wider perspective on layer recycling.

## [Anchor](https://qdrant.tech/articles/embedding-recycler/\#how-layer-recycling-works) How layer recycling works

The main idea of layer recycling is to accelerate the training (and inference)
by avoiding repeated passes of the same data object through the frozen layers.
Instead, it is possible to pass objects through those layers only once,
cache the output
and use them as inputs to the unfrozen layers in future epochs.

In the paper, they usually cache 50% of the layers, e.g., the output of the 6th multi-head self-attention block in a 12-block encoder.
However, they find out that it does not work equally for all the tasks.
For example, the question answering task suffers from a more significant degradation in performance with 50% of the layers recycled,
and they choose to lower it down to 25% for this task,
so they suggest determining the level of caching based on the task at hand.
they also note that caching provides a more considerable speedup for larger models and on lower-end machines.

In layer recycling, the cache is hit for exactly the same object.
It is easy to achieve this in textual data as it is easily hashable,
but you may need more advanced tricks to generate keys for the cache
when you want to generalize this technique to diverse data types.
For instance, hashing PyTorch tensors [does not work as you may expect](https://github.com/joblib/joblib/issues/1282).
Quaterion comes with an intelligent key extractor that may be applied to any data type,
but it is also allowed to customize it with a callable passed as an argument.
Thanks to this flexibility, we were able to run a variety of experiments in different setups,
and I believe that these findings will be helpful for your future projects.

## [Anchor](https://qdrant.tech/articles/embedding-recycler/\#experiments) Experiments

We conducted different experiments to test the performance with:

1. Different numbers of layers recycled in [the similar cars search example](https://quaterion.qdrant.tech/tutorials/cars-tutorial.html).
2. Different numbers of samples in the dataset for training and fine-tuning for similar cars search.
3. Different numbers of layers recycled in [the question answerring example](https://quaterion.qdrant.tech/tutorials/nlp_tutorial.html).

## [Anchor](https://qdrant.tech/articles/embedding-recycler/\#easy-layer-recycling-with-quaterion) Easy layer recycling with Quaterion

The easiest way of caching layers in Quaterion is to compose a [TrainableModel](https://quaterion.qdrant.tech/quaterion.train.trainable_model.html#quaterion.train.trainable_model.TrainableModel)
with a frozen [Encoder](https://quaterion-models.qdrant.tech/quaterion_models.encoders.encoder.html#quaterion_models.encoders.encoder.Encoder)
and an unfrozen [EncoderHead](https://quaterion-models.qdrant.tech/quaterion_models.heads.encoder_head.html#quaterion_models.heads.encoder_head.EncoderHead).
Therefore, we modified the `TrainableModel` in the [example](https://github.com/qdrant/quaterion/blob/master/examples/cars/models.py)
as in the following:

```python
class Model(TrainableModel):
    # ...

    def configure_encoders(self) -> Union[Encoder, Dict[str, Encoder]]:
        pre_trained_encoder = torchvision.models.resnet34(pretrained=True)
        self.avgpool = copy.deepcopy(pre_trained_encoder.avgpool)
        self.finetuned_block = copy.deepcopy(pre_trained_encoder.layer4)
        modules = []

        for name, child in pre_trained_encoder.named_children():
            modules.append(child)
            if name == "layer3":
                break

        pre_trained_encoder = nn.Sequential(*modules)

        return CarsEncoder(pre_trained_encoder)

    def configure_head(self, input_embedding_size) -> EncoderHead:
        return SequentialHead(self.finetuned_block,
        self.avgpool,
        nn.Flatten(),
        SkipConnectionHead(512, dropout=0.3, skip_dropout=0.2),
        output_size=512)

    # ...

```

This trick lets us finetune one more layer from the base model as a part of the `EncoderHead`
while still benefiting from the speedup in the frozen `Encoder` provided by the cache.

## [Anchor](https://qdrant.tech/articles/embedding-recycler/\#experiment-1-percentage-of-layers-recycled) Experiment 1: Percentage of layers recycled

The paper states that recycling 50% of the layers yields little to no loss in performance when compared to full fine-tuning.
In this setup, we compared performances of four methods:

1. Freeze the whole base model and train only `EncoderHead`.
2. Move one of the four residual blocks `EncoderHead` and train it together with the head layer while freezing the rest (75% layer recycling).
3. Move two of the four residual blocks to `EncoderHead` while freezing the rest (50% layer recycling).
4. Train the whole base model together with `EncoderHead`.

**Note**: During these experiments, we used ResNet34 instead of ResNet152 as the pretrained model
in order to be able to use a reasonable batch size in full training.
The baseline score with ResNet34 is 0.106.

| Model | RRP |
| --- | --- |
| Full training | 0.32 |
| 50% recycling | 0.31 |
| 75% recycling | 0.28 |
| Head only | 0.22 |
| Baseline | 0.11 |

As is seen in the table, the performance in 50% layer recycling is very close to that in full training.
Additionally, we can still have a considerable speedup in 50% layer recycling with only a small drop in performance.
Although 75% layer recycling is better than training only `EncoderHead`,
its performance drops quickly when compared to 50% layer recycling and full training.

## [Anchor](https://qdrant.tech/articles/embedding-recycler/\#experiment-2-amount-of-available-data) Experiment 2: Amount of available data

In the second experiment setup, we compared performances of fine-tuning strategies with different dataset sizes.
We sampled 50% of the training set randomly while still evaluating models on the whole validation set.

| Model | RRP |
| --- | --- |
| Full training | 0.27 |
| 50% recycling | 0.26 |
| 75% recycling | 0.25 |
| Head only | 0.21 |
| Baseline | 0.11 |

This experiment shows that, the smaller the available dataset is,
the bigger drop in performance we observe in full training, 50% and 75% layer recycling.
On the other hand, the level of degradation in training only `EncoderHead` is really small when compared to others.
When we further reduce the dataset size, full training becomes untrainable at some point,
while we can still improve over the baseline by training only `EncoderHead`.

## [Anchor](https://qdrant.tech/articles/embedding-recycler/\#experiment-3-layer-recycling-in-question-answering) Experiment 3: Layer recycling in question answering

We also wanted to test layer recycling in a different domain
as one of the most important takeaways of the paper is that
the performance of layer recycling is task-dependent.
To this end, we set up an experiment with the code from the [Question Answering with Similarity Learning tutorial](https://quaterion.qdrant.tech/tutorials/nlp_tutorial.html).

| Model | RP@1 | RRK |
| --- | --- | --- |
| Full training | 0.76 | 0.65 |
| 50% recycling | 0.75 | 0.63 |
| 75% recycling | 0.69 | 0.59 |
| Head only | 0.67 | 0.58 |
| Baseline | 0.64 | 0.55 |

In this task, 50% layer recycling can still do a good job with only a small drop in performance when compared to full training.
However, the level of degradation is smaller than that in the similar cars search example.
This can be attributed to several factors such as the pretrained model quality, dataset size and task definition,
and it can be the subject of a more elaborate and comprehensive research project.
Another observation is that the performance of 75% layer recycling is closer to that of training only `EncoderHead`
than 50% layer recycling.

## [Anchor](https://qdrant.tech/articles/embedding-recycler/\#conclusion) Conclusion

We set up several experiments to test layer recycling under different constraints
and confirmed that layer recycling yields varying performances with different tasks and domains.
One of the most important observations is the fact that the level of degradation in layer recycling
is sublinear with a comparison to full training, i.e., we lose a smaller percentage of performance than
the percentage we recycle. Additionally, training only `EncoderHead`
is more resistant to small dataset sizes.
There is even a critical size under which full training does not work at all.
The issue of performance differences shows that there is still room for further research on layer recycling,
and luckily Quaterion is flexible enough to run such experiments quickly.
We will continue to report our findings on fine-tuning efficiency.

**Fun fact**: The preview image for this article was created with Dall.e with the following prompt: “Photo-realistic robot using a tuning fork to adjust a piano.”
[Click here](https://qdrant.tech/articles_data/embedding-recycling/full.png)
to see it in full size!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/embedding-recycler.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/embedding-recycler.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573837985&cv=11&fst=1748573837985&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fembedding-recycler%2F&hn=www.googleadservices.com&frm=0&tiba=Layer%20Recycling%20and%20Fine-tuning%20Efficiency%20-%20Qdrant&npa=0&pscdl=noapi&auid=303805152.1748573838&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573837955&cv=11&fst=1748573837955&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fembedding-recycler%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Layer%20Recycling%20and%20Fine-tuning%20Efficiency%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=303805152.1748573838&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=11213839-1101-4dc8-bcfd-70078063ea4d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9c1d395e-aaa9-4103-bfca-1315c5f7769f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fembedding-recycler%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=11213839-1101-4dc8-bcfd-70078063ea4d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9c1d395e-aaa9-4103-bfca-1315c5f7769f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fembedding-recycler%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573839245&cv=11&fst=1748573839245&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fembedding-recycler%2F&hn=www.googleadservices.com&frm=0&tiba=Layer%20Recycling%20and%20Fine-tuning%20Efficiency%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=303805152.1748573838&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)