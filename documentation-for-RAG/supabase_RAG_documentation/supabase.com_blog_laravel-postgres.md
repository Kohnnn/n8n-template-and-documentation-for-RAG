---
url: "https://supabase.com/blog/laravel-postgres"
title: "Getting started with Laravel and Postgres"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Getting started with Laravel and Postgres

22 Jan 2024

•

4 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Getting started with Laravel and Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fgetting-started%2Flaravel%2Flaravel.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Every Supabase project comes with a full [Postgres](https://www.postgresql.org/) database, a free and open source database which is considered one of the world's most stable and advanced databases.

Postgres is an ideal choice for your Laravel PHP applications as Laravel ships with a Postgres adapter built in!

In this post we'll start from scratch, creating a new Laravel application, setting up the Laravel Breeze starter kit for user authentication, and connecting it to our Supabase Postgres database.

##### Need help migrating?

Supabase is one of the best [free alternatives to Heroku Postgres](https://supabase.com/alternatives/supabase-vs-heroku-postgres). See [this guide](https://supabase.com/docs/guides/resources/migrating-to-supabase/heroku) to learn how to migrate from Heroku to Supabase.

There's also a [Heroku to Supabase migration tool](https://migrate.supabase.com/) available to migrate in just a few clicks.

If you prefer video guide, you can follow along below. And make sure to subscribe to the [Supabase YouTube channel](https://www.youtube.com/channel/UCNTVzV1InxHV-YR0fSajqPQ?view_as=subscriber&sub_confirmation=1)!

Get started with Laravel and Postgres using Supabase. - YouTube

Supabase

54.4K subscribers

[Get started with Laravel and Postgres using Supabase.](https://www.youtube.com/watch?v=dg1suKt-7D4)

Supabase

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=dg1suKt-7D4 "Watch on YouTube")

## Create a Laravel Project [\#](https://supabase.com/blog/laravel-postgres\#create-a-laravel-project)

Make sure your PHP and Composer versions are up to date, then use `composer create-project` to scaffold a new Laravel project.

See the [Laravel docs](https://laravel.com/docs/10.x/installation#creating-a-laravel-project) for more details.

Terminal

`
composer create-project laravel/laravel example-app
`

## Install the Authentication template [\#](https://supabase.com/blog/laravel-postgres\#install-the-authentication-template)

Install [Laravel Breeze](https://laravel.com/docs/10.x/starter-kits#laravel-breeze), a simple implementation of all of Laravel's [authentication features](https://laravel.com/docs/10.x/authentication).

Terminal

`
composer require laravel/breeze --dev
php artisan breeze:install
`

Note: this template does not use [Supabase Auth](https://supabase.com/auth) but rather Laravel's built in Auth system. This means that [Supabase Auth pricing](https://supabase.com/pricing) does not apply. You'd only be billed for Database resources used in this case.

## Set up the Postgres connection details [\#](https://supabase.com/blog/laravel-postgres\#set-up-the-postgres-connection-details)

Go to [database.new](https://database.new/) and create a new Supabase project. Save your database password securely.

When your project is up and running, navigate to the [project connect page](https://supabase.com/dashboard/project/_?showConnect=true) to find the URI connection string.

Laravel ships with a Postgres adapter out of the box, you can simply configure it via the environment variables. You can find the database URL in your [Supabase Dashboard](https://supabase.com/dashboard/project/_/settings/database).

.env

`
DB_CONNECTION=pgsql
DATABASE_URL=postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
`

### Change the default schema [\#](https://supabase.com/blog/laravel-postgres\#change-the-default-schema)

By default Laravel uses the `public` schema. We recommend changing this as supabase exposes the `public` schema as a [data API](https://supabase.com/docs/guides/api).

You can change the schema of your Laravel application by modifying the `search_path` variable `config/database.php`:

config/database.php

`
'pgsql' => [\
    'driver' => 'pgsql',\
    'url' => env('DATABASE_URL'),\
    'host' => env('DB_HOST', '127.0.0.1'),\
    'port' => env('DB_PORT', '5432'),\
    'database' => env('DB_DATABASE', 'forge'),\
    'username' => env('DB_USERNAME', 'forge'),\
    'password' => env('DB_PASSWORD', ''),\
    'charset' => 'utf8',\
    'prefix' => '',\
    'prefix_indexes' => true,\
    'search_path' => 'laravel',\
    'sslmode' => 'prefer',\
],
`

## Run the database migrations [\#](https://supabase.com/blog/laravel-postgres\#run-the-database-migrations)

Laravel ships with database migration files that set up the required tables for Laravel Authentication and User Management.

Terminal

`
php artisan migrate
`

## Start the app [\#](https://supabase.com/blog/laravel-postgres\#start-the-app)

Terminal

`
php artisan serve
`

Run the development server. Go to [http://127.0.0.1:8000](http://127.0.0.1:8000/) in a browser to see your application. You can also navigate to [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register) and [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login) to register and log in users.

## Conclusion [\#](https://supabase.com/blog/laravel-postgres\#conclusion)

Supabase is the ideal platform for powering your Postgres database for your Laravel applications! Every Supabase project comes with a full Postgres database and a good number of [useful extension](https://supabase.com/docs/guides/database/extensions)!

Try it out now at [database.new](https://database.new/)!

## More Supabase [\#](https://supabase.com/blog/laravel-postgres\#more-supabase)

- [Migration guides](https://supabase.com/docs/guides/resources#migrate-to-supabase)
- [Options for connecting to your Postgres database](https://supabase.com/docs/guides/database/connecting-to-postgres)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaravel-postgres&text=Getting%20started%20with%20Laravel%20and%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaravel-postgres&text=Getting%20started%20with%20Laravel%20and%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaravel-postgres&t=Getting%20started%20with%20Laravel%20and%20Postgres)

[Last post\\
\\
**How pg\_graphql works** \\
\\
24 January 2024](https://supabase.com/blog/how-pg-graphql-works)

[Next post\\
\\
**What is SAML? A practical guide to the authentication protocol** \\
\\
17 January 2024](https://supabase.com/blog/what-is-saml-authentication)

[postgres](https://supabase.com/blog/tags/postgres) [developers](https://supabase.com/blog/tags/developers) [php](https://supabase.com/blog/tags/php)

On this page

- [Create a Laravel Project](https://supabase.com/blog/laravel-postgres#create-a-laravel-project)
- [Install the Authentication template](https://supabase.com/blog/laravel-postgres#install-the-authentication-template)
- [Set up the Postgres connection details](https://supabase.com/blog/laravel-postgres#set-up-the-postgres-connection-details)
  - [Change the default schema](https://supabase.com/blog/laravel-postgres#change-the-default-schema)
- [Run the database migrations](https://supabase.com/blog/laravel-postgres#run-the-database-migrations)
- [Start the app](https://supabase.com/blog/laravel-postgres#start-the-app)
- [Conclusion](https://supabase.com/blog/laravel-postgres#conclusion)
- [More Supabase](https://supabase.com/blog/laravel-postgres#more-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaravel-postgres&text=Getting%20started%20with%20Laravel%20and%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaravel-postgres&text=Getting%20started%20with%20Laravel%20and%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaravel-postgres&t=Getting%20started%20with%20Laravel%20and%20Postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)