---
url: "https://supabase.com/blog/how-design-works-at-supabase"
title: "How design works at Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# How design works at Supabase

08 Dec 2023

•

9 minute read

[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jonny Summers-MuirProduct Design](https://github.com/mildtomato)

[![Marijana Pavlinić avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmarijanapav.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Marijana PavlinićDesign](https://github.com/marijanapav)

[![Francesco Sansalvadore avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffsansalvadore.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Francesco SansalvadoreEngineering](https://github.com/fsansalvadore)

![How design works at Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Fdesign-at-supabase-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

After three years, only now are we figuring out “what design is” for Supabase and how it functions in the wider org.

We recently became a team of three, developing a somewhat-unique culture to increase the output and quality of our own team and the product teams. Here are a few insights into what we’ve learned along the way.

## Our approach to design [\#](https://supabase.com/blog/how-design-works-at-supabase\#our-approach-to-design)

To design at Supabase, you have to think like an agile developer.

What minimal increment will have the biggest impact, with the lowest engineering effort? We make small daily gains while simultaneously solving large milestones. We aim to [ship daily and dream in years.](https://twitter.com/DJ44/status/819316928623902720?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E819316928623902720%7Ctwgr%5E27904ffca0505db58a08f405f950312e7de970d3%7Ctwcon%5Es1_c10&ref_url=https%3A%2F%2Fsensible.blog%2F2020%2F11%2F24%2Fdream-in-years-plan-in-months-ship-in-days%2F)

The emphasis is on the daily gains, unblocking problems with design work so that no team is paralyzed by how something should work, function or look. This can manifest in: static mockups, interactive prototypes in Figma, code prototypes, wireframe sketches, and sometimes we actually start building it (👀). We do any work that can help the organization build consensus.

Let’s take an example, our LWX ticket page:

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Flwx-tickets-iterations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Late in the build process an idea was floated to try and integrate a _Wordle_ type easter egg into the site. We build some designs to help the discussion:

![something](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Flwx-ticket-1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![something](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Flwx-ticket-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The left image is Figma where as the right is Prod. The team aligned quickly on an outcome and aesthetic and then we iterate, simplify, and evolve the concept as we go.

The designs helped to avoid [bikeshedding](https://en.wiktionary.org/wiki/bikeshedding)—confining the engineering discussions to “how will someone find this” or “will someone use this”.

### Iterative changes [\#](https://supabase.com/blog/how-design-works-at-supabase\#iterative-changes)

After we have shipped to prod, design work becomes expired. Whatever is mocked before no longer serves a purpose.

We took some inspiration from [Linear’s approach](https://x.com/karrisaarinen/status/1715091479184736629?s=20)—taking screenshots of what is in prod, and using the screenshots to construct mockups.

Here’s an example where we are making changes to the Table Editor:

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Fscreenshots-in-mockups.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

A screenshot of the Table Editor from prod in a mockup

We simply screenshot what is in prod, (in this case the cells in the Table Editor) and then overlay any Figma elements on top to quickly iterate. We don’t need to keep re-building UI components in Figma just to keep up with what’s in prod.

## Principle led [\#](https://supabase.com/blog/how-design-works-at-supabase\#principle-led)

For a long time we operated without any sort of consensus of what Design _is_ at Supabase: what are our values, what do we like, what do we not like?

It’s surprising how far you can get without these. After three years, we noticed that we were drifting into contradictory aesthetics and it was becoming challenging to support other teams.

When Supabase was founded, the team agreed on a set of [Product Principles](https://supabase.com/docs/guides/getting-started/architecture#product-principles). Internally, we’ve expanded this concept to all teams, products, and functions at Supabase.

The Design team adopted and maintain two sets of principles:

- [Aesthetic Principles](https://supabase.com/blog/how-design-works-at-supabase#aesthetic-principles)
- [Product Design Principles](https://supabase.com/blog/how-design-works-at-supabase#product-design-principles)

### Aesthetic principles [\#](https://supabase.com/blog/how-design-works-at-supabase\#aesthetic-principles)

We needed to agree on what we collectively like and dislike on an emotional level. Aligning on a common aesthetic avoids debates on individual elements.

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Faesthetic-moodboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Aesthetic mood board of what Design team like externally

After the team voted on their likes and dislikes, patterns begin to emerge: colors, tones, shapes, typography, layout, etc.

We used these preferences to build higher-level alignment, leading to our founding principles such as:

#### Timelessness [\#](https://supabase.com/blog/how-design-works-at-supabase\#timelessness)

- We always ask critically: will this still feel good in a few years?
- Are we following a trend we’ve recently seen?
- _We buck trends, not follow them._

#### Less is more [\#](https://supabase.com/blog/how-design-works-at-supabase\#less-is-more)

- Always remove the fluff
- Remove overbearing information
- [Dieter Rams](https://en.wikipedia.org/wiki/Dieter_Rams#Less_and_More_exhibition) ftw

We enforce these principles by following agreed tactics: mantras such as “be more subtle”, “simplify simplify simplify”, “use brand green only for CTA”.

This has helped the team push in a unified direction. Perhaps you have already noticed recent updates? They are more fine-tuned, more subtle, use less green, and so on.

### Product design principles [\#](https://supabase.com/blog/how-design-works-at-supabase\#product-design-principles)

Product Principles are about collaborating with Product teams. We came up with a list of principles that we think are important for effective velocity. To share just a few of our favorites:

#### Design for the "Postgres developer" [\#](https://supabase.com/blog/how-design-works-at-supabase\#design-for-the-postgres-developer)

We are moving towards a SQL-first experience in the dashboard. You’ll see some LWX announcements that lean more into empowering developers to learn SQL.

#### Consolidation follows kaizen [\#](https://supabase.com/blog/how-design-works-at-supabase\#consolidation-follows-kaizen)

Product Teams must ship _[kaizen](https://en.wikipedia.org/wiki/Kaizen)_ improvements. But it’s the Design team’s role to consolidate after. This helps with velocity: we are not a blocker in the development process.

For example, yesterday the Frontend team added a “New organization” button in the Dashboard based on a message from Kevin (see below). They skipped Design team input and shipped a quick solution. The Design team can do a more refined layout update after LWX, improving the page as a whole.

![something](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Fkaizen-before-consildation.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

#### 80/20 [\#](https://supabase.com/blog/how-design-works-at-supabase\#8020)

We bias towards the 80% of developers using Supabase. Following the [Pareto Principle](https://www.investopedia.com/terms/p/paretoprinciple.asp), we focus on the smallest changes that have the largest impact on our userbase.

This isn’t always easy, since there is usually a vocal minority.

#### Build patterns [\#](https://supabase.com/blog/how-design-works-at-supabase\#build-patterns)

Repeatable actions that enforce muscle memory will always be preferred. When adding new features, (or, most likely nowadays; _overhauling features_) we always consider how the same UI patterns can work in other areas.

You will start to notice these principles being applied more throughout the LWX features announced this week.

## Tools and Tactics [\#](https://supabase.com/blog/how-design-works-at-supabase\#tools-and-tactics)

We use very few tools (across the entire org), and we build good processes and practices around them. Let’s review a couple for the Design team:

### Figma [\#](https://supabase.com/blog/how-design-works-at-supabase\#figma)

No introduction required. We’ve used Figma since the beginning and will continue to be our workhorse for application UI design and marketing design.

We’ve organized our Figma library into quarterly files, that are clearly labelled as “in progress” or “archived” so anyone can easily find the latest and greatest.

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Ffigma-organization.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Design system [\#](https://supabase.com/blog/how-design-works-at-supabase\#design-system)

We started maintaining a library during LW5, but only recently started using it in earnest. We’ve kept the system deliberately small, only adding what we’ve used more than a few times. The library then doesn’t spread into unique use-cases and suffer from content bloat.

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Ffigma-design-system.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Luckily, Figma features such as [nested components](https://www.figma.com/best-practices/component-architecture/#nested-components) came out while we were revamping this set of components. This meant we could reduce the footprint of the design system significantly. Figma libraries previously required every permutation of a component, but it’s now easy to contain things like swappable “icons” or pseudo states like “active” within components.

## The Design Engineer [\#](https://supabase.com/blog/how-design-works-at-supabase\#the-design-engineer)

They say designers who code are unicorns. So we found a few.

At some point in many Designer’s careers they become so frustrated with the speed of development and decide, _enough is enough_, _I’m not satisfied_, _I’m going to learn JavaScript!_

Or, it’s the other way round, a Developer is frustrated at designs handed to them, and decide it’s time to figure this out themselves.

We are describing a Design Engineer: The Unicorn.

Several team members now fit the “Design Engineer” description and it has enabled rapid shipping. Design doesn’t stop at wireframes: often some of the best iterations happen in code. Design work is treated as a reference more than a pixel-perfect outcome. With multiple Design Engineers, they are all co-owners, fine tuning what matters and what inevitably ends up in production.

### Design files that update prod [\#](https://supabase.com/blog/how-design-works-at-supabase\#design-files-that-update-prod)

Just today we saw this tweet:

[![something](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Fsoleio-tweet.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://x.com/soleio/status/1732082949670023373?s=20)

Today, this statement is true. But does it need to be? Can we update production from Figma? The answer is, yes; partly.

At Supabase, we have a pipeline that exports [Figma variables](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma) into [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties), used with TailwindCSS. What does this mean? Developing apps with TailwindCSS in the main monorepo uses the same color palette as our files in Figma.

Our Tailwind can now be used like this:

`background.default` in TailwindCSS is `"bg"`

`background.alternative` in TailwindCSS is `“bg-alternative”`

`foreground.DEFAULT` in TailwindCSS is `”text”`

`foreground.light` in TailwindCSS is `“text-light”`

Now we have a fully sync’d color system between design files and our actual development environment. We can also expand into other properties such as spacing, sizes, typography and so on.

## Team of three [\#](https://supabase.com/blog/how-design-works-at-supabase\#team-of-three)

The team has been kept small, and deliberately! Only adding people when we hit a resource tipping point. Today, we only have three people.

Jonny was the first team member in Supabase with any design background. We (just) survived until before LW5, when Marijana joined. And before LW7, Francesco joined. You may have noticed the quality creeping up while also accelerating recently.

All three compliment each other: while one shines in visual design, another does in product design, another in motion design. Though we also overlap enough in a way that helps to keep the ball rolling in an async setting.

### I like this, how do I join? [\#](https://supabase.com/blog/how-design-works-at-supabase\#i-like-this-how-do-i-join)

We’re always on the look out for talent, even if there’s no [job posting](https://supabase.com/careers), reach out to [Jonny](https://twitter.com/JSummersMuir), [Marijana](https://twitter.com/marijanapav) or [Francesco](https://twitter.com/frnk_snslvdr) on Twitter.

[Launch Week![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/launch-week)

11-15 Dec

Main Stage

[Day 1 -Supabase Studio: introducing an **AI Assistant**, **Postgres roles**, and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)

[Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)

[Day 3 -Introducing Supabase **Branching**, a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)

[Day 4 -Supabase Auth: **Identity Linking**, **Session Control**, **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)

[Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage

[01 -Supabase Album](https://supabase.productions/)

[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)

[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)

[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)

[05 -pg\_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)

[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)

[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)

[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)

[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)

[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)

[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)

[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)

[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-design-works-at-supabase&text=How%20design%20works%20at%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-design-works-at-supabase&text=How%20design%20works%20at%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-design-works-at-supabase&t=How%20design%20works%20at%20Supabase)

[Last post\\
\\
**Supabase Studio: AI Assistant and User Impersonation** \\
\\
11 December 2023](https://supabase.com/blog/studio-introducing-assistant)

[Next post\\
\\
**Postgres Language Server: implementing the Parser** \\
\\
8 December 2023](https://supabase.com/blog/postgres-language-server-implementing-parser)

[launch-week](https://supabase.com/blog/tags/launch-week) [design](https://supabase.com/blog/tags/design)

On this page

- [Our approach to design](https://supabase.com/blog/how-design-works-at-supabase#our-approach-to-design)
  - [Iterative changes](https://supabase.com/blog/how-design-works-at-supabase#iterative-changes)
- [Principle led](https://supabase.com/blog/how-design-works-at-supabase#principle-led)
  - [Aesthetic principles](https://supabase.com/blog/how-design-works-at-supabase#aesthetic-principles)
  - [Product design principles](https://supabase.com/blog/how-design-works-at-supabase#product-design-principles)
- [Tools and Tactics](https://supabase.com/blog/how-design-works-at-supabase#tools-and-tactics)
  - [Figma](https://supabase.com/blog/how-design-works-at-supabase#figma)
  - [Design system](https://supabase.com/blog/how-design-works-at-supabase#design-system)
- [The Design Engineer](https://supabase.com/blog/how-design-works-at-supabase#the-design-engineer)
  - [Design files that update prod](https://supabase.com/blog/how-design-works-at-supabase#design-files-that-update-prod)
- [Team of three](https://supabase.com/blog/how-design-works-at-supabase#team-of-three)
  - [I like this, how do I join?](https://supabase.com/blog/how-design-works-at-supabase#i-like-this-how-do-i-join)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-design-works-at-supabase&text=How%20design%20works%20at%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-design-works-at-supabase&text=How%20design%20works%20at%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-design-works-at-supabase&t=How%20design%20works%20at%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Flwx-tickets-iterations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Fscreenshots-in-mockups.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Faesthetic-moodboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Ffigma-organization.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-how-design-works-at-supabase%2Ffigma-design-system.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)