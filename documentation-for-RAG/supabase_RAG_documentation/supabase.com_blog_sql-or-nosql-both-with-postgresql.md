---
url: "https://supabase.com/blog/sql-or-nosql-both-with-postgresql"
title: "SQL or NoSQL? Why not use both (with PostgreSQL)?"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# SQL or NoSQL? Why not use both (with PostgreSQL)?

24 Nov 2022

•

18 minute read

[![Mark Burggraf avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fburggraf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Mark BurggrafEngineering](https://github.com/burggraf)

![SQL or NoSQL? Why not use both (with PostgreSQL)?](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-11-24-sql-nosql-postgresql%2Fsql-nosql-postgresql.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It's a tough decision for any developer starting a new project. Should you store your data in a standard, time-tested SQL database, or go with one of the newer NoSQL document-based databases? This seemingly simple decision can literally make or break your project down the line. Choose correctly and structure your data well, and you may sail smoothly into production and watch your app take off. Make the wrong choice and you could be headed for nightmares (and maybe even some major re-writes) before your app ever makes it out the door.

## Simplicity vs Power [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#simplicity-vs-power)

There are tradeoffs with both SQL and NoSQL solutions. Typically it's easier to get started with NoSQL data structures, especially when the data is complex or hierarchical. You can just take a JSON data object from your front-end code and throw it in the database and be done with it. But later when you need to access that data to answer some basic business questions, it's much more difficult. A SQL solution makes it easier to gather data and draw conclusions down the line. Let's look at an example:

Each day I track the food I eat, along with the number of calories in each item:

| Day | Food Item | Calories | Meal |
| --- | --- | --- | --- |
| 01 Jan | Apple | 72 | Breakfast |
| 01 Jan | Oatmeal | 146 | Breakfast |
| 01 Jan | Sandwich | 445 | Lunch |
| 01 Jan | Chips | 280 | Lunch |
| 01 Jan | Cookie | 108 | Lunch |
| 01 Jan | Mixed Nuts | 175 | Snack |
| 01 Jan | Pasta/Sauce | 380 | Dinner |
| 01 Jan | Garlic Bread | 200 | Dinner |
| 01 Jan | Broccoli | 32 | Dinner |

I also track the number of cups of water I drink and when I drink them:

| Day | Time | Cups |
| --- | --- | --- |
| Jan 01 | 08:15 | 1 |
| Jan 01 | 09:31 | 1 |
| Jan 01 | 10:42 | 2 |
| Jan 01 | 12:07 | 2 |
| Jan 01 | 14:58 | 1 |
| Jan 01 | 17:15 | 1 |
| Jan 01 | 18:40 | 1 |
| Jan 01 | 19:05 | 1 |

And finally, I track my exercise:

| Day | Time | Duration | Exercise |
| --- | --- | --- | --- |
| Jan 01 | 11:02 | 0.5 | Walking |
| Jan 02 | 09:44 | 0.75 | Bicycling |
| Jan 02 | 17:00 | 0.25 | Walking |

For each day I also track my current weight along with any notes for the day:

| Day | Weight | Notes |
| --- | --- | --- |
| Jan 01 | 172.6 | This new diet is awesome! |
| Jan 14 | 170.2 | Not sure all this is worth it. |
| Jan 22 | 169.8 | Jogged past a McDonald's today. It was hard. |
| Feb 01 | 168.0 | I feel better, but sure miss all that greasy food. |

## Gathering All That Data [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#gathering-all-that-data)

That's a lot of different data that needs to be gathered, stored, retrieved, and later analyzed. It's organized simply and easily, but the number of records varies from day to day. On any given day I may have zero or more entries for food, water, and exercise, and I may have zero or one entry for weight & notes.

In my app, I gather all the data for a single day on one page, to make it easier for my users. So, I get a JSON object for each day that looks like this:

`
{
"date": "2022-01-01",
"weight": 172.6,
"notes": "This new diet is awesome!",
"food": [\
    { "title": "Apple", "calories": 72, "meal": "Breakfast" },\
    { "title": "Oatmeal", "calories": 146, "meal": "Breakfast" },\
    { "title": "Sandwich", "calories": 445, "meal": "Lunch" },\
    { "title": "Chips", "calories": 280, "meal": "Lunch" },\
    { "title": "Cookie", "calories": 108, "meal": "Lunch" },\
    { "title": "Mixed Nuts", "calories": 175, "meal": "Snack" },\
    { "title": "Pasta/Sauce", "calories": 380, "meal": "Dinner" },\
    { "title": "Garlic Bread", "calories": 200, "meal": "Dinner" },\
    { "title": "Broccoli", "calories": 32, "meal": "Dinner" }\
],
"water": [\
    { "time": "08:15", "qty": 1 },\
    { "time": "09:31", "qty": 1 },\
    { "time": "10:42", "qty": 2 },\
    { "time": "10:42", "qty": 2 },\
    { "time": "12:07", "qty": 1 },\
    { "time": "14:58", "qty": 1 },\
    { "time": "17:15", "qty": 1 },\
    { "time": "18:40", "qty": 1 },\
    { "time": "19:05", "qty": 1 }\
],
"exercise": [{ "time": "11:02", "duration": 0.5, "type": "Walking" }]
}
`

## Saving the Data [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#saving-the-data)

Once we've gathered all the data for a day, we need to store it in our database. In a NoSQL database, this can be a pretty easy process, as we can just create a record (document) for a specific user for a specific date and throw document into a collection and we're done. With SQL, we have some structure we have to work within, and in this case it looks like 4 separate tables: food, water, exercise, and notes. We'd want to do 4 separate inserts here, one for each table. If we don't have data for a specific table (say no exercise was recorded today) then we can skip that table.

If you're using SQL to store this data, you might want to save each table's data as it's entered in your data entry form (and not wait until all the data is entered.) Or you might want to create a database function that takes all the JSON data, parses it, and writes it to all the related tables in a single transaction. There's a lot of ways to handle this, but suffice it to say this: it's a bit more complicated than saving the data in a NoSQL database.

### Retrieving the Data [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#retrieving-the-data)

If we want to display all the data for a single day, it's pretty much the same. With NoSQL you can grab the data for the user's day and then use it in your application. Nice! With SQL we need to query 4 tables to get all the data (or we could use a function to get it all in a single call.) Of course, when displaying the data, we'd need to first break up our JSON data into pieces that are needed by each section of our dashboard screen, and you could argue that it's simpler to map each SQL table with the dashboard section on the screen, but that's a trivial point.

### Analyzing the Data [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#analyzing-the-data)

Now that we've saved the data and we can retrieve it and display it, let's use it for some analysis. _Let's display a graph of how many total calories I've eaten over the past month._ With SQL, this is a simple task:

`
select
date,
sum(calories) as total_calories
from food_log
group by date
where user_id = 'xyz' and day between '2022-01-01' and '2022-01-31'
order by date;
`

Bam! Done! Now we can send those results to our graphing library and make a nice pretty picture of my eating habits.

But if we've stored this data in NoSQL, it gets a little more complicated. We'll need to:

- grab all the data for the user for the month
- parse each day's data to get the food log information
- loop through each day and total the calories
- send the aggregate data to our graphing module

If this is something we're going to do regularly, it makes sense to calculate the total calories for each day and store it in the day's document so we can get at that data faster. But that requires more work up front, and we still need to pull the data for each day and parse out that calorie total first. And if we update the data we still need to recalculate things and update that total. Eventually we'll want to do that with the water and exercise totals as well. The code will eventually start to get longer and more complex.

### SQL and NoSQL Together - FTW [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#sql-and-nosql-together---ftw)

Let's see how we can use the power of SQL together with the ease-of-use of NoSQL in the same database to make this all a bit easier. We'll create a table for each day of data (for each user) and store the basic fields such as `weight` and `notes` first. Then we'll just throw the `food_log`, `water_log`, and `exercise_log` fields in a `JSONB` field.

`
CREATE TABLE calendar (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    date date,
    user_id uuid NOT NULL,
    weight numeric,
    notes text,
    food_log jsonb,
    water_log jsonb,
    exercise_log jsonb
);
-- (Optional) - create a foreign key relationship for the user_id field
ALTER TABLE ONLY calendar
    ADD CONSTRAINT calendar_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth.users(id);
`

Now let's insert some data into the table. PostgreSQL offers both JSON and JSONB fields, and since the latter are more optimized by the database and much faster for query processing, we’ll almost always want to use JSONB. We’ll use JSONB fields for `food_log`, `water_log`, and `exercise_log` and just dump the data we got from our app right into those fields as a string:

`
insert into calendar
(date, user_id, weight, notes, food_log, water_log, exercise_log)
values
(
    '2022-01-01',
    'xyz',
    172.6,
    'This new diet is awesome!',
    '[\
      { "title": "Apple", "calories": 72, "meal": "Breakfast"},\
      { "title": "Oatmeal", "calories": 146, "meal": "Breakfast"},\
      { "title": "Sandwich", "calories": 445, "meal": "Lunch"},\
      { "title": "Chips", "calories": 280, "meal": "Lunch"},\
      { "title": "Cookie", "calories": 108, "meal": "Lunch"},\
      { "title": "Mixed Nuts", "calories": 175, "meal": "Snack"},\
      { "title": "Pasta/Sauce", "calories": 380, "meal": "Dinner"},\
      { "title": "Garlic Bread", "calories": 200, "meal": "Dinner"},\
      { "title": "Broccoli", "calories": 32, "meal": "Dinner"}\
     ]',
    '[\
      {"time": "08:15", "qty": 1},\
      {"time": "09:31", "qty": 1},\
      {"time": "10:42", "qty": 2},\
      {"time": "10:42", "qty": 2},\
      {"time": "12:07", "qty": 1},\
      {"time": "14:58", "qty": 1},\
      {"time": "17:15", "qty": 1},\
      {"time": "18:40", "qty": 1},\
      {"time": "19:05", "qty": 1}\
    ]',
    '[\
      {"time": "11:02", "duration": 0.5, "type": "Walking"}\
    ]'
);
`

While that's a big insert statement, it sure beats doing inserts on 4 separate tables. With all those food entries and water log entries, we would have had to made 1 entry in the main table, then 9 food\_log entries, 9 water\_log entries, and one exercise\_log entry for a total of 20 database records. We've wrapped that into a single record.

## But How Do We Query This Data? [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#but-how-do-we-query-this-data)

Great, we're collecting the data now, and it's easy to insert the data into the database. Editing the data isn't too bad either because we're just downloading the data to the client, updating the JSON field(s) as needed, and throwing them back into the database. Not too hard. But how can I query this data? What about that task from before? _Let's display a graph of how many total calories I've eaten over the past month._

In this case, that data is stored inside the `food_log` field inside the `calendar` table. If only PostgreSQL had a way of converting JSONB arrays into individual database records (recordsets). Well, it does! The `jsonb_array_elements` function will do this for us, allowing to create a simple table we can use to calculate our caloric intake.

Here's some SQL to turn that `food_log` array into individual output records:

`
select
user_id,
date,
jsonb_array_elements(food_log)->>'title' as title,
jsonb_array_elements(food_log)->'calories' as calories,
jsonb_array_elements(food_log)->'meal' as meal
from calendar
where user_id = 'xyz'
and date between '2022-01-01' and '2022-01-31';
`

This returns a table that looks like this:

| date | title | calories | meal |
| --- | --- | --- | --- |
| 2022-01-01 | Apple | 72 | Breakfast |
| 2022-01-01 | Oatmeal | 146 | Breakfast |
| 2022-01-01 | Sandwich | 445 | Lunch |
| 2022-01-01 | Chips | 280 | Lunch |
| 2022-01-01 | Cookie | 108 | Lunch |
| 2022-01-01 | Mixed Nuts | 175 | Snack |
| 2022-01-01 | Pasta/Sauce | 380 | Dinner |
| 2022-01-01 | Garlic Bread | 200 | Dinner |
| 2022-01-01 | Broccoli | 32 | Dinner |

A couple things to note:

- `jsonb_array_elements(food_log)->>'title' as title` this returns a text field, since the `->>` operator returns TEXT
- `jsonb_array_elements(food_log)->'calories' as calories` this returns a JSON object, since the `->` operator return JSON

If we want to `sum` the calories to get some totals, we can't have a JSON object, so we need to cast that to something more useful, like an `INTEGER`:

- `(jsonb_array_elements(food_log)->'calories')::INTEGER as calories` this returns an INTEGER

Now we can't just throw the `sum` operator on this to get the total calories by day. If we try this:

`
select
date,
sum((jsonb_array_elements(food_log)->'calories')::integer) as total_calories
from calendar where user_id = 'xyz'
and date between '2022-01-01' and '2022-01-31'
group by date;
`

we get an error back from PostgreSQL: **Failed to run sql query: aggregate function calls cannot contain set-returning function calls**.

Instead, we need to think of this as a set of building blocks, where our first SQL statement returns a table:

`
select
date,
(jsonb_array_elements(food_log)->'calories')::integer as calories
from calendar where user_id = 'xyz'
and date between '2022-01-01' and '2022-01-31';
`

Now we can take that "table" statement, throw some (parenthesis) around it, and query **it**:

`
with data as
(
select
    date,
    (jsonb_array_elements(food_log)->'calories')::integer as calories
from calendar
where user_id = 'xyz'
    and date between '2022-01-01' and '2022-01-31'
)
select date, sum(calories)
from data
group by date;
`

This gives us exactly what we want:

| date | sum |
| --- | --- |
| 2022-01-01 | 1838 |

If we add more data for the rest of the days of the month, we'll have all the data we need for a beautiful graph.

### Searching the Data [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#searching-the-data)

What if we want to answer the question: _How many calories were in the garlic bread I ate last month?_ This data is stored inside the `food_log` field in the `calendar` table. We can use the same type of query we used before to "flatten" the `food_log` data so we can search it.

To get every item I ate during the month of January, we can use:

`
select
date,
jsonb_array_elements(food_log)->>'title' as title,
(jsonb_array_elements(food_log)->'calories')::integer as calories
from calendar
where user_id = 'xyz'
and date between '2022-01-01' and '2022-01-31'
`

Now to search for the **garlic bread** we can just put (parenthesis) around this to make a "table" and then search for the item we want:

`
with my_food as
(
select
    date,
    jsonb_array_elements(food_log)->>'title' as title,
    (jsonb_array_elements(food_log)->'calories')::integer as calories
from calendar
where user_id = 'xyz'
    and date between '2022-01-01' and '2022-01-31'
)
select
title,
calories
from my_food
where title = 'Garlic Bread';
`

which gives us:

| title | calories |
| --- | --- |
| Garlic Bread | 200 |

## Conclusion [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#conclusion)

If we take a little time to study the [JSON Functions and Operators](https://www.postgresql.org/docs/9.5/functions-json.html) that PostgreSQL offers, we can turn Postgres into an easy-to-use NoSQL database that still retains all the power of SQL. This gives us a super easy way to store our complex JSON data coming from our application code in our database. Then we can use powerful SQL capabilities to analyze and present that data in our application. It's the best of both worlds!

## More Postgres resources [\#](https://supabase.com/blog/sql-or-nosql-both-with-postgresql\#more-postgres-resources)

- [Postgres Full Text Search vs the rest](https://supabase.com/blog/postgres-full-text-search-vs-the-rest)
- [Postgres WASM by Snaplet and Supabase](https://supabase.com/blog/postgres-wasm)
- [Choosing a Postgres Primary Key](https://supabase.com/blog/choosing-a-postgres-primary-key)
- [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
- [Postgres Views](https://supabase.com/blog/postgresql-views)
- [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsql-or-nosql-both-with-postgresql&text=SQL%20or%20NoSQL%3F%20Why%20not%20use%20both%20(with%20PostgreSQL)%3F)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsql-or-nosql-both-with-postgresql&text=SQL%20or%20NoSQL%3F%20Why%20not%20use%20both%20(with%20PostgreSQL)%3F)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsql-or-nosql-both-with-postgresql&t=SQL%20or%20NoSQL%3F%20Why%20not%20use%20both%20(with%20PostgreSQL)%3F)

[Last post\\
\\
**The Supabase Content Storm** \\
\\
6 December 2022](https://supabase.com/blog/the-supabase-content-storm)

[Next post\\
\\
**Flutter Authorization with RLS** \\
\\
22 November 2022](https://supabase.com/blog/flutter-authorization-with-rls)

[postgres](https://supabase.com/blog/tags/postgres) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Simplicity vs Power](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#simplicity-vs-power)
- [Gathering All That Data](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#gathering-all-that-data)
- [Saving the Data](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#saving-the-data)
  - [Retrieving the Data](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#retrieving-the-data)
  - [Analyzing the Data](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#analyzing-the-data)
  - [SQL and NoSQL Together - FTW](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#sql-and-nosql-together---ftw)
- [But How Do We Query This Data?](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#but-how-do-we-query-this-data)
  - [Searching the Data](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#searching-the-data)
- [Conclusion](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#conclusion)
- [More Postgres resources](https://supabase.com/blog/sql-or-nosql-both-with-postgresql#more-postgres-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsql-or-nosql-both-with-postgresql&text=SQL%20or%20NoSQL%3F%20Why%20not%20use%20both%20(with%20PostgreSQL)%3F)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsql-or-nosql-both-with-postgresql&text=SQL%20or%20NoSQL%3F%20Why%20not%20use%20both%20(with%20PostgreSQL)%3F)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsql-or-nosql-both-with-postgresql&t=SQL%20or%20NoSQL%3F%20Why%20not%20use%20both%20(with%20PostgreSQL)%3F)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)