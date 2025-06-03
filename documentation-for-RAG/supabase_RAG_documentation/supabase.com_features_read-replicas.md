---
url: "https://supabase.com/features/read-replicas"
title: "Read replicas | Supabase Features"
---

[Previous feature](https://supabase.com/features/queues) [Next feature](https://supabase.com/features/realtime-broadcast)

Stage:

Private Alpha

Available on self-hosted:

N/A

Supabase Read Replicas allow you to deploy additional read-only databases that are kept in sync with your Primary database. This feature enhances performance, improves resource management, and reduces latency for global applications.

## Key features

1. Load balancing: Distribute read operations across multiple databases, reducing load on the Primary.
2. Global deployment: Deploy replicas closer to users for reduced latency.
3. Dedicated endpoints: Each replica has its own database and API endpoints.
4. API load balancer: Automatically balance GET requests across all available endpoints.
5. Centralized configuration: Settings are propagated across all databases in a project.
6. Monitoring tools: Track replication lag and resource utilization through the Supabase Dashboard.

## Benefits:

- Improved performance: Serve data from the nearest location, reducing response times.
- Increased availability: Distribute read traffic across multiple replicas for enhanced resilience.
- Scalability: Handle higher read loads by offloading queries to replicas.
- Data redundancy: Replicas provide additional copies of your data.
- Analytics support: Run resource-intensive queries on replicas without impacting production.

## Read Replicas are particularly valuable for:

- Global applications serving users across different regions
- High-traffic websites with read-heavy workloads
- Real-time analytics dashboards requiring low-latency data access
- Applications needing to scale read capacity independently of write capacity

By leveraging Read Replicas, you can achieve consistent low-latency performance globally, improve application responsiveness for read operations, and enhance system reliability through better resource distribution and redundancy.

[Read Documentation](https://supabase.com/docs/guides/platform/read-replicas)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fread-replicas&text=Read%20replicas%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fread-replicas&text=Read%20replicas%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fread-replicas&t=Read%20replicas%20%7C%20Supabase%20Features)

[Queues](https://supabase.com/features/queues) [Realtime - Broadcast](https://supabase.com/features/realtime-broadcast)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)