---
url: "https://supabase.com/blog/supabase-soc2-hipaa"
title: "Supabase is now HIPAA and SOC2 Type 2 compliant"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase is now HIPAA and SOC2 Type 2 compliant

11 Aug 2023

•

5 minute read

[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)

![Supabase is now HIPAA and SOC2 Type 2 compliant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-5%2Fthumb-day5-compliance.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

While we weren’t [planning](https://news.ycombinator.com/item?id=35526018) to do anything official for this announcement, [the customer is always right](https://news.ycombinator.com/item?id=35555756).

Supabase is now officially SOC2 Type 2 and HIPAA compliant.

That’s all you need to know. The rest of this blog post will give you some background and what to expect if you’re planning to go through the same process.

## SOC2 [\#](https://supabase.com/blog/supabase-soc2-hipaa\#soc2)

We previously [discussed](https://supabase.com/blog/supabase-soc2) the process the SOC2 Type 1. To recap,

1. Type 1 certification verifies adherence to the guidelines at a specific _point in time_.
2. Type 2 certification verifies compliance over a _period of time_.

We received our Type 2 certification on May 22nd of this year and we plan to conduct annual Type 2 audits to ensure adherence to SOC2 guidelines.

We used the same auditor for the Type 2 certification and knew mostly what to expect. Some of our internal processes needed to change to make it easier to the evidence for our auditor. Examples of the kind of requests our auditor would ask for:

- List of all incidents which happened in a given time period. The postmortem for a few incidents from that list that the auditor chooses.
- List of all access requests in a given time period.
- List of vulnerabilities and when they were fixed
- List of Data deletion requests and evidence that a particular request was actioned on within our SLA.

Some of these were readily available in [Vanta](https://www.vanta.com/), our compliance monitoring tool. For others, we had to develop new processes to ensure that this information was all readily available. The Type 2 audit involves gathering a lot more evidence than the Type 1 audit. If we didn’t have proper systems and process in place before the audit, it would have been painful during evidence collection.

## HIPAA [\#](https://supabase.com/blog/supabase-soc2-hipaa\#hipaa)

Health Insurance Portability and Accountability Act (HIPAA) is a US law that sets national standards for protecting individuals' medical records and personal health information. Companies building applications with sensitive healthcare data must comply with HIPAA to ensure the security and privacy of patients' information.

A couple of definitions before go further. A **covered entity** refers to healthcare providers, health plans, and health insurance companies. **Business associates** are entities that perform certain functions with protected health information (PHI) on behalf of a covered entity. Both Business Associates and Covered entities are covered (pun intended) under HIPAA. Supabase is a business associate and our customers handling PHI can either be covered entities or other business associates.

We receive many requests from users who want to build healthcare apps on top of Supabase. Since you can [self-host Supabase](https://supabase.com/docs/guides/self-hosting), we often [encourage](https://github.com/orgs/supabase/discussions/1219) these users to do so. Starting today, these users have the option to use our hosted platform too with the HIPAA add-on 🎉.

### Going from SOC2 to HIPAA [\#](https://supabase.com/blog/supabase-soc2-hipaa\#going-from-soc2-to-hipaa)

![soc2 to HIPAA](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-5%2Fsoc2-to-hipaa.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Going from zero to a SOC2 certification was much harder, than going from SOC2 to HIPAA.

We used the same auditor to streamline the process. Many of the controls required for HIPAA compliance could be mapped to the testing they had already done for SOC2. Additional evidence for encryption, audit logs, business continuity and disaster recovery exercises was unnecessary since the auditor already had access to it. And some of the HIPAA checks such as Facility Access Controls were not applicable to us since [we are a remote company](https://supabase.com/blog/why-supabase-remote).

We also had to sign a Business Associate Agreement (BAA) with all of our vendors who would have access to PHI, such as AWS, and ensure that we follow their terms listed in the agreements. For example, when using AWS to store PHI, we could only use their [HIPAA Eligible Services](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/). There were similar requirements from the other vendors we use and to ensure that we were complying with all their requirements.

Similarly when you sign a BAA with us, you have some responsibilities you agree to when using Supabase to store PHI. These are documented in our [shared responsibility doc](https://supabase.com/docs/guides/platform/shared-responsibility-model#managing-healthcare-data).

We made a significant change to our incident management process for HIPAA. The [HIPAA Breach Notification](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) rules have strict requirements for handling breaches. For instance, business associates are required to notify the covered entity within 60 days of a breach. This also required us to appoint a HIPAA Security officer who would be responsible for reviewing any breach for PHI disclosure and communicating it’s impact to the Covered Entity.

![Data Breach Declaration](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-5%2Fdata-breach-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The not-so-fun but important stuff included updating a bunch of our policies to cover HIPAA requirements such as enforcing automatic log-offs as part of our workstation security policy. Shopping for a good Technology Errors and Omissions Insurance plan was another boring but important thing we had to finalize in the off-chance that we get hacked despite all our measures. [HIPAA fines](https://www.strongdm.com/blog/hipaa-violation-penalties) are no joke, you could rake up to 1.9 million dollars per violation per calendar year depending the severity of the breach!

## Build Healthcare Apps on Supabase [\#](https://supabase.com/blog/supabase-soc2-hipaa\#build-healthcare-apps-on-supabase)

If you want to start developing healthcare apps on Supabase, reach out to our team [here](https://forms.supabase.com/hipaa2) to sign our BAA. We are excited to see what you build!

## More Launch Week 8 [\#](https://supabase.com/blog/supabase-soc2-hipaa\#more-launch-week-8)

- [Supabase Local Dev: migrations, branching, and observability](https://supabase.com/blog/supabase-local-dev)
- [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
- [Launch Week 8](https://supabase.com/launch-week)
- [Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber)
- [Why we'll stay remote](https://supabase.com/blog/why-supabase-remote)
- [Postgres Language Server](https://github.com/supabase/postgres_lsp)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2-hipaa&text=Supabase%20is%20now%20HIPAA%20and%20SOC2%20Type%202%20compliant)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2-hipaa&text=Supabase%20is%20now%20HIPAA%20and%20SOC2%20Type%202%20compliant)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2-hipaa&t=Supabase%20is%20now%20HIPAA%20and%20SOC2%20Type%202%20compliant)

[Last post\\
\\
**Launch Week 8 Community Highlights** \\
\\
11 August 2023](https://supabase.com/blog/launch-week-8-community-highlights)

[Next post\\
\\
**Supavisor: Scaling Postgres to 1 Million Connections** \\
\\
11 August 2023](https://supabase.com/blog/supavisor-1-million)

[launch-week](https://supabase.com/blog/tags/launch-week) [security](https://supabase.com/blog/tags/security)

On this page

- [SOC2](https://supabase.com/blog/supabase-soc2-hipaa#soc2)
- [HIPAA](https://supabase.com/blog/supabase-soc2-hipaa#hipaa)
  - [Going from SOC2 to HIPAA](https://supabase.com/blog/supabase-soc2-hipaa#going-from-soc2-to-hipaa)
- [Build Healthcare Apps on Supabase](https://supabase.com/blog/supabase-soc2-hipaa#build-healthcare-apps-on-supabase)
- [More Launch Week 8](https://supabase.com/blog/supabase-soc2-hipaa#more-launch-week-8)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2-hipaa&text=Supabase%20is%20now%20HIPAA%20and%20SOC2%20Type%202%20compliant)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2-hipaa&text=Supabase%20is%20now%20HIPAA%20and%20SOC2%20Type%202%20compliant)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2-hipaa&t=Supabase%20is%20now%20HIPAA%20and%20SOC2%20Type%202%20compliant)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)