---
url: "https://supabase.com/blog/event-triggers-wo-superuser"
title: "PostgreSQL Event Triggers without superuser access"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# PostgreSQL Event Triggers without superuser access

08 May 2025

•

4 minute read

[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)

![PostgreSQL Event Triggers without superuser access](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2025-05-08-event-triggers-wo-superuser%2Fcover-event-triggers-dark.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Event Triggers in Postgres are powerful, but only a superuser can create them. In cloud environments, granting superuser access isn't an option.

But thanks to Postgres' extensibility, we can allow regular users to create Event Triggers, in a safe way.

In this blog post, we’ll explain how we do this in the `supautils` extension, using a combination of the Utility Hook and the Function Manager Hook.

## Privileged Role [\#](https://supabase.com/blog/event-triggers-wo-superuser\#privileged-role)

![Utility Hook](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2025-05-08-event-triggers-wo-superuser%2Futility-hook-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The core of `supautils` is the “privileged role”, which is a role that serves as proxy to superuser. It provides a safe subset of superuser capabilities and it’s accessible to regular users.

When the privileged role does a `create event trigger`, we intercept the statement with a Utility Hook ( `ProcessUtility_hook`).
Here we elevate the role to a superuser, continuing the usual flow and allowing the creation on Postgres core. As a last step, we downgrade to the privileged role and make
it the event trigger owner [1](https://supabase.com/blog/event-triggers-wo-superuser#user-content-fn-1).

Creating an event trigger like this is not safe though, as it would allow privilege escalation.

## The privilege escalation problem [\#](https://supabase.com/blog/event-triggers-wo-superuser\#the-privilege-escalation-problem)

Here, a problem arises. Once an Event Trigger is created:

- It targets every role.
- It runs using the target role privileges [2](https://supabase.com/blog/event-triggers-wo-superuser#user-content-fn-2).

This means that a malicious user can create an Event Trigger like:

`
create or replace function become_super()
    returns event_trigger
    language plpgsql as
$$
begin
    alter role malicious SUPERUSER;
end;
$$;
create event trigger bad_event_trigger on ddl_command_end
execute procedure become_super();
`

And once a superuser trips on the event trigger, it will fire with its privileges. Making the malicious user a superuser.

## Skipping Event Triggers [\#](https://supabase.com/blog/event-triggers-wo-superuser\#skipping-event-triggers)

![FMGR Hook](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2025-05-08-event-triggers-wo-superuser%2Ffmgr-hook-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

A solution would be skipping user Event Triggers for superusers.

The Function Manager hook ( `fmgr_hook`) allows us to intercept and modify functions’ execution.

We can intercept the Event Trigger function and replace it with a “noop”. Postgres doesn’t provide a noop function, but we can use the existing `version()` function for the same purpose.

Besides superusers, we also want to skip user event triggers for “reserved roles” [3](https://supabase.com/blog/event-triggers-wo-superuser#user-content-fn-3). These are used for managed services (like `pgbouncer`).

## User Event Triggers [\#](https://supabase.com/blog/event-triggers-wo-superuser\#user-event-triggers)

This now allows users to safely create Event Triggers, without superuser access:

`
-- use the privileged role, which is configured to be "postgres"
set role postgres;
select current_setting('is_superuser'); -- prove it's not a superuser
current_setting
-----------------
off
(1 row)
-- now create the event trigger
create function show_current_user()
returns event_trigger as $$
begin
raise notice 'the event trigger is executed for %', current_user;
end;
$$ language plpgsql;
create event trigger myevtrig on ddl_command_end
execute procedure show_current_user();
-- check it succeeds
create table foo();
NOTICE:  the event trigger is executed for postgres
set role myrole;
create table bar();
NOTICE:  the event trigger is executed for myrole
`

## Future in Postgres core [\#](https://supabase.com/blog/event-triggers-wo-superuser\#future-in-postgres-core)

We would also like to allow regular user event triggers in Postgres core. To this end, we’ve submitted [some patches](https://www.postgresql.org/message-id/flat/CAGRrpzbtYDkg7_xwfzrqByYgCJQbbL38tADyuN%2B6tAkbA-Pnkg%40mail.gmail.com) which are already generating fruitful discussion.

Note that user Event Triggers in Postgres core will likely be more restricted than the `supautils` version.

## Try it out [\#](https://supabase.com/blog/event-triggers-wo-superuser\#try-it-out)

User Event Triggers are now available for new projects on the Supabase platform.

You can also git clone the [supautils repo](https://github.com/supabase/supautils/) and `make install` it in your own deployment.

Finally, we want to give a special shout out to the [Zero Sync](https://zero.rocicorp.dev/) team, who pushed us to release this feature.

* * *

## Footnotes [\#](https://supabase.com/blog/event-triggers-wo-superuser\#footnote-label)

1. This is so the event trigger can be altered or dropped by end users. [↩](https://supabase.com/blog/event-triggers-wo-superuser#user-content-fnref-1)

2. This is not true if you mark the event trigger function as `security definer`, then it will run with the privileges of the function owner. But this is not a usual practice on event triggers, as they usually want to preserve the context of the current user. [↩](https://supabase.com/blog/event-triggers-wo-superuser#user-content-fnref-2)

3. These are configurable. You can read more about reserved roles [here](https://supabase.com/blog/roles-postgres-hooks). [↩](https://supabase.com/blog/event-triggers-wo-superuser#user-content-fnref-3)


Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fevent-triggers-wo-superuser&text=PostgreSQL%20Event%20Triggers%20without%20superuser%20access)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fevent-triggers-wo-superuser&text=PostgreSQL%20Event%20Triggers%20without%20superuser%20access)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fevent-triggers-wo-superuser&t=PostgreSQL%20Event%20Triggers%20without%20superuser%20access)

[Last post\\
\\
**Simplifying back-end complexity with Supabase Data APIs** \\
\\
17 May 2025](https://supabase.com/blog/simplify-backend-with-data-api)

[Next post\\
\\
**Top 10 Launches of Launch Week 14** \\
\\
4 April 2025](https://supabase.com/blog/launch-week-14-top-10)

[postgres](https://supabase.com/blog/tags/postgres) [planetpg](https://supabase.com/blog/tags/planetpg) [event triggers](https://supabase.com/blog/tags/event%20triggers) [extensions](https://supabase.com/blog/tags/extensions)

On this page

- [Privileged Role](https://supabase.com/blog/event-triggers-wo-superuser#privileged-role)
- [The privilege escalation problem](https://supabase.com/blog/event-triggers-wo-superuser#the-privilege-escalation-problem)
- [Skipping Event Triggers](https://supabase.com/blog/event-triggers-wo-superuser#skipping-event-triggers)
- [User Event Triggers](https://supabase.com/blog/event-triggers-wo-superuser#user-event-triggers)
- [Future in Postgres core](https://supabase.com/blog/event-triggers-wo-superuser#future-in-postgres-core)
- [Try it out](https://supabase.com/blog/event-triggers-wo-superuser#try-it-out)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fevent-triggers-wo-superuser&text=PostgreSQL%20Event%20Triggers%20without%20superuser%20access)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fevent-triggers-wo-superuser&text=PostgreSQL%20Event%20Triggers%20without%20superuser%20access)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fevent-triggers-wo-superuser&t=PostgreSQL%20Event%20Triggers%20without%20superuser%20access)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Utility Hook](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2025-05-08-event-triggers-wo-superuser%2Futility-hook-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![FMGR Hook](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2025-05-08-event-triggers-wo-superuser%2Ffmgr-hook-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)