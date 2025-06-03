---
url: "https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/"
title: "Automating Business Processes with Qdrant and n8n: Use Cases Beyond Simple Similarity Search - Qdrant"
---

0

# Automating Business Processes with Qdrant and n8n: Use Cases Beyond Simple Similarity Search

Evgeniya Sukhodolskaya

·

April 04, 2025

![Automating Business Processes with Qdrant and n8n: Use Cases Beyond Simple Similarity Search](https://qdrant.tech/blog/qdrant-n8n-2/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n-beyond-simple-similarity-search%2F&text=Automating%20Business%20Processes%20with%20Qdrant%20and%20n8n:%20Use%20Cases%20Beyond%20Simple%20Similarity%20Search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n-beyond-simple-similarity-search%2F "LinkedIn")

Low-code automation tools make it easy to turn ideas into reality quickly. As AI becomes central to modern business, having low-code platforms with built-in AI capabilities is no longer optional—it’s essential. [n8n](https://n8n.io/) is a great example, combining powerful AI integrations with flexible automation.

Vector search has become a key building block in modern AI systems. While it’s often used as memory or a knowledge base for generative AI, its potential goes much further.

In this blog, we explore combining a dedicated vector search engine like Qdrant with an AI automation platform like n8n, moving beyond basic Retrieval-Augmented Generation (RAG) use cases. We’ll show you how to use vector search for recommendations and big data analysis using ready-to-use n8n workflows.

## [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#setting-up-qdrant-in-n8n) Setting Up Qdrant in n8n

To start using Qdrant with n8n, you need to provide your Qdrant instance credentials in the [credentials](https://docs.n8n.io/integrations/builtin/credentials/qdrant/#using-api-key) tab. Select `QdrantApi` from the list.

### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#qdrant-cloud) Qdrant Cloud

To connect [Qdrant Cloud](https://qdrant.tech/documentation/cloud/) to n8n:

1. Open the [Cloud Dashboard](https://qdrant.to/cloud) and select a cluster.
2. From the **Cluster Details**, copy the `Endpoint` address—this will be used as the `Qdrant URL` in n8n.
3. Navigate to the **API Keys** tab and copy your API key—this will be the `API Key` in n8n.

For a walkthrough, see this [step-by-step video guide](https://youtu.be/fYMGpXyAsfQ?feature=shared&t=177).

### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#local-mode) Local Mode

For a fully local setup, a valuable option is n8n’s [Self-hosted AI Starter Kit](https://github.com/n8n-io/self-hosted-ai-starter-kit). This is an open-source Docker Compose template for local AI & low-code development environment.

This kit includes a [local instance of Qdrant](https://qdrant.tech/documentation/quickstart/). To get started:

1. Follow the instructions in the repository to install the AI Starter Kit.
2. Use the values from the `docker-compose.yml` file to fill in the connection details.

The default Qdrant configuration in AI Starter Kit’s `docker-compose.yml` looks like this:

```yaml
qdrant:
  image: qdrant/qdrant
  hostname: qdrant
  container_name: qdrant
  networks: ['demo']
  restart: unless-stopped
  ports:
    - 6333:6333
  volumes:
    - qdrant_storage:/qdrant/storage

```

From this configuration, the `Qdrant URL` in n8n Qdrant credentials is `http://qdrant:6333/`.
To set up a local Qdrant API key, add the following lines to the YAML file:

```yaml
qdrant:
  ...
  volumes:
    - qdrant_storage:/qdrant/storage
  environment:
    - QDRANT_API_KEY=test

```

After saving the configuration and running the Starter Kit, use `QDRANT_API_KEY` value (e.g., `test`) as the `API Key` and `http://qdrant:6333/` as the `Qdrant URL`.

## [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#beyond-simple-similarity-search) Beyond Simple Similarity Search

Vector search’s ability to determine semantic similarity between objects is often used to address models’ hallucinations, powering the memory of Retrieval-Augmented Generation-based applications.

Yet there’s more to vector search than just a “knowledge base” role. **By exploring the concept of “dissimilarity,” we unlock new possibilities.** By measuring how similar data points are in a semantic vector space, we can also analyze their differences.

This combination of similarity and dissimilarity expands vector search to recommendations, discovery search, and large-scale unstructured data analysis.

### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#recommendations) Recommendations

When searching for new music, films, books, or food, it can be difficult to articulate exactly what we want. Instead, we often rely on discovering new content through comparison to examples of what we like or dislike.

The [Qdrant Recommendation API](https://qdrant.tech/articles/new-recommendation-api/) is built to make these discovery searches possible by using positive and negative examples as anchors. It helps find new relevant results based on your preferences.

#### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#movie-recommendations) Movie Recommendations

Imagine a home cinema night—you’ve already watched Harry Potter 666 times and crave a new series featuring young wizards. Your favorite streaming service repetitively recommends all seven parts of the millennial saga. Frustrated, you turn to n8n to create an **Agentic Movie Recommendation tool**.

**Setup:**

1. **Dataset**: We use movie descriptions from the [IMDB Top 1000 Kaggle dataset](https://www.kaggle.com/datasets/omarhanyy/imdb-top-1000).
2. **Embedding Model**: We’ll use OpenAI `text-embedding-3-small`, but you can opt for any other suitable embedding model.

**Workflow:**

A [Template Agentic Movie Recommendation Workflow](https://n8n.io/workflows/2440-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-open-ai/) consists of three parts:

1. **Movie Data Uploader**: Embeds movie descriptions and uploads them to Qdrant using the [Qdrant Vector Store Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant). In the template workflow, the dataset is fetched from GitHub, but you can use any supported storage, for example [Google Cloud Storage node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage).
2. **AI Agent**: Uses the [AI Agent Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent) to formulate Recommendation API calls based on your natural language requests. Choose an LLM as a “brain” and define a [JSON schema](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/#specify-input-schema) for the recommendations tool powered by Qdrant. This schema lets the LLM map your requests to the tool input format.
3. **Recommendations Tool**: A [subworkflow](https://docs.n8n.io/flow-logic/subworkflows/) that calls the Qdrant Recommendation API using the [HTTP Request Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest). The agent extracts relevant and irrelevant movie descriptions from your chat message and passes them to the tool. The tool embeds them with `text-embedding-3-small` and uses the Qdrant Recommendation API to get movie recommendations, which are passed back to the agent.

Set it up, run a chat and ask for “ _something about wizards but not Harry Potter_.”
What results do you get?

* * *

If you’d like a detailed walkthrough of building this workflow step-by-step, watch the video below:

RAG Movie Recommendations chatbot with Qdrant and n8n - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[RAG Movie Recommendations chatbot with Qdrant and n8n](https://www.youtube.com/watch?v=O5mT8M7rqQQ)

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

[Watch on](https://www.youtube.com/watch?v=O5mT8M7rqQQ&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 32:09
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=O5mT8M7rqQQ "Watch on YouTube")

This recommendation scenario is easily adaptable to any language or data type (images, audio, video).

### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#big-data-analysis) Big Data Analysis

The ability to map data to a vector space that reflects items’ similarity and dissimilarity relationships provides a range of mathematical tools for data analysis.

Vector search dedicated solutions are built to handle billions of data points and quickly compute distances between them, simplifying clustering, classification, dissimilarity sampling, deduplication, interpolation, and anomaly detection at scale.

The combination of this vector search feature with automation tools like n8n creates production-level solutions capable of monitoring data temporal shifts, managing data drift, and discovering patterns in seemingly unstructured data.

A practical example is worth a thousand words. Let’s look at **Qdrant-based anomaly detection and classification tools**, which are designed to be used by the [n8n AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent) for data analysis automation.

To make it more interesting, this time we’ll focus on image data.

#### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#anomaly-detection-tool) Anomaly Detection Tool

One definition of “anomaly” comes intuitively after projecting vector representations of data points into a 2D space—Qdrant webUI provides this functionality. Points that don’t belong to any clusters are more likely to be anomalous.

![anomalies-on-2D](https://qdrant.tech/blog/qdrant-n8n-2/anomalies-2D.png)

With that intuition comes the recipe for building an anomaly detection tool. We will demonstrate it on anomaly detection in agricultural crops. Qdrant will be used to:

1. Store vectorized images.
2. Identify a “center” (representative) for each crop cluster.
3. Define the borders of each cluster.
4. Check if new images fall within these boundaries. If an image does not fit within any cluster, it is flagged as anomalous. Alternatively, you can check if an image is anomalous to a specific cluster.

![anomaly-detection](https://qdrant.tech/blog/qdrant-n8n-2/anomaly-detection.png)

**Setup:**

1. **Dataset**: We use the [Agricultural Crops Image Classification dataset](https://www.kaggle.com/datasets/mdwaquarazam/agricultural-crops-image-classification).
2. **Embedding Model**: The [Voyage AI multimodal embedding model](https://docs.voyageai.com/docs/multimodal-embeddings). It can project images and text data into a shared vector space.

**1\. Uploading Images to Qdrant**

Since the [Qdrant Vector Store node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/) does not support embedding models outside the predefined list (which doesn’t include Voyage AI), we embed and upload data to Qdrant via direct API calls in [HTTP Request nodes](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/).

**Workflow:**

_There are three workflows: (1) Uploading images to Qdrant (2) Setting up cluster centers and thresholds (3) Anomaly detection tool itself._

An [1/3 Uploading Images to Qdrant Template Workflow](https://n8n.io/workflows/2654-vector-database-as-a-big-data-analysis-tool-for-ai-agents-13-anomaly12-knn/) consists of the following blocks:

1. **Check Collection**: Verifies if a collection with the specified name exists in Qdrant. If not, it creates one.
2. **Payload Index**: Adds a [payload index](https://qdrant.tech/documentation/concepts/indexing/#payload-index) on the `crop_name` payload (metadata) field. This field stores crop class labels, and indexing it improves the speed of filterable searches in Qdrant. It changes the way a vector index is constructed, adapting it for fast vector search under filtering constraints. For more details, refer to this [guide on filtering in Qdrant](https://qdrant.tech/articles/vector-search-filtering/).
3. **Fetch Images**: Fetches images from Google Cloud Storage using the [Google Cloud Storage node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage).
4. **Generate IDs**: Assigns UUIDs to each data point.
5. **Embed Images**: Embeds the images using the Voyage API.
6. **Batch Upload**: Uploads the embeddings to Qdrant in batches.

**2\. Defining a Cluster Representative**

We used two approaches (it’s not an exhaustive list) to defining a cluster representative, depending on the availability of labeled data:

| Method | Description |
| --- | --- |
| **Medoids** | A point within the cluster that has the smallest total distance to all other cluster points. This approach needs labeled data for each cluster. |
| **Perfect Representative** | A representative defined by a textual description of the ideal cluster member—the multimodality of Voyage AI embeddings allows for this trick. For example, for cherries: _“Small, glossy red fruits on a medium-sized tree with slender branches and serrated leaves.”_ The closest image to this description in the vector space is selected as the representative. This method requires experimentation to align descriptions with real data. |

![cluster-representative](https://qdrant.tech/blog/qdrant-n8n-2/cluster-representative.png)

**Workflow:**

Both methods are demonstrated in the [2/3 Template Workflow for Anomaly Detection](https://n8n.io/workflows/2655-vector-database-as-a-big-data-analysis-tool-for-ai-agents-23-anomaly/).

| **Method** | **Steps** |
| --- | --- |
| **Medoids** | 1\. Sample labeled cluster points from Qdrant.<br>2\. Compute a **pairwise distance matrix** for the cluster using Qdrant’s [Distance Matrix API](https://qdrant.tech/documentation/concepts/explore/?q=distance+#distance-matrix). This API helps with scalable cluster analysis and data points relationship exploration. Learn more in [this article](https://qdrant.tech/articles/distance-based-exploration/).<br>3\. For each point, calculate the sum of its distances to all other points. The point with the smallest total distance (or highest similarity for COSINE distance metric) is the medoid.<br>4\. Mark this point as the cluster representative. |
| **Perfect Representative** | 1\. Define textual descriptions for each cluster (e.g., AI-generated).<br>2\. Embed these descriptions using Voyage.<br>3\. Find the image embedding closest to the description one.<br>4\. Mark this image as the cluster representative. |

**3\. Defining the Cluster Border**

**Workflow:**

The approach demonstrated in [2/3 Template Workflow for Anomaly Detection](https://n8n.io/workflows/2655-vector-database-as-a-big-data-analysis-tool-for-ai-agents-23-anomaly/) works similarly for both types of cluster representatives.

1. Within a cluster, identify the furthest data point from the cluster representative (it can also be the 2nd or Xth furthest point; the best way to define it is through experimentation—for us, the 5th furthest point worked well). Since we use COSINE similarity, this is equivalent to the most similar point to the [opposite](https://mathinsight.org/image/vector_opposite) of the cluster representative (its vector multiplied by -1).
2. Save the distance between the representative and respective furthest point as the cluster border (threshold).

**4\. Anomaly Detection Tool**

**Workflow:**

With the preparatory steps complete, you can set up the anomaly detection tool, demonstrated in the [3/3 Template Workflow for Anomaly Detection](https://n8n.io/workflows/2656-vector-database-as-a-big-data-analysis-tool-for-ai-agents-33-anomaly/).

Steps:

1. Choose the method of the cluster representative definition.
2. Fetch all the clusters to compare the candidate image against.
3. Using Voyage AI, embed the candidate image in the same vector space.
4. Calculate the candidate’s similarity to each cluster representative. The image is flagged as anomalous if the similarity is below the threshold for all clusters (outside the cluster borders). Alternatively, you can check if it’s anomalous to a particular cluster, for example, the cherries one.

* * *

Anomaly detection in image data has diverse applications, including:

- Moderation of advertisements.
- Anomaly detection in vertical farming.
- Quality control in the food industry, such as [detecting anomalies in coffee beans](https://qdrant.tech/articles/detecting-coffee-anomalies/).
- Identifying anomalies in map tiles for tasks like automated map updates or ecological monitoring.

This tool is adaptable to these use cases and, when combined with n8n integrations, has the potential to become a production-level business solution.

#### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#classification-tool) Classification Tool

The anomaly detection tool can also be used for classification, but there’s a simpler approach: K-Nearest Neighbors (KNN) classification.

> “Show me your friends, and I will tell you who you are.”

![KNN-2D](https://qdrant.tech/blog/qdrant-n8n-2/KNN.png)

The KNN method labels a data point by analyzing its classified neighbors and assigning this point the majority class in the neighborhood. This approach doesn’t require all data points to be labeled—a subset of labeled examples can serve as anchors to propagate labels across the dataset. Qdrant is well-suited for this task, offering fast neighbor searches with filtering capabilities.

Let’s build a KNN-based image classification tool.

**Setup**

1. **Dataset**: We’ll use the [Land-Use Scene Classification dataset](https://www.kaggle.com/datasets/apollo2506/landuse-scene-classification). Satellite imagery analysis has applications in ecology, rescue operations, and map updates.
2. **Embedding Model**: As for anomaly detection, we’ll use the [Voyage AI multimodal embedding model](https://docs.voyageai.com/docs/multimodal-embeddings).

Additionally, it’s good to have test and validation data to determine the optimal value of K for your dataset.

**Workflow:**

Uploading images to Qdrant can be done using the same workflow— [1/3 Uploading Images to Qdrant Template Workflow](https://n8n.io/workflows/2654-vector-database-as-a-big-data-analysis-tool-for-ai-agents-13-anomaly12-knn/), just by swapping the dataset.

The [KNN-Classification Tool Template](https://n8n.io/workflows/2657-vector-database-as-a-big-data-analysis-tool-for-ai-agents-22-knn/) has the following steps:

1. **Embed Image**: Embeds the candidate for classification using Voyage.
2. **Fetch neighbors**: Retrieves the K closest labeled neighbors from Qdrant.
3. **Majority Voting**: Determines the prevailing class in the neighborhood by simple majority voting.
4. **Optional: Ties Resolving**: In case of ties, expands the neighborhood radius.

Of course, this is a simple solution, and there exist more advanced approaches with higher precision & no need for labeled data—for example, you could try [metric learning with Qdrant](https://qdrant.tech/articles/metric-learning-tips/).

Though classification seems like a task that was solved in machine learning decades ago, it’s not so trivial to deal with in production. Issues like data drift, shifting class definitions, mislabeled data, and fuzzy differences between classes create unexpected problems, which require continuous adjustments of classifiers. Vector Search can be an unusual but effective solution, interesting due to its scalability.

#### [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#live-walkthrough) Live Walkthrough

To see how n8n agents use these tools in practice, and to revisit the main ideas of the “ _Big Data Analysis_” section, watch our integration webinar:

Build production-ready AI Agents with Qdrant and n8n - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Build production-ready AI Agents with Qdrant and n8n](https://www.youtube.com/watch?v=_BQTnXpuH-E)

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

[Watch on](https://www.youtube.com/watch?v=_BQTnXpuH-E&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 1:20:41
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=_BQTnXpuH-E "Watch on YouTube")

## [Anchor](https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/\#whats-next) What’s Next?

Vector search is not limited to similarity search or basic RAG. When combined with automation platforms like n8n, it becomes a powerful tool for building smarter systems. Think dynamic routing in customer support, content moderation based on user behavior, or AI-driven alerts in data monitoring dashboards.

This blog showed how to use Qdrant and n8n for AI-backed recommendations, classification, and anomaly detection. But that’s just the start—try vector search for:

- **Deduplication**
- **Dissimilarity search**
- **Diverse sampling**

With Qdrant and n8n, there’s plenty of room to create something unique!

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=fe2def23-b128-46f5-929e-4911e3856a5a)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0f80f81b-43c4-4eef-a00f-379df785be2b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=fddbc933-87a8-4a7b-a6e8-6844170b3fe3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n-beyond-simple-similarity-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0f80f81b-43c4-4eef-a00f-379df785be2b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=fddbc933-87a8-4a7b-a6e8-6844170b3fe3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n-beyond-simple-similarity-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n-beyond-simple-similarity-search%2F&portalId=139603372&pageTitle=Automating+Business+Processes+with+Qdrant+and+n8n%3A+Use+Cases+Beyond+Simple+Similarity+Search+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=2edf31612ad2ec5c3dc0da66724fca2a&hssc=265983056.1.1748573672700&hstc=265983056.2edf31612ad2ec5c3dc0da66724fca2a.1748573672700.1748573672700.1748573672700.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-n8n-beyond-simple-similarity-search%2F&pageTitle=Automating+Business+Processes+with+Qdrant+and+n8n%3A+Use+Cases+Beyond+Simple+Similarity+Search+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=2edf31612ad2ec5c3dc0da66724fca2a&hssc=265983056.1.1748573672700&hstc=265983056.2edf31612ad2ec5c3dc0da66724fca2a.1748573672700.1748573672700.1748573672700.1&hsfp=3707738794).