---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify/"
title: "Spotify node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify/#spotify-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.spotify.md "Edit this page")

# Spotify node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify/\#spotify-node "Permanent link")

Use the Spotify node to automate work in Spotify, and integrate Spotify with other applications. n8n has built-in support for a wide range of Spotify features, including getting album and artist information.

On this page, you'll find a list of operations the Spotify node supports and links to more resources.

Credentials

Refer to [Spotify credentials](https://docs.n8n.io/integrations/builtin/credentials/spotify/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify/\#operations "Permanent link")

- Album
  - Get an album by URI or ID.
  - Get a list of new album releases.
  - Get an album's tracks by URI or ID.
  - Search albums by keyword.
- Artist
  - Get an artist by URI or ID.
  - Get an artist's albums by URI or ID.
  - Get an artist's related artists by URI or ID.
  - Get an artist's top tracks by URI or ID.
  - Search artists by keyword.
- Library
  - Get the user's liked tracks.
- My Data
  - Get your followed artists.
- Player
  - Add a song to your queue.
  - Get your currently playing track.
  - Skip to your next track.
  - Pause your music.
  - Skip to your previous song.
  - Get your recently played tracks.
  - Resume playback on the current active device.
  - Set volume on the current active device.
  - Start playing a playlist, artist, or album.
- Playlist
  - Add tracks from a playlist by track and playlist URI or ID.
  - Create a new playlist.
  - Get a playlist by URI or ID.
  - Get a playlist's tracks by URI or ID.
  - Get a user's playlists.
  - Remove tracks from a playlist by track and playlist URI or ID.
  - Search playlists by keyword.
- Track
  - Get a track by its URI or ID.
  - Get audio features for a track by URI or ID.
  - Search tracks by keyword

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify/\#templates-and-examples "Permanent link")

**Add liked songs to a Spotify monthly playlist**

by Lucas

[View template details](https://n8n.io/workflows/1074-add-liked-songs-to-a-spotify-monthly-playlist/)

**IOT Button Remote / Spotify Control Integration with MQTT**

by Hubschrauber

[View template details](https://n8n.io/workflows/2383-iot-button-remote-spotify-control-integration-with-mqtt/)

**Download recently liked songs automatically with Spotify**

by Mario

[View template details](https://n8n.io/workflows/2285-download-recently-liked-songs-automatically-with-spotify/)

[Browse Spotify integration templates](https://n8n.io/integrations/spotify/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top