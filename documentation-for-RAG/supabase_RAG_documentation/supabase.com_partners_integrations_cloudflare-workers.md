---
url: "https://supabase.com/partners/integrations/cloudflare-workers"
title: "CloudFlare Workers | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![CloudFlare Workers](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fcloudflare-integration%2Fcloudflare_workers_logo.png%3Ft%3D2023-07-21T11%253A07%253A47.005Z&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# CloudFlare Workers

## Overview

Using Supabase in Cloudflare Workers has always been a great way to interact with your data from the edge. Supabase-js communicates with your Supabase Postgres instance via HTTP using PostgREST, so you never need to worry about running out of database connections.

In this guide we'll walk you through a new addition to the Cloudflare Workers dashboard - the ability to authenticate directly with your Supabase account, and automatically inject your Supabase environment variables into your Worker code.

## How To Enable Supabase Integration in Cloudflare Workers

Start by heading to the [Cloudflare Dashboard](https://dash.cloudflare.com/), go to the Workers & Pages tab and hit 'Create Application' followed by 'Create Worker'.

![Cloudflare Dashboard 2](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/2.png)

Deploy the Hello World example Worker. Once it's deployed hit 'Configure Worker'.

![Cloudflare Dashboard 3](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/3.png)

On the configuration page select the Settings tab, followed by the Integrations option.

You should now see the database integration options. On the Supabase card, click 'Add Integration'

![Cloudflare Dashboard 4](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/4.png)

After reviewing and accepting the terms, you will be shown the option to connect and a Supabase popup should appear.

Follow the flow by selecting your Supabase Org and the Project you wish to connect to. If you don't have any projects yet, head over to the [Supabase Dashboard](https://supabase.com/dashboard) to create one.

![Cloudflare Dashboard 5](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/5.png)

Once it's connected you will be given the option to select which Supabase Key you want to pull into the Worker context.

The `Anon` key here is one that always adhires to the Database's RLS policies (read more on [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security)).

The `Service Role` is typically ok to use in backend contexts, such as Cloudflare Workers, but note that this key **bypasses your Row Level Security policies**, and has the ablity to read, write, and delete any data in your database.

![Cloudflare Dashboard 6](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/6.png)

Once this is done the `SUPABASE_KEY` and `SUPABASE_URL` environment variables will now be available from your Cloudflare Worker code.

![Cloudflare Dashboard 7](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/7.png)

You can now install the supabase-js client in your Worker:

`npm install @supabase/supabase-js`

Then you can initiate the Supabase client, and start querying your data:

`
import { createClient } from '@supabase/supabase-js'
export default {
async fetch(request, env) {
    const supabase = createClient(env.SUPABASE_URL, env.SUPABASE_KEY)
    const { data, error } = await supabase.from('countries').select('*')
    if (error) throw error
    return new Response(JSON.stringify(data), {
      headers: {
        'Content-Type': 'application/json',
      },
    })
},
}
`

The snippet above assumes you already have a `countries` table. Run the following in the [SQL Editor in the Supabase Dashboard](https://supabase.com/dashboard/project/_/sql) if you wish to install this demo schema:

`
create table countries (
id serial primary key,
name varchar(255) not null
);
insert into countries
(name)
values
('Oceania');
insert into countries
(name)
values
('Genovia');
insert into countries
(name)
values
('Wakanda');
insert into countries
(name)
values
('Lilliput');
`

Remember that you don't need to use supabase-js to connect to your Supabase database, you can connect "directly" to the underlying Postgres database using the connection string (every Supabase database comes pre-installed with a [connection pooler](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pool)), or you can try Cloudflare's new [TCP socket method of connecting to Postgres](https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/) directly from Cloudflare Workers.

- [Cloudflare Integration Docs](https://developers.cloudflare.com/workers/learning/integrations/databases/#supabase).
- [Cloudflare Dashboard](https://dash.cloudflare.com/).
- [Cloudflare Integration Announcement](https://blog.cloudflare.com/announcing-database-integrations/).

## Details

DeveloperCloudFlare

Category [DevTools](https://supabase.com/partners/integrations#devtools)

Website [workers.cloudflare.com](https://workers.cloudflare.com/)

Documentation [Learn](https://workers.cloudflare.com/)

Third-party integrations and docs are managed by Supabase partners.