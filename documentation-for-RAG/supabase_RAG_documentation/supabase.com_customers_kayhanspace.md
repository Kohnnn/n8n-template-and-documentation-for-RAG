---
url: "https://supabase.com/customers/kayhanspace"
title: "Kayhan Space | Supabase Customer Stories"
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# Kayhan Space saw 8x improvement in developer speed when moving to Supabase

The Kayhan Space team migrated to Supabase from Amazon RDS and Auth0 to simplify infrastructure and unlock developer velocity.

![Kayhan Space saw 8x improvement in developer speed when moving to Supabase logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fkayhanspace.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Making spaceflight safer

[https://kayhan.space](https://kayhan.space/)

FoundedUnited States

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

> It’s literally a night and day difference. With Supabase and Next.js, it’s been very smooth and
> very fast to get new features out.
>
> ![Hyun S., Chief Product Officer, Kayhan Space avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fhyun-kayhanspace.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Hyun S., Chief Product Officer, Kayhan Space

[Kayhan Space](https://kayhan.space/) is a software-first aerospace company building tools to help satellite operators make more intelligent and safer actions in orbit. Their flagship product, [Satcat](https://www.satcat.com/), alerts users of potential close approaches, displays real-time orbital data, and helps operators plan collision-avoidance maneuvers and coordinate with one another. After consolidating their commercial and government tools into Satcat, they re-architected their stack using Supabase to accelerate development, improve scalability, and streamline authentication.

## The challenge [\#](https://supabase.com/customers/kayhanspace\#the-challenge)

Kayhan Space originally built their systems using Amazon RDS for data storage and Auth0 for authentication. As they transitioned from enterprise-only sales to a hybrid B2B and B2C model, they needed a platform that could:

- Handle self-serve onboarding for thousands of public users
- Support complex access control for sensitive government and commercial data
- Accelerate development and reduce cross-functional overhead between frontend and backend teams
- Scale seamlessly with public interest, especially during unexpected traffic spikes

They also faced significant friction with their previous stack:

- Auth0’s pricing model and B2B-B2C transition were inflexible
- RDS required additional tooling for simple access patterns
- Non-engineering staff needed access to data
- Developer productivity was limited by the fragmented nature of AWS services

## Choosing Supabase [\#](https://supabase.com/customers/kayhanspace\#choosing-supabase)

When Satcat moved from prototype to production, Kayhan Space chose Supabase as the backbone of their new stack. The decision was driven by several key factors:

- **All-in-one platform**: Supabase offered a [managed Postgres database](https://supabase.com/database), built-in [Auth](https://supabase.com/auth), and a powerful dashboard in one place
- **Ease of use**: Connecting OAuth providers and managing privileged access was simple, even for non-engineers
- **Row-Level Security**: RLS allowed them to enforce complex, multi-tenant data access controls at the database level
- **Familiar stack**: Supabase worked seamlessly with their frontend in Next.js and enabled rapid prototyping without backend bottlenecks

> Supabase felt like a restaurant kitchen where all the tools are organized and ready to go. Even I
> use it daily to check signups and debug issues without touching the command line.
>
> ![Hyun S., Chief Product Officer, Kayhan Space avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fhyun-kayhanspace.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Hyun S., Chief Product Officer, Kayhan Space

## The approach [\#](https://supabase.com/customers/kayhanspace\#the-approach)

Kayhan Space began using Supabase for lightweight prototyping—just login and data persistence. As Satcat became the company’s core focus, they doubled down on Supabase:

- Migrated from RDS and Auth0 to Supabase Database and Supabase Auth
- Used RLS extensively to isolate data access across different product tiers and types of users
- Implemented JSON-based storage patterns where flexibility was needed, like trajectory planning
- Shifted from RPCs to direct SQL queries in their Next.js app for performance and simplicity
- Integrated with Grafana for monitoring and analytics

The transition was fast and developer-friendly, enabling frontend engineers to build features independently without constantly relying on backend changes.

## The results [\#](https://supabase.com/customers/kayhanspace\#the-results)

- **8x increase in development speed** after consolidating tools and adopting Supabase
- **Zero downtime with Supabase** during a major traffic spike (tens of thousands of users in three days) sparked by public interest in a re-orbiting Soviet satellite
- **Improved collaboration** between frontend and backend teams due to tight coupling between Supabase and Next.js
- **Real-time observability** via custom dashboards to monitor user behavior and system health
- **Support for large datasets**, including time series and historical orbital trajectories for over 60,000 satellites

Supabase has become part of the daily workflow for both engineers and product leadership. Even non-technical team members use the dashboard to inspect user activity and debug UI issues.

## Future outlook [\#](https://supabase.com/customers/kayhanspace\#future-outlook)

Kayhan Space plans to continue expanding Satcat for both public and enterprise users. On the technical side, their roadmap includes:

- Scaling read performance with Supabase Read Replicas
- Continuing to explore Postgres-based spatial, geospatial indexing, and time series capabilities
- Building additional features that rely on Supabase’s RLS and database extensibility

As they grow, Supabase will remain a foundational layer in their mission to make space safer and more transparent for operators and the public.

> We didn’t even entertain self-hosting. Supabase just worked, right out of the box. It saved us so
> many engineering hours.
>
> ![Hyun S., Chief Product Officer, Kayhan Space avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fhyun-kayhanspace.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Hyun S., Chief Product Officer, Kayhan Space

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)