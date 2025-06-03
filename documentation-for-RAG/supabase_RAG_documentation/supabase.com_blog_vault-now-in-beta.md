---
url: "https://supabase.com/blog/vault-now-in-beta"
title: "Supabase Vault is now in Beta"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Vault is now in Beta

16 Dec 2022

•

8 minute read

[![Michel Pelletier avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmichelp.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Michel PelletierEngineering](https://github.com/michelp)

![Supabase Vault is now in Beta](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fvault%2Fog-vault.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

During our last Launch Week we [announced](https://supabase.com/blog/supabase-vault) Supabase Vault as our “one more thing”. Today we're releasing it progressively across the platform.

Vault is a new Postgres extension and accompanying Supabase UI that makes it safe and easy to store encrypted secrets and encrypt other stored data in your database. This foundation opens up a lot of possibilities for Postgres that go beyond what is available in a stock distribution. From a product perspective we're grouping various features under the “Vault banner”. Let's explore a few of these features.

❇️ UPDATE JUNE 2023 ❇️

Supabase Vault is now available on every Supabase project. [Check it out](https://supabase.com/dashboard/project/_/settings/vault/secrets)

## Secrets Management [\#](https://supabase.com/blog/vault-now-in-beta\#secrets-management)

Practically speaking, the Vault is a table of Secrets and Encryption Keys that are stored using [Authenticated Encryption](https://en.wikipedia.org/wiki/Authenticated_encryption) on disk, but available in decrypted form through a Postgres view so that the secrets can be used by applications from SQL. Because the secrets are stored encrypted and authenticated, any backups or replication streams also preserve this encryption in a way that can't be forged.

We've created a dashboard UI for the Vault that makes storing secrets easy. Click a button and type in your secret, optionally create a new key that is referenced by id (or use the existing default), and submit. Your secret is now stored on disk encrypted using the specified key id.

There are two main parts to the Vault UI, Secrets and Encryption Keys:

- **Secrets:** Use the Vault to store Secrets - everything from Environment Variables to API Keys. You can use these Secrets anywhere in your database: Postgres [Functions](https://supabase.com/docs/guides/database/functions), Triggers, and [Webhooks](https://supabase.com/docs/guides/database/webhooks). From a SQL perspective, accessing secrets is as easy as querying a table (or in this case, a view). The underlying secrets tables will be stored in encrypted form.
- **Encryption Keys:** encryption keys are used to encrypt data inside your database. Fun fact: the Secrets you store in the Vault are encrypted with an Encryption Key which we set up by default and is not accessible to SQL or stored in your database alongside the same data it is used to encrypt. You can create different Encryption Keys for different purposes, for example: one for encrypting user-data, and another for application-data.

## Transparent Column Encryption (TCE) [\#](https://supabase.com/blog/vault-now-in-beta\#transparent-column-encryption-tce)

Our recent [blog post](https://supabase.com/blog/transparent-column-encryption-with-postgres) describes TCE in-depth. TCE is one of the safest ways to encrypt your data so that it doesn't leak into logs and backups, as well as providing your users with row-level authenticated encryption. TCE is the foundational feature of the Vault, but you can use it on your own tables if you choose to if the Vault isn't sufficient for your needs, for example if you have multiple tables that you wish to have encrypted columns. Any Postgres value that can be cast to `text` or `bytea` can use TCE to encrypt the data that is stored to disk.

### Encrypting columns [\#](https://supabase.com/blog/vault-now-in-beta\#encrypting-columns)

In the “New Column” flow on the Dashboard, you can select that a `text` or `bytea` column is encrypted, and select an existing key id or create a new one. This is functionally identical to the Vault above, but you can apply it to any of your existing tables. In a sense the Vault is a pre-created table and UI for you to get started quickly storing secrets, and to be a centralized point for “global” secrets management, but your not stuck with just that, you can encrypt multiple columns in multiple tables, how you want to store your secret data can be entirely up to you.

![Encrypting columns](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fvault%2Fvault-encrypting-columns.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Once you've setup an encrypted column, just insert data into the table like you would any other table. If you put in an email address for example, you will see that what is stored is not an email at all, but an encrypted value.

![Encrypted data](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fvault%2Fvault-encrypted-data.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Decrypted data can be accessed by a special view that is automatically created whenever you create an encrypted column on a table. This view decrypts the data row-by-row as you access it. By default this view is called `decrypted_<your-table-name>`, so in the example provided, the decryption view for the `profiles` table is `decrypted_profiles`. In addition to the existing `emails` column, there is a new column in the view called `decrypted_emails` that contains the decrypted email value. It's that simple!

![Decrypted data](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fvault%2Fvault-decrypted-data.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Deep Dive on How The Vault works [\#](https://supabase.com/blog/vault-now-in-beta\#deep-dive-on-how-the-vault-works)

Encrypted Columns in PostgreSQL - Secrets Management with Supabase Vault - YouTube

Supabase

54.4K subscribers

[Encrypted Columns in PostgreSQL - Secrets Management with Supabase Vault](https://www.youtube.com/watch?v=QHLPNDrdN2w)

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

[Watch on YouTube](https://www.youtube.com/watch?v=QHLPNDrdN2w "Watch on YouTube")

As we mentioned, the Vault uses pgsodium's Transparent Column Encryption (TCE) to store secrets in an authenticated encrypted form. There are some details around that you may be curious about, what does authenticated mean, and where are encryption keys store? This section explains those details.

The first important feature of TCE is that it uses an [Authenticated Encryption with Associated Data](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data_(AEAD)) encryption algorithm based on libsodium. “Authenticated Encryption” means that in addition to the data being encrypted, it is also “signed” so that it cannot be forged, the decryption function verifies that the signature is valid **before decrypting the value**. “Associated Data” means that in addition to signing the secret, you can include any other columns in your row in the signature computation, “associating” those columns with the secret. This doesn't encrypt those other columns, but it does ensure that **they are authentic** and cannot be forged because they are included in the secret's signature. So you know when you restore your database dumps, not only are the secrets safe, but also the “associated” columns are also authentic and unforged.

Another important feature of pgsodium is that the encryption keys are never stored in the database alongside the encrypted data, instead, only a **Key ID** is stored, which refers to a key that is only accessible outside of SQL. Even if an attacker can capture a dump of your entire database, they will see only encrypted data and key ids, **never the raw key itself**. This is an important safety precaution, there would be no point in storing the encryption key in the database alongside the encrypted data, this would be like locking your front door but leaving the key in the lock! Storing the key outside the database fixes this issue.

You might be wondering, ok then where are the keys stored? Supabase creates and manages the root keys from which all key ids are derived in our internal customer backend systems. We keep this key safe and separate from your data, and provide an alternate dashboard endpoint for accessing the key if you want to decrypt your data outside of Supabase.

## Future possibilities [\#](https://supabase.com/blog/vault-now-in-beta\#future-possibilities)

Privacy is becoming one of the most important features in a modern product. Supabase's embrace of the pgsodium extension aims to make this simple. Some of the possibilities we are looking into are:

- **End-to-end encryption**: give your users the ability to encrypt their personal data so even you, the developer cannot access it, using the libsodium [encrypted streams](https://doc.libsodium.org/secret-key_cryptography/secretstream) API that is exposed by pgsodium. After exchanging keys, parties can stream unlimited amounts of data from peer to peer without being intercepted by any party in between, including Supabase.
- **Group encryption**: have you ever joined a group on Whatsapp and been frustrated that you can't read the previous messages? That's because group encryption is hard. We hope to make that easier using new algorithms like [signcryption](https://github.com/jedisct1/libsodium-signcryption) to support multi-party encrypted messages that can be easily encoded into a token format and use to support streaming encryption keys.
- **Public Key Management:** Public Key Encryption can be hard, but pgsodium makes it easier by exposing all of the public key encryption functions that are supported by libsodium. Making and distributing key pairs is now easy, no need to run arcane GPG scripts or mess with SSL libraries. libsodium contains state of the art public key encryption, and by extension so does pgsodium. These features are available now on the Supabase platform and offer a lot of possibilities to unshackle developers from other confusing and inadequate solutions available today.

### Using the Vault [\#](https://supabase.com/blog/vault-now-in-beta\#using-the-vault)

To learn how to use Supabase Vault, check out the [docs](https://supabase.com/docs/guides/database/vault). Supabase Vault is now available on all [Supabase projects](https://supabase.com/dashboard/project/_/settings/vault/secrets) (some projects will have to enable via request).

## More Launch Week 6 [\#](https://supabase.com/blog/vault-now-in-beta\#more-launch-week-6)

- [Day 1: New Supabase Docs, built with Next.js](https://supabase.com/blog/new-supabase-docs-built-with-nextjs)
- [Day 2: Supabase Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/storage-image-resizing-smart-cdn)
- [Day 3: Multi-factor Authentication via Row Level Security Enforcement](https://supabase.com/blog/mfa-auth-via-rls)
- [Day 4: Supabase Wrappers, a Postgres FDW framework written in Rust](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)
- [Community Day](https://supabase.com/blog/launch-week-6-community-day)
- [Point in Time Recovery is now available](https://supabase.com/blog/postgres-point-in-time-recovery)
- [Custom Domain Names are now available](https://supabase.com/blog/custom-domain-names)
- [Wrap Up: everything we shipped](https://supabase.com/blog/launch-week-6-wrap-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvault-now-in-beta&text=Supabase%20Vault%20is%20now%20in%20Beta)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvault-now-in-beta&text=Supabase%20Vault%20is%20now%20in%20Beta)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvault-now-in-beta&t=Supabase%20Vault%20is%20now%20in%20Beta)

[Last post\\
\\
**PostgREST 11 pre-release** \\
\\
16 December 2022](https://supabase.com/blog/postgrest-11-prerelease)

[Next post\\
\\
**Supabase Wrappers, a Postgres FDW framework written in Rust** \\
\\
15 December 2022](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)

[launch-week](https://supabase.com/blog/tags/launch-week) [postgres](https://supabase.com/blog/tags/postgres) [encryption](https://supabase.com/blog/tags/encryption) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Secrets Management](https://supabase.com/blog/vault-now-in-beta#secrets-management)
- [Transparent Column Encryption (TCE)](https://supabase.com/blog/vault-now-in-beta#transparent-column-encryption-tce)
  - [Encrypting columns](https://supabase.com/blog/vault-now-in-beta#encrypting-columns)
- [Deep Dive on How The Vault works](https://supabase.com/blog/vault-now-in-beta#deep-dive-on-how-the-vault-works)
- [Future possibilities](https://supabase.com/blog/vault-now-in-beta#future-possibilities)
  - [Using the Vault](https://supabase.com/blog/vault-now-in-beta#using-the-vault)
- [More Launch Week 6](https://supabase.com/blog/vault-now-in-beta#more-launch-week-6)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvault-now-in-beta&text=Supabase%20Vault%20is%20now%20in%20Beta)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvault-now-in-beta&text=Supabase%20Vault%20is%20now%20in%20Beta)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvault-now-in-beta&t=Supabase%20Vault%20is%20now%20in%20Beta)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)