---
url: "https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers"
title: "Calendars in Postgres using Foreign Data Wrappers"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Calendars in Postgres using Foreign Data Wrappers

20 Dec 2024

•

6 minute read

[![Bo Lu avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fburmecia.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Bo LuEngineering](https://github.com/burmecia)

![Calendars in Postgres using Foreign Data Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2Fog-calcom.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're releasing Foreign Data Wrappers for [Cal.com](https://cal.com/) so that you can create event bookings directly from Postgres.

This is especially useful for signup forms where you create an event in your database and schedule an event simultaneously: now you can do all this in a single Postgres transaction.

## What's Cal.com? [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#whats-calcom)

[Cal.com](http://cal.com/) is an open-source scheduling platform that allows individuals and businesses to book and manage appointments. It is designed to work with a variety of use cases, from personal calendars to enterprise-grade scheduling systems. They have a great [developer toolkit](https://cal.com/platform).

## Creating event bookings with Postgres [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#creating-event-bookings-with-postgres)

[Cal.com](http://cal.com/) offers various scheduling features. One of the most common scenarios for developers is creating a new event in a calendar (for example, after someone has purchased a flight).

Let's use your Supabase database to create an event in [Cal.com](http://cal.com/), using Postgres Foreign Data Wrappers.

### Set up a Cal.com account [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#set-up-a-calcom-account)

- Sign up on [Cal.com](http://cal.com/)
- Visit [Settings -> Developer -> API keys](https://app.cal.com/settings/developer/api-keys) to create an API key

![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F01-cal-api-key.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Set up a Supabase account [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#set-up-a-supabase-account)

- Sign up on [supabase.com](http://supabase.com/)
- Create a project or open an existing project
- Go to [supabase.com/dashboard/project/\_/database/extensions](https://supabase.com/dashboard/project/_/database/extensions) to enable `wrappers` extension

![enable wrappers extension](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F02-enable-wrapper-ext.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Create Wasm wrapper and a foreign server [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#create-wasm-wrapper-and-a-foreign-server)

Visit [Supabase SQL Editor](https://supabase.com/dashboard/project/_/sql/new), use below SQL to create the Wasm foreign data wrapper:

`
create foreign data wrapper wasm_wrapper
handler wasm_fdw_handler
validator wasm_fdw_validator;
`

And then create a foreign server for [Cal.com](http://cal.com/) connection with your API Key:

`
create server cal_server
foreign data wrapper wasm_wrapper
options (
    fdw_package_url 'https://github.com/supabase/wrappers/releases/download/wasm_cal_fdw_v0.1.0/cal_fdw.wasm',
    fdw_package_name 'supabase:cal-fdw',
    fdw_package_version '0.1.0',
    fdw_package_checksum '4afe4fac8c51f2caa1de8483b3817d2cec3a14cd8a65a3942c8b4ff6c430f08a',
    api_key '<your Cal.com API key>'
);
`

Find the latest version and checksum in the docs:
[fdw.dev/catalog/cal](https://fdw.dev/catalog/cal/)

### Set up foreign tables [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#set-up-foreign-tables)

Now let's setup the foreign tables. First of all, create a dedicate schema for the foreign tables:

`
create schema if not exists cal;
`

And then create a foreign table for [Event Types](https://app.cal.com/event-types):

`
create foreign table cal.event_types (
attrs jsonb
)
server cal_server
options (
    object 'event-types'
);
`

And another foreign table for [Bookings](https://app.cal.com/bookings/upcoming):

`
create foreign table cal.bookings (
attrs jsonb
)
server cal_server
options (
    object 'bookings',
    rowid_column 'attrs'
);
`

Note the `rowid_column` option which is required to insert data into `cal.bookings` table, we will see it later.

### Query Event Types and Bookings from Cal.com [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#query-event-types-and-bookings-from-calcom)

Great, now we are all set, it's time to query some juicy data from Cal.com! Let's start query from [Event Types](https://app.cal.com/event-types) first:

`
-- extract event types
select
etg->'profile'->>'name' as profile,
et->>'id' as id,
et->>'title' as title
from cal.event_types t
cross join json_array_elements((attrs->'eventTypeGroups')::json) etg
cross join json_array_elements((etg->'eventTypes')::json) et;
`

![query event types from Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F03-query-event-types.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Note all the scheduling information returned from [Cal.com](http://cal.com/) API are stored in the JSON column `attrs` , from which we can extract any fields of that object. For example, we can extract `id`, `title`, `name` and etc., from [Bookings](https://app.cal.com/bookings/upcoming) object:

`
-- extract bookings
select
bk->>'id' as id,
bk->>'title' as title,
bk->'responses'->>'name' as name,
bk->>'startTime' as start_time
from cal.bookings t
cross join json_array_elements((attrs->'bookings')::json) bk;
`

![query bookings from Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F04-query-booking.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Oops, it looks like we haven't booked any meetings with anybody yet. Now it's the fun part, let's make a booking on [Cal.com](http://cal.com/) from Supabase!

### Make a bookings on Cal.com from Supabase [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#make-a-bookings-on-calcom-from-supabase)

To make a booking directly from Postgres, all we need to do is to insert a record to `cal.bookings` foreign table, with the booking details in JSON format. For example,

`
-- make a 15 minutes meeting with Elon Musk
insert into cal.bookings(attrs)
values (
'{
     "start": "2025-01-01T23:30:00.000Z",
     "eventTypeId": 1398027,
     "attendee": {
       "name": "Elon Musk",
       "email": "elon.musk@x.com",
       "timeZone": "America/New_York"
     }
}'::jsonb
);
`

![make a bookings from postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F05-make-booking.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Here you can see we made a 15 minutes meeting booking with Elon, just to give him a happy new year greeting 😄. Note the `eventTypeId` , “1398027”, is our `15 Min Meeting` event type ID, you can find yours by querying the `cal.event_types` foreign table using above example SQL.

After inserting the booking record, we can verify it appears on our upcoming list in [Cal.com](http://cal.com/).

![verify bookings is on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F06-verify-on-cal.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

When we query `cal.bookings` again using the previous SQL, we can see our new booking record is in the results as well.

![verify bookings on Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F07-verify-on-supabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

That wraps up our tutorial! We've covered how to interact with [Cal.com](http://cal.com/) in Supabase using foreign wrapper and tables. For more information about available objects and fields, refer to the [Cal.com API v2 reference](https://cal.com/docs/api-reference/v2/introduction) and the [Wrappers Cal.com Wasm Wrapper documentation](https://fdw.dev/catalog/cal/).

## Built with Wrappers [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#built-with-wrappers)

The [Cal.com](http://cal.com/) FDW is built with [Wrappers](https://fdw.dev/), a framework for Postgres Foreign Data Wrappers (FDW). Our latest release supports [Wasm (WebAssembly)](https://webassembly.org/) to simplify development for API-based services.

## Explore more [\#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers\#explore-more)

We've built a variety of wrappers available on [fdw.dev](https://fdw.dev/), ranging from popular tools like [Stripe](https://stripe.com/) and [Notion](https://www.notion.com/) to databases like [ClickHouse](https://clickhouse.com/) and [BigQuery](https://cloud.google.com/bigquery). Check out the [full catalog](https://fdw.dev/catalog/) and get started with Supabase today:

[database.new](https://database.new/)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&t=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)

[Last post\\
\\
**AI Hackathon at Y Combinator** \\
\\
20 December 2024](https://supabase.com/blog/ai-hackathon-at-y-combinator)

[Next post\\
\\
**Supabase Launch Week 13 Hackathon Winners** \\
\\
20 December 2024](https://supabase.com/blog/lw13-hackathon-winners)

[wasm](https://supabase.com/blog/tags/wasm) [wrappers](https://supabase.com/blog/tags/wrappers) [integration](https://supabase.com/blog/tags/integration)

On this page

- [What's Cal.com?](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#whats-calcom)
- [Creating event bookings with Postgres](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#creating-event-bookings-with-postgres)
  - [Set up a Cal.com account](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-a-calcom-account)
  - [Set up a Supabase account](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-a-supabase-account)
  - [Create Wasm wrapper and a foreign server](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#create-wasm-wrapper-and-a-foreign-server)
  - [Set up foreign tables](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-foreign-tables)
  - [Query Event Types and Bookings from Cal.com](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#query-event-types-and-bookings-from-calcom)
  - [Make a bookings on Cal.com from Supabase](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#make-a-bookings-on-calcom-from-supabase)
- [Built with Wrappers](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#built-with-wrappers)
- [Explore more](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#explore-more)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&t=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F01-cal-api-key.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![enable wrappers extension](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F02-enable-wrapper-ext.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![query event types from Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F03-query-event-types.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![query bookings from Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F04-query-booking.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![make a bookings from postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F05-make-booking.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![verify bookings is on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F06-verify-on-cal.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![verify bookings on Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F07-verify-on-supabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)