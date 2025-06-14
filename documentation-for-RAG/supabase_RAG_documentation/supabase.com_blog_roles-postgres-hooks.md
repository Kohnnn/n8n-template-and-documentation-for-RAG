---
url: "https://supabase.com/blog/roles-postgres-hooks"
title: "Protecting reserved roles with PostgreSQL Hooks"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Protecting reserved roles with PostgreSQL Hooks

02 Jul 2021

•

14 minute read

[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)

![Protecting reserved roles with PostgreSQL Hooks](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgres-hooks%2Fcover-postgres-hooks.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

PostgreSQL manages permissions through roles. To create these roles, a database user needs the `CREATEROLE` privilege,
which not only allows role creation but also _modification_ of any role (except superusers).

At Supabase, we use dedicated roles for each of our customers' backend services. For instance, our [Storage API](https://supabase.com/storage)
uses the `supabase_storage_admin` role for connecting to the database. Giving the `CREATEROLE` privilege to our customers would allow them to
drop this role and take their own Storage API down.

And yet, we want to give our customers the ability to manage roles the same as they do it in on-premises databases,
with the usual `CREATE ROLE`, `ALTER ROLE`, and `DROP ROLE` statements.

So, how do we grant them the `CREATEROLE` privilege and, at the same time, protect our own roles? In this blog post,
we explain how we managed to do this by using PostgreSQL Hooks in our [SupaUtils](https://github.com/supabase/supautils) extension.

## Reserved Roles [\#](https://supabase.com/blog/roles-postgres-hooks\#reserved-roles)

PostgreSQL has a list of [predefined roles](https://www.postgresql.org/docs/14/predefined-roles.html) — all prefixed
with "pg\_" — that cannot be dropped or altered. Attempting to do so will throw an error mentioning that the role is "reserved".

`
alter role pg_monitor createdb;
ERROR:  role name "pg_monitor" is reserved
DETAIL:  Cannot alter reserved roles.
`

This mechanism is an internal implementation detail. Unfortunately Postgres doesn't allow us to define our own reserved roles.

### RDS reserved roles [\#](https://supabase.com/blog/roles-postgres-hooks\#rds-reserved-roles)

Amazon RDS has a similar defense mechanism, all of its predefined roles — prefixed with "rds" — cannot be modified.

`
alter role rdsadmin rename to another;
ERROR: The "rdsadmin" role cannot be renamed.
DETAIL: The "rdsadmin" role cannot be renamed because either the source
        or the target name refer to an Amazon RDS reserved role name.
LOCATION:  handle_rename, rdsutils.c:1534
`

Again, the error mentions that the role is "reserved".

Also note the `rdsutils.c` mention. That's not a stock Postgres source file. This means that the logic comes
from an RDS extension. We can confirm this is the case by showing the preloaded libraries.

`
show shared_preload_libraries;
shared_preload_libraries
-----------------------------
rdsutils,pg_stat_statements
`

`rdsutils` can be seen there. Naturally this lead us into thinking we can achieve the same logic with an extension
of our own, and thus the SupaUtils idea was born.

## Extending PostgreSQL with Hooks [\#](https://supabase.com/blog/roles-postgres-hooks\#extending-postgresql-with-hooks)

PostgreSQL hooks allow us to extend internal functionality. Hooks can modify behavior at different places,
including when running SQL statements.

For example, if we wanted to enforce our own password restrictions whenever a user changes passwords, we could
use the `check_password_hook` to verify the password. We would write out our own Custom Logic, and raise an error
if the password fails the password requirements.

![This is an images of the lifecycle of a Postgres Hook.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgres-hooks%2Fhooks-postgres-alter-role.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

For `SupaUtils`, we're particularly interested in the `ProcessUtility_hook`, which allows us to hook into **utility statements:** every statement except `select`, `insert`, `delete` or `update`. They include `alter role` and `drop role`, which are the statements we want to hook on.

### Hooks are global function pointers [\#](https://supabase.com/blog/roles-postgres-hooks\#hooks-are-global-function-pointers)

To use hooks, we can override functions pointers that are global. On the Postgres codebase, the `ProcessUtility_hook` is basically used[1](https://supabase.com/blog/roles-postgres-hooks#user-content-fn-1) like this:

`
// src/backend/tcop/utility.c
// ProcessUtility_hook is NULL by default
ProcessUtility_hook_type ProcessUtility_hook = NULL;
// This function is used for processing all the utility statements
void
ProcessUtility(PARAMS_OMITTED_FOR_BREVITY)
{
// call the ProcessUtility_hook if it's not NULL
if (ProcessUtility_hook)
(*ProcessUtility_hook)(PARAMS_OMITTED_FOR_BREVITY);
// otherwise call the standard function used to process utility statements
else
standard_ProcessUtility(PARAMS_OMITTED_FOR_BREVITY);
}
`

As you can see, `ProcessUtility_hook` is `NULL` by default, so our extension should set it for the hook to run. Also, the `standard_ProcessUtility` function is the one that actually does the job of creating or modifying the roles (among other things) so our hook should also call it.

### Loading and running the hook [\#](https://supabase.com/blog/roles-postgres-hooks\#loading-and-running-the-hook)

Each extension set in `shared_preload_libraries` will get its `_PG_init` function called. This function will allow us to set our hook onto `ProcessUtility_hook`.

Since hooks are global function pointers, it might be the case that another extension modifies the hook pointer (on its own `_PG_init`) before us and sets its own hook. So we need to ensure we also run this previously-set hook, before or after our own hook runs.

It's typically[2](https://supabase.com/blog/roles-postgres-hooks#user-content-fn-2) done like this:

`
// variable to store the previous hook
static ProcessUtility_hook_type prev_hook = NULL;
// initialize our extension
void
_PG_init(void)
{
// ProcessUtility_hook has the global function pointer.
// Store its value in case another extension already set its own hook.
prev_hook = ProcessUtility_hook;
// Now override the ProcessUtility_hook with our hook
ProcessUtility_hook = our_hook;
}
static void
our_hook(PARAMS_OMITTED_FOR_BREVITY)
{
// our hook logic goes here
// If there was a previous hook, run it after our hook
if (prev_hook)
    prev_hook(PARAMS_OMITTED_FOR_BREVITY);
// If there's no previous hook, call the standard function
else
    standard_ProcessUtility(PARAMS_OMITTED_FOR_BREVITY);
}
`

## Setting up the SupaUtils extension [\#](https://supabase.com/blog/roles-postgres-hooks\#setting-up-the-supautils-extension)

We can use the concepts above to build our extension.

First we'll need a Makefile in order to compile the extension code and include it into our PostgreSQL installation.

`
# Makefile
# Our shared library
MODULE_big = supautils
# Our object files to build for the library
OBJS = src/supautils.o
# Tell pg_config to pass us the PostgreSQL extensions makefile(PGXS)
# and include it into our own Makefile through the standard "include" directive.
PG_CONFIG = pg_config
PGXS := $(shell $(PG_CONFIG) --pgxs)
include $(PGXS)
`

For the source file, we'll start with variable definitions and functions declarations.

`
// src/supautils.c
// include common declarations
#include "postgres.h"
// required macro for extension libraries to work
PG_MODULE_MAGIC;
// variable for the previous hook
static ProcessUtility_hook_type prev_hook = NULL;
// variable for our reserved roles configuration parameter
static char *reserved_roles = NULL;
// function declaration for extension initialization
void _PG_init(void);
// function declaration for our hook
static void supautils_hook(
    PlannedStmt *pstmt,
    const char *queryString,
    ProcessUtilityContext context,
    ParamListInfo params,
    QueryEnvironment *queryEnv,
    DestReceiver *dest,
    QueryCompletion *completionTag
);
// function declaration for our pure function that will return a reserved role
static char* look_for_reserved_role(Node *utility_stmt, List *reserved_role_list);
`

Up next we'll define each one of these function declarations.

## Initializing the extension [\#](https://supabase.com/blog/roles-postgres-hooks\#initializing-the-extension)

Let's now `_PG_init` our extension. Besides setting the hook here, we want to define our reserved roles as a configuration parameter, that way they can be modified by editing the `postgresql.conf` file. For this, we can use the `DefineCustomStringVariable` function, which inserts the parameter into Postgres "Grand Unified Configuration"(GUC) system.

`
void
_PG_init(void)
{
// Store the previous hook
prev_hook = ProcessUtility_hook;
// Set our hook
ProcessUtility_hook = supautils_hook;
// Define our "supautils.reserved_roles" parameter
// some arguments are unused so they are left as NULL
DefineCustomStringVariable("supautils.reserved_roles",
"Comma-separated list of roles that cannot be altered or dropped",
NULL,
// It will be assigned to the reserved_roles variable
&reserved_roles,
NULL,
// We should be able to reload this parameter without restarting the server,
// e.g. with "select pg_reload_conf()".
PGC_SIGHUP,
0,
NULL, NULL, NULL);
}
`

## Running the SupaUtils hook [\#](https://supabase.com/blog/roles-postgres-hooks\#running-the-supautils-hook)

Now that our hook is set, we'll define what it will do. As specified in the [ProcessUtility\_hook\_type](https://github.com/postgres/postgres/blob/f807e3410fdfc29ced6590c7c2afa76637e001ad/src/include/tcop/utility.h#L71-L75), the hook's first parameter is a `PlannedStmt`, this represents the planned statement — the output from the Postgres planner. This is a step before the statement is executed.

We'll look for the presence of a reserved role in the planned statement. If there's one present, we'll report an error and abort the statement execution step.

`
static void
supautils_hook(
      // The planned statement
      PlannedStmt *pstmt,
      // These parameters are here for completion, we'll not use any of them
      const char *queryString,
      ProcessUtilityContext context,
      ParamListInfo params,
      QueryEnvironment *queryEnv,
      DestReceiver *dest,
      QueryCompletion *completionTag
)
{
// Get the utility statement from the planned statement
Node     *utility_stmt = pstmt->utilityStmt;
// Only do the logic if supautils.reserved_roles is not NULL
if(reserved_roles){
    // The found reserved role, assume none was found by default
    char *reserved_role = NULL;
    // Temp var for storing the list of reserved roles
    List *reserved_role_list;
    // split the comma-separated string into a List by using a
    // helper function from varlena.h
    if (!SplitIdentifierString(pstrdup(reserved_roles), ',', &reserved_role_list))
      // abort and report an error if the splitting fails
      ereport(ERROR,
          (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
           errmsg("parameter \"%s\" must be a comma-separated list of "
             "identifiers", reserved_roles)));
    // look for the reserved role in an internal function
    reserved_role = look_for_reserved_role(utility_stmt, reserved_role_list);
    // we're done with the list so free it from memory
    list_free(reserved_role_list);
    // abort and report an error if a reserved role was found
    if(reserved_role)
      ereport(ERROR,
        (errcode(ERRCODE_INSUFFICIENT_PRIVILEGE),
         errmsg("\"%s\" is a reserved role, it cannot be modified", reserved_role)));
}
// Run the previous hook if defined or call the standard function
if (prev_hook)
    prev_hook(pstmt, queryString,
                context, params, queryEnv,
                dest, completionTag);
else
    standard_ProcessUtility(pstmt, queryString,
                context, params, queryEnv,
                dest, completionTag);
}
`

## Looking for the reserved role [\#](https://supabase.com/blog/roles-postgres-hooks\#looking-for-the-reserved-role)

Lastly, we'll define how we look for the reserved role.

At this stage, we already have the utility statement and the reserved role list. All that's left to do is to define if the utility statement is an `ALTER ROLE` or `DROP ROLE` statement, and whether if the role it affects is a reserved one.

`
static char*
look_for_reserved_role(Node *utility_stmt, List *reserved_role_list)
{
// Check the utility statement type
switch (utility_stmt->type)
{
    // Matches statements like:
    // ALTER ROLE role NOLOGIN
    case T_AlterRoleStmt:
    {
      // cast the utility statement to an alter role statement
      AlterRoleStmt *stmt = (AlterRoleStmt *) utility_stmt;
      //RoleSpec has the role name plus some attributes
      RoleSpec *role = stmt->role;
      // postgres defines its own list utilities in pg_list.h
      // ListCell is an element of the list that we'll use for iteration
      ListCell *role_cell;
      // pg_list.h includes the foreach macro for iterating over lists
      foreach(role_cell, reserved_role_list)
      {
      	// get the list element
        char *reserved_role = (char *) lfirst(role_cell);
        // compare the statement role with the reserved role
        // get_rolespec_name will get the RoleSpec role name,
        // even in cases where the role is the special case of
        // "current_user" or "session_user"
        if (strcmp(get_rolespec_name(role), reserved_role) == 0)
          return reserved_role;
      }
      break;
    }
    // Matches statements like:
    // DROP ROLE role
    case T_DropRoleStmt:
    {
      // cast the utility statement to a drop role statement
      DropRoleStmt *stmt = (DropRoleStmt *) utility_stmt;
      ListCell *item;
      // the logic is the same as before, iterate over the reserved role list
      // and find a match
      foreach(item, stmt->roles)
      {
        RoleSpec *role = lfirst(item);
        ListCell *role_cell;
        foreach(role_cell, reserved_role_list)
        {
          char *reserved_role = (char *) lfirst(role_cell);
          if (strcmp(get_rolespec_name(role), reserved_role) == 0)
            return reserved_role;
        }
      }
      break;
    }
    default:
      break;
}
// Didn't find any reserved role on the statement, so return NULL
return NULL;
}
`

## Testing the extension [\#](https://supabase.com/blog/roles-postgres-hooks\#testing-the-extension)

Now that the code is finished, we can test the extension. Since we already have a `Makefile`, the extension can be installed by doing `make && make install`. Then, in postgresql.conf:

`
# set the extension as preloaded, this will require a restart
shared_preload_libraries="supautils"
# the reserved roles
supautils.reserved_roles="supabase_storage_admin, supabase_auth_admin"
`

We'll now try to alter or drop the reserved roles:

`
alter role supabase_storage_admin nologin password 'fake';
ERROR:  "supabase_storage_admin" is a reserved role, it cannot be modified
drop role supabase_auth_admin;
ERROR:  "supabase_auth_admin" is a reserved role, it cannot be modified
-- Success!!
`

## Wrapping up [\#](https://supabase.com/blog/roles-postgres-hooks\#wrapping-up)

As you can see, PostgreSQL Hooks allow us to intercept SQL statements. There are many types of hooks, you can see unofficial documentation for these at [AmatanHead/psql-hooks](https://github.com/AmatanHead/psql-hooks).

The full SupaUtils code is in our [GitHub repository](https://github.com/supabase/supautils/).

By the way, if you like working on PostgreSQL tooling and extensions: we are hiring [PostgreSQL experts](https://supabase.com/docs/careers/postgres-experts)!

## More Postgres resources [\#](https://supabase.com/blog/roles-postgres-hooks\#more-postgres-resources)

- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
- [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
- [Postgres Views](https://supabase.com/blog/postgresql-views)
- [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
- [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
- [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
- [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)

## Footnotes [\#](https://supabase.com/blog/roles-postgres-hooks\#footnote-label)

1. You can see the `ProcessUtility_hook` declaration [here](https://github.com/postgres/postgres/blob/11e9caff82bc7326e2bc9782937cb03875050cc4/src/backend/tcop/utility.c#L75-L76) and its usage [here](https://github.com/postgres/postgres/blob/11e9caff82bc7326e2bc9782937cb03875050cc4/src/backend/tcop/utility.c#L515-L527). [↩](https://supabase.com/blog/roles-postgres-hooks#user-content-fnref-1)

2. This is also done on [pg\_stat\_statements](https://github.com/postgres/postgres/blob/6991e774e0304f5ef488cf1ae4fa79578b6ae3d5/contrib/pg_stat_statements/pg_stat_statements.c#L1130-L1137) and [sepgsql](https://github.com/postgres/postgres/blob/6991e774e0304f5ef488cf1ae4fa79578b6ae3d5/contrib/sepgsql/hooks.c#L381-L388). [↩](https://supabase.com/blog/roles-postgres-hooks#user-content-fnref-2)


Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Froles-postgres-hooks&text=Protecting%20reserved%20roles%20with%20PostgreSQL%20Hooks)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Froles-postgres-hooks&text=Protecting%20reserved%20roles%20with%20PostgreSQL%20Hooks)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Froles-postgres-hooks&t=Protecting%20reserved%20roles%20with%20PostgreSQL%20Hooks)

[Last post\\
\\
**Supabase Launch Week II: The SQL** \\
\\
22 July 2021](https://supabase.com/blog/supabase-launch-week-sql)

[Next post\\
\\
**Supabase Beta May 2021** \\
\\
2 June 2021](https://supabase.com/blog/supabase-beta-may-2021)

[postgres](https://supabase.com/blog/tags/postgres) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Reserved Roles](https://supabase.com/blog/roles-postgres-hooks#reserved-roles)
- [Extending PostgreSQL with Hooks](https://supabase.com/blog/roles-postgres-hooks#extending-postgresql-with-hooks)
- [Setting up the SupaUtils extension](https://supabase.com/blog/roles-postgres-hooks#setting-up-the-supautils-extension)
- [Initializing the extension](https://supabase.com/blog/roles-postgres-hooks#initializing-the-extension)
- [Running the SupaUtils hook](https://supabase.com/blog/roles-postgres-hooks#running-the-supautils-hook)
- [Looking for the reserved role](https://supabase.com/blog/roles-postgres-hooks#looking-for-the-reserved-role)
- [Testing the extension](https://supabase.com/blog/roles-postgres-hooks#testing-the-extension)
- [Wrapping up](https://supabase.com/blog/roles-postgres-hooks#wrapping-up)
- [More Postgres resources](https://supabase.com/blog/roles-postgres-hooks#more-postgres-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Froles-postgres-hooks&text=Protecting%20reserved%20roles%20with%20PostgreSQL%20Hooks)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Froles-postgres-hooks&text=Protecting%20reserved%20roles%20with%20PostgreSQL%20Hooks)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Froles-postgres-hooks&t=Protecting%20reserved%20roles%20with%20PostgreSQL%20Hooks)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)