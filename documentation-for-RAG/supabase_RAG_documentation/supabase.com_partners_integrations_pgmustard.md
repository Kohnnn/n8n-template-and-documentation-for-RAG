---
url: "https://supabase.com/partners/integrations/pgmustard"
title: "pgMustard | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![pgMustard](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpgmustard%2Fpgmustard-icon.png&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# pgMustard

![pgMustard](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpgmustard%2Fpgmustard-1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![pgMustard](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpgmustard%2Fpgmustard-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![pgMustard](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpgmustard%2Fpgmustard-3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

Reading EXPLAIN ANALYZE output can be tough.

Even if you know how, Postgres includes so much useful information, it is easy to miss something important. And for queries that do a lot, the plans are even more useful-yet-time-consuming.

pgMustard speeds up your journey from knowing which query is a problem to working out what can be done about it.

## Documentation

This guide explains how to troubleshoot slow queries on Supabase using `explain` and pgMustard.

[pgMustard](https://pgmustard.com/) is a visualization tool for [`explain analyze`](https://www.postgresql.org/docs/current/using-explain.html#USING-EXPLAIN-ANALYZE) that also gives performance tips.

## Step 1: Get the query plan from Supabase

Use `explain analyze` to get a query plan from Postgres. This will run the query behind the scenes, so be careful with data modification queries.

pgMustard requires plans to be in json format, and the buffers, verbose, and settings parameters allow it to give better tips.

So a good prefix for your query would be:

`
explain (analyze, format json, buffers, verbose, settings)
`

Run the query, and copy the output.

![01-supabase-run-query](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/pgmustard/documentation/01-supabase-run-query.png)

If you’re using the Supabase SQL Editor, this is easily copied from the cell titled `QUERY PLAN`, as seen above.

If you have any trouble, check out pgMustard’s guide for [getting a query plan](https://www.pgmustard.com/getting-a-query-plan).

## Step 2: Paste the query plan into pgMustard

Paste the json output into pgMustard and press Submit.

![02-paste-plan-pgmustard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/pgmustard/documentation/02-paste-plan-pgmustard.png)

## Step 3: Look through the top tips and slowest operations

Review the top tips in pgMustard. These are scored on a scale of 0 to 5 stars, based on how much time-saving potential they have (5 stars meaning lots of potential).

![03-review-tips-pgmustard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/pgmustard/documentation/03-review-tips-pgmustard.png)

Click one of the tips, or one of the operations, to see more information.

![04-click-tip-pgmustard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/pgmustard/documentation/04-click-tip-pgmustard.png)

## Step 4: Consider your options

If you get some promising suggestions, you may wish to explore them.

If you don’t get any tips, your query might be quite fast for the amount of work it’s doing.

For the example we saw in Step 3, let's try adding an index on the `customer_name` field in Supabase.

![05-create-index-supabase](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/pgmustard/documentation/05-create-index-supabase.png)

Going through Steps 1-3 again, we now get an efficient index scan, that will scale nicely as our data grows.

![06-check-pgmustard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/pgmustard/documentation/06-check-pgmustard.png)

We could look into why Postgres isn’t choosing to do an index-only scan here, but pgMustard is letting us know that it doesn’t think we’ll gain much by doing so, by scoring the tip 0.3 out of 5.

## Resources

- [pgMustard](https://www.pgmustard.com/) official website.
- [pgMustard explain glossary](https://www.pgmustard.com/docs/explain).

## Details

Watch an introductory video

![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

DeveloperpgMustard Ltd

Category [DevTools](https://supabase.com/partners/integrations#devtools)

Website [www.pgmustard.com](https://www.pgmustard.com/)

Documentation [Learn](https://www.pgmustard.com/)

Third-party integrations and docs are managed by Supabase partners.