---
url: "https://supabase.com/blog/supabase-functions-updates"
title: "Updates for Supabase Functions"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Updates for Supabase Functions

30 Jul 2021

•

8 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Updates for Supabase Functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffunctions-updates%2Fthumb-supabase-hooks.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The question on everyone's mind - are we launching Supabase Functions? Well, it's complicated.

Today we're announcing _part_ of Functions - Supabase Hooks - in Alpha, for all **new** projects.

We're also releasing support for Postgres Functions and Triggers in our Dashboard, and some timelines for the rest of Supabase Functions.
Let's cover the features we're launching today before the item that everyone is waiting for: Supabase Functions.

## PostgreSQL Functions [\#](https://supabase.com/blog/supabase-functions-updates\#postgresql-functions)

(Not to be confused with Supabase Functions!)

Postgres has built-in support for [SQL functions](https://www.postgresql.org/docs/current/sql-createfunction.html). Today we're making it even easier for developers to build PostgreSQL Functions by releasing a native Functions editor. Soon we'll release some handy templates!

![Postgres Functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffunctions-updates%2Fpostgres-functions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can call PostgreSQL Functions with `supabase-js` using your project API \[ [Docs](https://supabase.com/docs/reference/javascript/rpc)\]:

hideCopy

`
const { data, error } = await supabase.rpc('best_star_wars_series', {
name: 'The Prequels',
})
`

## PostgreSQL Triggers [\#](https://supabase.com/blog/supabase-functions-updates\#postgresql-triggers)

[Triggers](https://www.postgresql.org/docs/current/trigger-definition.html) are another amazing feature of Postgres, which allows you to execute any SQL code after inserting, updating, or deleting data.

While triggers are a staple of Database Administrators, they can be a bit complex and hard to use. We plan to change that with a simple interface for building and managing PostgreSQL triggers.

![Postgres Triggers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffunctions-updates%2Fpostgres-triggers.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Supabase Functions [\#](https://supabase.com/blog/supabase-functions-updates\#supabase-functions)

They say building a startup is like jumping off a cliff and assembling the plane on the way down. At Supabase it's more like assembling a 747 since, although we're still in Beta, thousands of companies depend on us to power their apps and websites.

For the past few months we've been designing Supabase Functions based on our customer feedback.

### BYO Functions, zero lock-in [\#](https://supabase.com/blog/supabase-functions-updates\#byo-functions-zero-lock-in)

A recurring request from our customers is the ability to trigger their _existing_ Functions.
This is especially true for our Enterprise customers, but also Jamstack developers who develop API Functions directly within their stack (like Next.js [API routes](https://nextjs.org/docs/api-routes/introduction), or Redwood [Serverless Functions](https://redwoodjs.com/docs/serverless-functions)).

### Timeline [\#](https://supabase.com/blog/supabase-functions-updates\#timeline)

To meet these goals, we're releasing Supabase Functions in stages:

- _Stage 1:_ Give developers the ability to trigger external HTTP functions - today, using Database Webhooks.
- _Stage 2:_ Give developers the ability to trigger their own Serverless functions on AWS and GCP - Q4 2021.
- _Stage 3:_ Release our own Serverless Functions (Supabase Functions) - Q4 for Early Preview customers.

![Supabase Functions timeline](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffunctions-updates%2Ffunctions-timeline.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Database Webhooks (Alpha) [\#](https://supabase.com/blog/supabase-functions-updates\#database-webhooks-alpha)

(Note: Database Webhooks were previously called "Function Hooks")

Today we're releasing Functions Hooks in `ALPHA`. The `ALPHA` tag means that it is NOT stable, but it's available for testing and feedback. The API will change, so do not use it for anything critical. You have been warned.

Hooks? Triggers? Firestore has the concept of [Function Triggers](https://firebase.google.com/docs/functions/firestore-events), which are very cool.
Supabase Hooks are the same concept, just with a different name.
Postgres already has the concept of [Triggers](https://www.postgresql.org/docs/current/triggers.html), and we thought this would be less confusing[1](https://supabase.com/blog/supabase-functions-updates#user-content-fn-1).

### Hook Events [\#](https://supabase.com/blog/supabase-functions-updates\#hook-events)

Database Webhooks allow you to "listen" to any change in your tables to trigger an asynchronous Function. You can hook into a few different events: `INSERT`, `UPDATE`, and `DELETE`. All events are fired **after** a database row is changed. Keen eyes will be able to spot the similarity to Postgres triggers, and that's because Database Webhooks are just a convenience wrapper around triggers.

![Hook Events](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffunctions-updates%2Fhook-events.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Hook Targets [\#](https://supabase.com/blog/supabase-functions-updates\#hook-targets)

Supabase will support several different targets.

- HTTP/Webhooks: Send HTTP requests directly from your Postgres Database.
- AWS Lambda/Google Cloud Run: Provide Supabase with a restricted IAM role to trigger Serverless functions natively.
- Supabase Functions: We'll develop an end-to-end experience.

![Supabase Database Webhooks](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffunctions-updates%2Fsupabase-function-hooks.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Hook Payload [\#](https://supabase.com/blog/supabase-functions-updates\#hook-payload)

If the target is a Serverless function or an HTTP `POST` request, the payload is automatically generated from the underlying table data. The format matches Supabase [Realtime](https://supabase.com/docs/reference/javascript/subscribe), except in this case you don't a client to "listen" to the changes. This provides yet another mechanism for responding to database changes.

hideCopy

`
type InsertPayload = {
type: 'INSERT'
table: string
schema: string
record: TableRecord<T>
old_record: null
}
type UpdatePayload = {
type: 'UPDATE'
table: string
schema: string
record: TableRecord<T>
old_record: TableRecord<T>
}
type DeletePayload = {
type: 'DELETE'
table: string
schema: string
record: null
old_record: TableRecord<T>
}
`

## Hooks technical design: `pg_net v0.1` [\#](https://supabase.com/blog/supabase-functions-updates\#hooks-technical-design-pg_net-v01)

As with most of the Supabase platform, we leverage PostgreSQL's native functionality to implement Database Webhooks (previously called "Function Hooks").

To build hooks, we've released a new PostgreSQL Extension, [pg\_net](https://github.com/supabase/pg_net/), an asynchronous networking extension with an emphasis on scalability/throughput. In its initial (unstable) release we expose:

- asynchronous HTTP `GET` requests.
- asynchronous HTTP `POST` requests with a JSON payload.

The extension is (currently) capable of >300 requests per second and is the networking layer underpinning Database Webhooks. For a complete view of capabilities, check out [the docs](https://supabase.github.io/pg_net/api/).

### **Usage** [\#](https://supabase.com/blog/supabase-functions-updates\#usage)

`pg_net` allows you to make asynchronous HTTP requests directly within your SQL queries.

`
-- Make a request
select
    net.http_post(
        url:='https://httpbin.org/post',
        body:='{"hello": "world"}'::jsonb
    );
-- Immediately returns a response ID
http_post
---------
        1
`

After making a request, the extension will return an ID. You can use this ID to collect a response.

hideCopy

`
-- Collect the response from a request
select
*
from
net.http_collect_response(1);
-- Results (1 row)
status  | message | response
--------+---------+----------
SUCCESS        ok     (
                        status_code := 200,
                        headers     := '{"date": ...}',
                        body        := '{"args": ...}'
                      )::net.http_response_result
`

You can cast the response to JSON within PostgreSQL:

`
-- Collect the response json payload from a request
select
    (response).body::json
from
    net.http_collect_response(request_id:=1);
`

Result:

noCopy

`
{
"args": {},
"data": "{\"hello\": \"world\"}",
"files": {},
"form": {},
"headers": {
     "Accept": "*/*",
     "Content-Length": "18",
     "Content-Type": "application/json",
     "Host": "httpbin.org",
     "User-Agent": "pg_net/0.1",
     "X-Amzn-Trace-Id": "Root=1-61031a5c-7e1afeae69bffa8614d8e48e"
},
"json": {
     "hello": "world"
},
"origin": "135.63.38.488",
"url": "https://httpbin.org/post"
}
(1 row)
`

### Implementation [\#](https://supabase.com/blog/supabase-functions-updates\#implementation)

To build asynchronous behavior, we use a PostgreSQL [background worker](https://www.postgresql.org/docs/current/bgworker.html) with a [queue](https://github.com/supabase/pg_net/blob/3d52e7758909bb73bf7fa4586f42cea73ed239b6/sql/pg_net--0.1.sql#L11-L19). This, coupled with the [libcurl multi interface](https://curl.se/libcurl/c/libcurl-multi.html), enables us to do multiple simultaneous requests in the same background worker process.

Shout out to [Paul Ramsey](https://github.com/pramsey), who gave us the implementation idea in [pgsql-http](https://github.com/pramsey/pgsql-http/#to-do). While we originally hoped to add background workers to his extension, the implementation became too cumbersome and we decided to start with a clean slate. The advantage of being async can be seen by making some requests with both extensions:

hideCopy

`
\timing on
-- using pgsql-http to fetch from "supabase.io" 10 times
select
    *
from
http_get('https://supabase.com')
cross join
generate_series(1, 10) _;
-- Returns in 3.5 seconds
Time: 3501.935 ms
-- using pg_net to fetch from "supabase.io" 10 times
select
    net.http_get('https://supabase.com')
from
    generate_series (1,10) _;
-- Returns in 1.5 milliseconds
Time: 1.562 ms
`

Of course, the sync version waits until each request is completed to return the result, taking around 3.5 seconds for 10 requests; while the async version returns almost immediately in 1.5 milliseconds. This is really important for Supabase hooks, which run requests for every event fired from a SQL trigger - potentially thousands of requests per second.

### Future/Roadmap [\#](https://supabase.com/blog/supabase-functions-updates\#futureroadmap)

This is only the beginning! First we'll thoroughly test it and make a stable release, then we expect to add support for

- the remaining HTTP methods ( `PUT` / `PATCH`)
- synchronous HTTP
- additional protocols e.g. SMTP, FTP
- more throughput (using epoll)

## Get started today [\#](https://supabase.com/blog/supabase-functions-updates\#get-started-today)

Database Webhooks is enabled today on all [new projects](https://supabase.com/dashboard). Find it under Database > Alpha Preview > Database Webhooks.

![Enable hooks](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffunctions-updates%2Fenable-hooks.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Footnotes [\#](https://supabase.com/blog/supabase-functions-updates\#footnote-label)

1. Postgres also has the concept of [Hooks](https://supabase.com/blog/roles-postgres-hooks), but they're more of an internal concept. [↩](https://supabase.com/blog/supabase-functions-updates#user-content-fnref-1)


Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-functions-updates&text=Updates%20for%20Supabase%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-functions-updates&text=Updates%20for%20Supabase%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-functions-updates&t=Updates%20for%20Supabase%20Functions)

[Last post\\
\\
**The Supabase Hackathon** \\
\\
30 July 2021](https://supabase.com/blog/1-the-supabase-hackathon)

[Next post\\
\\
**Supabase Swag Store** \\
\\
30 July 2021](https://supabase.com/blog/supabase-swag-store)

[launch-week](https://supabase.com/blog/tags/launch-week) [functions](https://supabase.com/blog/tags/functions)

On this page

- [PostgreSQL Functions](https://supabase.com/blog/supabase-functions-updates#postgresql-functions)
- [PostgreSQL Triggers](https://supabase.com/blog/supabase-functions-updates#postgresql-triggers)
- [Supabase Functions](https://supabase.com/blog/supabase-functions-updates#supabase-functions)
  - [BYO Functions, zero lock-in](https://supabase.com/blog/supabase-functions-updates#byo-functions-zero-lock-in)
  - [Timeline](https://supabase.com/blog/supabase-functions-updates#timeline)
- [Database Webhooks (Alpha)](https://supabase.com/blog/supabase-functions-updates#database-webhooks-alpha)
  - [Hook Events](https://supabase.com/blog/supabase-functions-updates#hook-events)
  - [Hook Targets](https://supabase.com/blog/supabase-functions-updates#hook-targets)
  - [Hook Payload](https://supabase.com/blog/supabase-functions-updates#hook-payload)
- [Hooks technical design: `pg_net v0.1`](https://supabase.com/blog/supabase-functions-updates#hooks-technical-design-pg_net-v01)
  - [**Usage**](https://supabase.com/blog/supabase-functions-updates#usage)
  - [Implementation](https://supabase.com/blog/supabase-functions-updates#implementation)
  - [Future/Roadmap](https://supabase.com/blog/supabase-functions-updates#futureroadmap)
- [Get started today](https://supabase.com/blog/supabase-functions-updates#get-started-today)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-functions-updates&text=Updates%20for%20Supabase%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-functions-updates&text=Updates%20for%20Supabase%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-functions-updates&t=Updates%20for%20Supabase%20Functions)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)