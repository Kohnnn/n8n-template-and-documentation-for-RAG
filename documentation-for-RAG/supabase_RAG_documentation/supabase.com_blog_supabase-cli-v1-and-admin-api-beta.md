---
url: "https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta"
title: "Supabase CLI v1 and Management API Beta"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase CLI v1 and Management API Beta

15 Aug 2022

•

5 minute read

[![Bobbie Soedirgo avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsoedirgo.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Bobbie SoedirgoEngineering](https://github.com/soedirgo)

[![Qiao Han avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsweatybridge.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Qiao HanEngineering](https://github.com/sweatybridge)

![Supabase CLI v1 and Management API Beta](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-cli%2Fthumbnail.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we are moving the Supabase CLI v1 out of beta. The Supabase CLI is capable of managing database migrations and generating TypeScript types. Follow these [install instructions](https://supabase.com/docs/guides/cli) to get started.

In addition, we are releasing a Management API (in beta). The Management API is a REST API that allows you to manage organizations, projects, Edge Functions, and more. You can read the [API docs](https://supabase.com/docs/reference/api) or interact with the Management API from the Supabase CLI v1.

(Note: The Management API was previously called the Admin API.)

Supabase Launch Week 5: Day 1 - Supabase CLI v1 and Admin API Beta - YouTube

Supabase

54.4K subscribers

[Supabase Launch Week 5: Day 1 - Supabase CLI v1 and Admin API Beta](https://www.youtube.com/watch?v=OpPOaJI_Z28)

Supabase

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

Full screen is unavailable. [Learn More](https://support.google.com/youtube/answer/6276924)

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

[Watch on YouTube](https://www.youtube.com/watch?v=OpPOaJI_Z28 "Watch on YouTube")

_Watch the CLI team announcing the new features._

## Manage organizations, projects, Edge Functions, and more [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#manage-organizations-projects-edge-functions-and-more)

If you've used [Supabase Edge Functions](https://supabase.com/blog/supabase-edge-functions#quickstart), you've used the Supabase CLI. We're extending it to let you manage organizations and projects.

`
supabase login
supabase orgs list
supabase projects create my-project --org-id cool-green-pqdr0qc --db-password ******** --region us-east-1
`

Once your new Supabase project is created, use the CLI to link it locally to begin development.

`
supabase link --project-ref <project-id>
`

View the [Supabase CLI docs](https://supabase.com/docs/reference/cli) for the full list of available commands.

## Schema migrations [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#schema-migrations)

You asked for more database migration support, and we listened. We've made improvements to manually-written migrations and auto generated schema diffs.

### Schema diff-ing [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#schema-diff-ing)

Previously we supported schema diff-ing using PgAdmin. We found that the tool did not account for default privileges when generating role grants. This leads to verbose statements when diff-ing complex schema changes.

To improve the usability of `db diff` command, we are introducing another tool, [migra](https://github.com/djrobstep/migra), via the `--use-migra` experimental flag. We found that `migra` runs faster and produces more concise DDL statements. While the generated scripts are [not perfect](https://supabase.com/blog/supabase-cli#migrations), we hope this tool helps you iterate quicker on your migration scripts. Over time (and with your feedback) we hope to improve schema-diffing to cover all edge-cases.

`
$ supabase db diff --use-migra --file file_name
# Creates a DDL script: supabase/migrations/<datetime_string>_file_name.sql
`

Running the above command diffs the `public` schema of your local development database against a fresh shadow database. You may specify other schema by passing in the `--schema` flag multiple times or as a comma separate list. More details in our [migration guide](https://supabase.com/docs/guides/cli/cicd-workflow#creating-a-new-migration).

In the long-term we hope to consolidate on a single diff-ing tool which is perfect, but diff-ing is hard so we would need your help and feedback to improve tooling.

### Manual migrations [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#manual-migrations)

You can test manual migrations locally without data loss using local branching. Run the following commands to clone your local database to a new branch.

`
supabase db branch new my_branch
supabase db branch switch my_branch
`

Now you can run any DDL statements from Studio UI's SQL Editor. To undo the changes, simply switch back and delete the new branch.

`
supabase db branch switch main
supabase db branch delete my_branch
`

## CI / CD [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#ci--cd)

Automating migrations and tests on your CI / CD pipeline gives developers more confidence that each PR contains a working migration script. CLI v1 focuses on both local and [GitHub Actions](https://github.com/supabase/setup-cli) support for the following workflows.

Test all migrations on a fresh local database:

`
supabase init
supabase start
`

Release schema changes to staging and production:

`
$ supabase link --project-ref $PROJECT_ID
$ supabase db push
`

We created an [example project](https://github.com/supabase/supabase-action-example) showing how to set up GitHub Actions to test and migrate with Supabase CLI v1.

## Type generation [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#type-generation)

You can now generate TypeScript types using the CLI:

`
# in a project set up with the CLI:
supabase gen types typescript --local
supabase gen types typescript --db-url $SUPABASE_DB_URL
`

Of course, the types aren't very useful on its own, you need some way to consume it. For that, stay tuned for tomorrow! 😉

## Management API [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#management-api)

The CLI is the first consumer of our new Management API. Over the next few weeks, we'll be adding the endpoints needed to programmatically manage your Supabase projects and organizations. This is ideal for CI/CD workflows and spinning up test environments.

Here's an example of deploying a new project from the command line (generate your access token from the [Supabase Dashboard](https://supabase.com/dashboard/account/tokens)).

`
curl 'https://api.supabase.com/v1/projects' \
  -H 'Authorization: Bearer <[your-access-token](https://supabase.com/dashboard/account/tokens)>' \
  -H "Content-Type: application/json" \
  -d '{"name": "my-project", "organization_id": "cool-green-pqdr0qc", "region": "us-east-1", "plan": "free", "db_pass": "********"}'
`

The response JSON will match the example below:

`
{
"id": "abcdefghijklmnopqrst",
"organization_id": "cool-green-pqdr0qc",
"name": "hello",
"region": "us-east-1",
"created_at": "2022-08-12T17:37:11.88819Z"
}
`

Check out the [API docs](https://supabase.com/docs/reference/api) to browse all the functionality added so far.

The new API also opens the door to a whole new suite of integrations, including Zapier, Terraform, Pulumi etc. We're looking forward to seeing how the dev community interacts with these new public endpoints. Try it out and let us know which functionality you'd like to see next.

## More Launch Week 5 [\#](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta\#more-launch-week-5)

- [Launch Week Page](https://supabase.com/launch-week)
- [Launch Week 5 Hackathon](https://supabase.com/blog/launch-week-5-hackathon)
- [Supabase Series B](https://supabase.com/blog/supabase-series-b)
- [Open Source at Supabase - Founders Fireside Chat](https://www.youtube.com/watch?v=4t_63HT3rZY)
- [Day 2 - supabase-js v2 Release Candidate](https://supabase.com/blog/supabase-js-v2)
- [Youtube Video - supabase-js v2 Release Candidate](https://www.youtube.com/watch?v=iqZlPtl_b-I)
- [Day 3 - Supabase is SOC2 compliant](https://supabase.com/blog/supabase-soc2)
- [Youtube video - Security Day](https://www.youtube.com/watch?v=6bGQotxisoY)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cli-v1-and-admin-api-beta&text=Supabase%20CLI%20v1%20and%20Management%20API%20Beta)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cli-v1-and-admin-api-beta&text=Supabase%20CLI%20v1%20and%20Management%20API%20Beta)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cli-v1-and-admin-api-beta&t=Supabase%20CLI%20v1%20and%20Management%20API%20Beta)

[Last post\\
\\
**supabase-js v2** \\
\\
16 August 2022](https://supabase.com/blog/supabase-js-v2)

[Next post\\
\\
**Supabase Series B** \\
\\
12 August 2022](https://supabase.com/blog/supabase-series-b)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Manage organizations, projects, Edge Functions, and more](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#manage-organizations-projects-edge-functions-and-more)
- [Schema migrations](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#schema-migrations)
  - [Schema diff-ing](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#schema-diff-ing)
  - [Manual migrations](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#manual-migrations)
- [CI / CD](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#ci--cd)
- [Type generation](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#type-generation)
- [Management API](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#management-api)
- [More Launch Week 5](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta#more-launch-week-5)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cli-v1-and-admin-api-beta&text=Supabase%20CLI%20v1%20and%20Management%20API%20Beta)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cli-v1-and-admin-api-beta&text=Supabase%20CLI%20v1%20and%20Management%20API%20Beta)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cli-v1-and-admin-api-beta&t=Supabase%20CLI%20v1%20and%20Management%20API%20Beta)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)