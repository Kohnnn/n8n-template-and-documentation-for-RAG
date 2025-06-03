---
url: "https://supabase.com/customers/xendit"
title: "Xendit | Supabase Customer Stories"
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# Xendit use Supabase and create a full solution shipped to production in less than one week.

As a payment processor, Xendit are responsible for verifying that all transactions are legal.

![Xendit use Supabase and create a full solution shipped to production in less than one week. logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fxendit.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Xendit is a financial technology company that provides payment solutions and simplifies the payment process for businesses in Indonesia, the Philippines, and Southeast Asia, from SMEs and e-commerce startups to large enterprises.

[https://xendit.co](https://xendit.co/)

FoundedJakarta Selatan

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

## Challenge [\#](https://supabase.com/customers/xendit\#challenge)

As a payment processor, Xendit are responsible for verifying that all transactions are legal. Any transactions which are suspicions must be verified against a strict set of criteria, and the parties involved need to be checked against international sanctions lists. This is a critical anti-money-laundering operation and needs to be performed in realtime to prevent any delays on legitimate payments.

## Why they chose Supabase [\#](https://supabase.com/customers/xendit\#why-they-chose-supabase)

Xendit needed something fast. Something that was cheaper than using the global players like Worldcheck or Refinitiv. Xendit already uses Postgres for a lot of their critical infrastructure, and so Xendit team are familiar with the technology and comfortable in it's ability to scale.

## What they built [\#](https://supabase.com/customers/xendit\#what-they-built)

Xendit parses international sanctions lists from the UN and the Indonesian government and loads them into Supabase. Since Supabase provides a full Postgres server, they can then use the [Trigram](https://www.postgresql.org/docs/current/pgtrgm.html) extension to perform full-text search on the lists, with a relevance score on every search.

Supabase was perfect for their use case, as they needed something built fast. The full solution was built and in production in less than one week.

> The full solution was built and in production in less than one week.

Xendit created a database function for searching, which they are able to call directly using their Python clients. They have plans to iterate on the current implementation using more advanced techniques, like machine learning, but for now the Supabase system has been in Production for 9 months without a problem.

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)