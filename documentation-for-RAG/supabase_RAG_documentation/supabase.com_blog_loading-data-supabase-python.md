---
url: "https://supabase.com/blog/loading-data-supabase-python"
title: "Python data loading with Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Python data loading with Supabase

17 Jun 2022

•

7 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Python data loading with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2Fpython.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Python is an excellent choice when it comes to data science. With a wide selection of libraries and built-in analytics tools, you can crunch data with ease, analyze even the most complex datasets, and visualize your results in beautiful charts and graphs.

Supabase is backend-as-a-service built on top of PostgreSQL. It's an excellent choice for building modern data-intensive apps and tooling.

Thanks to our incredible community, Supabase now has a powerful and open source [Python SDK](https://github.com/supabase-community/supabase-py). With Supabase and Python, you can automate tasks such as CRUD operations with only a few lines of code. This guide will first create a simple schema in Supabase, then we'll use the Supabase Python SDK to show how you can load sample data.

## Prerequisites [\#](https://supabase.com/blog/loading-data-supabase-python\#prerequisites)

Before we dive in, let's look at some prerequisites you'll need:

- Python version > 3.7
  - The SDK only supports version > 3.7. You can download a supported Python version from [here](https://www.python.org/downloads/).
- Python virtual environment
  - This is optional, but it will avoid issues of package dependencies and version conflicts. You can find the steps to create a virtual environment [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/). We will be using PyCharm to harness its venv creation capabilities.
- Faker python package
  - We will be using the [faker-commerce](https://pypi.org/project/faker-commerce/) package from the Faker library in Python to generate realistic sample data.

## Loading data into Supabase using Python [\#](https://supabase.com/blog/loading-data-supabase-python\#loading-data-into-supabase-using-python)

Supabase is built for developers, and you can [get started for free](https://supabase.com/dashboard) using your existing Github account. Once your Supabase account is set up, you will access the Supabase dashboard. From here, go to All Project > New Project.

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Give your project a name and set the database password. You can also choose the region and adjust the pricing plan based on the requirements of your project.

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Your project will spin up within 2 minutes.

## Creating tables in Supabase [\#](https://supabase.com/blog/loading-data-supabase-python\#creating-tables-in-supabase)

In this example, we'll be creating 2 tables in Supabase:

- Vendor (fields are vendor\_name, vendor\_location, and total\_employees)
- Product (vendor\_id as FK, product\_name, price, and total orders)

The database schema will look like the following:

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Let us now begin creating the tables. Once you create a project, you will need to go to Table Editor > New Table

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F4.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now, you can create a table according to the defined schema.

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F5.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
Click on Save to create your vendor table. Similarly, create the product table.

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F6.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Before you click Save, you need to set up the foreign key relationship between the Product and Vendor table. To do this, select the button next to “vendor\_id”

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F7.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
Select the vendor\_id primary key from the “Vendor” table.

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F8.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Click on Save and you are good to go. You should now see the 2 tables under Table Editor.

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F9.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Installing the Python SDK [\#](https://supabase.com/blog/loading-data-supabase-python\#installing-the-python-sdk)

Once you have set up the tables and installed the prerequisites, you can now start playing around with the [Python SDK](https://github.com/supabase-community/supabase-py). To install the SDK, run the following command:

`pip3 install supabase`

Ensure that you are running this inside your python virtual environment. This will take a few minutes to complete.

## Using Supabase API keys [\#](https://supabase.com/blog/loading-data-supabase-python\#using-supabase-api-keys)

The SDK authentication uses API keys pointing to a project URL. To find out your project URL and APIs, go to Settings > API.

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F10.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Setting up the environment variables [\#](https://supabase.com/blog/loading-data-supabase-python\#setting-up-the-environment-variables)

API credentials and project URL can be stored in environment variables. Setting the environment variables in bash/zsh is very simple. All we need to do is run:

`
export <variable_name>=<variable_value>
`

So for our example we will set them up like this:

`
export SUPABASE_URL=<<the value under config > URL>>
export SUPABASE_KEY=<<the value present in Project API keys > anon public>>
export SUPABASE_SECRET_KEY=<<the value present in Project API keys > service_role secret>>
`

## Inserting data into Supabase [\#](https://supabase.com/blog/loading-data-supabase-python\#inserting-data-into-supabase)

Here is a snippet of the code we will be using to insert random data into our tables:

`
import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce
def add_entries_to_vendor_table(supabase, vendor_count):
    fake = Faker()
    foreign_key_list = []
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    for i in range(vendor_count):
        value = {'vendor_name': fake.company(), 'total_employees': fake.random_int(40, 169),
                 'vendor_location': fake.country()}
        main_list.append(value)
    data = supabase.table('Vendor').insert(main_list).execute()
    data_json = json.loads(data.json())
    data_entries = data_json['data']
    for i in range(len(data_entries)):
        foreign_key_list.append(int(data_entries[i]['vendor_id']))
    return foreign_key_list
def add_entries_to_product_table(supabase, vendor_id):
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    iterator = fake.random_int(1, 15)
    for i in range(iterator):
        value = {'vendor_id': vendor_id, 'product_name': fake.ecommerce_name(),
                 'inventory_count': fake.random_int(1, 100), 'price': fake.random_int(45, 100)}
        main_list.append(value)
    data = supabase.table('Product').insert(main_list).execute()
def main():
    vendor_count = 10
    load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    fk_list = add_entries_to_vendor_table(supabase, vendor_count)
    for i in range(len(fk_list)):
        add_entries_to_product_table(supabase, fk_list[i])
main()
`

To summarize what we have done using this code snippet:

- We have inserted 10 random vendors to the table.
- For each of the 10 vendors, we have inserted a number of different products

## Reading the data stored in Supabase [\#](https://supabase.com/blog/loading-data-supabase-python\#reading-the-data-stored-in-supabase)

Data can also be viewed directly from the Supabase dashboard. To do this, go to `Table Editor > All tables`

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F11.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![screen shot of supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpython-1%2F12.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
Note: In case you cannot see any of the data, you should hit the Refresh button.

## Conclusion [\#](https://supabase.com/blog/loading-data-supabase-python\#conclusion)

With Python, data loading into Supabase is easy. It just takes a few easy steps to get started with the Python SDK and Supabase. In the next part of this blog series, we will learn [how to visualize the data that we just loaded into Supabase using Metabase](https://supabase.com/blog/visualizing-supabase-data-using-metabase). Stay tuned!

If you have any questions please reach out via [Twitter](https://twitter.com/supabase) or join our [Discord](https://discord.supabase.com/).

## More Python and Supabase resources [\#](https://supabase.com/blog/loading-data-supabase-python\#more-python-and-supabase-resources)

- [supabase-py](https://github.com/supabase-community/supabase-py)
- [Slack Consolidate: a slackbot built with Python and Supabase](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages)
- [Supabase-py (Database) on Replit](https://replit.com/@Supabase/Supabase-py-Database?v=1)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Floading-data-supabase-python&text=Python%20data%20loading%20with%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Floading-data-supabase-python&text=Python%20data%20loading%20with%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Floading-data-supabase-python&t=Python%20data%20loading%20with%20Supabase)

[Last post\\
\\
**Partial data dumps using Postgres Row Level Security** \\
\\
28 June 2022](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)

[Next post\\
\\
**Supabase Beta May 2022** \\
\\
1 June 2022](https://supabase.com/blog/beta-update-may-2022)

[python](https://supabase.com/blog/tags/python) [open-source](https://supabase.com/blog/tags/open-source) [community](https://supabase.com/blog/tags/community)

On this page

- [Prerequisites](https://supabase.com/blog/loading-data-supabase-python#prerequisites)
- [Loading data into Supabase using Python](https://supabase.com/blog/loading-data-supabase-python#loading-data-into-supabase-using-python)
- [Creating tables in Supabase](https://supabase.com/blog/loading-data-supabase-python#creating-tables-in-supabase)
- [Installing the Python SDK](https://supabase.com/blog/loading-data-supabase-python#installing-the-python-sdk)
- [Using Supabase API keys](https://supabase.com/blog/loading-data-supabase-python#using-supabase-api-keys)
- [Setting up the environment variables](https://supabase.com/blog/loading-data-supabase-python#setting-up-the-environment-variables)
- [Inserting data into Supabase](https://supabase.com/blog/loading-data-supabase-python#inserting-data-into-supabase)
- [Reading the data stored in Supabase](https://supabase.com/blog/loading-data-supabase-python#reading-the-data-stored-in-supabase)
- [Conclusion](https://supabase.com/blog/loading-data-supabase-python#conclusion)
- [More Python and Supabase resources](https://supabase.com/blog/loading-data-supabase-python#more-python-and-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Floading-data-supabase-python&text=Python%20data%20loading%20with%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Floading-data-supabase-python&text=Python%20data%20loading%20with%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Floading-data-supabase-python&t=Python%20data%20loading%20with%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)