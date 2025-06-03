---
url: "https://supabase.com/blog/self-host-maps-storage-protomaps"
title: "Self-host Maps with Protomaps and Supabase Storage"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Self-host Maps with Protomaps and Supabase Storage

19 Jun 2024

•

11 minute read

[![Brandon Liu avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fbdon.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Brandon LiuGuest Author](https://github.com/bdon)

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Self-host Maps with Protomaps and Supabase Storage](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fprotomaps_storage%2Fprotomaps_storage_og.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Do you prefer the audio-visual learning? Watch the video guide!](https://supabase.link/protomaps-storage-yt)

[Protomaps](https://protomaps.com/) is an open source map of the world, deployable as a single static file on [Supabase Storage](https://supabase.com/storage).

In this tutorial, you will learn to

- Use Protomaps to excract an area into a static PMTiles file.
- Upload the PMTiles file to Supabase Storage.
- Use MapLibre to render the Map onto a Web Page.
- Use Supabase Edge Functions to restrict File Access.

## Extract an area into a static PMTiles file [\#](https://supabase.com/blog/self-host-maps-storage-protomaps\#extract-an-area-into-a-static-pmtiles-file)

Protomaps provides a [`pmtiles` CLI](https://docs.protomaps.com/guide/getting-started#_1-install-the-cli) that can be used to cut out certain areas from the world map and compress those into a single static file.

For example, we can [extract a small area](https://docs.protomaps.com/guide/getting-started#_3-extract-any-area) around Utrecht in the Netherlands like this:

`
pmtiles extract https://build.protomaps.com/20240618.pmtiles my_area.pmtiles --bbox=5.068050,52.112086,5.158424,52.064140
`

Note: make sure to update the date to the latest daily build!

This will create a `my_area.pmtiles` file which you can upload to Supabase Storage.

## Upload the PMTiles file to Supabase Storage [\#](https://supabase.com/blog/self-host-maps-storage-protomaps\#upload-the-pmtiles-file-to-supabase-storage)

In your [Supabase Dashboard](https://supabase.com/dashboard/project/_/storage/buckets) navigate to `Storage` and click "New Bucket" and create a new public bucket called `public-maps`.

Upload the `my_area.pmtiles` file created earlier to your public bucket. Once uploaded, click the file and tap "Get URL".

Supabase Storage supports the required [HTTP Range Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests) out of the box, allowing you to use the public storage URL directly from your maps client.

## Use MapLibre to render the Map [\#](https://supabase.com/blog/self-host-maps-storage-protomaps\#use-maplibre-to-render-the-map)

PMTiles easily works with both [MapLibre GL](https://docs.protomaps.com/pmtiles/maplibre) and [Leaflet](https://docs.protomaps.com/pmtiles/leaflet). In our example we wil use [MapLibre GL](https://maplibre.org/maplibre-gl-js/docs/), which is a TypeScript library that uses WebGL to render interactive maps from vector tiles in a browser.

This is a vanilla JS example which uses CDN releases of the libraries. You can very easily adapt it to work with React as well, for example using the [react-map-gl](https://visgl.github.io/react-map-gl/) library.

index.html

`
<html>
<head>
    <title>Overture Places</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://unpkg.com/maplibre-gl@4.1.2/dist/maplibre-gl.css"
      crossorigin="anonymous"
    />
    <script
      src="https://unpkg.com/maplibre-gl@4.1.2/dist/maplibre-gl.js"
      crossorigin="anonymous"
    ></script>
    <script src="https://unpkg.com/protomaps-themes-base@2.0.0-alpha.5/dist/index.js"></script>
    <script src="https://unpkg.com/pmtiles@3.0.6/dist/pmtiles.js"></script>
    <style>
      body {
        margin: 0;
      }
      #map {
        height: 100%;
        width: 100%;
      }
    </style>
</head>
<body>
    <div id="map"></div>
    <script type="text/javascript">
      // Add the PMTiles Protocol:
      let protocol = new pmtiles.Protocol()
      maplibregl.addProtocol('pmtiles', protocol.tile)
      // Load the Map tiles directly from Supabase Storage:
      const map = new maplibregl.Map({
        hash: true,
        container: 'map',
        style: {
          version: 8,
          glyphs: 'https://cdn.protomaps.com/fonts/pbf/{fontstack}/{range}.pbf',
          sources: {
            protomaps: {
              attribution:
                '<a href="https://github.com/protomaps/basemaps">Protomaps</a> © <a href="https://openstreetmap.org">OpenStreetMap</a>',
              type: 'vector',
              url: 'pmtiles://https://<your-project-ref>.supabase.co/storage/v1/object/public/public-maps/my_area.pmtiles',
            },
          },
          layers: protomaps_themes_base.default('protomaps', 'dark'),
        },
      })
    </script>
</body>
</html>
`

## Use Supabase Edge Functions to restrict Access [\#](https://supabase.com/blog/self-host-maps-storage-protomaps\#use-supabase-edge-functions-to-restrict-access)

A public Supabase Storage bucket allows access from any origin, which might not be ideal for your use case. At the time of writing, you're not able to modify the CORS settings for Supabase Storage buckets, however you can utilize [Supabase Edge Functions](https://supabase.com/docs/guides/functions) to restrict access to your PMTiles files, allowing you to even pair it with [Supabase Auth](https://supabase.com/docs/guides/auth) to restrict access to certain users for example.

In your Supabase Dashboard, create a new private storage bucket called `maps-private` and upload your `my_area.pmtiles` file there. Files in private buckets can only be accessed through either a short-lived signed URL, or by passing the secret service role key as an authorization header. Since our Edge Function is a secure server-side environment, we can utilize the latter approach here.

Using the [Supabase CLI](https://github.com/supabase/cli), create a new Edge Function by running `supabase functions new maps-private`, then add the following code to your newly created function:

supabase/functions/maps-private/index.ts

``
const ALLOWED_ORIGINS = ['http://localhost:8000']
const corsHeaders = {
'Access-Control-Allow-Origin': ALLOWED_ORIGINS.join(','),
'Access-Control-Allow-Headers':
    'authorization, x-client-info, apikey, content-type, range, if-match',
'Access-Control-Expose-Headers': 'range, accept-ranges, etag',
'Access-Control-Max-Age': '300',
}
Deno.serve((req) => {
// This is needed if you're planning to invoke your function from a browser.
if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
}
// Check origin
const origin = req.headers.get('Origin')
if (!origin || !ALLOWED_ORIGINS.includes(origin)) {
    return new Response('Not Allowed', { status: 405 })
}
const reqUrl = new URL(req.url)
const url = `${Deno.env.get('SUPABASE_URL')}/storage/v1/object/authenticated${reqUrl.pathname}`
const { method, headers } = req
// Add Auth header
const modHeaders = new Headers(headers)
modHeaders.append('authorization', `Bearer ${Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!}`)
return fetch(url, { method, headers: modHeaders })
})
``

If you want to further restrict access based on authenticated users, you can pair your Edge Function with Supabase Auth as shown in [this example](https://supabase.com/docs/guides/functions/auth#fetching-the-user).

Lastly, we need to deploy our Edge Function to Supabase by running `supabase functions deploy maps-private --no-verify-jwt`. Note that the [`--no-verify-jwt` flag](https://supabase.com/docs/reference/cli/supabase-functions-deploy) is required if you want to allow public access from your website without any Supabase Auth User.

Now we can simply replace the public storage URL with our Edge Functions URL to proxy the range requests to our private bucket:

index.html

`
// ...
const map = new maplibregl.Map({
hash: true,
container: 'map',
style: {
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
    layers: protomaps_themes_base.default('protomaps', 'dark'),
},
})
// ...
`

Now go ahead and serve your `index.html` file, for example via Python SimpleHTTPServer: `python3 -m http.server` and admire your beautiful map on [localhost:8000](http://localhost:8000/)!

## Expo React Native [\#](https://supabase.com/blog/self-host-maps-storage-protomaps\#expo-react-native)

As you might know, I'm a big React Native fan, and when writing this tutorial I was very excited about making this work in Expo mobile apps also.

Unfortunately, at the time of writing, custom protocols are not supported in [maplibre-react-native](https://github.com/maplibre/maplibre-react-native). There is an issues tracking this [here](https://github.com/maplibre/maplibre-react-native/issues/28), so if there are any native mobile wizards out there, I'd very much appreciate your contributions!

In the meantime, however, the Expo team had a great idea, what about leveraging [React DOM components](https://docs.expo.dev/guides/dom-components/), which are currently experimentally supported in Expo SDK 52 preview.

This approach allows you to utilize [react-map-gl](https://github.com/visgl/react-map-gl) and [maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) across your Expo web and mobile apps.

[Do you prefer the audio-visual learning? Watch the video guide!](https://supabase.link/react-native-maps-yt).

Or jump straight into the [code](https://supabase.link/react-native-maps-gh).

Follow the steps to [install the canary release](https://docs.expo.dev/versions/unversioned#canary-releases).

To render a React component to the DOM, add the 'use dom' directive to the top of the web component file:

Map.jsx

`
'use dom'
import 'text-encoding-polyfill'
import { useEffect } from 'react'
import Map from 'react-map-gl'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'
import { Protocol } from 'pmtiles'
export default function MapBox(_) {
useEffect(() => {
    let protocol = new Protocol()
    maplibregl.addProtocol('pmtiles', protocol.tile)
    return () => {
      maplibregl.removeProtocol('pmtiles')
    }
}, [])
return (
    <div style={{ width: '100%', height: '100%' }}>
      <Map
        style={{ width: '100%', height: 900 }}
        mapStyle={{
          version: 8,
          sources: {
            sample: {
              type: 'vector',
              url: 'pmtiles://https://r2-public.protomaps.com/protomaps-sample-datasets/cb_2018_us_zcta510_500k.pmtiles',
            },
          },
          layers: [\
            {\
              id: 'zcta',\
              source: 'sample',\
              'source-layer': 'zcta',\
              type: 'line',\
              paint: {\
                'line-color': '#999',\
              },\
            },\
          ],
        }}
        mapLib={maplibregl}
      />
    </div>
)
}
`

Inside the native component file, import the web component to use it:

App.jsx

`
import { StatusBar } from 'expo-status-bar'
import { StyleSheet, Text, View } from 'react-native'
import Map from './Map.jsx'
export default function App() {
return (
    <View style={styles.container}>
      <Map dom={{ autoSize: true }} />
      <StatusBar style="auto" />
    </View>
)
}
const styles = StyleSheet.create({
container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'stretch',
    justifyContent: 'center',
},
})
`

## Conclusion [\#](https://supabase.com/blog/self-host-maps-storage-protomaps\#conclusion)

Protomaps is a fantastic open source project that allows you to host your own Google Maps alternative on Supabase Storage. You can further extend this with powerful PostGIS capabilities to programmatically generate [Vector Tiles](https://github.com/mapbox/vector-tile-spec) which we will explore in the next post in this series. So make sure you subscribe to our [Twitter](https://x.com/supabase) and [YouTube](https://www.youtube.com/@Supabase) channels to not miss out! See you then!

## More Supabase [\#](https://supabase.com/blog/self-host-maps-storage-protomaps\#more-supabase)

- [Watch the video guide](https://youtu.be/l7QBpiLRwJc)
- [Find the code](https://github.com/supabase/supabase/tree/master/examples/storage/protomaps)
- [Getting started with PostGIS video](https://youtu.be/MWfB0t5u3V0)
- [PostGIS docs guide](https://supabase.com/docs/guides/database/extensions/postgis)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fself-host-maps-storage-protomaps&text=Self-host%20Maps%20with%20Protomaps%20and%20Supabase%20Storage)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fself-host-maps-storage-protomaps&text=Self-host%20Maps%20with%20Protomaps%20and%20Supabase%20Storage)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fself-host-maps-storage-protomaps&t=Self-host%20Maps%20with%20Protomaps%20and%20Supabase%20Storage)

[Last post\\
\\
**Generate Vector Tiles with PostGIS** \\
\\
26 June 2024](https://supabase.com/blog/postgis-generate-vector-tiles)

[Next post\\
\\
**Cal.com launches Expert Marketplace built with Next.js and Supabase.** \\
\\
18 June 2024](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase)

[storage](https://supabase.com/blog/tags/storage) [postgis](https://supabase.com/blog/tags/postgis) [maps](https://supabase.com/blog/tags/maps) [react-native](https://supabase.com/blog/tags/react-native)

On this page

- [Extract an area into a static PMTiles file](https://supabase.com/blog/self-host-maps-storage-protomaps#extract-an-area-into-a-static-pmtiles-file)
- [Upload the PMTiles file to Supabase Storage](https://supabase.com/blog/self-host-maps-storage-protomaps#upload-the-pmtiles-file-to-supabase-storage)
- [Use MapLibre to render the Map](https://supabase.com/blog/self-host-maps-storage-protomaps#use-maplibre-to-render-the-map)
- [Use Supabase Edge Functions to restrict Access](https://supabase.com/blog/self-host-maps-storage-protomaps#use-supabase-edge-functions-to-restrict-access)
- [Expo React Native](https://supabase.com/blog/self-host-maps-storage-protomaps#expo-react-native)
- [Conclusion](https://supabase.com/blog/self-host-maps-storage-protomaps#conclusion)
- [More Supabase](https://supabase.com/blog/self-host-maps-storage-protomaps#more-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fself-host-maps-storage-protomaps&text=Self-host%20Maps%20with%20Protomaps%20and%20Supabase%20Storage)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fself-host-maps-storage-protomaps&text=Self-host%20Maps%20with%20Protomaps%20and%20Supabase%20Storage)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fself-host-maps-storage-protomaps&t=Self-host%20Maps%20with%20Protomaps%20and%20Supabase%20Storage)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)