---
url: "https://supabase.com/blog/automatic-cli-login"
title: "Automatic CLI login"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Automatic CLI login

01 Dec 2023

•

4 minute read

[![Kamil Ogórek avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkamilogorek.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Kamil OgórekIntegrations Lead](https://twitter.com/kamilogorek)

![Automatic CLI login](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fautomatic-cli-login%2Fautomatic-cli-login-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Using the [Supabase CLI](https://supabase.com/docs/guides/cli) is the go-to method for many to interact with their Supabase projects. It enables easy local project development, working with the local database, managing migrations, and generating types, among other functionalities. However, some scenarios demand connecting to the real Supabase project, requiring a login. Until now, the login process involved typing `supabase login`, which prompted users to manually generate a token from [supabase.com/dashboard/account/tokens](https://supabase.com/dashboard/account/tokens) and paste it back into the terminal.

This method proved inconvenient and suboptimal for our users, especially for those recording courses or tutorial videos, as they repeatedly had to go through the whole process manually. We are committed to prioritizing Developer Experience (DX), so we decided to improve this.

But what if logging in were as simple as typing `supabase login` and, if you were already logged into your dashboard, everything happened automatically? This streamlined approach began with `1.114.0`.

## How does Automatic CLI login work exactly? [\#](https://supabase.com/blog/automatic-cli-login\#how-does-automatic-cli-login-work-exactly)

When you type `supabase login`, several things occur. First, a random UUID is generated to represent your unique login attempt. Next, a token name is created using your username, machine name, and the current timestamp. Most importantly, a pair of private/public P-256 elliptic curve Diffie-Hellman (ECDH) keys is generated. These keys remain valid only for the duration of the process; once you log in or cancel the CLI process, they become unusable.

Supabase CLI Automatic Login - YouTube

Supabase

54.4K subscribers

[Supabase CLI Automatic Login](https://www.youtube.com/watch?v=lNgsIITU3pc)

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

[Watch on YouTube](https://www.youtube.com/watch?v=lNgsIITU3pc "Watch on YouTube")

After gathering all this data, a unique URL is generated containing the session ID, token name, and your public key. The CLI then attempts to open this URL in your current environment's default browser. Once it opens, it verifies your authentication. If you're not authenticated, you're redirected to the login page, prompted to log into the dashboard, and upon successful authentication, redirected back to the originally requested page.

With your identity confirmed, the CLI sends the provided session data to our management API, requesting its magic.

The Management API generates a new access token for your account, creates its pair of ECDH keys, and encrypts the token using your public key and the server's private key. This encrypted token, alongside the server's public key, your session ID, and expiration date, is then stored in our database.

To send it back to your CLI it needs to be stored in a database.

## Securely exchanging the token using ECDH [\#](https://supabase.com/blog/automatic-cli-login\#securely-exchanging-the-token-using-ecdh)

At Supabase, we make every effort to avoid storing credentials such as access tokens in our database. However, this presents a challenge. To address it, we encrypt the generated token using an encryption key shared between your CLI and the management API. This is done using [Elliptic-Curve Diffie-Hellman](https://arstechnica.com/information-technology/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/) — a method of getting two parties to agree on a shared secret but only using public keys. To do this, a one-time P-256 public key is generated on each login and sent to the API, and likewise the API generates its own one-time public key. It then uses ECDH to compute a shared secret which is used to encrypt the generated access token and stored in the database. Since the private keys are not stored anywhere and are immediately thrown out, the CLI is the only one that will be able to decrypt the access token.

Meanwhile, the CLI continues its role in the process. It periodically polls our public API for the specific session ID it generated. Upon a successful poll, it extracts the encrypted token from the response, uses the server's public key, and this time, employing its private key (stored in RAM), decrypts the previously encrypted token, securely storing it in your operating system's vault.

Upon completion of this process, you're done! If you're already logged into the dashboard, it's as simple as a single command and hitting Enter to complete the entire login process.

## Conclusion [\#](https://supabase.com/blog/automatic-cli-login\#conclusion)

In this post, we dive into the new CLI automatic login, exploring its technical setup and security measures, including encryption. Of course, if you prefer not to automatically open the browser, provide a token manually, pass it from the environment, or change the default token name, you can achieve all of these using the provided flags. For details on what's possible, use `supabase login --help`.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-cli-login&text=Automatic%20CLI%20login)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-cli-login&text=Automatic%20CLI%20login)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-cli-login&t=Automatic%20CLI%20login)

[Last post\\
\\
**Supabase Launch Week X Hackathon** \\
\\
5 December 2023](https://supabase.com/blog/supabase-hackathon-lwx)

[Next post\\
\\
**GitHub OAuth in your Python Flask app** \\
\\
21 November 2023](https://supabase.com/blog/oauth2-login-python-flask-apps)

[CLI](https://supabase.com/blog/tags/CLI) [DX](https://supabase.com/blog/tags/DX)

On this page

- [How does Automatic CLI login work exactly?](https://supabase.com/blog/automatic-cli-login#how-does-automatic-cli-login-work-exactly)
- [Securely exchanging the token using ECDH](https://supabase.com/blog/automatic-cli-login#securely-exchanging-the-token-using-ecdh)
- [Conclusion](https://supabase.com/blog/automatic-cli-login#conclusion)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-cli-login&text=Automatic%20CLI%20login)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-cli-login&text=Automatic%20CLI%20login)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-cli-login&t=Automatic%20CLI%20login)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)