---
url: "https://supabase.com/customers/meshy"
title: "Scaling Innovation with Supabase: Meshy’s Migration to Cost-Effective Authentication"
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# Scaling Innovation with Supabase: Meshy’s Migration to Cost-Effective Authentication

Discover how a rapidly growing Meshy migrated from an expensive authentication model with Auth0 to Supabase Auth, and significantly reduced their costs.

![Scaling Innovation with Supabase: Meshy’s Migration to Cost-Effective Authentication logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fmeshy.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Meshy.AI is a cutting-edge startup revolutionizing 3D asset creation. Their AI-powered platform generates high-quality, production-ready 3D models from simple text prompts or images. It transforms workflows for indie game developers and major studios by reducing creation times from weeks to minutes.

[https://www.meshy.ai/](https://www.meshy.ai/)

Use caseUser Authentication, Cost Optimization, Scalability

SolutionsSupabase Auth

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

> Supabase reduced our costs significantly and made our authentication migration seamless and
> scalable. It’s exactly what we needed to support our growing user base.
>
> ![Ye Kuang, CTO at Meshy avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fye-kuang.jpg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ye Kuang, CTO at Meshy

[Meshy](https://www.meshy.ai/) is revolutionizing 3D asset creation by generating high-quality, production-ready 3D models from simple text prompts or an [image to 3D model](https://www.meshy.ai/features/image-to-3d) process. Their cutting-edge AI technology accelerates workflows for indie game developers and major studios by reducing model creation times from weeks to minutes

Discover how a rapidly growing Meshy migrated from an expensive authentication model with Auth0 to Supabase Auth, and significantly reduced their costs.

## The Challenge - Balancing Costs and Scalability for a Rapidly Growing User Base [\#](https://supabase.com/customers/meshy\#the-challenge---balancing-costs-and-scalability-for-a-rapidly-growing-user-base)

Meshy was experiencing significant growth, with its user base expanding by approximately 50,000 new users each month. This rapid increase has led to ~1M registered users and ~100K monthly active users.

### Meshy Tech Stack [\#](https://supabase.com/customers/meshy\#meshy-tech-stack)

Meshy uses a robust and efficient tech stack tailored to its needs as a growing startup. Their backend is built with Go and Python, while their database is PostgreSQL, hosted on AWS, serving both as a traditional database and a task queue for Graphics Processing Unit-based workers. For authentication, they were using Auth0 but now rely on Supabase Auth. On the front end, they leverage Next.js for the application and Three.js for 3D visualization, ensuring a seamless and interactive user experience.

This setup balances reliability, scalability, and performance for their AI-driven 3D asset generation platform.

Previously, they were using Auth0 to manage their authentication needs. While technically sufficient, Auth0’s pricing model proved unsustainable for a startup where most active users were on free trial accounts.

Meshy needed an alternative solution that would:

- Provide reliable authentication at a reasonable cost.
- Support enterprise-level features like SAML 2.0 for centralized identity provider (IDP) integration.
- Offer a seamless migration path with no disruption to existing users.

Auth0’s escalating costs and features suited large enterprises rather than startups with many free user accounts, which made a switch imperative. Meshy needed a solid authentication solution at a reasonable price.

## The Approach: A Smooth Transition from Auth0 to Supabase [\#](https://supabase.com/customers/meshy\#the-approach-a-smooth-transition-from-auth0-to-supabase)

Meshy took a 2-step process to move to Supabase – Selection and Migration.

### Step 1: Selection [\#](https://supabase.com/customers/meshy\#step-1-selection)

Meshy went through a selection process before choosing Supabase, involving:

**Exploring Alternatives**

Meshy considered other authentication providers, including Firebase Auth and AWS Cognito, as part of their evaluation process.

**Discovery**

The team learned about Supabase through online searches related to PostgreSQL and authentication solutions and previous exposure to Supabase in release pipelines at another SaaS company.

**The Decision to Choose Supabase**

Meshy ultimately selected Supabase due to several key factors:

- **Reputation in the Open Source Community:** Supabase’s focus on simplifying PostgreSQL gained significant traction among developers. Supabase was recommended to Meshy through word of mouth.
- **Developer-Friendly Approach:** Supabase aligned well with their needs as a developer-centric startup.
- **Confidence from Customer Stories:** Success stories of other companies migrating from Auth0 to Supabase helped reassure the team about its reliability and suitability.

The combination of features, reputation, and community-driven confidence solidified the decision to migrate to Supabase.

Meshy chose Supabase for its cost-effectiveness, developer-friendly tools, and robust features.

### Step 2: Migration [\#](https://supabase.com/customers/meshy\#step-2-migration)

The entire migration process took around a month. The first two weeks were part-time and involved 3 team members prototyping to validate the migration plan.

The following two weeks involved building production pipelines, migrating the schema, and bulk migration.

Detailed planning ensured the migration went seamlessly, but all existing customers could still log in if there was an issue.

The team built hooks to align account systems between Auth0 and Supabase to prevent user access disruptions.

Metadata, user credentials, and social login data were migrated smoothly, with only minor adjustments for Google login metadata.

Supabase’s clear documentation and support team ensured the migration stayed on schedule, making it a straightforward process compared to the team's previous experiences.

## The Solution - Flexible, Scalable Authentication with Supabase [\#](https://supabase.com/customers/meshy\#the-solution---flexible-scalable-authentication-with-supabase)

The migration to Supabase gave Meshy a developer-friendly, cost-conscious environment with scalable authentication to meet their rapidly growing business needs.

The benefits included:

**Cost Savings**

Supabase’s straightforward pricing model reduced monthly costs from tens of thousands to just a fraction of Auth0’s fees.

**Scalability**

The platform seamlessly supports 500k+ registered users and 100k MAUs without stability issues.

**Future-Ready Features**

Supabase’s support for SAML 2.0 and SOC2 compliance enables Meshy to meet enterprise customer demands.

**Developer-Focused Tools**

The team benefited from streamlined integration and customization, reducing development overhead and long-term maintenance costs.

## The Results - Cutting Costs and Supporting Growth with Supabase [\#](https://supabase.com/customers/meshy\#the-results---cutting-costs-and-supporting-growth-with-supabase)

**Significant Cost Reduction:** Annual authentication expenses dropped drastically, freeing resources for further development.

**Improved Developer Efficiency:** The migration process was quick and effective, saving months of development effort compared to alternatives.

**Enhanced Scalability:** Supabase’s stable infrastructure seamlessly supports Meshy’s growing user base and prepares them for future enterprise features.

## Future Plans [\#](https://supabase.com/customers/meshy\#future-plans)

Now that Meshy have migrated their Auth workloads and experienced the cost savings and scalability benefits, they are exploring other Supabase features such as PgVector.

## Why Supabase? [\#](https://supabase.com/customers/meshy\#why-supabase)

> Supabase delivered exactly what we needed: an affordable, scalable, and developer-friendly
> authentication solution. We’re excited about the opportunities it opens for our growth and
> innovation.
>
> ![Ye Kuang, CTO at Meshy avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fye-kuang.jpg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ye Kuang, CTO at Meshy

### Learn More [\#](https://supabase.com/customers/meshy\#learn-more)

If you’d like to learn how to migrate your users from Auth0 to Supabase Auth, this [webinar](https://supabase.com/events/scale-to-millions-goodtape-auth) and [migration guide will take you through the whole process step by step](https://supabase.com/docs/guides/platform/migrating-to-supabase/auth0).

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)