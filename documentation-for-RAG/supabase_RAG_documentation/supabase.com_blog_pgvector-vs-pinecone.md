---
url: "https://supabase.com/blog/pgvector-vs-pinecone"
title: "pgvector vs Pinecone: cost and performance"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# pgvector vs Pinecone: cost and performance

10 Oct 2023

•

9 minute read

[![Egor Romanov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fegor-romanov.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Egor RomanovEngineering](https://github.com/egor-romanov)

![pgvector vs Pinecone: cost and performance](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fpgvector-pinecone-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

At Supabase, we believe that a combination of Postgres and pgvector serves as a better alternative to single-purpose databases like Pinecone for AI tasks. This isn't the first time a Postgres-based solution has successfully rivaled specialized databases designed for specific data types. Timescale for time-series data and Greenplum for analytics are just a few examples.

We decided to put Postgres vector performance to the test and run a direct comparison between pgvector and Pinecone.

## What is Pinecone? [\#](https://supabase.com/blog/pgvector-vs-pinecone\#what-is-pinecone)

Pinecone is a fully managed cloud Vector Database that is only suitable for storing and searching vector data. It offers straightforward start-up and scalability. It employs a proprietary ANN index and lacks support for exact nearest neighbors search or fine-tuning. The only setting that allows you to adjust the balance between query accuracy and speed is the choice of pod type when creating an index.

So, before we dive into their performance, let us first introduce Pinecone's offerings.

### Pinecone has 3 Pod types for indexes [\#](https://supabase.com/blog/pgvector-vs-pinecone\#pinecone-has-3-pod-types-for-indexes)

An index on Pinecone is made up of pods, which are units of cloud resources (vCPU, RAM, disk) that provide storage and compute for each index.

| Type | Capacity / Vectors | QPS | Accuracy | Price per unit per month |
| --- | --- | --- | --- | --- |
| s1 | 5,000,000 768d (~2,500,000 1536d) | Slowest | 0.98 | $80 |
| p1 | 1,000,000 768d (~500,000 1536d) | Medium | 0.99 | $80 |
| p2 | 1,100,000 768d (~550,000 1536d) | Fastest | 0.94 | $120 |

Pods can be scaled in 2 dimensions: vertically and horizontally:

- **vertical scaling** can be used to fit more vectors on a single pod: x1, x2, x4, x8;
- **horizontal scaling** increases the number of pods or creates replicas to boost queries per second (QPS). This works linearly for Pinecone: doubling the number of replica pods doubles your QPS.

## Benchmarking methodology [\#](https://supabase.com/blog/pgvector-vs-pinecone\#benchmarking-methodology)

We utilized the [ANN Benchmarks](https://github.com/erikbern/ann-benchmarks) methodology, a standard for benchmarking vector databases. Our tests used the [dbpedia dataset](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M/blob/main/README.md) of 1,000,000 OpenAI embeddings (1536 dimensions) and inner product distance metric for both Pinecone and pgvector.

To compare Pinecone and pgvector on equal grounds, we opted for the following setups:

- **pgvector**: A single Supabase 2XL instance approximating ~410$/month (8-core ARM CPU and 32 GB RAM). An HNSW index with the following build parameters: `m='36'`, `ef_construction='128'`.
- **Pinecone**: Vertically scaled pod to the minimum option that fits the dbpedia dataset into the index on a single pod. We then added replicas to match the budget (slightly exceeding in all cases with ~$480/month).

To reduce network latency, we placed our clients in the same cloud provider and region as the database. Experiments were run in a parallel configuration, varying the number of concurrent clients from 5 to 100 to determine the maximum QPS for each setup.

### Measuring accuracy in Pinecone [\#](https://supabase.com/blog/pgvector-vs-pinecone\#measuring-accuracy-in-pinecone)

There is no available information on Pinecone's proprietary ANN index. Likewise, they doesn't provide information about query accuracy, nor does it support exact nearest neighbors search (KNN). So to measure Pinecone's accuracy, we had to compare its results with pgvector's exact search (KNN without indexes) for the same queries. This seems to be the only way to measure Pinecone's index accuracy.

## Benchmarking Results [\#](https://supabase.com/blog/pgvector-vs-pinecone\#benchmarking-results)

### Pinecone with s1 pod type [\#](https://supabase.com/blog/pgvector-vs-pinecone\#pinecone-with-s1-pod-type)

As the index can fit in a single s1.x1 pod ($80/month), we created five additional replicas. Our Pinecone setup consisted of **six s1 pods** (totaling $480/month). We measured Pinecone's accuracy for the dbpedia dataset using the s1 pod type, achieving a score of 0.98 at the 10 nearest neighbors (accuracy@10).

To match the measured .98 accuracy@10 of Pinecone s1 pods, we set `ef_search=32` for pgvector (HNSW) queries, and observed the following results:

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fs1x1--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The pgvector HNSW index can manage 1185% more queries per second while being $70 cheaper per month.

Interestingly, we'd often heard that the pgvector IVFFlat was too slow until the HNSW support was introduced. However, even the pgvector IVFFlat index on the same compute exceeds the Pinecone s1 pod and manages 143% more queries per second:

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fivfflat--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### p1 pod type [\#](https://supabase.com/blog/pgvector-vs-pinecone\#p1-pod-type)

With Pinecone p1 pods, we can fit the dbpedia dataset into the index on a single p1.x2 pod ($160/month). So, by adding two more replicas, we maintained our budget. Therefore, our second experiment involved a Pinecone setup scale of **three p1.x2 pods** (totaling $480/month). The measured accuracy@10 for the p1.x2 pod and dbpedia dataset was 0.99.

To match the .99 accuracy of Pinecone's p1.x2, we set `ef_search=40` for pgvector (HNSW) queries.

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fp1x2--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

pgvector demonstrated much better performance again with over 4x better QPS than the Pinecone setup, while still being $70 cheaper per month. As Pinecone can linearly scale by adding more replicas, you can estimate that you would need 12-13 p1.x2 pods to match pgvector performance. This equates to approximately $2000 per month versus ~$410 per month for a 2XL on Supabase.

### p2 pod type [\#](https://supabase.com/blog/pgvector-vs-pinecone\#p2-pod-type)

This is Pinecone's fastest pod type, but the increased QPS results in an accuracy trade-off. We measured `accuracy@10=0.94` for the p2 pods and the dbpedia dataset. It is possible to fit the index on a single p2.x2 pod (240$/month), so we could add 1 replica. Thus, Pinecone's setup for the third experiment consisted of **two p2.x2 pods** (totaling $480/month).

To match Pinecone's .94 accuracy, we set `ef_search=10` for pgvector ( [HNSW](https://www.notion.so/Blogpost-pgvector-vs-Pinecone-cost-and-performance-5d5cc429818d45358ba2d3a8a06e1ecf?pvs=21)) queries. In this test, pgvector's accuracy was actually better by 1% with .95 accuracy@10, and it was still significantly faster despite the better accuracy.

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fp2x2--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Here's something important to highlight: pgvector is faster than Pinecone's fastest pod type, even with an accuracy@10=0.99 compared to Pinecone's 0.94. Pinecone's most expensive option sacrifices 5% accuracy just to match pgvector's speed.

## Additional thoughts on Pinecone vs. pgvector [\#](https://supabase.com/blog/pgvector-vs-pinecone\#additional-thoughts-on-pinecone-vs-pgvector)

It's only fair to note that Pinecone may be cheaper than pgvector since you could use a single p1.x2 pod without replicas, costing about $160 per month, and you would still achieve approximately 60 QPS with `accuracy@10=0.99`. For pgvector on Supabase, this means you might not be able to fit the index in RAM as you may use a large ($110) or XL ($210) compute add-on and will fall back to KNN search without any indexes. However, this translates to potentially adding more vectors, similar to the s1 pod on Pinecone.

Real user stories indicate this might not be problematic. For instance, Quivr expanded to 1 million vectors without using any indexes:

![tweet about quivr getting to almost 1M vectors with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fquivr-tweet.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## pgvector's hidden cost-saving benefits [\#](https://supabase.com/blog/pgvector-vs-pinecone\#pgvectors-hidden-cost-saving-benefits)

There are also a couple of benefits from a developer experience perspective that we often take for granted when using Postgres:

- Postgres offers numerous features applicable to your vectors: database backups, row-level security, client libraries support and ORMs for 18 languages, complete ACID compliance, bulk updates and deletes (metadata updates in seconds).
- Having all your data in a sole Postgres instance (or a cluster) reduces roundtrips in production and allows running the entire developer setup locally.
- Implementing additional databases can increase operational complexity and the learning curve.
- Postgres is battle-tested and robust, whereas most specialized vector databases haven't had time to demonstrate their reliability.

## Start using HNSW [\#](https://supabase.com/blog/pgvector-vs-pinecone\#start-using-hnsw)

All [new Supabase databases](https://database.new/) automatically ship with pgvector v0.5.0 which includes the new HNSW indexes. Try it out today and let us know what you think!

## More pgvector and AI resources [\#](https://supabase.com/blog/pgvector-vs-pinecone\#more-pgvector-and-ai-resources)

- [pgvector v0.5.0: Faster semantic search with HNSW indexes](https://supabase.com/blog/increase-performance-pgvector-hnsw)
- [Docs pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
- [Choosing Compute Add-on for AI workloads](https://supabase.com/docs/guides/ai/choosing-compute-addon)
- [pgvector: Fewer dimensions are better](https://supabase.com/blog/fewer-dimensions-are-better-pgvector)
- [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
- [ChatGPT plugins now support Postgres & Supabase](https://supabase.com/blog/chatgpt-plugins-support-postgres)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-vs-pinecone&text=pgvector%20vs%20Pinecone%3A%20cost%20and%20performance)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-vs-pinecone&text=pgvector%20vs%20Pinecone%3A%20cost%20and%20performance)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-vs-pinecone&t=pgvector%20vs%20Pinecone%3A%20cost%20and%20performance)

[Last post\\
\\
**Supabase is now compatible with Next.js 14** \\
\\
1 November 2023](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14)

[Next post\\
\\
**Offline-first React Native Apps with Expo, WatermelonDB, and Supabase** \\
\\
8 October 2023](https://supabase.com/blog/react-native-offline-first-watermelon-db)

[AI](https://supabase.com/blog/tags/AI) [performance](https://supabase.com/blog/tags/performance) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [What is Pinecone?](https://supabase.com/blog/pgvector-vs-pinecone#what-is-pinecone)
  - [Pinecone has 3 Pod types for indexes](https://supabase.com/blog/pgvector-vs-pinecone#pinecone-has-3-pod-types-for-indexes)
- [Benchmarking methodology](https://supabase.com/blog/pgvector-vs-pinecone#benchmarking-methodology)
  - [Measuring accuracy in Pinecone](https://supabase.com/blog/pgvector-vs-pinecone#measuring-accuracy-in-pinecone)
- [Benchmarking Results](https://supabase.com/blog/pgvector-vs-pinecone#benchmarking-results)
  - [Pinecone with s1 pod type](https://supabase.com/blog/pgvector-vs-pinecone#pinecone-with-s1-pod-type)
  - [p1 pod type](https://supabase.com/blog/pgvector-vs-pinecone#p1-pod-type)
  - [p2 pod type](https://supabase.com/blog/pgvector-vs-pinecone#p2-pod-type)
- [Additional thoughts on Pinecone vs. pgvector](https://supabase.com/blog/pgvector-vs-pinecone#additional-thoughts-on-pinecone-vs-pgvector)
- [pgvector's hidden cost-saving benefits](https://supabase.com/blog/pgvector-vs-pinecone#pgvectors-hidden-cost-saving-benefits)
- [Start using HNSW](https://supabase.com/blog/pgvector-vs-pinecone#start-using-hnsw)
- [More pgvector and AI resources](https://supabase.com/blog/pgvector-vs-pinecone#more-pgvector-and-ai-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-vs-pinecone&text=pgvector%20vs%20Pinecone%3A%20cost%20and%20performance)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-vs-pinecone&text=pgvector%20vs%20Pinecone%3A%20cost%20and%20performance)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-vs-pinecone&t=pgvector%20vs%20Pinecone%3A%20cost%20and%20performance)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fs1x1--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fivfflat--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fp1x2--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![visual of an example skip list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fp2x2--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![tweet about quivr getting to almost 1M vectors with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-10-pgvector-vs-pinecone%2Fquivr-tweet.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)