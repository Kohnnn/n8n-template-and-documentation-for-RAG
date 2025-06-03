---
url: "https://supabase.com/blog/postgis-generate-vector-tiles"
title: "Generate Vector Tiles with PostGIS"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Generate Vector Tiles with PostGIS

26 Jun 2024

•

12 minute read

[![Brandon Liu avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fbdon.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Brandon LiuGuest Author](https://github.com/bdon)

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Generate Vector Tiles with PostGIS](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgis_vector_tiles%2Foverture_postgis_mvt.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Do you prefer audio-visual learning? Watch the video guide!](https://supabase.link/supa-gis-yt-docs)

[Or jump straight into the code](https://github.com/bdon/supabase-vector-tile)

[Overture Maps Foundation](https://overturemaps.org/) is a [Joint Development Foundation Project](https://jointdevelopment.org/) initiated by Amazon, Meta, Microsoft, and tomtom, aiming to create reliable, easy-to-use, and interoperable open map data.

Overture Maps allows us to download open map data, like places of interest, as [GeoJSON](https://geojson.org/) which we can transform into SQL and ingest into our Postgres database on Supabase.

Using PostGIS we can then programmatically generate vector tiles and serve them to our MapLibre GL client using supabase-js.

Vector tiles are packets of geographic data, packaged into pre-defined roughly-square shaped "tiles" for transfer over the web. Map data is requested by a client as a set of "tiles" corresponding to square areas of land of a pre-defined size and location.

Especially for large datasets, this has the benefit that the data transfer is greatly reduced because only data within the current viewport, and at the current zoom level needs to be transferred.

In this tutorial, you will learn to

- Use Overture Maps to download open map places data in GeoJSON format.
- Use GDAL ogr2ogr to transform GeoJSON into SQL statements.
- Import location data and JSON metadata into your Supabase Postgres database using psql.
- Use PostGIS' `ST_AsMVT` to aggregate a set of rows corresponding to a tile layer into a binary vector tile representation.
- Use MapLibre's `addProtocol` to visualize large PostGIS tables by making remote procedure calls with supabase-js.
- Use supabase-js to fetch additional JSON metadata on demand

## Download open map data with Overture Maps [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#download-open-map-data-with-overture-maps)

Overture Maps provides a [python command-line tool](https://docs.overturemaps.org/getting-data/overturemaps-py/) to download data within a region of interest and converts it to several common geospatial file formats.

We can download places in Singapore into a GeoJSON file with this command:

`
overturemaps download --bbox=103.570233,1.125077,104.115855,1.490957 -f geojson --type=place -o places.geojson
`

Depending on the size of the bounding box this can take quite some time!

## Transform GeoJSON into SQL [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#transform-geojson-into-sql)

In the next step, we can use [GDAL ogr2ogr](https://gdal.org/programs/ogr2ogr.html) to transform the GeoJSON file into a PostGIS compatible SQL file.

You can install `GDAL` via `homebrew brew install gdal` or follow the [download instructions](https://gdal.org/download.html).

`
PG_USE_COPY=true ogr2ogr -f pgdump places.sql places.geojson
`

## Import location data into Supabase [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#import-location-data-into-supabase)

Enable the PostGIS extension on your Supabase Database on a dedicated separate `gis` schema. To do so you can navigate to the [SQL Editor](https://supabase.com/dashboard/project/_/sql/new) and run the following SQL, or you can enable the extension from the [Database Extensions Settings](https://supabase.com/dashboard/project/_/database/extensions).

As PostGIS can be quite compute heavy, we recommend enabling it on a dedicated separate schema, for example, named `gis`!

`
CREATE SCHEMA IF NOT EXISTS "gis";
CREATE EXTENSION IF NOT EXISTS "postgis" WITH SCHEMA "gis";
`

Import the open map data into a `places` table in Supabase:

`
psql -h aws-0-us-west-1.pooler.supabase.com -p 5432 -d postgres -U postgres.project-ref < places.sql
`

You can find the credentials in the [project connect page](https://supabase.com/dashboard/project/_?showConnect=true) of your Supabase Dashboard.

### Enable RLS and create a public read policy [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#enable-rls-and-create-a-public-read-policy)

We want the places data to be available publicly, so we can create a row level security policy that enables public read access.

In your Supabase Dashboard, navigate to the [SQL Editor](https://supabase.com/dashboard/project/_/sql/new) and run the following:

`
ALTER TABLE "public"."places" ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Enable read access for all users" ON "public"."places" FOR SELECT USING (true);
`

## Generate vector tiles with PostGIS [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#generate-vector-tiles-with-postgis)

To programmatically generate vector tiles on client-side request, we need to create a Postgres function that we can invoke via a [remote procedure call](https://supabase.com/docs/reference/javascript/rpc). In your SQL Editor, run:

`
CREATE OR REPLACE FUNCTION mvt(z integer, x integer, y integer)
RETURNS text
LANGUAGE plpgsql
AS $$
DECLARE
    mvt_output text;
BEGIN
    WITH
    -- Define the bounds of the tile using the provided Z, X, Y coordinates
    bounds AS (
        SELECT ST_TileEnvelope(z, x, y) AS geom
    ),
    -- Transform the geometries from EPSG:4326 to EPSG:3857 and clip them to the tile bounds
    mvtgeom AS (
        SELECT
            -- include the name and id only at zoom 13 to make low-zoom tiles smaller
            CASE
            WHEN z > 13 THEN id
            ELSE NULL
            END AS id,
            CASE
            WHEN z > 13 THEN names::json->>'primary'
            ELSE NULL
            END AS primary_name,
            categories::json->>'main' as main_category,
            ST_AsMVTGeom(
                ST_Transform(wkb_geometry, 3857), -- Transform the geometry to Web Mercator
                bounds.geom,
                4096, -- The extent of the tile in pixels (commonly 256 or 4096)
                0,    -- Buffer around the tile in pixels
                true  -- Clip geometries to the tile extent
            ) AS geom
        FROM
            places, bounds
        WHERE
            ST_Intersects(ST_Transform(wkb_geometry, 3857), bounds.geom)
    )
    -- Generate the MVT from the clipped geometries
    SELECT INTO mvt_output encode(ST_AsMVT(mvtgeom, 'places', 4096, 'geom'),'base64')
    FROM mvtgeom;
    RETURN mvt_output;
END;
$$;
`

To limit the amount of data sent over the wire, we limit the amount of metadata to include in the vector tile. For example we add a condition for the zoom level, and only return the place name when the user has zoomed in beyond level 13.

## Use supabase-js to fetch vector tiles from MapLibre GL client [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#use-supabase-js-to-fetch-vector-tiles-from-maplibre-gl-client)

You can find the full `index.html` code on [GitHub](https://github.com/bdon/supabase-vector-tile/blob/main/index.html). Here we'll highlight how to add a new protocol to MapLibreGL to fetch the bas64 encoded binary vector tile data via supabase-js so that MapLibre GL can fetch and render the data as your users interact with the map:

index.html

``
const client = supabase.createClient('your-supabase-api-url', 'your-supabase-anon-key')
function base64ToArrayBuffer(base64) {
var binaryString = atob(base64)
var bytes = new Uint8Array(binaryString.length)
for (var i = 0; i < binaryString.length; i++) {
    bytes[i] = binaryString.charCodeAt(i)
}
return bytes
}
maplibregl.addProtocol('supabase', async (params, abortController) => {
const re = new RegExp(/supabase:\/\/(.+)\/(\d+)\/(\d+)\/(\d+)/)
const result = params.url.match(re)
const { data, error } = await client.rpc('mvt', {
    z: result[2],
    x: result[3],
    y: result[4],
})
const encoded = base64ToArrayBuffer(data)
if (!error) {
    return { data: encoded }
} else {
    throw new Error(`Tile fetch error:`)
}
})
``

With the supabase protocol registered, we can now add it to our MapLibre GL sources on top of a basemap like [Protomaps](https://protomaps.com/) for example:

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
      supabase: {
        type: 'vector',
        tiles: ['supabase://boston/{z}/{x}/{y}'],
        attribution: '© <a href="https://overturemaps.org">Overture Maps Foundation</a>',
      },
      protomaps: {
        type: 'vector',
        url: 'https://api.protomaps.com/tiles/v3.json?key=your-protomaps-api-key',
        attribution: 'Basemap © <a href="https://openstreetmap.org">OpenStreetMap</a>',
      },
    },
},
})
// ...
`

## On demand fetch additional JSON metadata [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#on-demand-fetch-additional-json-metadata)

To limit the amount of data sent over the wire, we don't encode all the metadata in the vector tile itself, but rather set up an onclick handler to fetch the additional metadata on demand within the MapLibre GL popup:

index.html

``
// ..
const popup = new maplibregl.Popup({
closeButton: true,
closeOnClick: false,
maxWidth: 'none',
})
function loadDetails(element, id) {
element.innerHTML = 'loading...'
client
    .from('places')
    .select(
      `
          websites,
          socials,
          phones,
          addresses,
          source:  sources->0->dataset
        `
    )
    .eq('id', id)
    .single()
    .then(({ data, error }) => {
      if (error) return console.error(error)
      element.parentElement.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`
    })
}
map.on('click', 'overture-pois-text', async (e) => {
if (e.features.length > 0) {
    const feature = e.features[0]
    console.log(feature)
    popup.setHTML(
      `
        <table style="font-size:12px">
            <tr>
                <td>id:</td>
                <td>${feature.properties.id}</td>
            </tr>
            <tr>
                <td>name:</td>
                <td>${feature.properties.primary_name}</td>
            </tr>
            <tr>
                <td>main_category:</td>
                <td>${feature.properties.main_category}</td>
            </tr>
            <tr>
                <td>details:</td>
                <td>
                  <span onclick="loadDetails(this, '${feature.properties.id}')">
                    load details
                  </span>
                </td>
            </tr>
        </table>
      `
    )
    popup.setLngLat(e.lngLat)
    popup.addTo(map)
}
})
// ...
``

## Conclusion [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#conclusion)

PostGIS is incredibly powerful, allowing you to programmatically generate vector tiles from table rows stored in Postgres. Paired with Supabase's auto generated REST API and supabase-js client library you're able to build interactive geospatial applications with ease!

Want to learn more about Maps and PostGIS? Make sure to follow our [Twitter](https://x.com/supabase) and [YouTube](https://www.youtube.com/@Supabase) channels to not miss out! See you then!

## More Supabase [\#](https://supabase.com/blog/postgis-generate-vector-tiles\#more-supabase)

- [Watch the video guide](https://supabase.link/supa-gis-yt-docs)
- [Find the code](https://github.com/bdon/supabase-vector-tile)
- [Self-host Maps on Supabase Storage with Protomaps](https://supabase.link/protomaps-storage-yt)
- [Getting started with PostGIS](https://supabase.link/postgis-quickstart-yt)
- [PostGIS docs guide](https://supabase.com/docs/guides/database/extensions/postgis)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&t=Generate%20Vector%20Tiles%20with%20PostGIS)

[Last post\\
\\
**Postgres Realtime location sharing with MapLibre** \\
\\
4 July 2024](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre)

[Next post\\
\\
**Self-host Maps with Protomaps and Supabase Storage** \\
\\
19 June 2024](https://supabase.com/blog/self-host-maps-storage-protomaps)

[postgres](https://supabase.com/blog/tags/postgres) [postgis](https://supabase.com/blog/tags/postgis) [maps](https://supabase.com/blog/tags/maps)

On this page

- [Download open map data with Overture Maps](https://supabase.com/blog/postgis-generate-vector-tiles#download-open-map-data-with-overture-maps)
- [Transform GeoJSON into SQL](https://supabase.com/blog/postgis-generate-vector-tiles#transform-geojson-into-sql)
- [Import location data into Supabase](https://supabase.com/blog/postgis-generate-vector-tiles#import-location-data-into-supabase)
  - [Enable RLS and create a public read policy](https://supabase.com/blog/postgis-generate-vector-tiles#enable-rls-and-create-a-public-read-policy)
- [Generate vector tiles with PostGIS](https://supabase.com/blog/postgis-generate-vector-tiles#generate-vector-tiles-with-postgis)
- [Use supabase-js to fetch vector tiles from MapLibre GL client](https://supabase.com/blog/postgis-generate-vector-tiles#use-supabase-js-to-fetch-vector-tiles-from-maplibre-gl-client)
- [On demand fetch additional JSON metadata](https://supabase.com/blog/postgis-generate-vector-tiles#on-demand-fetch-additional-json-metadata)
- [Conclusion](https://supabase.com/blog/postgis-generate-vector-tiles#conclusion)
- [More Supabase](https://supabase.com/blog/postgis-generate-vector-tiles#more-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&t=Generate%20Vector%20Tiles%20with%20PostGIS)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)