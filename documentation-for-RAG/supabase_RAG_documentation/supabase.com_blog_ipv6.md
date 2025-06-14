---
url: "https://supabase.com/blog/ipv6"
title: "Brace yourself, IPv6 is coming"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Brace yourself, IPv6 is coming

12 Jan 2024

•

5 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Brace yourself, IPv6 is coming](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024%2Fipv6%2Fipv4-ipv6.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

On February 1st 2024, AWS will [start charging for IPv4 addresses](https://aws.amazon.com/blogs/aws/new-aws-public-ipv4-address-charge-public-ip-insights/). This will cost $0.005 per hour - around $4 month.

A more accurate title for this post would be “Brace yourself, IPv4 is leaving”, because I can't imagine many companies will pay to keep using the IPv4 address. While $4 is relatively small for an individual, my hypothesis is that AWS is a foundational layer to many infrastructure companies, like Supabase - we offer a full EC2 instance for every Postgres database, so this would add millions to our AWS bill.

Infrastructure companies on AWS have a few choices:

1. Pass on the cost to the customer.
2. Provide a workaround (for example, a proxy).
3. Only offer IPv6 and hope the world will catch up.

Let's explore the difficulties of `3`.

## IPv4 vs IPv6 [\#](https://supabase.com/blog/ipv6\#ipv4-vs-ipv6)

As a quick primer, an IPv4 looks like this: `93.184.216.34`. It is the “address” of a server, similar to a phone number - it tells your computer where to find something on the internet. The problem is there are only ~4.3 billion IPv4 addresses, and we're running out.

An IPv6 looks like this: `2607:f8b0:4006:819::200e` **.** It functions the same as an IPv4, except that there are 340 undecillion of them - that's more than the grains of sand on the planet (by many orders of magnitude). We won't run out any time soon.

IPv6 is clearly a _good_ thing, so what's the challenge? It mostly comes down to:

1. ISP support
2. Tooling support

## ISP support [\#](https://supabase.com/blog/ipv6\#isp-support)

The biggest challenge to global adoptions is ISP support. Does your Internet Service Provider [support IPv6](https://test-ipv6.com/)? Probably not.

When you type a website's domain name, it's translated into an IP address. Traditionally, these addresses have been IPv4:

`example.com` → `93.184.216.34`

These domain names will eventually be translated into IPv6:

`example.com` → `2607:f8b0:4006:819::200e`

After your ISP receives this address, it is responsible for routing all traffic to the correct destination. Unfortunately many ISPs simply aren't ready for this - they require [newer switches](https://networkengineering.stackexchange.com/questions/52847/how-to-check-if-switch-is-ipv6-fully-compatible), newer [software](https://serverfault.com/questions/470169/snat-in-ip6tables), and [interoperability](https://www.juniper.net/documentation/us/en/software/junos/is-is/topics/concept/ipv6-dual-stack-understanding.html) with IPv4. All of this costs money, and for the past 10 years this investment hasn't been worthwhile.

Here are some of the ways that you will be affected when domains/servers start resolving to IPv6 instead of IPv4, if your ISP doesn't support IPv6:

- Do you have a web server set up in AWS? You won't be able to SSH into it.
- Are you connected to a Supabase database from your local machine using the [direct connection](https://supabase.com/docs/guides/database/connecting-to-postgres#direct-connections)? You need to use the [connection pooler](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler) which will resolve as IPv4 instead (we will pay for IPv4 addresses on these).
- Are you connecting to any AWS server from Vercel? That will start [failing](https://github.com/orgs/vercel/discussions/47) soon if you don't set up an IPv4 address for that server.

## Tooling support [\#](https://supabase.com/blog/ipv6\#tooling-support)

A lot of developer tools simply aren't set up for IPv6 yet. We can use Supabase as an example - our data team needed to make the following changes to support IPv6 with their toolchain:

- Add IPv6 support to the VPC network.
- Add IPv6 support to our Airflow VM.
- Add IPv6 support to Docker and Compose.

These seem small, so to really convey what a PITA this can be, here were the steps for Docker:

1/ Update `/etc/docker/daemon.json`:

`
"ipv6": true,
"fixed-cidr-v6": "fd00:ffff::/80",
"ip6tables": true,
"experimental": true
`

2/ Restart the Docker service:

`
systemctl restart docker
`

3/ Create a temporary IPv6 net and test it:

`
docker network create --ipv6 --subnet fd00:ffff::/80 ip6net
docker run --rm -it --network ip6net busybox ping6 google.com -c3
`

4/ Check IPv6 iptables config (FORWARD)

`
ip6tables -L
`

5/ Add IPv6 network config to the compose config file `docker-compose.yaml`

`
# enable IPv6 to default network
networks:
default:
    enable_ipv6: true
    ipam:
      config:
        - subnet: fd00:c16a:601e::/80
          gateway: fd00:c16a:601e::1
`

6/ Check if it is working from a container

`
docker exec -it "airflow_airflow-worker_1" bash
curl -6 https://ifconfig.co/ip
`

That's … a lot more complicated than it should be for a tool as ubiquitous as Docker.

## Get ahead of the curve [\#](https://supabase.com/blog/ipv6\#get-ahead-of-the-curve)

I suspect that the next few months there is going to be a lot of talk about IPv6.

The fallout from AWS's changes will likely start slow. AWS will simply start charging their customers rather than revoking the IPv4 address. Once that happens, infrastructure companies will notice their bills increasing and start removing IPv4, or providing proxies. Providers might even require some downtime to implement [kernel-level changes](https://github.com/supabase/postgres/pull/753/files) to support IPv6.

If you want to ensure your company continues to run smoothly, start making as many changes as possible now before the start of February.

## Supabase support for IPv6 [\#](https://supabase.com/blog/ipv6\#supabase-support-for-ipv6)

If you are a Supabase customer, we have 3 simple solutions:

1. Switch your “direct” database connection to our new Supavisor database proxy. You can find these details in the [project connect page](https://supabase.com/dashboard/project/_?showConnect=true).
2. We will bring out a paid add-on for IPv4. This will be $4/m - we will simply pass on the AWS cost to you. Update: The add-on is now available on all paid plans.
3. We'll support you. We know that this period will be difficult for many. If you encounter any issues, simply reach out to us via [supabase.help](https://supabase.help/) and we will make sure your databases continue to run smoothly.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fipv6&text=Brace%20yourself%2C%20IPv6%20is%20coming)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fipv6&text=Brace%20yourself%2C%20IPv6%20is%20coming)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fipv6&t=Brace%20yourself%2C%20IPv6%20is%20coming)

[Last post\\
\\
**Using React Query with Next.js App Router and Supabase Cache Helpers** \\
\\
12 January 2024](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers)

[Next post\\
\\
**Elixir clustering using Postgres** \\
\\
9 January 2024](https://supabase.com/blog/elixir-clustering-using-postgres)

[aws](https://supabase.com/blog/tags/aws) [ipv6](https://supabase.com/blog/tags/ipv6) [networking](https://supabase.com/blog/tags/networking)

On this page

- [IPv4 vs IPv6](https://supabase.com/blog/ipv6#ipv4-vs-ipv6)
- [ISP support](https://supabase.com/blog/ipv6#isp-support)
- [Tooling support](https://supabase.com/blog/ipv6#tooling-support)
- [Get ahead of the curve](https://supabase.com/blog/ipv6#get-ahead-of-the-curve)
- [Supabase support for IPv6](https://supabase.com/blog/ipv6#supabase-support-for-ipv6)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fipv6&text=Brace%20yourself%2C%20IPv6%20is%20coming)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fipv6&text=Brace%20yourself%2C%20IPv6%20is%20coming)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fipv6&t=Brace%20yourself%2C%20IPv6%20is%20coming)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)