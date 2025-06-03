---
url: "https://supabase.com/features/database-backups"
title: "Database backups | Supabase Features"
---

[Previous feature](https://supabase.com/features/database-webhooks) [Next feature](https://supabase.com/features/declarative-schemas)

Stage:

General Availability

Available on self-hosted:

Requires [wal-g](https://github.com/wal-g/wal-g)

Supabase offers comprehensive database backup solutions to protect your data and ensure business continuity. These include daily backups and Point-in-Time Recovery (PITR), providing robust safeguards against various disaster scenarios.

## Key features

1. Daily backups: Automatically created for all Pro, Team, and Enterprise plans.
   - Pro: 7 days retention
   - Team: 14 days retention
   - Enterprise: Up to 30 days retention
2. Point-in-Time Recovery (PITR): Available as an add-on for finer granularity.
   - Allows restoration to any point within seconds
   - Achieves a Recovery Point Objective (RPO) of two minutes in worst-case scenarios
3. Backup types:
   - Logical backups: Used for smaller databases (0-15GB)
   - Physical backups: Used for larger databases (>15GB) and projects with PITR or read replicas
4. Flexible restoration options: Restore to a specific daily backup or a precise moment with PITR.
5. Automated process: Backups are managed and monitored by the Supabase team.

## Database backups are crucial for:

- Protecting against accidental data loss or corruption
- Recovering from infrastructure failures
- Meeting regulatory compliance requirements
- Facilitating data migration or cloning for development

Supabase's backup solutions provide a balance of security, flexibility, and ease of use, ensuring your data remains protected and recoverable as your project grows.

[Read Documentation](https://supabase.com/docs/guides/platform/backups)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fdatabase-backups&text=Database%20backups%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fdatabase-backups&text=Database%20backups%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fdatabase-backups&t=Database%20backups%20%7C%20Supabase%20Features)

[Database Webhooks](https://supabase.com/features/database-webhooks) [Declarative Schemas](https://supabase.com/features/declarative-schemas)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Database backups thumbnail](https://supabase.com/_next/image?url=%2Fimages%2Ffeatures%2Fbackups.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Database backups thumbnail](https://supabase.com/_next/image?url=%2Fimages%2Ffeatures%2Fbackups-light.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)