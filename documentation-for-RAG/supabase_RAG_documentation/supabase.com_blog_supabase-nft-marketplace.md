---
url: "https://supabase.com/blog/supabase-nft-marketplace"
title: "Supabase Launches NFT Marketplace"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Launches NFT Marketplace

01 Apr 2021

•

3 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Launches NFT Marketplace](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnft%2Fnft-3.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Crypto at Supabase [\#](https://supabase.com/blog/supabase-nft-marketplace\#crypto-at-supabase)

Most people don’t know this but the Supabase team has a long history of involvement in the NFT game. In 2018, [Copple](https://www.blockpunk.net/en/collection/paul-copplestone) and [Rory](https://www.blockpunk.net/en/collection/rory-wilding) were minted as NFTs on [Blockpunk.net](https://www.blockpunk.net/), an Ethereum based Anime-NFT platform that four Supabase core team members helped build. We also helped in the building of the world’s first tokenised anime premiere - [Vevara in Your Dream](https://www.animationmagazine.net/anime/first-tokenized-anime-film-vevara-in-your-dream-debuts/).

The team were also founding members of the [Guacchain Foundation](https://github.com/awalias/guacchain), an economic experiment in a deflationary-based monetary system, inspired by the fact that Avacados ripen faster when stored together.

NFTs are now capturing the imagination of speculators everywhere, but NFTs as they exist today have a major flaw. We call it the _Copy-Paste Problem_. The Copy-Paste problem is when a token contains a URL to an image hosted on the web, or even on IPFS; there is nothing stopping someone who does not own the token, from heading to that URL, and just downloading the image for themselves.

As our latest foray into NFTs we’re announcing [BuyMeth.com](https://buymeth.com/), (Meth = \[M\]isleading \[E\]ncrypted \[Th\]umbnails) an NFT marketplace that solves the copy-paste problem of NFTs today.

![Supabase NFT marketplace BuyMeth.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnft%2Fnft-1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### How does it work? [\#](https://supabase.com/blog/supabase-nft-marketplace\#how-does-it-work)

Each NFT stores a blurhash representation of a full image, but also a link to the full encrypted version of the image stored on IPFS. The full image is always encrypted with the key of the _current_ owner.

When a sale is initiated i.e. the seller accepts a buyers offer, Metamask re-encrypts the image with the public key of the buyer, and uploads it to IPFS, the url in the NFT is updated and the buyer assigned as the new owner. After the sale, a 1 week challenge period is initiated where the proceeds of the sale are kept in an escrow contract. The buyer can then decrypt the contents of the image, and can run an automated verification function to verify that the image received (when hashed) does indeed produce the publically available blurhash (or thumbnail). If it does not, then the buyer can submit a claim to the sales contract, along with a proof of the invalid file, and claim back the proceeds.

![Most popular NFTs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnft%2Fnft-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

As a way to dis-incentivise previous owners of the image to not reveal the original image, we bake in a royalty mechanism, whereby previous owners receive a fraction of the sale price each time, the artwork changes hands.

Despite the undeniable value of such a platform, this announcement is of course an April Fools joke. We are not launching a Supabase NFT platform; but we are [Launching a TON of other stuff this week](https://supabase.com/blog/launch-week).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&t=Supabase%20Launches%20NFT%20Marketplace)

[Last post\\
\\
**Workflows are coming to Supabase** \\
\\
2 April 2021](https://supabase.com/blog/supabase-workflows)

[Next post\\
\\
**Supabase CLI** \\
\\
31 March 2021](https://supabase.com/blog/supabase-cli)

[supabase](https://supabase.com/blog/tags/supabase) [nfts](https://supabase.com/blog/tags/nfts)

On this page

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&t=Supabase%20Launches%20NFT%20Marketplace)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)