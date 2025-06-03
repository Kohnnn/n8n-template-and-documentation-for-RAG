---
url: "https://supabase.com/blog/organization-based-billing"
title: "Organization-based Billing, Project Transfers, Team Plan"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Organization-based Billing, Project Transfers, Team Plan

31 Aug 2023

•

13 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

[![Kevin Grüneberg avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkevcodez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Kevin GrünebergEngineering](https://github.com/kevcodez)

![Organization-based Billing, Project Transfers, Team Plan](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Forg-billing-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

To simplify our continuously growing platform, we're updating our billing system with some improvements requested by our community. This change provides a more intuitive and industry-aligned approach to billing. We're also laying the groundwork for features like [branching](https://supabase.com/blog/supabase-local-dev#branching-and-preview-environments), rolling out a self-serve [Team Plan](https://supabase.com/pricing), [long-requested](https://github.com/orgs/supabase/discussions/6681) project transfers between organizations, and an extra 1GB of egress on the Free Plan.

We've attempted to keep these changes as simple as possible, offering _more generous_ quotas for the Free Plan. If we missed anything, it's because [billing is hard](https://www.getlago.com/blog/why-billing-systems-are-a-nightmare-for-engineers). We're still committed to our [original goals](https://supabase.com/blog/pricing#goals-for-our-pricing-structure) for predictable pricing.

We've been documenting Kevin's updates to our billing system while it's being used by half-a-million databases:

"No, it's necessary" - Interstellar Docking Scene - 1080p HD - YouTube

L

661 subscribers

["No, it's necessary" - Interstellar Docking Scene - 1080p HD](https://www.youtube.com/watch?v=6ixvpLCdqkA)

L

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=6ixvpLCdqkA "Watch on YouTube")

## Moving from project-based to org-based billing [\#](https://supabase.com/blog/organization-based-billing\#moving-from-project-based-to-org-based-billing)

Supabase has organizations and projects. An organization may contain multiple projects. A project is a Supabase instance. Previously, each project had an individual subscription, plan and add-ons.

![org_billing_before.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Forg-billing-before.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Many of you have expressed your confusion with per-project pricing, the number of invoices and the different ways to manage the subscription.

With this change, we're moving subscriptions to the organization level. Each organization has a single subscription with a single plan (Free, Pro, Team or Enterprise). Project addons such as [compute upgrades](https://supabase.com/docs/guides/platform/compute-add-ons), [custom domains](https://supabase.com/docs/guides/platform/custom-domains) and [PITR](https://supabase.com/docs/guides/platform/backups#point-in-time-recovery) are still configured per project and are added to your organization subscription.

![org_billing_after.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Forg-billing-after.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Additionally, we lay the groundwork for upcoming features like [environment branching](https://supabase.com/blog/supabase-local-dev#branching-and-preview-environments), usage notifications, more sophisticated cost control and much more.

## Quota/Features per organization [\#](https://supabase.com/blog/organization-based-billing\#quotafeatures-per-organization)

With Organization-based Billing, the quotas and features will be granted across your entire organization. Independent of how many projects you launch, your included quota stays the same. For billing purposes, we sum the usage across all projects in a single, monthly invoice.

As the plan is set for your entire organization, upgrading your organization to a paid plan means that you unlock the benefits of the paid plan for **all** projects inside your organizations. For example, if you upgrade to the Pro Plan you get email support for every project inside that org rather than just a single project.

You can launch as many organizations as you want. For example, you can create two organizations on the Pro Plan for $25 each and launch a single project in each. This provides the same quotas and pricing that you'd receive today. Importantly, each subsequent database inside that Organization will cost $0.01344/hour (roughly $10 per month), rather than $25.

Read more about quotas and Organization-based Billing including examples in our [docs](https://supabase.com/docs/guides/platform/billing-on-supabase).

## Free Plan [\#](https://supabase.com/blog/organization-based-billing\#free-plan)

Most importantly, there is only one change that affects the Free Plan: you receive an extra 1GB of egress for free.

| Usage Item | Old plan (project based) | New plan (org based) |
| --- | --- | --- |
| Egress | 4GB (2GB Database + 2GB Storage) | 5GB across Database + Storage |
| Database Space | 500MB | 500MB |
| Storage Space | 1GB | 1GB |
| Monthly Active Users | 50,000 MAU | 50,000 MAU |
| Edge Function Invocations | 500K | 500K |
| Edge Function Count | 10 | 10 |
| Realtime Message Count | 2 million | 2 million |
| Realtime Peak Connections | 200 | 200 |
|  | 2 free projects | 2 "free orgs"<br>(1 free database per org) |

We're giving you an extra 1GB of egress for free and, as an added benefit, it's unified across your org. This means that if you aren't using Supabase Storage, you get even more Database Egress.

If you are currently running 2 free projects however, **this does require some work from you**. Because we are now working on an Org-level, instead of Projects, you will need to:

1. Create a new “Free org”
2. Transfer one of your free projects into the newly-created org

This should be done before the end of October, but don't worry - we'll give you frequent comms and clear instructions once the change has been rolled out (4th Sept).

## No more upfront payments for databases [\#](https://supabase.com/blog/organization-based-billing\#no-more-upfront-payments-for-databases)

Currently, plans include one Micro Compute instance. When you upgrade the [Compute Add-On](https://supabase.com/docs/guides/platform/compute-add-ons), you immediately prepay the prorated amount (days remaining in your current billing cycle), and then pay upfront for the entire month when your billing cycle resets. When you downgrade, you get the appropriate credits for unused time.

Full-month upfront payments are annoying, especially when you just want to do a temporary upgrade. We've heard your feedback and are moving billing for compute to hourly usage.

With Organization-based Billing you won't get an immediate charge upfront when changing compute, instead we'll bill you based on compute hours when your billing cycle resets.

If you launch a second or third instance on your paid plan, it just adds additional compute hours that we'll bill you on.

We only count compute usage for instances that are active. Paused projects do not count towards
compute usage.

To read more about usage-based billing for compute, head over to the [docs](https://supabase.com/docs/guides/platform/manage-your-usage/compute).

## Unified Egress [\#](https://supabase.com/blog/organization-based-billing\#unified-egress)

With Project-based billing, you have different quotas for each service. For example, on the Pro Plan you get 50GB of database egress and 200GB of storage egress included. If you're not using storage at all, you're missing out on the included quota.

In an effort to provide a more fair egress quota for all users, we are unifying egress to be a single usage-based item. You get a total quota, i.e. 250GB on the Pro Plan, that you can use for anything - Storage, Realtime, Auth or Database. You can still see a breakdown of the different types of egress on your organization usage page.

![Unified Egress](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Funified-egress.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Fewer invoices [\#](https://supabase.com/blog/organization-based-billing\#fewer-invoices)

With Project-based billing, each project has an individual billing cycle, so as you create more projects you also create more invoices.

With Organization-based Billing, you receive a single invoice. Launching a new project, removing an old project, and upgrading or downgrading compute no longer triggers additional invoices.

## Project Transfers [\#](https://supabase.com/blog/organization-based-billing\#project-transfers)

A [highly requested feature](https://github.com/orgs/supabase/discussions/6681) since we first launched Supabase has been the ability to transfer projects between organizations. This hasn't been possible due to subscriptions being tied to specific projects. We know a lot of users need to transfer projects and are happy to say that Organization-based Billing will finally make this possible without a manual project migration via pgdump or the CLI.

![Project Transfer Overview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Fproject-transfer-overview.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Read more about [Project Transfers](https://supabase.com/docs/guides/platform/project-transfer).

## Self-Serve Team Plan [\#](https://supabase.com/blog/organization-based-billing\#self-serve-team-plan)

We did a soft launch of the [Team Plan](https://supabase.com/pricing) in June. With the previous billing, it required manual adjustments of the subscriptions as all projects are supposed to be covered by the Team Plan, whereas you're only paying $599 for the plan once. This required Supabase intervention to communicate the confusing state of billing and also do the adjustments. With Organization-based Billing the Team Plan becomes fully self-serve. Users can upgrade a Free/Pro organization to Team Plan or downgrade to a Pro/Free Plan from a Team Plan organization. The main benefits of the Team Plan include:

- Additional Organization member roles
- Daily backups stored for 14 days
- Standardised Security Questionnaire
- SSO for Supabase Dashboard
- Priority email support & SLAs
- 28-day Log retention
- SOC2 Certifications
- HIPAA add-on capability

## Customer Migration Plan [\#](https://supabase.com/blog/organization-based-billing\#customer-migration-plan)

Starting from 4th of September 2023, all new organizations will use Organization-based Billing.

For existing customers, we'll be rolling out Organization-based Billing over the course of a few weeks. We'll automatically migrate those customers not directly affected (i.e. just a single project). Additionally, we'll actively reach out to customers that have multiple projects inside a single organization, as those will have to choose the target plan and whether they want to move projects to different organizations.

### Self-Serve-Migration [\#](https://supabase.com/blog/organization-based-billing\#self-serve-migration)

Shortly after the launch, during the first week of September, you'll be able to initiate the migration to Organization-based Billing yourself. Everyone will be migrated to the new billing eventually, this is just a way to speed things up.

![Self-Serve migration for organization-based billing](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Forg-billing-migration.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Glimpse into the future [\#](https://supabase.com/blog/organization-based-billing\#glimpse-into-the-future)

This is just the start. With this we can now work on:

- **Improved usage stats** \- near real-time stats with deeper drill-down into what exactly is causing usage and how to reduce it.
- **More cost control** \- fine-grained cost-control that will replace the current spend cap.
- **Usage and budget monitoring** \- let users configure alerts that notify users when a certain usage is reached.

There is much much more and we're determined to make billing as seamless, frictionless and transparent as we can.

## FAQs [\#](https://supabase.com/blog/organization-based-billing\#faqs)

What happens to the 2 Free Plan projects?

We are not changing your 2 free project limit. You can have two organizations on a Free Plan with one project each.

What happens to the spend cap?

The spend cap still exists, it's just set on the organization-level and not per project. Head over to your [organization billing settings](https://supabase.com/dashboard/org/_/billing) to toggle your spend cap. We're working on more fine-grained control over costs to supersede the spend cap.

Am I going to pay a different amount?

Most customers will pay less because we are offering more egress for free and it's cheaper to have multiple projects on the Pro Plan in a single organization. We're very conscious about the current users and use-cases. Check our docs for more [detailed breakdown and some examples](https://supabase.com/docs/guides/platform/billing-on-supabase).

Does the migration come with any downtime?

Not at all. There are no service disruptions during the migration, as we're not touching your projects' infrastructure.

## Help, my bill increased! [\#](https://supabase.com/blog/organization-based-billing\#help-my-bill-increased)

This is a major change, and we've tried to design it in a way that's cheaper for everyone. If your bill has increased as a result of this change, that's not our intention. Please submit a Support ticket [on the dashboard](https://supabase.com/dashboard/support/new?category=billing&subject=Organization%20based%20billing) and we'll figure out a solution.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forganization-based-billing&text=Organization-based%20Billing%2C%20Project%20Transfers%2C%20Team%20Plan)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forganization-based-billing&text=Organization-based%20Billing%2C%20Project%20Transfers%2C%20Team%20Plan)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Forganization-based-billing&t=Organization-based%20Billing%2C%20Project%20Transfers%2C%20Team%20Plan)

[Last post\\
\\
**pgvector v0.5.0: Faster semantic search with HNSW indexes** \\
\\
6 September 2023](https://supabase.com/blog/increase-performance-pgvector-hnsw)

[Next post\\
\\
**Launch Week 8 Hackathon Winners** \\
\\
24 August 2023](https://supabase.com/blog/launch-week-8-hackathon-winners)

[supabase](https://supabase.com/blog/tags/supabase)

On this page

- [Moving from project-based to org-based billing](https://supabase.com/blog/organization-based-billing#moving-from-project-based-to-org-based-billing)
- [Quota/Features per organization](https://supabase.com/blog/organization-based-billing#quotafeatures-per-organization)
- [Free Plan](https://supabase.com/blog/organization-based-billing#free-plan)
- [No more upfront payments for databases](https://supabase.com/blog/organization-based-billing#no-more-upfront-payments-for-databases)
- [Unified Egress](https://supabase.com/blog/organization-based-billing#unified-egress)
- [Fewer invoices](https://supabase.com/blog/organization-based-billing#fewer-invoices)
- [Project Transfers](https://supabase.com/blog/organization-based-billing#project-transfers)
- [Self-Serve Team Plan](https://supabase.com/blog/organization-based-billing#self-serve-team-plan)
- [Customer Migration Plan](https://supabase.com/blog/organization-based-billing#customer-migration-plan)
- [Glimpse into the future](https://supabase.com/blog/organization-based-billing#glimpse-into-the-future)
- [FAQs](https://supabase.com/blog/organization-based-billing#faqs)
- [Help, my bill increased!](https://supabase.com/blog/organization-based-billing#help-my-bill-increased)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forganization-based-billing&text=Organization-based%20Billing%2C%20Project%20Transfers%2C%20Team%20Plan)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forganization-based-billing&text=Organization-based%20Billing%2C%20Project%20Transfers%2C%20Team%20Plan)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Forganization-based-billing&t=Organization-based%20Billing%2C%20Project%20Transfers%2C%20Team%20Plan)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Unified Egress](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Funified-egress.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Project Transfer Overview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Fproject-transfer-overview.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Self-Serve migration for organization-based billing](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-31-org-billing%2Forg-billing-migration.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)