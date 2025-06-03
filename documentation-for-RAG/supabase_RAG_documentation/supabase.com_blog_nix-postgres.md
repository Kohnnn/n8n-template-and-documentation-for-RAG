---
url: "https://supabase.com/blog/nix-postgres"
title: "Packaging Supabase with Nix"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Packaging Supabase with Nix

25 Apr 2024

•

5 minute read

[![Sam Rose avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsamrose.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Sam RoseEngineering](https://github.com/samrose)

![Packaging Supabase with Nix](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnix-postgres.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## What is Nix? [\#](https://supabase.com/blog/nix-postgres\#what-is-nix)

Straight from the [Nix manual](https://nixos.org/manual/nix/stable/introduction#introduction):

> Nix is a _purely functional package manager_. This means that it treats packages like values in purely functional programming languages such as Haskell — they are built by functions that don’t have side-effects, and they never change after they have been built. Nix stores packages in the _Nix store_, usually the directory `/nix/store`, where each package has its own unique sub-directory such as

`
/nix/store/b6gvzjyb2pg0kjfwrjmg1vfhh54ad73z-firefox-33.1/
`

> where `b6gvzjyb2pg0…` is a unique identifier for the package that captures all its dependencies (it’s a cryptographic hash of the package’s build dependency graph). This enables many powerful features.

## Powerful features like what? [\#](https://supabase.com/blog/nix-postgres\#powerful-features-like-what)

The implications of purely functional builds are too far reaching to fully explore here, but the key properties we’re excited about are:

- **Dependency Isolation:** Dependencies are managed in total isolation from each other, preventing conflicts and ensuring that each component functions as expected.
- **Deterministic Builds:** A side-effect of explicit defining input components and isolating their builds is that those builds become deterministic, reproducing bit for bit identical outputs on each run. This ensures reliability and consistency over time.
- **Efficient Caching:** With deterministic builds, components can be freely cached and reused to significantly reduce build times.

## Current Builds [\#](https://supabase.com/blog/nix-postgres\#current-builds)

The main artifacts from the `supabase/postgres` build pipeline include:

- An AWS AMI for hosting EC2 instances with our flavor of Postgres with Supabase add-ons
- A Docker image with those same components that can be used for local hosting or deployment on Fly.io

We use popular tools like Packer and Ansible in tandem with GitHub Actions to build, test, and release those artifacts in CI.

Over time the Supabase Platform has grown up. We started with Postgres, PostgREST and Realtime. Next came Auth, and Storage, then GraphQL, and Functions. Postgres itself also has a suite of independently versioned extensions that we maintain and periodically upgrade.

As the constraints from the various tools in our stack combined it became impractical to run builds on local development machines. To accommodate, we pushed all builds to consistent build machines on CI. Today those builds take between 30-60 minutes. Given some of the larger components we bake in, like PL/v8, we’re fairly happy with that runtime. Even so, we can do better!

## How’s it going? [\#](https://supabase.com/blog/nix-postgres\#hows-it-going)

When first exploring Nix, we started with a prototype [supabase/nix-postgres](https://github.com/supabase/nix-postgres), which implemented the basics of our Postgres build with the majority of our supported extensions. Initial experiments showed that the nix cache significantly reduces our build times. The size of the reduction depends on how much of the cache is invalidated by the change being made. Broadly speaking, the cache reduces build times for common operations from roughly 40 minutes to between 1 and 5 minutes!

We have now added the [nix build in parallel with our Ansible/Packer build](https://github.com/supabase/postgres/pull/909) in the main `supabase/postgres` repository and are steadily reducing the differences between the two. Using Nix (and Nix Flakes) we created a package set, which now lives at [/nix](https://github.com/supabase/postgres/tree/develop/nix) and is coordinated with [flake.nix](https://github.com/supabase/postgres/blob/develop/flake.nix).

We are currently working on integrating our Nix packaged assets into our AMI build in a way that will allow our teams to continue to use packer and ansible to build and configure AWS AMI images, but sources postgres from our Nix build. We think that integrated approach will make it simpler for Supabase to adopt and leverage Nix. We’ll increase our internal documentation and education on the Nix aspects of the build pipeline. We’ll also be in a great position to use Nix community tooling to scan for vulnerabilities, versions, etc and create automation around those issues.

## What’s coming? [\#](https://supabase.com/blog/nix-postgres\#whats-coming)

The further we delve into the project, the more opportunities present themselves. Some of the planned features we’re excited about are:

- Slimmer Docker Images - We can generate low-profile docker images from the same Nix build using the amazing [nix2container](https://github.com/nlewo/nix2container) project, and push those images to our docker registry. This approach also saves computation, build time, and storage space.
- Reliable Upgrades and Migrations - Identifying and mitigating all the ways backups and upgrades can fail is a challenge. Early in the project we worked up a generic solution for testing migrations from any two versions of Supabase built with Nix using a [1 liner](https://github.com/supabase/postgres/blob/develop/nix/docs/migration-tests.md). That makes it trivially easy to add new cases to the test suite to improve coverage.
- Local builds - Given Nix’s isolated build environment, if it works in CI, it works locally! The ability to create fast builds locally should significantly reduce CI failures and improve development velocity.
- Cross platform builds - Our main build runs on Linux, but MacOS support is in the works and Windows can be supported with WSL
- Faster Component Upgrades - We can support a wide matrix of Postgres and extension versions. For each variation, we can build, test, and even deploy, without changing other variations of the bundle, allowing us to QA component upgrades more quickly.

Stay tuned for updates as we leverage the power of Nix to bring more robust and efficient solutions to our community!

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnix-postgres&text=Packaging%20Supabase%20with%20Nix)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnix-postgres&text=Packaging%20Supabase%20with%20Nix)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnix-postgres&t=Packaging%20Supabase%20with%20Nix)

[Last post\\
\\
**Exploring Support Tooling at Supabase: A Dive into SLA Buddy** \\
\\
25 April 2024](https://supabase.com/blog/exploring-support-tooling)

[Next post\\
\\
**Supabase Storage: now supports the S3 protocol** \\
\\
18 April 2024](https://supabase.com/blog/s3-compatible-storage)

[supabase-engineering](https://supabase.com/blog/tags/supabase-engineering)

On this page

- [What is Nix?](https://supabase.com/blog/nix-postgres#what-is-nix)
- [Powerful features like what?](https://supabase.com/blog/nix-postgres#powerful-features-like-what)
- [Current Builds](https://supabase.com/blog/nix-postgres#current-builds)
- [How’s it going?](https://supabase.com/blog/nix-postgres#hows-it-going)
- [What’s coming?](https://supabase.com/blog/nix-postgres#whats-coming)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnix-postgres&text=Packaging%20Supabase%20with%20Nix)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnix-postgres&text=Packaging%20Supabase%20with%20Nix)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnix-postgres&t=Packaging%20Supabase%20with%20Nix)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)