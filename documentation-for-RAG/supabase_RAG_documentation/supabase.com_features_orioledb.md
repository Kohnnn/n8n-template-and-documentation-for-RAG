---
url: "https://supabase.com/features/orioledb"
title: "OrioleDB | Supabase Features"
---

[Previous feature](https://supabase.com/features/network-restrictions) [Next feature](https://supabase.com/features/passwordless-login-via-magicklink)

Stage:

Public Alpha

Available on self-hosted:

Yes

OrioleDB is a PostgreSQL storage extension built on its pluggable storage framework. Serving as a direct replacement for PostgreSQL's Heap storage, it addresses scalability challenges while harnessing the full power of modern hardware. Designed to integrate effortlessly with PostgreSQL, OrioleDB enhances performance, efficiency, and scalability, all while maintaining the reliability and robustness PostgreSQL users depend on.

## Key benefits:

1. Fully integrated: A drop-in replacement for PostgreSQL’s Heap storage, enabling easy adoption without major changes to existing workflows.
2. Enhanced scalability: Eliminates buffer mapping bottlenecks and utilizes lock-less page reading, significantly improving vertical scalability and hardware utilization.
3. Superior performance: Proven to outperform PostgreSQL Heap by up to 5.5x in benchmarks, particularly under high-load and large-scale scenarios.
4. Reduced maintenance overhead: Undo log-based MVCC eliminates storage bloat and removes the need for VACUUM, preventing common performance degradation.
5. Efficient storage management: Built-in compression reduces storage requirements by up to 5x, enabling more cost-effective data handling.
6. Modern write-ahead logging (WAL): Row-level WAL supports parallelism and is designed for future active-active multi-master configurations.
7. Optimized for large datasets: Index-organized tables improve data locality, reducing disk I/O for workloads exceeding memory cache capacity.

## Roadmap Features:

1. Decoupled storage and compute with S3 integration for unlimited scalability.
2. Planned columnar indexes to enable hybrid OLTP and OLAP workloads on the same system.
3. Multi-master replication for better availability and fault tolerance.

[Read Documentation](https://supabase.com/docs/guides/database/orioledb)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Forioledb&text=OrioleDB%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Forioledb&text=OrioleDB%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Forioledb&t=OrioleDB%20%7C%20Supabase%20Features)

[Network restrictions](https://supabase.com/features/network-restrictions) [Passwordless login via Magic Links](https://supabase.com/features/passwordless-login-via-magicklink)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![OrioleDB thumbnail](https://supabase.com/_next/image?url=%2Fimages%2Ffeatures%2Forioledb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![OrioleDB thumbnail](https://supabase.com/_next/image?url=%2Fimages%2Ffeatures%2Forioledb-light.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)