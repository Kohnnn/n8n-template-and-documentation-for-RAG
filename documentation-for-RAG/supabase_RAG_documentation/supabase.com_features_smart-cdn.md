---
url: "https://supabase.com/features/smart-cdn"
title: "Smart Content Delivery Network | Supabase Features"
---

[Previous feature](https://supabase.com/features/server-side-auth) [Next feature](https://supabase.com/features/social-login)

Stage:

General Availability

Available on self-hosted:

Requires [Cloudflare](https://www.cloudflare.com/)

Supabase's Smart CDN automatically synchronizes asset metadata to the edge, ensuring content is quickly delivered and remains up-to-date without manual intervention.

## Key features

1. Automatic cache revalidation: Invalidates CDN cache when assets are changed or deleted.
2. Improved cache hit rate: Shields origin server from unchanged asset requests, even with different query strings.
3. Long-term edge caching: Stores assets on the CDN for extended periods while maintaining freshness.
4. Flexible browser caching: Control browser cache duration using the cacheControl option.
5. Rapid propagation: Changes reflect across global data centers within 60 seconds.
6. Cache bypass option: Use unique query strings to fetch directly from the origin when needed.

## Benefits:

- Content freshness: Users always receive the most recent version of assets.
- Reduced origin load: Minimize requests to the origin server by optimizing edge caching.
- Improved user experience: Deliver fast-loading, up-to-date content globally.
- Cost optimization: Reduce bandwidth costs by serving more content from the edge.

## The Smart CDN feature is valuable for:

- Dynamic websites with frequently updated content
- E-commerce platforms with real-time inventory updates
- News and media sites delivering the latest information
- Applications with rapidly changing user-generated content
- Global platforms requiring both speed and content accuracy

Supabase's Smart CDN optimizes both performance and content accuracy, providing a superior user experience for applications with dynamic or frequently updated content, without the complexity of manual cache management.

[Read Documentation](https://supabase.com/docs/guides/storage/cdn/smart-cdn)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fsmart-cdn&text=Smart%20Content%20Delivery%20Network%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fsmart-cdn&text=Smart%20Content%20Delivery%20Network%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fsmart-cdn&t=Smart%20Content%20Delivery%20Network%20%7C%20Supabase%20Features)

[Server-side Auth](https://supabase.com/features/server-side-auth) [Social login](https://supabase.com/features/social-login)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)