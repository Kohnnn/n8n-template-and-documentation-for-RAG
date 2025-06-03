---
url: "https://supabase.com/blog/using-supabase-replit"
title: "Using Supabase in Replit"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Using Supabase in Replit

11 Mar 2021

•

4 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Using Supabase in Replit](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Freplit-og.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Replit.com](http://replit.com/) is an awesome new browser based IDE where you can code alone or collaboratively with friends using their awesome multiplayer features! It's particularly useful for education, and sharing code examples with others.

They support a ton of different languages and execution environments and even recently introduced a simple key value store you can use to persist data.

As a Replit user, if you want to access larger amounts of data direct from your repl, or if you fancy accessing some super-powerful query tools, at some point you may want to start interacting with a relational database. Supabase is a good fit here; just like Replit, you don't need to worry about servers, and hosting, you can just click a few buttons and get a fully featured relational database which you can start communicating with directly from javacript, using supabase-js.

Using Supabase in Replit with node.js - YouTube

Supabase

54.4K subscribers

[Using Supabase in Replit with node.js](https://www.youtube.com/watch?v=lQ5iIxaYduI)

Supabase

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=lQ5iIxaYduI "Watch on YouTube")

Here's how to start a Supabase + Node.js repl:

Sign up for [replit.com](http://replit.com/) and hit new repl in the top left

![Untitled-2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2Fu3dljulzsyqu58i75epn.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Select node.js, give it a name, and click Create repl

![Untitled-1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2F7rcfbb12sfabevto571j.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Import supabase's createClient method and hit run to install the required libs:

`
const { createClient } = require('@supabase/supabase-js')
`

Setup a new Supabase project and grab the URL and anon key from Settings > API. Create the client in javascript using:

`
const supabase = createClient(
'https://ajsstlnzcmdmzbtcgbbd.supabase.co',
'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
)
`

![Untitled-3](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2F5j5aqyjdh74qm83slmli.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now that supabase is connected you'll want to add some data to your db, you can grab any SQL dataset on the web, or make your own, but the fasted way to test is to open the SQL tab in the Supabase dashboard and click the Countries sample database and click Run.

![Untitled-4](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2F54yykm6h9hqpric87zad.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

From within your repl you can now query your countries table like:

`
// .then() syntax
supabase.
.from('countries')
.select('*')
.limit(5)
.then(console.log)
.catch(console.error)
// or...
// async/await syntax
const main = async() => {
const { data, error } = supabase
    .from('countries')
    .select('*')
    .limit(5)
if (error) {
    console.log(error)
    return
}
console.log(data)
}
main()
`

Once this is working, if you want to learn more about the [query interface](https://supabase.com/docs/reference/javascript/filter) you might want to try some of these challenges:

`
// 1. List all the countries in Antarctica
// 2. Fetch the iso3 code of the country with ID 3
// 3. List the countries with 'Island' in the name
// 4. Count the number of countries that start with 'Z' or 'Q'
// 5. Fetch all the Countries where continents is null
`

There are full solutions provided in the video version of this blog, but some examples you may find useful are:

`
// or
const { data, error } = await supabase
.from('cities')
.select('name, country_id')
.or('id.eq.20,id.eq.30')
// is
const { data, error } = await supabase.from('cities').select('name, country_id').is('name', null)
// in
const { data, error } = await supabase
.from('cities')
.select('name, country_id')
.in('name', ['Rio de Janeiro', 'San Francisco'])
// neq (not equal to)
const { data, error } = await supabase
.from('cities')
.select('name, country_id')
.neq('name', 'The shire')
// full docs here: /docs/reference/javascript/filter
`

We look forward to showing off some more Supabase + Replit examples.

You can find my example repl here: [https://repl.it/@awalias/supabase-test#index.js](https://repl.it/@awalias/supabase-test#index.js)

Supabase has a Free Plan, head over to [https://supabase.com/dashboard](https://supabase.com/dashboard) to get started.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&t=Using%20Supabase%20in%20Replit)

[Last post\\
\\
**Developers stay up to date with intheloop.dev** \\
\\
22 March 2021](https://supabase.com/blog/In-The-Loop)

[Next post\\
\\
**Toad, a link shortener with simple APIs for low-coders** \\
\\
8 March 2021](https://supabase.com/blog/toad-a-link-shortener-with-simple-apis-for-low-coders)

[replit](https://supabase.com/blog/tags/replit) [node-js](https://supabase.com/blog/tags/node-js) [postgres](https://supabase.com/blog/tags/postgres)

On this page

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&t=Using%20Supabase%20in%20Replit)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)