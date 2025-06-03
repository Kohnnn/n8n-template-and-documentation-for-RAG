---
url: "https://supabase.com/blog/data-api-nearest-read-replica"
title: "Data API Routes to Nearest Read Replica"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Data API Routes to Nearest Read Replica

04 Apr 2025

•

3 minute read

[![José Ledesma avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F52402874%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
José LedesmaEngineering](https://github.com/jose-ledesma)

![Data API Routes to Nearest Read Replica](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-data-api-nearest-rr%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we’re releasing Data API requests routing to the nearest Read Replica by extending our [API load balancer](https://supabase.com/docs/guides/platform/read-replicas#api-load-balancer) to handle geo-routing.

It’s an impactful improvement that will minimize request latency for your globally distributed applications. It’s available by default when using a load balancer endpoint.

## What is geo-routing? [\#](https://supabase.com/blog/data-api-nearest-read-replica\#what-is-geo-routing)

Geo-routing automatically directs your Data API requests to the geographically closest read replica of your database, reducing latency and improving response times for your users around the world.

![Geo-routing diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-data-api-nearest-rr%2Fgeo-routing.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Previously, if you had read replicas in Frankfurt, Singapore, and Virginia, a user located in Europe may experience dramatically different latencies because they could be making requests to any of the replicas.

Our new geo-routing automatically connects users to the nearest read replica so the same user would only make requests to the read replica in the Frankfurt region.

## How geo-routing works [\#](https://supabase.com/blog/data-api-nearest-read-replica\#how-geo-routing-works)

Our geo-routing system uses geospatial algorithms to determine the optimal read replica for each request:

1. Each incoming API request includes geolocation data from the network edge (specifically the `cf.colo` property, which provides the IATA airport code of the datacenter that received the request).
2. We maintain a coordinate mapping system that associates each region where read replicas can be deployed with precise geospatial coordinates.
3. When a request arrives, we calculate the distance between the network edge and each available read replica using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) (which determines the great-circle distance between two points on a sphere using their longitudes and latitudes).
4. The system automatically routes the request to the geographically closest read replica, minimizing network latency without requiring any configuration on your part.
5. In cases where multiple databases exist in the same region we implement a round-robin strategy to ensure balanced load distribution.

The entire process is completely seamless to your application and users, requiring no changes to your code or configuration besides updating your project URL ( `<project_ref>-all.supabase.co`) today.

To get the most from geo-routing, deploy read replicas in regions where your users are concentrated. The more strategically you place your read replicas, the more your users will benefit from reduced latency and improved response times.

## Initial release and roadmap [\#](https://supabase.com/blog/data-api-nearest-read-replica\#initial-release-and-roadmap)

As an initial release, geo-routing is available with the following limitations:

- Currently limited to read-only Data API (PostgREST) requests

If you're already using our API load balancer there's nothing you need to do; geo-routing is automatically applied to your Data API requests.

Otherwise, you can enable this feature by ensuring your project is using the API load balancer endpoint ( `<project_ref>-all.supabase.co`)

We're actively working on expanding geo-routing support to other Supabase products, such as Auth, Storage, and Realtime. Stay tuned for updates.

## Get started today [\#](https://supabase.com/blog/data-api-nearest-read-replica\#get-started-today)

As always, we welcome your feedback, let us know what you think!

- [Sign up for Supabase](https://supabase.com/dashboard/sign-up) and get started today

[Launch Week 14](https://supabase.com/launch-week)

Mar 31 - Apr 04 '25

[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)

[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)

[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)

[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)

[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage

[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)

[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)

[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)

[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)

[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)

[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)

[Community Meetups](https://supabase.com/events?category=meetup)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdata-api-nearest-read-replica&text=Data%20API%20Routes%20to%20Nearest%20Read%20Replica)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdata-api-nearest-read-replica&text=Data%20API%20Routes%20to%20Nearest%20Read%20Replica)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdata-api-nearest-read-replica&t=Data%20API%20Routes%20to%20Nearest%20Read%20Replica)

[Last post\\
\\
**Supabase MCP Server** \\
\\
4 April 2025](https://supabase.com/blog/mcp-server)

[Next post\\
\\
**Declarative Schemas for Simpler Database Management** \\
\\
3 April 2025](https://supabase.com/blog/declarative-schemas)

[launch-week](https://supabase.com/blog/tags/launch-week) [postgrest](https://supabase.com/blog/tags/postgrest)

On this page

- [What is geo-routing?](https://supabase.com/blog/data-api-nearest-read-replica#what-is-geo-routing)
- [How geo-routing works](https://supabase.com/blog/data-api-nearest-read-replica#how-geo-routing-works)
- [Initial release and roadmap](https://supabase.com/blog/data-api-nearest-read-replica#initial-release-and-roadmap)
- [Get started today](https://supabase.com/blog/data-api-nearest-read-replica#get-started-today)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdata-api-nearest-read-replica&text=Data%20API%20Routes%20to%20Nearest%20Read%20Replica)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdata-api-nearest-read-replica&text=Data%20API%20Routes%20to%20Nearest%20Read%20Replica)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdata-api-nearest-read-replica&t=Data%20API%20Routes%20to%20Nearest%20Read%20Replica)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Geo-routing diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-data-api-nearest-rr%2Fgeo-routing.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)