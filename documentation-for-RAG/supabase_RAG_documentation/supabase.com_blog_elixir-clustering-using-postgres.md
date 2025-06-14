---
url: "https://supabase.com/blog/elixir-clustering-using-postgres"
title: "Elixir clustering using Postgres"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Elixir clustering using Postgres

09 Jan 2024

•

6 minute read

[![Filipe Cabaço avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffilipecabaco.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Filipe CabaçoEngineering](https://twitter.com/filipecabaco)

![Elixir clustering using Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felixir-clustering-using-postgres%2Felixir-clustering-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Elixir offers a powerful feature by allowing multiple nodes to communicate between them without extra services in the middle, reducing the overall complexity of your system.

![Elixir nodes communicating between each other without extra services in the middle](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felixir-clustering-using-postgres%2Felixir-multiple-nodes.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

However, when it comes to connecting the servers, there seems to be a barrier of entry that many people encounter, including ourselves, on how to provide the name discovery required to connect said servers. We have released our approach to solving this problem by open-sourcing [libcluster Postgres Strategy](https://github.com/supabase/libcluster_postgres) and today, we explore the motivations behind its creation and the methodologies employed in its development.

![Elixir nodes communicating between each other without extra services in the middle](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felixir-clustering-using-postgres%2Flibcluster.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Why do we need a distributed Erlang Cluster? [\#](https://supabase.com/blog/elixir-clustering-using-postgres\#why-do-we-need-a-distributed-erlang-cluster)

At Supabase, we use clustering in all of our Elixir projects which include [Logflare](https://supabase.com/docs/guides/database/extensions/wrappers/logflare), [Supavisor](https://supabase.com/blog/supavisor-postgres-connection-pooler) and [Realtime](https://supabase.com/docs/guides/realtime). With multiple servers connected, we can load shed, create globally distributed services, and provide the best service to our customers so we’re closer to them geographically and to their instances, reducing overall latency.

![Example of Realtime architecture where a customer from CA will connect to the server closest to them and their Supabase instance](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felixir-clustering-using-postgres%2Frealtime-architecture.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

To achieve a connected cluster, we wanted to be as cloud-agnostic as possible. This makes our self-hosting options more accessible. We don’t want to introduce extra services to solve this single issue - Postgres is the logical way to achieve it.

The other piece of the puzzle was already built by the Erlang community being the defacto library to facilitate the creation of connected Elixir servers: [libcluster](https://github.com/bitwalker/libcluster).

## What is libcluster? [\#](https://supabase.com/blog/elixir-clustering-using-postgres\#what-is-libcluster)

[libcluster](https://github.com/bitwalker/libcluster) is the go-to package for connecting multiple BEAM instances and setting up healing strategies. libcluster provides out-of-the-box strategies and it allows users to define their own strategies by implementing a simple behavior that defines cluster formation and healing according to the supporting service you want to use.

## How did we use Postgres? [\#](https://supabase.com/blog/elixir-clustering-using-postgres\#how-did-we-use-postgres)

Postgres provides an event system using two commands: [NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) and [LISTEN](https://www.postgresql.org/docs/current/sql-listen.html) so we can use them to propagate events within our Postgres instance.

To use these features, you can use psql itself or any other Postgres client. Start by listening on a specific channel, and then notify to receive a payload.

`
postgres=# LISTEN channel;
LISTEN
postgres=# NOTIFY channel, 'payload';
NOTIFY
Asynchronous notification "channel" with payload "payload" received from server process with PID 326.
`

Now we can replicate the same behavior in Elixir and [Postgrex](https://hex.pm/packages/postgrex) within IEx (Elixir's interactive shell).

`
Mix.install([{:postgrex, "~> 0.17.3"}])
config = [\
hostname: "localhost",\
username: "postgres",\
password: "postgres",\
database: "postgres",\
port: 5432\
]
{:ok, db_notification_pid} = Postgrex.Notifications.start_link(config)
Postgrex.Notifications.listen!(db_notification_pid, "channel")
{:ok, db_conn_pid} = Postgrex.start_link(config)
Postgrex.query!(db_conn_pid, "NOTIFY channel, 'payload'", [])
receive do msg -> IO.inspect(msg) end
# Mailbox will have a message with the following content:
# {:notification, #PID<0.223.0>, #Reference<0.57446457.3896770561.212335>, "channel", "test"}
`

## Building the strategy [\#](https://supabase.com/blog/elixir-clustering-using-postgres\#building-the-strategy)

Using the libcluster `Strategy` behavior, inspired by [this GitHub repository](https://github.com/kevbuchanan/libcluster_postgres) and knowing how `NOTIFY/LISTEN` works, implementing a strategy becomes straightforward:

1. We send a `NOTIFY` to a channel with our `node()` address to a configured channel

`
# lib/cluster/strategy/postgres.ex:52
def handle_continue(:connect, state) do
    with {:ok, conn} <- Postgrex.start_link(state.meta.opts.()),
         {:ok, conn_notif} <- Postgrex.Notifications.start_link(state.meta.opts.()),
         {_, _} <- Postgrex.Notifications.listen(conn_notif, state.config[:channel_name]) do
      Logger.info(state.topology, "Connected to Postgres database")
      meta = %{
        state.meta
        | conn: conn,
          conn_notif: conn_notif,
          heartbeat_ref: heartbeat(0)
      }
      {:noreply, put_in(state.meta, meta)}
    else
      reason ->
        Logger.error(state.topology, "Failed to connect to Postgres: #{inspect(reason)}")
        {:noreply, state}
    end
end
`

1. We actively listen for new `{:notification, pid, reference, channel, payload}` messages and connect to the node received in the payload

`
# lib/cluster/strategy/postgres.ex:80
def handle_info({:notification, _, _, _, node}, state) do
    node = String.to_atom(node)
    if node != node() do
      topology = state.topology
      Logger.debug(topology, "Trying to connect to node: #{node}")
      case Strategy.connect_nodes(topology, state.connect, state.list_nodes, [node]) do
        :ok -> Logger.debug(topology, "Connected to node: #{node}")
        {:error, _} -> Logger.error(topology, "Failed to connect to node: #{node}")
      end
    end
    {:noreply, state}
end
`

1. Finally, we configure a heartbeat that is similar to the first message sent for cluster formation so libcluster is capable of heal if need be

`
# lib/cluster/strategy/postgres.ex:73
def handle_info(:heartbeat, state) do
    Process.cancel_timer(state.meta.heartbeat_ref)
    Postgrex.query(state.meta.conn, "NOTIFY #{state.config[:channel_name]}, '#{node()}'", [])
    ref = heartbeat(state.config[:heartbeat_interval])
    {:noreply, put_in(state.meta.heartbeat_ref, ref)}
end
`

These three simple steps allow us to connect as many nodes as needed, regardless of the cloud provider, by utilizing something that most projects already have: a Postgres connection.

## Conclusion [\#](https://supabase.com/blog/elixir-clustering-using-postgres\#conclusion)

In this post, we have described our approach to connecting multiple nodes in Elixir using Postgres. We have also made this strategy available for anyone to use. Please check the code at [github.com/supabase/libcluster\_postgres](https://github.com/supabase/libcluster_postgres)

A special thank you to [@gotbones](https://twitter.com/gotbones) for creating libcluster and [@kevinbuch\_](https://twitter.com/kevinbuch_) for the original inspiration for this strategy.

## More Supabase Realtime [\#](https://supabase.com/blog/elixir-clustering-using-postgres\#more-supabase-realtime)

- [Realtime docs](https://supabase.com/docs/guides/realtime)
- [Realtime: Multiplayer Edition](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability)
- [Video - How to subscribe to real-time changes on your database](https://www.youtube.com/watch?v=2rUjcmgZDwQ)
- [Video - Listening to real-time changes on the database with Flutter and Supabase](https://www.youtube.com/watch?v=gboTC2lcgzw)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Felixir-clustering-using-postgres&text=Elixir%20clustering%20using%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Felixir-clustering-using-postgres&text=Elixir%20clustering%20using%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Felixir-clustering-using-postgres&t=Elixir%20clustering%20using%20Postgres)

[Last post\\
\\
**Brace yourself, IPv6 is coming** \\
\\
12 January 2024](https://supabase.com/blog/ipv6)

[Next post\\
\\
**Supabase Beta December 2023** \\
\\
5 January 2024](https://supabase.com/blog/beta-update-december-2023)

[supabase-engineering](https://supabase.com/blog/tags/supabase-engineering) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Why do we need a distributed Erlang Cluster?](https://supabase.com/blog/elixir-clustering-using-postgres#why-do-we-need-a-distributed-erlang-cluster)
- [What is libcluster?](https://supabase.com/blog/elixir-clustering-using-postgres#what-is-libcluster)
- [How did we use Postgres?](https://supabase.com/blog/elixir-clustering-using-postgres#how-did-we-use-postgres)
- [Building the strategy](https://supabase.com/blog/elixir-clustering-using-postgres#building-the-strategy)
- [Conclusion](https://supabase.com/blog/elixir-clustering-using-postgres#conclusion)
- [More Supabase Realtime](https://supabase.com/blog/elixir-clustering-using-postgres#more-supabase-realtime)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Felixir-clustering-using-postgres&text=Elixir%20clustering%20using%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Felixir-clustering-using-postgres&text=Elixir%20clustering%20using%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Felixir-clustering-using-postgres&t=Elixir%20clustering%20using%20Postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Elixir nodes communicating between each other without extra services in the middle](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felixir-clustering-using-postgres%2Felixir-multiple-nodes.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Elixir nodes communicating between each other without extra services in the middle](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felixir-clustering-using-postgres%2Flibcluster.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Example of Realtime architecture where a customer from CA will connect to the server closest to them and their Supabase instance](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felixir-clustering-using-postgres%2Frealtime-architecture.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)