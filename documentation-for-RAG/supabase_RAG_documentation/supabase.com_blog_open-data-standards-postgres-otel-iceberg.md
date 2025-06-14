---
url: "https://supabase.com/blog/open-data-standards-postgres-otel-iceberg"
title: "Open Data Standards: Postgres, OTel, and Iceberg"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Open Data Standards: Postgres, OTel, and Iceberg

26 May 2025

•

7 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Open Data Standards: Postgres, OTel, and Iceberg](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fopen-data-standards%2Fthree-open-data-standards-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

There are three emerging standards in the world of data: Postgres, Open Telemetry, and Iceberg.

Postgres is arguably a standard already. [OTel](https://opentelemetry.io/) and [Iceberg](https://iceberg.apache.org/) are nascent but they have the same ingredients helped Postgres become the world's most popular database. I've been asked many times "why did Postgres win?". The typical response is "extensibility", which is correct, but incomplete.

Besides being a great product, Postgres has some important open source dynamics: the nuance lies in the open source model.

## The Three Tenets of Open Source [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#the-three-tenets-of-open-source)

I've realized there are three tenets of open source. Developers will assess the "open sourceness" of any project by:

1. **License:** is the license [OSI-approved](https://opensource.org/licenses).
2. **Self-hosting:** how feasible is it to self-host the _entire product_.
3. **Commercialization**: is the project commercially unencumbered and vendor neutral or (even better) is it backed by _many_ commercial entities.

The third tenet took me a while to grasp. Yes, Postgres won because it's a great product, but even better: it cannot be owned by any single entity. The governance and cultural resistance makes it impossible. Postgres is like the International Space Station where several large commercial entities collaborated because no single entity can own it.

Postgres checks the "open source" checkbox, but it's not a magic-bullet for all data-related tasks.

## The Three Data Personas [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#the-three-data-personas)

In the data space there are 3 primary "data personas" and their respective tools:

1. **OLTP Databases:** used by _developers_ to build apps.
2. **Telemetry:** used by _SREs_ to manage infra and optimize applications.
3. **OLAP/Warehousing**: used by _data engineers/scientists_ to draw insights.

The data lifecycle typically flows from `1 → 2 → 3`: first a developer builds an application, then they add basic telemetry (sometimes just click events in their OLTP database), and eventually their OLTP database becomes large enough that they need a data warehouse.

The three personas are distinct in their way of operating and preferred tools. That said, the industry continues to shift left: as data tooling improves, observability and warehousing is increasingly the domain of the developer. This shift isn't an intentional action by SREs or data engineers. It's because databases are becoming more scalable and developers/startups can cope for longer before hiring specialized help.

## The Three Open Data Standards [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#the-three-open-data-standards)

Around these three data use-cases, I've started to see three open data standards emerging that exhibit the same open source tenets:

1. OLTP: Postgres
2. Telemetry: Open Telemetry
3. OLAP: Iceberg

The second two are interesting because they are "standards" rather than "tools". The dynamic is similar to HTML (standard) and browsers (tools): data is stored/transferred in an agreed format and the tools need to adopt the standard or get left behind.

![Open standards](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fopen-data-standards%2Fopen-standards-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

These standards start as a grass-roots movement and commercial entities are compelled to adopt them through a [disruptive technology](https://en.wikipedia.org/wiki/Disruptive_innovation) dilemma:

- if they _don't_ adopt the standard, they will miss out on the growing trend.
- if they _do_ adopt the standard, they lower the lock-in for their own tool/platform.

This is a _fantastic_ dynamic for the developer community, and one that we [strongly believe in](https://supabase.com/docs/guides/getting-started/architecture#everything-is-portable): _portability forces companies to compete on experience_.

Diving deeper into each of these tools:

### Postgres is the open OLTP standard [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#postgres-is-the-open-oltp-standard)

While Postgres is a _tool_, it has also become a _standard_. Nearly every new database offering aims for "Postgres [wire](https://www.postgresql.org/docs/current/protocol.html) compatibility". Because Postgres isn't owned by any individual commercial entity, every major cloud can offer it - or even is _forced_ to offer it because it’s a standard. Hell, even Oracle cloud offers it. If you have a bad experience with any particular vendor, you can simply `pg_dump` your data and take it to another provider. Postgres uses the [PostgreSQL license](https://www.postgresql.org/about/licence/), which is functionally equivalent to MIT.

### OTel is the open telemetry standard [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#otel-is-the-open-telemetry-standard)

It's even in the name "open telemetry". [OTel](https://opentelemetry.io/) is still nascent and incredibly [complicated](https://news.ycombinator.com/item?id=42655102), but it fits the open source tenets above: the license is Apache 2.0 and it’s vendor neutral. Just as the major cloud providers embraced Postgres, the leading telemetry platforms are now adopting OTel including [Datadog](https://docs.datadoghq.com/integrations/otel/), [Honeycomb](https://docs.honeycomb.io/send-data/opentelemetry/), [Grafana Labs](https://grafana.com/grafana/dashboards/15983-opentelemetry-collector/), and [Elastic](https://www.elastic.co/docs/solutions/observability/apm/use-opentelemetry-with-apm). For self-hosting, developers are able to choose from a various open source options like [SigNoz](https://github.com/SigNoz/signoz), [OpenObserve](https://github.com/openobserve/openobserve), and the default OTel [tools](https://github.com/open-telemetry/opentelemetry-collector).

### Iceberg is the open OLAP standard [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#iceberg-is-the-open-olap-standard)

[Open Table Formats](https://www.startdataengineering.com/post/what_why_table_format/) are a relatively new development. They are simply an "agreed format" for organizing large amounts of data. Because the format is agreed, any tool can query it. There are a few competing Open Table Formats including [DeltaLake](https://delta.io/) and [Hudi](https://hudi.apache.org/), but [Iceberg](https://iceberg.apache.org/) has emerged as the leader.

All the major data warehouses are adopting Iceberg, including [Databricks](https://docs.databricks.com/aws/en/delta/uniform), [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg), and [ClickHouse](https://clickhouse.com/docs/engines/table-engines/integrations/iceberg). The most important commercial entity however, driving the Third Tenet of Open Source, is AWS. At the end of 2024 AWS announced [S3 Tables](https://aws.amazon.com/blogs/aws/new-amazon-s3-tables-storage-optimized-for-analytics-workloads/), which makes it trivial to store data in S3 using Iceberg format in S3.

## S3 is the ultimate data infrastructure [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#s3-is-the-ultimate-data-infrastructure)

Object storage is so cheap that it's becoming the fundamental substrate of all three open data standards. All data tooling built today is adopting some form of interoperability with S3, or an S3-compatible service.

The AWS S3 team are releasing updates that will accelerate the concept of "S3 as a database" - including [Conditional Writes](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/) and [S3 Express](https://aws.amazon.com/blogs/aws/new-amazon-s3-express-one-zone-high-performance-storage-class/) which is 10x faster than "standard S3” and recently became [85% cheaper](https://aws.amazon.com/blogs/aws/up-to-85-price-reductions-for-amazon-s3-express-one-zone/).

![S3 as a database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fopen-data-standards%2Fs3-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The tooling for S3 interoperability differs slightly depending on the use-case:

- For OLTP databases, where performance is paramount, there will always be a "disk" layer between S3. There is simply no way that a network disk can operate at the speed of NVMe SSDs. The key interoperability with S3 will be ZeroETL and Tiered Storage: the ability to move "cold" data easily between your operational database and S3. Postgres offers several methods to read the data out of Iceberg, including [pg\_mooncake](https://github.com/Mooncake-Labs/pg_mooncake), [pg\_duckdb](https://github.com/duckdb/pg_duckdb), and [Iceberg Foreign Data Wrappers](https://github.com/supabase/wrappers/pull/462).
- For Telemetry and Warehousing, cardinality is the key factor. As S3 becomes cheaper, businesses are storing exponentially more data in object storage, driving an architecture where storage and compute are decoupled. This has sparked demand for database offerings that serve as compute layers, connecting directly to S3. Most of these are embedded databases, like [DuckDB](https://duckdb.org/2021/10/29/duckdb-wasm.html) (OLAP), SQLite’s [cloud-backed storage](https://sqlite.org/cloudsqlite/doc/trunk/www/index.wiki), [turbopuffer](https://turbopuffer.com/) (vectors/embeddings), [SlateDB](https://slatedb.io/) (KV), and [Tonbo](https://tonbo.io/) (Arrow). These embedded databases can run within your application or be used as a standalone tool.

## Data at Supabase [\#](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg\#data-at-supabase)

Supabase is now relatively well-known as a Postgres provider. We've spent 5 years building a delightful database platform for developers and that will continue to be our focus.

What's unique about Supabase is that we're not _just_ a Postgres provider (despite the [memes](https://itsjustpostgres.com/)). We also offer [Supabase Storage](https://supabase.com/storage), an S3-compatible object store. Where we're going is less about a database, and more about data. This includes:

- Adding OTel to all of the open source tools we maintain.
- Adding Iceberg support in Supabase Storage.
- Adding Iceberg support to [Supabase ETL](https://github.com/supabase/supabase_etl) for zero-ETL between Postgres and Iceberg.
- Adding Iceberg read/write capabilities to Postgres via extensions and FDWs.

Our focus from here is the three Open Data Standards: Postgres, OTel, and Iceberg.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopen-data-standards-postgres-otel-iceberg&text=Open%20Data%20Standards%3A%20Postgres%2C%20OTel%2C%20and%20Iceberg)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopen-data-standards-postgres-otel-iceberg&text=Open%20Data%20Standards%3A%20Postgres%2C%20OTel%2C%20and%20Iceberg)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fopen-data-standards-postgres-otel-iceberg&t=Open%20Data%20Standards%3A%20Postgres%2C%20OTel%2C%20and%20Iceberg)

[Next post\\
\\
**Simplifying back-end complexity with Supabase Data APIs** \\
\\
17 May 2025](https://supabase.com/blog/simplify-backend-with-data-api)

[postgres](https://supabase.com/blog/tags/postgres) [iceberg](https://supabase.com/blog/tags/iceberg) [otel](https://supabase.com/blog/tags/otel)

On this page

- [The Three Tenets of Open Source](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#the-three-tenets-of-open-source)
- [The Three Data Personas](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#the-three-data-personas)
- [The Three Open Data Standards](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#the-three-open-data-standards)
  - [Postgres is the open OLTP standard](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#postgres-is-the-open-oltp-standard)
  - [OTel is the open telemetry standard](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#otel-is-the-open-telemetry-standard)
  - [Iceberg is the open OLAP standard](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#iceberg-is-the-open-olap-standard)
- [S3 is the ultimate data infrastructure](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#s3-is-the-ultimate-data-infrastructure)
- [Data at Supabase](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg#data-at-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopen-data-standards-postgres-otel-iceberg&text=Open%20Data%20Standards%3A%20Postgres%2C%20OTel%2C%20and%20Iceberg)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fopen-data-standards-postgres-otel-iceberg&text=Open%20Data%20Standards%3A%20Postgres%2C%20OTel%2C%20and%20Iceberg)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fopen-data-standards-postgres-otel-iceberg&t=Open%20Data%20Standards%3A%20Postgres%2C%20OTel%2C%20and%20Iceberg)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Open standards](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fopen-data-standards%2Fopen-standards-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![S3 as a database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fopen-data-standards%2Fs3-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)