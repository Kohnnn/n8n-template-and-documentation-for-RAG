---
url: "https://supabase.com/blog/postgrest-aggregate-functions"
title: "PostgREST Aggregate Functions"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# PostgREST Aggregate Functions

29 Feb 2024

•

10 minute read

[![Tim Abdulla avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ftimabdulla.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tim AbdullaGuest Author](https://github.com/timabdulla)

![PostgREST Aggregate Functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Faggregate_functions_og.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[PostgREST v12 has been released,](https://github.com/PostgREST/postgrest/releases/tag/v12.0.0) and with it comes the release of a much-requested feature: **aggregate functions**.

As a bit of background, aggregate functions are a database feature that allow you to summarize your data by performing calculations across groups of rows. Previously, you could only use aggregate functions _indirectly_ with PostgREST, for instance, by using them in a view, but with the latest release, you can now use aggregate functions on the fly, dynamically slicing-and-dicing data directly through the PostgREST API.

In this post, we’ll go through a few examples of some of the neat things you can do with this new feature. We’ll also discuss the importance of ensuring you have the appropriate safeguards in place to prevent potential performance issues that may arise when using aggregate functions.

For the most complete information, please be sure to refer to [the section on aggregate functions in the documentation](https://postgrest.org/en/v12.0/references/api/aggregate_functions.html).

## The Basics of Aggregate Functions [\#](https://supabase.com/blog/postgrest-aggregate-functions\#the-basics-of-aggregate-functions)

PostgREST supports a handful of the most-common aggregate functions from PostgreSQL: `avg()`, `count()`, `max()`, `min()`, and `sum()`. These functions more or less do what their names suggest, but you can always take a deeper look at the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-aggregate.html) to learn more.

Let’s take a look at an example. Imagine we have a table called `movies` that has the following columns: `name`, `release_year`, `genre`, and `box_office_earnings`. Let’s say that we want to grab the max and min of the `release_year` column across all of the movies in our dataset. That’s pretty simple to achieve:

cURL

`
$ curl 'http://postgrest/movies?select=release_year.max(),release_year.min()'
`

supabase-js

`
const { data, error } = await supabase
.from('movies')
.select('release_year.max(), release_year.min()')
`

`
[\
{\
    "max": 2022,\
    "min": 2018\
}\
]
`

As you can see, to use an aggregate function, we just place the function after the column in the `select` parameter. Easy.

Now, what if we want to get a little fancier and get the max and min of the `release_year` for every `genre` in our dataset? If you’re familiar with aggregate functions in SQL, then your mind will probably go right away to `GROUP BY`. In PostgREST, there is no need to _explicitly_ specify a `GROUP BY`; instead, you can just add your grouping columns right to the `select` parameter. Any column without an aggregate function in the `select` list will be used as a grouping column:

cURL

`
$ curl 'http://postgrest/movies?select=genre,release_year.max(),release_year.min()'
`

supabase-js

`
const { data, error } = await supabase
.from('movies')
.select('genre, release_year.max(), release_year.min()')
`

`
[\
{\
    "genre": "Adventure",\
    "max": 2021,\
    "min": 2020\
},\
{\
    "genre": "Horror",\
    "max": 2022,\
    "min": 2019\
},\
{\
    "genre": "Sci-Fi",\
    "max": 2022,\
    "min": 2018\
},\
{\
    "genre": "Mystery",\
    "max": 2019,\
    "min": 2019\
}\
]
`

Generally speaking, aggregate functions can be used with other PostgREST features you’re already familiar with. For instance, you can use [vertical filtering](https://postgrest.org/en/stable/references/api/tables_views.html#vertical-filtering) to apply aggregates to a slimmed down version of your dataset, like only movies released after the year 2000, or you can use [column renaming](https://postgrest.org/en/stable/references/api/tables_views.html#renaming-columns) to change the name of the aggregated column in the results, like for example changing the names of the `max` and `min` columns from the previous examples to instead be `max_release_year` and `min_release_year`.

## Aggregate Functions and Embedded Resources [\#](https://supabase.com/blog/postgrest-aggregate-functions\#aggregate-functions-and-embedded-resources)

Aggregate functions also play nicely with [embedded resources](https://postgrest.org/en/stable/references/api/resource_embedding.html), opening up a world of potential use cases.

Building on the previous examples, let’s say that we have a table called `directors` that has a **one-to-many relationship** with our `movies` table from before. We’ll be using a couple of columns from the `directors` table in this section: `name` and `country`.

Let’s say for every director, we want to get the `release_year` of their oldest and newest movies. We can do that without too much trouble:

cURL

`
$ curl 'http://postgrest/directors?select=name,movies(newest_movie_year:release_year.max(),oldest_movie_year:release_year.min())'
`

supabase-js

``
const { data, error } = await supabase.from('directors').select(`name,
		movies(
			newest_movie_year:release_year.max(),
			oldest_movie_year:release_year.min()
		)`)
``

`
[\
{\
    "name": "Maria Gonzalez",\
    "movies": [\
      {\
        "newest_movie_year": 2022,\
        "oldest_movie_year": 2018\
      }\
    ]\
},\
{\
    "name": "John Smith",\
    "movies": [\
      {\
        "newest_movie_year": 2022,\
        "oldest_movie_year": 2019\
      }\
    ]\
},\
{\
    "name": "Amit Patel",\
    "movies": [\
      {\
        "newest_movie_year": 2021,\
        "oldest_movie_year": 2019\
      }\
    ]\
}\
]
`

As shown above, you can use aggregate functions _within_ the context of an embedded resource: For each set of movies that belongs to a particular director, we apply the given aggregate functions, in this case applying the `min()` and `max()` functions to the `release_year`.

You can also see that we made use of a column renaming — as was briefly described earlier — to make the results a little easier to understand.

Note that we didn’t use grouping columns here, but we could use them to drill-down even further: For instance, we could grab the earliest and latest values of the `release_year` column for each director _by_ `genre` by adding `genre` as a grouping column.

Let’s look at another example, but this time going the opposite way: We’ll use `movies` as our **top-level resource** and embed `directors` through a **one-to-one** relationship.

Now, we want to get the average `box_office_earnings` for our movies, grouped by the `country` of the director. To do that, we can use the following API call:

cURL

`
$ curl 'http://postgrest/movies?select=avg_earnings:box_office_earnings.avg(),...directors(country)'
`

supabase-js

``
const { data, error } = await supabase.from('movies').select(`
		avg_earnings:box_office_earnings.avg(),
    ...directors(country)
	`)
``

`
[\
{\
    "avg_earnings": 10200000.38,\
    "country": "Spain"\
},\
{\
    "avg_earnings": 8933333.79,\
    "country": "India"\
},\
{\
    "avg_earnings": 8933333.84,\
    "country": "United States"\
}\
]
`

In this case, we have used [the ability to spread the columns from an embedded resource](https://postgrest.org/en/stable/references/api/resource_embedding.html#spread-embedded-resource) to use the director’s `country` as a grouping column, even though the aggregate function `avg()` is being applied to a column of `movies`, not `directors`.

Because spreading columns brings them to the top-level, they are treated as columns of the top-level for purposes of aggregation and grouping. That means any aggregate functions applied to the columns of a spread resource are applied within the context of the top-level, too.

## Staying Safe with Aggregate Functions [\#](https://supabase.com/blog/postgrest-aggregate-functions\#staying-safe-with-aggregate-functions)

Now that we’ve gone through a few examples of how to use aggregate functions, it’s important to discuss how to _safely_ use aggregate functions in your application. Because of the potential performance risks with aggregate functions, we have [**disabled** aggregate functions by default](https://postgrest.org/en/stable/references/configuration.html#db-aggregates-enabled). Only after reviewing the risks and ensuring appropriate safeguards are in place should you enable this feature. On Supabase, you can enable it by modifying the PostgREST connection role and then reloading the server configuration, like so:

`
ALTER ROLE authenticator SET pgrst.db_aggregates_enabled = 'true';
NOTIFY pgrst, 'reload config';
`

Now you may be thinking, “what’s the big deal?” Aggregate functions may not seem any more likely to pose performance problems than other parts of PostgREST, but there is one key difference: Aggregate functions can operate across an effectively limitless number of rows, whereas other parts of PostgREST — thanks to pagination — can be limited to operate only across a certain number of rows.

For example, imagine our `movies` table from before has twenty million rows. If we wanted to get the max of the `release_year` for all movies and there is no index on the `release_year` column, it’s going to take a _looooong_ time.

Even worse, imagine that someone with bad intentions wants to do bad things to your innocent server: It could be relatively simple for the attacker to bombard your server with expensive aggregation queries, preventing your server from having the capacity to deal with legitimate traffic, a form of denial-of-service attack.

One strategy for preventing potential performance issues is using the [`pg_plan_filter_module`](https://github.com/pgexperts/pg_plan_filter). Using this extension, you can set an upper limit on the _cost_ of queries that PostgREST will run.

`
ALTER USER authenticator SET plan_filter.statement_cost_limit = 1e7;
`

Before PostgreSQL executes a query, it first comes up with a plan on how it will execute it, and as part of that plan, it comes up with a cost. As you might imagine, higher costs are associated with slower queries, and therefore setting an upper bound can limit your exposure to performance problems or even denial-of-service attacks. `pg_plan_filter_module` enables you to easily set this upper bound using PostgreSQL configuration.

You can even change this limit on a per-role basis, allowing more privileged roles free rein in the queries they run, while less-privileged roles — perhaps external users of your public API, for instance — could have tighter limits.

`
-- anonymous users can only run cheap queries
ALTER
USER anon
SET
plan_filter.statement_cost_limit = 10000;
-- authenticated users can run more expensive queries
ALTER
USER authenticated
SET
plan_filter.statement_cost_limit = 1e6;
`

You can take a look at an example of using per-role configuration with PostgREST [in the documentation](https://postgrest.org/en/stable/references/transactions.html#impersonated-role-settings).

## Summing Up [\#](https://supabase.com/blog/postgrest-aggregate-functions\#summing-up)

PostgREST v12 now has aggregate functions, giving you a lot more flexibility in how you work with your data. Even better, it’s deeply integrated with other PostgREST features you already know, providing you with a powerful new abstraction that fits in frictionlessly with existing features.

While we are excited to bring aggregate functions to PostgREST, it’s important for administrators and users to understand the risks that come with them, hence why this feature comes as opt-in only. Make sure to have a strategy in place — like using `pg_plan_filter_module` — before enabling aggregate functions to ensure maximum protection.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-aggregate-functions&text=PostgREST%20Aggregate%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-aggregate-functions&text=PostgREST%20Aggregate%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-aggregate-functions&t=PostgREST%20Aggregate%20Functions)

[Last post\\
\\
**Implementing semantic image search with Amazon Titan and Supabase Vector** \\
\\
26 March 2024](https://supabase.com/blog/semantic-image-search-amazon-bedrock)

[Next post\\
\\
**Build a content recommendation app with Flutter and OpenAI** \\
\\
26 February 2024](https://supabase.com/blog/content-recommendation-with-flutter)

[postgrest](https://supabase.com/blog/tags/postgrest)

On this page

- [The Basics of Aggregate Functions](https://supabase.com/blog/postgrest-aggregate-functions#the-basics-of-aggregate-functions)
- [Aggregate Functions and Embedded Resources](https://supabase.com/blog/postgrest-aggregate-functions#aggregate-functions-and-embedded-resources)
- [Staying Safe with Aggregate Functions](https://supabase.com/blog/postgrest-aggregate-functions#staying-safe-with-aggregate-functions)
- [Summing Up](https://supabase.com/blog/postgrest-aggregate-functions#summing-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-aggregate-functions&text=PostgREST%20Aggregate%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-aggregate-functions&text=PostgREST%20Aggregate%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-aggregate-functions&t=PostgREST%20Aggregate%20Functions)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)