---
url: "https://supabase.com/customers/bree"
title: "Bree | Supabase Customer Stories"
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# Bree's Migration to Supabase from Fauna

Bree found 10X performance gains, greater developer velocity, and a better foundation for AI when switching to Supabase.

![Bree's Migration to Supabase from Fauna logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fbree.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Helping people living paycheck-to-paycheck access better, faster financial products.

[https://www.trybree.com](https://www.trybree.com/)

FoundedCanada

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

> We hit scalability limits with Fauna, and Supabase was a step up across the board. The developer
> experience, ecosystem, support for AI. It’s the complete package.
>
> ![Ryan Han, Head of Engineering and AI, Bree avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fryan-han-bree.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ryan Han, Head of Engineering and AI, Bree

## Breaking free from the limitations of Fauna [\#](https://supabase.com/customers/bree\#breaking-free-from-the-limitations-of-fauna)

[Bree](https://www.trybree.com/) is a Canadian FinTech startup focused on helping over 20 million Canadians living paycheck to paycheck access better, faster financial products. As the company scaled, it needed to move quickly, experimenting, shipping features, and iterating on user feedback in near real time. But their initial backend stack was holding them back.

Bree had originally built their infrastructure on Fauna, a NoSQL database with a proprietary query language (FQL). The limitations quickly surfaced.

> Fauna’s custom language, FQL, introduced friction in our development process. It took time to
> learn and made it harder for our team to iterate and ship at the speed we needed.
>
> ![Ryan Han, Head of Engineering and AI, Bree avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fryan-han-bree.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ryan Han, Head of Engineering and AI, Bree

Engineering velocity suffered. Teams couldn’t iterate on product features without hitting roadblocks, and performance tuning became an ongoing challenge.

And when Fauna announced its end of life, it only added urgency. Bree needed a replacement quickly, and it had to be developer-friendly, scalable, and suitable for AI-powered product development.

## Choosing Supabase [\#](https://supabase.com/customers/bree\#choosing-supabase)

Bree had long been aware of Supabase. Supabase had earned its reputation among builders and indie developers for its ease of use and instant setup. But what sold Bree was how well Supabase aligned with their long-term technical goals.

> Builders around the world use Supabase for exciting projects. It is so intuitive that developers
> can start building immediately and ship production-ready features in a day.
>
> ![Ryan Han, Head of Engineering and AI, Bree avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fryan-han-bree.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ryan Han, Head of Engineering and AI, Bree

After a thorough evaluation of vendors, Bree chose Supabase for several reasons:

- A fully managed Postgres foundation gave the team the performance and reliability they wanted without having to learn a new language.
- A tightly integrated suite of tools: [Auth](https://supabase.com/auth), [Edge Functions](https://supabase.com/edge-functions), [Vectors](https://supabase.com/modules/vector), and more.
- A rich ecosystems of partners and plugins

> It’s almost the default database for AI-first development. It’s integrated with Lovable, with V0,
> and with Cursor—which we use heavily. Supabase just fits.
>
> ![Ryan Han, Head of Engineering and AI, Bree avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fryan-han-bree.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ryan Han, Head of Engineering and AI, Bree

Performance benchmarks and onboarding experience also played a key role. “Supabase had the best onboarding experience, the best performance benchmarks, and the best developer experience,” said Han.

Even beyond the product, Bree valued Supabase’s commitment to supporting startups. “Their attitude toward startups like us made the whole package very attractive.”

## A thoughtful migration strategy with zero downtime [\#](https://supabase.com/customers/bree\#a-thoughtful-migration-strategy-with-zero-downtime)

Migrating from Fauna’s NoSQL architecture to a relational Postgres database required careful coordination. Bree took a phased approach, designed to minimize disruption, avoid downtime, and ensure full data integrity along the way.

Phase one focused on replicating Fauna’s schemas in Supabase using Postgres `jsonb` columns to accommodate Fauna’s document-style structure. Bree built ETL pipelines and verification scripts to ensure data consistency across both platforms. This dual-write phase ensured every read and write operation was fully synchronized.

Read our blog post on [migrating from Fauna to Supabase](https://supabase.com/blog/migrating-from-fauna-to-supabase).

One of the primary challenges was handling type mismatches. Bree built conversion scripts to synchronize NoSQL data types with Postgres.

Once they verified the sync was intact, Bree were able to switch off Fauna and have Supabase as the main primary database.

Phase two, now underway, is focused on modularizing the data model, splitting large documents into normalized tables. This will allow Bree to take full advantage of Postgres performance and query flexibility.

## 10X performance gains, developer velocity, and a better foundation for AI [\#](https://supabase.com/customers/bree\#10x-performance-gains-developer-velocity-and-a-better-foundation-for-ai)

The results of Bree’s migration to Supabase have been immediate and measurable. Engineers can ship faster, performance is up across the board, and Supabase has become a foundational part of the team’s AI-driven development workflow.

> After migrating to Supabase, we saw immediate lift in developer velocity. Engineers can iterate on
> features much faster by writing Postgres SQL queries.
>
> ![Ryan Han, Head of Engineering and AI, Bree avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fryan-han-bree.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ryan Han, Head of Engineering and AI, Bree

Latency improvements are notable. Bree has observed double-digit reductions in response times across core functions and expects further gains as their architecture is optimized for Supabase.

> It already has double-digit latency improvements. With further optimization, some functions were
> 10x faster.
>
> ![Ryan Han, Head of Engineering and AI, Bree avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fryan-han-bree.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ryan Han, Head of Engineering and AI, Bree

Supabase has also enhanced Bree’s ability to develop AI-first features. They’re able to use the [Supabase MCP Server](https://supabase.com/docs/guides/getting-started/mcp) to power their development in Cursor. As Bree expands its AI initiatives, Supabase’s native support for vector databases and seamless integrations make it the clear choice for long-term scalability.

## Why Supabase? [\#](https://supabase.com/customers/bree\#why-supabase)

Bree’s journey reflects the reasons developers and fast-moving teams choose Supabase:

- **Faster time to market** – Supabase eliminates backend friction, enabling teams to build and ship faster
- **Integrated suite of tools** – Developers get a complete platform including Postgres, Auth, Edge Functions, Vectors, and more
- **AI-native infrastructure** – Supabase supports tools like Cursor and `pgvector` out of the box, making it ideal for AI-powered development
- **Built to scale** – With high availability, backups, and a flexible Postgres foundation, Supabase is ready for growth

> Supabase puts your mind at ease. It has the best support experience I’ve ever seen. It’s a
> disruptive technology to bring to any organization. It’s very worth switching to.
>
> ![Ryan Han, Head of Engineering and AI, Bree avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fryan-han-bree.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ryan Han, Head of Engineering and AI, Bree

## **Ready to build and scale with Supabase?** [\#](https://supabase.com/customers/bree\#ready-to-build-and-scale-with-supabase)

Start your journey today at [www.supabase.com](https://supabase.com/)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)