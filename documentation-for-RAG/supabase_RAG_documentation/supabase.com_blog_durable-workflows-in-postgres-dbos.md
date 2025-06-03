---
url: "https://supabase.com/blog/durable-workflows-in-postgres-dbos"
title: "Running Durable Workflows in Postgres using DBOS"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Running Durable Workflows in Postgres using DBOS

10 Dec 2024

•

6 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Running Durable Workflows in Postgres using DBOS](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fog.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Michael Stonebraker is the inventor of Postgres and a Turing Award winner. His latest venture is [DBOS](https://www.dbos.dev/), a three-year joint research project between Stanford and MIT. The DBOS team have built a Durable Workflow engine using Postgres. It's one of the more elegant designs I've seen, leveraging the features of Postgres to keep it lightweight and fast.

The DBOS team have released a Supabase integration, so you can use your Postgres database as a durable workflow engine.

![DBOS Supabase integration](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdbos-integration.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

**Continue reading or just get started?**

I really love the design of DBOS, so I'm going to write more below. Their design is aligned with our philosophy at Supabase: “just use Postgres”. I'll take you through the lower-level details in the rest of this post. If you just want to get started using DBOS with Supabase, get started using their tutorial:

[Use DBOS With Supabase →](https://docs.dbos.dev/integrations/supabase)

## What's a Durable Workflow engine? [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#whats-a-durable-workflow-engine)

Let's start with a common situation where a workflow is useful: you're running an e-commerce platform where an order goes through multiple “steps”:

![Workflow steps](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdurable-workflow-engine-dark.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The process is simple, but writing a _robust_ program for this is surprisingly difficult. Some potential problems:

- You get to step 2, “Check Inventory”, and you're out of stock. You need to wait 24 hours for the new inventory before you can ship it. You need that “step” to sleep for a day.
- Your program crashes during step 3, “Ship Order”, and it doesn't record that you've shipped the inventory. You end up sending the same order twice.

A Durable Workflow Engine helps with these problems (and more). There are a few on the market that provide different architectures like [Oban](https://oban.pro/), [Trigger.dev](https://trigger.dev/), [Inngest](https://www.inngest.com/), [Windmill](https://www.windmill.dev/), [Temporal](https://temporal.io/), and [AWS Step Functions](https://aws.amazon.com/step-functions/).

DBOS offers a relatively unique approach to Workflows, storing the state in your own Postgres database. Let's explore how DBOS does it.

## What is DBOS? [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#what-is-dbos)

DBOS is a platform where you can write your programming logic in serverless functions (similar to Supabase Edge Functions). Functions can be written in either [Python](https://docs.dbos.dev/python/programming-guide) or [TypeScript](https://docs.dbos.dev/typescript/programming-guide).

### Creating workflows with decorators [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#creating-workflows-with-decorators)

One thing that's different to Supabase Edge Functions is the ability to add **decorators** to your Functions with `DBOS.step()` and `DBOS.workflow()`:

![Python decorators](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdbos-python.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

When you do this, DBOS stores the “state” of every step in Postgres:

![DBOS state in Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdbos-state-in-pg-dark.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This is the part I find the most interesting! If you're a gamer, it's a bit like having a “ [save point](https://en.wikipedia.org/wiki/Saved_game)” in your programs. If a Function fails at any point, a new Function can start, picking up at the last checkpoint.

![DBOS save point](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fsave-final-fantasy.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Storing function state in Postgres [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#storing-function-state-in-postgres)

When you create an application with DBOS, they create a new database inside your Postgres cluster for storing this state.

Using their “Widget Store” example, you can see two new databases -

1. `widget_store`: for storing the application data
2. `widget_store_dbos_sys`: for storing the workflow state.

![Postgres cluster](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdatabases.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The `widget_store_dbos_sys` database holds the workflow state:

![DBOS Schema](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fschema.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### **Workflow logic** [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#workflow-logic)

The DBOS team were kind enough to share some of the logic with me about how their workflow engine works:

1. When a workflow starts, it generates a unique ID and stores it in a Postgres `workflow_status` table with a `PENDING` status. It also stores its inputs in Postgres.
2. Each time a step completes, it stores its output in a Postgres `operation_outputs` table.
3. When a workflow completes, it updates its status in the Postgres `workflow_status` table to `SUCCESS` (or to `ERROR`, if it threw an uncaught exception).

### Error logic [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#error-logic)

If a program is interrupted, on restart the DBOS library launches a background thread that resumes all incomplete workflows from the last completed step.

1. It queries Postgres to find all `PENDING` workflows, then starts each one. Because workflows are just Python functions, it can restart a workflow by simply calling the workflow function with its original inputs, retrieved from Postgres.
2. As a workflow re-executes, before trying each step, it first checks Postgres to see if that step was previously executed. If it finds the step in Postgres, it doesn't re-execute the step, instead re-using its original output.
3. Eventually, the workflow reaches the first step whose output isn't stored in Postgres and resumes execution from there - “resuming from the last completed step.”

All this works because workflows are deterministic, so they can re-execute them using stored step outputs to recover their pre-interruption state.

## The benefits of using Postgres [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#the-benefits-of-using-postgres)

DBOS isn't the first to create a workflow engine. Others in the market include [Temporal](https://temporal.io/) and [AWS Step Functions](https://aws.amazon.com/step-functions/). DBOS provides a number of benefits over workflow engines that use external orchestrators like AWS Step Functions:

### Performance [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#performance)

Because a step transition is just a Postgres write (~1ms) versus an async dispatch from an external orchestrator (~100ms), it means DBOS is [25x faster than AWS Step Functions](https://www.dbos.dev/blog/dbos-vs-aws-step-functions-benchmark):

![Add a message](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fperformance.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Exactly-once execution [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#exactly-once-execution)

DBOS has a special `@DBOS.Transaction` decorator. This runs the entire step inside a Postgres transaction. This guarantees exactly-once execution for databases transactional steps.

### Idempotency [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#idempotency)

You can set an idempotency key for a workflow to guarantee it executes only once, even if called multiple times with that key. Under the hood, this works by setting the workflow's unique ID to your idempotency key.

### Other Postgres features [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#other-postgres-features)

Since it's all in Postgres, you get all the tooling you're familiar with. Backups, GUIs, CLI tools - you name it. It all “just works”.

## Get started [\#](https://supabase.com/blog/durable-workflows-in-postgres-dbos\#get-started)

To get started with DBOS and Supabase, check out their official integration docs:

[Use DBOS With Supabase →](https://docs.dbos.dev/integrations/supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdurable-workflows-in-postgres-dbos&text=Running%20Durable%20Workflows%20in%20Postgres%20using%20DBOS)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdurable-workflows-in-postgres-dbos&text=Running%20Durable%20Workflows%20in%20Postgres%20using%20DBOS)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdurable-workflows-in-postgres-dbos&t=Running%20Durable%20Workflows%20in%20Postgres%20using%20DBOS)

[Last post\\
\\
**How to Hack the Base!** \\
\\
19 December 2024](https://supabase.com/blog/how-to-hack-the-base)

[Next post\\
\\
**database.build v2: Bring-your-own-LLM** \\
\\
6 December 2024](https://supabase.com/blog/database-build-v2)

[integration](https://supabase.com/blog/tags/integration) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [What's a Durable Workflow engine?](https://supabase.com/blog/durable-workflows-in-postgres-dbos#whats-a-durable-workflow-engine)
- [What is DBOS?](https://supabase.com/blog/durable-workflows-in-postgres-dbos#what-is-dbos)
  - [Creating workflows with decorators](https://supabase.com/blog/durable-workflows-in-postgres-dbos#creating-workflows-with-decorators)
  - [Storing function state in Postgres](https://supabase.com/blog/durable-workflows-in-postgres-dbos#storing-function-state-in-postgres)
  - [**Workflow logic**](https://supabase.com/blog/durable-workflows-in-postgres-dbos#workflow-logic)
  - [Error logic](https://supabase.com/blog/durable-workflows-in-postgres-dbos#error-logic)
- [The benefits of using Postgres](https://supabase.com/blog/durable-workflows-in-postgres-dbos#the-benefits-of-using-postgres)
  - [Performance](https://supabase.com/blog/durable-workflows-in-postgres-dbos#performance)
  - [Exactly-once execution](https://supabase.com/blog/durable-workflows-in-postgres-dbos#exactly-once-execution)
  - [Idempotency](https://supabase.com/blog/durable-workflows-in-postgres-dbos#idempotency)
  - [Other Postgres features](https://supabase.com/blog/durable-workflows-in-postgres-dbos#other-postgres-features)
- [Get started](https://supabase.com/blog/durable-workflows-in-postgres-dbos#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdurable-workflows-in-postgres-dbos&text=Running%20Durable%20Workflows%20in%20Postgres%20using%20DBOS)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdurable-workflows-in-postgres-dbos&text=Running%20Durable%20Workflows%20in%20Postgres%20using%20DBOS)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdurable-workflows-in-postgres-dbos&t=Running%20Durable%20Workflows%20in%20Postgres%20using%20DBOS)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![DBOS state in Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdbos-state-in-pg-dark.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![DBOS Supabase integration](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdbos-integration.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Workflow steps](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdurable-workflow-engine-dark.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Python decorators](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdbos-python.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![DBOS save point](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fsave-final-fantasy.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Postgres cluster](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fdatabases.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![DBOS Schema](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fschema.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Add a message](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdbos%2Fperformance.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)