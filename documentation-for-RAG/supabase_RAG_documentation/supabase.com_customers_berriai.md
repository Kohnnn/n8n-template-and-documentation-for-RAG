---
url: "https://supabase.com/customers/berriai"
title: "Berri AI boosts productivity by migrating from AWS RDS to Supabase Vector"
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# Berri AI boosts productivity by migrating from AWS RDS to Supabase Vector

Learn how Berri AI overcame challenges with self-hosting their vector database on AWS RDS and successfully migrated to Supabase.

![Berri AI boosts productivity by migrating from AWS RDS to Supabase Vector logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fberriai.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Supercharge your products with the power of LLMs like ChatGPT & go from prototype to production in less than a week.

[https://www.berri.ai/](https://www.berri.ai/)

Backed byY Combinator

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

Berri AI is an API for businesses to programmatically create custom ChatGPT instances on their data. Their customers build production-ready ChatGPT Apps in minutes with features such as prebuilt flows, editable options, authentication, and logging.

## The Challenge [\#](https://supabase.com/customers/berriai\#the-challenge)

Initially, Berri AI attempted to develop with AWS RDS to reduce latency and gain more control over their infrastructure. However, they encountered various challenges, including development cycles, difficulties debugging errors, limited accessibility for non-database team members, and the complexity of managing connection pools and rollbacks. These issues hindered their ability to make changes quickly and impacted their overall productivity.

> The Python SDK simplified the process for me as a non-database person, empowering me to make
> changes and bug fixes. This significantly improved our update velocity, which had a huge impact on
> our productivity.
>
> ![Krrish D. - Co-Founder & CEO, Berri AI avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fkrrish-d.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Krrish D. - Co-Founder & CEO, Berri AI

## Why they chose Supabase: [\#](https://supabase.com/customers/berriai\#why-they-chose-supabase)

Berri AI migrated their vector database from AWS RDS to Supabase for several compelling reasons:

1. **Community:** After considering alternatives like Pinecone and Chroma, they prioritized a solution with a strong and accessible community, along with [managed infrastructure](https://supabase.com/docs/guides/platform).
2. **Fewer services to manage:** Since they were already utilizing Supabase for other purposes, it made sense for Berri AI to consolidate their systems and avoid the complexities of self-hosting. One of the major pain points they faced with their previous setup was managing connection pools and handling errors with the Postgres database hosted on AWS. This involved writing extensive code and dealing with rollbacks, with each database update function requiring 40-50 lines of code. Supabase simplified this process significantly by condensing it to just one line of code, eliminating the burdens of managing dependencies and handling new errors. This significantly improved their update velocity, which had a huge impact on their productivity.
3. **Better tooling:** Berri AI experienced frustration with pg\_admin. Supabase's user-friendly interface offered a seamless and efficient way to manage and read tables, eliminating the need for pg\_admin and providing a simple alternative. This streamlined their workflow and saved valuable time and effort. The accessibility of Supabase's client SDKs and intuitive interface played a crucial role in their decision as well. Team members who were not database experts found it easy to navigate and make changes, reducing reliance on specialized expertise and improving their overall workflow.
4. **Simplicity:** Supabase provides the ability to add new columns in a no-code manner, which provided flexibility and agility in responding to evolving requirements. This feature empowered the team to make on-the-fly adjustments and meet their immediate needs effectively.
5. **Flexibility:** Berri AI also appreciated Supabase's flexibility in allowing them to choose their [preferred embedding method](https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings), as it was not tied to a specific embedding model. This ensured compatibility and adaptability for their specific use case.

The migration to [Supabase Vector](https://supabase.com/vector), which facilitated efficient storage and retrieval of vectors, proved to be a significant advantage for Berri AI's operations.

> Switching to Supabase Vector was a game-changer for us. The faster view times allowed me to
> quickly access and debug data, enhancing my ability to analyze individual customer issues. The
> no-code option to add new columns on the fly was fantastic, enabling us to adapt swiftly.
>
> ![Krrish D. - Co-Founder & CEO, Berri AI avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fkrrish-d.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Krrish D. - Co-Founder & CEO, Berri AI

## What They Built [\#](https://supabase.com/customers/berriai\#what-they-built)

Berri AI built a platform that enables developers to create and manage custom ChatGPT instances for each individual user, integrating seamlessly with their unique data.

![BerriAI is backed by YCombinator](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Fberriai%2Fberriai-image.jpeg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

With Berri AI, businesses can rapidly scale the power of ChatGPT to cater to the needs of every user. The platform provides an out-of-the-box solution for managing a fleet of ChatGPT instances, offering businesses the ability to deliver personalized responses to user queries. This includes answering specific questions related to order status, monthly revenue, or generating personalized learning experiences in the education technology (EdTech) sector, such as summarizing lecture slides or generating practice questions from textbooks.

The platform's integration with Supabase empowers businesses to unlock the full potential of ChatGPT and deliver customized solutions for a wide range of use cases.

> With Supabase, my life has become much easier. Previously, managing connection pools and dealing
> with errors in the Postgres database hosted on AWS was a constant challenge. I had to write 40-50
> lines of code for each function, handle rollbacks, and struggle with dependencies and errors. But
> with Supabase, updating the database is now just one line of code. I no longer need to deal with
> complex dependencies and obscure errors. Additionally, the frustration of using pgadmin is gone.
> Supabase provides a simple UI that allows me to effortlessly manage and interact with my tables.
>
> ![Ishaan Jaffer - Co-Founder & CTO, Berri AI avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fishaan-jaffer.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Ishaan Jaffer - Co-Founder & CTO, Berri AI

## The Results [\#](https://supabase.com/customers/berriai\#the-results)

Berri AI achieved significant improvements in their operations by choosing Supabase Vector. They experienced streamlined database management, increased update velocity, and improved efficiency in accessing and debugging data. The user-friendly interface and flexibility of Supabase empowered non-experts within the team and facilitated agile adaptations to changing requirements. Overall, this decision transformed their workflow, enhancing productivity and positioning Berri AI for continued success and growth.

To learn more about how Supabas Vector can help you store vector embeddings at scale and build AI apps with ease, [reach out to us](https://forms.supabase.com/enterprise).

## Tech stack [\#](https://supabase.com/customers/berriai\#tech-stack)

- Zeet
- AWS
- OpenAI
- Hugging Face
- Supabase

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)