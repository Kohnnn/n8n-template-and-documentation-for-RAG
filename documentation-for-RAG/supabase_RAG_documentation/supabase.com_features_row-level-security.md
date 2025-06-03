---
url: "https://supabase.com/features/row-level-security"
title: "Authorization via Row Level Security | Supabase Features"
---

[Previous feature](https://supabase.com/features/ai-integrations) [Next feature](https://supabase.com/features/auto-generated-graphql-api)

Stage:

General Availability

Available on self-hosted:

Yes

Supabase's Row Level Security (RLS) feature allows you to implement granular authorization rules directly in your Postgres database, securing your data at the row level.

## Key features

1. Policy-based access control: Create SQL rules to determine data access for each table.
2. Role-specific policies: Define different access rules for authenticated and anonymous users.
3. Flexible policy types: Implement SELECT, INSERT, UPDATE, and DELETE policies.
4. Integration with Supabase Auth: Use built-in helper functions like auth.uid() and auth.jwt() in policies.
5. Performance optimization: Utilize indexes and optimized query patterns for efficient policy execution.
6. Bypass options: Use service keys or create roles with bypassrls privilege for administrative tasks.

## Benefits:

- Enhanced data security: Control access to individual rows based on user attributes or roles.
- Simplified application logic: Reduce complex authorization checks in your application code.
- Consistency across clients: Ensure uniform access control regardless of data access method.
- Centralized policy management: Define and manage access rules directly in the database.

## RLS is particularly valuable for:

- Multi-tenant applications requiring data isolation
- Healthcare systems needing patient data privacy
- Financial platforms with strict data access controls
- Collaborative tools where users should only see their own or shared data
- Any application dealing with sensitive or personalized data

Supabase's RLS feature provides a powerful tool for implementing sophisticated access control patterns with minimal application code, enhancing security while simplifying development.

[Read Documentation](https://supabase.com/docs/guides/auth/row-level-security)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Frow-level-security&text=Authorization%20via%20Row%20Level%20Security%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Frow-level-security&text=Authorization%20via%20Row%20Level%20Security%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Frow-level-security&t=Authorization%20via%20Row%20Level%20Security%20%7C%20Supabase%20Features)

[AI Integrations](https://supabase.com/features/ai-integrations) [Auto-generated GraphQL API via pg\_graphql](https://supabase.com/features/auto-generated-graphql-api)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)