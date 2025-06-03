---
url: "https://qdrant.tech/articles/memory-consumption/"
title: "Minimal RAM you need to serve a million vectors - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Minimal RAM you need to serve a million vectors

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Minimal RAM you need to serve a million vectors

Andrei Vasnetsov

·

December 07, 2022

![Minimal RAM you need to serve a million vectors](https://qdrant.tech/articles_data/memory-consumption/preview/title.jpg)

When it comes to measuring the memory consumption of our processes, we often rely on tools such as `htop` to give us an indication of how much RAM is being used. However, this method can be misleading and doesn’t always accurately reflect the true memory usage of a process.

There are many different ways in which `htop` may not be a reliable indicator of memory usage.
For instance, a process may allocate memory in advance but not use it, or it may not free deallocated memory, leading to overstated memory consumption.
A process may be forked, which means that it will have a separate memory space, but it will share the same code and data with the parent process.
This means that the memory consumption of the child process will be counted twice.
Additionally, a process may utilize disk cache, which is also accounted as resident memory in the `htop` measurements.

As a result, even if `htop` shows that a process is using 10GB of memory, it doesn’t necessarily mean that the process actually requires 10GB of RAM to operate efficiently.
In this article, we will explore how to properly measure RAM usage and optimize [Qdrant](https://qdrant.tech/) for optimal memory consumption.

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#how-to-measure-actual-ram-requirements) How to measure actual RAM requirements

We need to know memory consumption in order to estimate how much RAM is required to run the program.
So in order to determine that, we can conduct a simple experiment.
Let’s limit the allowed memory of the process and observe at which point it stops functioning.
In this way we can determine the minimum amount of RAM the program needs to operate.

One way to do this is by conducting a grid search, but a more efficient method is to use binary search to quickly find the minimum required amount of RAM.
We can use docker to limit the memory usage of the process.

Before running each benchmark, it is important to clear the page cache with the following command:

```bash
sudo bash -c 'sync; echo 1 > /proc/sys/vm/drop_caches'

```

This ensures that the process doesn’t utilize any data from previous runs, providing more accurate and consistent results.

We can use the following command to run Qdrant with a memory limit of 1GB:

```bash
docker run -it --rm \
    --memory 1024mb \
    --network=host \
    -v "$(pwd)/data/storage:/qdrant/storage" \
    qdrant/qdrant:latest

```

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#lets-run-some-benchmarks) Let’s run some benchmarks

Let’s run some benchmarks to see how much RAM Qdrant needs to serve 1 million vectors.

We can use the `glove-100-angular` and scripts from the [vector-db-benchmark](https://github.com/qdrant/vector-db-benchmark) project to upload and query the vectors.
With the first run we will use the default configuration of Qdrant with all data stored in RAM.

```bash
# Upload vectors
python run.py --engines qdrant-all-in-ram --datasets glove-100-angular

```

After uploading vectors, we will repeat the same experiment with different RAM limits to see how they affect the memory consumption and search speed.

```bash
# Search vectors
python run.py --engines qdrant-all-in-ram --datasets glove-100-angular --skip-upload

```

### [Anchor](https://qdrant.tech/articles/memory-consumption/\#all-in-memory) All in Memory

In the first experiment, we tested how well our system performs when all vectors are stored in memory.
We tried using different amounts of memory, ranging from 1512mb to 1024mb, and measured the number of requests per second (rps) that our system was able to handle.

| Memory | Requests/s |
| --- | --- |
| 1512mb | 774.38 |
| 1256mb | 760.63 |
| 1200mb | 794.72 |
| 1152mb | out of memory |
| 1024mb | out of memory |

We found that 1152MB memory limit resulted in our system running out of memory, but using 1512mb, 1256mb, and 1200mb of memory resulted in our system being able to handle around 780 RPS.
This suggests that about 1.2GB of memory is needed to serve around 1 million vectors, and there is no speed degradation when limiting memory usage above 1.2GB.

### [Anchor](https://qdrant.tech/articles/memory-consumption/\#vectors-stored-using-mmap) Vectors stored using MMAP

Let’s go a bit further!
In the second experiment, we tested how well our system performs when **vectors are stored using the memory-mapped file** (mmap).
Create collection with:

```http
PUT /collections/benchmark
{
  "vectors": {
    ...
    "on_disk": true
  }
}

```

This configuration tells Qdrant to use mmap for vectors if the segment size is greater than 20000Kb (which is approximately 40K 128d-vectors).

Now the out-of-memory happens when we allow using **600mb** RAM only

Experiments details

| Memory | Requests/s |
| --- | --- |
| 1200mb | 759.94 |
| 1100mb | 687.00 |
| 1000mb | 10 |

— use a bit faster disk —

| Memory | Requests/s |
| --- | --- |
| 1000mb | 25 rps |
| 750mb | 5 rps |
| 625mb | 2.5 rps |
| 600mb | out of memory |

At this point we have to switch from network-mounted storage to a faster disk, as the network-based storage is too slow to handle the amount of sequential reads that our system needs to serve the queries.

But let’s first see how much RAM we need to serve 1 million vectors and then we will discuss the speed optimization as well.

### [Anchor](https://qdrant.tech/articles/memory-consumption/\#vectors-and-hnsw-graph-stored-using-mmap) Vectors and HNSW graph stored using MMAP

In the third experiment, we tested how well our system performs when vectors and [HNSW](https://qdrant.tech/articles/filtrable-hnsw/) graph are stored using the memory-mapped files.
Create collection with:

```http
PUT /collections/benchmark
{
  "vectors": {
    ...
    "on_disk": true
  },
  "hnsw_config": {
    "on_disk": true
  },
  ...
}

```

With this configuration we are able to serve 1 million vectors with **only 135mb of RAM**!

Experiments details

| Memory | Requests/s |
| --- | --- |
| 600mb | 5 rps |
| 300mb | 0.9 rps / 1.1 sec per query |
| 150mb | 0.4 rps / 2.5 sec per query |
| 135mb | 0.33 rps / 3 sec per query |
| 125mb | out of memory |

At this point the importance of the disk speed becomes critical.
We can serve the search requests with 135mb of RAM, but the speed of the requests makes it impossible to use the system in production.

Let’s see how we can improve the speed.

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#how-to-speed-up-the-search) How to speed up the search

To measure the impact of disk parameters on search speed, we used the `fio` tool to test the speed of different types of disks.

```bash
# Install fio
sudo apt-get install fio

# Run fio to check the random reads speed
fio --randrepeat=1 \
    --ioengine=libaio \
    --direct=1 \
    --gtod_reduce=1 \
    --name=fiotest \
    --filename=testfio \
    --bs=4k \
    --iodepth=64 \
    --size=8G \
    --readwrite=randread

```

Initially, we tested on a network-mounted disk, but its performance was too slow, with a read IOPS of 6366 and a bandwidth of 24.9 MiB/s:

```text
read: IOPS=6366, BW=24.9MiB/s (26.1MB/s)(8192MiB/329424msec)

```

To improve performance, we switched to a local disk, which showed much faster results, with a read IOPS of 63.2k and a bandwidth of 247 MiB/s:

```text
read: IOPS=63.2k, BW=247MiB/s (259MB/s)(8192MiB/33207msec)

```

That gave us a significant speed boost, but we wanted to see if we could improve performance even further.
To do that, we switched to a machine with a local SSD, which showed even better results, with a read IOPS of 183k and a bandwidth of 716 MiB/s:

```text
read: IOPS=183k, BW=716MiB/s (751MB/s)(8192MiB/11438msec)

```

Let’s see how these results translate into search speed:

| Memory | RPS with IOPS=63.2k | RPS with IOPS=183k |
| --- | --- | --- |
| 600mb | 5 | 50 |
| 300mb | 0.9 | 13 |
| 200mb | 0.5 | 8 |
| 150mb | 0.4 | 7 |

As you can see, the speed of the disk has a significant impact on the search speed.
With a local SSD, we were able to increase the search speed by 10x!

With the production-grade disk, the search speed could be even higher.
Some configurations of the SSDs can reach 1M IOPS and more.

Which might be an interesting option to serve large datasets with low search latency in Qdrant.

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#conclusion) Conclusion

In this article, we showed that Qdrant has flexibility in terms of RAM usage and can be used to serve large datasets. It provides configurable trade-offs between RAM usage and search speed. If you’re interested to learn more about Qdrant, [book a demo today](https://qdrant.tech/contact-us/)!

We are eager to learn more about how you use Qdrant in your projects, what challenges you face, and how we can help you solve them.
Please feel free to join our [Discord](https://qdrant.to/discord) and share your experience with us!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/memory-consumption.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/memory-consumption.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1db23905-68e4-4a88-b1e6-f64b71966554&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eb88119b-63b3-45d4-9387-762a3e1df528&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmemory-consumption%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573723808&cv=11&fst=1748573723808&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmemory-consumption%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Minimal%20RAM%20you%20need%20to%20serve%20a%20million%20vectors%20-%20Qdrant&npa=0&pscdl=noapi&auid=1807943334.1748573724&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573723797&cv=11&fst=1748573723797&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmemory-consumption%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Minimal%20RAM%20you%20need%20to%20serve%20a%20million%20vectors%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1807943334.1748573724&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1db23905-68e4-4a88-b1e6-f64b71966554&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eb88119b-63b3-45d4-9387-762a3e1df528&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmemory-consumption%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573724474&cv=11&fst=1748573724474&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fmemory-consumption%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Minimal%20RAM%20you%20need%20to%20serve%20a%20million%20vectors%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1807943334.1748573724&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)