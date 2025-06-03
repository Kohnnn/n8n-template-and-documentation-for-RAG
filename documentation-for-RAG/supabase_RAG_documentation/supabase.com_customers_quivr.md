---
url: "https://supabase.com/customers/quivr"
title: "Quivr launch 5,000 Vector databases on Supabase."
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# Quivr launch 5,000 Vector databases on Supabase.

Learn how one of the most popular Generative AI projects uses Supabase as their Vector Store.

![Quivr launch 5,000 Vector databases on Supabase. logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fquivr.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Quivr is an open source 'second brain'. It's like a private ChatGPT, personalized with your own data: you upload your documents and you can then search and ask questions using generative AI.

[https://quivr.app](https://quivr.app/)

Use caseGenerative AI

SolutionsSupabase Vector, Supabase Auth

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

## The challenge: Building a second brain [\#](https://supabase.com/customers/quivr\#the-challenge-building-a-second-brain)

In May of 2023, [Stan Girard's](https://twitter.com/_StanGirard) started building small prototypes that allowed him to "chat with documents". After 2 weeks of research, he settled on an idea - build a "second brain" where a user could dump all their digital knowledge (audio, URLs, text, and code) into a vector store and query it with GPT4.

He built the first version in a single afternoon, pushed it to GitHub, and then [tweeted about it](https://twitter.com/_StanGirard/status/1657021618571313155?s=20). One viral tweet later, and [Quivr](https://github.com/StanGirard/quivr) was born.

## Choosing a vector database [\#](https://supabase.com/customers/quivr\#choosing-a-vector-database)

A critical piece of the tech stack was the vector store. Stan needed a place to store millions of embeddings. After comparing between Supabase, Pinecone, and Chroma, he settled on [Supabase Vector](https://supabase.com/vector), our open source vector offering for developing AI applications. The decision was driven largely by his familiarity with Postgres, and the tight integration with Vercel.

> Supabase Vector powered by pgvector allowed us to create a simple and efficient product. We are
> storing over 1.6 million embeddings and the performance and results are great. Open source
> develop can easily contribute thanks to the SQL syntax known by millions of developers.
>
> ![Stan Girard, Founder of Quivr. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fstan-girard-avatar.jpeg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Stan Girard, Founder of Quivr.

## Building an open source community [\#](https://supabase.com/customers/quivr\#building-an-open-source-community)

It didn't take long for the Quivr community to grow. After the viral launch, the [Quivr repo](https://github.com/StanGirard/quivr) stayed at number 1 on [GitHub Trending](https://github.com/trending) for 4 days. Today, it has over 22,000 GitHub stars and 67 contributors. Supabase has been a key part of the open source stack since the beginning.

> Because Supabase is open source, the possibility of running it locally made it a better choice
> compared with other products like Auth0. Since Auth is integrated with the Vector database it
> made Quivr much simpler. Features like Storage and Edge Functions allowed us to expand Quivr's
> functionality while keeping the project simple.
>
> ![Stan Girard, Founder of Quivr. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fstan-girard-avatar.jpeg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Stan Girard, Founder of Quivr.

## Launching 5000 databases [\#](https://supabase.com/customers/quivr\#launching-5000-databases)

One of the most pivotal growth events was getting picked up by [an influential YouTuber](https://www.youtube.com/watch?v=rFEbz93G9U8). His 11-minute overview of Quivr launched over 2000 Quivr projects on Supabase in one week. There are now 5,100 Quivr databases on Supabase, making it one of the most influential communities on the Supabase platform.

## Launching a hosted product [\#](https://supabase.com/customers/quivr\#launching-a-hosted-product)

Stan also launched a [hosted version of Quivr](https://www.quivr.app/), for users to sign up and get started immediately, without requiring any self-hosting infrastructure. Quivr's open source success has translated through their hosted platform, with 17,000 signups in just over 2 months, with 200 new users joining every day. The hosted database provides embedding storage for 1.6 million vectors and similarity search for over 100,000 files.

With 500 daily active users, the [Quivr.app](http://quivr.app/) is becoming the preferred way for users to create a second brain.

## Tech Stack [\#](https://supabase.com/customers/quivr\#tech-stack)

- Backend: Fast API + Langchain, hosted on AWS Fargate
- Frontend: Next.js, hosted on Vercel
- Database: Supabase Vector, using pgvector
- LLM: OpenAI, Anthropic, Nomic
- Semantic search using GPT For ALL, Anthropic, and OpenAI
- Auth: Supabase Auth

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)