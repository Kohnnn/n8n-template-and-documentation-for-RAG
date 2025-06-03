---
url: "https://qdrant.tech/blog/vector-image-search-rag/"
title: "Vector Search Complexities: Insights from Projects in Image Search and RAG - Noé Achache | Vector Space Talks - Qdrant"
---

0

# Vector Search Complexities: Insights from Projects in Image Search and RAG - Noé Achache \| Vector Space Talks

Demetrios Brinkmann

·

January 09, 2024

![Vector Search Complexities: Insights from Projects in Image Search and RAG - Noé Achache | Vector Space Talks](https://qdrant.tech/blog/vector-image-search-rag/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fvector-image-search-rag%2F&text=Vector%20Search%20Complexities:%20Insights%20from%20Projects%20in%20Image%20Search%20and%20RAG%20-%20No%c3%a9%20Achache%20%7c%20Vector%20Space%20Talks "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fvector-image-search-rag%2F "LinkedIn")

> _“I really think it’s something the technology is ready for and would really help this kind of embedding model jumping onto the text search projects.”_
>
> – Noé Achache on the future of image embedding

Exploring the depths of vector search? Want an analysis of its application in image search and document retrieval? Noé got you covered.

Noé Achache is a Lead Data Scientist at Sicara, where he worked on a wide range of projects mostly related to computer vision, prediction with structured data, and more recently LLMs.

_**Listen to the episode on [Spotify](https://open.spotify.com/episode/2YgcSFjP7mKE0YpDGmSiq5?si=6BhlAMveSty4Yt7umPeHjA), Apple Podcast, Podcast addicts, Castbox. You can also watch this episode on [YouTube](https://youtu.be/1vKoiFAdorE).**_

Insights from Diverse Projects in Image Search and RAG - Noé Achache \| Vector Space Talk #008 - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Insights from Diverse Projects in Image Search and RAG - Noé Achache \| Vector Space Talk #008](https://www.youtube.com/watch?v=1vKoiFAdorE)

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

[Watch on](https://www.youtube.com/watch?v=1vKoiFAdorE&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 40:18
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=1vKoiFAdorE "Watch on YouTube")

Navigating the Complexities of Vector Search: Practical Insights from Diverse Projects in Image Search and RAG - Noé Achache \| Vector Space Talk #008 by Vector Space Talks by Qdrant

![Currently playing episode](https://d2a9bkgsuxmqe2.cloudfront.net/staging/podcast_uploaded_episode400/39633897/39633897-1703250860712-f8da745f7c244.jpg)

## Navigating th…

Vector Space Talks by Qdrant[By Qdrant](https://creators.spotify.com/pod/show/qdrant-vector-space-talk/episodes/Navigating-the-Complexities-of-Vector-Search-Practical-Insights-from-Diverse-Projects-in-Image-Search-and-RAG---No-Achache--Vector-Space-Talk-008-e2diivl/a-aap4q5d)Dec 22, 2023

Share

00:00

40:18

## [Anchor](https://qdrant.tech/blog/vector-image-search-rag/\#top-takeaways)**Top Takeaways:**

Discover the efficacy of Dino V2 in image representation and the complexities of deploying vector databases, while navigating the challenges of fine-tuning and data safety in sensitive fields.

In this episode, Noe, shares insights on vector search from image search to retrieval augmented generation, emphasizing practical application in complex projects.

5 key insights you’ll learn:

1. Cutting-edge Image Search: Learn about the advanced model Dino V2 and its efficacy in image representation, surpassing traditional feature transform methods.
2. Data Deduplication Strategies: Gain knowledge on the sophisticated process of deduplicating real estate listings, a vital task in managing extensive data collections.
3. Document Retrieval Techniques: Understand the challenges and solutions in retrieval augmented generation for document searches, including the use of multi-language embedding models.
4. Protection of Sensitive Medical Data: Delve into strategies for handling confidential medical information and the importance of data safety in health-related applications.
5. The Path Forward in Model Development: Hear Noe discuss the pressing need for new types of models to address the evolving needs within the industry.

> Fun Fact: The best-performing model Noé mentions for image representation in his image search project is Dino V2, which interestingly didn’t require fine-tuning to understand objects and patterns.

## [Anchor](https://qdrant.tech/blog/vector-image-search-rag/\#show-notes) Show Notes:

00:00 Relevant experience in vector DB projects and talks.

05:57 Match image features, not resilient to changes.

07:06 Compute crop vectors, and train to converge.

11:37 Simple training task, improve with hard examples.

15:25 Improving text embeddings using hard examples.

22:29 Future of image embedding for document search.

27:28 Efficient storage and retrieval process feature.

29:01 Models handle varied data; sparse vectors now possible.

35:59 Use memory, avoid disk for CI integration.

37:43 Challenging metadata filtering for vector databases and new models

## [Anchor](https://qdrant.tech/blog/vector-image-search-rag/\#more-quotes-from-no%C3%A9) More Quotes from Noé:

_“So basically what was great is that Dino manages to understand all objects and close patterns without fine tuning. So you can get an off the shelf model and get started very quickly and start bringing value very quickly without having to go through all the fine tuning processes.”_

– Noé Achache

_“And at the end, the embeddings was not learning any very complex features, so it was not really improving it.”_

– Noé Achache

_“When using an API model, it’s much faster to use it in asynchronous mode like the embedding equation went something like ten times or 100 times faster. So it was definitely, it changed a lot of things.”_

– Noé Achache

## [Anchor](https://qdrant.tech/blog/vector-image-search-rag/\#transcript) Transcript:

Demetrios:
Noe. Great to have you here everyone. We are back for another vector space talks and today we are joined by my man Noe, who is the lead data scientist at Sicara, and if you do not know, he is working on a wide range of projects, mostly related to computer vision. Vision. And today we are talking about navigating the complexities of vector search. We’re going to get some practical insights from diverse projects in image search and everyone’s favorite topic these days, retrieval augmented generation, aka rags. So noe, I think you got something for us. You got something planned for us here?

Noe Acache:
Yeah, I do. I can share them.

Demetrios:
All right, well, I’m very happy to have you on here, man. I appreciate you doing this. And let’s get you sharing your screen so we can start rocking, rolling.

Noe Acache:
Okay. Can you see my screen?

Demetrios:
Yeah. Awesome.

Noe Acache:
Great. Thank you, Demetrius, for the great introduction. I just completed quickly. So as you may have guessed, I’m french. I’m a lead data scientist at Sicara. So Secura is a service company helping its clients in data engineering and data science, so building projects for them. Before being there, I worked at realtics on optical character recognition, and I’m now working mostly on, as you said, computer vision and also Gen AI. So I’m leading the geni side and I’ve been there for more than three years.

Noe Acache:
So some relevant experience on vector DB is why I’m here today, because I did four projects, four vector soft projects, and I also wrote an article on how to choose your database in 2023, your vector database. And I did some related talks in other conferences like Pydata, DVC, all the geni meetups of London and Paris. So what are we going to talk about today? First, an overview of the vector search projects. Just to give you an idea of the kind of projects we can do with vector search. Then we will dive into the specificities of the image search project and then into the specificities of the text search project. So here are the four projects. So two in image search, two in text search. The first one is about matching objects in videos to sell them afterwards.

Noe Acache:
So basically you have a video. We first detect the object. So like it can be a lamp, it can be a piece of clothes, anything, we classify it and then we compare it to a large selection of similar objects to retrieve the most similar one to a large collection of sellable objects. The second one is about deduplicating real estate adverts. So when agencies want to sell a property, like sometimes you have several agencies coming to take pictures of the same good. So you have different pictures of the same good. And the idea of this project was to match the different pictures of the same good, the same profile.

Demetrios:
I’ve seen that dude. I have been a victim of that. When I did a little house shopping back like five years ago, it would be the same house in many different ones, and sometimes you wouldn’t know because it was different photos. So I love that you were thinking about it that way. Sorry to interrupt.

Noe Acache:
Yeah, so to be fair, it was the idea of my client. So basically I talk about it a bit later with aggregating all the adverts and trying to deduplicate them. And then the last two projects are about drugs retrieval, augmented generation. So the idea to be able to ask questions to your documentation. The first one was for my company’s documentation and the second one was for a medical company. So different kind of complexities. So now we know all about this project, let’s dive into them. So regarding the image search project, to compute representations of the images, the best performing model from the benchmark, and also from my experience, is currently Dino V two.

Noe Acache:
So a model developed by meta that you may have seen, which is using visual transformer. And what’s amazing about it is that using the attention map, you can actually segment what’s important in the picture, although you haven’t told it specifically what’s important. And as a human, it will learn to focus on the dog, on this picture and do not take into consideration the noisy background. So when I say best performing model, I’m talking about comparing to other architecture like Resnet efficient nets models, an approach I haven’t tried, which also seems interesting. If anyone tried it for similar project, please reach out afterwards. I’ll be happy to talk about it. Is sift for feature transform something about feature transform. It’s basically a more traditional method without learned features through machine learning, as in you don’t train the model, but it’s more traditional methods.

Noe Acache:
And you basically detect the different features in an image and then try to find the same features in an image which is supposed to post to be the same. All the blue line trying to match the different features. Of course it’s made to match image with exactly the same content, so it wouldn’t really work. Probably not work in the first use case, because we are trying to match similar clothes, but which are not exactly the same one. And also it’s known to be not very resilient with the changes of angles when it changes too much, et cetera. So it may not be very good as well for the second use case, but again, I haven’t tried it, so just leaving it here on the side. Just a quick word about how Dino works in case you’re interested. So it’s a vision transformer and it’s trade in an unsupervised way, as in you don’t have any labels provided, so you just take pictures and you first extract small crops and large crops and you augment them.

Noe Acache:
And then you’re going to use the model to compute vectors, representations of each of these crops. And since they all represent the same image, they should all be the same. So then you can compute a loss to see how they diverge and to basically train them to become the same. So this is how it works and how it works. And the difference between the second version is just that they use more data sets and the distillation method to have a very performant model, which is also very fast to run regarding the first use case. So, matching objects in videos to sellable items for people who use Google lengths before, it’s quite similar, where in Google lens you can take a picture of something and then it will try to find similar objects to buy. So again, you have a video and then you detect one of the objects in the video, put it and compare it to a vector database which contains a lot of objects which are similar for the representation. And then it will output the most similar lamp here.

Noe Acache:
Now we’re going to try to analyze how this project went regarding the positive outcomes and the changes we faced. So basically what was great is that Dino manages to understand all objects and close patterns without fine tuning. So you can get an off the shelf model and get started very quickly and start bringing value very quickly without having to go through all the fine tuning processes. And it also manages to focus on the object without segmentation. What I mean here is that we’re going to get a box of the object, and in this box there will be a very noisy background which may disturb the matching process. And since Dino really manages to focus on the object, that’s important on the image. It doesn’t really matter that we don’t segmentate perfectly the image. Regarding the vector database, this project started a while ago, and I think we chose the vector database something like a year and a half ago.

Noe Acache:
And so it was before all the vector database hype. And at the time, the most famous one was Milvos, the only famous one actually. And we went for an on premise development deployment. And actually our main learning is that the DevOps team really struggled to deploy it, because basically it’s made of a lot of pods. And the documentations about how these pods are supposed to interact together is not really perfect. And it was really buggy at this time. So the clients lost a lot of time and money in this deployment. The challenges, other challenges we faced is that we noticed that the matching wasn’t very resilient to large distortions.

Noe Acache:
So for furnitures like lamps, it’s fine. But let’s say you have a trouser and a person walking. So the trouser won’t exactly have the same shape. And since you haven’t trained your model to specifically know, it shouldn’t focus on the movements. It will encode this movement. And then in the matching, instead of matching trouser, which looks similar, it will just match trouser where in the product picture the person will be working as well, which is not really what we want. And the other challenges we faced is that we tried to fine tune the model, but our first fine tuning wasn’t very good because we tried to take an open source model and, and get the labels it had, like on different furnitures, clothes, et cetera, to basically train a model to classify the different classes and then remove the classification layer to just keep the embedding parts. The thing is that the labels were not specific enough.

Noe Acache:
So the training task was quite simple. And at the end, the embeddings was not learning any very complex features, so it was not really improving it. So jumping onto the areas of improvement, knowing all of that, the first thing I would do if I had to do it again will be to use the managed milboss for a better fine tuning, it would be to labyd hard examples, hard pairs. So, for instance, you know that when you have a matching pair where the similarity score is not too high or not too low, you know, it’s where the model kind of struggles and you will find some good matching and also some mistakes. So it’s where it kind of is interesting to level to then be able to fine tune your model and make it learn more complex things according to your tasks. Another possibility for fine tuning will be some sort of multilabel classification. So for instance, if you consider tab close, you could say, all right, those disclose contain buttons. It have a color, it have stripes.

Noe Acache:
And for all of these categories, you’ll get a score between zero and one. And concatenating all these scores together, you can get an embedding which you can put in a vector database for your vector search. It’s kind of hard to scale because you need to do a specific model and labeling for each type of object. And I really wonder how Google lens does because their algorithm work very well. So are they working more like with this kind of functioning or this kind of functioning? So if anyone had any thought on that or any idea, again, I’d be happy to talk about it afterwards. And finally, I feel like we made a lot of advancements in multimodal training, trying to combine text inputs with image. We’ve made input to build some kind of complex embeddings. And how great would it be to have an image embeding you could guide with text.

Noe Acache:
So you could just like when creating an embedding of your image, just say, all right, here, I don’t care about the movements, I only care about the features on the object, for instance. And then it will learn an embedding according to your task without any fine tuning. I really feel like with the current state of the arts we are able to do this. I mean, we need to do it, but the technology is ready.

Demetrios:
Can I ask a few questions before you jump into the second use case?

Noe Acache:
Yes.

Demetrios:
What other models were you looking at besides the dyno one?

Noe Acache:
I said here, compared to Resnet, efficient nets and these kind of architectures.

Demetrios:
Maybe this was too early, or maybe it’s not actually valuable. Was that like segment anything? Did that come into the play?

Noe Acache:
So segment anything? I don’t think they redo embeddings. It’s really about segmentation. So here I was just showing the segmentation part because it’s a cool outcome of the model and it shows that the model works well here we are really here to build a representation of the image we cannot really play with segment anything for the matching, to my knowledge, at least.

Demetrios:
And then on the next slide where you talked about things you would do differently, or the last slide, I guess the areas of improvement you mentioned label hard examples for fine tuning. And I feel like, yeah, there’s one way of doing it, which is you hand picking the different embeddings that you think are going to be hard. And then there’s another one where I think there’s tools out there now that can kind of show you where there are different embeddings that aren’t doing so well or that are more edge cases.

Noe Acache:
Which tools are you talking about?

Demetrios:
I don’t remember the names, but I definitely have seen demos online about how it’ll give you a 3d space and you can kind of explore the different embeddings and explore what’s going on I.

Noe Acache:
Know exactly what you’re talking about. So tensorboard embeddings is a good tool for that. I could actually demo it afterwards.

Demetrios:
Yeah, I don’t want to get you off track. That’s something that came to mind if.

Noe Acache:
You’Re talking about the same tool. Turns out embedding. So basically you have an embedding of like 1000 dimensions and it just reduces it to free dimensions. And so you can visualize it in a 3d space and you can see how close your embeddings are from each other.

Demetrios:
Yeah, exactly.

Noe Acache:
But it’s really for visualization purposes, not really for training purposes.

Demetrios:
Yeah, okay, I see.

Noe Acache:
Talking about the same thing.

Demetrios:
Yeah, I think that sounds like what I’m talking about. So good to know on both of these. And you’re shooting me straight on it. Mike is asking a question in here, like text embedding, would that allow you to include an image with alternate text?

Noe Acache:
An image with alternate text? I’m not sure the question.

Demetrios:
So it sounds like a way to meet regulatory accessibility requirements if you have. I think it was probably around where you were talking about the multimodal and text to guide the embeddings and potentially would having that allow you to include an image with alternate text?

Noe Acache:
The idea is not to. I feel like the question is about inserting text within the image. It’s what I understand. My idea was just if you could create an embedding that could combine a text inputs and the image inputs, and basically it would be trained in such a way that the text would basically be used as a guidance of the image to only encode the parts of the image which are required for your task to not be disturbed by the noisy.

Demetrios:
Okay. Yeah. All right, Mike, let us know if that answers the question or if you have more. Yes. He’s saying, yeah, inserting text with image for people who can’t see.

Noe Acache:
Okay, cool.

Demetrios:
Yeah, right on. So I’ll let you keep cruising and I’ll try not to derail it again. But that was great. It was just so pertinent. I wanted to stop you and ask some questions.

Noe Acache:
Larry, let’s just move in. So second use case is about deduplicating real estate adverts. So as I was saying, you have two agencies coming to take different pictures of the same property. And the thing is that they may not put exactly the same price or the same surface or the same location. So you cannot just match them with metadata. So what our client was doing beforehand, and he kind of built a huge if machine, which is like, all right, if the location is not too far and if the surface is not too far. And the price, and it was just like very complex rules. And at the end there were a lot of edge cases.

Noe Acache:
It was very hard to maintain. So it was like, let’s just do a simpler solution just based on images. So it was basically the task to match images of the same properties. Again on the positive outcomes is that the dino really managed to understand the patterns of the properties without any fine tuning. And it was resilient to read different angles of the same room. So like on the pictures I shown, I just showed, the model was quite good at identifying. It was from the same property. Here we used cudrant for this project was a bit more recent.

Noe Acache:
We leveraged a lot the metadata filtering because of course we can still use the metadata even it’s not perfect just to say, all right, only search vectors, which are a price which is more or less 10% this price. The surface is more or less 10% the surface, et cetera, et cetera. And indexing of this metadata. Otherwise the search is really slowed down. So we had 15 million vectors and without this indexing, the search could take up to 20, 30 seconds. And with indexing it was like in a split second. So it was a killer feature for us. And we use quantization as well to save costs because the task was not too hard.

Noe Acache:
Since using the metadata we managed to every time reduce the task down to a search of 1000 vector. So it wasn’t too annoying to quantize the vectors. And at the end for 15 million vectors, it was only $275 per month, which with the village version, which is very decent. The challenges we faced was really about bathrooms and empty rooms because all bathrooms kind of look similar. They have very similar features and same for empty rooms since there is kind of nothing in them, just windows. The model would often put high similarity scores between two bathroom of different properties and same for the empty rooms. So again, the method to overcome this thing will be to label harpers. So example were like two images where the model would think they are similar to actually tell the model no, they are not similar to allow it to improve its performance.

Noe Acache:
And again, same thing on the future of image embedding. I really think it’s something the technology is ready for and would really help this kind of embedding model jumping onto the text search projects. So the principle of retribution generation for those of you who are not familiar with it is just you take some documents, you have an embedding model here, an embedding model trained on text and not on images, which will output representations from these documents, put it in a vector database, and then when a user will ask a question over the documentation, it will create an embedding of the request and retrieve the most similar documents. And afterwards we usually pass it to an LLM, which will generate an answer. But here in this talk, we won’t focus on the overall product, but really on the vector search part. So the two projects was one, as I told you, a rack for my nutrition company, so endosion with around a few hundred thousand of pages, and the second one was for medical companies, so for the doctors. So it was really about the documentation search rather than the LLM, because you cannot output any mistake. The model we used was OpenAI Ada two.

Noe Acache:
Why? Mostly because for the first use case it’s multilingual and it was off the shelf, very easy to use, so we did not spend a lot of time on this project. So using an API model made it just much faster. Also it was multilingual, approved by the community, et cetera. For the second use case, we’re still working on it. So since we use GPT four afterwards, because it’s currently the best LLM, it was also easier to use adatu to start with, but we may use a better one afterwards because as I’m saying, it’s not the best one if you refer to the MTAB. So the massive text embedding benchmark made by hugging face, which basically gathers a lot of embeddings benchmark such as retrieval for instance, and so classified the different model for these benchmarks. The M tab is not perfect because it’s not taking into account cross language capabilities. All the benchmarks are just for one language and it’s not as well taking into account most of the languages, like it’s only considering English, Polish and Chinese.

Noe Acache:
And also it’s probably biased for models trained on close source data sets. So like most of the best performing models are currently closed source APIs and hence closed source data sets, and so we don’t know how they’ve been trained. So they probably trained themselves on these data sets. At least if I were them, it’s what I would do. So I assume they did it to gain some points in these data sets.

Demetrios:
So both of these rags are mainly with documents that are in French?

Noe Acache:
Yes. So this one is French and English, and this one is French only.

Demetrios:
Okay. Yeah, that’s why the multilingual is super important for these use cases.

Noe Acache:
Exactly. Again, for this one there are models for French working much better than other two, so we may change it afterwards, but right now the performance we have is decent. Since both projects are very similar, I’ll jump into the conclusion for both of them together. So Ada two is good for understanding diverse context, wide range of documentation, medical contents, technical content, et cetera, without any fine tuning. The cross language works quite well, so we can ask questions in English and retrieve documents in French and the other way around. And also, quick note, because I did not do it from the start, is that when using an API model, it’s much faster to use it in asynchronous mode like the embedding equation went something like ten times or 100 times faster. So it was definitely, it changed a lot of things. Again, here we use cudrant mostly to leverage the free tier so they have a free version.

Noe Acache:
So you can pop it in a second, get the free version, and using the feature which allows to put the vectors on disk instead of storing them on ram, which makes it a bit slower, you can easily support few hundred thousand of vectors and with a very decent response time. The challenge we faced is that mostly for the notion, so like mostly in notion, we have a lot of pages which are just a title because they are empty, et cetera. And so when pages have just a title, the content is so small that it will be very similar actually to a question. So often the documents were retrieved were document with very little content, which was a bit frustrating. Chunking appropriately was also tough. Basically, if you want your retrieval process to work well, you have to divide your documents the right way to create the embeddings. So you can use matrix rules, but basically you need to divide your documents in content which semantically makes sense and it’s not always trivial. And also for the rag, for the medical company, sometimes we are asking questions about a specific drug and it’s just not under our search is just not retrieving the good documents, which is very frustrating because a basic search would.

Noe Acache:
So to handle these changes, a good option would be to use models handing differently question and documents like Bg or cohere. Basically they use the same model but trained differently on long documents and questions which allow them to map them differently in the space. And my guess is that using such model documents, which are only a title, et cetera, will not be as close as the question as they are right now because they will be considered differently. So I hope it will help this problem. Again, it’s just a guess, maybe I’m wrong. Heap research so for the keyword problem I was mentioning here, so in the recent release, Cudran just enabled sparse vectors which make actually TFEdev vectors possible. The TFEDEF vectors are vectors which are based on keywords, but basically there is one number per possible word in the data sets, and a lot of zeros, so storing them as a normal vector will make the vector search very expensive. But as a sparse vector it’s much better.

Noe Acache:
And so you can build a debrief search combining the TFDF search for keyword search and the other search for semantic search to get the best of both worlds and overcome this issue. And finally, I’m actually quite surprised that with all the work that is going on, generative AI and rag, nobody has started working on a model to help with chunking. It’s like one of the biggest challenge, and I feel like it’s quite doable to have a model which will our model, or some kind of algorithm which will understand the structure of your documentation and understand why it semantically makes sense to chunk your documents. Dude, so good.

Demetrios:
I got questions coming up. Don’t go anywhere. Actually, it’s not just me. Tom’s also got some questions, so I’m going to just blame it on Tom, throw him under the bus. Rag with medical company seems like a dangerous use case. You can work to eliminate hallucinations and other security safety concerns, but you can’t make sure that they’re completely eliminated, right? You can only kind of make sure they’re eliminated. And so how did you go about handling these concerns?

Noe Acache:
This is a very good question. This is why I mentioned this project is mostly about the document search. Basically what we do is that we use chainlit, which is a very good tool for chatting, and then you can put a react front in front of it to make it very custom. And so when the user asks a question, we provide the LLM answer more like as a second thought, like something the doctor could consider as a fagon thought. But what’s the most important is that we directly put the, instead of just citing the sources, we put the HTML of the pages the source is based on, and what bring the most value is really these HTML pages. And so we know the answer may have some problems. The fact is, based on documents, hallucinations are almost eliminated. Like, we don’t notice any hallucinations, but of course they can happen.

Noe Acache:
So it’s really the way, it’s really a product problem rather than an algorithm problem, an algorithmic problem, yeah. The documents retrieved rather than the LLM answer.

Demetrios:
Yeah, makes sense. My question around it is a lot of times in the medical space, the data that is being thrown around is super sensitive. Right. And you have a lot of Pii. How do you navigate that? Are you just not touching that?

Noe Acache:
So basically we work with a provider in front which has public documentation. So it’s public documentation. There is no PII.

Demetrios:
Okay, cool. So it’s not like some of it.

Noe Acache:
Is private, but still there is no PII in the documents.

Demetrios:
Yeah, because I think that’s another really incredibly hard problem is like, oh yeah, we’re just sending all this sensitive information over to the IDA model to create embeddings with it. And then we also pass it through Chat GPT before we get it back. And next thing you know, that is the data that was used to train GPT five. And you can say things like create an unlimited poem and get that out of it. So it’s super sketchy, right?

Noe Acache:
Yeah, of course, one way to overcome that is to, for instance, for the notion project, it’s our private documentation. We use Ada over Azure, which guarantees data safety. So it’s quite a good workaround. And when you have to work with different level of security, if you deal with PII, a good way is to play with metadata. Depending on the security level of the person who has the question, you play with the metadata to output only some kind of documents. The database metadata.

Demetrios:
Excellent. Well, don’t let me stop you. I know you had some conclusionary thoughts there.

Noe Acache:
No, sorry, I was about to conclude anyway. So just to wrap it up, so we got some good models without any fine tuning. With the model, we tried to overcome them, to overcome these limitations we still faced. For MS search, fine tuning is required at the moment. There’s no really any other way to overcome it otherwise. While for tech search, fine tuning is not really necessary, it’s more like tricks which are required about using eBrid search, using better models, et cetera. So two kind of approaches, Qdrant really made a lot of things easy. For instance, I love the feature where you can use the database as a disk file.

Noe Acache:
You can even also use it in memory for CI integration and stuff. But since for all my experimentations, et cetera, I won’t use it as a disk file because it’s much easier to play with. I just like this feature. And then it allows to use the same tool for your experiment and in production. When I was playing with milverse, I had to use different tools for experimentation and for the database in production, which was making the technical stock a bit more complex. Sparse vector for Tfedef, as I was mentioning, which allows to search based on keywords to make your retrieval much better. Manage deployment again, we really struggle with the deployment of the, I mean, the DevOps team really struggled with the deployment of the milverse. And I feel like in most cases, except if you have some security requirements, it will be much cheaper to use the managed deployments rather than paying dev costs.

Noe Acache:
And also with the free cloud and on these vectors, you can really do a lot of, at least start a lot of projects. And finally, the metadata filtering and indexing. So by the way, we went into a small trap. It’s that indexing. It’s recommended to index on your metadata before adding your vectors. Otherwise your performance may be impacted. So you may not retrieve the good vectors that you need. So it’s interesting thing to take into consideration.

Noe Acache:
I know that metadata filtering is something quite hard to do for vector database, so I don’t really know how it works, but I assume there is a good reason for that. And finally, as I was mentioning before, in my view, new types of models are needed to answer industrial needs. So the model we are talking about, tech guidance to make better image embeddings and automatic chunking, like some kind of algorithm and model which will automatically chunk your documents appropriately. So thank you very much. If you still have questions, I’m happy to answer them. Here are my social media. If you want to reach me out afterwards, twitch out afterwards, and all my writing and talks are gathered here if you’re interested.

Demetrios:
Oh, I like how you did that. There is one question from Tom again, asking about if you did anything to handle images and tables within the documentation when you were doing those rags.

Noe Acache:
No, I did not do anything for the images and for the tables. It depends when they are well structured. I kept them because the model manages to understand them. But for instance, we did a small pock for the medical company when he tried to integrate some external data source, which was a PDF, and we wanted to use it as an HTML to be able to display the HTML otherwise explained to you directly in the answer. So we converted the PDF to HTML and in this conversion, the tables were absolutely unreadable. So even after cleaning. So we did not include them in this case.

Demetrios:
Great. Well, dude, thank you so much for coming on here. And thank you all for joining us for yet another vector space talk. If you would like to come on to the vector space talk and share what you’ve been up to and drop some knowledge bombs on the rest of us, we’d love to have you. So please reach out to me. And I think that is it for today. Noe, this was awesome, man. I really appreciate you doing this.

Noe Acache:
Thank you, Demetrius. Have a nice day.

Demetrios:
We’ll see you all later. Bye.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=69aec995-cb48-4fdc-96fb-d7856974011d)

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

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fvector-image-search-rag%2F&portalId=139603372&pageTitle=Vector+Search+Complexities%3A+Insights+from+Projects+in+Image+Search+and+RAG+-+No%C3%A9+Achache+%7C+Vector+Space+Talks+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=cb2073d5283ec7381a3d98433fb2db26&hssc=265983056.1.1748574589843&hstc=265983056.cb2073d5283ec7381a3d98433fb2db26.1748574589843.1748574589843.1748574589843.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fvector-image-search-rag%2F&pageTitle=Vector+Search+Complexities%3A+Insights+from+Projects+in+Image+Search+and+RAG+-+No%C3%A9+Achache+%7C+Vector+Space+Talks+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=cb2073d5283ec7381a3d98433fb2db26&hssc=265983056.1.1748574589843&hstc=265983056.cb2073d5283ec7381a3d98433fb2db26.1748574589843.1748574589843.1748574589843.1&hsfp=3707738794).

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b7ae7a4c-282e-418a-82f5-ea498c93875a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=931eb709-04a9-4eba-87d9-65ff8f5af44e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fvector-image-search-rag%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b7ae7a4c-282e-418a-82f5-ea498c93875a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=931eb709-04a9-4eba-87d9-65ff8f5af44e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fvector-image-search-rag%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)