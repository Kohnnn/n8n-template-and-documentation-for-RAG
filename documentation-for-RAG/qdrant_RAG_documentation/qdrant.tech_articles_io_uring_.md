---
url: "https://qdrant.tech/articles/io_uring/"
title: "Qdrant under the hood: io_uring - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Qdrant under the hood: io\_uring

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Qdrant under the hood: io\_uring

Andre Bogus

·

June 21, 2023

![Qdrant under the hood: io_uring](https://qdrant.tech/articles_data/io_uring/preview/title.jpg)

With Qdrant [version 1.3.0](https://github.com/qdrant/qdrant/releases/tag/v1.3.0) we
introduce the alternative io\_uring based _async uring_ storage backend on
Linux-based systems. Since its introduction, io\_uring has been known to improve
async throughput wherever the OS syscall overhead gets too high, which tends to
occur in situations where software becomes _IO bound_ (that is, mostly waiting
on disk).

## [Anchor](https://qdrant.tech/articles/io_uring/\#inputoutput) Input+Output

Around the mid-90s, the internet took off. The first servers used a process-
per-request setup, which was good for serving hundreds if not thousands of
concurrent request. The POSIX Input + Output (IO) was modeled in a strictly
synchronous way. The overhead of starting a new process for each request made
this model unsustainable. So servers started forgoing process separation, opting
for the thread-per-request model. But even that ran into limitations.

I distinctly remember when someone asked the question whether a server could
serve 10k concurrent connections, which at the time exhausted the memory of
most systems (because every thread had to have its own stack and some other
metadata, which quickly filled up available memory). As a result, the
synchronous IO was replaced by asynchronous IO during the 2.5 kernel update,
either via `select` or `epoll` (the latter being Linux-only, but a small bit
more efficient, so most servers of the time used it).

However, even this crude form of asynchronous IO carries the overhead of at
least one system call per operation. Each system call incurs a context switch,
and while this operation is itself not that slow, the switch disturbs the
caches. Today’s CPUs are much faster than memory, but if their caches start to
miss data, the memory accesses required led to longer and longer wait times for
the CPU.

### [Anchor](https://qdrant.tech/articles/io_uring/\#memory-mapped-io) Memory-mapped IO

Another way of dealing with file IO (which unlike network IO doesn’t have a hard
time requirement) is to map parts of files into memory - the system fakes having
that chunk of the file in memory, so when you read from a location there, the
kernel interrupts your process to load the needed data from disk, and resumes
your process once done, whereas writing to the memory will also notify the
kernel. Also the kernel can prefetch data while the program is running, thus
reducing the likelyhood of interrupts.

Thus there is still some overhead, but (especially in asynchronous
applications) it’s far less than with `epoll`. The reason this API is rarely
used in web servers is that these usually have a large variety of files to
access, unlike a database, which can map its own backing store into memory
once.

### [Anchor](https://qdrant.tech/articles/io_uring/\#combating-the-poll-ution) Combating the Poll-ution

There were multiple experiments to improve matters, some even going so far as
moving a HTTP server into the kernel, which of course brought its own share of
problems. Others like Intel added their own APIs that ignored the kernel and
worked directly on the hardware.

Finally, Jens Axboe took matters into his own hands and proposed a ring buffer
based interface called _io\_uring_. The buffers are not directly for data, but
for operations. User processes can setup a Submission Queue (SQ) and a
Completion Queue (CQ), both of which are shared between the process and the
kernel, so there’s no copying overhead.

![io_uring diagram](https://qdrant.tech/articles_data/io_uring/io-uring.png)

Apart from avoiding copying overhead, the queue-based architecture lends
itself to multithreading as item insertion/extraction can be made lockless,
and once the queues are set up, there is no further syscall that would stop
any user thread.

Servers that use this can easily get to over 100k concurrent requests. Today
Linux allows asynchronous IO via io\_uring for network, disk and accessing
other ports, e.g. for printing or recording video.

## [Anchor](https://qdrant.tech/articles/io_uring/\#and-what-about-qdrant) And what about Qdrant?

Qdrant can store everything in memory, but not all data sets may fit, which can
require storing on disk. Before io\_uring, Qdrant used mmap to do its IO. This
led to some modest overhead in case of disk latency. The kernel may
stop a user thread trying to access a mapped region, which incurs some context
switching overhead plus the wait time until the disk IO is finished. Ultimately,
this works very well with the asynchronous nature of Qdrant’s core.

One of the great optimizations Qdrant offers is quantization (either
[scalar](https://qdrant.tech/articles/scalar-quantization/) or
[product](https://qdrant.tech/articles/product-quantization/)-based).
However unless the collection resides fully in memory, this optimization
method generates significant disk IO, so it is a prime candidate for possible
improvements.

If you run Qdrant on Linux, you can enable io\_uring with the following in your
configuration:

```yaml
# within the storage config
storage:
	# enable the async scorer which uses io_uring
	async_scorer: true

```

You can return to the mmap based backend by either deleting the `async_scorer`
entry or setting the value to `false`.

## [Anchor](https://qdrant.tech/articles/io_uring/\#benchmarks) Benchmarks

To run the benchmark, use a test instance of Qdrant. If necessary spin up a
docker container and load a snapshot of the collection you want to benchmark
with. You can copy and edit our [benchmark script](https://qdrant.tech/articles_data/io_uring/rescore-benchmark.sh)
to run the benchmark. Run the script with and without enabling
`storage.async_scorer` and once. You can measure IO usage with `iostat` from
another console.

For our benchmark, we chose the laion dataset picking 5 million 768d entries.
We enabled scalar quantization + HNSW with m=16 and ef\_construct=512.
We do the quantization in RAM, HNSW in RAM but keep the original vectors on
disk (which was a network drive rented from Hetzner for the benchmark).

If you want to reproduce the benchmarks, you can get snapshots containing the
datasets:

- [mmap only](https://storage.googleapis.com/common-datasets-snapshots/laion-768-6m-mmap.snapshot)
- [with scalar quantization](https://storage.googleapis.com/common-datasets-snapshots/laion-768-6m-sq-m16-mmap.shapshot)

Running the benchmark, we get the following IOPS, CPU loads and wall clock times:

|  | oversampling | parallel | ~max IOPS | CPU% (of 4 cores) | time (s) (avg of 3) |
| --- | --- | --- | --- | --- | --- |
| io\_uring | 1 | 4 | 4000 | 200 | 12 |
| mmap | 1 | 4 | 2000 | 93 | 43 |
| io\_uring | 1 | 8 | 4000 | 200 | 12 |
| mmap | 1 | 8 | 2000 | 90 | 43 |
| io\_uring | 4 | 8 | 7000 | 100 | 30 |
| mmap | 4 | 8 | 2300 | 50 | 145 |

Note that in this case, the IO operations have relatively high latency due to
using a network disk. Thus, the kernel takes more time to fulfil the mmap
requests, and application threads need to wait, which is reflected in the CPU
percentage. On the other hand, with the io\_uring backend, the application
threads can better use available cores for the rescore operation without any
IO-induced delays.

Oversampling is a new feature to improve accuracy at the cost of some
performance. It allows setting a factor, which is multiplied with the `limit`
while doing the search. The results are then re-scored using the original vector
and only then the top results up to the limit are selected.

## [Anchor](https://qdrant.tech/articles/io_uring/\#discussion) Discussion

Looking back, disk IO used to be very serialized; re-positioning read-write
heads on moving platter was a slow and messy business. So the system overhead
didn’t matter as much, but nowadays with SSDs that can often even parallelize
operations while offering near-perfect random access, the overhead starts to
become quite visible. While memory-mapped IO gives us a fair deal in terms of
ease of use and performance, we can improve on the latter in exchange for
some modest complexity increase.

io\_uring is still quite young, having only been introduced in 2019 with kernel
5.1, so some administrators will be wary of introducing it. Of course, as with
performance, the right answer is usually “it depends”, so please review your
personal risk profile and act accordingly.

## [Anchor](https://qdrant.tech/articles/io_uring/\#best-practices) Best Practices

If your on-disk collection’s query performance is of sufficiently high
priority to you, enable the io\_uring-based async\_scorer to greatly reduce
operating system overhead from disk IO. On the other hand, if your
collections are in memory only, activating it will be ineffective. Also note
that many queries are not IO bound, so the overhead may or may not become
measurable in your workload. Finally, on-device disks typically carry lower
latency than network drives, which may also affect mmap overhead.

Therefore before you roll out io\_uring, perform the above or a similar
benchmark with both mmap and io\_uring and measure both wall time and IOps).
Benchmarks are always highly use-case dependent, so your mileage may vary.
Still, doing that benchmark once is a small price for the possible performance
wins. Also please
[tell us](https://discord.com/channels/907569970500743200/907569971079569410)
about your benchmark results!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/io_uring.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/io_uring.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575094832&cv=11&fst=1748575094832&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fio_uring%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20under%20the%20hood%3A%20io_uring%20-%20Qdrant&npa=0&pscdl=noapi&auid=688469615.1748575095&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575094804&cv=11&fst=1748575094804&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fio_uring%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20under%20the%20hood%3A%20io_uring%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=688469615.1748575095&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9548964f-8d87-4649-9b32-448e94a612b9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3445204b-5adf-451e-bcde-388c259a9562&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fio_uring%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9548964f-8d87-4649-9b32-448e94a612b9&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3445204b-5adf-451e-bcde-388c259a9562&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fio_uring%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575096435&cv=11&fst=1748575096435&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fio_uring%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20under%20the%20hood%3A%20io_uring%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=688469615.1748575095&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)