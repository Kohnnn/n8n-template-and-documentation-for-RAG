---
url: "https://docs.n8n.io/hosting/scaling/performance-benchmarking/"
title: "Performance and benchmarking | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/scaling/performance-benchmarking/#performance-and-benchmarking)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/scaling/performance-benchmarking.md "Edit this page")

# Performance and benchmarking [\#](https://docs.n8n.io/hosting/scaling/performance-benchmarking/\#performance-and-benchmarking "Permanent link")

n8n can handle up to 220 workflow executions per second on a single instance, with the ability to scale up further by adding more instances.

This document outlines n8n's performance benchmarking. It describes the factors that affect performance, and includes two example benchmarks.

## Performance factors [\#](https://docs.n8n.io/hosting/scaling/performance-benchmarking/\#performance-factors "Permanent link")

The performance of n8n depends on factors including:

- The workflow type
- The resources available to n8n
- How you configure n8n's scaling options

## Run your own benchmarking [\#](https://docs.n8n.io/hosting/scaling/performance-benchmarking/\#run-your-own-benchmarking "Permanent link")

To get an accurate estimate for your use case, run n8n's [benchmarking framework](https://github.com/n8n-io/n8n/tree/master/packages/%40n8n/benchmark). The repository contains more information about the benchmarking.

## Example: Single instance performance [\#](https://docs.n8n.io/hosting/scaling/performance-benchmarking/\#example-single-instance-performance "Permanent link")

This test measures how response time increases as requests per second increase. It looks at the response time when calling the Webhook Trigger node.

Setup:

- Hardware: ECS c5a.large instance (4GB RAM)
- n8n setup: Single n8n instance (running in main mode, with Postgres database)
- Workflow: Webhook Trigger node, Edit Fields node

[![Graph showing n8n response times by requests per second](https://docs.n8n.io/_images/hosting/scaling/benchmarking-single-instance-100-250.png)](https://docs.n8n.io/_images/hosting/scaling/benchmarking-single-instance-100-250.png)

This graph shows the percentage of requests to the Webhook Trigger node getting a response within 100 seconds, and how that varies with load. Under higher loads n8n usually still processes the data, but takes over 100s to respond.

## Example: Multi-instance performance [\#](https://docs.n8n.io/hosting/scaling/performance-benchmarking/\#example-multi-instance-performance "Permanent link")

This test measures how response time increases as requests per second increase. It looks at the response time when calling the Webhook Trigger node.

Setup:

- Hardware: seven ECS c5a.4xlarge instances (8GB RAM each)
- n8n setup: two webhook instances, four worker instances, one database instance (MySQL), one main instance running n8n and Redis
- Workflow: Webhook Trigger node, Edit Fields node
- Multi-instance setups use [Queue mode](https://docs.n8n.io/hosting/scaling/queue-mode/)

[![Graph showing n8n response times by requests per second](https://docs.n8n.io/_images/hosting/scaling/benchmarking-multi-instance-500-2500.png)](https://docs.n8n.io/_images/hosting/scaling/benchmarking-multi-instance-500-2500.png)

This graph shows the percentage of requests to the Webhook Trigger node getting a response within 100 seconds, and how that varies with load. Under higher loads n8n usually still processes the data, but takes over 100s to respond.
Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top