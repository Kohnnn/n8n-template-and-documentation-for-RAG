---
url: "https://supabase.com/blog/local-first-expo-legend-state"
title: "Local-first Realtime Apps with Expo and Legend-State"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Local-first Realtime Apps with Expo and Legend-State

23 Sep 2024

•

11 minute read

[![Jay Meistrich avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjmeistrich.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jay MeistrichGuest Author](https://x.com/jmeistrich)

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Local-first Realtime Apps with Expo and Legend-State](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flocal-first-expo-legend_state%2Flocal-first-expo-legend_state-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Do you prefer audio-visual learning? Watch the video guide!](https://supabase.link/local-first-expo-legend-state-yt)

[Or jump straight into the code](https://github.com/expo/examples/tree/master/with-legend-state-supabase)

Or run `npx create-expo-app --example with-legend-state-supabase` to create a new app with this example.

[Legend-State](https://legendapp.com/open-source/state/v3/) is a super fast all-in-one state and sync library that lets you write less code to make faster apps. Legend-State has four primary goals:

1. As easy as possible to use.
2. The fastest React state library.
3. Fine-grained reactivity for minimal renders.
4. Powerful sync and persistence (with Supabase support built in!)

And, to put the cherry on top, it works with Expo and React Native (via [React Native Async Storage](https://github.com/react-native-async-storage/async-storage?tab=readme-ov-file#react-native-async-storage)). This makes it a perfect match for building local-first mobile and web apps.

## What is a Local-First Architecture? [\#](https://supabase.com/blog/local-first-expo-legend-state\#what-is-a-local-first-architecture)

In local-first software, "the availability of another computer should never prevent you from working" ( [via Martin Kleppmann](https://www.youtube.com/watch?v=NMq0vncHJvU)). When you are offline, you can still read and write directly from/to a database on your device. You can trust the software to work offline, and you know that when you are connected to the internet, your data will be seamlessly synced and available on any of your devices running the app. When you're online, this architecture is well suited for "multiplayer" apps, as [popularized by Figma](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/).

To dig deeper into what local-first is and how it works, refer to the [Expo docs](https://docs.expo.dev/guides/local-first/).

## How Legend-State makes it work [\#](https://supabase.com/blog/local-first-expo-legend-state\#how-legend-state-makes-it-work)

A primary goal of Legend-State is to make automatic persisting and syncing both easy and very robust, as it's meant to be used to power all storage and sync of complex apps.

Any changes made while offline are persisted between sessions to be retried whenever connected. To do this, the sync system subscribes to changes on an observable, then on change goes through a multi-step flow to ensure that changes are persisted and synced.

1. Save the pending changes to local persistence.
2. Save the changes to local persistence.
3. Save the changes to remote persistence.
4. On remote save, set any needed changes (like updated\_at) back into the observable and local persistence.
5. Clear the pending changes in local persistence.

## Setting up the Project [\#](https://supabase.com/blog/local-first-expo-legend-state\#setting-up-the-project)

To set up a new React Native project you can use the `create-expo-app` utility. You can create a blank app or choose from different [examples](https://github.com/expo/examples).

For this tutorial, go ahead and create a new blank Expo app:

`
npx create-expo-app@latest --template blank
`

## Installing Dependencies [\#](https://supabase.com/blog/local-first-expo-legend-state\#installing-dependencies)

The main dependencies you need are [Legend State](https://www.npmjs.com/package/@legendapp/state) and [supabase-js](https://www.npmjs.com/package/@supabase/supabase-js). Additionally, to make things work for React Native, you will need [React Native Async Storage](https://github.com/react-native-async-storage/async-storage?tab=readme-ov-file#react-native-async-storage) and [react-native-get-random-values](https://www.npmjs.com/package/react-native-get-random-values) (to generate uuids).

Install the required dependencies via `expo install`:

`
npx expo install @legendapp/state@beta @supabase/supabase-js react-native-get-random-values @react-native-async-storage/async-storage
`

## Configuring Supabase [\#](https://supabase.com/blog/local-first-expo-legend-state\#configuring-supabase)

If you don't have a Supabase project already, head over to [database.new](https://database.new/) and create a new project.

Next, create a `.env.local` file in the root of your project and add the following env vars. You can find these in your [Supabase dashboard](https://supabase.com/dashboard/project/_/settings/api).

`
EXPO_PUBLIC_SUPABASE_URL=
EXPO_PUBLIC_SUPABASE_ANON_KEY=
`

Next, set up a utils file to hold all the logic for interacting with Supabase, we'll call it `utils/SupaLegend.ts`.

utils/SupaLegend.ts

`
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(
process.env.EXPO_PUBLIC_SUPABASE_URL,
process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
)
`

## Configuring Legend-State [\#](https://supabase.com/blog/local-first-expo-legend-state\#configuring-legend-state)

Legend-State is very versatile and allows you to choose different persistence and storage strategies. For this example, we'll use `React Native Async Storage` for local persistence across platforms and `supabase` for remote persistence.

Extend your `utils/SupaLegend.ts` file with the following configuration:

utils/SupaLegend.ts

`
import { createClient } from '@supabase/supabase-js'
import { observable } from '@legendapp/state'
import { syncedSupabase } from '@legendapp/state/sync-plugins/supabase'
import { configureSynced } from '@legendapp/state/sync'
import { observablePersistAsyncStorage } from '@legendapp/state/persist-plugins/async-storage'
import AsyncStorage from '@react-native-async-storage/async-storage'
const supabase = createClient(
process.env.EXPO_PUBLIC_SUPABASE_URL,
process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
)
// Create a configured sync function
const customSynced = configureSynced(syncedSupabase, {
// Use React Native Async Storage
persist: {
    plugin: observablePersistAsyncStorage({
      AsyncStorage,
    }),
},
generateId,
supabase,
changesSince: 'last-sync',
fieldCreatedAt: 'created_at',
fieldUpdatedAt: 'updated_at',
// Optionally enable soft deletes
fieldDeleted: 'deleted',
})
export const todos$ = observable(
customSynced({
    supabase,
    collection: 'todos',
    select: (from) => from.select('id,counter,text,done,created_at,updated_at,deleted'),
    actions: ['read', 'create', 'update', 'delete'],
    realtime: true,
    // Persist data and pending changes locally
    persist: {
      name: 'todos',
      retrySync: true, // Persist pending changes and retry
    },
    retry: {
      infinite: true, // Retry changes with exponential backoff
    },
})
)
`

`syncedSupabase` is the Legend-State sync plugin for Supabase and adds some default configuration for usage with supabase-js.

## Setting up the Database Schema [\#](https://supabase.com/blog/local-first-expo-legend-state\#setting-up-the-database-schema)

If you haven't alread, install the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) and run `supabase init` to initialize your project.

Next, create the initial database migration to set up the `todos` table:

`
supabase migrations new init
`

This will create a new SQL migration file in the `supabase/migrations` directory. Open it and add the following SQL code:

`
create table todos (
id uuid default gen_random_uuid() primary key,
counter bigint generated by default as identity,
text text,
done boolean default false,
created_at timestamptz default now(),
updated_at timestamptz default now(),
deleted boolean default false -- needed for soft deletes
);
-- Enable realtime
alter
publication supabase_realtime add table todos;
-- Legend-State helper to facilitate "Sync only diffs" (changesSince: 'last-sync') mode
CREATE OR REPLACE FUNCTION handle_times()
    RETURNS trigger AS
    $$
    BEGIN
    IF (TG_OP = 'INSERT') THEN
        NEW.created_at := now();
        NEW.updated_at := now();
    ELSEIF (TG_OP = 'UPDATE') THEN
        NEW.created_at = OLD.created_at;
        NEW.updated_at = now();
    END IF;
    RETURN NEW;
    END;
    $$ language plpgsql;
CREATE TRIGGER handle_times
    BEFORE INSERT OR UPDATE ON todos
    FOR EACH ROW
EXECUTE PROCEDURE handle_times();
`

The `created_at`, `updated_at`, and `deleted` columns are used by Legend-State to track changes and sync efficiently. The `handle_times` function is used to automatically set the `created_at` and `updated_at` columns when a new row is inserted or an existing row is updated. This allows to efficiently sync only the changes since the last sync.

Next, run `supabase link` to link your local project to your Supabase project and run `supabase db push` to apply the init migration to your Supabase database.

## Generating TypeScript Types [\#](https://supabase.com/blog/local-first-expo-legend-state\#generating-typescript-types)

Legend-State integrates with supabase-js to provide end-to-end type safety. This means you can use the existing [Supabase CLI workflow](https://supabase.com/docs/guides/api/rest/generating-types) to generate TypeScript types for your Supabase tables.

`
supabase start
supabase gen types --lang=typescript --local > utils/database.types.ts
`

Next, in your `utils/SupaLegend.ts` file, import the generated types inject them into the Supabase client.

utils/SupaLegend.ts

`
import { createClient } from '@supabase/supabase-js'
import { Database } from './database.types'
// [...]
const supabase = createClient<Database>(
process.env.EXPO_PUBLIC_SUPABASE_URL,
process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
)
// [...]
`

From here, Legend-State will automatically infer the types for your Supabase tables and make them available within the observable.

## Fetching Data and subscribing to realtime updates [\#](https://supabase.com/blog/local-first-expo-legend-state\#fetching-data-and-subscribing-to-realtime-updates)

Above, you've configured the `todos$` observable. You can now import this in your `tsx` files to fetch and automatically sync changes.

App.tsx

`
import { observer } from '@legendapp/state/react'
import { todos$ as _todos$ } from './utils/SupaLegend'
const Todos = observer(({ todos$ }: { todos$: typeof _todos$ }) => {
// Get the todos from the state and subscribe to updates
const todos = todos$.get()
const renderItem = ({ item: todo }: { item: Tables<'todos'> }) => <Todo todo={todo} />
if (todos)
    return <FlatList data={Object.values(todos)} renderItem={renderItem} style={styles.todos} />
return <></>
})
`

`observer` is the suggested way of consuming observables for the best performance and safety.

It turns the entire component into an observing context - it automatically tracks observables for changes when `get()` is called, even from within hooks or helper functions.

This means, as long as realtime is enabled on the respective table, the component will automatically update when changes are made to the data!

Also, thanks to the persist and retry settings above, Legend-State will automatically retry to sync changes if the connection is lost.

## Inserting, and updating data [\#](https://supabase.com/blog/local-first-expo-legend-state\#inserting-and-updating-data)

To add a new todo from the application, you will need to generate a uuid locally to insert it into our todos observable. You can use the `uuid` package to generate a uuid. For this to work in React Native you will also need the `react-native-get-random-values` polyfill.

In your `SupaLegend.ts` file add the following:

utils/SupaLegend.ts

`
// [...]
import 'react-native-get-random-values'
import { v4 as uuidv4 } from 'uuid'
// [...]
// Provide a function to generate ids locally
const generateId = () => uuidv4()
export function addTodo(text: string) {
const id = generateId()
// Add keyed by id to the todos$ observable to trigger a create in Supabase
todos$[id].assign({
    id,
    text,
})
}
export function toggleDone(id: string) {
todos$[id].done.set((prev) => !prev)
}
`

Now, in your `App.tsx` file, you can import the `addTodo` and `toggleDone` methods and call them when the user submits a new todo or checks off one:

App.tsx

`
import { useState } from 'react'
import { FlatList, StyleSheet, Text, TextInput, TouchableOpacity } from 'react-native'
// [...]
import { observer } from '@legendapp/state/react'
import { addTodo, todos$ as _todos$, toggleDone } from './utils/SupaLegend'
// [...]
// Emojis to decorate each todo.
const NOT_DONE_ICON = String.fromCodePoint(0x1f7e0)
const DONE_ICON = String.fromCodePoint(0x2705)
// The text input component to add a new todo.
const NewTodo = () => {
const [text, setText] = useState('')
const handleSubmitEditing = ({ nativeEvent: { text } }) => {
    setText('')
    addTodo(text)
}
return (
    <TextInput
      value={text}
      onChangeText={(text) => setText(text)}
      onSubmitEditing={handleSubmitEditing}
      placeholder="What do you want to do today?"
      style={styles.input}
    />
)
}
// A single todo component, either 'not done' or 'done': press to toggle.
const Todo = ({ todo }: { todo: Tables<'todos'> }) => {
const handlePress = () => {
    toggleDone(todo.id)
}
return (
    <TouchableOpacity
      key={todo.id}
      onPress={handlePress}
      style={[styles.todo, todo.done ? styles.done : null]}
    >
      <Text style={styles.todoText}>
        {todo.done ? DONE_ICON : NOT_DONE_ICON} {todo.text}
      </Text>
    </TouchableOpacity>
)
}
`

## Up next: Adding Auth [\#](https://supabase.com/blog/local-first-expo-legend-state\#up-next-adding-auth)

Since Legend-State utilizes supabase-js under the hood, you can use [Supabase Auth](https://supabase.com/docs/guides/auth) and [row level security](https://supabase.com/docs/guides/database/postgres/row-level-security) to restrict access to the data.

For a tutorial on how to add user management to your Expo React Native application, refer to [this guide](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native).

## Conclusion [\#](https://supabase.com/blog/local-first-expo-legend-state\#conclusion)

Legend-State and Supabase are a powerful combination for building local-first applications. Legend-State pairs nicely with supabase-js, Supabase Auth and Supabase Realtime, allowing you to tap into the full power of the Supabase Stack while building fast and delightful applications that work across web and mobile platforms.

Want to learn more about Legend-State? Refer to their [docs](https://legendapp.com/open-source/state/v3/) and make sure to follow Jay Meistrich on [Twitter](https://twitter.com/jmeistrich)!

## More Supabase Resources [\#](https://supabase.com/blog/local-first-expo-legend-state\#more-supabase-resources)

- [Expo User Management Tutorial](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native)
- [React Native Auth](https://supabase.com/blog/react-native-authentication)
- [React Native File Upload](https://supabase.com/blog/react-native-storage)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flocal-first-expo-legend-state&text=Local-first%20Realtime%20Apps%20with%20Expo%20and%20Legend-State)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flocal-first-expo-legend-state&text=Local-first%20Realtime%20Apps%20with%20Expo%20and%20Legend-State)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flocal-first-expo-legend-state&t=Local-first%20Realtime%20Apps%20with%20Expo%20and%20Legend-State)

[Last post\\
\\
**Supabase Launch Week 12 Hackathon Winners** \\
\\
30 September 2024](https://supabase.com/blog/lw12-hackathon-winners)

[Next post\\
\\
**Edge Functions are now 2x smaller and boot 3x faster** \\
\\
12 September 2024](https://supabase.com/blog/edge-functions-faster-smaller)

[mobile](https://supabase.com/blog/tags/mobile) [local-first](https://supabase.com/blog/tags/local-first) [react-native](https://supabase.com/blog/tags/react-native)

On this page

- [What is a Local-First Architecture?](https://supabase.com/blog/local-first-expo-legend-state#what-is-a-local-first-architecture)
- [How Legend-State makes it work](https://supabase.com/blog/local-first-expo-legend-state#how-legend-state-makes-it-work)
- [Setting up the Project](https://supabase.com/blog/local-first-expo-legend-state#setting-up-the-project)
- [Installing Dependencies](https://supabase.com/blog/local-first-expo-legend-state#installing-dependencies)
- [Configuring Supabase](https://supabase.com/blog/local-first-expo-legend-state#configuring-supabase)
- [Configuring Legend-State](https://supabase.com/blog/local-first-expo-legend-state#configuring-legend-state)
- [Setting up the Database Schema](https://supabase.com/blog/local-first-expo-legend-state#setting-up-the-database-schema)
- [Generating TypeScript Types](https://supabase.com/blog/local-first-expo-legend-state#generating-typescript-types)
- [Fetching Data and subscribing to realtime updates](https://supabase.com/blog/local-first-expo-legend-state#fetching-data-and-subscribing-to-realtime-updates)
- [Inserting, and updating data](https://supabase.com/blog/local-first-expo-legend-state#inserting-and-updating-data)
- [Up next: Adding Auth](https://supabase.com/blog/local-first-expo-legend-state#up-next-adding-auth)
- [Conclusion](https://supabase.com/blog/local-first-expo-legend-state#conclusion)
- [More Supabase Resources](https://supabase.com/blog/local-first-expo-legend-state#more-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flocal-first-expo-legend-state&text=Local-first%20Realtime%20Apps%20with%20Expo%20and%20Legend-State)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flocal-first-expo-legend-state&text=Local-first%20Realtime%20Apps%20with%20Expo%20and%20Legend-State)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flocal-first-expo-legend-state&t=Local-first%20Realtime%20Apps%20with%20Expo%20and%20Legend-State)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)