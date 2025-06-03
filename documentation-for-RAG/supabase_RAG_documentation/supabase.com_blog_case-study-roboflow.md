---
url: "https://supabase.com/blog/case-study-roboflow"
title: "Roboflow.com choose Supabase to power Paint.wtf leaderboard"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Roboflow.com choose Supabase to power Paint.wtf leaderboard

09 Feb 2021

•

3 minute read

[![Rory Wilding avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Froryw10.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Rory WildingHead of Growth](https://github.com/roryw10)

![Roboflow.com choose Supabase to power Paint.wtf leaderboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Froboflow-website.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Brad Dwyer is the founder of [Roboflow](https://roboflow.com/?ref=supabase), a startup helping developers build computer vision into their applications. Their solution allows developers, with zero computer vision experience, to go from images to a trained computer vision model in minutes.

Learn how Brad and Roboflow used Supabase to launch [Paint.wtf](https://paint.wtf/), a product which survived traffic generated from the front page of Hacker News, Reddit, and Product Hunt.

![Supabase and Strive are partnering up to teach OSS.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Froboflow-website.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## From idea to a launch in a weekend [\#](https://supabase.com/blog/case-study-roboflow\#from-idea-to-a-launch-in-a-weekend)

Brad and a friend ( [Erik Dunteman](https://twitter.com/erikdoingthings)) wanted to experiment with OpenAI's new [CLIP](https://openai.com/blog/clip/) model through a side project they could build in a weekend. CLIP classifies a wide range of images by flipping image classification into a text similarity task. Current image classifiers are limited because they are trained on a fixed number of categories. In contrast, CLIP learns from the raw text describing the images meaning the classifier isn't limited by labels and supervised learning. The team recognised that CLIP opens up a vast range of use cases that have been difficult previously due to the time required to collect images and train the model.

Roboflow settled on a straightforward concept: they prompt users to draw an image which is then fed into CLIP. The AI then judges how close the drawing is to the given prompt and assigns it a score. Users' performance is tracked on a leaderboard for each prompt and users can see how well they performed against their peers according to the model.

## Leaderboards that Count [\#](https://supabase.com/blog/case-study-roboflow\#leaderboards-that-count)

Brad and the team needed a leaderboard to make this idea work. While their first intuition was to use Firebase, it lacks the built-in functionality for counting the number of documents in a collection - a critical function for implementing their leaderboard design.

![Supabase and Strive are partnering up to teach OSS.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Froboflow-stat.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You might export data to BigQuery, or implement an increment function on collection change, however PostgreSQL has great built in support for counting and Brad felt like this would be the perfect opportunity to test out Supabase and get the functionality he needed for the leaderboards to work reliably and without implementing add-ons.

## One weekend to break the internet [\#](https://supabase.com/blog/case-study-roboflow\#one-weekend-to-break-the-internet)

Brad and the team built the product overnight and launched it on Hacker News. Paint.wtf went on to make it to Hacker News and Reddit's first page, and getting traction on Product Hunt. As a result, they had to handle serious user volumes; at its peak, users were submitting over 2 new drawings every second.

Over 100K users submitted drawings in a 24 hour span. At this point, Brad knew he had picked the right setup for his leaderboard as even with this massive spike in usage it continued to perform reliably so his users could get accurate and up to date rankings for their submissions.

![Supabase and Strive are partnering up to teach OSS.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Froboflow-gallery.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Paint.Wtf has continued to get sustained coverage in the media and has continued to pick up new and unexpected use cases. For example, remote teams are using Paint.wtf as part of their daily ice breaker activities during COVID to keep up team social cohesion.

![Supabase and Strive are partnering up to teach OSS.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Froboflow-quote.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Ship fast, and carry on scaling [\#](https://supabase.com/blog/case-study-roboflow\#ship-fast-and-carry-on-scaling)

Thanks to Supabase, Roboflow could launch quickly and keep scaling despite the huge user volumes their innovative project generated overnight.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcase-study-roboflow&text=Roboflow.com%20choose%20Supabase%20to%20power%20Paint.wtf%20leaderboard)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcase-study-roboflow&text=Roboflow.com%20choose%20Supabase%20to%20power%20Paint.wtf%20leaderboard)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcase-study-roboflow&t=Roboflow.com%20choose%20Supabase%20to%20power%20Paint.wtf%20leaderboard)

[Last post\\
\\
**Cracking PostgreSQL Interview Questions** \\
\\
27 February 2021](https://supabase.com/blog/cracking-postgres-interview)

[Next post\\
\\
**Supabase Beta January 2021** \\
\\
2 February 2021](https://supabase.com/blog/supabase-beta-january-2021)

[AI](https://supabase.com/blog/tags/AI)

On this page

- [From idea to a launch in a weekend](https://supabase.com/blog/case-study-roboflow#from-idea-to-a-launch-in-a-weekend)
- [Leaderboards that Count](https://supabase.com/blog/case-study-roboflow#leaderboards-that-count)
- [One weekend to break the internet](https://supabase.com/blog/case-study-roboflow#one-weekend-to-break-the-internet)
- [Ship fast, and carry on scaling](https://supabase.com/blog/case-study-roboflow#ship-fast-and-carry-on-scaling)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcase-study-roboflow&text=Roboflow.com%20choose%20Supabase%20to%20power%20Paint.wtf%20leaderboard)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcase-study-roboflow&text=Roboflow.com%20choose%20Supabase%20to%20power%20Paint.wtf%20leaderboard)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcase-study-roboflow&t=Roboflow.com%20choose%20Supabase%20to%20power%20Paint.wtf%20leaderboard)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)