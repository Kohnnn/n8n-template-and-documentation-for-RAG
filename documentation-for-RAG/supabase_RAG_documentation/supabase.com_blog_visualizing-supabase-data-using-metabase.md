---
url: "https://supabase.com/blog/visualizing-supabase-data-using-metabase"
title: "Visualizing Supabase Data using Metabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Visualizing Supabase Data using Metabase

29 Jun 2022

•

5 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Visualizing Supabase Data using Metabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fsupabase-python-metabase.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Data helps organizations make better decisions. With a programming language like Python to analyze your data and transform data into visual representations, you can effortlessly tell the story of your business. One way to create customized visuals from your data would be to use data visualization libraries in Python like [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [Ggplot2](https://ggplot2.tidyverse.org/index.html), [Plotly](https://plotly.com/), or [Pandas](https://pandas.pydata.org/). When you want to accomplish this task with little or no code (not even SQL), you might consider using tools like [Metabase](https://www.metabase.com/).

With Metabase, a powerful visualization tool, you can quickly turn your data into easy-to-understand visuals like graphs, pie charts, flow diagrams, and much more. Then, using Metabase’s intuitive interface, you can cut through the data noise and focus on what’s essential for your business.

In the previous blog of this series, we explained [how to use Python to load data into Supabase](https://supabase.com/blog/loading-data-supabase-python). In this blog, we will create different kinds of charts out of the data stored in Supabase using Metabase.

## Prerequisites [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#prerequisites)

Before we dive in, let’s look at some prerequisites that you will need:

- **Supabase project with data**

Based on our [previous article](https://supabase.com/blog/loading-data-supabase-python), we assume we already have a Supabase project setup and have data loaded into it.

- **Metabase Docker Container**

To take advantage of the open-source version of Metabase, you can use the Metabase docker container [here](https://hub.docker.com/r/metabase/metabase).

## Visualizing data in Supabase with Metabase [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#visualizing-data-in-supabase-with-metabase)

### Launching Metabase [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#launching-metabase)

To launch Metabase, simply go to [http://localhost:3000/setup/](http://localhost:3000/setup/) which is the default port that the Metabase server will be listening to.

After Metabase is launched, select your preferred language and add your contact information. In the _Add your data_ markdown, you will need to choose PostgreSQL.

![screen shot of adding postgres data to metabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fadding-postgresql-data-metabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You will be prompted to add the necessary connection information to your Supabase project. Go to your [Supabase project](https://supabase.com/dashboard/) and hit _Settings > Database to get the database info_.

![screen shot of supabase dashboard database connection information](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fsupabase-dashboard-connect-database-info.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Enter the necessary information on Metabase and hit next. Finally, select your data preference, after which you will land on the Metabase homepage.

### View Database and Tables [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#view-database-and-tables)

We can now see the "Supabase DB" Supabase project under "Our data".

![screen shot of metabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-with-supabase-db.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

To view the tables, go to _SupabaseDB > public_

![screen shot of metabase dashboard table view](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-02.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### View Table Data Insights [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#view-table-data-insights)

Go back to the home page and select public schema under "Try these x-rays based on your data"

![screen shot of metabase dashboard schema view](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-03.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Here is the output of the product table.

![screen shot of metabase data visualization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-visualization-supabase-db.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

As you can see, we can get some handy information from this like:

- How many products are present with a given range of inventory count.
- How many products are present for a given range of price.
- The ratio between the number of employees to the number of products.
- How many products each vendor has created.

If you have column-specific views, you can select the _zoom-in_ option under _More x-rays_.

![screen shot of metabase data visualization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-visualization-supabase-db-02.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

For example, let's select the total employees field.

![screen shot of metabase data visualization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-visualization-supabase-data.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

With information like this, you will be able to answer some key questions like

- What are some common statistics for company employees like average, minimum, maximum, and standard deviation?
- What is the distribution of the employees across different geo locations?
- What is the distribution of the employees across different vendors?

## Using custom SQL queries [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#using-custom-sql-queries)

We can also use custom queries to set up our dashboards. To do this, go to _New > SQL query._

![screen shot of metabase custom queries dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-04.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Next, under the database, select "SupabaseDB".

![screen shot of metabase custom queries dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-05.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We will be using the following SQL query:

`
select "Vendor".vendor_name, product_name, "Vendor".total_employees
from
"Product"
left join "Vendor" on "Product".vendor_id = "Vendor".vendor_id
where "Vendor".total_employees;
`

This query should fetch us the vendor name and the product where the number of employees for a given vendor is less than 110.

To run the SQL query, hit the play button.

![screen shot of metabase data visualization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-06.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This will be shown below in the output window. To visualize the data, hit the visualization button.

![screen shot of metabase data visualization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-07.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Next, select the type of visualizer you want. Let us choose _Bar_.

![screen shot of metabase data visualization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-dashboard-08.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Choose the appropriate x-axis and y-axis fields, and you will be able to view the data in bar format.

![screen shot of metabase data visualization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fmetabase-report.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Conclusion [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#conclusion)

Data visualization empowers organizations to turn unused data into actionable insights, leading to faster and better decision-making. Why wait?

![screen shot of a meme saying visualization works every time](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Ffinal-meme.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

With our [Free Plan Supabase account](https://supabase.com/dashboard/), you can start a new project today and use Metabase to visualize your app data.

If you have any questions please reach out via [Twitter](https://twitter.com/supabase) or join our [Discord](https://discord.supabase.com/).

## More Python and Supabase resources [\#](https://supabase.com/blog/visualizing-supabase-data-using-metabase\#more-python-and-supabase-resources)

- [supabase-py](https://github.com/supabase-community/supabase-py)
- [Slack Consolidate: a slackbot built with Python and Supabase](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages)
- [Supabase-py (Database) on Replit](https://replit.com/@Supabase/Supabase-py-Database?v=1)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvisualizing-supabase-data-using-metabase&text=Visualizing%20Supabase%20Data%20using%20Metabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvisualizing-supabase-data-using-metabase&text=Visualizing%20Supabase%20Data%20using%20Metabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvisualizing-supabase-data-using-metabase&t=Visualizing%20Supabase%20Data%20using%20Metabase)

[Last post\\
\\
**Flutter Tutorial: building a Flutter chat app** \\
\\
30 June 2022](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)

[Next post\\
\\
**Partial data dumps using Postgres Row Level Security** \\
\\
28 June 2022](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)

[python](https://supabase.com/blog/tags/python) [open-source](https://supabase.com/blog/tags/open-source) [community](https://supabase.com/blog/tags/community)

On this page

- [Prerequisites](https://supabase.com/blog/visualizing-supabase-data-using-metabase#prerequisites)
- [Visualizing data in Supabase with Metabase](https://supabase.com/blog/visualizing-supabase-data-using-metabase#visualizing-data-in-supabase-with-metabase)
  - [Launching Metabase](https://supabase.com/blog/visualizing-supabase-data-using-metabase#launching-metabase)
  - [View Database and Tables](https://supabase.com/blog/visualizing-supabase-data-using-metabase#view-database-and-tables)
  - [View Table Data Insights](https://supabase.com/blog/visualizing-supabase-data-using-metabase#view-table-data-insights)
- [Using custom SQL queries](https://supabase.com/blog/visualizing-supabase-data-using-metabase#using-custom-sql-queries)
- [Conclusion](https://supabase.com/blog/visualizing-supabase-data-using-metabase#conclusion)
- [More Python and Supabase resources](https://supabase.com/blog/visualizing-supabase-data-using-metabase#more-python-and-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvisualizing-supabase-data-using-metabase&text=Visualizing%20Supabase%20Data%20using%20Metabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvisualizing-supabase-data-using-metabase&text=Visualizing%20Supabase%20Data%20using%20Metabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvisualizing-supabase-data-using-metabase&t=Visualizing%20Supabase%20Data%20using%20Metabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)