---
url: "https://supabase.com/features/cdn"
title: "Content Delivery Network | Supabase Features"
---

[Previous feature](https://supabase.com/features/client-library-swift) [Next feature](https://supabase.com/features/supabase-cron)

Stage:

General Availability

Available on self-hosted:

Requires [Cloudflare](https://www.cloudflare.com/)

Supabase's Content Delivery Network (CDN) feature caches and serves assets uploaded to Supabase Storage efficiently across the globe, improving latency for users worldwide.

## Key features

1. Global distribution: Serve content from geographically distributed servers.
2. Origin caching: Cache content from the storage server in your project's region.
3. Intelligent routing: Direct users to the nearest CDN node for faster access.
4. Cache status tracking: Monitor cache hits and misses via the cf-cache-status header.
5. Public and private bucket support: Optimize caching based on bucket privacy settings.

## Benefits:

- Improved performance: Reduce latency by serving content from servers closest to the user.
- Scalability: Handle high traffic loads without straining your main servers.
- Global reach: Deliver content efficiently to users worldwide without managing global infrastructure.
- Enhanced security: Additional layer of protection against DDoS and other application attacks.
- Improved availability: Increase content redundancy through distributed serving.

## The CDN feature is valuable for:

- Media-heavy websites serving large images or video files
- Global applications requiring fast content delivery across different regions
- E-commerce platforms needing to serve product images quickly
- Content publishers distributing large documents or multimedia files
- Any application dealing with large file downloads or streaming

Supabase's CDN significantly improves the performance and user experience of your applications, especially for users accessing large files or media content globally, without the complexity of managing your own CDN infrastructure.

[Read Documentation](https://supabase.com/docs/guides/storage/cdn)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fcdn&text=Content%20Delivery%20Network%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fcdn&text=Content%20Delivery%20Network%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fcdn&t=Content%20Delivery%20Network%20%7C%20Supabase%20Features)

[Client Library - Swift](https://supabase.com/features/client-library-swift) [Cron](https://supabase.com/features/supabase-cron)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)