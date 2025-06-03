---
url: "https://supabase.com/blog/pgrouting-postgres-graph-database"
title: "Postgres as a Graph Database: (Ab)using pgRouting"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Postgres as a Graph Database: (Ab)using pgRouting

25 Feb 2025

•

13 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Postgres as a Graph Database: (Ab)using pgRouting](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgrouting-graph%2Fpgrouting-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[pgRouting](https://github.com/pgRouting/pgrouting) is a Postgres extension. It's often used for finding the “shortest path” between two locations, however it's a hidden gem in Postgres and can be used for basic graph functionality.

![pgrouting on HN](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgrouting-graph%2Fpgrouting-hn.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

pgRouting is typically combined with PostGIS for working with geospatial data, but it can also be [useful beyond that](https://news.ycombinator.com/item?id=26350454) as a lightweight alternative to Graph extensions like [Apache AGE](https://age.apache.org/), or specialized graph databases like [Neo4j](https://neo4j.com/).

Let's explore some useful applications of pgRouting and graphs.

## What is pgRouting? [\#](https://supabase.com/blog/pgrouting-postgres-graph-database\#what-is-pgrouting)

pgRouting is an extension of PostGIS that provides geospatial routing functionality. You can use it to calculate the shortest path, perform network analysis, and solve complex routing problems on a graph-based structure. Most commonly, this is used in Geographic Information Systems (GIS) for tasks like determining the fastest route between two locations.

![pgrouting map](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgrouting-graph%2Fpgrouting-map.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Working with Graphs [\#](https://supabase.com/blog/pgrouting-postgres-graph-database\#working-with-graphs)

The power of pgRouting lies in its ability to work with any data structured as a graph. A graph is essentially a network of interconnected points, where:

- **Nodes** represent entities.
- **Edges** represent relationships or paths between those nodes.

In maps / [GIS](https://en.wikipedia.org/wiki/Geographic_information_system), nodes and edges represent intersections and roads respectively. However, this structure can also be applied to abstract systems like a social networks, where users are nodes and friendships are edges.

![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgrouting-graph%2Fgraph-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Non-GIS Use Cases for pgRouting [\#](https://supabase.com/blog/pgrouting-postgres-graph-database\#non-gis-use-cases-for-pgrouting)

Let's explore how pgRouting can be applied to a few non- [GIS](https://en.wikipedia.org/wiki/Geographic_information_system) problems.

### Task scheduling [\#](https://supabase.com/blog/pgrouting-postgres-graph-database\#task-scheduling)

In any project, tasks have dependencies. For example, task B can only start after task A is completed. This creates a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG), where:

- nodes represent tasks
- edges represent dependencies

One of the most challenging aspects of managing projects is determining the “critical path” — the project's overall duration, determined by the longest sequence of dependencies.

![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgrouting-graph%2Fpath-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Using pgRouting, you can model your task's dependencies, using graph algorithms to find the critical path. Suppose we have a table tasks with task dependencies modeled as a graph:

`
-- Create the tasks table with dependencies
create table tasks (
id serial primary key,
name text not null
);
-- insert tasks into the table
insert into tasks (name)
values
('Start Project'),
('Task A'),
('Task B'),
('Task C'),
('Task D'),
('End Project');
-- create the dependencies table
create table dependencies (
id serial primary key,
source integer not null, -- task id where the dependency starts
target integer not null, -- task id where the dependency ends
duration integer not null, -- duration of the task in days
constraint fk_source foreign key (source) references tasks (id),
constraint fk_target foreign key (target) references tasks (id)
);
-- insert dependencies with durations (directed edges)
insert into dependencies (source, target, duration)
values
(1, 2, 3), -- start project -> task a (3 days)
(2, 3, 4), -- task a -> task b (4 days)
(3, 4, 5), -- task b -> task c (5 days)
(4, 5, 2), -- task c -> task d (2 days)
(5, 6, 6);
-- task d -> end project (6 days)
`

You can then use the [`pgr_dijkstra()`](https://docs.pgrouting.org/latest/en/pgr_dijkstra.html) function to find the shortest (or longest) path through the tasks, allowing you to map out the project schedule effectively:

`
create schema if not exists extensions;
create extension pgrouting schema extensions cascade;
-- find the longest path using pgr_dijkstra()
-- (as it calculates shortest path, use negative weights)
select * FROM extensions.pgr_dijkstra(
    'select id, source, target, duration as cost from dependencies',
    1,  -- Start Project (Task ID 1)
    6   -- End Project (Task ID 6)
);
`

Which returns a table showing that this project will take 20 days from start to finish:

| **seq** | **path\_seq** | **node** | **edge** | **cost** | **agg\_cost** |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 3 | 0 |
| 2 | 2 | 2 | 2 | 4 | 3 |
| 3 | 3 | 3 | 3 | 5 | 7 |
| 4 | 4 | 4 | 4 | 2 | 12 |
| 5 | 5 | 5 | 5 | 6 | 14 |
| 6 | 6 | 6 | -1 | 0 | 20 |

Tangent: the Dijkstra algorithm

The `pgr_dijkstra()` function implements [Dijkstra's\\
algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm), which is used to find the
shortest path between nodes in a graph. This algorithm guarantees the shortest path from a
source node to a target node (or all other nodes), based on the cost of edges connecting the
nodes.

Fun fact: Dijkstra's algorithm was published in 1959 by Dutch computer scientist Edsger
Dijkstra. It's a “greedy” algorithm, meaning it always picks the closest, cheapest node to
explore next.

### Reverse proxy routing based on resource allocation [\#](https://supabase.com/blog/pgrouting-postgres-graph-database\#reverse-proxy-routing-based-on-resource-allocation)

Distributed systems usually involve allocating resources efficiently across a network of nodes. Each node might represent a physical location or a computing process, and the edges represent the available pathways to move resources between them. For example, in a cloud infrastructure, pgRouting could help determine how to allocate compute tasks across a set of distributed servers by finding the shortest or least-congested path to route data.

Suppose you have a network of servers represented by nodes and their data connections as edges in a table servers.

`
-- create the servers table representing the nodes
create table servers (
id serial primary key,
name text,
x double precision, -- x coordinate for spatial data (latitude)
y double precision -- y coordinate for spatial data (longitude)
);
-- insert some sample servers
insert into servers (name, x, y)
values
('server a', 0, 0),
('server b', 2, 1),
('server c', 4, 3),
('server d', 3, 5);
-- create the server_connections table representing the edges
create table server_latency (
id serial primary key,
source integer,
target integer,
cost double precision, -- cost could represent latency or bandwidth
x1 double precision, -- x coordinate of source
y1 double precision, -- y coordinate of source
x2 double precision, -- x coordinate of target
y2 double precision, -- y coordinate of target,
constraint fk_source foreign key (source) references servers (id),
constraint fk_target foreign key (target) references servers (id)
);
-- insert connections between servers
insert into server_latency (source, target, cost, x1, y1, x2, y2)
values
(1, 2, 1.5, 0, 0, 2, 1), -- server a -> server b with a cost of 1.5 (could be latency)
(2, 3, 2.0, 2, 1, 4, 3), -- server b -> server c with a cost of 2.0
(2, 4, 1.8, 2, 1, 3, 5), -- server b -> server d with a cost of 1.8
(4, 3, 1.0, 3, 5, 4, 3);
-- server d -> server c with a cost of 1.0
`

You can then use [`pgr_astar`](https://docs.pgrouting.org/latest/en/pgr_aStar.html)() to find the most efficient path for data or compute tasks to travel through this network, optimizing for speed or load:

`
-- Query to find the most efficient path (using pgr_astar)
select *
from
extensions.pgr_astar(
    'select id, source, target, cost, x1, y1, x2, y2 from server_latency',
    1,
    3 -- Start from Server A (id=1) to Server C (id=3)
);
`

Tangent: the A\* algorithm

The `pgr_astar()` function is an implementation of the [A\* (A-star)\\
algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm). It's used to find the most
efficient (shortest) path between two points in a graph. A\* is commonly used in navigation and
routing because it is more efficient than Dijkstra's algorithm in many scenarios, especially
when you have spatial data with coordinates (e.g., X, Y positions).

Fun fact: A\* was originally designed in the 1960s for artificial intelligence applications and
pathfinding in games. Today, it's one of the most widely used algorithms in video game
development to help characters navigate complex environments efficiently.

### Recommendation engines like YouTube [\#](https://supabase.com/blog/pgrouting-postgres-graph-database\#recommendation-engines-like-youtube)

In recommendation engines or search algorithms that use knowledge graphs, pgRouting can be used to build relationships between entities and events. Take YouTube's recommendation algorithm, we can structure this data as a graph where:

- **Nodes** represent entities like users, videos, or categories.
- **Edges** represent relationships or interactions between those entities, such as a user liking a video or videos being part of the same category.

Let's create a list of “nodes”:

`
create table categories (
id serial primary key,
name text
);
insert into categories (name)
values
('Graph Theory'),
('AI & Machine Learning'),
('Python Programming');
create table videos (
id serial primary key,
title text,
category_id int references categories (id)
);
insert into videos (title, category_id)
values
('Intro to Graph Theory', 1),
('Advanced Graph Algorithms', 1),
('Graph Neural Networks', 2),
('Beginner Python Tutorial', 3),
('Advanced Python Techniques', 3);
`

And some “edges”:

`
create table video_relationships (
source_video_id int references videos (id),
target_video_id int references videos (id),
relationship_type text, -- 'same_category', 'watched_by_same_users', etc.
weight int default 1 -- strength of the relationship
);
insert into video_relationships (source_video_id, target_video_id, relationship_type, weight)
values
(1, 2, 'same_category', 5), -- "Intro to Graph Theory" and "Advanced Graph Algorithms" are in the same category
(2, 3, 'watched_by_same_users', 3), -- "Advanced Graph Algorithms" and "Graph Neural Networks" are often watched together
(4, 5, 'same_category', 5); -- "Beginner Python Tutorial
create table interactions (
user_id int references auth.users (id),
video_id int references videos (id),
interaction_type text, -- 'liked', 'viewed', etc.
weight int default 1 -- strength of the interaction
);
insert into interactions (user_id, video_id, interaction_type, weight)
values
('user_01', 1, 'viewed', 5), -- "User 01" watched "Intro to Graph Theory" to the end (weight = 5)
('user_01', 2, 'liked', 5), -- "User 01" liked "Advanced Graph Algorithms"
('user_02', 3, 'viewed', 2), -- "User 02" watched "Graph Neural Networks" and bounced halfway through (weight = 2)
('user_03', 4, 'liked', 5), -- "User 03" liked "Beginner Python Tutorial"
('user_03', 5, 'viewed', 2);
-- "User 03" watched "Advanced Python Techniques" and bounced halfway through (weight = 2)
`

Now we can use the `pgr_dijkstra()` function to find the shortest or most relevant path between a user and new videos. For example, let's find videos that are most relevant to `user_01` considering their past interactions:

Tangent: ranking recommendations

Since it's “just postgres” it's simple enough to rank the results using an `order by` clause. For example, if we stored the `pgr_dijkstra()` results above in a table called “recommendations”, we use this a query like this to sort the paths by the highest ranking:

`
select videos.title, sum(weight) as recommendation_score
from
recommendations
join videos on recommendations.target = videos.id
group by videos.title
order by recommendation_score desc;
`

## Get Started [\#](https://supabase.com/blog/pgrouting-postgres-graph-database\#get-started)

pgRouting is a powerful extension for Postgres that can be used to solve a wide range of graph-based problems. Check out the [pgRouting docs](https://docs.pgrouting.org/latest/en/index.html) for more information on how to use it. You can also use it on Supabase:

- Docs: [pgrouting: Geospatial Routing](https://supabase.com/docs/guides/database/extensions/pgrouting)
- Launch a new Postgres database: [database.new](https://database.new/)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgrouting-postgres-graph-database&text=Postgres%20as%20a%20Graph%20Database%3A%20(Ab)using%20pgRouting)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgrouting-postgres-graph-database&text=Postgres%20as%20a%20Graph%20Database%3A%20(Ab)using%20pgRouting)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgrouting-postgres-graph-database&t=Postgres%20as%20a%20Graph%20Database%3A%20(Ab)using%20pgRouting)

[Last post\\
\\
**Dedicated Poolers** \\
\\
7 March 2025](https://supabase.com/blog/dedicated-poolers)

[Next post\\
\\
**AI Hackathon at Y Combinator** \\
\\
20 December 2024](https://supabase.com/blog/ai-hackathon-at-y-combinator)

[postgres](https://supabase.com/blog/tags/postgres)

On this page

- [What is pgRouting?](https://supabase.com/blog/pgrouting-postgres-graph-database#what-is-pgrouting)
- [Working with Graphs](https://supabase.com/blog/pgrouting-postgres-graph-database#working-with-graphs)
- [Non-GIS Use Cases for pgRouting](https://supabase.com/blog/pgrouting-postgres-graph-database#non-gis-use-cases-for-pgrouting)
  - [Task scheduling](https://supabase.com/blog/pgrouting-postgres-graph-database#task-scheduling)
  - [Reverse proxy routing based on resource allocation](https://supabase.com/blog/pgrouting-postgres-graph-database#reverse-proxy-routing-based-on-resource-allocation)
  - [Recommendation engines like YouTube](https://supabase.com/blog/pgrouting-postgres-graph-database#recommendation-engines-like-youtube)
- [Get Started](https://supabase.com/blog/pgrouting-postgres-graph-database#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgrouting-postgres-graph-database&text=Postgres%20as%20a%20Graph%20Database%3A%20(Ab)using%20pgRouting)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgrouting-postgres-graph-database&text=Postgres%20as%20a%20Graph%20Database%3A%20(Ab)using%20pgRouting)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgrouting-postgres-graph-database&t=Postgres%20as%20a%20Graph%20Database%3A%20(Ab)using%20pgRouting)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgrouting-graph%2Fgraph-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpgrouting-graph%2Fpath-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)