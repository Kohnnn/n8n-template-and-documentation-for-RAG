---
url: "https://supabase.com/blog/designing-with-ai-midjourney"
title: "Designing with AI: Generating unique artwork for every user"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Designing with AI: Generating unique artwork for every user

07 Apr 2023

•

12 minute read

[![Marijana Pavlinić avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmarijanapav.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Marijana PavlinićDesign](https://github.com/marijanapav)

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Designing with AI: Generating unique artwork for every user](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fheader.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

While Supabase Launch Weeks happen online, we love the idea of bringing everyone together as if it was an in-person conference. Our ticketing system is one of the ways that we emulate this.

We have been issuing tickets since Launch Week 5, and they were so successful that we have done them ever since. It’s become a challenge to outdo the previous effort with something better every time.

## Prompts with Midjourney [\#](https://supabase.com/blog/designing-with-ai-midjourney\#prompts-with-midjourney)

You've probably heard of this "AI" tech, and most likely tired of the low-effort SkyNet memes. We wanted to do something more integrated with our developer/designer workflow. Something that we could share with developers & designers that they might find useful.

[Midjourney](https://www.midjourney.com/) was where we started for art generation. We experimented with prompts, blends, and colors to create eye-catching visuals for each ticket connected to a GitHub profile. Some first attempts and ideas included prompts like:

`
/imagine abstract 3 layers of waves on a dark background with light refracting through it, very cool subtle minimal dark illustration, purple light leak with subtle highlights
`

In our exploration of different commands and prompts, we found that the `/blend` command was particularly enjoyable and helpful for creating the desired visuals. This command allowed us to quickly upload multiple images and experiment with different combinations and aesthetics to create a cohesive new image. For designers, the `/blend` command is like `/imagine` but visual, making it easy to visually experiment with different elements. Experiments included blurred edges, planetoid shapes, light leaks, shadows, swirls, motion blurs, waves, cubes, reflections, bokeh, and lots and lots of _“make it look really really blurred”_.

![midjoruney experiments](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fexperiments.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

After exploring a variety of text prompts, blends, and styles, we decided that most of the visuals we generated were too chaotic and busy for our Launch Week tickets. Images felt cluttered and overwhelming, making it difficult to read overlaid text. We shifted our focus to creating a cleaner, simpler aesthetic. This required a selective approach to the visual components we wanted to include.

After what-seemed-like hours (okay, just a few), we were able to generate some interesting artwork that could be useful. We chose purple hues and simpler swirls - minimalist visuals that could serve as backgrounds for our tickets and landing page.

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fmidjourney-variations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Final AI generated images

### Chasing Gold Behind the Scenes [\#](https://supabase.com/blog/designing-with-ai-midjourney\#chasing-gold-behind-the-scenes)

When we were happy with the main visual for Launch Week 7, we also needed to create gold visuals for the extra special tickets, and those needed to look the same… but gold. Initially, we thought we could simply use the prompt `/imagine *seed number* make it gold` to generate the desired effect. To our surprise, MidJourney did not cooperate with this idea:

![midjourney failed attempts.jpg](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Ffailed-attempts.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We tried excluding certain elements, such as faces or circles to refine the output, and at one point every prompt ended with a `-- no faces, -- no circles, -- no gold bars ...`, but the occasional gold bars still appeared.

We needed to come up with a different approach (even though this approach seemed more fun).

Eventually, we just added a golden overlay gradient to previously generated images and then used `/blend` to blend the purple and the gold together.

And voila, we had a baseline for generating variations:

![midjourney blending variations](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fmidjourney-blending-variations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The final visual that you see everywhere won us over because of its vibrant swirls. While each swirl looks slightly different, a consistent style is still maintained throughout.

Fortunately, we didn't require full-width images for each ticket. Upscaled MidJourney images sufficed. Nevertheless, we had to recreate the main visual on the landing page in vectors to use it effectively. You can view it in full glory at [https://supabase.com/launch-week/7](https://supabase.com/launch-week/7).

![Screenshot 2023-04-06 at 09.47.47.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Flaunch-week-7-ticket-home.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Open Graph images [\#](https://supabase.com/blog/designing-with-ai-midjourney\#open-graph-images)

An important aspect of Launch Week tickets is their shareability. Each Launch Week we’ve been blown away by how many developers post their tickets on social channels (and we absolutely love seeing them!).

When you share your unique ticket URL, the image shown on the social preview is called an Open Graph image (or OG image for short).

These images are generated for each unique URL and ticket. This requires a bit of magic, which in our case means using a [Supabase Edge Function](https://supabase.com/docs/guides/functions) together with [Supabase Storage](https://supabase.com/docs/guides/storage) for smart caching.

### Supabase Edge Function 🤝 Supabase Storage [\#](https://supabase.com/blog/designing-with-ai-midjourney\#supabase-edge-function-supabase-storage)

Our Edge Function handles the generation of each ticket image, and also does a bunch of other things under the hood, like detecting if the ticket was shared on socials. This will become important later!

`
if (userAgent?.toLocaleLowerCase().includes('twitter')) {
// Attendee shared on Twitter
await supabaseAdminClient
    .from('lw7_tickets')
    .update({ sharedOnTwitter: 'now' })
    .eq('username', username)
    .is('sharedOnTwitter', null)
} else if (userAgent?.toLocaleLowerCase().includes('linkedin')) {
// Attendee shared on LinkedIn
await supabaseAdminClient
    .from('lw7_tickets')
    .update({ sharedOnLinkedIn: 'now' })
    .eq('username', username)
    .is('sharedOnLinkedIn', null)
}
`

We want to be as efficient as possible because generating a png file in an edge function is an expensive operation. We generate each ticket only once and then save it to Supabase Storage (which has a [smart CDN cache built in](https://supabase.com/blog/storage-image-resizing-smart-cdn#smart-cdn-deep-dive)).

So in the first step we check if we can fetch the user’s image from storage:

``
// Try to get image from Supabase Storage CDN.
storageResponse = await fetch(
`${STORAGE_URL}/tickets/regular/${BUCKET_FOLDER_VERSION}/${username}.png`
)
``

If we can’t find the image in storage, then we kick off the ticket generation pipeline, using Vercel’s awesome [open-source satori library](https://github.com/vercel/satori) transforms HTML & CSS into svgs!

Each image includes the user’s GitHub details. We use [`supabase-js`](https://supabase.com/docs/reference/javascript/installing) for authentication: users log in with their GitHub account and we store their username in a table in Postgres.

Since this table includes email addresses, we secure it using [RLS](https://supabase.com/docs/guides/auth/row-level-security) to ensure each user can only view their own data. At the same time, we want these tickets to be publicly shareable, and that’s where [Postgres Views](https://supabase.com/blog/postgresql-views) come in handy.

By creating a view, we can selectively publicize parts of our table and also compute some additional values on the fly:

`
drop view if exists lw7_tickets_golden;
create or replace view lw7_tickets_golden as
with
    lw7_referrals as (
      select
        referred_by,
        count(*) as referrals
      from lw7_tickets
      where referred_by is not null
      group by referred_by
    )
select
    lw7_tickets."id",
    lw7_tickets."name",
    lw7_tickets."username",
    lw7_tickets."ticketNumber",
    lw7_tickets."createdAt",
    lw7_tickets."sharedOnTwitter",
    lw7_tickets."sharedOnLinkedIn",
    lw7_tickets."bg_image_id",
    case
      when lw7_referrals.referrals is null then 0
      else lw7_referrals.referrals
    end as referrals,
    case
      when lw7_tickets."sharedOnTwitter" is not null
      and lw7_tickets."sharedOnLinkedIn" is not null then true
      else false
    end as golden
from
    lw7_tickets
    left outer join lw7_referrals on lw7_tickets.username = lw7_referrals.referred_by;
select *
from lw7_tickets_golden;
`

We can now retrieve that username by using the following code:

`
// Get ticket data
const { data, error } = await supabaseAdminClient
.from('lw7_tickets_golden')
.select('name, ticketNumber, golden, bg_image_id')
.eq('username', username)
.maybeSingle()
if (error) console.log(error.message)
if (!data) throw new Error('user not found')
const { name, ticketNumber, bg_image_id } = data
const golden = data?.golden ?? false
`

You can now probably guess why our edge function was tracking requests from the Twitter and LinkedIn bots! That’s exactly the condition used to turn your ticket golden. How cool is that, with the power of Postgres, we can do all of this within the Database, absolutely mind-blowing. Also, we can easily track a referral count. Relational DBs for the win!

With our public view in place, we can now easily retrieve the relevant ticket details needed to generate the image, via `supabase-js`:

The ticket image itself is just a layering of some background images, your GitHub profile picture, and some text elements, et voila you’ve got yourself a unique ticket image!

![Main background image](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fticket-backdrop.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Main background image

![Ticket outline](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fticket-outline.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Ticket outline

![Random AI generated background for the ticket outline](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fticket-ai-background.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Random AI generated background for the ticket outline

![Layer it all together and put some nice text on top and you got yourself a beautiful ticket!](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fticket-details.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Layer it all together and put some nice text on top and you got yourself a beautiful ticket!

Once generated, we can conveniently upload the image to Supabase Storage using `supabase-js`. This ensures fast response times as well as efficient resource usage.

``
const type = golden ? 'golden' : 'regular'
// Upload image to storage.
const { error: storageError } = await supabaseAdminClient.storage
.from('images')
.upload(`lw7/tickets/${type}/${BUCKET_FOLDER_VERSION}/${username}.png`, generatedImage.body, {
    contentType: 'image/png',
    cacheControl: '31536000',
    upsert: false,
})
``

And of course, all of this is open source, you can find the full function code [here](https://github.com/supabase/supabase/tree/master/apps/www/supabase/functions/lw7-ticket-og). Please feel free to utilize it for your own Launches!

### Turning tickets golden in realtime [\#](https://supabase.com/blog/designing-with-ai-midjourney\#turning-tickets-golden-in-realtime)

Using the power of the entire Supabase stack, we’ve designed a pretty neat mechanic to allow users to turn their tickets golden.

In previous Launch Weeks, we employed the [fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) to sprinkle golden tickets around using the ticket number sequence. This time around we wanted to make it more interactive and allow the user to earn their golden ticket, increasing their chance to win swag.

Remember the Twitter and LinkedIn bot detection from above? We use those to generate the `golden` column in our public view:

`
case
when lw7_tickets."sharedOnTwitter" is not null
and lw7_tickets."sharedOnLinkedIn" is not null then true
else false
end as golden
`

As folks are sharing their tickets on socials to earn their gold status, we also want to give them realtime feedback on their progress. Luckily we also have a feature for that, [Supabase Realtime](https://supabase.com/realtime).

Something that would have been a headache in the past is just a couple of lines of client-side JavaScript:

``
const channel = supabase
.channel('changes')
.on(
    'postgres_changes',
    {
      event: 'UPDATE',
      schema: 'public',
      table: 'lw7_tickets',
      filter: `username=eq.${username}`,
    },
    (payload) => {
      const golden = !!payload.new.sharedOnTwitter && !!payload.new.sharedOnLinkedIn
      setUserData({
        ...payload.new,
        golden,
      })
      if (golden) {
        channel.unsubscribe()
      }
    }
)
.subscribe()
``

Interested to know how this fits within your Next.js application? Find the code [here](https://github.com/supabase/supabase/blob/master/apps/www/components/LaunchWeek/7/Ticket/TicketForm.tsx#L70-L102).

## Displaying the images [\#](https://supabase.com/blog/designing-with-ai-midjourney\#displaying-the-images)

We have some images, so how can we now display them somewhere? [@Francesco Sansalvadore](https://twitter.com/frnk_snslvdr) saw one of our team members trying to “swipe” on the tickets slider component on the [launch week page](https://supabase.com/launch-week/7/tickets) and he thought, why not feature all the fantastic people who generated tickets on a single page?

We built a [ticket wall](https://supabase.com/launch-week/7/tickets) that you can scroll endlessly. We approached it with an infinite scroll technique, lazy-loading a few tickets at a time.

![launch week 7 ticket wall](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Flaunch-week-7-ticket-wall.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

If you’re interested in a more detailed step-by-step guide to reproduce this effect, take a look at the [Infinite scroll with Next.js, Framer Motion, and Supabase](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion) blog post.

## Get your ticket [\#](https://supabase.com/blog/designing-with-ai-midjourney\#get-your-ticket)

You too can also be Charlie Bucket and have a Golden Ticket. There is no chocolate factory, however, but we do have some amazing swag to win.

Up for grabs are:

- Supabase mechanical keyboard. In fact, we have 3 of them to give away!\_ Guaranteed to annoy your co-workers/cat/partner/ yourself.
- Socks: _Perfect for your `<footer>`. Right?!.. anyway._
- T-shirts - _Just don’t put them in a tumble dryer_
- and; of course a bunch of stickers.

## More Supabase AI reading [\#](https://supabase.com/blog/designing-with-ai-midjourney\#more-supabase-ai-reading)

- [Supabase storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/blog/openai-embeddings-postgres-vector)
- [Supabase Docs Search](http://supabase.com/docs)
- [Streaming Data in Edge Functions](https://www.youtube.com/watch?v=9N66JBRLNYU)
- [Next.js OpenAI Doc Search template](https://github.com/supabase-community/nextjs-openai-doc-search)

### More Launch Week 7

[Designing with AI\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/designing-with-ai-midjourney)

[Supavisor\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://github.com/supabase/supavisor)

[Open Source Logging\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-logs-self-hosted)

[Self-hosted Deno Edge Functions\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)

[Storage v3: Resumable Uploads with support for 50GB files\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/storage-v3-resumable-uploads)

[Supabase Auth: SSO, Mobile, and Server-side support\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-auth-sso-pkce)

[Community Highlight\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/launch-week-7-community-highlights)

[Studio Updates\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-studio-2.0)

[dbdev\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/dbdev)

[Postgres TLE\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/pg-tle)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdesigning-with-ai-midjourney&text=Designing%20with%20AI%3A%20Generating%20unique%20artwork%20for%20every%20user)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdesigning-with-ai-midjourney&text=Designing%20with%20AI%3A%20Generating%20unique%20artwork%20for%20every%20user)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdesigning-with-ai-midjourney&t=Designing%20with%20AI%3A%20Generating%20unique%20artwork%20for%20every%20user)

[Last post\\
\\
**Supabase Beta March 2023** \\
\\
8 April 2023](https://supabase.com/blog/supabase-beta-update-march-2023)

[Next post\\
\\
**The Supabase AI Hackathon** \\
\\
7 April 2023](https://supabase.com/blog/launch-week-7-hackathon)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Prompts with Midjourney](https://supabase.com/blog/designing-with-ai-midjourney#prompts-with-midjourney)
  - [Chasing Gold Behind the Scenes](https://supabase.com/blog/designing-with-ai-midjourney#chasing-gold-behind-the-scenes)
- [Open Graph images](https://supabase.com/blog/designing-with-ai-midjourney#open-graph-images)
  - [Supabase Edge Function 🤝 Supabase Storage](https://supabase.com/blog/designing-with-ai-midjourney#supabase-edge-function-%F0%9F%A4%9D-supabase-storage)
  - [Turning tickets golden in realtime](https://supabase.com/blog/designing-with-ai-midjourney#turning-tickets-golden-in-realtime)
- [Displaying the images](https://supabase.com/blog/designing-with-ai-midjourney#displaying-the-images)
- [Get your ticket](https://supabase.com/blog/designing-with-ai-midjourney#get-your-ticket)
- [More Supabase AI reading](https://supabase.com/blog/designing-with-ai-midjourney#more-supabase-ai-reading)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdesigning-with-ai-midjourney&text=Designing%20with%20AI%3A%20Generating%20unique%20artwork%20for%20every%20user)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdesigning-with-ai-midjourney&text=Designing%20with%20AI%3A%20Generating%20unique%20artwork%20for%20every%20user)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdesigning-with-ai-midjourney&t=Designing%20with%20AI%3A%20Generating%20unique%20artwork%20for%20every%20user)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fdesigning-with-ai-midjourney%2Fmidjourney-variations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)