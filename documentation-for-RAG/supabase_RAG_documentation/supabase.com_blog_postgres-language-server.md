---
url: "https://supabase.com/blog/postgres-language-server"
title: "Postgres Language Server: Initial Release"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Postgres Language Server: Initial Release

29 Mar 2025

•

17 minute read

[![Philipp Steinrötter avatar](https://supabase.com/_next/image?url=%2Fimages%2Fphilipp-steinrotter.jpg&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Philipp SteinrötterGuest Author](https://twitter.com/psteinroe)

[![Julian Domke avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F68325451%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Julian DomkeGuest Author](https://x.com/juleswritescode)

![Postgres Language Server: Initial Release](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-postgres-language-server%2Fpostgres-language-server-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we’re announcing the initial release of Postgres Language Server - a Language Server Protocol (LSP) implementation for Postgres and a collection of language tools focusing on reliable SQL tooling and developer experience.

![Postgres Language Server demo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-postgres-language-server%2Fpostgres-language-server-demo.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This initial release supports the following:

- Autocompletion
- Syntax Error Highlighting
- Type-checking (via [EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html) error insights)
- Linter, inspired by [Squawk](https://squawkhq.com/)

The Language Server is available via:

- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=Supabase.postgrestools)
- Neovim (via [`nvim-lspconfig`](https://github.com/neovim/nvim-lspconfig/blob/master/lua/lspconfig/configs/postgres_lsp.lua) + [`mason`](https://github.com/mason-org/mason-registry/blob/main/packages/postgrestools/package.yaml))

You can also install the CLI from:

- [GitHub Releases](https://github.com/supabase-community/postgres-language-server/releases) (precompiled binaries)
- npm ( [`@postgrestools/postgrestools`](https://www.npmjs.com/package/@postgrestools/postgrestools))

For more details, check out [our documentation](https://pgtools.dev/) or the [GitHub repo](https://github.com/supabase-community/postgres-language-server). We would love for the community’s support by reporting issues and contributing documentation.

Getting to the initial release has been a 2-year-long journey. We have learned Rust, spent weeks on research and iterations, dug our way out of rabbit holes, and made friends along the way. We have also discarded most of what we so proudly wrote about in the previous blog post [Postgres Language Server: implementing the Parser](https://supabase.com/blog/postgres-language-server-implementing-parser) – but more on that later.

Below is a mix of what we've come up with, challenges we've encountered, and where we'll go from here.

Let's dive in.

## The Architecture of a Language Server [\#](https://supabase.com/blog/postgres-language-server\#the-architecture-of-a-language-server)

The most important decision when implementing a Language Server is the architecture of the underlying data model, which greatly depends on the language itself.

For example, C++ supports header files and has a declaration-before-use rule. That's why the Language Server can compile headers once and cache them. When you type within a file, the compiler restarts from just after the header section of that file. All other files and headers are read from cache, so the compilation unit is reasonably small.

`
// start of header. iostream is parsed and analyzed once.
#include <iostream>
// end of header
// if the user types below, we just have to re-analyze three lines.
// Everything else, including types and definitions from other files,
// can be read from cache.
void main() {
std::cout << "Hello, World!" << std::
}
`

Types are usually defined within the codebase and resolved from there. In the TypeScript example below, the Language Server first has to compile `foo.ts` and launch a database containing `Foo` so it can resolve the type of `bar`.

`
// foo.ts
export type Foo = {
bar: string
}
// bar.ts
import { Foo } from './foo'
const bar: Foo = { bar: 'I am a string' }
`

Many languages use variations of this.

But for most parts of Postgres (or any SQL dialect, really), the rules are different: While types can be defined within the source code (e.g., within a migration file by using [declarative schema management](https://supabase.com/docs/guides/local-development/declarative-database-schemas)), the database itself is the single source of truth, and there is no relation between files.

Besides, the variety of schema and migration management tools employed today means we cannot make assumptions about how the source code is structured and whether it reflects the current state.

For our Postgres Language Server, we can therefore assume that

- The smallest unit of compilation is a single statement
- The database schema is the single source of truth for any type information
- All statements are independent: To make sense of any statement, we only need to parse said statement, and nothing else

## Technical Challenges [\#](https://supabase.com/blog/postgres-language-server\#technical-challenges)

For this project, the most challenging part is the parser – both when initially parsing the document and when processing user input.

As laid out in a [previous blog post](https://supabase.com/blog/postgres-language-server-implementing-parser), implementing a parser for Postgres is hard because of the ever-evolving and complex syntax of Postgres. It's also one of the reasons why existing Postgres tooling is scarce, hardly maintained, and often does not work very well.

This is why we decided not to create a custom parser. Instead, we leverage the existing [libpg\_query](https://github.com/pganalyze/libpg_query) library to parse SQL code reliably. The pganalyze team has published a great blog post on [why this approach is preferred](https://pganalyze.com/blog/parse-postgresql-queries-in-ruby).

However, `libpg_query` is designed to parse _executable_ SQL — not to provide language intelligence. This limitation posed several challenges, requiring us to find pragmatic solutions along the way. The biggest challenge of this project has been (and continues to be) resisting the urge to chase perfection, avoiding unnecessary complexity, and prioritizing practical solutions instead.

Let’s explore some of these solutions by walking through the document lifecycle.

## Document Lifecycle [\#](https://supabase.com/blog/postgres-language-server\#document-lifecycle)

The document lifecycle is at the core of every Language Server. It describes how we turn raw text input into a model of the code, provide language-specific smarts back to the client, and then efficiently process changes to do it all again, and fast.

To understand how everything works, let’s see how a document is processed.

## Splitting the Source [\#](https://supabase.com/blog/postgres-language-server\#splitting-the-source)

Whenever a user opens a new document, we first run it through our custom statement splitter.

It is responsible for cutting a SQL file with potentially invalid or incomplete statements into individual statements. We need this because the `libpg_query` parser is built to parse _executable_ SQL – it will return an error on the first invalid token it encounters. When we first cut the SQL file, we can run the parser on each statement individually. If a statement cannot be parsed, we report the syntax error to the user.

At first, we spend months trying to chase perfection by implementing a “light” Postgres parser.

The idea was to just care about the tokens that are distinct for a specific statement. For example, if we saw a `CREATE` token followed by a `FUNCTION` token, we could be relatively sure this was going to be a `CREATE FUNCTION` statement, and we could expect `(` and `)` to follow it. This approach almost worked, but eventually became a rabbit hole of never ending edge-cases (damn you, recursion!).

We had once again learned an important lesson: If anything requires an implementation per statement type or per syntax element, we better find another way.

After some time off, we decided to make another attempt focusing on the simplest approach.

The goal was to make the statement splitter work well for 80% of cases, and to provide a reasonable fallback for the rest. Inspired by [this blog post by matklad](https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html), we implemented a simple Pratt Parser.

The splitter now tries to be “smart” about common statement types. For example, it knows that a `SELECT` cannot be followed by another `SELECT`, unless the latter is within a sub-statement. Hence, the following is cut into two statements:

`
SELECT a FROM (SELECT a FROM b) sub WHERE
SELECT 1;
-- is cut into
SELECT a FROM (SELECT a FROM b) sub WHERE
--
SELECT 1;
`

We hope that this custom implementation will suffice for 80% of use cases.

For everything else, we’ve built a simple fallback: We always split statements at semi-colons or double newlines. This means that the following works, too – it will be cut into two statements, and we report a syntax error for the first.

`
i like to use my sql file as a notepad -- Error!
select 1;
`

There might still be cases we did not think about - which is where we need your help: please try it out and report any issues you find. If our solution is not good enough, we will go back to the drawing board.

## Identifying Statements [\#](https://supabase.com/blog/postgres-language-server\#identifying-statements)

After we split the SQL source into separate statements, we store each statement's range and assign it an identifier that is unique within the document. Outside a document, a statement is then identified by the path of the document and its statement ID.

`
/// Globally unique statement
#[derive(Hash)]
pub(crate) struct Statement {
/// Path of the document
pub(crate) path: PgTPath,
/// Unique id within the document
pub(crate) id: StatementId,
}
`

We use a hash of the `Statement` struct to cache per-statement results (e.g. diagnostics) in our workspace. Since the statement can change over time, the cache key does not include the text or the range of the statement.

## Parsing the Statements [\#](https://supabase.com/blog/postgres-language-server\#parsing-the-statements)

Now that we have identified the document's statements, we can parse them into workable data structures.

To do this, we run both `tree-sitter` and `libpg_query` on them.

`libpg_query` provides precise parsing, helps to detect syntax errors, extracts statement types, and analyzes their structure for diagnostics and linting. But it cannot handle invalid or incomplete SQL, which often appears during live editing.

This is where `tree-sitter` comes in. While not as precise, it can always produce a syntax tree, even for malformed statements. This is very useful, especially for handling incomplete statements in autocompletion.

With both parsers combined, we get accurate results for valid SQL and can also deal with incomplete input. The idea to use `tree-sitter` in addition to `libpg_query` came from [a comment on our previous Hacker News post](https://news.ycombinator.com/item?id=38570680), so thank you for that:

![Hacker News comment](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-postgres-language-server%2Fhacker-news-comment.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Ironically, the parser we wrote [an entire blog post about](https://supabase.com/blog/postgres-language-server-implementing-parser) isn't even in use anymore.

It did enable us to pin-point the exact location of a node within the abstract syntax tree (AST). For example, in the following statement, we could show the diagnostics only on `DROP COLUMN test` instead of the entire `ALTER TABLE` statement:

`
ALTER TABLE contact
	DROP COLUMN test,
	ALTER COLUMN another DROP NOT NULL;
`

While that is certainly a nice feature, the implementation effort was simply not justified. We might revisit it later, but for now, we've decided that the combination of `libpg_query` and `tree-sitter` is good enough.

With this and the statement splitter, we are coming out of a deep rabbit hole with a clearer path ahead of us.

## Loading Schema Information [\#](https://supabase.com/blog/postgres-language-server\#loading-schema-information)

Now that we have opened a document and parsed its statements, the missing piece for analysis is schema information.

To provide this, we lazily populate a schema cache. Similar to PostgREST, this cache is a simple in-memory data structure that stores details about tables, columns, functions, and other schema elements.

`
pub struct SchemaCache {
pub schemas: Vec<Schema>,
pub tables: Vec<Table>,
pub functions: Vec<Function>,
pub types: Vec<PostgresType>,
pub versions: Vec<Version>,
pub columns: Vec<Column>,
}
`

We only load the schema cache when it is first needed (e.g. for autocompletion). Once loaded, we keep it in memory, ensuring that schema data is available without unnecessary overhead. If no database connection is configured, we can't load any schema information, so we simply disable features requiring that.

## Providing Diagnostics [\#](https://supabase.com/blog/postgres-language-server\#providing-diagnostics)

When the client asks for diagnostics, we load all statements alongside their ranges and text content from a document. With the statement identifier, we check if the `libpg_query` AST is available. If it is not available, we collect the emitted syntax errors instead. If it is available, on the other hand, we pass it to both the type checker and the linter.

Again, the type checker is very simple: Since we maintain a database connection, we can just ask Postgres to do the heavy lifting by `PREPARE`-ing the statement. If the statement contains a type issue, such as a missing column, the error is returned as diagnostics to the user.

Our linter is heavily inspired by [Squawk](https://squawkhq.com/). It takes the AST emitted by `libpg_query` and runs all configured rules on them. We spent some time optimizing the infrastructure of the linter in order to lower the barrier of contributing new rules and ask that the community [can support us there](https://github.com/supabase-community/postgres_lsp/issues/131).

In the end, providing diagnostics happens without noticeable delay for the user (we promise the GIF was not edited 🤞):

![Fast diagnostics](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-postgres-language-server%2Ffast-diagnostics.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Processing Changes [\#](https://supabase.com/blog/postgres-language-server\#processing-changes)

Now that we've successfully reported diagnostics, the user will want to fix the issues.

For an IDE to feel responsive, these changes must be processed within milliseconds. To achieve this, we take advantage of the fact that all SQL statements are independent of each other, which allows us to invalidate only those statements that have actually changed.

If you want to dive deeper into how snappy IDEs are built, check out [this blog\\
post](https://rust-analyzer.github.io/blog/2020/07/20/three-architectures-for-responsive-ide.html).

Let’s look at an example.

`
select first from test;
select seond from test; -- a typo we want to fix
select third from test;
`

The last time we checked, "second" was spelled somewhat differently, so that's a typo we need to fix. Before going ahead and adding the missing `c`, we need to understand how text files are usually stored and processed in IDEs.

From the user’s perspective, inserting a character simply makes the current line longer. However, an IDE doesn’t inherently work with lines—it instead processes raw strings that may contain `\n` characters. When a character is inserted, everything after the cursor position shifts to the right, affecting not only the current line, but the subsequent lines as well.

In our case, this means we need to update the ranges of all affected statements. Since SQL statements are independent, we know that:

- Statements before the change remain unaffected.
- The modified statement expands to fit the new character.
- Statements after the modification are shifted "to the right" by one character.

When we fix the typo, this is the corresponding diff:

`
--- old.sql	2025-03-27
+++ new.sql	2025-03-27
@@ -1,3 +1,3 @@
select first from test; -- no changes
-select seond from test;
+select second from test; -- range extended by 1 character
select third from test; -- moved right by 1 character
`

As mentioned before, each statement in the document is assigned a unique ID, and we store only their ranges. So, when processing this change, we do need to create a new entry for the modified statement, since its content has changed – but for the third statement, simply updating its stored range is enough, meaning we don’t need to invalidate its cache! The AST does not need to be re-parsed.

The above example is intentionally simplified. There are other cases to consider, such as edits occurring **between** two statements, or merging two statements into one. However, the basic gist remains: identify all modified statements, replace the affected ones, and for those that come afterward, simply update their ranges.

## Responsive Autocompletion [\#](https://supabase.com/blog/postgres-language-server\#responsive-autocompletion)

The one feature where developers will truly notice efficient change processing is autocompletion, so we try to be as efficient as possible providing suggestions.

Since autocompletion is primarily needed for incomplete statements, we cannot use `libpg_query`.
We rely only on `tree-sitter` for parsing.

When you change a character in your `SELECT` clause, we update the existing `tree-sitter` Concrete Syntax Tree (CST) instead of re-parsing it. We then read the relevant suggestion types (columns, tables, etc.) from our `SchemaCache` , so no database query is necessary. This approach of updating and reading from existing data structures lets us provide suggestions without any noticeable delay. (Some would call it – drumroll – "blazingly fast".)

In order to choose which suggestions are the most relevant, we take the changed node and the CST and then iterate over the possible items using a simple scoring algorithm.

Some examples:

- If the changed node is within a `SELECT` clause, it would not make sense to suggest a table name. We reduce those items' score.
- If the changed node contains the "public" schema name, it would not make sense to suggest a table from the "private" schema. We reduce those items' score.
- If the CST contains a `FROM` clause, it would make sense to suggest columns belonging to the queried table. We increase those columns' scores.

While the hard part is gathering the information about the current statement, the actual scoring code is as simple as it gets:

``
fn check_matches_schema(
/// `self` is the currently investigated suggestion item.
	&mut self,
/// `ctx` contains the information about the changed CST node and the
/// containing statement.
	ctx: &CompletionContext
) {
let schema_name = match ctx.schema_name.as_ref() {
    None => return,
    Some(n) => n,
};
let data_schema = self.get_schema_name();
if schema_name == data_schema {
    self.score += 25;
} else {
    self.score -= 10;
}
}
``

Once we've investigated all relevant items, we filter out those not meeting a threshold, sort them by score, and return the first 50 to the user.

It will take some time to dial in the scoring mechanism so that the completion suggestions feel intuitive and relevant, but this approach will take us there.

## Not Just a Language Server [\#](https://supabase.com/blog/postgres-language-server\#not-just-a-language-server)

This entire blog post (and the first 18 months of the project) focused primarily on the Language Server. It's arguably the most prominent use case and remains our highest priority.

However, our vision for this project is larger: We want to create a home for all the great Postgres tooling out there, build the missing pieces, and make everything as accessible as possible. Therefore, the Language Server is just one out of many entry points. We've already built a client-server architecture that allows our workspace API to be used anywhere:

- from the CLI by running `postgrestools check test.sql`
- behind a HTTP API
- (hopefully soon) from Wasm right in your browser.

This approach is _heavily_ inspired by (and borrows a lot from) [Biome](https://github.com/biomejs/biome). Without their sophisticated and well-structured codebase, we wouldn’t have been able to implement an entire toolchain infrastructure this quickly over the past months. Cheers to Open Source!

## What’s Next [\#](https://supabase.com/blog/postgres-language-server\#whats-next)

Over the next few weeks, we'll focus on improving reliability.

The Language Server still has a few hiccups, so we want to make the current toolset as frictionless as possible before we work on any more features.

Once we're happy with the results, we'll try to make the Postgres LSP accessible to more people by:

- writing installation guides
- publishing extensions for other editors
- writing documentation to enable future contributors

If you want, you can already help us by installing the Language Server and reporting any issues we might have overlooked, or you could suggest features that we should implement later on (we're currently planning PL/pgSQL support, a Wasm build for [pglite](https://github.com/electric-sql/pglite), and parsing SQL function bodies).

We also added a few [issues](https://github.com/supabase-community/postgres_lsp/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen) to our [repository](https://github.com/supabase-community/postgres_lsp) for anybody who wants to contribute by writing code. Any kind of help is highly appreciated!

Happy coding! 🧀

[Launch Week 14](https://supabase.com/launch-week)

Mar 31 - Apr 04 '25

[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)

[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)

[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)

[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)

[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage

[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)

[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)

[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)

[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)

[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)

[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)

[Community Meetups](https://supabase.com/events?category=meetup)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server&text=Postgres%20Language%20Server%3A%20Initial%20Release)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server&text=Postgres%20Language%20Server%3A%20Initial%20Release)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server&t=Postgres%20Language%20Server%3A%20Initial%20Release)

[Last post\\
\\
**Supabase Auth: Bring Your Own Clerk** \\
\\
31 March 2025](https://supabase.com/blog/clerk-tpa-pricing)

[Next post\\
\\
**Migrating from Fauna to Supabase** \\
\\
21 March 2025](https://supabase.com/blog/migrating-from-fauna-to-supabase)

[launch-week](https://supabase.com/blog/tags/launch-week) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [The Architecture of a Language Server](https://supabase.com/blog/postgres-language-server#the-architecture-of-a-language-server)
- [Technical Challenges](https://supabase.com/blog/postgres-language-server#technical-challenges)
- [Document Lifecycle](https://supabase.com/blog/postgres-language-server#document-lifecycle)
- [Splitting the Source](https://supabase.com/blog/postgres-language-server#splitting-the-source)
- [Identifying Statements](https://supabase.com/blog/postgres-language-server#identifying-statements)
- [Parsing the Statements](https://supabase.com/blog/postgres-language-server#parsing-the-statements)
- [Loading Schema Information](https://supabase.com/blog/postgres-language-server#loading-schema-information)
- [Providing Diagnostics](https://supabase.com/blog/postgres-language-server#providing-diagnostics)
- [Processing Changes](https://supabase.com/blog/postgres-language-server#processing-changes)
- [Responsive Autocompletion](https://supabase.com/blog/postgres-language-server#responsive-autocompletion)
- [Not Just a Language Server](https://supabase.com/blog/postgres-language-server#not-just-a-language-server)
- [What’s Next](https://supabase.com/blog/postgres-language-server#whats-next)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server&text=Postgres%20Language%20Server%3A%20Initial%20Release)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server&text=Postgres%20Language%20Server%3A%20Initial%20Release)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server&t=Postgres%20Language%20Server%3A%20Initial%20Release)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)