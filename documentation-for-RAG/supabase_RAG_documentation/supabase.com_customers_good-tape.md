---
url: "https://supabase.com/customers/good-tape"
title: "Good Tape migrates to Supabase managed Postgres and Authentication and achieves database efficiency and a 60% cost reduction."
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# Good Tape migrates to Supabase managed Postgres and Authentication and achieves database efficiency and a 60% cost reduction.

Explore how Good Tape achieved remarkable database efficiency and reduced costs by 60% through their successful migration to Supabase's managed services.

![Good Tape migrates to Supabase managed Postgres and Authentication and achieves database efficiency and a 60% cost reduction. logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fgood-tape.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Good Tape is a secure transcription service that makes it easy for journalists and other professionals to turn audio recordings into text, regardless of sound quality and language.

[https://www.goodtape.io](https://www.goodtape.io/)

Use caseGenerative AI, Transcription

SolutionsDatabase, Auth, Realtime, Edge Functions

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

Good Tape started as a hackathon project by Jakob Steinn. The initial idea was to help journalists at Zetland, the news agency where he worked, transcribe their stories from audio to text. In the past, they had done this by hand since existing tools didn't support smaller language areas like Danish. With the help from his colleagues at Zetland, the prototype went from proof of concept on Google Colab, to proper web service leveraging OpenAI's Whisper arriving at the foundation that today is Good Tape.

That was one year ago. The initial hackathon product transformed into Good Tape, which allows users to upload their audio files and instantly get them transcribed by AI.

![Good Tape's home page](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Fgoodtape%2Fgoodtape-website.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## The challenge: Accommodating hyper-growth [\#](https://supabase.com/customers/good-tape\#the-challenge-accommodating-hyper-growth)

Good Tape recently crossed the €1M ARR threshold and is growing +25% MoM. Built with security and privacy in mind, Good Tape has customers in more than 130 countries and has helped journalists in countries like Taiwan, Denmark, and The Netherlands - doing roughly 75,000 transcriptions per week in 98 different languages. The product saves them hours upon hours of manual transcription work and allows for new use cases like categorization and classification of previously inaccessible data. But this hyper-growth also came with its own challenges.

One such challenge was authentication. Good Tape started off with Auth0. When they scaled beyond hobbyist levels, the cost to support auth exploded. From Steinn, "their pricing is absolutely wild."

More importantly, since Steinn was the only full-time developer, Good Tape needed a database solution that didn't put the burden of database debugging and support on their small team. At first, they went with a Postgres database on Fly, which was "not a managed solution but gave all the tools to feel like it was managed." But as they scaled, they started noticing limitations with reliability and performance.

The critical moment for Good Tape came when their primary database went down, and in an event caused by internal network issues, one of their read replicas was promoted to be primary, leaving them with two active leaders. That caused the cluster to go into an irreparable state, from which they could not boot up again.

> As we wanted more reliability, I have had to learn a lot more about databases. And that's
> knowledge that I wish I didn't have to know.
>
> ![Jakob Steinn - Lead Developer at Good Tape avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fjakob-steinn-goodtape.jpeg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Jakob Steinn - Lead Developer at Good Tape

## Why Supabase? [\#](https://supabase.com/customers/good-tape\#why-supabase)

That prompted Steinn to look for a new solution that would allow them to build without having to look over their shoulder at their database. In particular, Supabase's managed database came up as the answer to his database problems of support and uptime. In migrating, Steinn was pleasantly surprised by the support from Supabase both pre- and post-sales.

For the database migration, Kevin Brolly, Head of Customer Success, provided invaluable assistance. Additionally, for the authentication migration, Kevin Grüneberg, Billing Lead, provided guidance [based on his own experience](https://kevcodez.medium.com/migrating-125-000-users-from-auth0-to-supabase-81c0568de307). Both migrations proceeded exceptionally smoothly.

Post migration, Steinn appreciated the communication and safety that Supabase offered. Complex database issues that had previously taken them long engineering hours to identify, plan, and fix were now managed and handled by Supabase. One of which is automatically adding more disk space before it's too late. This allows Steinn and the Good Tape team to focus on their core product.

Further, while implementing Supabase, he was impressed with "the sheer amount of educational content and incredible documentation. It was amazing. So really, really, really great." Beyond just the developer resources, once finished with the migration, Steinn ran a small POC with [Supabase Auth](https://supabase.com/docs/guides/auth). It was then that he found that Supabase could solve their authentication cost issues and also add extra benefits that were impossible if he was working with multiple vendors". The main thing was having our authentication together with our database and seeing the benefits of having those two in the same place. One example is [row-level security](https://supabase.com/docs/guides/auth/row-level-security)… that just sells me immediately."

> My biggest regret is not having gone with Supabase from the beginning.
>
> ![Jakob Steinn - Lead Developer at Good Tape avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fjakob-steinn-goodtape.jpeg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Jakob Steinn - Lead Developer at Good Tape

## The Results [\#](https://supabase.com/customers/good-tape\#the-results)

Good Tape migrated both their Postgres Fly database and Auth0 workloads to Supabase in a single month.

Prior to Supabase, Steinn had spent three months of his time doing nothing but server infrastructure and incident response. With Supabase, he's been able to be entirely hands-off with the database. Moving to Supabase has had the quantitative effect of adding a full-time engineer to the Good Tape team and also the qualitative effect of freeing Steinn to focus on what he loves: building and improving the product.

That includes initiatives like the Good Tape archive, where users can upload any file they want, including 4k Dolby Atmos videos, Good Tape will use Supabase Edge Functions as the translation layer to serve only the audio stream of the uploaded file, such as FLAC, OPUS or MP3. Another feature that Steinn is excited about is the new search capability built on top of pgvector. Supabase has not only enabled Good Tape to save backend engineering time, but it has also broadened the team's ambitions.

In terms of costs, Good Tape has seen a remarkable reduction in backend expenses. Before migrating to Supabase's comprehensive backend solution, they were paying nearly $1,500 per month for authentication through Auth0, and their database-related expenses exceeded $2,600 per month with Fly. With the transition to Supabase, they not only lowered their total costs to $1,600, resulting in a 60% reduction in expenses, but they also saved valuable engineering time that allowed them to focus on their core product.

The best part for Steinn has been the peace of mind with Supabase's managed services. Where in the past, his vacations had always been interrupted - "Every time I was in an airport, our database would go down". With Supabase now managing the database, Steinn can visit friends and family in Iceland without any concerns.

> Moving to Supabase has saved the company. We wouldn't have worked if we hadn't made the right
> \[backend\] decision… So Supabase helped us stay in production and not become an internal tool.
>
> ![Jakob Steinn - Lead Developer at Good Tape avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fjakob-steinn-goodtape.jpeg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Jakob Steinn - Lead Developer at Good Tape

> To learn more about how Supabase can help you manage and scale your database, **[reach out to us](https://forms.supabase.com/enterprise)**.

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)