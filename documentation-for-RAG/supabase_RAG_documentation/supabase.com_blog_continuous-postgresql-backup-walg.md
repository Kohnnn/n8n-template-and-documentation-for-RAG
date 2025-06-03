---
url: "https://supabase.com/blog/continuous-postgresql-backup-walg"
title: "Continuous PostgreSQL Backups using WAL-G"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Continuous PostgreSQL Backups using WAL-G

02 Aug 2020

•

6 minute read

[![Angelico de los Reyes avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdragarcia.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Angelico de los ReyesEngineering](https://github.com/dragarcia)

Have you ever wanted to restore your database's state to a particular moment in time? This post explains how, using WAL-G.

## Introduction [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#introduction)

[WAL-G](https://github.com/wal-g/wal-g) is an [open-source continuous archiving tool](https://www.citusdata.com/blog/introducing-wal-g-faster-restores-for-postgres/) used to easily set up and recover from [physical backups](https://supabase.com/blog/postgresql-physical-logical-backups) in Postgres. It mainly handles the storage and retrieval of physical backups and WAL archives to and from a chosen cloud storage provider. In this post, we will walk you through on how to effortlessly set up WAL-G for your database as well as guide you on what to do if and when disaster strikes.

## Prerequisites [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#prerequisites)

For this tutorial, we will be using two instances running Postgres databases on [Ubuntu 18.04](https://releases.ubuntu.com/18.04/). One instance will act as your main database, the other is your recovery database. If you’re using another operating system some file paths may vary.

### Installations [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#installations)

Make sure the below packages are installed in your instances. Alternatively, you can spin up the [latest version](https://github.com/supabase/postgres/releases/tag/v0.13.0) of [Supabase Postgres](https://github.com/supabase/postgres) which would already have everything configured and installed, along with other [goodies](https://github.com/supabase/postgres#features). It is readily available in either the [AWS](https://aws.amazon.com/marketplace/pp/B08915TCJ2?qid=1595854723755&sr=0-1&ref_=srh_res_product_title) or [Digital Ocean](https://marketplace.digitalocean.com/apps/supabase-postgres) marketplaces and only takes [a few minutes](https://supabase.com/docs/postgres/postgres-intro) to get running.

#### Postgres 12 [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#postgres-12)

A quick installation guide can be found [here](https://www.postgresql.org/download/linux/ubuntu/).

#### envdir [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#envdir)

[envdir](http://manpages.ubuntu.com/manpages/bionic/man8/envdir.8.html) allows us to run other programs with a modified environment based on the files in the provided directory. This can be installed through the [daemontools](https://cr.yp.to/daemontools.html) package:

`
$ sudo apt-get install -y daemontools
`

#### WAL-G [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#wal-g)

`
$ wget https://github.com/wal-g/wal-g/releases/download/v0.2.15/wal-g.linux-amd64.tar.gz
$ tar -zxvf wal-g.linux-amd64.tar.gz
$ mv wal-g /usr/local/bin/
`

### AWS credentials and resources [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#aws-credentials-and-resources)

When storing backups, WAL-G has numerous [cloud storage provider options](https://github.com/wal-g/wal-g#configuration) for us to choose from. For this tutorial, we will be using AWS. Have the following prepared:

- AWS Access & Secret keys.
- An S3 bucket.

## Setting it up [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#setting-it-up)

### 1\. Configure environment variables [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#1-configure-environment-variables)

The directory `/etc/wal-g.d/env` is created and contains files that stores environment variables. It would later be used in WAL-G commands via envdir.

`
$ umask u=rwx,g=rx,o=
$ mkdir -p /etc/wal-g.d/env
$ echo 'secret-key-content' > /etc/wal-g.d/env/AWS_SECRET_ACCESS_KEY
$ echo 'access-key' > /etc/wal-g.d/env/AWS_ACCESS_KEY_ID
$ echo 's3://backup-bucket/project-directory' > /etc/wal-g.d/env/WALG_S3_PREFIX
$ echo 'db password' > /etc/wal-g.d/env/PGPASSWORD
$ chown -R root:postgres /etc/wal-g.d
`

### 2\. Enable WAL archiving [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#2-enable-wal-archiving)

Here, we enable [WAL archiving](https://www.postgresql.org/docs/12/continuous-archiving.html) and instruct Postgres to store the archives in the specified S3 bucket via WAL-G.

`
$ echo "archive_mode = yes" >> /etc/postgresql/12/main/postgresql.conf
$ echo "archive_command = 'envdir /etc/wal-g.d/env /usr/local/bin/wal-g wal-push %p'" >> /etc/postgresql/12/main/postgresql.conf
$ echo "archive_timeout = 60" >> /etc/postgresql/12/main/postgresql.conf
`

### 3\. Restart the database [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#3-restart-the-database)

The database is restarted to let the changes in the configuration to take effect.

`
$ sudo /etc/init.d/postgresql restart
`

### 4\. Create your first physical backup [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#4-create-your-first-physical-backup)

`
$ sudo -su postgres envdir /etc/wal-g.d/env /usr/local/bin/wal-g backup-push /var/lib/postgresql/12/main
`

At this point, if you were to check the S3 path that you provided, the following two newly created and populated directories would be observed:

![Alt Text](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2020%2Flai1mxg62kffyd2khmtm.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

From then on, subsequent physical backups would be found in the directory `basebackups_005` and any WAL archives would be sent to the directory `wal_005`.

### 5\. \[Optional\] Schedule regular physical backups [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#5-optional-schedule-regular-physical-backups)

A CRON job can then be set to schedule physical backups to be performed everyday:

`
$ echo "0 0 * * * postgres /usr/bin/envdir /etc/wal-g.d/env /usr/local/bin/wal-g backup-push /var/lib/postgresql/12/main" > /etc/cron.d/pg_backup
`

Here, the instance has been instructed to back up the database at the start of each day at midnight. By physically backing up your instance regularly, overall recovery time could be faster. Restoring from a physical backup from yesterday would lead to fewer WAL archive files to be replayed as compared to restoring from one from a month ago.

* * *

## Disaster strikes [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#disaster-strikes)

Something goes wrong with the database or instance. We will now use what available physical backups we have in the S3 bucket to recover and restore all of our data on to a new instance.

### 1\. Configure environment variables [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#1-configure-environment-variables-1)

The configuration should be the **same** as the original instance. For recovery and restoration, we would not need the variable `PGPASSWORD`.

`
$ umask u=rwx,g=rx,o=
$ mkdir -p /etc/wal-g.d/env
$ echo 'secret-key-content' > /etc/wal-g.d/env/AWS_SECRET_ACCESS_KEY
$ echo 'access-key' > /etc/wal-g.d/env/AWS_ACCESS_KEY_ID
$ echo 's3://backup-bucket/project-directory' > /etc/wal-g.d/env/WALG_S3_PREFIX
$ chown -R root:postgres /etc/wal-g.d
`

### 2\. Stop the database [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#2-stop-the-database)

`
$ sudo /etc/init.d/postgresql stop
`

### 3\. Switch to the user `postgres` [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#3-switch-to-the-user-postgres)

`
$ sudo -su postgres
`

### 4\. Prepare the database for recovery [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#4-prepare-the-database-for-recovery)

#### Set restore\_command [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#set-restore_command)

Through [restore\_command](https://www.postgresql.org/docs/12/continuous-archiving.html#:~:text=must%20specify%20is%20the%20restore_command,%20which%20tells%20PostgreSQL%20how%20to%20retrieve%20archived%20WAL%20file%20segments), we instruct Postgres to pull all WAL archives from our S3 bucket to use during recovery.

`
$ echo "restore_command = '/usr/bin/envdir /etc/wal-g.d/env /usr/local/bin/wal-g wal-fetch \"%f\" \"%p\" >> /tmp/wal.log 2>&1'" >> /etc/postgresql/12/main/postgresql.conf
`

#### \[Optional\] Achieve Point in Time Recovery (PITR) [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#optional-achieve-point-in-time-recovery-pitr)

If we want to restore the database only up to a certain point in time (eg. right before the disaster), we can do so by setting both [recovery\_target\_time](https://www.postgresql.org/docs/12/runtime-config-wal.html#:~:text=recovery_target_time%20(timestamp)) and [recovery\_target\_action](https://www.postgresql.org/docs/12/runtime-config-wal.html#:~:text=recovery_target_action%20(enum)). Do note that the timezone would need to match that of the original instance. This is usually at the UTC (+00) timezone.

`
$ echo "recovery_target_time = '2020-07-27 01:23:00.000000+00'" >> /etc/postgresql/12/main/postgresql.conf
$ echo "recovery_target_action = 'promote'" >> /etc/postgresql/12/main/postgresql.conf
`

### 5\. Restore from physical backup [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#5-restore-from-physical-backup)

The current data directory is deleted and is replaced with the latest version of the physical backup from the S3 bucket.

`
$ rm -rf /var/lib/postgresql/12/main
$ envdir /etc/wal-g.d/env /usr/local/bin/wal-g backup-fetch /var/lib/postgresql/12/main LATEST
`

### 6\. Create a `recovery.signal` file [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#6-create-a-recoverysignal-file)

This file [instructs](https://www.postgresql.org/docs/12/continuous-archiving.html#:~:text=Set%20recovery%20configuration%20settings%20in%20postgresql.conf%20(see%20Section%2019.5.4)%20and%20create%20a%20file%20recovery.signal%20in%20the%20cluster%20data%20directory) Postgres that the database should undergo recovery mode upon start.

`
$ touch /var/lib/postgresql/12/main/recovery.signal
`

### 7\. Log out of `postgres` and start the database [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#7-log-out-of-postgres-and-start-the-database)

`
$ exit
$ sudo /etc/init.d/postgresql start
`

Once Postgres finishes starting up and completes recovery mode, all data or data up to the specified point in time would have been successfully restored on to the new instance. Disaster averted.

## More Postgres resources [\#](https://supabase.com/blog/continuous-postgresql-backup-walg\#more-postgres-resources)

- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
- [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
- [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
- [Postgres Views](https://supabase.com/blog/postgresql-views)
- [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
- [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
- [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcontinuous-postgresql-backup-walg&text=Continuous%20PostgreSQL%20Backups%20using%20WAL-G)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcontinuous-postgresql-backup-walg&text=Continuous%20PostgreSQL%20Backups%20using%20WAL-G)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcontinuous-postgresql-backup-walg&t=Continuous%20PostgreSQL%20Backups%20using%20WAL-G)

[Last post\\
\\
**Supabase Auth** \\
\\
5 August 2020](https://supabase.com/blog/supabase-auth)

[Next post\\
\\
**Supabase Alpha July 2020** \\
\\
2 August 2020](https://supabase.com/blog/supabase-alpha-july-2020)

[postgres](https://supabase.com/blog/tags/postgres) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Introduction](https://supabase.com/blog/continuous-postgresql-backup-walg#introduction)
- [Prerequisites](https://supabase.com/blog/continuous-postgresql-backup-walg#prerequisites)
- [Setting it up](https://supabase.com/blog/continuous-postgresql-backup-walg#setting-it-up)
- [Disaster strikes](https://supabase.com/blog/continuous-postgresql-backup-walg#disaster-strikes)
- [More Postgres resources](https://supabase.com/blog/continuous-postgresql-backup-walg#more-postgres-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcontinuous-postgresql-backup-walg&text=Continuous%20PostgreSQL%20Backups%20using%20WAL-G)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcontinuous-postgresql-backup-walg&text=Continuous%20PostgreSQL%20Backups%20using%20WAL-G)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcontinuous-postgresql-backup-walg&t=Continuous%20PostgreSQL%20Backups%20using%20WAL-G)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)