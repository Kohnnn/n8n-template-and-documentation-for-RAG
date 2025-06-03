---
url: "https://supabase.com/blog/automating-performance-tests"
title: "Automating performance tests"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Automating performance tests

21 Feb 2024

•

18 minute read

[![Egor Romanov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fegor-romanov.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Egor RomanovEngineering](https://github.com/egor-romanov)

![Automating performance tests](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fautomating-performance-tests-OG.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Performance testing is one of the non-functional testing types that evaluates a system's compliance with its performance requirements. It reveals if your app can handle user load, unexpected spikes, or recover from stressful workloads. In this blogpost you will learn about how we got to the automated performance testing. I hope our lessons will make this journey easier for you.

At the end of this post you will have a practical approach for doing performance testing manually and automatically and a set of tools and templates to get started.

## How this started? [\#](https://supabase.com/blog/automating-performance-tests\#how-this-started)

When I joined Supabase we had a challenging task of rewriting Realtime service so that users would be able to stream database updates with respect to RLS policies. Such a huge design change could not happen without having an impact on throughput.

We decided to extensively test how the new Realtime would perform prior to launch to:

- compare the capabilities of the new version and the current version,
- determine the speed, performance, and stability of the new Realtime and establish standards for the future,
- understand how it is scaling,
- find bugs.

In fact we had to test 2 versions at once for the new Realtime. The new architecture allowed it to work not only with a single database instance, but also as a multitenant independent service, distributed all over the world to bring presence and broadcast functionalities.

Realtime v1 & v2:

![Realtime v1 & v2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Frealtime-v1-and-v2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Realtime v3:

![Realtime v3](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Frealtime-v3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The important aspect of Realtime is that this is a streaming service working over websocket protocol.

### The difference between HTTP and Websocket [\#](https://supabase.com/blog/automating-performance-tests\#the-difference-between-http-and-websocket)

| HTTP | Websocket |
| --- | --- |
| Request-Response | Full duplex |
| Short-lived connection | Persistent connection |
| Requests always initiated by client | Both client and server can init a message sending |

These differences and Realtime specific affect how performance testing should be implemented.

- Many persistent connections to the server,
- Latency in message delivery is more impactful,
- Few tools support WebSocket,
- May consume more resources of load generators,
- Different scripts for generating messages and working with subscribers,
- Several scenarios of work (database changes, broadcast, presence).

## Load generation tool [\#](https://supabase.com/blog/automating-performance-tests\#load-generation-tool)

We had to choose the tool for generating the load. And I thought that k6 would be the great fit. This was my table of pros and cons for this decision:

| pros | cons |
| --- | --- |
| Recommend by colleagues | No default GUI |
| JS for scripts and go for extensions | Still young |
| Good documentation |  |
| OSS and huge community |  |
| WS out of the box and extensions for database |  |

## Manual testing setup [\#](https://supabase.com/blog/automating-performance-tests\#manual-testing-setup)

We started with a task to compare 3 versions of Realtime: Replication (v1), RLS (v2), and Cluster (v3). And came up with the following infrastructure:

- For Realtime v1 and v2, the service was deployed close to the database and served only requests to this single DB.
- For Realtime v3, the service was deployed as a separate cluster in the Fly cloud.
- Load generators were a couple of VMs deployed to AWS.

![Manual testing setup](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fmanual-testing-setup.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This gave us the first results!

![Standard k6 console output](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fk6-output.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

But take a look at these results. We noticed that numbers for message delivery latency were not great. While this output would be ok if everything was good, it was not enough to make conclusions about what was going wrong. That’s why I decided to add Grafana.

### Grafana for better visibility [\#](https://supabase.com/blog/automating-performance-tests\#grafana-for-better-visibility)

Luckily community around k6 is great and already solved this issue. So I plugged in k6-prometheus extension to send metrics from load test, created cloud Grafana project which comes with Prometheus instance to send metrics to, built my first dashboard, and continued testing:

![Grafana dashboard with messages stop reaching clients and high latency](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-performance-results.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

With Grafana it became clear that issue was with the resource exhaustion on the loader instances. So I migrated VMs to instances with more compute ( `c5.4xlarge`) and tried again:

![Grafana dashboard with more compute but metrics stopped reaching Prometheus](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-performance-results-with-more-compute.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This time my testing was interrupted by metrics stopped reaching the Prometheus at some point during the test. The investigation revealed that volume of the data from the load test was too high for Prometheus push endpoint.

### Telegraf is here to help [\#](https://supabase.com/blog/automating-performance-tests\#telegraf-is-here-to-help)

To solve this once and for all, I put intermediary Telegraf service, that would pull all the metrics from k6 script and push them to cloud Prometheus.

Telegraf core features for us:

- Collects metrics from different sources: k6 scripts, host (cpu, ram, network, etc.);
- Monitors the health of the load generator itself;
- Integrates with many time series databases (Influx, VictoriaMetrics, Prometheus, etc.);
- In-memory metric buffer;
- Pull & push for both collection and delivery of metrics.

And finally our manual setup for performance testing was completed.

![Grafana dashboard with Telegraf in the middle, no more issues](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-performance-testing-results.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

On our way here we fixed a couple of bugs in the new Realtime and achieved some great results!

## Complete manual setup [\#](https://supabase.com/blog/automating-performance-tests\#complete-manual-setup)

It may be that this is all you need for now, so I will list everything you would need to replicate this setup below. Here is how it looks like, just replace Realtime with the service you are testing, and check if it fits:

![Complete manual setup diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fcomplete-manual-setup.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

| Component | Description |
| --- | --- |
| [k6](https://github.com/supabase/benchmarks/blob/main/examples/realtime/replication/terraform/k6/subs.js) | Load generator scripts |
| VM in the cloud [with the following preparation](https://github.com/supabase/benchmarks/tree/main/infra/ami) | Hosts for k6 and Telegraf |
| Prometheus and [Grafana](https://github.com/supabase/benchmarks/blob/main/examples/realtime/grafana.json) | Observability stack |
| [Telegraf](https://github.com/supabase/benchmarks/blob/main/k6/telegraf.conf) | Collect metrics from k6 and host and push them to Prometheus |
| [Launches table in Grafana](https://gist.github.com/egor-romanov/df6b61f5b0ac3a6f4afdbb19154a612f) | To navigate through the history of launches |

![Grafana dashboard with launches table](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-launches-table.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Manual setup shortcomings [\#](https://supabase.com/blog/automating-performance-tests\#manual-setup-shortcomings)

While solving the basic tasks, we still had one unresolved:

- Compare multiple options ✅
- Determine speed, performance, stability ✅
- Understand how it is scaling ✅
- Find bugs ✅
- Determine standards for an app ✅
- Check if it continues to meet standards with future releases 🚫

While we can think that with each new release someone will go, start a VM from paused state and trigger a test. In reality this is unlikely to happen. And in addition to that, we got a couple additional issues that needed to be addressed.

- You can forget to stop the virtual machine or not stop the SUT,
- It is difficult to share resources with developers,
- It is inconvenient to update code on multiple load generators,
- Bad UX for launch history.

## Automate everything [\#](https://supabase.com/blog/automating-performance-tests\#automate-everything)

The solution to all these problems is automation. And at first I took a look at the k6 cloud. It is the great platform, but the price for testing Realtime service, or similar applications that require huge amounts of simultaneous users connected is extremely high. With our workloads it could easily cost us hundred thousands or more per year.

After a search for an open-source options, I was left with the only choice of implementing my own service with the following requirements:

- Able to run virtual machines to create load;
- Able to launch the application under test;
- Convenient work with run history;
- Send current code to load generators;
- Manage secrets and variables;
- Integration with CI;
- Do not depend on vendors;
- Fast and easy to develop.

## Building benchmarking app [\#](https://supabase.com/blog/automating-performance-tests\#building-benchmarking-app)

The first technology I decided to use was terraform. As it is open-source, it allows to provide infrastructure using many different cloud providers, and it has a great golang SDK.

I left observability stack intact: Prometheus, Grafana and Telegraf demonstrated their ability to perform exceptionally well, to store results for year or even more, and to build reach insightful dashboards with metrics from multiple sources.

I built a simple golang app prototype in a matter of days. App could store and execute terraforms and k6 scenarios, gave access to launch history, secured secrets, and everything with access policies and user management.

![Benchmarks setup with app to manage load tests and observability stack](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fbuilding-benchmarking-app.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Here is how the app looks like:

![App to manage load tests dashboard with launch history](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-results.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Did we resolve our issues? [\#](https://supabase.com/blog/automating-performance-tests\#did-we-resolve-our-issues)

Let’s bring the list of what was left:

- Check if it continues to meet standards with future releases
  - ✅, the app has an API that can be used from GitHub actions.
- You can forget to stop the virtual machine or not stop the SUT
  - ✅, as this is now automatically done by the app.
- It is difficult to share resources with developers
  - ✅, not anymore, since now resource creation is automated by app.
- It is inconvenient to update code on multiple load generators
  - ✅, the latest version of code is always delivered to loaders by the app.
- Bad UX for launch history
  - ✅, the whole history is available on the app's dashboard with links to relevant Grafana timespans for detailed analysis.

## Our experience [\#](https://supabase.com/blog/automating-performance-tests\#our-experience)

We have run tests for up to 1,000,000 concurrent virtual users for Supavisor and up to 200,000 for the Realtime service.

![Grafana dashboard with 1M concurrent users for Supavisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fsupavisor-1m.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can find more details about this test in the [Supavisor: Scaling Postgres to 1 Million Connections](https://supabase.com/blog/supavisor-1-million) post.

![Grafana dashboard with 200k concurrent users for Realtime](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Frealtime-200k.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It took from a couple of hours to a couple of days to add performance testing process for other services we provide: Storage, ImgProxy, Edge Runtime, Supavisor, PostgREST, Postgres.

This approach helped us to add performance testing for new projects and return to it with new releases much faster across all products at Supabase.

## Complete automated performance testing setup [\#](https://supabase.com/blog/automating-performance-tests\#complete-automated-performance-testing-setup)

If you want to replicate our approach, I am leaving the list of things we use. Start with our benchmarks repo, where you will find a code for the benchmarks app, and a bunch of examples (real performance tests we use):

| Component | Description |
| --- | --- |
| [repo](https://github.com/supabase/benchmarks/tree/main) | Benchmarks app source code and examples |
| [prod instance](https://supabench.fly.dev/#) | Our benchmarks app instance |
| [Terraform documentation](https://developer.hashicorp.com/terraform/docs) | Read about Terraform and how to use it |
| [Virtual machine image](https://github.com/supabase/benchmarks/tree/main/infra/ami) | Prepare VM for running k6 load scripts |
| [Grafana and Prometheus or VictoriaMetrics setup](https://github.com/supabase/benchmarks/tree/main/.docker) | Observability stack setup |

## Conclusion [\#](https://supabase.com/blog/automating-performance-tests\#conclusion)

In this post you learned two approaches for organizing the performance testing process. Choose the one that fits the current state of your project and ship battle-tested applications without worrying about how they are going to handle the load.

## More performance resources [\#](https://supabase.com/blog/automating-performance-tests\#more-performance-resources)

- [Supavisor: Scaling Postgres to 1 Million Connections](https://supabase.com/blog/supavisor-1-million)
- [pgvector vs Pinecone: cost and performance](https://supabase.com/blog/pgvector-vs-pinecone)
- [Matryoshka embeddings: faster OpenAI vector search using Adaptive Retrieval](https://supabase.com/blog/matryoshka-embeddings)
- [Choosing Compute Add-on for AI workloads](https://supabase.com/docs/guides/ai/choosing-compute-addon)
- [pgvector 0.6.0: 30x faster with parallel index builds](https://supabase.com/blog/pgvector-fast-builds)
- [pgvector: Fewer dimensions are better](https://supabase.com/blog/fewer-dimensions-are-better-pgvector)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomating-performance-tests&text=Automating%20performance%20tests)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomating-performance-tests&text=Automating%20performance%20tests)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomating-performance-tests&t=Automating%20performance%20tests)

[Last post\\
\\
**Build a content recommendation app with Flutter and OpenAI** \\
\\
26 February 2024](https://supabase.com/blog/content-recommendation-with-flutter)

[Next post\\
\\
**Matryoshka embeddings: faster OpenAI vector search using Adaptive Retrieval** \\
\\
13 February 2024](https://supabase.com/blog/matryoshka-embeddings)

[performance](https://supabase.com/blog/tags/performance)

On this page

- [How this started?](https://supabase.com/blog/automating-performance-tests#how-this-started)
  - [The difference between HTTP and Websocket](https://supabase.com/blog/automating-performance-tests#the-difference-between-http-and-websocket)
- [Load generation tool](https://supabase.com/blog/automating-performance-tests#load-generation-tool)
- [Manual testing setup](https://supabase.com/blog/automating-performance-tests#manual-testing-setup)
  - [Grafana for better visibility](https://supabase.com/blog/automating-performance-tests#grafana-for-better-visibility)
  - [Telegraf is here to help](https://supabase.com/blog/automating-performance-tests#telegraf-is-here-to-help)
- [Complete manual setup](https://supabase.com/blog/automating-performance-tests#complete-manual-setup)
- [Manual setup shortcomings](https://supabase.com/blog/automating-performance-tests#manual-setup-shortcomings)
- [Automate everything](https://supabase.com/blog/automating-performance-tests#automate-everything)
- [Building benchmarking app](https://supabase.com/blog/automating-performance-tests#building-benchmarking-app)
  - [Did we resolve our issues?](https://supabase.com/blog/automating-performance-tests#did-we-resolve-our-issues)
- [Our experience](https://supabase.com/blog/automating-performance-tests#our-experience)
- [Complete automated performance testing setup](https://supabase.com/blog/automating-performance-tests#complete-automated-performance-testing-setup)
- [Conclusion](https://supabase.com/blog/automating-performance-tests#conclusion)
- [More performance resources](https://supabase.com/blog/automating-performance-tests#more-performance-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomating-performance-tests&text=Automating%20performance%20tests)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomating-performance-tests&text=Automating%20performance%20tests)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomating-performance-tests&t=Automating%20performance%20tests)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Realtime v1 & v2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Frealtime-v1-and-v2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Realtime v3](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Frealtime-v3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Manual testing setup](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fmanual-testing-setup.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Standard k6 console output](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fk6-output.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Grafana dashboard with messages stop reaching clients and high latency](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-performance-results.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Grafana dashboard with more compute but metrics stopped reaching Prometheus](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-performance-results-with-more-compute.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Grafana dashboard with Telegraf in the middle, no more issues](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-performance-testing-results.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Complete manual setup diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fcomplete-manual-setup.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Grafana dashboard with launches table](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-launches-table.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Benchmarks setup with app to manage load tests and observability stack](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fbuilding-benchmarking-app.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![App to manage load tests dashboard with launch history](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fgrafana-results.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Grafana dashboard with 1M concurrent users for Supavisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Fsupavisor-1m.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Grafana dashboard with 200k concurrent users for Realtime](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-02-21-automating-performance-tests%2Frealtime-200k.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)