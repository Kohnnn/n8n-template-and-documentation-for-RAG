---
url: "https://supabase.com/partners/integrations/plasmic"
title: "Plasmic | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Plasmic](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fplasmic%2Fplasmic-logo.png&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Plasmic

![Plasmic](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fplasmic%2Fplasmic-1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Plasmic](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fplasmic%2Fplasmic-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Plasmic](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fplasmic%2Fplasmic-3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

By integrating Supabase with Plasmic — a visual builder for the web — you can create data-backed applications without writing code. Although many users leverage Plasmic for rapid landing page development, this tutorial demonstrates its power as a general-purpose visual builder for React, enabling the creation of fully featured read-write applications.

## Documentation

In this guide, we’ll walk you through building a crowd-sourced Pokémon Pokédex by connecting **Supabase**, an open-source Firebase alternative, with **Plasmic**, a visual web builder.

Live demo (signing up is quick):

[https://plasmic-supabase-demo.vercel.app](https://plasmic-supabase-demo.vercel.app/)

Repository:

[https://github.com/plasmicapp/plasmic/tree/master/examples/supabase-demo](https://github.com/plasmicapp/plasmic/tree/master/examples/supabase-demo)

Plasmic project:

[https://studio.plasmic.app/projects/66RKaSPCwKxYjCfXWHCxn6](https://studio.plasmic.app/projects/66RKaSPCwKxYjCfXWHCxn6)

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/16.png)

At a high level:

- **Supabase** serves as the backend (powered by Postgres) for storing Pokémon data and managing authentication. Our code base includes React components for querying the database, displaying data, and handling user sessions.
- **Plasmic** is used to build the application’s pages and design its visual layout. We import our Supabase components into Plasmic Studio, where they can be visually arranged and configured (for instance, to display data).
- Plasmic-designed pages are rendered back into the Next.js application.

## Step 1: Set up your Backend on Supabase

- On the [Supabase dashboard](https://supabase.com/dashboard), click New project and give your project a name.

By default, Supabase configures email-based signups, storing users in the `users` table.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/15.png)

- Navigate to the **Table Editor** in the left sidebar. Here, create a **New table** to store your Pokémon entries. Ensure you are in the `schema public` view and create a table called `entries` with six columns:
  - `id`: A unique identifier for the entry, automatically generated as the primary column.
  - `user_id`: Create a relation to the user table by clicking the link 🔗 icon next to the column name and selecting the `id` column from the `user` table.
  - `name`, `description`, `imageUrl`: These columns store the Pokémon’s name, description, and image URL respectively.
  - `inserted_at`: Automatically populated with the timestamp when the row is first inserted.

> Note: In this tutorial, we’ve turned off Row Level Security (RLS). In a production environment, you should create policies that restrict who can create, edit, and delete posts. With RLS off, any user can modify the database without restrictions.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/14.png)

For convenience, you can import the following CSV file into Supabase to pre-populate your database. To import, select **Import data via spreadsheet** in the new table dialog box (this does not work on existing tables):

[pokedex-export.csv](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/documentation/pokedex-export.csv)

You’ll also need to create a function in your database to fetch the schema. This function will retrieve the Supabase database schema to display the table and column names in Plasmic Studio.

To do this, navigate to **Database** → **Functions** and click **Add a new function**.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/13.png)

Use `get_table_info` as the function name and leave the schema as public. In the **Return type** field, select `JSON`.

Paste the following function definition:

`
DECLARE
result json;
BEGIN
WITH tables AS (
    SELECT c.oid :: int8     AS id,
        nc.nspname       AS schema,
        c.relname       AS name,
        obj_description(c.oid) AS comment
    FROM  pg_namespace nc
        JOIN pg_class c
         ON nc.oid = c.relnamespace
    WHERE c.relkind IN ( 'r', 'p' )
        AND
    ( pg_has_role(c.relowner, 'USAGE')
      OR has_table_privilege(c.oid,
       'SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER')
      OR has_any_column_privilege(c.oid, 'SELECT, INSERT, UPDATE, REFERENCES')
    )
),
columns AS (
    SELECT c.table_schema AS schema,
        c.table_name AS table,
        c.column_name AS name,
        c.column_default AS default,
        c.data_type,
        c.udt_name AS format,
        (c.is_identity = 'YES') AS is_identity,
        (c.is_updatable = 'YES') AS is_updatable,
        CASE
          WHEN pk.column_name IS NOT NULL THEN TRUE
          ELSE FALSE
        END AS is_primary_key,
        array_to_json(array
                (SELECT e.enumlabel
                FROM pg_enum e
                JOIN pg_type t ON e.enumtypid = t.oid
                WHERE t.typname = udt_name
                ORDER BY e.enumsortorder)) AS enums
    FROM information_schema.columns c
    LEFT JOIN
     (SELECT ku.table_catalog,
         ku.table_schema,
         ku.table_name,
         ku.column_name
      FROM information_schema.table_constraints AS tc
      INNER JOIN information_schema.key_column_usage AS ku ON tc.constraint_type = 'PRIMARY KEY'
      AND tc.constraint_name = ku.constraint_name) pk ON c.table_catalog = pk.table_catalog
    AND c.table_schema = pk.table_schema
    AND c.table_name = pk.table_name
    AND c.column_name = pk.column_name
)
SELECT json_agg(t)
INTO result
FROM (
    SELECT
      name,
      COALESCE(
       (
        SELECT
         array_agg(
          row_to_json(columns)
         ) FILTER (
          WHERE
           columns.schema = tables.schema AND columns.table = tables.name
         )
        FROM
         columns
       ),
       '{}'::json[]
      ) AS columns
    FROM
      tables
    WHERE
      schema NOT IN (
       'information_schema', 'pg_catalog',
       'pg_temp_1', 'pg_toast', 'pg_toast_temp_1'
      ) AND
      name NOT IN ('buckets',
       'objects', 'migrations', 's3_multipart_uploads', 's3_multipart_uploads_parts', 'schema_migrations', 'subscription', 'messages')
) t;
RETURN result;
END;
`

Since we’ve disabled RLS for now, ensure that your function is executable by the anonymous user. To do this, navigate to the SQL Editor in the sidebar and run the following query:

`
GRANT EXECUTE ON FUNCTION get_table_info() TO anon;
`

> Important! Make sure to revert this step when you add RLS to your table later.

## Step 2: Set up your codebase

We have a working code example available [here](https://github.com/plasmicapp/plasmic/tree/master/examples/supabase-demo). This starter project includes all the code components you need to begin querying Supabase through Plasmic Studio.

> Code components are React components defined in your code base that we import into Plasmic Studio. Your project is configured to look for these at `http://localhost:3000/plasmic-host`. You can use and style these components in your design. See `supabase-demo/plasmic-init.ts` to understand how they are registered with Plasmic.

First, clone the repo to your development machine:

`
git clone --depth=1 git@github.com:plasmicapp/plasmic.git
cd plasmic/examples/supabase-demo/
`

Copy `.env.example` to `.env` to store your environment variables for the local development server. Then, add your Supabase project’s URL and public key (found in the API tab on the left pane of your Supabase dashboard).

Install the dependencies and fetch the Supabase schema by running:

`
yarn
`

Now, start the development server (it listens on [http://localhost:3000](http://localhost:3000/)):

`
yarn dev
`

## Step 3: Explore the existing application

Open [http://localhost:3000](http://localhost:3000/) in your web browser. The project is already set up for user sign-ups and logins and includes an admin interface for adding and editing Pokémon in the database. Feel free to sign up with your email address and add Pokémon entries. Note that Supabase requires email verification before you can log in.

If you pre-populated the database in Step 1, you should see the following homepage after logging in. Otherwise, you can manually add Pokémon via the UI.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/12.png)

## Step 4: Clone the Plasmic project

Now, let’s make some enhancements! The code base is initially set up with a read-only copy of the Plasmic project. Let’s create an editable copy first.

Open the default starter Plasmic project here:

[https://studio.plasmic.app/projects/66RKaSPCwKxYjCfXWHCxn6](https://studio.plasmic.app/projects/66RKaSPCwKxYjCfXWHCxn6)

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/11.png)

To create an editable copy, click the **Copy Project** button in the blue bar. This will clone the project and redirect you to your copy.

### Step 4a: Configure your code base to use the new Plasmic project

Take note of the `project ID` and `API token`. You can find the project ID in the URL:

`https://studio.plasmic.app/projects/PROJECTID`.

The API token is available by clicking the **Code** button in the top bar.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/10.png)

Return to `.env` and update the corresponding project ID and token fields.

### Step 4b: Configure your Plasmic project app host

To ensure Plasmic looks for your code components on your development server, update your project’s app host to [http://localhost:3000/plasmic-host](http://localhost:3000/plasmic-host).

> **Note**: Keep your development server running at [http://localhost:3000](http://localhost:3000/) for the project to load.

After restarting both the dev server and Plasmic Studio, you should be able to edit both the Studio and your codebase.

## Step 4: Deployment (optional)

You can host your application using Vercel, Netlify, AWS, or any other provider you prefer.

In this section, we will cover deployment using Vercel:

1. First, create a GitHub repository for your project.
2. Next, log into vercel.app and add a new project.
3. Point to the repository you created in the first step.
4. Go to the project settings.
5. Set the Build & Development settings to the following:

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/9.png)

6. Set the Node.js version to 20.x.
7. Go to the Environment Variables tab and copy the contents of your .env file.
8. Trigger a deployment of your project.
9. (optional) go back to step 4b, and point to your /plasmic-host page using your newly created domain. (for example, [https://plasmic-supabase-demo.vercel.app/plasmic-host](https://plasmic-supabase-demo.vercel.app/plasmic-host))

You can also refer to this [video](https://www.youtube.com/watch?v=atSGchKVe5I&ab_channel=Plasmic) to see how another project is configured on Vercel and Netlify.

You are not able to use Plasmic hosting for this example, because it uses code components. Plasmic hosting does not have access to your codebase, meaning you would need to host your Next.js server using 3rd party providers.

## Step 5: Create a new page – Look up Pokémon by name

Let’s create a lookup page for our Pokédex using the code components from the code base.

1. Create a new page called `Guess` and set its path to `/guess`.
2. Add a NavBar and any additional elements to enhance the layout (we used two vertical containers for background and centering).
3. Insert a `SupabaseDataProvider` by opening the AddDrawer (click the blue + button).

> For source, see `components/CodeComponents/DatabaseComponents/SupabaseDataProvider`.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/8.png)

Above the `SupabaseDataProvider`, add a text input element and a heading. Change the text input’s placeholder to `Type your guess`. Your layout should resemble the following:

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/7.png)

Next, configure the props for the `SupabaseDataProvider` in the right-hand panel:

- **Table:** Set this to the table you created in Supabase.
- **Columns:** Provide a comma-separated list of the columns you want to select from the table.
- **Filters:** Define which data to fetch (similar to a WHERE clause).
- **Single:** Specify whether to fetch a single record or multiple records.

Additionally, we set a visibility condition so that data is fetched only when the input contains more than three characters.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/6.png)

This is how the filter parameter should appear, with the operation set to eq (meaning it will fetch records where the property equals a specific value).

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/5.png)

The `SupabaseDataProvider` passes down the fetched data, leaving it up to you to decide how to use it.

Next, add a `Post` component (used on the homepage) to display the Pokémon.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/4.png)

If no matching Pokémon exists in the database, configure a nearby text node to inform the user. Control its visibility based on the data from the `SupabaseDataProvider`—this is how you can access that data in the Studio:

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/3.png)

Finally, add your new page as a link in the NavBar component. Try this as an exercise 🙂

## Step 6: Check your dev server

If your development server has been running all along, you’ll notice that the site automatically fetches and rebuilds as you make changes in Plasmic Studio. To restart the dev server, run:

`
yarn dev
`

Then, view the results at [http://localhost:3000/guess](http://localhost:3000/guess)

## How does this all work under the hood?

All the code components are defined in your codebase, and you’re free to enhance them to support more powerful querying capabilities in Plasmic Studio.

### Email Verification API Route

To sign up, users must verify their email address. After signing up, they receive an email with a verification link. Clicking the link directs them to the API route at `/pages/api/auth/confirm.ts`, which confirms the OTP code and redirects them to the homepage.

Learn more here: [https://supabase.com/docs/guides/auth/server-side/nextjs?queryGroups=router&router=pages](https://supabase.com/docs/guides/auth/server-side/nextjs?queryGroups=router&router=pages)

### SupabaseDataProvider

This simple component executes queries and populates the application's data. If your data is mostly static, consider using `usePlasmicQueryData` instead of the mutable version.

``
import { Database } from "@/types/supabase";
import { createSupabaseClient } from "@/util/supabase/component";
import { Filter, applyFilter, isValidFilter } from "@/util/supabase/helpers";
import {
DataProvider,
usePlasmicCanvasContext,
useSelector,
} from "@plasmicapp/loader-nextjs";
import { useMutablePlasmicQueryData } from "@plasmicapp/query";
import { ReactNode } from "react";
export interface SupabaseDataProviderProps {
children?: ReactNode;
tableName?: keyof Database["public"]["Tables"];
columns?: string[];
className?: string;
filters?: any;
single?: boolean;
}
export function SupabaseDataProvider(props: SupabaseDataProviderProps) {
const supabase = createSupabaseClient();
const inEditor = usePlasmicCanvasContext();
// These props are set in the Plasmic Studio
const { children, tableName, columns, className, filters, single } = props;
const currentUser = useSelector("auth");
const validFilters = filters?.filter((f: any) => isValidFilter(f)) as
    | Filter[]
    | undefined;
const selectFields = columns?.join(",") || "";
// Error messages are currently rendered in the component
if (!tableName) {
    return <p>You need to set the tableName prop</p>;
} else if (!selectFields) {
    return <p>You need to set the columns prop</p>;
}
// Performs the Supabase query
async function makeQuery() {
    // dont perform query if user is not logged in.
    // allow to query in editor mode for demo purposes
    if (!inEditor && !currentUser?.email) {
      return;
    }
    let query = supabase.from(tableName!).select(selectFields || "");
    query = applyFilter(query, validFilters);
    // This is where the Single property comes into play—either querying for a single record or multiple records.
    const { data, error, status } = await (single
      ? query.single()
      : query.order("id", { ascending: false }));
    if (error && status !== 406) {
      throw error;
    }
    return data;
}
// The first parameter is a unique cache key for the query.
// If you want to update the cache - you are able to use the Refresh Data function in the Plasmic Studio.
const { data } = useMutablePlasmicQueryData(
    `${tableName}-${JSON.stringify(filters)}`,
    async () => {
      try {
        return await makeQuery();
      } catch (err) {
        console.error(err);
        return {};
      }
      // As an additional way to control the cache flow - you are able to specify the revalidate options.
      // For example, you can revalidate the data on mount and on page focus, to make sure that data is always up-to-date.
      // If your data is mostly static - turn these options off.
    },
    { revalidateOnMount: true, revalidateOnFocus: true }
);
return (
    <div className={className}>
      <DataProvider name={tableName} data={data}>
        {children}
      </DataProvider>
    </div>
);
}
``

**How it is registered:**

`
// /plasmic-init.ts
PLASMIC.registerComponent(SupabaseQuery, {
name: "SupabaseQuery",
providesData: true,
props: {
    children: "slot",
    tableName: tableNameProp,
    columns: {
      ...columnProp,
      multiSelect: true,
    },
    filters: filtersProp,
    single: "boolean",
},
importPath: "./components/CodeComponents/DatabaseComponents",
});
`

The shared props for this registration are defined below. We use the `dbSchema` variable from an auto-generated file that fetches the Supabase schema. This file refreshes during `yarn build` or when you run `yarn`, allowing the Studio to display current tables and columns without hardcoding them.

`
const tableNameProp = {
type: "choice" as const,
multiSelect: false,
options: dbSchema.map((table) => table.name) || [],
};
const columnProp = {
type: "choice" as const,
options: (props: any) => {
    const table = dbSchema.find((t) => t.name === props.tableName);
    return table?.columns?.map((column) => column.name) ?? [];
},
};
const filtersProp = {
type: "array" as const,
nameFunc: (item: any) => item.name || item.key,
itemType: {
    type: "object" as const,
    fields: {
      name: {
        type: "choice" as const,
        options: ["eq", "match"],
      },
      args: {
        type: "array" as const,
        itemType: {
          type: "object" as const,
          fields: {
            column: columnProp,
            value: "string" as const,
          },
        },
      },
    },
},
};
`

### SupabaseForm

This component performs database mutations (such as delete, update, or insert operations). It wraps form elements and calls an action upon submission. In most cases, a submit button triggers the form, and the `onSuccess` hook is useful for redirecting the user or refreshing page data.

`
import { Database } from "@/types/supabase";
import { createSupabaseClient } from "@/util/supabase/component";
import { Filter, applyFilter, isValidFilter } from "@/util/supabase/helpers";
import React, { ReactNode } from "react";
export interface SupabaseFormProps {
children?: ReactNode;
tableName?: keyof Database["public"]["Tables"];
method?: "upsert" | "insert" | "update" | "delete";
filters?: any;
data?: any;
onSuccess?: () => void;
className?: string;
}
export function SupabaseForm(props: SupabaseFormProps) {
const { children, tableName, method, filters, data, className, onSuccess } =
    props;
const supabase = createSupabaseClient();
if (!tableName) {
    return <p>You need to set the tableName prop</p>;
}
if (!method) {
    return <p>You need to choose a method</p>;
}
if (method !== "delete" && !data) {
    return <p>You need to set the data prop</p>;
}
const validFilters = filters?.filter((f: any) => isValidFilter(f)) as
    | Filter[]
    | undefined;
async function onSubmit(e: React.FormEvent) {
    e?.preventDefault();
    try {
      const table = supabase.from(tableName!);
      let query: any;
      switch (method) {
        case "update": {
          query = table.update(data);
          break;
        }
        case "upsert": {
          query = table.upsert(data);
        }
        case "insert": {
          query = table.insert(data);
        }
        case "delete": {
          query = table.delete();
        }
        default: {
          throw new Error("Invalid method");
        }
      }
      query = applyFilter(query, validFilters);
      const { error } = await query;
      if (error) {
        console.error(error);
      } else if (onSuccess) {
        onSuccess();
      }
    } catch (error) {
      console.error(error);
    }
}
return (
    <form onSubmit={onSubmit} className={className}>
      {children}
    </form>
);
}
`

**How it is registered:**

`
PLASMIC.registerComponent(SupabaseForm, {
name: "SupabaseForm",
props: {
    children: "slot",
    tableName: tableNameProp,
    filters: filtersProp,
    method: {
      type: "choice",
      options: ["upsert", "insert", "update", "delete"],
    },
    data: "exprEditor",
    onSuccess: {
      type: "eventHandler",
      argTypes: [],
    },
},
});
`

### SupabaseUserSession

This component provides global user data across the application and is registered as a [GlobalContext](https://docs.plasmic.app/learn/global-contexts/). If you’d prefer not to log in every time to see content from a specific user’s perspective, you can set a `staticToken` in the context settings.

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/2.png)

You can find the authentication token from the hosted application by inspecting any network request. The token is in the Authentication header (everything after “Bearer”).

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/plasmic/1.png)

**Source code:**

`
import { createSupabaseClient } from "@/util/supabase/component";
import {
DataProvider,
usePlasmicCanvasContext,
} from "@plasmicapp/loader-nextjs";
import { User } from "@supabase/supabase-js";
import React from "react";
export function SupabaseUserSession({
children,
staticToken,
}: {
className?: string;
staticToken?: string;
children?: React.ReactNode;
}) {
const supabase = createSupabaseClient();
const [currentUser, setCurrentUser] = React.useState<User | null>(null);
const [isLoaded, setIsLoaded] = React.useState(false);
const inEditor = usePlasmicCanvasContext();
React.useEffect(() => {
    if (inEditor) {
      if (staticToken) {
        supabase.auth
          .getUser(staticToken)
          .then((res) => {
            setCurrentUser(res.data.user);
          })
          .finally(() => {
            setIsLoaded(true);
          });
      }
      return;
    }
    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((event, session) => {
      if (event == "SIGNED_OUT") {
        setCurrentUser(null);
      } else if (["SIGNED_IN", "INITIAL_SESSION"].includes(event) && session) {
        setCurrentUser(session.user);
      }
      setIsLoaded(true);
    });
    return subscription.unsubscribe;
}, []);
return (
    <DataProvider name="auth" data={currentUser || {}}>
      {isLoaded && children}
    </DataProvider>
);
}
`

**How it is registered:**

`
PLASMIC.registerGlobalContext(SupabaseUserSession, {
name: "SupabaseUserSession",
importPath: "./components/CodeComponents/GlobalContexts",
providesData: true,
props: { staticToken: "string" },
});
`

### RedirectIf

This component redirects the user based on a condition you specify. In our example, it redirects users from inner pages if they are not logged in.

**Source code:**

`
import { usePlasmicCanvasContext } from "@plasmicapp/loader-nextjs";
import React from "react";
export interface RedirectIfProps {
children?: any;
className?: string;
condition?: any;
onFalse?: () => void;
}
export function RedirectIf(props: RedirectIfProps) {
const { children, className, onFalse, condition } = props;
const inEditor = usePlasmicCanvasContext();
React.useEffect(() => {
    if (inEditor || !onFalse || condition) {
      return;
    }
    onFalse();
}, [condition, inEditor]);
// Validation
if (typeof condition === "undefined") {
    return (
      <p>
        Condition needs to be a boolean prop. Try to add exclamation marks to
        the value.
      </p>
    );
}
return <div className={className}>{children}</div>;
}
`

**And how it is registered:**

`
PLASMIC.registerComponent(RedirectIf, {
name: "RedirectIf",
props: {
    children: "slot",
    onFalse: {
      type: "eventHandler",
      argTypes: [],
    },
    condition: "exprEditor",
},
});
`

## Details

Watch an introductory video

![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

DeveloperPlasmic

Category [Low-Code](https://supabase.com/partners/integrations#low-code)

Website [www.plasmic.app](https://www.plasmic.app/)

Documentation [Learn](https://www.plasmic.app/)

Third-party integrations and docs are managed by Supabase partners.