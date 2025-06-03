---
url: "https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre"
title: "Postgres Realtime location sharing with MapLibre"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Postgres Realtime location sharing with MapLibre

04 Jul 2024

•

8 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Postgres Realtime location sharing with MapLibre](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgres_realtime_maplibre%2Fpostgres_realtime_maplibre.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Do you prefer audio-visual learning? Watch the video guide!](https://supabase.link/realtime-maps-yt)

[Or jump straight into the code](https://supabase.link/realtime-maps-gh)

This tutorial is building upon the previous learnings on Postgis and Supabase and adding Supabase Realtime on top. If you're new to this topic, we recommend you review the following first:

- Getting started with PostGIS and Supabase [\[video\]](https://supabase.link/postgis-quickstart-yt) [\[docs\]](https://supabase.com/docs/guides/database/extensions/postgis)
- Self-host Maps with Protomaps and Supabase Storage [\[video\]](https://supabase.link/protomaps-storage-yt) [\[blog\]](https://supabase.com/blog/self-host-maps-storage-protomaps)
- Generate Vector Tiles with PostGIS [\[video\]](https://supabase.link/supa-gis-yt) [\[blog\]](https://supabase.com/blog/postgis-generate-vector-tiles)

In this tutorial, you will learn to

- Use a Supabase Edge Function to build a Telegram Bot that captures live location data.
- Use an RPC (remote procedure call) to insert location data into Postgres from an Edge Function.
- Use Supabase Realtime to listen to changes in the database.
- Use MapLibre GL JS in React to draw live location data onto the map.

## Use an Edge Functions to write location data to Supabase [\#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre\#use-an-edge-functions-to-write-location-data-to-supabase)

In this section, you will create an Edge Function that will capture live location data from a Telegram Bot. The Telegram Bot will send location data to the Edge Function, which will then insert the data into Supabase.

For a detailed guide on how to create a Telegram Bot, please refer to our docs [here](https://supabase.com/docs/guides/functions/examples/telegram-bot).

You can find the production ready code for the Telegram Bot Supabase Edge Function on [GitHub](https://github.com/thorwebdev/location-tRacer/blob/main/supabase/functions/telegram-bot/index.ts). This is the relevant code that listens to the live location updates and writes them to the database:

/supabase/functions/telegram-bot/index.ts

``
import { Bot, webhookCallback } from 'https://deno.land/x/grammy@v1.20.3/mod.ts'
import { createClient } from 'jsr:@supabase/supabase-js@2.39.7'
import { Database } from '../_shared/database.types.ts'
const token = Deno.env.get('BOT_TOKEN')
if (!token) throw new Error('BOT_TOKEN is unset')
const supabase = createClient<Database>(
Deno.env.get('SUPABASE_URL')!,
Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
)
const bot = new Bot(token)
// ...
bot.on('edit:location', async (ctx) => {
const {
    location,
    from: { id: user_id },
    edit_date,
} = ctx.update.edited_message!
if (location) {
    // Insert into db
    const { error } = await supabase.rpc('location_insert', {
      _user_id: user_id,
      _lat: location.latitude,
      _long: location.longitude,
      _timestamp: edit_date,
    })
    if (
      error &&
      error.message !==
        'null value in column "event_id" of relation "locations" violates not-null constraint' &&
      error.message !== 'duplicate key value violates unique constraint "locations_pkey"'
    ) {
      return console.log(`edit:location:insert:error:user:${user_id}: ${error.message}`)
    }
}
return
})
const handleUpdate = webhookCallback(bot, 'std/http')
Deno.serve(async (req) => {
const headers = req.headers
try {
    const url = new URL(req.url)
    if (url.searchParams.get('secret') !== Deno.env.get('FUNCTION_SECRET')) {
      return new Response('not allowed', { status: 405 })
    }
    return await handleUpdate(req)
} catch (err) {
    console.log(headers)
    console.error(err)
}
return new Response()
})
``

## Use an RPC to insert location data into Postgres [\#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre\#use-an-rpc-to-insert-location-data-into-postgres)

The edge function above uses an RPC (remote procedure call) to insert the location data into the database. The RPC is defined in our [Supabase Migrations](https://github.com/thorwebdev/location-tRacer/blob/main/supabase/migrations/20240227024905_init.sql#L80). The RPC first validates that the user has an active session and then inserts the location data into the `locations` table:

`
CREATE OR REPLACE FUNCTION public.location_insert(_timestamp bigint, _lat double precision, _long double precision, _user_id bigint)
RETURNS void AS $$
declare active_event_id uuid;
begin
select event_id into active_event_id from public.sessions where user_id = _user_id and status = 'ACTIVE'::session_status;
INSERT INTO public.locations(event_id, user_id, created_at, lat, long, location)
VALUES (active_event_id, _user_id, to_timestamp(_timestamp), _lat, _long, st_point(_long, _lat));
end;
$$ LANGUAGE plpgsql VOLATILE;
`

## Use Supabase Realtime to listen to changes in the database [\#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre\#use-supabase-realtime-to-listen-to-changes-in-the-database)

In this section, you will use Supabase Realtime to listen to changes in the database. The Realtime API is a powerful tool that allows you to broadcast changes in the database to multiple clients.

The full client-side code for listening to the realtime changes and drawing the marker onto the map is available on [GitHub](https://github.com/thorwebdev/location-tRacer/blob/main/app/app/realtimemap/%5Bevent%5D/page.tsx).

We're going to brake it down into a couple of steps:

Since we're working in React, we will set up the Realtime subscription in the `useEffect` hook. If you're using Next.js, it's important to mark this with `use client` as we will need client-side JavaScript to make this happen:

/app/app/realtimemap/%5Bevent%5D/page.tsx

``
// ...
export default function Page({ params }: { params: { event: string } }) {
const supabase = createClient<Database>()
const [locations, setLocations] = useState<{
    [key: string]: Tables<'locations'>
} | null>(null)
const locationsRef = useRef<{
    [key: string]: Tables<'locations'>
} | null>()
locationsRef.current = locations
useEffect(() => {
    // Listen to realtime updates
    const subs = supabase
      .channel('schema-db-changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT', // Listen only to INSERTs
          schema: 'public',
          table: 'locations',
          filter: `event_id=eq.${params.event}`,
        },
        (payload) => {
          const loc = payload.new as Tables<'locations'>
          const updated = {
            ...locationsRef.current,
            [loc.user_id.toString()]: loc,
          }
          setLocations(updated)
        }
      )
      .subscribe()
    console.log('Subscribed')
    return () => {
      subs.unsubscribe()
    }
}, [])
// ...
``

## Use MapLibre GL JS in React to draw live location data onto the map [\#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre\#use-maplibre-gl-js-in-react-to-draw-live-location-data-onto-the-map)

The realtime subscription listener above updates the state of the `locations` object with the new location data, anytime it is inserted into the table. We can now use `react-map-gl` to easily draw the location markers onto the map:

/app/app/realtimemap/%5Bevent%5D/page.tsx

`
// ...
<Map
className="map"
cooperativeGestures={true}
initialViewState={{
    longitude: 103.852713,
    latitude: 1.285727,
    zoom: 13,
}}
mapStyle={{
    version: 8,
    glyphs: 'https://cdn.protomaps.com/fonts/pbf/{fontstack}/{range}.pbf',
    sources: {
      protomaps: {
        attribution:
          '<a href="https://github.com/protomaps/basemaps">Protomaps</a> © <a href="https://openstreetmap.org">OpenStreetMap</a>',
        type: 'vector',
        url: 'pmtiles://https://<project_ref>.supabase.co/functions/v1/maps-private/my_area.pmtiles',
      },
    },
    transition: {
      duration: 0,
    },
    // @ts-ignore
    layers: layers('protomaps', 'light'),
}}
// @ts-ignore
mapLib={maplibregl}
>
{Object.entries(locations).map(([key, value]) => (
    <Marker key={key} longitude={value.long} latitude={value.lat} color="red" />
))}
</Map>
`

Note that we're using [Protomaps](https://protomaps.com/) hosted on Supabase Storage here for the base map. To learn about this read our [previous tutorial here](https://supabase.com/blog/self-host-maps-storage-protomaps).

That's it, this is how easy it is to add realtime location data to your applications using Supabase! We can't wait to see what you will build!

## Conclusion [\#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre\#conclusion)

Supabase Realtime is ideal for broadcasting location data to multiple clients. Combined with the power of PostGIS and the broader Postgres extension ecosystem, its's a powerful solution for all your geospatial needs!

Want to learn more about Maps and PostGIS? Make sure to follow our [Twitter](https://x.com/supabase) and [YouTube](https://www.youtube.com/@Supabase) channels to not miss out! See you then!

## More Supabase [\#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre\#more-supabase)

- [Watch the video guide](https://supabase.link/realtime-maps-yt)
- [Find the code](https://supabase.link/realtime-maps-gh)
- [Build your own open source Google Maps API alternative](https://supabase.link/supa-gis-yt)
- [Self-host Maps on Supabase Storage with Protomaps](https://supabase.link/protomaps-storage-yt)
- [Getting started with PostGIS](https://supabase.link/postgis-quickstart-yt)
- [PostGIS docs guide](https://supabase.com/docs/guides/database/extensions/postgis)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&t=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)

[Last post\\
\\
**Simplifying Time-Based Queries with Range Columns** \\
\\
11 July 2024](https://supabase.com/blog/range-columns)

[Next post\\
\\
**Generate Vector Tiles with PostGIS** \\
\\
26 June 2024](https://supabase.com/blog/postgis-generate-vector-tiles)

[postgres](https://supabase.com/blog/tags/postgres) [realtime](https://supabase.com/blog/tags/realtime) [maps](https://supabase.com/blog/tags/maps)

On this page

- [Use an Edge Functions to write location data to Supabase](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-an-edge-functions-to-write-location-data-to-supabase)
- [Use an RPC to insert location data into Postgres](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-an-rpc-to-insert-location-data-into-postgres)
- [Use Supabase Realtime to listen to changes in the database](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-supabase-realtime-to-listen-to-changes-in-the-database)
- [Use MapLibre GL JS in React to draw live location data onto the map](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-maplibre-gl-js-in-react-to-draw-live-location-data-onto-the-map)
- [Conclusion](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#conclusion)
- [More Supabase](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#more-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&t=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)