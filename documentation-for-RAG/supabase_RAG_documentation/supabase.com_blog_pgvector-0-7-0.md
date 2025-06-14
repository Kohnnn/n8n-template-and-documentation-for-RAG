---
url: "https://supabase.com/blog/pgvector-0-7-0"
title: "What's new in pgvector v0.7.0"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# What's new in pgvector v0.7.0

02 May 2024

•

8 minute read

[![Pavel Borisov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F63344111%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Pavel BorisovPostgres Engineer](https://github.com/pashkinelfe)

![What's new in pgvector v0.7.0](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgvector-0-7-0.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Real-world embedding datasets often contain redundancy buried within the vector space. For example, when vectors cluster around certain central points in a multidimensional space, it reveals an exploitable structure. By reducing this redundancy, we can achieve memory and performance savings with a minimal impact on precision. Several approaches to leverage this idea have been introduced in pgvector since version 0.7.0:

- float16 vector representation
- sparse vectors
- bit vectors

### Float16 vectors [\#](https://supabase.com/blog/pgvector-0-7-0\#float16-vectors)

An HNSW index is most efficient when it fits into shared memory and avoids being evicted due to concurrent operations, which Postgres performs to minimize costly I/O operations. Historically, pgvector supported only 32-bit vectors. In version 0.7.0, pgvector introduces 16-bit float HNSW indexes which consume exactly half the memory. That reduction in memory keeps operations at maximum performance for twice as long.

There are two options when using float16 vectors:

- Index using float16, but the underlying table continues to use float32
- The index and the underlying table both use float16. This options uses 50% as much disk space in addition to requiring 50% less shared memory to operate efficiently. Performance is further improved with more vectors fitting in a single Postgres page and with fewer page evictions due to concurrent operations.

To duplicate an existing float32 embedding table to float16 one:

`
create table embedding_half (
id serial,
vector halfvec(1536),
primary key (id)
);
insert into embedding_half (vector)
select
vector::halfvec(1536)
from
embedding_full;
`

With 900K OpenAI 1536-dimensional vectors, the table size is 3.5Gb. For comparison, `embedding_full` required 7Gb.

Then we can build a float16 HNSW index:

`
create index on embedding_half using hnsw (vector halfvec_l2_ops);
`

To test the performance of index creation, we chose a `c7g.metal` instance with 128Gb memory and the following parameters:

`
shared_buffers = 50000MB
maintenance_work_mem = 30000MB
max_parallel_maintenance_workers = {0-63}
wal_level=minimal
max_wal_size = 10GB
autovacuum = off
full_page_writes = off
fsync = off
`

![security-peformance-advisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgvector-0-7-0-perf.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

HNSW build times recently experienced a stepwise improvement in the 0.6.2 release, which introduced parallel builds. 0.7.0 with the halfvec (float16) feature improves that speedup a further 30%.

Note that float16 vector arithmetic on the ARM architecture is identical to float32, so serial build times (with one parallel worker) have not improved. However there is a significant difference for parallel builds due to better pages and I/O utilization. Also note that this test doesn't use pre-warming or other artificial enhancements.

Both heap and HNSW relations for float16 occupy only half of the space compared to the previous float32 ones.

There is a proposal to speed it up even more in the future by using SVE intrinsics on ARM architecture (see: [https://github.com/pgvector/pgvector/pull/536](https://github.com/pgvector/pgvector/pull/536)).

Jonathan Katz [made his measurements](https://jkatz05.com/post/postgres/pgvector-performance-150x-speedup) on HNSW performance using `r7gd.16xlarge` (64 vCPU, 512GiB RAM), and his results are even better. For float16, HNSW build times are up to 3x faster. For select’s performance, ANN benchmark results show that precision is not changed with decreasing bitness, and queries per second (QPS) is similar to in-memory cases. But when real machine queries are using I/O or some HNSW pages are evicted from memory due to concurrent connections, there would be a meaningful difference. With only half of memory needed to accommodate the same HNSW index, cost for the same performance and precision is also significantly less.

|  | Vector / Vector | Vector / HalfVec |
| --- | --- | --- |
| **Index size (MB)** | 7734 | 3867 |
| **Index build time (s)** | 264 | 90 |
| **Recall @ ef\_search=10** | 0.819 | 0.809 |
| **QPS @ ef\_search=10** | 1231 | 1219 |
| **Recall @ ef\_search=40** | 0.945 | 0.945 |
| **QPS @ ef\_search=40** | 627 | 642 |
| **Recall @ ef\_search=200** | 0.987 | 0.987 |
| **QPS @ ef\_search=200** | 191 | 190 |

For full results on the different datasets, see [this GitHub issue](https://github.com/pgvector/pgvector/issues/326#issuecomment-2028467121).

### Sparse vectors [\#](https://supabase.com/blog/pgvector-0-7-0\#sparse-vectors)

If vectors contain many zero components, then a sparse vector representation can save significant storage space. For example, to populate sparse vectors:

`
create embedding_sparse (
id serial,
vector sparsevec(1536),
primary key (id)
)
insert into embedding_sparse (embedding) values ('{1:0.1,3:0.2,5:0.3}/1536'), ('{1:0.4,3:0.5,5:0.6}/1536');
`

The sparse vector only consumes storage space for the non-zero components. In this case, thats 3 values in a 1536 vector.

Note the new vector syntax `{1:3,3:1,5:2}/1536` for the sparse vector representation in:

`
select * from embedding_sparse order by vector <-> '{1:3,3:1,5:2}/1536' limit 5;
`

### Bit vectors [\#](https://supabase.com/blog/pgvector-0-7-0\#bit-vectors)

Using binary quantization we can represent float vector as a vector in binary space. This reduces storage size dramatically and is intended as a way to quickly “pre-select” from a data set before performing an additional search within the subset. When properly parameterized, the secondary select can be very fast, even without an index.

`
create index on embedding
using hnsw ((binary_quantize(vector)::bit(1000)) bit_hamming_ops);
select
*
from
embedding
order by
binary_quantize(vector)::bit(3) <~> binary_quantize('[1,-2,3]')
limit 5;
`

To use a binary quantized HNSW index to pre-select from a larger dataset and then make a fast selection from the resulting subset, without an index:

`
select * from (
select
    *
from
    embedding
order by
    binary_quantize(vector)::bit(3) <~> binary_quantize('[1,-2,3]')
limit 20
)
order by
vector <=> '[1,-2,3]'
limit 5;
`

It allows building a small and fast HNSW index for select, insert, or update operations while still having fast vector search. Exact configuration for the `limit` clauses are data dependent, so you’ll want to experiment with the sub-select size and the number of final results directly on your own dataset.

### New distance functions [\#](https://supabase.com/blog/pgvector-0-7-0\#new-distance-functions)

pgvector 0.7.0 also added support for L1 distance operator `<+>`.

And new distance types for indexing:

[L1 distance](https://en.wikipedia.org/wiki/Taxicab_geometry) \- added in 0.7.0

`
create index on items using hnsw (embedding vector_l1_ops);
`

[Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) \- added in 0.7.0

`
create index on items using hnsw (embedding bit_hamming_ops);
`

[Jaccard distance](https://en.wikipedia.org/wiki/Jaccard_index) \- added in 0.7.0

`
create index on vector using hnsw (vector bit_jaccard_ops);
`

### Conclusion [\#](https://supabase.com/blog/pgvector-0-7-0\#conclusion)

Over the last year pgvector has had significant development in both functionality and performance, including HNSW indexes, parallel builds, and many other options. With the introduction of half vectors (float16), sparse vectors, and bit vectors, we're now seeing over 100x speedup compared to one year ago.

For a more complete comparison of pgvector performance over the last year, check out [this post by Jonathan Katz](https://jkatz05.com/post/postgres/pgvector-performance-150x-speedup/).

### Using v0.7.0 in Supabase [\#](https://supabase.com/blog/pgvector-0-7-0\#using-v070-in-supabase)

All new projects ship with pgvector v0.7.0 (or later). Be sure to enable the extension if you haven't already:

`
create extension if not exists vector
with
schema extensions;
`

If you are unsure which version of pgvector your project is using, search for `vector` on the [Extensions page](https://supabase.com/dashboard/project/_/database/extensions). If you are using a previous version, you can upgrade
by navigating to the **Service Versions** section on the [Infrastructure page](https://supabase.com/dashboard/project/_/settings/infrastructure) and upgrading your Postgres version to `15.1.1.47` or later.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-0-7-0&text=What%27s%20new%20in%20pgvector%20v0.7.0)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-0-7-0&text=What%27s%20new%20in%20pgvector%20v0.7.0)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-0-7-0&t=What%27s%20new%20in%20pgvector%20v0.7.0)

[Last post\\
\\
**The open source Kahoot alternative** \\
\\
9 May 2024](https://supabase.com/blog/meetup-kahoot-alternative)

[Next post\\
\\
**Open Source Hackathon 2024 winners** \\
\\
30 April 2024](https://supabase.com/blog/supabase-oss-hackathon-winners)

[supabase-engineering](https://supabase.com/blog/tags/supabase-engineering) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Float16 vectors](https://supabase.com/blog/pgvector-0-7-0#float16-vectors)
- [Sparse vectors](https://supabase.com/blog/pgvector-0-7-0#sparse-vectors)
- [Bit vectors](https://supabase.com/blog/pgvector-0-7-0#bit-vectors)
- [New distance functions](https://supabase.com/blog/pgvector-0-7-0#new-distance-functions)
- [Conclusion](https://supabase.com/blog/pgvector-0-7-0#conclusion)
- [Using v0.7.0 in Supabase](https://supabase.com/blog/pgvector-0-7-0#using-v070-in-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-0-7-0&text=What%27s%20new%20in%20pgvector%20v0.7.0)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-0-7-0&text=What%27s%20new%20in%20pgvector%20v0.7.0)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-0-7-0&t=What%27s%20new%20in%20pgvector%20v0.7.0)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)