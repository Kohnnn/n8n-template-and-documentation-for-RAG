---
url: "https://supabase.com/blog/meetup-kahoot-alternative"
title: "The open source Kahoot alternative"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# The open source Kahoot alternative

09 May 2024

•

7 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![The open source Kahoot alternative](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foss-kahoot-alternative%2Fthumbnail.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Recently as part of our [GA Week](https://supabase.com/ga-week) and with the help of our amazing community leaders we had meetups at over 30 different locations worldwide! Seeing all the fun pictures and videos of the community meetups was amazing!

To make the meetups more engaging, we prepared an interactive quiz game that everyone could play. We were initially going to use Kahoot for this. Still, we thought it would be an excellent opportunity to showcase the power of Supabase and open source, so we built an open-source version of Kahoot with some pre-filled Supabase / tech questions for everyone to play at the meetup.

## What we built for the meetup [\#](https://supabase.com/blog/meetup-kahoot-alternative\#what-we-built-for-the-meetup)

![Kahoot alternative host page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foss-kahoot-alternative%2Fhost-page.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Kahoot alternative that we built is a simplified version of Kahoot. Mainly having fewer features on the admin side of things, but as an individual player participating, the experience should be similar to the actual Kahoot.

The game has two screens: the host screen and the player screen. The host can start a game by choosing one of the available quiz sets. Because we had meetups from around the globe, we created the same 10-question quiz sets in 4 different languages.

![Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foss-kahoot-alternative%2Fdashboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Once the host clicks the button to start a game, a lobby screen with a QR code appears. The players can scan the QR codes with their phones, name themselves, and enter the game.

The host can start the quiz game once everyone in the room has entered the lobby. The players are shown the question first and then the choices five seconds later for each question. They answer the quiz on their phones, and the sooner they answer, the more points they get.

Once all the questions are answered, the points are summed up, and the leaderboard is shown on the screen.

Actual leaderboard from the Tokyo meetup.

![Leaderboard from Tokyo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foss-kahoot-alternative%2Fresults.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Building the Kahoot alternative app [\#](https://supabase.com/blog/meetup-kahoot-alternative\#building-the-kahoot-alternative-app)

I will not go into every implementation detail, as it would be long, but you can find the GitHub repository with the full code [here](https://github.com/supabase-community/kahoot-alternative). The app is a Next.js app without using any server-side rendering, and it utilizes three core Supabase features: auth, database, and realtime.

### Auth [\#](https://supabase.com/blog/meetup-kahoot-alternative\#auth)

For authentication, we used the brand new [anonymous sign-in](https://supabase.com/docs/guides/auth/auth-anonymous) feature to sign in the players automatically in the background. This way, players don’t feel the friction after scanning the QR code and can get started with the game quickly. It also allows us to set a row-level security policy to ensure players have limited read and write permissions in the game.

When a user registers for a game, we check if the user is already signed in, and if not, the app signs them in.

`
const { data: sessionData, error: sessionError } = await supabase.auth.getSession()
let userId: string | null = null
if (sessionData.session) {
userId = sessionData.session?.user.id ?? null
} else {
const { data, error } = await supabase.auth.signInAnonymously()
userId = data?.user?.id ?? null
}
`

### Database [\#](https://supabase.com/blog/meetup-kahoot-alternative\#database)

The database stores everything that happens in the app. We have 6 different tables to store everything from the questions to the answers that users leave for each question in a game. Each time the admin clicks the “Start Game” button of a quiz set from the host dashboard, a new game is created. The database is designed so that the same set of users can play games with the same quiz set multiple times. The full table definitions under `superbase/migrations` in the [GitHub repo](https://github.com/supabase-community/kahoot-alternative/tree/main/supabase/migrations).

![Database diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foss-kahoot-alternative%2Ferd.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Realtime [\#](https://supabase.com/blog/meetup-kahoot-alternative\#realtime)

Realtime is the core of the app. The critical feature of Kahoot is to keep all the connected clients in sync with the game state, so we heavily relied on realtime to share the game states. The admin subscribes to Postgres changes on the `participants`, `games`, and `answers` table. The subscription on the `participants` table is used when it first displays the list of participants on the lobby screen. The subscription on the games table is used to listen to the game state as the admin clicks the next button to move through the questions. Subscriptions on the answers table count how many people have answered the question so that the results can be displayed when everyone has answered the question.

Within the host page, we chain multiple Postgres changes listeners like the following to bundle the realtime subscriptions into one.

``
supabase
.channel('game')
.on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'participants',
      filter: `game_id=eq.${gameId}`,
    },
    (payload) => {
      setParticipants((currentParticipants) => {
        return [...currentParticipants, payload.new as Participant]
      })
    }
)
.on(
    'postgres_changes',
    {
      event: 'UPDATE',
      schema: 'public',
      table: 'games',
      filter: `id=eq.${gameId}`,
    },
    (payload) => {
      const game = payload.new as Game
      setCurrentQuestionSequence(game.current_question_sequence)
      setCurrentScreen(game.phase as AdminScreens)
    }
)
.subscribe()
``

## The Results [\#](https://supabase.com/blog/meetup-kahoot-alternative\#the-results)

Through this open-source app created using Next.js and Supabase, we brought everyone together during meetups worldwide by providing an engaging experience.

Thanks to everyone who participated. I hope you enjoyed it, and a massive thank you to everyone who hosted the meetups.

Twitter Embed

[Visit this post on X](https://twitter.com/tristanbob/status/1781340495899406511?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[![](https://pbs.twimg.com/profile_images/1904999092121710592/mIHl2H24_normal.jpg)](https://twitter.com/tristanbob?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[Tristan Rhodes](https://twitter.com/tristanbob?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[@tristanbob](https://twitter.com/tristanbob?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

·

[Follow](https://twitter.com/intent/follow?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&screen_name=tristanbob)

[View on X](https://twitter.com/tristanbob/status/1781340495899406511?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

I’m proud of my second place showing at the Salt Lake City [@supabase](https://twitter.com/supabase?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative) meetup hosted by [@KyleRummens](https://twitter.com/KyleRummens?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative).

[![Image](https://pbs.twimg.com/media/GLiXvPFbcAAPFGh?format=jpg&name=900x900)](https://x.com/tristanbob/status/1781340495899406511/photo/1)

[3:14 PM · Apr 19, 2024](https://twitter.com/tristanbob/status/1781340495899406511?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[X Ads info and privacy](https://help.twitter.com/en/twitter-for-websites-ads-info-and-privacy)

[7](https://twitter.com/intent/like?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&tweet_id=1781340495899406511) [Reply](https://twitter.com/intent/tweet?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&in_reply_to=1781340495899406511)

Copy link

[Read 1 reply](https://twitter.com/tristanbob/status/1781340495899406511?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781340495899406511%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

Twitter Embed

[Visit this post on X](https://twitter.com/Debbyiecodes/status/1781626949552525323?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[![](https://pbs.twimg.com/profile_images/1826559500943314944/R69MLI_T_normal.jpg)](https://twitter.com/Debbyiecodes?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[Dherrbie](https://twitter.com/Debbyiecodes?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[@Debbyiecodes](https://twitter.com/Debbyiecodes?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

·

[Follow](https://twitter.com/intent/follow?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&screen_name=Debbyiecodes)

[View on X](https://twitter.com/Debbyiecodes/status/1781626949552525323?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

Yesterday's evening, I attended [@supabase](https://twitter.com/supabase?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative) first Meetup in Nigeria. Learnt about Supabase and why I should consider using it.
I also won a cash price for being the first position in the Kahoot game . Shout-out to the organizers [@GeekyAdams](https://twitter.com/GeekyAdams?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative) .

[![Embedded video](https://pbs.twimg.com/ext_tw_video_thumb/1781626852001361920/pu/img/7cl8Du8SERDFQfqN.jpg)](https://twitter.com/Debbyiecodes/status/1781626949552525323?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[![Image](https://pbs.twimg.com/media/GLmcOuRW0AMlJBz?format=jpg&name=360x360)](https://x.com/Debbyiecodes/status/1781626949552525323/video/1)

[![Image](https://pbs.twimg.com/media/GLmcQHeW8AEIjCS?format=jpg&name=small)](https://x.com/Debbyiecodes/status/1781626949552525323/video/1)

[![Image](https://pbs.twimg.com/media/GLmcRLoWoAAZXiK?format=jpg&name=small)](https://x.com/Debbyiecodes/status/1781626949552525323/video/1)

[10:12 AM · Apr 20, 2024](https://twitter.com/Debbyiecodes/status/1781626949552525323?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

[X Ads info and privacy](https://help.twitter.com/en/twitter-for-websites-ads-info-and-privacy)

[41](https://twitter.com/intent/like?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&tweet_id=1781626949552525323) [Reply](https://twitter.com/intent/tweet?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&in_reply_to=1781626949552525323)

Copy link

[Read 7 replies](https://twitter.com/Debbyiecodes/status/1781626949552525323?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1781626949552525323%7Ctwgr%5Ed1b1fe370951292b6146c653d414a69719ec4f14%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative)

## Contributing to open source [\#](https://supabase.com/blog/meetup-kahoot-alternative\#contributing-to-open-source)

Kahoot is a complex app with many features, and many of those features are missing from this alternative app. Especially on the host dashboard, there are a lot of things that could/ should be added, like adding/ editing quz sets or looking back on past game results. Again, the GitHub repo can be found [here](https://github.com/supabase-community/kahoot-alternative), and we are always welcome to receive pull requests. If you want to get into Open source, a casual project like this is a great starting point. Any kind of PR is welcome. Adding/ editing docs/ readme is greatly appreciated, as well. If unsure where to start, ping us about the issue, and we can help you.

## Resources [\#](https://supabase.com/blog/meetup-kahoot-alternative\#resources)

- [Kahoot alternative GitHub repo](https://github.com/supabase-community/kahoot-alternative)
- [Anonymous Sign-in guide](https://supabase.com/docs/guides/auth/auth-anonymous)
- [Realtime Postgres changes guide](https://supabase.com/docs/guides/realtime/postgres-changes)
- [Supabase Next.js quick starter guide](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)

[![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-black.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-white.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Week](https://supabase.com/ga-week)

15-19 April

[Day 1 -Supabase is officially launching into General Availability](https://supabase.com/ga)

[Day 2 -Supabase Functions now supports AI models](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)

[Day 3 -Supabase Auth now supports Anonymous sign-ins](https://supabase.com/blog/anonymous-sign-ins)

[Day 4 -Supabase Storage: now supports the S3 protocol](https://supabase.com/blog/s3-compatible-storage)

[Day 5 -Supabase Security Advisor & Performance Advisor](https://supabase.com/blog/security-performance-advisor)

Build Stage

[01 -PostgreSQL Index Advisor](https://github.com/supabase/index_advisor)

[02 -Branching now Publicly Available](https://supabase.com/blog/branching-publicly-available)

[03 -Oriole joins Supabase](https://supabase.com/blog/supabase-acquires-oriole)

[04 -Supabase on AWS Marketplace](https://supabase.com/blog/supabase-aws-marketplace)

[05 -Supabase Bootstrap](https://supabase.com/blog/supabase-bootstrap)

[06 -Supabase Swift](https://supabase.com/blog/supabase-swift)

[07 -Top 10 Launches from Supabase GA Week](https://supabase.com/blog/ga-week-summary)

[Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon)

[Community Meetups](https://supabase.com/ga-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&text=The%20open%20source%20Kahoot%20alternative)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&text=The%20open%20source%20Kahoot%20alternative)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&t=The%20open%20source%20Kahoot%20alternative)

[Last post\\
\\
**Cal.com launches Expert Marketplace built with Next.js and Supabase.** \\
\\
18 June 2024](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase)

[Next post\\
\\
**What's new in pgvector v0.7.0** \\
\\
2 May 2024](https://supabase.com/blog/pgvector-0-7-0)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [What we built for the meetup](https://supabase.com/blog/meetup-kahoot-alternative#what-we-built-for-the-meetup)
- [Building the Kahoot alternative app](https://supabase.com/blog/meetup-kahoot-alternative#building-the-kahoot-alternative-app)
- [The Results](https://supabase.com/blog/meetup-kahoot-alternative#the-results)
- [Contributing to open source](https://supabase.com/blog/meetup-kahoot-alternative#contributing-to-open-source)
- [Resources](https://supabase.com/blog/meetup-kahoot-alternative#resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&text=The%20open%20source%20Kahoot%20alternative)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&text=The%20open%20source%20Kahoot%20alternative)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmeetup-kahoot-alternative&t=The%20open%20source%20Kahoot%20alternative)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

Twitter Widget Iframe

![Database diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foss-kahoot-alternative%2Ferd.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)