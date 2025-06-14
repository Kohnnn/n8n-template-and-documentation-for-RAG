---
url: "https://supabase.com/blog/flutter-tutorial-building-a-chat-app"
title: "Flutter Tutorial: building a Flutter chat app"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Flutter Tutorial: building a Flutter chat app

30 Jun 2022

•

39 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Flutter Tutorial: building a Flutter chat app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Fflutter-chat-app.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This is the first of a series of Flutter Tutorials. During the series, you will learn how to build cross-platform apps without worrying about the backend.

In the first part, I will show you how to build a chat application, where users can sign up and talk to other users in a single chat room. The exchange of messages will happen in real time, meaning that you do not have to refresh the page to load new messages.

In the second part, I will show you how to implement [Authentication and Authorization (with RLS)](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls) to the chat app.

In order to build this chat app, we will need a database to store all of the chat information. We will be using [Supabase](https://supabase.com/) to store the chat information. Supabase is a back end as a service that provides auth, database, storage and functions to easily create a scalable application. Supabase is a suitable backend for this app, because it provides a nice set of APIs on Postgres database that we can easily call by using the SDK. It is also perfect for chat apps like the one we are about to create, because we can subscribe to real time changes on the database.

This article also assumes that you have installed Flutter already on your machine. If not, you can go to the [official Flutter page](https://docs.flutter.dev/get-started/install) to start the installation.

You can find the complete version of this app in [this](https://github.com/supabase-community/flutter-chat) Github repository.

## Overview of the final chat app [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#overview-of-the-final-chat-app)

The application we are creating today is a simple real time chat application. Users can sign up/ sign in using email and password. Once they are in, they can read and send messages to a shared room across all users of the application. Because we are using Flutter, the app can run on iOS, Android, or on the web.

![chat app running on ios, android and web](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Fchat-app-screenshot.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Techstack will be fairly simple. We have Flutter on the frontend, Supabase on the backend and that is it! Since Supabase provides nice APIs to access the Postgres database, we don't need to create our own. We will access Supabase through the [supabase\_flutter package](https://pub.dev/packages/supabase_flutter), which provides an intuitive way of reading and writing data to the database.

![architecture diagram of the chat app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Farchitecture-diagram.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Setting up the scene [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#setting-up-the-scene)

### Create a blank Flutter application [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#create-a-blank-flutter-application)

We will start out by creating an empty Flutter project.

First, open your terminal and type

`
flutter create my_chat_app
`

Once it is done, you can go into your app and run it.

`
cd my_chat_app
flutter run
`

You should be able to now see the default counter app that every Flutter project starts with. With that, let's open the app in your favorite code editor and get started with coding!

### Install dependencies [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#install-dependencies)

Open pubspec.yaml file and let's install a few dependencies of this app.

`
supabase_flutter: ^1.0.0
timeago: ^3.1.0
`

`supabase_flutter` will provide us easy access to our Postgres database hosted on Supabase. `timeago` is a simple library that takes a `DateTime` and returns nice strings displaying how long ago the time was. This will be used to display the timestamps of each chat bubble.

Run `flutter pub get` to install the packages. Note that you will have to terminate `flutter run` and re-run it again after this package installation.

### Creating a new Supabase project [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#creating-a-new-supabase-project)

If you do not have a Supabase account yet, do not worry, you can [get started for free](https://supabase.com/dashboard/).

You will be prompted to sign in using your Github account with a big green button, so let's go ahead and press it. Proceed with the sign up process and once you are done, you will be taken to a list of projects. You can go ahead and create a new project by pressing the “New Project” button at the top.

![Create new Supabase project](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Fcreate-new-supabase-project.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You will be entering a few things here like the name of the project. You can call it “chat” for now. For the database password, go ahead and hit the “Generate a password” button to generate a random password. We won't use this password in this app, but if you ever need it, you can always override it later to whatever you want it to be. You can leave the pricing plan for free as Supabase has a very generous Free Plan that will be way more than enough for our chat app. Once you have entered everything, you can press the “Create new Project” button. Spinning up a brand new Supabase project could take a few minutes.

Once your project is ready, we can dive into setting up our project!

### Setting up tables in Supabase [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#setting-up-tables-in-supabase)

Once your project is ready, we can dive into setting up our project!

In order to create the chat app, we will create 2 tables.

- profiles - stores user profile data
- messages - contains the contents of each message along with who sent it.

Each message is associated with one profile to represent who posted the message.

![we will create profiles and messages tables](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Fentity-relations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can run the following SQL in your SQL editor of your Supabase dashboard.

![we will create profiles and messages tables](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Fsql-editor.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

`
create table if not exists public.profiles (
    id uuid references auth.users on delete cascade not null primary key,
    username varchar(24) not null unique,
    created_at timestamp with time zone default timezone('utc' :: text, now()) not null,
    -- username should be 3 to 24 characters long containing alphabets, numbers and underscores
    constraint username_validation check (username ~* '^[A-Za-z0-9_]{3,24}$')
);
comment on table public.profiles is 'Holds all of users profile information';
create table if not exists public.messages (
    id uuid not null primary key default gen_random_uuid(),
    profile_id uuid default auth.uid() references public.profiles(id) on delete cascade not null,
    content varchar(500) not null,
    created_at timestamp with time zone default timezone('utc' :: text, now()) not null
);
comment on table public.messages is 'Holds individual messages sent on the app.';
`

After running the SQL, you should see the tables in your table editor on your Supabase dashboard. You can click any of the tables to view the stored data, note that all of the tables should be empty at this point.

![profiles and messages table will be viewable from table editor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Ftable-editor.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase allows us to listen to real time changes on the database with additional configuration. We want to enable real time on our `messages` table, so that we can display the chats when new data is added. Go back to SQL editor and run the following SQL to enable real time for `messages`.

`
-- *** Add tables to the publication to enable real time subscription ***
alter publication supabase_realtime add table public.messages;
`

Now that we have defined what our data looks like, let’s have some fun writing Flutter code!

## Building the Flutter chat application [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#building-the-flutter-chat-application)

### Step 1: Define constants that to be used throughout the application [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#step-1-define-constants-that-to-be-used-throughout-the-application)

We will start out by creating a constants.dart file and define a few constants that will make things easier down the line. We will use the supabase variable to access our database and auth features.

`
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
/// Supabase client
final supabase = Supabase.instance.client;
/// Simple preloader inside a Center widget
const preloader =
    Center(child: CircularProgressIndicator(color: Colors.orange));
/// Simple sized box to space out form elements
const formSpacer = SizedBox(width: 16, height: 16);
/// Some padding for all the forms to use
const formPadding = EdgeInsets.symmetric(vertical: 20, horizontal: 16);
/// Error message to display the user when unexpected error occurs.
const unexpectedErrorMessage = 'Unexpected error occurred.';
/// Basic theme to change the look and feel of the app
final appTheme = ThemeData.light().copyWith(
primaryColorDark: Colors.orange,
appBarTheme: const AppBarTheme(
    elevation: 1,
    backgroundColor: Colors.white,
    iconTheme: IconThemeData(color: Colors.black),
    titleTextStyle: TextStyle(
      color: Colors.black,
      fontSize: 18,
    ),
),
primaryColor: Colors.orange,
textButtonTheme: TextButtonThemeData(
    style: TextButton.styleFrom(
      foregroundColor: Colors.orange,
    ),
),
elevatedButtonTheme: ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      foregroundColor: Colors.white,
      backgroundColor: Colors.orange,
    ),
),
inputDecorationTheme: InputDecorationTheme(
    floatingLabelStyle: const TextStyle(
      color: Colors.orange,
    ),
    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(12),
      borderSide: const BorderSide(
        color: Colors.grey,
        width: 2,
      ),
    ),
    focusColor: Colors.orange,
    focusedBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(12),
      borderSide: const BorderSide(
        color: Colors.orange,
        width: 2,
      ),
    ),
),
);
/// Set of extension methods to easily display a snackbar
extension ShowSnackBar on BuildContext {
/// Displays a basic snackbar
void showSnackBar({
    required String message,
    Color backgroundColor = Colors.white,
}) {
    ScaffoldMessenger.of(this).showSnackBar(SnackBar(
      content: Text(message),
      backgroundColor: backgroundColor,
    ));
}
/// Displays a red snackbar indicating error
void showErrorSnackBar({required String message}) {
    showSnackBar(message: message, backgroundColor: Colors.red);
}
}
`

### Step 2: Initialize Supabase [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#step-2-initialize-supabase)

In order to use Supabase, we need to [initialize](https://supabase.com/docs/reference/dart/initializing#flutter-initialize) it at the top of the main function. Let’s edit the main.dart file so that we can initialize Supabase. Note that within the build method of MyApp, we are loading the theme data created in the `constants.dart` file and the home is set to SplashPage(), which we will create in later sections.

You can find your Supabase URL and Supabase anon key under settings -> API in your dashboard.

![Location of your Supabase credentials](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Fsupabase-credentials.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

`
import 'package:flutter/material.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:my_chat_app/pages/splash_page.dart';
Future<void> main() async {
WidgetsFlutterBinding.ensureInitialized();
await Supabase.initialize(
    // TODO: Replace credentials with your own
    url: 'SUPABASE_URL',
    anonKey: 'SUPABASE_ANON_KEY',
);
runApp(const MyApp());
}
class MyApp extends StatelessWidget {
const MyApp({Key? key}) : super(key: key);
@override
Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'My Chat App',
      theme: appTheme,
      home: const SplashPage(),
    );
}
}
`

### Step 3: Redirect users depending on auth state using splash page [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#step-3-redirect-users-depending-on-auth-state-using-splash-page)

When a user launches the app, we want to redirect those who have already signed in to the Chat page and those who have not signed in yet to the register page.
In order to achieve this, we will create a splash page, which is just a page with a preloader at the middle from the user, but takes care of fetching auth state and redirects users accordingly behind the scenes.
Within the `_redirect()` method, we are fetching the auth state and navigating the user accordingly.

`
import 'package:flutter/material.dart';
import 'package:my_chat_app/pages/chat_page.dart';
import 'package:my_chat_app/pages/register_page.dart';
import 'package:my_chat_app/utils/constants.dart';
/// Page to redirect users to the appropriate page depending on the initial auth state
class SplashPage extends StatefulWidget {
const SplashPage({Key? key}) : super(key: key);
@override
SplashPageState createState() => SplashPageState();
}
class SplashPageState extends State<SplashPage> {
@override
void initState() {
    super.initState();
    _redirect();
}
Future<void> _redirect() async {
    // await for for the widget to mount
    await Future.delayed(Duration.zero);
    final session = supabase.auth.currentSession;
    if (session == null) {
      Navigator.of(context)
          .pushAndRemoveUntil(RegisterPage.route(), (route) => false);
    } else {
      Navigator.of(context)
          .pushAndRemoveUntil(ChatPage.route(), (route) => false);
    }
}
@override
Widget build(BuildContext context) {
    return const Scaffold(body: preloader);
}
}
`

### Step 4 : Define data models to be used within the app [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#step-4--define-data-models-to-be-used-within-the-app)

We need to create data model classes that we will use within our app. We will map the tables we had creating Profile and Message class. They will also contain a fromMap constructor to easily create them from the return value of Supabase.

`
class Profile {
Profile({
    required this.id,
    required this.username,
    required this.createdAt,
});
/// User ID of the profile
final String id;
/// Username of the profile
final String username;
/// Date and time when the profile was created
final DateTime createdAt;
Profile.fromMap(Map<String, dynamic> map)
      : id = map['id'],
        username = map['username'],
        createdAt = DateTime.parse(map['created_at']);
}
`

`
class Message {
Message({
    required this.id,
    required this.profileId,
    required this.content,
    required this.createdAt,
    required this.isMine,
});
/// ID of the message
final String id;
/// ID of the user who posted the message
final String profileId;
/// Text content of the message
final String content;
/// Date and time when the message was created
final DateTime createdAt;
/// Whether the message is sent by the user or not.
final bool isMine;
Message.fromMap({
    required Map<String, dynamic> map,
    required String myUserId,
})  : id = map['id'],
        profileId = map['profile_id'],
        content = map['content'],
        createdAt = DateTime.parse(map['created_at']),
        isMine = myUserId == map['profile_id'];
}
`

### Step 5: Create register page with email, password and username [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#step-5-create-register-page-with-email-password-and-username)

Now that we have defined a few handy constants, it is time to dive into creating pages.
The first page we will create is the register page.
This page will take an email address, password, and username within a form widget.
The username will be the primary identifier when users search for other users within the app.
Once a user performs registration, they will be taken to the chat page. Let's create a `lib/pages/register_page.dart` file and paste the following code.

`
import 'package:flutter/material.dart';
import 'package:my_chat_app/pages/chat_page.dart';
import 'package:my_chat_app/pages/login_page.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class RegisterPage extends StatefulWidget {
const RegisterPage({Key? key, required this.isRegistering}) : super(key: key);
static Route<void> route({bool isRegistering = false}) {
    return MaterialPageRoute(
      builder: (context) => RegisterPage(isRegistering: isRegistering),
    );
}
final bool isRegistering;
@override
State<RegisterPage> createState() => _RegisterPageState();
}
class _RegisterPageState extends State<RegisterPage> {
final bool _isLoading = false;
final _formKey = GlobalKey<FormState>();
final _emailController = TextEditingController();
final _passwordController = TextEditingController();
final _usernameController = TextEditingController();
Future<void> _signUp() async {
    final isValid = _formKey.currentState!.validate();
    if (!isValid) {
      return;
    }
    final email = _emailController.text;
    final password = _passwordController.text;
    final username = _usernameController.text;
    try {
      await supabase.auth.signUp(
          email: email, password: password, data: {'username': username});
      Navigator.of(context)
          .pushAndRemoveUntil(ChatPage.route(), (route) => false);
    } on AuthException catch (error) {
      context.showErrorSnackBar(message: error.message);
    } catch (error) {
      context.showErrorSnackBar(message: unexpectedErrorMessage);
    }
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Register'),
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: formPadding,
          children: [\
            TextFormField(\
              controller: _emailController,\
              decoration: const InputDecoration(\
                label: Text('Email'),\
              ),\
              validator: (val) {\
                if (val == null || val.isEmpty) {\
                  return 'Required';\
                }\
                return null;\
              },\
              keyboardType: TextInputType.emailAddress,\
            ),\
            formSpacer,\
            TextFormField(\
              controller: _passwordController,\
              obscureText: true,\
              decoration: const InputDecoration(\
                label: Text('Password'),\
              ),\
              validator: (val) {\
                if (val == null || val.isEmpty) {\
                  return 'Required';\
                }\
                if (val.length < 6) {\
                  return '6 characters minimum';\
                }\
                return null;\
              },\
            ),\
            formSpacer,\
            TextFormField(\
              controller: _usernameController,\
              decoration: const InputDecoration(\
                label: Text('Username'),\
              ),\
              validator: (val) {\
                if (val == null || val.isEmpty) {\
                  return 'Required';\
                }\
                final isValid = RegExp(r'^[A-Za-z0-9_]{3,24}$').hasMatch(val);\
                if (!isValid) {\
                  return '3-24 long with alphanumeric or underscore';\
                }\
                return null;\
              },\
            ),\
            formSpacer,\
            ElevatedButton(\
              onPressed: _isLoading ? null : _signUp,\
              child: const Text('Register'),\
            ),\
            formSpacer,\
            TextButton(\
              onPressed: () {\
                Navigator.of(context).push(LoginPage.route());\
              },\
              child: const Text('I already have an account'),\
            )\
          ],
        ),
      ),
    );
}
}
`

If you look at the validator function of the username field, you notice that we are enforcing the same regular expression check as what we defined in our table definition of profiles.

If you take a closer look at the `_signup()` method, you notice that the username is passed as a `data`.
By passing `data` to your sign up method, you can populate the meta data field of your authenticated users.
We will need to copy this username into our profiles table so that other users can find you.
In order to do this, we will utilize a [Postgres function](https://supabase.com/docs/guides/database/functions) and Postgres trigger.
Run the following SQL to create a Postgres function that will automatically run when a new user signs up to our application.
Since we have set a unique constraint on the username column of our profiles table, the sign up will fail if a user chooses a username that is already taken.

``
-- Function to create a new row in profiles table upon signup
-- Also copies the username value from metadata
create or replace function handle_new_user() returns trigger as $$
    begin
        insert into public.profiles(id, username)
        values(new.id, new.raw_user_meta_data->>'username');
        return new;
    end;
$$ language plpgsql security definer;
-- Trigger to call `handle_new_user` when new user signs up
create trigger on_auth_user_created
    after insert on auth.users
    for each row
    execute function handle_new_user();
``

Also, Supabase has email confirmation turned on by default, meaning that every time someone signs up, they have to click the confirmation link they receive in their email.
This is ideal for a production app, but for our sample app, we can turn it off since we want to get up and running with building a functioning chat app.
We will cover secure authentications using Supabase in later articles.
Go to authentication → settings and turn off the switch of `Enable email confirmations`.

![turn off email confirmation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat%2Fturn-off-email-confirmation.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Step 6: Create login page [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#step-6-create-login-page)

Login page will also be a simple page with an email and password field.
Once they have signed in, the user will be taken to the rooms page.

`
import 'package:flutter/material.dart';
import 'package:my_chat_app/pages/chat_page.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class LoginPage extends StatefulWidget {
const LoginPage({Key? key}) : super(key: key);
static Route<void> route() {
    return MaterialPageRoute(builder: (context) => const LoginPage());
}
@override
_LoginPageState createState() => _LoginPageState();
}
class _LoginPageState extends State<LoginPage> {
bool _isLoading = false;
final _emailController = TextEditingController();
final _passwordController = TextEditingController();
Future<void> _signIn() async {
    setState(() {
      _isLoading = true;
    });
    try {
      await supabase.auth.signInWithPassword(
        email: _emailController.text,
        password: _passwordController.text,
      );
      Navigator.of(context)
          .pushAndRemoveUntil(ChatPage.route(), (route) => false);
    } on AuthException catch (error) {
      context.showErrorSnackBar(message: error.message);
    } catch (_) {
      context.showErrorSnackBar(message: unexpectedErrorMessage);
    }
    if (mounted) {
      setState(() {
        _isLoading = true;
      });
    }
}
@override
void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Sign In')),
      body: ListView(
        padding: formPadding,
        children: [\
          TextFormField(\
            controller: _emailController,\
            decoration: const InputDecoration(labelText: 'Email'),\
            keyboardType: TextInputType.emailAddress,\
          ),\
          formSpacer,\
          TextFormField(\
            controller: _passwordController,\
            decoration: const InputDecoration(labelText: 'Password'),\
            obscureText: true,\
          ),\
          formSpacer,\
          ElevatedButton(\
            onPressed: _isLoading ? null : _signIn,\
            child: const Text('Login'),\
          ),\
        ],
      ),
    );
}
}
`

### Step 7: Create a chat page to receive and send real time messages [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#step-7-create-a-chat-page-to-receive-and-send-real-time-messages)

Last, we create the Chat page.
This page will load the messages in real time and display them to the users.
Users will also be able to send messages to everyone else using the app.
We are using the [stream()](https://supabase.com/docs/reference/dart/stream) method on Supabase SDK to load the messages in realtime.
As those messages come in, we are lazily loading the profiles of each message’s sender.
We will display the user icon as soon as their profile data is available.

`
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:my_chat_app/models/message.dart';
import 'package:my_chat_app/models/profile.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:timeago/timeago.dart';
/// Page to chat with someone.
///
/// Displays chat bubbles as a ListView and TextField to enter new chat.
class ChatPage extends StatefulWidget {
const ChatPage({Key? key}) : super(key: key);
static Route<void> route() {
    return MaterialPageRoute(
      builder: (context) => const ChatPage(),
    );
}
@override
State<ChatPage> createState() => _ChatPageState();
}
class _ChatPageState extends State<ChatPage> {
late final Stream<List<Message>> _messagesStream;
final Map<String, Profile> _profileCache = {};
@override
void initState() {
    final myUserId = supabase.auth.currentUser!.id;
    _messagesStream = supabase
        .from('messages')
        .stream(primaryKey: ['id'])
        .order('created_at')
        .map((maps) => maps
            .map((map) => Message.fromMap(map: map, myUserId: myUserId))
            .toList());
    super.initState();
}
Future<void> _loadProfileCache(String profileId) async {
    if (_profileCache[profileId] != null) {
      return;
    }
    final data =
        await supabase.from('profiles').select().eq('id', profileId).single();
    final profile = Profile.fromMap(data);
    setState(() {
      _profileCache[profileId] = profile;
    });
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Chat')),
      body: StreamBuilder<List<Message>>(
        stream: _messagesStream,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            final messages = snapshot.data!;
            return Column(
              children: [\
                Expanded(\
                  child: messages.isEmpty\
                      ? const Center(\
                          child: Text('Start your conversation now :)'),\
                        )\
                      : ListView.builder(\
                          reverse: true,\
                          itemCount: messages.length,\
                          itemBuilder: (context, index) {\
                            final message = messages[index];\
                            /// I know it's not good to include code that is not related\
                            /// to rendering the widget inside build method, but for\
                            /// creating an app quick and dirty, it's fine 😂\
                            _loadProfileCache(message.profileId);\
                            return _ChatBubble(\
                              message: message,\
                              profile: _profileCache[message.profileId],\
                            );\
                          },\
                        ),\
                ),\
                const _MessageBar(),\
              ],
            );
          } else {
            return preloader;
          }
        },
      ),
    );
}
}
/// Set of widget that contains TextField and Button to submit message
class _MessageBar extends StatefulWidget {
const _MessageBar({
    Key? key,
}) : super(key: key);
@override
State<_MessageBar> createState() => _MessageBarState();
}
class _MessageBarState extends State<_MessageBar> {
late final TextEditingController _textController;
@override
Widget build(BuildContext context) {
    return Material(
      color: Colors.grey[200],
      child: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            children: [\
              Expanded(\
                child: TextFormField(\
                  keyboardType: TextInputType.text,\
                  maxLines: null,\
                  autofocus: true,\
                  controller: _textController,\
                  decoration: const InputDecoration(\
                    hintText: 'Type a message',\
                    border: InputBorder.none,\
                    focusedBorder: InputBorder.none,\
                    contentPadding: EdgeInsets.all(8),\
                  ),\
                ),\
              ),\
              TextButton(\
                onPressed: () => _submitMessage(),\
                child: const Text('Send'),\
              ),\
            ],
          ),
        ),
      ),
    );
}
@override
void initState() {
    _textController = TextEditingController();
    super.initState();
}
@override
void dispose() {
    _textController.dispose();
    super.dispose();
}
void _submitMessage() async {
    final text = _textController.text;
    final myUserId = supabase.auth.currentUser!.id;
    if (text.isEmpty) {
      return;
    }
    _textController.clear();
    try {
      await supabase.from('messages').insert({
        'profile_id': myUserId,
        'content': text,
      });
    } on PostgrestException catch (error) {
      context.showErrorSnackBar(message: error.message);
    } catch (_) {
      context.showErrorSnackBar(message: unexpectedErrorMessage);
    }
}
}
class _ChatBubble extends StatelessWidget {
const _ChatBubble({
    Key? key,
    required this.message,
    required this.profile,
}) : super(key: key);
final Message message;
final Profile? profile;
@override
Widget build(BuildContext context) {
    List<Widget> chatContents = [\
      if (!message.isMine)\
        CircleAvatar(\
          child: profile == null\
              ? preloader\
              : Text(profile!.username.substring(0, 2)),\
        ),\
      const SizedBox(width: 12),\
      Flexible(\
        child: Container(\
          padding: const EdgeInsets.symmetric(\
            vertical: 8,\
            horizontal: 12,\
          ),\
          decoration: BoxDecoration(\
            color: message.isMine\
                ? Theme.of(context).primaryColor\
                : Colors.grey[300],\
            borderRadius: BorderRadius.circular(8),\
          ),\
          child: Text(message.content),\
        ),\
      ),\
      const SizedBox(width: 12),\
      Text(format(message.createdAt, locale: 'en_short')),\
      const SizedBox(width: 60),\
    ];
    if (message.isMine) {
      chatContents = chatContents.reversed.toList();
    }
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 18),
      child: Row(
        mainAxisAlignment:
            message.isMine ? MainAxisAlignment.end : MainAxisAlignment.start,
        children: chatContents,
      ),
    );
}
}
`

With that, we are done creating our application. If you kept your `flutter run` running, you should now see a fully functional application on your device or simulator. You can install it on another device or simulator to chat with each other in real time.

## Conclusion / Future improvements [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#conclusion--future-improvements)

We saw how easily it is to create a chat application when you combine amazing tools like Flutter and Supabase. One thing that was missing from this chat application is authorization. We did implement registration, but that was only to distinguish different users. In the coming up article, we will cover how you can add authorization using [row level security](https://supabase.com/docs/guides/auth/row-level-security) in Supabase to secure this chat application. With authorization, we can create private chat rooms so that messages can only be seen by those inside those rooms.

If you have any questions please reach out via [Twitter](https://twitter.com/dshukertjr) or join our [Discord](https://discord.supabase.com/).

## More Flutter Resources [\#](https://supabase.com/blog/flutter-tutorial-building-a-chat-app\#more-flutter-resources)

- [Part 2: Flutter Authentication and Authorization with RLS](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls)
- [Flutter Supabase Quick Starter Guide](https://supabase.com/docs/guides/with-flutter)
- [supabase-flutter v1.0 released](https://supabase.com/blog/supabase-flutter-sdk-v1-released)
- [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
- [Open source map based Flutter app with CI/CD and scalable statemanagement example](https://github.com/dshukertjr/spot)
- [Build a Flutter app with Very Good CLI and Supabase](https://verygood.ventures/blog/flutter-app-very-good-cli-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-tutorial-building-a-chat-app&text=Flutter%20Tutorial%3A%20building%20a%20Flutter%20chat%20app)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-tutorial-building-a-chat-app&text=Flutter%20Tutorial%3A%20building%20a%20Flutter%20chat%20app)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-tutorial-building-a-chat-app&t=Flutter%20Tutorial%3A%20building%20a%20Flutter%20chat%20app)

[Last post\\
\\
**Supabase Beta June 2022** \\
\\
6 July 2022](https://supabase.com/blog/beta-update-june-2022)

[Next post\\
\\
**Visualizing Supabase Data using Metabase** \\
\\
29 June 2022](https://supabase.com/blog/visualizing-supabase-data-using-metabase)

[flutter](https://supabase.com/blog/tags/flutter) [realtime](https://supabase.com/blog/tags/realtime) [mobile](https://supabase.com/blog/tags/mobile)

On this page

- [Overview of the final chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#overview-of-the-final-chat-app)
- [Setting up the scene](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#setting-up-the-scene)
  - [Create a blank Flutter application](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#create-a-blank-flutter-application)
  - [Install dependencies](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#install-dependencies)
  - [Creating a new Supabase project](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#creating-a-new-supabase-project)
  - [Setting up tables in Supabase](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#setting-up-tables-in-supabase)
- [Building the Flutter chat application](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#building-the-flutter-chat-application)
  - [Step 1: Define constants that to be used throughout the application](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#step-1-define-constants-that-to-be-used-throughout-the-application)
  - [Step 2: Initialize Supabase](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#step-2-initialize-supabase)
  - [Step 3: Redirect users depending on auth state using splash page](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#step-3-redirect-users-depending-on-auth-state-using-splash-page)
  - [Step 4 : Define data models to be used within the app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#step-4--define-data-models-to-be-used-within-the-app)
  - [Step 5: Create register page with email, password and username](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#step-5-create-register-page-with-email-password-and-username)
  - [Step 6: Create login page](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#step-6-create-login-page)
  - [Step 7: Create a chat page to receive and send real time messages](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#step-7-create-a-chat-page-to-receive-and-send-real-time-messages)
- [Conclusion / Future improvements](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#conclusion--future-improvements)
- [More Flutter Resources](https://supabase.com/blog/flutter-tutorial-building-a-chat-app#more-flutter-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-tutorial-building-a-chat-app&text=Flutter%20Tutorial%3A%20building%20a%20Flutter%20chat%20app)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-tutorial-building-a-chat-app&text=Flutter%20Tutorial%3A%20building%20a%20Flutter%20chat%20app)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-tutorial-building-a-chat-app&t=Flutter%20Tutorial%3A%20building%20a%20Flutter%20chat%20app)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)