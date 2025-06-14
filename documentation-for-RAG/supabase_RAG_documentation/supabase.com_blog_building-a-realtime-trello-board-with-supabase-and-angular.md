---
url: "https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular"
title: "Building a Realtime Trello Board with Supabase and Angular"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Building a Realtime Trello Board with Supabase and Angular

24 Aug 2022

•

48 minute read

[![Simon Grimm avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaimon24.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Simon GrimmGuest Author](https://twitter.com/schlimmson)

![Building a Realtime Trello Board with Supabase and Angular](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fangular-supabase.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Everyone can code up a little hello world example quickly with a platform like [Supabase](https://supabase.com/) \- but what about a _real world_ project of bigger scale?

That's exactly what you will learn in this article:

We are building a Trello board with Supabase, Angular and Tailwind!

![Supabase Trello Example](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Along our jurney we will:

- write some **advanced SQL** to create our tables
- implement **magic link sign in** and user authentication with Angular
- make use of **the realtime capabilities**!

Building a Realtime Trello Board with Supabase and Angular - YouTube

Simon Grimm

117K subscribers

[Building a Realtime Trello Board with Supabase and Angular](https://www.youtube.com/watch?v=jmCiI_OSarA)

Simon Grimm

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

[Watch on YouTube](https://www.youtube.com/watch?v=jmCiI_OSarA "Watch on YouTube")

Watch the video version of the tutorial.

Since there are quite some code snippets we need I've put together the [full source code on Github](https://github.com/saimon24/supabase-trello-angular) so you can easily run the project yourself!

If you are not familiar with [Trello](https://trello.com/), it's a way to manage projects with different boards, lists and cards!

Ready for a wild adventure? Then let's begin inside our Supabase account!

## Creating the Supabase Project [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#creating-the-supabase-project)

First of all we need a new Supabase project. If you don't have a Supabase account yet, you can [get started for free](https://supabase.com/dashboard/)!

In your dashboard, click "New Project" and leave it to the default settings, but make sure you keep a copy o your Database password!

The only thing we will change manually for now is disabling the email confirmation step. By doing this, users will be directly able to sign in when using the magic link, so go to the **Authentication** tab of your project, select **Settings** and scroll down to your **Auth Providers** where you can disable it.

![Disable Email confirm](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fdisable-email-confirm.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Everything else regarding authentication\[ [https://supabase.com/docs/guides/auth](https://supabase.com/docs/guides/auth)\] is handled by Supabase and we don't need to worry about it at the moment!

## Defining your Tables with SQL [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#defining-your-tables-with-sql)

Since Supabase uses Postgres under the hood, we need to write some SQL to define our tables.

Let's start with something easy, which is the general definition of our tables:

- `boards`: Keep track of user created boards
- `lists`: The lists within one board
- `cards`: The cards with tasks within one list
- `ssers`: A table to keep track of all registered users
- `user_boards`: A many to many table to keep track which boards a user is part of

We're not going into SQL details, but you should be able to paste the following snippets into the **SQL Editor** of your project.

![SQL Editor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fsql-editor.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Simply navigate to the menu item and click on **\+ New query**, paste in the SQL and hit **RUN** which hopefully executes without issues:

`
drop table if exists user_boards;
drop table if exists cards;
drop table if exists lists;
drop table if exists boards;
drop table if exists users;
-- Create boards table
create table boards (
id bigint generated by default as identity primary key,
creator uuid references auth.users not null default auth.uid(),
title text default 'Untitled Board',
created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
-- Create lists table
create table lists (
id bigint generated by default as identity primary key,
board_id bigint references boards ON DELETE CASCADE not null,
title text default '',
position int not null default 0,
created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
-- Create Cards table
create table cards (
id bigint generated by default as identity primary key,
list_id bigint references lists ON DELETE CASCADE not null,
board_id bigint references boards ON DELETE CASCADE not null,
position int not null default 0,
title text default '',
description text check (char_length(description) > 0),
assigned_to uuid references auth.users,
done boolean default false,
created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
-- Many to many table for user <-> boards relationship
create table user_boards (
id bigint generated by default as identity primary key,
user_id uuid references auth.users ON DELETE CASCADE not null default auth.uid(),
board_id bigint references boards ON DELETE CASCADE
);
-- User ID lookup table
create table users (
id uuid not null primary key,
email text
);
-- Make sure deleted records are included in realtime
alter table cards replica identity full;
alter table lists replica identity full;
-- Function to get all user boards
create or replace function get_boards_for_authenticated_user()
returns setof bigint
language sql
security definer
set search_path = ''
stable
as $$
    select board_id
    from public.user_boards
    where user_id = auth.uid()
$$;
`

Besides the creation of tables we also changed the replica identity, which helps to alter retrieve records when a row is deleted.

Finally we defined a very important **function** that we will use to make the table secure using [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security).

This function will retrieve all boards of a user from the `user_boards` table and will be used in our policies now.

We now enabled the row level security for the different tables and define some **policies** so only users with the right access can read/update/delete rows.

Go ahead and run another SQL query in the editor now:

`
-- boards row level security
alter table boards enable row level security;
-- Policies
create policy "Users can create boards" on boards for
insert to authenticated with CHECK (true);
create policy "Users can view their boards" on boards for
    select using (
      id in (
        select get_boards_for_authenticated_user()
      )
    );
create policy "Users can update their boards" on boards for
    update using (
      id in (
        select get_boards_for_authenticated_user()
      )
    );
create policy "Users can delete their created boards" on boards for
    delete using ((select auth.uid()) = creator);
-- user_boards row level security
alter table user_boards enable row level security;
create policy "Users can add their boards" on user_boards for
    insert to authenticated with check (true);
create policy "Users can view boards" on user_boards for
    select using ((select auth.uid()) = user_id);
create policy "Users can delete their boards" on user_boards for
    delete using ((select auth.uid()) = user_id);
-- lists row level security
alter table lists enable row level security;
-- Policies
create policy "Users can edit lists if they are part of the board" on lists for
    all using (
      board_id in (
        select get_boards_for_authenticated_user()
      )
    );
-- cards row level security
alter table cards enable row level security;
-- Policies
create policy "Users can edit cards if they are part of the board" on cards for
    all using (
      board_id in (
        select get_boards_for_authenticated_user()
      )
    );
`

Finally we need a **trigger** that reacts to changes in our database.

In our case we want to listen to the creation of new boards, which will automatically create the board < - > user connection in the `user_boards` table.

Additionally we will also add every new authenticated user to our `users` table since you later don't have access to the internal auth table of Supabase!

Therefore run one last query:

`
-- inserts a row into user_boards
create function public.handle_board_added()
returns trigger
language plpgsql
security definer
as $$
begin
insert into public.user_boards (board_id, user_id)
values (new.id, auth.uid());
return new;
end;
$$;
-- trigger the function every time a board is created
create trigger on_board_created
after insert on boards
for each row execute procedure public.handle_board_added();
create or replace function public.handle_new_user()
returns trigger as $$
begin
insert into public.users (id, email)
values (new.id, new.email);
return new;
end;
$$ language plpgsql security definer;
create trigger on_auth_user_created
after insert on auth.users
for each row execute procedure public.handle_new_user();
`

At this point our Supabase project is configured correctly and we can move into the actual application!

## Creating the Angular Project [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#creating-the-angular-project)

We are not bound to any framework, but in this article we are using [Angular](https://supabase.com/docs/guides/with-angular) to build a robust web application.

Get started by using the [Angular CLI](https://angular.io/cli) to generate a new project and then add some components and services that we will need.

Finally we can install the [Supabase JS package](https://github.com/supabase/supabase-js) and two additional helper packages for some cool functionality, so go ahead and run:

`
ng new trelloBoard --routing --style=scss
cd ./trelloBoard
# Generate components and services
ng generate component components/login
ng generate component components/inside/workspace
ng generate component components/inside/board
ng generate service services/auth
ng generate service services/data
# Install Supabase and additional packages
npm install @supabase/supabase-js
npm install ngx-spinner ngx-gravatar
`

To import the installed packages we can quickly change our **src/app/app.module.ts** to:

`
import { NgModule } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { AppRoutingModule } from './app-routing.module'
import { AppComponent } from './app.component'
import { LoginComponent } from './components/login/login.component'
import { BoardComponent } from './components/inside/board/board.component'
import { WorkspaceComponent } from './components/inside/workspace/workspace.component'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { NgxSpinnerModule } from 'ngx-spinner'
import { FormsModule } from '@angular/forms'
import { GravatarModule } from 'ngx-gravatar'
@NgModule({
declarations: [AppComponent, LoginComponent, BoardComponent, WorkspaceComponent],
imports: [\
    FormsModule,\
    BrowserModule,\
    AppRoutingModule,\
    BrowserAnimationsModule,\
    NgxSpinnerModule,\
    GravatarModule,\
],
providers: [],
bootstrap: [AppComponent],
})
export class AppModule {}
`

On top of that the [ngx-spinner](https://github.com/Napster2210/ngx-spinner) needs another entry in the **angular.json** to copy over resources so we can later easily display a loading indicator, so open it and change the `styles` array to this:

`
"styles": [\
"src/styles.scss",\
"node_modules/ngx-spinner/animations/ball-scale-multiple.css"\
],
`

Since we have already generated some components, we can also change our app routing to inlcude the new pages in the **src/app/app-routing.module.ts** now:

`
import { BoardComponent } from './components/inside/board/board.component'
import { WorkspaceComponent } from './components/inside/workspace/workspace.component'
import { LoginComponent } from './components/login/login.component'
import { NgModule } from '@angular/core'
import { RouterModule, Routes } from '@angular/router'
const routes: Routes = [\
{\
    path: '',\
    component: LoginComponent,\
},\
{\
    path: 'workspace',\
    component: WorkspaceComponent,\
},\
{\
    path: 'workspace/:id',\
    component: BoardComponent,\
},\
{\
    path: '**',\
    redirectTo: '/',\
},\
]
@NgModule({
imports: [RouterModule.forRoot(routes, {})],
exports: [RouterModule],
})
export class AppRoutingModule {}
`

Our app will start with the login screen, after which we can move to the workspace with our boards and finally dive into one specific board to show all its lists and cards.

To correctly use the Angular router we can now update the **src/app/app.component.html** so it only holds one line:

`
<router-outlet></router-outlet>
`

Finally the most important configuration step: Adding our Supabase credentials to the **src/environments/environment.ts** like this:

`
export const environment = {
production: false,
supabaseUrl: 'YOUR-URL',
supabaseKey: 'YOUR-ANON-KEY',
}
`

You can find those values in your Supabase project by clicking on the **Settings** icon and then navigating to **API** where it shows your **Project API keys**.

![Supabase project settings](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fproject-settings.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The `anon` key is safe to use in a frontend project since we have enabled RLS on our database anyway!

## Adding Tailwind for Styling [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#adding-tailwind-for-styling)

We could build an ugly project or easily make it look awesome by installing [Tailwind CSS](https://tailwindcss.com/) \- we opt for the second in this article!

There are certainly other styling libraries that you can use, so this step is completely optional but required in order to make code of this tutorial work.

Therefore we follow the [Angular guide](https://tailwindcss.com/docs/guides/angular) and install Tailwind like this:

`
npm install -D tailwindcss postcss autoprefixer @tailwindcss/forms
npx tailwindcss init
`

Now we also need to update our **tailwind.config.js** to this:

`
/** @type {import('tailwindcss').Config} */
module.exports = {
content: ['./src/**/*.{html,ts}'],
theme: {
    extend: {},
},
plugins: [require('@tailwindcss/forms')],
}
`

Finally we include the styling in our **src/styles.scss**:

`
@tailwind base;
@tailwind components;
@tailwind utilities;
`

And with that the whole project configuration is done and we can focus 100% on the functionality of our Trello clone!

## Building a Magic Link Sign In [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#building-a-magic-link-sign-in)

We could now add all sorts of authetnication using the auth providers that Supabase provides, but we will simply use a magic link sign in where users only need to pass their email.

To kick this off we will implement a simple authentication service that keeps track of our current user with a **BehaviourSubject** so we can easily emit new values later when the user session changes.

We are also loading the session once "by hand" using `getUser()` since the `onAuthStateChange` event is usually not broadcasted when the page loads, and we want to load a stored session in that case as well.

In order to send an email to the user we only need to call `signIn()` and only pass an email - Supabase takes care of the rest for us!

Therefore get started by changing the **src/app/services/auth.service.ts** to this now:

`
import { Injectable } from '@angular/core'
import { Router } from '@angular/router'
import { createClient, SupabaseClient, User } from '@supabase/supabase-js'
import { BehaviorSubject } from 'rxjs'
import { environment } from 'src/environments/environment'
@Injectable({
providedIn: 'root',
})
export class AuthService {
private supabase: SupabaseClient
private _currentUser: BehaviorSubject<boolean | User | any> = new BehaviorSubject(null)
constructor(private router: Router) {
    this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)
    // Manually load user session once on page load
    // Note: This becomes a promise with getUser() in the next version!
    const user = this.supabase.auth.user()
    if (user) {
      this._currentUser.next(user)
    } else {
      this._currentUser.next(false)
    }
    this.supabase.auth.onAuthStateChange((event, session) => {
      if (event == 'SIGNED_IN') {
        this._currentUser.next(session!.user)
      } else {
        this._currentUser.next(false)
        this.router.navigateByUrl('/', { replaceUrl: true })
      }
    })
}
signInWithEmail(email: string) {
    // Note: This becomes signInWithOTP() in the next version!
    return this.supabase.auth.signIn({
      email,
    })
}
logout() {
    this.supabase.auth.signOut()
}
get currentUser() {
    return this._currentUser.asObservable()
}
}
`

That's a solid starting point for our authetnication logic, and now we just need to use those functions on our login page.

Additionally we will also listen to user changes here since this is the page a user will load when clicking on the magic link. We can use the `currentUser` from our service so we don't need any additional logic for that.

Once we start the sign in we can also use our cool spinner package to show a little indicator and afterwards flip the value of `linkSuccess` so we can present a little text in our UI.

We're keeping it fairly easy, so let's change the **src/app/components/login/login.component.ts** to:

`
import { Router } from '@angular/router'
import { AuthService } from './../../services/auth.service'
import { Component, OnInit } from '@angular/core'
import { NgxSpinnerService } from 'ngx-spinner'
@Component({
selector: 'app-login',
templateUrl: './login.component.html',
styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
email = ''
linkSuccess = false
constructor(
    private auth: AuthService,
    private spinner: NgxSpinnerService,
    private router: Router
) {
    this.auth.currentUser.subscribe((user) => {
      if (user) {
        this.router.navigateByUrl('/workspace', { replaceUrl: true })
      }
    })
}
ngOnInit(): void {}
async signIn() {
    this.spinner.show()
    const result = await this.auth.signInWithEmail(this.email)
    this.spinner.hide()
    if (!result.error) {
      this.linkSuccess = true
    } else {
      alert(result.error.message)
    }
}
}
`

Last piece is our UI now, and since we are using Tailwind the HTML snippets won't look very beautiful.

Nonetheless, it's just some CSS and connecting our fields and buttons to the right functions, so go ahead and change the **src/app/components/login/login.component.html** to:

`
<ngx-spinner type="ball-scale-multiple"></ngx-spinner>
<div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
<div class="sm:mx-auto sm:w-full sm:max-w-md">
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Supabase Trello</h2>
</div>
<div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
    <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
      <div class="space-y-6" *ngIf="!linkSuccess; else check_mails">
        <div class="space-y-6">
          <label for="email" class="block text-sm font-medium text-gray-700"> Email address </label>
          <div class="mt-1">
            <input
              type="email"
              [(ngModel)]="email"
              autocomplete="email"
              placeholder="john@doe.com"
              class="block w-full rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-emerald-500 focus:outline-none focus:ring-emerald-500 sm:text-sm"
            />
          </div>
        </div>
        <div>
          <button
            (click)="signIn()"
            class="flex w-full justify-center rounded-md border border-transparent bg-emerald-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2"
          >
            Send magic link
          </button>
        </div>
      </div>
      <ng-template #check_mails> Please check your emails! </ng-template>
    </div>
</div>
</div>
`

Once you are done you should have a stylish login page!

![Login](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Flogin.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

When you enter your email and click the button, you should automatically receive an email with a link that will open up your app in the browser again - and this time it should actually forward you to the workspace area immediately.

![Magic Link Email](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fmagic-link-email.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now at this point we could also enter that _internal_ page manually by changing the URL without being authorized, so let's add a mechanism to prevent that.

## Protecting your Pages with a Guard [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#protecting-your-pages-with-a-guard)

In Angular we protect pages with a guard, and because we already keep track of the user in our authentication service it's gonna be super easy to protect pages that only authorized users should see.

Get started by generating a new guard:

`
ng generate guard guards/auth --implements CanActivate
`

That guard will now check the Observable of our service, filter out the initial state and then see if a user is allowed to access a page or not.

Bring up the new **src/app/guards/auth.guard.ts** and change it to this:

`
import { AuthService } from './../services/auth.service'
import { Injectable } from '@angular/core'
import { CanActivate, Router, UrlTree } from '@angular/router'
import { Observable } from 'rxjs'
import { filter, map, take } from 'rxjs/operators'
@Injectable({
providedIn: 'root',
})
export class AuthGuard implements CanActivate {
constructor(
    private auth: AuthService,
    private router: Router
) {}
canActivate(): Observable<boolean | UrlTree> {
    return this.auth.currentUser.pipe(
      filter((val) => val !== null), // Filter out initial Behaviour subject value
      take(1), // Otherwise the Observable doesn't complete!
      map((isAuthenticated) => {
        if (isAuthenticated) {
          return true
        } else {
          return this.router.createUrlTree(['/'])
        }
      })
    )
}
}
`

Now we can apply this guard to all routes that we want to protect, so open up our **src/app/app-routing.module.ts** and add it to the two internal pages we want to protect:

`
import { AuthGuard } from './guards/auth.guard'
import { BoardComponent } from './components/inside/board/board.component'
import { WorkspaceComponent } from './components/inside/workspace/workspace.component'
import { LoginComponent } from './components/login/login.component'
import { NgModule } from '@angular/core'
import { RouterModule, Routes } from '@angular/router'
const routes: Routes = [\
{\
    path: '',\
    component: LoginComponent,\
},\
{\
    path: 'workspace',\
    component: WorkspaceComponent,\
    canActivate: [AuthGuard],\
},\
{\
    path: 'workspace/:id',\
    component: BoardComponent,\
    canActivate: [AuthGuard],\
},\
{\
    path: '**',\
    redirectTo: '/',\
},\
]
@NgModule({
imports: [RouterModule.forRoot(routes, {})],
exports: [RouterModule],
})
export class AppRoutingModule {}
`

Now only signed in users can access those pages, and we can move a step forward to the boards logic.

## Creating the Workspace [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#creating-the-workspace)

Once a user arrives at the workspace page, we want to list all boards of a user and implement the ability to add boards.

To do so, we start off within a service again which takes care of all the interaction between our code and Supabase, so the view can focus on the data presentation.

Our first function will simplye insert an empty object into the `boards` table, which we define as a const so we can't add any typos to our code.

Because we defined a default value for new rows in our SQL in the beginning, we don't have to pass any other data here.

To load all tables of a user could simply query the `user_boards` table, but we might want more information about the related board so we can also [query referenced tables](https://supabase.com/docs/reference/javascript/select?example=query-referenced-tables) to load the board information!

Go ahead and begin the **src/app/services/data.service.ts** with this:

``
import { Injectable } from '@angular/core'
import { SupabaseClient, createClient } from '@supabase/supabase-js'
import { environment } from 'src/environments/environment'
export const BOARDS_TABLE = 'boards'
export const USER_BOARDS_TABLE = 'user_boards'
export const LISTS_TABLE = 'lists'
export const CARDS_TABLE = 'cards'
export const USERS_TABLE = 'users'
@Injectable({
providedIn: 'root',
})
export class DataService {
private supabase: SupabaseClient
constructor() {
    this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)
}
async startBoard() {
    // Minimal return will be the default in the next version and can be removed here!
    return await this.supabase.from(BOARDS_TABLE).insert({}, { returning: 'minimal' })
}
async getBoards() {
    const boards = await this.supabase.from(USER_BOARDS_TABLE).select(`
    boards:board_id ( title, id )
`)
    return boards.data || []
}
}
``

In fact that's enough for our first interaction with our Supabase tables, so we can move on to our view again and load the user boards when the page loads.

Additionally we want to add a board, and here we encounter one of those _real world problems_:

Because we have a **database trigger** that adds an entry when a new table is added, the user is not immediately authorized to access the new board row! Only once the trigger has finished, the RLS that checks user boards can confirm that this user is part of the board.

Therefore we add another line to load the boards again and pop the last added element so we can automatically navigate into its details page.

Now open the **src/app/components/inside/workspace/workspace.component.ts** and change it to:

``
import { AuthService } from './../../../services/auth.service'
import { Router } from '@angular/router'
import { DataService } from './../../../services/data.service'
import { Component, OnInit } from '@angular/core'
@Component({
selector: 'app-workspace',
templateUrl: './workspace.component.html',
styleUrls: ['./workspace.component.scss'],
})
export class WorkspaceComponent implements OnInit {
boards: any[] = []
user = this.auth.currentUser
constructor(
    private dataService: DataService,
    private router: Router,
    private auth: AuthService
) {}
async ngOnInit() {
    this.boards = await this.dataService.getBoards()
}
async startBoard() {
    const data = await this.dataService.startBoard()
    // Load all boards because we only get back minimal data
    // Trigger needs to run first
    // Otherwise RLS would fail
    this.boards = await this.dataService.getBoards()
    if (this.boards.length > 0) {
      const newBoard = this.boards.pop()
      if (newBoard.boards) {
        this.router.navigateByUrl(`/workspace/${newBoard.boards.id}`)
      }
    }
}
signOut() {
    this.auth.logout()
}
}
``

To display all of this we build up another view with Tailwind and also use the Gravatar package to display a little image of the current user based on the email.

Besides that we simply iterate all boards, add the router link to a board based on the ID and add a button to create new boards, so bring up the **src/app/components/inside/workspace/workspace.component.html** and change it to:

`
<header class="bg-emerald-600">
<nav class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div
      class="flex w-full items-center justify-between border-b border-emerald-500 py-6 lg:border-none"
    >
      <div class="flex items-center">
        <a routerLink="/workspace">
          <img class="h-6 w-auto" src="https://supabase.com/docs/supabase-dark.svg" alt="" />
        </a>
      </div>
      <div class="ml-10 flex items-center space-x-4">
        <span class="text-white">{{ (user | async)?.email }}</span>
        <img ngxGravatar [email]="(user | async)?.email" />
        <button
          (click)="signOut()"
          class="inline-block rounded-md border border-transparent bg-white py-1 px-4 text-base font-medium text-emerald-600 hover:bg-emerald-50"
        >
          Logout
        </button>
      </div>
    </div>
</nav>
</header>
<main class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
<ul
    role="list"
    class="grid grid-cols-2 gap-x-4 gap-y-8 sm:grid-cols-3 sm:gap-x-6 lg:grid-cols-4 xl:gap-x-8"
>
    <li
      *ngFor="let board of boards"
      [routerLink]="board.boards.id"
      class="relative h-52 rounded bg-emerald-200 py-4 px-4 text-lg font-semibold hover:cursor-pointer hover:bg-emerald-300"
    >
      {{ board.boards.title }}
    </li>
    <li
      (click)="startBoard()"
      class="relative h-52 rounded bg-emerald-500 py-4 px-4 text-lg font-semibold hover:cursor-pointer"
    >
      + New board
    </li>
</ul>
</main>
`

At this point we have a functional board logic and actually already route to the following details page.

![Workspace page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fworkspace.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The logout functionality will also remove our session and guide us back to the login, so we have covered that flow at the same time already.

Time for some more interaction with our Supabase tables!

## Adding CRUD Functions for the Database [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#adding-crud-functions-for-the-database)

On our board details page we now need to interact with all the tables and mostly perform CRUD functionality - Create, read, update or delete records of our database.

Since there's no real value in discussing every line, let's quickly add the following bunch of functions to our **src/app/services/data.service.ts**:

`
// CRUD Board
async getBoardInfo(boardId: string) {
    return await this.supabase
      .from(BOARDS_TABLE)
      .select('*')
      .match({ id: boardId })
      .single();
}
async updateBoard(board: any) {
    return await this.supabase
      .from(BOARDS_TABLE)
      .update(board)
      .match({ id: board.id });
}
async deleteBoard(board: any) {
    return await this.supabase
      .from(BOARDS_TABLE)
      .delete()
      .match({ id: board.id });
}
// CRUD Lists
async getBoardLists(boardId: string) {
    const lists = await this.supabase
      .from(LISTS_TABLE)
      .select('*')
      .eq('board_id', boardId)
      .order('position');
    return lists.data || [];
}
async addBoardList(boardId: string, position = 0) {
    return await this.supabase
      .from(LISTS_TABLE)
      .insert({ board_id: boardId, position, title: 'New List' })
      .select('*')
      .single();
}
async updateBoardList(list: any) {
    return await this.supabase
      .from(LISTS_TABLE)
      .update(list)
      .match({ id: list.id });
}
async deleteBoardList(list: any) {
    return await this.supabase
      .from(LISTS_TABLE)
      .delete()
      .match({ id: list.id });
}
// CRUD Cards
async addListCard(listId: string, boardId: string, position = 0) {
    return await this.supabase
      .from(CARDS_TABLE)
      .insert(
        { board_id: boardId, list_id: listId, position }
      )
      .select('*')
      .single();
}
async getListCards(listId: string) {
    const lists = await this.supabase
      .from(CARDS_TABLE)
      .select('*')
      .eq('list_id', listId)
      .order('position');
    return lists.data || [];
}
async updateCard(card: any) {
    return await this.supabase
      .from(CARDS_TABLE)
      .update(card)
      .match({ id: card.id });
}
async deleteCard(card: any) {
    return await this.supabase
      .from(CARDS_TABLE)
      .delete()
      .match({ id: card.id });
}
`

Most if not all of this is basic SQL as described in the [Supabase docs for Database](https://supabase.com/docs/reference/javascript/select)

One additional function is missing, and that's a simple invitation logic. However we gonna skip the "Ok I want to join this board" step and simply add invited users to a new board. Sometimes users need to be forced to do what's good for them.

Therfore we will try to find the user ID of a user based on the entered email, and if it exists we will create a new entry in the `user_boards` table for that user:

`
// Invite others
async addUserToBoard(boardId: string, email: string) {
    const user = await this.supabase
      .from(USERS_TABLE)
      .select('id')
      .match({ email })
      .single();
    if (user.data?.id) {
      const userId = user.data.id;
      const userBoard = await this.supabase.from(USER_BOARDS_TABLE).insert({
        user_id: userId,
        board_id: boardId,
      });
      return userBoard;
    } else {
      return null;
    }
}
`

With those functions in place I think we are more than ready to create a powerful board page.

## Creating the Boards View [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#creating-the-boards-view)

This page is the most essential and most challenging part of our app, as it's the place where the actual work happens and users collaborate on boards.

However, we will begin by setting up the basic stuff and introduce **realtime functionality and presence** in a separate step afterwards.

Because it would be tedious to split the page into multiple code snippets we'll go with one big and I'll explain what's going on:

- We first need to load some general board info like the title using `getBoardInfo()` and the passed ID of the board
- We then need to load all **lists** of a board using `getBoardLists()`
- We then need to load every **card** for every list using `getListCards()`

To keep track of data and changes we hold all cards in the `listCards` object that stores all cards under the related list ID key.

In terms of additional logic we might want to update or delete the board, which we can do simply with the previously created service functions.

Same is true for lists and cards, which can be added, updated or removed.

However, this will not (yet) update our local data, since we want to implement this with realtime updates later.

For now go ahead and change the **src/app/components/inside/board/board.component.ts** to:

`
import { DataService } from './../../../services/data.service'
import { Component, HostListener, OnInit } from '@angular/core'
import { ActivatedRoute, Router } from '@angular/router'
@Component({
selector: 'app-board',
templateUrl: './board.component.html',
styleUrls: ['./board.component.scss'],
})
export class BoardComponent implements OnInit {
lists: any[] = []
boardId: string | null = null
editTitle: any = {}
editCard: any = {}
boardInfo: any = null
titleChanged = false
listCards: any = {}
addUserEmail = ''
constructor(
    private route: ActivatedRoute,
    private dataService: DataService,
    private router: Router
) {}
async ngOnInit() {
    this.boardId = this.route.snapshot.paramMap.get('id')
    if (this.boardId) {
      // Load general board information
      const board = await this.dataService.getBoardInfo(this.boardId)
      this.boardInfo = board.data
      // Retrieve all lists
      this.lists = await this.dataService.getBoardLists(this.boardId)
      // Retrieve cards for each list
      for (let list of this.lists) {
        this.listCards[list.id] = await this.dataService.getListCards(list.id)
      }
      // For later...
      this.handleRealtimeUpdates()
    }
}
//
// BOARD logic
//
async saveBoardTitle() {
    await this.dataService.updateBoard(this.boardInfo)
    this.titleChanged = false
}
async deleteBoard() {
    await this.dataService.deleteBoard(this.boardInfo)
    this.router.navigateByUrl('/workspace')
}
//
// LISTS logic
//
async addList() {
    const newList = await this.dataService.addBoardList(this.boardId!, this.lists.length)
}
editingTitle(list: any, edit = false) {
    this.editTitle[list.id] = edit
}
async updateListTitle(list: any) {
    await this.dataService.updateBoardList(list)
    this.editingTitle(list, false)
}
async deleteBoardList(list: any) {
    await this.dataService.deleteBoardList(list)
}
//
// CARDS logic
//
async addCard(list: any) {
    await this.dataService.addListCard(list.id, this.boardId!, this.listCards[list.id].length)
}
editingCard(card: any, edit = false) {
    this.editCard[card.id] = edit
}
async updateCard(card: any) {
    await this.dataService.updateCard(card)
    this.editingCard(card, false)
}
async deleteCard(card: any) {
    await this.dataService.deleteCard(card)
}
// Invites
async addUser() {
    await this.dataService.addUserToBoard(this.boardId!, this.addUserEmail)
    this.addUserEmail = ''
}
handleRealtimeUpdates() {
    // TODO
}
}
`

That was a massive file - make sure you take the time to go through it at least once or twice to better understand the differetn functions we added.

Now we need to tackle the view of that page, and because it's Tailwind the snippets won't be shorter.

We can begin with the easier part, which is the header area that displays a back button, the board information that can be updated on click and a delete button to well, you know what.

Bring up the **src/app/components/inside/board/board.component.html** and add this first:

`
<header class="bg-emerald-600">
<nav class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div
      class="flex w-full items-center justify-between border-b border-emerald-500 py-6 lg:border-none"
    >
      <div class="flex items-center">
        <a routerLink="/workspace" class="font-semibold text-emerald-900"> < Back </a>
      </div>
      <div class="flex gap-4">
        <input
          *ngIf="boardInfo"
          (ngModelChange)="titleChanged = true"
          class="ml-10 space-x-4 bg-emerald-600 font-bold text-white"
          [(ngModel)]="boardInfo.title"
        />
        <button class="font-medium" *ngIf="titleChanged" (click)="saveBoardTitle()">Save</button>
      </div>
      <div class="flex">
        <button class="text-small font-medium text-red-700" (click)="deleteBoard()">
          Delete board
        </button>
      </div>
    </div>
</nav>
</header>
`

Since we will have more of these update input fields later, let's quickly add a col `HostListener` to our app so we can detect at least the ESC key event and then close all of those edit input fields in our **src/app/components/inside/board/board.component.ts**

`
@HostListener('document:keydown', ['$event']) onKeydownHandler(
    event: KeyboardEvent
) {
    if (event.keyCode === 27) {
      // Close whatever needs to be closed!
      this.titleChanged = false;
      Object.keys(this.editCard).map((item) => {
        this.editCard[item] = false;
        return item;
      });
      Object.keys(this.editTitle).map((item) => {
        this.editTitle[item] = false;
        return item;
      });
    }
}
`

Finally we need to iterate all lists, and for every list display all cards.

Actually a pretty simple task, but since we need more buttons to control the elements so we can delete, add and update them to whole code becomes a bit more bloated.

Nonetheless we can continue below the previous code in our **src/app/components/inside/board/board.component.html** and add this:

`
<main class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
<div class="grid grid-cols-2 gap-x-4 gap-y-8 sm:grid-cols-3 sm:gap-x-6 lg:grid-cols-4 xl:gap-x-8">
    <!-- ITERATE ALL LISTS -->
    <div
      *ngFor="let list of lists"
      class="min-h-52 relative h-auto rounded bg-emerald-200 py-4 px-4 text-sm font-semibold"
    >
      <div class="flex gap-2 pb-4">
        <p
          (click)="editingTitle(list, true)"
          class="hover:cursor-pointer"
          *ngIf="!editTitle[list.id]"
        >
          {{ list.title }}
        </p>
        <input
          [(ngModel)]="list.title"
          *ngIf="editTitle[list.id]"
          class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-emerald-500 focus:outline-none focus:ring-emerald-500 sm:text-sm"
        />
        <button class="font-medium" *ngIf="editTitle[list.id]" (click)="updateListTitle(list)">
          Save
        </button>
      </div>
      <!-- ITERATE LIST CARDS -->
      <div class="flex flex-col items-center gap-2">
        <div
          class="flex h-auto w-full flex-col gap-2 hover:cursor-pointer"
          *ngFor="let card of listCards[list.id]"
          (click)="editingCard(card, true)"
        >
          <p class="h-10 bg-white py-2 px-2" *ngIf="!editCard[card.id]">{{ card.title }}</p>
          <input
            [(ngModel)]="card.title"
            *ngIf="editCard[card.id]"
            class="block rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-emerald-500 focus:outline-none focus:ring-emerald-500 sm:text-sm"
          />
          <div class="align-items-center flex justify-between">
            <button class="font-medium" *ngIf="editCard[card.id]" (click)="updateCard(card)">
              Update
            </button>
            <button
              class="font-medium text-red-600"
              *ngIf="editCard[card.id]"
              (click)="deleteCard(card)"
            >
              Delete
            </button>
          </div>
        </div>
        <div (click)="addCard(list)" class="pt-8 text-gray-500 hover:cursor-pointer">
          + Add a card
        </div>
        <button class="text-small font-medium text-red-700" (click)="deleteBoardList(list)">
          Delete list
        </button>
      </div>
    </div>
    <div
      (click)="addList()"
      class="relative h-16 rounded bg-emerald-500 py-4 px-4 text-lg font-semibold hover:cursor-pointer"
    >
      + New list
    </div>
</div>
</main>
`

At this point we are able to add a list, add a new card in that list and finally update or delete all of that!

![Board functionality](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Most of this won't update the view since we will handle this with realtime updates in a minute, so you need to refresh your page after adding a card or list right now!

But we can actually already add our invitation logic, which just needs another input field so we can invite another email to work with us on the board.

Add the following in the `<main>` tag of our **src/app/components/inside/board/board.component.html** at the bottom:

`
<div class="flex items-center gap-4 py-12">
<span class="block text-3xl font-extrabold text-gray-900">Invite</span>
<input
    [(ngModel)]="addUserEmail"
    placeholder="john@doe.com"
    class="block rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-emerald-500 focus:outline-none focus:ring-emerald-500 sm:text-sm"
/>
<button
    (click)="addUser()"
    class="inline-flex items-center rounded border border-transparent bg-emerald-600 px-2.5 py-1.5 text-xs font-medium text-white shadow-sm hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2"
>
    Invite
</button>
</div>
`

The required function in our class and service already exists, so you can now already invite other users (who are already signed up!) and from their account see the same board as you have.

## Handling Realtime Table Changes [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#handling-realtime-table-changes)

The cool thing is is how easy we are now able to implement real time functionality - the only thing required for this is to turn it on.

We can do this right inside the table editor of Supabase, so go to your tables, click that little arrow next to edi so you can edit the table and then enable realtime for bot **cards** and **lists**!

![Supabase Realtime](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimon-grimm-angular-realtime%2Fsupabase-realtime.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now we are able to retrieve those updates if we listen for them, and while the API for this might slightly change with the next Supabase JS update, the general idea can still be applied:

We create a new `Subject` and return it as an `Observable`, and then listen to changes of our tables by using `on()`.

Whenever we get an update, we emit that change to the Subject so we have one stream of updates that we can return to our view.

To continue, bring up the **src/app/services/data.service.ts** and add this additional function:

`
getTableChanges() {
    const changes = new Subject();
    this.supabase
      .from(CARDS_TABLE)
      .on('*', (payload: any) => {
        changes.next(payload);
      })
      .subscribe();
    this.supabase
      .from(LISTS_TABLE)
      .on('*', (payload: any) => {
        changes.next(payload);
      })
      .subscribe();
    return changes.asObservable();
}
`

Now that we can easily get all the updates to our relevant tables in realtime, we just need to handle them accordingly.

This is just a matter of finding out which **event** occurred (INSERT, UPDATE, DELETE) and then applying the changes to our local data to add, change or remove data.

Go ahead by finally implementing our function in the **src/app/components/inside/board/board.component.ts** that we left open until now:

`
handleRealtimeUpdates() {
    this.dataService.getTableChanges().subscribe((update: any) => {
      const record = update.new?.id ? update.new : update.old;
      const event = update.eventType;
      if (!record) return;
      if (update.table == 'cards') {
        if (event === 'INSERT') {
          this.listCards[record.list_id].push(record);
        } else if (event === 'UPDATE') {
          const newArr = [];
          for (let card of this.listCards[record.list_id]) {
            if (card.id == record.id) {
              card = record;
            }
            newArr.push(card);
          }
          this.listCards[record.list_id] = newArr;
        } else if (event === 'DELETE') {
          this.listCards[record.list_id] = this.listCards[\
            record.list_id\
          ].filter((card: any) => card.id !== record.id);
        }
      } else if (update.table == 'lists') {
        // TODO
      }
    });
}
`

This handles the events if the table of our event is **cards**, buzt the second part is somewhat similar.

I simply put the code for the `else` case in a second block, to not make the first handling look that big - but it's pretty much the same logic of handling the different cases and now updating everything related to **lists**:

`
else if (update.table == 'lists') {
if (event === 'INSERT') {
    this.lists.push(record);
    this.listCards[record.id] = [];
} else if (event === 'UPDATE') {
    this.lists.filter((list: any) => list.id === record.id)[0] = record;
    const newArr = [];
    for (let list of this.lists) {
      if (list.id == record.id) {
        list = record;
      }
      newArr.push(list);
    }
    this.lists = newArr;
} else if (event === 'DELETE') {
    this.lists = this.lists.filter((list: any) => list.id !== record.id);
}
}
`

With that final piece of code we are completely done with our Supabase Angular Trello clone, and you can enjoy the fruits of your hard work!

## Conclusion [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#conclusion)

Building projects with Supabase is awesome, and hopefully this real world clone example gave you insight into different areas that you need to think about.

You can [find the full code of this tutorial on Github](https://github.com/saimon24/supabase-trello-angular) where you just need to insert your own Supabase instance and then create the tables with the included SQL file.

If you enjoyed the tutorial, you can [find many more tutorials on my YouTube channel](https://www.youtube.com/simongrimmdev_) where I help web developers build awesome mobile apps.

Until next time and happy coding with Supabase!

## Resources [\#](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular\#resources)

- [Quickstart: Angular](https://supabase.com/docs/guides/with-angular)
- [Authentication in Ionic Angular with Supabase](https://supabase.com/blog/authentication-in-ionic-angular)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-a-realtime-trello-board-with-supabase-and-angular&text=Building%20a%20Realtime%20Trello%20Board%20with%20Supabase%20and%20Angular)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-a-realtime-trello-board-with-supabase-and-angular&text=Building%20a%20Realtime%20Trello%20Board%20with%20Supabase%20and%20Angular)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-a-realtime-trello-board-with-supabase-and-angular&t=Building%20a%20Realtime%20Trello%20Board%20with%20Supabase%20and%20Angular)

[Last post\\
\\
**Launch Week 5 Hackathon Winners** \\
\\
25 August 2022](https://supabase.com/blog/launch-week-5-hackathon-winners)

[Next post\\
\\
**Community Day** \\
\\
19 August 2022](https://supabase.com/blog/launch-week-5-community-day)

[angular](https://supabase.com/blog/tags/angular) [realtime](https://supabase.com/blog/tags/realtime) [community](https://supabase.com/blog/tags/community)

On this page

- [Creating the Supabase Project](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#creating-the-supabase-project)
- [Defining your Tables with SQL](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#defining-your-tables-with-sql)
- [Creating the Angular Project](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#creating-the-angular-project)
- [Adding Tailwind for Styling](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#adding-tailwind-for-styling)
- [Building a Magic Link Sign In](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#building-a-magic-link-sign-in)
- [Protecting your Pages with a Guard](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#protecting-your-pages-with-a-guard)
- [Creating the Workspace](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#creating-the-workspace)
- [Adding CRUD Functions for the Database](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#adding-crud-functions-for-the-database)
- [Creating the Boards View](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#creating-the-boards-view)
- [Handling Realtime Table Changes](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#handling-realtime-table-changes)
- [Conclusion](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#conclusion)
- [Resources](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular#resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-a-realtime-trello-board-with-supabase-and-angular&text=Building%20a%20Realtime%20Trello%20Board%20with%20Supabase%20and%20Angular)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-a-realtime-trello-board-with-supabase-and-angular&text=Building%20a%20Realtime%20Trello%20Board%20with%20Supabase%20and%20Angular)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-a-realtime-trello-board-with-supabase-and-angular&t=Building%20a%20Realtime%20Trello%20Board%20with%20Supabase%20and%20Angular)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)