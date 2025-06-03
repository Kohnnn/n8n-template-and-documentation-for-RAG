---
url: "https://supabase.com/blog/supabase-storage"
title: "Storage is now available in Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Storage is now available in Supabase

30 Mar 2021

•

9 minute read

[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)

![Storage is now available in Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Fph-1.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

🆕 Storage has undergone significant enhancements with two major releases since its initial launch. Here is what is new:

- [Supabase Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/storage-image-resizing-smart-cdn)
- [Supabase Storage v3: Resumable Uploads with support for 50GB files](https://supabase.com/blog/storage-v3-resumable-uploads)

Today, we are launching one of most requested features - [Storage!](https://supabase.com/storage) When you sign up for Supabase, you get a Postgres database with realtime subscriptions, user management, auto-generated APIs and now a scalable object store. These services integrate very well with each other and you don't need to sign up for yet another service just for your storage requirements.

As with anything that we build in Supabase, Storage is fast, secure and scalable. You can use it to store terabytes of Machine Learning training data, your e-commerce product gallery or just your growing collection of JPEGs featuring cats playing synths in space.

This post outlines our design decisions while building Storage, and we'll show you how to use it in your own applications.

## Architecture [\#](https://supabase.com/blog/supabase-storage\#architecture)

There are three key components to Supabase Storage:

- Backend (where the objects are actually stored).
- Middleware (access and permissions). This consists of an API Server and Postgres.
- Frontend (a nice UI).

The Storage API server sits behind Kong, an API Gateway. It talks to different storage backends like S3, Backblaze, etc to retrieve and store objects.

Object metadata and security rules are stored in your Postgres database.

We have built a powerful file explorer right into the dashboard, and using our Client libraries you can integrate Storage into your applications.

![Storage Infrastructure](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Finfra.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Frontend [\#](https://supabase.com/blog/supabase-storage\#frontend)

We set out to build the most usable front-end for storing content. Using Lists to display file hierarchies is a poor experience for exploring files - the most common use-case of a shared File system.

As avid Mac users, we've defaulted to using the column-based explorer in Finder as it allow us to quickly drill into nested folders and provides a clear birds eye view of file hierarchies at the same time.

We put in a lot of effort to make sure that the dashboard is fast and easy to navigate with our miller-based column view, allowing you to get to deeply nested folders quickly. If you're a fan of List Views though, don't worry! We have that option available too. The choice is yours.

![Frontend views](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Fph-5.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Our File Browser also has a rich preview for a wide set of file types including images, audio, and videos.

![Frontend preview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Fph-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

And if you already know the location of a file but want to save a few clicks, you can paste the path into the location bar and navigate to it directly.

![Frontend navigation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Fph-4.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Designing the storage middleware [\#](https://supabase.com/blog/supabase-storage\#designing-the-storage-middleware)

We focused on performance, security and interoperability with the rest of the Supabase ecosystem.

### Integration with the Supabase ecosystem [\#](https://supabase.com/blog/supabase-storage\#integration-with-the-supabase-ecosystem)

Supabase is a [collection of open source tools](https://supabase.com/docs#how-it-works) which integrate very well with each other. We evaluated open source object storage servers like [Ceph](https://ceph.io/), [Swift](https://www.openstack.org/software/releases/ocata/components/swift), [Minio](https://min.io/) and [Zenko](https://github.com/scality/Zenko) but none of these tools were a good fit for our existing ecosystem.

**Postgres Compatibility**

Each of these open source tools are amazing, but they all had a major drawback - we couldn't use Postgres as the server's datastore. If you haven't noticed yet, our team likes Postgres a lot 😉.

For example, Minio [uses etcd](https://docs.min.io/docs/minio-multi-user-quickstart-guide.html) (when used in multi-user gateway mode) and Zenko [requires mongodb and Kafka.](https://zenko.readthedocs.io/en/latest/operation/Architecture/index.html) Every project on Supabase is a dedicated Postgres database, so leveraging it for object and user metadata is more efficient, reducing the number of dependencies for anyone using the Supabase ecosystem of tools.

**Smaller footprint**

We are using managed services like [S3](https://aws.amazon.com/s3/), [Wasabi](https://wasabi.com/) and [Backblaze](https://www.backblaze.com/) for our storage backend. We won't be managing our own hard disks and storage capacity, and so we don't require a lot of features offered by existing tools. For example, a large part of Minio's codebase is to offer erasure encoding and bitrot protection, automatically making use of new disks attached to the cluster.

**Integration with Supabase Auth**

Existing tools do not play well with our authentication system. For example, Minio is bundled with its own [auth system](https://docs.min.io/docs/minio-admin-complete-guide.html#user) and there is no easy way to map Minio users to [Supabase users](https://supabase.com/docs/guides/auth).

In the end, we opted to build our own [Storage API server](https://github.com/supabase/storage-api).

## Security [\#](https://supabase.com/blog/supabase-storage\#security)

### Authentication [\#](https://supabase.com/blog/supabase-storage\#authentication)

Our storage service sits behind [Kong](https://github.com/kong/kong) along with other services like [PostgREST](https://github.com/PostgREST/postgrest) and [Realtime](https://github.com/supabase/realtime). This allows us to reuse our existing Authentication system - any requests with a valid API key are authenticated and passed to the storage API.

### Authorization [\#](https://supabase.com/blog/supabase-storage\#authorization)

For Authorization, we wanted to avoid creating a new DSL like Firebase. Instead, we created one where you can write policies in the One True Language - SQL!

![One True Language](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Ftrue-language.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

To do this, we leverage Postgres' Row Level Security. We create a table for `buckets` and `objects` inside each Supabase project. These tables are namespaced in a separate schema called `storage`.

The idea is simple - if a user is able to `select` from the `objects` table, they can retrieve the object too. Using Postgres' Row Level Security, you can define fine-grained Policies to determine access levels for different users.

When a user makes a request for a file, the API detects the user in the `Authorization` header and tries to `select` from the `objects` table. If a valid row is returned, the Storage API pipes the object back from S3. Similarly if the user is able to delete the row from the objects table, they can delete the object from the storage backend too.

For example, if you want to give "read" access to a bucket called `avatars` you would use this policy:

`
create policy "Read access for avatars."
on storage.objects for select using (
	bucket_id = 'avatars'
);
`

Extending this example, if you want to give access to a subfolder only (in this case called `public`):

`
create policy "Read access for public avatars."
on storage.objects for select using (
	bucket_id = 'avatars'
	and (storage.foldername(name))[1] = 'public'
);
`

We have created helper functions like `foldername()`, `filename()` and `extension()` in the storage schema to make Policies even simpler.

This system integrates with our [User Management system](https://supabase.com/docs/guides/auth). Here is an example policy which gives access to a particular file to a Supabase user:

`
create policy crud_uid_file
on storage.objects for all using (
	bucket_id = 'avatars'
	and name = 'folder/only_uid.jpg'
	and (select auth.uid()) = 'd8c7bce9-cfeb-497b-bd61-e66ce2cbdaa2'
);
`

Using the power of Postgres' Row Level Security, you can create pretty much any policy imaginable.

### Performance [\#](https://supabase.com/blog/supabase-storage\#performance)

The storage server is built with [Fastify](https://www.fastify.io/) and Typescript. Fastify is one of the [fastest](https://www.fastify.io/benchmarks/) Node frameworks and our initial benchmark results look very promising.

We use Node streams everywhere. Objects are uploaded directly to S3 with minimal in-memory buffering. This minimizes RAM consumption even while uploading huge objects. The code does become a bit more complicated when using streams. For example, you can't figure out the size of the object being uploaded before streaming it to S3. But we believe this tradeoff is worth it.

Postgres is another hidden gem for our storage performance. For example, what if you had a bucket with thousands of objects, and you needed to find all objects which a user has access to? Without Postgres, you would retrieve all objects from that folder, evaluate each policy in the storage middleware and only return the objects which the user has access to. But we can avoid this completely with Postgres! We use Postgres to evaluate all the polices, and the storage middleware just returns the objects which the user has access to.

Supabase Storage has some opinionated defaults with respect to caching. Objects retrieved from S3 typically do not have a `Cache-Control` header. This isn't optimal for a Storage system since browsers don't cache objects completely without this header. Objects retrieved from Supabase Storage by default have a Cache-Control header of 1 hour. Of course, you can override this behaviour by specifying a different cache time when creating the object.

## Storage Backend [\#](https://supabase.com/blog/supabase-storage\#storage-backend)

File objects are stored in an S3 bucket within the same region as your Supabase project. S3 has a high durability of 99.999999999% and is scalable as an object store.

While we started with S3, other storage backends like Wasabi, Backblaze and Openstack Swift expose an S3 compatible API. It will be simple to add more S3 compatible storage options in the future.

We have intentionally kept the API surface for the storage backend very small, in case the community also wants to add storage options which don't support the S3 API.

### Client libraries [\#](https://supabase.com/blog/supabase-storage\#client-libraries)

You may be itching to get started tinkering around with our new Supabase storage - we have an example app prepared for you right [here](https://github.com/supabase/supabase-js/tree/master/example/next-storage) which simulates a simple context of setting an avatar image for a user. This will help you to get a high level overview of how to use your project's storage with our client library. For greater detail, refer to our storage API documentation [here](https://supabase.com/docs/reference/javascript/storage-createbucket).

![Example app 1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Fph-7.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Example app 2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Fph-6.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## What's next [\#](https://supabase.com/blog/supabase-storage\#whats-next)

- We currently support S3 and will be adding more storage backends. Vote for the storage backends you would like to see us implement [here](https://github.com/supabase/supabase/discussions/982).
- We will integrate our storage service with a Content Delivery Network. With a CDN, objects are cached on a global network. This leads to faster access times for your users around the world. \*\*SHIPPED: [Supabase Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/storage-image-resizing-smart-cdn#smart-cdn)
- We are working on transformations like resizing of images and automatic optimization of different media types. This makes it easy to embed Supabase objects directly in your websites and mobile applications without additional processing. \*\*SHIPPED: [Supabase Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/storage-image-resizing-smart-cdn#image-resizing)
- A better editor to make authoring policies easier and less error prone.
- Reach out to us if you would like to help out with adding storage support in one of the [community maintained client libraries](https://supabase.com/docs/reference/javascript/installing).

Take it for a spin on our [dashboard](https://supabase.com/dashboard/) and let us know what you think!

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-storage&text=Storage%20is%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-storage&text=Storage%20is%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-storage&t=Storage%20is%20now%20available%20in%20Supabase)

[Last post\\
\\
**Supabase CLI** \\
\\
31 March 2021](https://supabase.com/blog/supabase-cli)

[Next post\\
\\
**Supabase Beta Pricing** \\
\\
29 March 2021](https://supabase.com/blog/pricing)

[supabase](https://supabase.com/blog/tags/supabase) [storage](https://supabase.com/blog/tags/storage)

On this page

- [Architecture](https://supabase.com/blog/supabase-storage#architecture)
- [Frontend](https://supabase.com/blog/supabase-storage#frontend)
- [Designing the storage middleware](https://supabase.com/blog/supabase-storage#designing-the-storage-middleware)
- [Security](https://supabase.com/blog/supabase-storage#security)
- [Storage Backend](https://supabase.com/blog/supabase-storage#storage-backend)
- [What's next](https://supabase.com/blog/supabase-storage#whats-next)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-storage&text=Storage%20is%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-storage&text=Storage%20is%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-storage&t=Storage%20is%20now%20available%20in%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)