---
url: "https://qdrant.tech/blog/binary-quantization/"
title: "Binary Quantization - Andrey Vasnetsov | Vector Space Talks - Qdrant"
---

0

# Binary Quantization - Andrey Vasnetsov \| Vector Space Talks

Demetrios Brinkmann

·

January 09, 2024

![Binary Quantization - Andrey Vasnetsov | Vector Space Talks](https://qdrant.tech/blog/binary-quantization/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fbinary-quantization%2F&text=Binary%20Quantization%20-%20Andrey%20Vasnetsov%20%7c%20Vector%20Space%20Talks "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fbinary-quantization%2F "LinkedIn")

> _“Everything changed when we actually tried binary quantization with OpenAI model.”_
>
> – Andrey Vasnetsov

Ever wonder why we need quantization for vector indexes? Andrey Vasnetsov explains the complexities and challenges of searching through proximity graphs. Binary quantization reduces storage size and boosts speed by 30x, but not all models are compatible.

Andrey worked as a Machine Learning Engineer most of his career. He prefers practical over theoretical, working demo over arXiv paper. He is currently working as the CTO at Qdrant a Vector Similarity Search Engine, which can be used for semantic search, similarity matching of text, images or even videos, and also recommendations.

_**Listen to the episode on [Spotify](https://open.spotify.com/episode/7dPOm3x4rDBwSFkGZuwaMq?si=Ip77WCa_RCCYebeHX6DTMQ), Apple Podcast, Podcast addicts, Castbox. You can also watch this episode on [YouTube](https://youtu.be/4aUq5VnR_VI).**_

Binary Quantization - Andrey Vasnetsov \| Vector Space Talk #001 - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Binary Quantization - Andrey Vasnetsov \| Vector Space Talk #001](https://www.youtube.com/watch?v=4aUq5VnR_VI)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=4aUq5VnR_VI&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 20:44
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=4aUq5VnR_VI "Watch on YouTube")

Binary Quantization - Andrey Vasnetsov \| Vector Space Talk #001 by Vector Space Talks by Qdrant

![Currently playing episode](https://d2a9bkgsuxmqe2.cloudfront.net/staging/podcast_uploaded_episode400/39633897/39633897-1699901052140-d8e1972aaa36a.jpg)

## Binary Quantization …

Vector Space Talks by Qdrant[By Qdrant](https://creators.spotify.com/pod/show/qdrant-vector-space-talk/episodes/Binary-Quantization---Andrey-Vasnetsov--Vector-Space-Talk-001-e2bsa3m/a-aajrqfd)Nov 15, 2023

Share

00:00

20:43

## [Anchor](https://qdrant.tech/blog/binary-quantization/\#top-takeaways) Top Takeaways:

Discover how oversampling optimizes precision in real-time, enhancing the accuracy without altering stored data structures in our very first episode of the Vector Space Talks by Qdrant, with none other than the CTO of Qdrant, Andrey Vasnetsov.

In this episode, Andrey shares invaluable insights into the world of binary quantization and its profound impact on Vector Space technology.

5 Keys to Learning from the Episode:

1. The necessity of quantization and the complex challenges it helps to overcome.
2. The transformative effects of binary quantization on processing speed and storage size reduction.
3. A detailed exploration of oversampling and its real-time precision control in query search.
4. Understanding the simplicity and effectiveness of binary quantization, especially when compared to more intricate quantization methods.
5. The ongoing research and potential impact of binary quantization on future models.

> Fun Fact: Binary quantization can deliver processing speeds over 30 times faster than traditional quantization methods, which is a revolutionary advancement in Vector Space technology.

## [Anchor](https://qdrant.tech/blog/binary-quantization/\#show-notes) Show Notes:

00:00 Overview of HNSW vector index.

03:57 Efficient storage needed for large vector sizes.

07:49 Oversampling controls precision in real-time search.

12:21 Comparison of vectors using dot production.

15:20 Experimenting with models, OpenAI has compatibility.

18:29 Qdrant architecture doesn’t support removing original vectors.

## [Anchor](https://qdrant.tech/blog/binary-quantization/\#more-quotes-from-andrey) More Quotes from Andrey:

_“Inside Qdrant we use HNSW vector Index, which is essentially a proximity graph. You can imagine it as a number of vertices where each vertex is representing one vector and links between those vertices representing nearest neighbors.”_

– Andrey Vasnetsov

_“The main idea is that we convert the float point elements of the vector into binary representation. So, it’s either zero or one, depending if the original element is positive or negative.”_

– Andrey Vasnetsov

_“We tried most popular open source models, and unfortunately they are not as good compatible with binary quantization as OpenAI.”_

– Andrey Vasnetsov

## [Anchor](https://qdrant.tech/blog/binary-quantization/\#transcript) Transcript:

Demetrios:
Okay, welcome everyone. This is the first and inaugural vector space talks, and who better to kick it off than the CTO of Qdrant himself? Andrey V. Happy to introduce you and hear all about this binary quantization that you’re going to be talking about. I’ve got some questions for you, and I know there are some questions that came through in the chat. And the funny thing about this is that we recorded it live on Discord yesterday. But the thing about Discord is you cannot trust the recordings on there. And so we only got the audio and we wanted to make this more visual for those of you that are watching on YouTube. Hence here we are recording it again.

Demetrios:
And so I’ll lead us through some questions for you, Andrey. And I have one thing that I ask everyone who is listening to this, and that is if you want to give a talk and you want to showcase either how you’re using Qdrant, how you’ve built a rag, how you have different features or challenges that you’ve overcome with your AI, landscape or ecosystem or stack that you’ve set up, please reach out to myself and I will get you on here and we can showcase what you’ve done and you can give a talk for the vector space talk. So without further ado, let’s jump into this, Andrey, we’re talking about binary quantization, but let’s maybe start a step back. Why do we need any quantization at all? Why not just use original vectors?

Andrey Vasnetsov:
Yep. Hello, everyone. Hello Demetrios. And it’s a good question, and I think in order to answer it, I need to first give a short overview of what is vector index, how it works and what challenges it possess. So, inside Qdrant we use so called HNSW vector Index, which is essentially a proximity graph. You can imagine it as a number of vertices where each vertex is representing one vector and links between those vertices representing nearest neighbors. So in order to search through this graph, what you actually need to do is do a greedy deep depth first search, and you can tune the precision of your search with the beam size of the greedy search process. But this structure of the index actually has its own challenges and first of all, its index building complexity.

Andrey Vasnetsov:
Inserting one vector into the index is as complicated as searching for one vector in the graph. And the graph structure overall have also its own limitations. It requires a lot of random reads where you can go in any direction. It’s not easy to predict which path the graph will take. The search process will take in advance. So unlike traditional indexes in traditional databases, like binary trees, like inverted indexes, where we can pretty much serialize everything. In HNSW it’s always random reads and it’s actually always sequential reads, because you need to go from one vertex to another in a sequential manner. And this actually creates a very strict requirement for underlying storage of vectors.

Andrey Vasnetsov:
It had to have a very low latency and it have to support this randomly spatter. So basically we can only do it efficiently if we store all the vectors either in very fast solid state disks or if we use actual RAM to store everything. And RAM is not cheap these days, especially considering that the size of vectors increases with each new version of the model. And for example, OpenAI model is already more than 1000 dimensions. So you can imagine one vector is already 6 data, no matter how long your text is, and it’s just becoming more and more expensive with the advancements of new models and so on. So in order to actually fight this, in order to compensate for the growth of data requirement, what we propose to do, and what we already did with different other quantization techniques is we actually compress vectors into quantized vector storage, which is usually much more compact for the in memory representation. For example, on one of the previous releases we have scalar quantization and product quantization, which can compress up to 64 times the size of the vector. And we only keep in fast storage these compressed vectors.

Andrey Vasnetsov:
We retrieve them and get a list of candidates which will later rescore using the original vectors. And the benefit here is this reordering or rescoring process actually doesn’t require any kind of sequential or random access to data, because we already know all the IDs we need to rescore, and we can efficiently read it from the disk using asynchronous I O, for example, and even leverage the advantage of very cheap network mounted disks. And that’s the main benefit of quantization.

Demetrios:
I have a few questions off the back of this one, being just a quick thing, and I’m wondering if we can double benefit by using this binary quantization, but also if we’re using smaller models that aren’t the GBTs, will that help?

Andrey Vasnetsov:
Right. So not all models are as big as OpenAI, but what we see, the trend in this area, the trend of development of different models, indicates that they will become bigger and bigger over time. Just because we want to store more information inside vectors, we want to have larger context, we want to have more detailed information, more detailed separation and so on. This trend is obvious if like five years ago the usual size of the vector was 100 dimensions now the usual size is 700 dimensions, so it’s basically.

Demetrios:
Preparing for the future while also optimizing for today.

Andrey Vasnetsov:
Right?

Demetrios:
Yeah. Okay, so you mentioned on here oversampling. Can you go into that a little bit more and explain to me what that is?

Andrey Vasnetsov:
Yeah, so oversampling is a special technique we use to control precision of the search in real time, in query time. And the thing is, we can internally retrieve from quantized storage a bit more vectors than we actually need. And when we do rescoring with original vectors, we assign more precise score. And therefore from this overselection, we can pick only those vectors which are actually good for the user. And that’s how we can basically control accuracy without rebuilding index, without changing any kind of parameters inside the stored data structures. But we can do it real time in just one parameter change of the search query itself.

Demetrios:
I see, okay, so basically this is the quantization. And now let’s dive into the binary quantization and how it works.

Andrey Vasnetsov:
Right, so binary quantization is actually very simple. The main idea that we convert the float point elements of the vector into binary representation. So it’s either zero or one, depending if the original element is positive or negative. And by doing this we can approximate dot production or cosine similarity, whatever metric you use to compare vectors with just hemming distance, and hemming distance is turned to be very simple to compute. It uses only two most optimized CPU instructions ever. It’s Pixor and Popcount. Instead of complicated float point subprocessor, you only need those tool. It works with any register you have, and it’s very fast.

Andrey Vasnetsov:
It uses very few CPU cycles to actually produce a result. That’s why binary quantization is over 30 times faster than regular product. And it actually solves the problem of complicated index building, because this computation of dot products is the main source of computational requirements for HNSW.

Demetrios:
So if I’m understanding this correctly, it’s basically taking all of these numbers that are on the left, which can be, yes, decimal numbers.

Andrey Vasnetsov:
On the left you can see original vector and it converts it in binary representation. And of course it does lose a lot of precision in the process. But because first we have very large vector and second, we have oversampling feature, we can compensate for this loss of accuracy and still have benefit in both speed and the size of the storage.

Demetrios:
So if I’m understanding this correctly, it’s basically saying binary quantization on its own probably isn’t the best thing that you would want to do. But since you have these other features that will help counterbalance the loss in accuracy. You get the speed from the binary quantization and you get the accuracy from these other features.

Andrey Vasnetsov:
Right. So the speed boost is so overwhelming that it doesn’t really matter how much over sampling is going to be, we will still benefit from that.

Demetrios:
Yeah. And how much faster is it? You said that, what, over 30 times faster?

Andrey Vasnetsov:
Over 30 times and some benchmarks is about 40 times faster.

Demetrios:
Wow. Yeah, that’s huge. And so then on the bottom here you have dot product versus hammering distance. And then there’s. Yeah, hamming. Sorry, I’m inventing words over here on your slide. Can you explain what’s going on there?

Andrey Vasnetsov:
Right, so dot production is the metric we usually use in comparing a pair of vectors. It’s basically the same as cosine similarity, but this normalization on top. So internally, both cosine and dot production actually doing only dot production, that’s usual metric we use. And in order to do this operation, we first need to multiply each pair of elements to the same element of the other vector and then add all these multiplications in one number. It’s going to be our score instead of this in binary quantization, in binary vector, we do XOR operation and then count number of ones. So basically, Hemming distance is an approximation of dot production in this binary space.

Demetrios:
Excellent. Okay, so then it looks simple enough, right? Why are you implementing it now after much more complicated product quantization?

Andrey Vasnetsov:
It’s actually a great question. And the answer to this is binary questization looked too simple to be true, too good to be true. And we thought like this, we tried different things with open source models that didn’t work really well. But everything changed when we actually tried binary quantization with OpenAI model. And it turned out that OpenAI model has very good compatibility with this type of quantization. Unfortunately, not every model have as good compatibility as OpenAI. And to be honest, it’s not yet absolutely clear for us what makes models compatible and whatnot. We do know that it correlates with number of dimensions, but it is not the only factor.

Andrey Vasnetsov:
So there is some secret source which exists and we should find it, which should enable models to be compatible with binary quantization. And I think it’s actually a future of this space because the benefits of this hemming distance benefits of binary quantization is so great that it makes sense to incorporate these tricks on the learning process of the model to make them more compatible.

Demetrios:
Well, you mentioned that OpenAI’s model is one that obviously works well with binary quantization, but there are models that don’t work well with it, which models have not been very good.

Andrey Vasnetsov:
So right now we are in the process of experimenting with different models. We tried most popular open source models, and unfortunately they are not as good compatible with binary quantization as OpenAI. We also tried different closed source models, for example Cohere AI, which is on the same level of compatibility with binary quantization as OpenAI, but they actually have much larger dimensionality. So instead of 1500 they have 4000. And it’s not yet clear if only dimensionality makes this model compatible. Or there is something else in training process, but there are open source models which are getting close to OpenAI 1000 dimensions, but they are not nearly as good as Openi in terms of this compression compatibility.

Demetrios:
So let that be something that hopefully the community can help us figure out. Why is it that this works incredibly well with these closed source models, but not with the open source models? Maybe there is something that we’re missing there.

Andrey Vasnetsov:
Not all closed source models are compatible as well, so some of them work similar as open source, but a few works well.

Demetrios:
Interesting. Okay, so is there a plan to implement other quantization methods, like four bit quantization or even compressing two floats into one bit?

Andrey Vasnetsov:
Right, so our choice of quantization is mostly defined by available CPU instructions we can apply to perform those computations. In case of binary quantization, it’s straightforward and very simple. That’s why we like binary quantization so much. In case of, for example, four bit quantization, it is not as clear which operation we should use. It’s not yet clear. Would it be efficient to convert into four bits and then apply multiplication of four bits? So this would require additional investigation, and I cannot say that we have immediate plans to do so because still the binary quincellation field is not yet explored on 100% and we think it’s a lot more potential with this than currently unlocked.

Demetrios:
Yeah, there’s some low hanging fruits still on the binary quantization field, so tackle those first and then move your way over to four bit and all that fun stuff. Last question that I’ve got for you is can we remove original vectors and only keep quantized ones in order to save disk space?

Andrey Vasnetsov:
Right? So unfortunately Qdrant architecture is not designed and not expecting this type of behavior for several reasons. First of all, removing of the original vectors will compromise some features like oversampling, like segment building. And actually removing of those original vectors will only be compatible with some types of quantization for example, it won’t be compatible with scalar quantization because in this case we won’t be able to rebuild index to do maintenance of the system. And in order to maintain, how would you say, consistency of the API, consistency of the engine, we decided to enforce always enforced storing of the original vectors. But the good news is that you can always keep original vectors on just disk storage. It’s very cheap. Usually it’s ten times or even more times cheaper than RAM, and it already gives you great advantage in terms of price. That’s answer excellent.

Demetrios:
Well man, I think that’s about it from this end, and it feels like it’s a perfect spot to end it. As I mentioned before, if anyone wants to come and present at our vector space talks, we’re going to be doing these, hopefully biweekly, maybe weekly, if we can find enough people. And so this is an open invitation for you, and if you come present, I promise I will send you some swag. That is my promise to you. And if you’re listening after the fact and you have any questions, come into discord on the Qdrant. Discord. And ask myself or Andrey any of the questions that you may have as you’re listening to this talk about binary quantization. We will catch you all later.

Demetrios:
See ya, have a great day. Take care.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=36ba1495-86bb-469c-b853-1edfd73463e6)

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

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fbinary-quantization%2F&portalId=139603372&pageTitle=Binary+Quantization+-+Andrey+Vasnetsov+%7C+Vector+Space+Talks+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=2abd0a281e537d85a2dbf0d2e0304c47&hssc=265983056.1.1748574168889&hstc=265983056.2abd0a281e537d85a2dbf0d2e0304c47.1748574168889.1748574168889.1748574168889.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fbinary-quantization%2F&pageTitle=Binary+Quantization+-+Andrey+Vasnetsov+%7C+Vector+Space+Talks+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=2abd0a281e537d85a2dbf0d2e0304c47&hssc=265983056.1.1748574168889&hstc=265983056.2abd0a281e537d85a2dbf0d2e0304c47.1748574168889.1748574168889.1748574168889.1&hsfp=3707738794).

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=3f784e8a-fc96-4015-ab81-c856fba720c0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c5d99a13-ab9e-4a45-81b0-26d4afc77a16&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fbinary-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=3f784e8a-fc96-4015-ab81-c856fba720c0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c5d99a13-ab9e-4a45-81b0-26d4afc77a16&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fbinary-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)