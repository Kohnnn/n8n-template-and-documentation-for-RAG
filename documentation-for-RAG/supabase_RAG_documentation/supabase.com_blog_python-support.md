---
url: "https://supabase.com/blog/python-support"
title: "Supabase Python"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Python

16 Aug 2024

•

6 minute read

[![Guilherme Souza avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgrdsdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Guilherme SouzaEngineering](https://github.com/grdsdev)

![Supabase Python](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_python.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

As the Supabase community has grown, so has demand for a diverse collection of client libraries and framework specific SDKs. This demand for the most part has been serviced by the open source community itself, which currently maintains [dozens of libraries](https://github.com/supabase-community/#client-libraries).

When folks make requests to the hosted Supabase service we're able to build up a good picture of how broadly some of these libraries are used, and when a particular library achieves broad adoption it makes sense for us to add official support for it. Examples of libraries that have made the leap from community supported to officially supported include [supabase-flutter](https://github.com/supabase/supabase-flutter) and [supabase-swift](https://github.com/supabase/supabase-swift/).

There has always been incredible community support for the Python client libraries, over the last year and a half however we've seen a huge surge in adoption. This has been driven by the broad adoption of Supabase in the AI and ML community, many of whom are keen Pythonistas.

So today, we're announcing that the following Python Client Libraries are now officially supported on the Supabase platform:

- [supabase-py](https://github.com/supabase/supabase-py)
- [auth-py](https://github.com/supabase/auth-py)
- [storage-py](https://github.com/supabase/storage-py)
- [functions-py](https://github.com/supabase/functions-py)
- [realtime-py](https://github.com/supabase/realtime-py)

[supabase-py](https://github.com/supabase/supabase-py) was originally started by maintainer [lqmanh](https://github.com/lqmanh) in September of 2020, and was shortly after joined by [fedden](https://github.com/fedden) and [J0](https://github.com/J0) (who went on to become a full time member of the Supabase Team). In recent years development has been driven by [silentworks](https://github.com/silentworks) and [juancarlospaco](https://github.com/juancarlospaco) who have both been instrumental in the push to reaching feature parity with [supabase-js](https://github.com/supabase/supabase-js).

Thank you so much to everyone who has contributed to the client libs so far and hopefully we'll see more community libs making the push for official support in the future.

Below is an overview of some recent features added to the collection of Python libs.

## Enabled HTTP2 by default [\#](https://supabase.com/blog/python-support\#enabled-http2-by-default)

Supabase clients will automatically use HTTP 2.0 when available by default, offering a seamless performance boost to your existing applications.

This improvement is implemented in a completely transparent way, and requires no changes to your existing code, while potentially delivering significant latency reduction and performance enhancements.

See also:

- [https://github.com/supabase/functions-py/pull/115](https://github.com/supabase/functions-py/pull/115)
- [https://github.com/supabase/auth-py/pull/534](https://github.com/supabase/auth-py/pull/534)
- [https://github.com/supabase/postgrest-py/pull/462](https://github.com/supabase/postgrest-py/pull/462)
- [https://github.com/supabase/storage-py/pull/271](https://github.com/supabase/storage-py/pull/271)

## Follow redirects by default [\#](https://supabase.com/blog/python-support\#follow-redirects-by-default)

Supabase clients now automatically follow all HTTP redirects by default, aligning with the behavior of Supabase clients in other programming languages.

This enhancement improves consistency across the ecosystem and simplifies the handling of redirects, reducing the need for manual intervention in common scenarios like URL changes or load balancing.

See also:

- [https://github.com/supabase/postgrest-py/pull/449](https://github.com/supabase/postgrest-py/pull/449)
- [https://github.com/supabase/functions-py/pull/107](https://github.com/supabase/functions-py/pull/107)
- [https://github.com/supabase/storage-py/pull/257](https://github.com/supabase/storage-py/pull/257)
- [https://github.com/supabase/auth-py/pull/511](https://github.com/supabase/auth-py/pull/511)

## Keep-alive enabled by default [\#](https://supabase.com/blog/python-support\#keep-alive-enabled-by-default)

Supabase clients now automatically include a `keep-alive` HTTP header by default, that was sometimes missing, addressing this inconsistency in previous versions.

This enhancement optimizes connection management, potentially reducing latency, and improving performance by maintaining persistent connections with the server, especially beneficial for applications making very frequent API calls.

## Edge Functions Regions [\#](https://supabase.com/blog/python-support\#edge-functions-regions)

Added support for specifying the region that the edge function will run on (a region is basically a physical location in the world).

See also:

- [https://github.com/supabase/functions-py/pull/126](https://github.com/supabase/functions-py/pull/126)

## Realtime V2 [\#](https://supabase.com/blog/python-support\#realtime-v2)

Realtime has been upgraded to version `2.0` with lots of improvements and fixes, including updated examples and the new Presence-related features (broadcast, subscribe, track, etc).

See also:

- [https://github.com/supabase/realtime-py/pull/139](https://github.com/supabase/realtime-py/pull/139)
- [https://github.com/supabase/realtime-py/pull/178](https://github.com/supabase/realtime-py/pull/178)

## Auth improvements [\#](https://supabase.com/blog/python-support\#auth-improvements)

Anonymous logins have been added to the Auth client, including a new `is_anonymous` boolean property that has been added to the class `User`, also `sign_in_with_id_token()` and `sign_in_with_sso()` methods have been added to the Auth Client, among a lot of other bug fixes.

See also:

- [https://github.com/supabase/auth-py/pull/528](https://github.com/supabase/auth-py/pull/528)
- [https://github.com/supabase/auth-py/pull/548](https://github.com/supabase/auth-py/pull/548)
- [https://github.com/supabase/auth-py/pull/553](https://github.com/supabase/auth-py/pull/553)
- [https://github.com/supabase/auth-py/pull/506](https://github.com/supabase/auth-py/pull/506)

## Postgrest quoting/escaping in queries [\#](https://supabase.com/blog/python-support\#postgrest-quotingescaping-in-queries)

Supabase improved PostgreSQL query safety by implementing `sanitize_param()` for parameter sanitization in internal SQL queries on the client-side, ensuring more secure data handling and query execution across all operations.

## Running with unverified SSL [\#](https://supabase.com/blog/python-support\#running-with-unverified-ssl)

Some users need to run the Supabase clients with invalid or unverified SSL for whatever reason (SSL debuggers/tracers/profilers/etc in development environments), a new optional boolean argument was added to the constructors of the clients, then passing `verify=False` enables it to run with unverified SSL without warnings.

`
from postgrest import SyncPostgrestClient
url: str = "https://example.com"
h: dict = {"Custom-Header": "value"}
with SyncPostgrestClient(url, schema="pub", headers=h, verify = False) as client:
    session = client.session
    assert session.base_url == "https://example.com"
`

See also:

- [https://github.com/supabase/functions-py/pull/106](https://github.com/supabase/functions-py/pull/106)
- [https://github.com/supabase/storage-py/pull/256](https://github.com/supabase/storage-py/pull/256)
- [https://github.com/supabase/auth-py/pull/506](https://github.com/supabase/auth-py/pull/506)
- [https://github.com/supabase/postgrest-py/pull/448](https://github.com/supabase/postgrest-py/pull/448)
- [https://github.com/supabase/supabase-py/pull/813](https://github.com/supabase/supabase-py/pull/813)

## Close socket in Realtime [\#](https://supabase.com/blog/python-support\#close-socket-in-realtime)

The Supabase Realtime library now includes a new `close()` method for closing the socket connections.

This addition provides developers with finer control over the connection lifecycle, allowing explicit closing of the socket connections when needed.

`
import os
from realtime import AsyncRealtimeClient
def callback1(payload):
    print("Callback 1: ", payload)
SUPABASE_ID: str = os.environ.get("SUPABASE_ID")
API_KEY: str = os.environ.get("SUPABASE_KEY")
URL: str = f"wss://{SUPABASE_ID}.supabase.co/realtime/v1/websocket"
client = AsyncRealtimeClient(URL, API_KEY)
await client.connect()
channel_1 = s.channel("realtime:public:sample")
channel_1.subscribe().on_postgres_changes("INSERT", callback1)
await client.listen()
await client.close()
`

See also:

- [https://github.com/supabase-community/realtime-py/pull/142](https://github.com/supabase-community/realtime-py/pull/142)

## Edge Functions timeouts [\#](https://supabase.com/blog/python-support\#edge-functions-timeouts)

Timeouts for Edge Functions are now fixed and long-running functions finish correctly, there is no longer a library client-side internal timeout cutting off the functions.

Users can now confidently implement more complex operations in Edge Functions.

`
import os
from supabase import create_client
from supabase.lib.client_options import ClientOptions
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
options = ClientOptions(function_client_timeout = 15)
client = create_client(url, key, options)
client.functions.url = "http://127.0.0.1:54321/functions/v1/hello-world"
print(client.functions.invoke("hello"))
`

See also:

- [https://github.com/supabase/functions-py/pull/120](https://github.com/supabase/functions-py/pull/120)
- [https://github.com/supabase/supabase-py/pull/846](https://github.com/supabase/supabase-py/pull/846)

## New tool Vec2pg to migrate data to Supabase [\#](https://supabase.com/blog/python-support\#new-tool-vec2pg-to-migrate-data-to-supabase)

A new simple and extensible CLI tool to migrate vector data from other services and SASS into Supabase was created, it can migrate vector data from Pinecone and Qdrant into Supabase with a single command, streamlining workflows and enhancing data portability across AI and ML projects.

You can vote for other vector database providers to be added in the future!

See also:

- [https://github.com/supabase-community/vec2pg](https://github.com/supabase-community/vec2pg)
- [https://github.com/supabase-community/vec2pg/pull/5](https://github.com/supabase-community/vec2pg/pull/5)
- [https://github.com/supabase-community/vec2pg/issues/6](https://github.com/supabase-community/vec2pg/issues/6)

## Updated CI [\#](https://supabase.com/blog/python-support\#updated-ci)

Continuous Integration builds for all the libraries have been upgraded and made more strict (linters, etc).

See also:

- [https://github.com/supabase/supabase-py/pull/772](https://github.com/supabase/supabase-py/pull/772)
- [https://github.com/supabase/supabase-py/pull/774](https://github.com/supabase/supabase-py/pull/774)
- [https://github.com/supabase/functions-py/pull/93](https://github.com/supabase/functions-py/pull/93)
- [https://github.com/supabase/functions-py/pull/92](https://github.com/supabase/functions-py/pull/92)
- [https://github.com/supabase/storage-py/pull/240](https://github.com/supabase/storage-py/pull/240)
- [https://github.com/supabase/storage-py/pull/237](https://github.com/supabase/storage-py/pull/237)
- [https://github.com/supabase/realtime-py/pull/132](https://github.com/supabase/realtime-py/pull/132)
- [https://github.com/supabase/realtime-py/pull/131](https://github.com/supabase/realtime-py/pull/131)
- [https://github.com/supabase/postgrest-py/pull/424](https://github.com/supabase/postgrest-py/pull/424)
- [https://github.com/supabase/postgrest-py/pull/422](https://github.com/supabase/postgrest-py/pull/422)
- [https://github.com/supabase/functions-py/pull/139](https://github.com/supabase/functions-py/pull/139)
- [https://github.com/supabase/storage-py/pull/287](https://github.com/supabase/storage-py/pull/287)
- [https://github.com/supabase/auth-py/pull/572](https://github.com/supabase/auth-py/pull/572)
- [https://github.com/supabase/postgrest-py/pull/484](https://github.com/supabase/postgrest-py/pull/484)
- [https://github.com/supabase/supabase-py/pull/887](https://github.com/supabase/supabase-py/pull/887)
- [https://github.com/supabase/realtime-py/pull/182](https://github.com/supabase/realtime-py/pull/182)

## Miscellaneous [\#](https://supabase.com/blog/python-support\#miscellaneous)

- Unittests coverage was improved across all code repositories.
- Cyclomatic complexity has been analyzed and improved in all the libraries (mccabe, prospector).
- Multiple fixes for code style, symbol naming, documentation, comments, and docstrings.

## Contributing [\#](https://supabase.com/blog/python-support\#contributing)

If you'd like to get involved in contributing to our Python client libraries see [here](https://github.com/supabase/supabase-py/blob/main/CONTRIBUTING.md) for some information on how to contribute, and check the list of [open issues](https://github.com/supabase/supabase-py/issues) for some inspiration on what to work on.

## Getting started [\#](https://supabase.com/blog/python-support\#getting-started)

Full documentation is available for the Supabase Python Client libraries on the [Supabase Docs site](https://supabase.com/docs/reference/python/introduction).

[Launch Week12](https://supabase.com/launch-week/12)

12-16 August

[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)

[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)

[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)

[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)

[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage

[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)

[02 -pg\_replicate](https://news.ycombinator.com/item?id=41209994)

[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)

[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)

[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)

[06 -vec2pg](https://supabase.com/blog/vec2pg)

[07 -pg\_graphql](https://supabase.com/blog/pg-graphql-1-5-7)

[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)

[09 -python-support](https://supabase.com/blog/python-support)

[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)

[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&t=Supabase%20Python)

[Last post\\
\\
**PostgREST 12.2: Prometheus metrics** \\
\\
16 August 2024](https://supabase.com/blog/postgrest-12-2)

[Next post\\
\\
**The Supabase Book by David Lorenz** \\
\\
16 August 2024](https://supabase.com/blog/supabase-book-by-david-lorenz)

[launch-week](https://supabase.com/blog/tags/launch-week) [database](https://supabase.com/blog/tags/database)

On this page

- [Enabled HTTP2 by default](https://supabase.com/blog/python-support#enabled-http2-by-default)
- [Follow redirects by default](https://supabase.com/blog/python-support#follow-redirects-by-default)
- [Keep-alive enabled by default](https://supabase.com/blog/python-support#keep-alive-enabled-by-default)
- [Edge Functions Regions](https://supabase.com/blog/python-support#edge-functions-regions)
- [Realtime V2](https://supabase.com/blog/python-support#realtime-v2)
- [Auth improvements](https://supabase.com/blog/python-support#auth-improvements)
- [Postgrest quoting/escaping in queries](https://supabase.com/blog/python-support#postgrest-quotingescaping-in-queries)
- [Running with unverified SSL](https://supabase.com/blog/python-support#running-with-unverified-ssl)
- [Close socket in Realtime](https://supabase.com/blog/python-support#close-socket-in-realtime)
- [Edge Functions timeouts](https://supabase.com/blog/python-support#edge-functions-timeouts)
- [New tool Vec2pg to migrate data to Supabase](https://supabase.com/blog/python-support#new-tool-vec2pg-to-migrate-data-to-supabase)
- [Updated CI](https://supabase.com/blog/python-support#updated-ci)
- [Miscellaneous](https://supabase.com/blog/python-support#miscellaneous)
- [Contributing](https://supabase.com/blog/python-support#contributing)
- [Getting started](https://supabase.com/blog/python-support#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&t=Supabase%20Python)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)