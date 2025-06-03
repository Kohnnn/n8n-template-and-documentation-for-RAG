---
url: "https://supabase.com/blog/flutter-authentication"
title: "Getting started with Flutter authentication"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Getting started with Flutter authentication

18 Jul 2023

•

14 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Getting started with Flutter authentication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fflutter-authentication.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Flutter is Google’s open-source framework to develop cross-platform applications. In this article, we will take a look at how we can implement authentication using Google sign-in to secure our application using the [Supabase SDK for Flutter](https://supabase.com/docs/reference/dart/introduction).

We will also dive into the deep ends of Open ID Connect sign-in to better understand how third-party sign-ins are being performed. You can check out the code of the sample in this article [here](https://github.com/supabase/supabase/tree/master/examples/auth/flutter-native-google-auth).

## Prerequisites [\#](https://supabase.com/blog/flutter-authentication\#prerequisites)

This article assumes you are comfortable with writing a basic application in Flutter. No knowledge of Supabase is required.

We will use the following tools

- [Flutter](https://docs.flutter.dev/get-started/install) \- we used v3.10.5 for this article
- Supabase - create your account [here](https://database.new/) if you do not have one
- IDE of your choosing

## What is Open ID Connect? [\#](https://supabase.com/blog/flutter-authentication\#what-is-open-id-connect)

We will implement third-party login with Google utilizing the Open ID Connect functionality of Supabase Auth. Open ID Connect, or OIDC is a protocol built on top of OAuth 2.0 that allows third-party applications to request the users to provide some personal information, such as name or profile image, in the form of an identity token along with an access token. This identity token can then be verified and decoded by the application to obtain that personal information.

Supabase auth provides `signInWithIdToken` method where we can sign in a user using their ID token obtained from third-party auth providers such as Google. Upon signing a user with the `signInWithIdToken` method, Supabase automatically populates the content of the ID token in the Supabase user metadata for easy access to the information. We will be utilizing this feature in this example to display the user profile upon the user signing in.

In today’s example, our app will make a request to Google, obtain the identity token, and we will use it to sign the user in as well as obtain basic user information.

## What we will build [\#](https://supabase.com/blog/flutter-authentication\#what-we-will-build)

We will build a simple app with a login screen and a home screen. The user is first presented with the login screen, and only after they sign in, can they proceed to the home screen. The login screen presents a login button that will kick off a third-party authentication flow to complete the sign-in. The profile screen displays user information such as the profile image or their full name.

![Flutter Google sign in](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fflutter-google-sign-in.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Setup the Flutter project [\#](https://supabase.com/blog/flutter-authentication\#setup-the-flutter-project)

Let’s start by creating a fresh Flutter project.

`
flutter create myauthapp
`

then we can install the dependencies. Change the working directory to the newly created app directory and run the following command to install our dependencies.

`
flutter pub add supabase_flutter google_sign_in
`

The [supabase\_flutter](https://pub.dev/packages/supabase_flutter) package is used to interact with a Supabase instance. The [google\_sign\_in](https://pub.dev/packages/google_sign_in) package is used to implement social sign-in with Google.

We are done installing our dependencies. Let’s set up [authentication](https://supabase.com/docs/guides/auth) now.

## Configure Google sign-in on Supabase Auth [\#](https://supabase.com/blog/flutter-authentication\#configure-google-sign-in-on-supabase-auth)

We will obtain client IDs for iOS, Android, and web from the Google Cloud console, and register them to our Supabase project.
The web client ID will be used by the auth server of Supabase to verify the ID token provided by the Google sign-in package.

First, create your Google Cloud project [here](https://cloud.google.com/) if you do not have one yet.
Within your Google Cloud project, follow the [Get an OAuth client ID for the iOS](https://developers.google.com/identity/sign-in/ios/start-integrating#get_an_oauth_client_id) guide, [Configure a Google API Console project for Android](https://developers.google.com/identity/sign-in/android/start-integrating#configure_a_project) guide, and [Get your backend server's OAuth 2.0 client ID](https://developers.google.com/identity/sign-in/android/start-integrating#configure_a_project) to obtain client IDs for iOS, Android, and web respectively.

Once you have the client IDs, let’s add them to our Supabase dashboard. If you don’t have a Supabase project created yet, you can create one at [database.new](https://database.new/) for free. The name is just an internal name, so we can call it “Auth” for now.
The database password won't be used in this example and can be reconfigured later, so press the `Generate a password` button and let Supabase generate a secure random password. The region should be anywhere close to where you live, or where your users live in an actual production app.
Lastly, for the pricing plan choose the Free Plan that allows you to connect with all major social OAuth providers and supports up to 50,000 monthly active users.

![Supabase project creation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fsupabase-project-creation.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Your project should be ready in a minute or two. Once your project is ready, open `authentication -> Providers -> Google` to set up Google auth. Toggle the `Enable Sign in with Google` switch first. Then add the web client ID you obtained in your Google Cloud console to `Authorized Client IDs` field. No need to add the Android or iOS client IDs here.

Turn on the `Skip nonce checks` option. This would allow us to use the Google sign in package on iOS, which is not compatible with providing a method to access or specify a nonce.

![Supabase auth Google auth provider](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fsupabase-google-provider.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We also need some iOS specific settings. Open `ios/Runner/Info.plist` file and add the `CFBundleURLTypes` like the following. You need to provide the reverse client ID of the iOS client ID you registered earlier.

`
<key>CFBundleURLTypes</key>
<array>
<dict>
    <key>CFBundleTypeRole</key>
    <string>Editor</string>
    <key>CFBundleURLSchemes</key>
    <array>
      <!-- TODO Replace this value: -->
      <!-- Copied from GoogleService-Info.plist key REVERSED_CLIENT_ID -->
      <string>com.googleusercontent.apps.my-ios</string>
    </array>
</dict>
</array>
`

That is it for setting up our [Supabase auth to prepare for Google sign-in](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=flutter).

Finally, we can initialize Supabase in our Flutter application with the credentials of our Supabase instance. Update your `main.dart` file and add `Supabase.initialize()` in the `main` function like the following. Note that you will see some errors since the home screen is set to the `LoginScreen`, which we will create later.

`
import 'package:flutter/material.dart';
import 'package:myauthapp/screens/login_screen.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
void main() async {
/// TODO: update Supabase credentials with your own
await Supabase.initialize(
    url: 'YOUR_SUPABASE_URL',
    anonKey: 'YOUR_ANON_KEY',
);
runApp(const MyApp());
}
final supabase = Supabase.instance.client;
class MyApp extends StatelessWidget {
const MyApp({super.key});
@override
Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Auth',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const LoginScreen(),
    );
}
}
`

You can find your Supabase URL and Anon key in `Settings -> API` from your [Supabase dashboard](https://supabase.com/dashboard/project/_/settings/api).

![Supabase credentials](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fsupabase-credentials.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Create the Login Screen [\#](https://supabase.com/blog/flutter-authentication\#create-the-login-screen)

We will have two screens for this app, `LoginScreen` and `ProfileScreen`. `LoginScreen` presents a single sign-in button for the user to perform Google sign-in. Create a `lib/screens/login_screen.dart` file add add the following.

`
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:myauthapp/main.dart';
import 'package:myauthapp/screens/profile_screen.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class LoginScreen extends StatefulWidget {
const LoginScreen({super.key});
@override
State<LoginScreen> createState() => _LoginScreenState();
}
class _LoginScreenState extends State<LoginScreen> {
@override
void initState() {
    _setupAuthListener();
    super.initState();
}
void _setupAuthListener() {
    supabase.auth.onAuthStateChange.listen((data) {
      final event = data.event;
      if (event == AuthChangeEvent.signedIn) {
        Navigator.of(context).pushReplacement(
          MaterialPageRoute(
            builder: (context) => const ProfileScreen(),
          ),
        );
      }
    });
}
Future<AuthResponse> _googleSignIn() async {
    /// TODO: update the Web client ID with your own.
    ///
    /// Web Client ID that you registered with Google Cloud.
    const webClientId = 'my-web.apps.googleusercontent.com';
    /// TODO: update the iOS client ID with your own.
    ///
    /// iOS Client ID that you registered with Google Cloud.
    const iosClientId = 'my-ios.apps.googleusercontent.com';
    // Google sign in on Android will work without providing the Android
    // Client ID registered on Google Cloud.
    final GoogleSignIn googleSignIn = GoogleSignIn(
      clientId: iosClientId,
      serverClientId: webClientId,
    );
    final googleUser = await googleSignIn.signIn();
    final googleAuth = await googleUser!.authentication;
    final accessToken = googleAuth.accessToken;
    final idToken = googleAuth.idToken;
    if (accessToken == null) {
      throw 'No Access Token found.';
    }
    if (idToken == null) {
      throw 'No ID Token found.';
    }
    return supabase.auth.signInWithIdToken(
      provider: OAuthProvider.google,
      idToken: idToken,
      accessToken: accessToken,
    );
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: _googleSignIn,
          child: const Text('Google login'),
        ),
      ),
    );
}
}
`

In terms of UI, this page is very simple, it just has a basic `Scaffold` with an `AppBar`, and has a button right in the middle of the body. Upon pressing the button, Google sign in flow starts. The user is presented with a Google authentication screen where they will complete the consent to allow our application to sign the user in using a Google account, as well as allow us to view some personal information.

![Google sign in](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fgoogle-sign-in.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Within the `onPressed` callback of the button, we are calling the `_googleSignIn` method.
This method calls the Google sign-in package to perform the sign-in flow.
Once the user completes the sign-in flow, we obtain an access token and an ID token.
We will pass these tokens to Supabase auth to then obtain a Supabase session.

## Create the Profile Screen [\#](https://supabase.com/blog/flutter-authentication\#create-the-profile-screen)

The `ProfileScreen` will be just a simple UI presenting some of the information we obtained in the `LoginPage`. We can access the user data with `supabase.auth.currentUser`, where Supabase has saved the personal information in a property called `userMetadata`. In this example, we are displaying the `avatar_url` and `full_name` to display a basic profile page. Create a `lib/screens/profile_screen.dart` file and add the following.

`
import 'package:flutter/material.dart';
import 'package:myauthapp/main.dart';
import 'package:myauthapp/screens/login_screen.dart';
class ProfileScreen extends StatelessWidget {
const ProfileScreen({super.key});
@override
Widget build(BuildContext context) {
    final user = supabase.auth.currentUser;
    final profileImageUrl = user?.userMetadata?['avatar_url'];
    final fullName = user?.userMetadata?['full_name'];
    return Scaffold(
      appBar: AppBar(
        title: const Text('Profile'),
        actions: [\
          TextButton(\
            onPressed: () async {\
              await supabase.auth.signOut();\
              if (context.mounted) {\
                Navigator.of(context).pushReplacement(\
                  MaterialPageRoute(builder: (context) => const LoginScreen()),\
                );\
              }\
            },\
            child: const Text('Sign out'),\
          )\
        ],
      ),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [\
            if (profileImageUrl != null)\
              ClipOval(\
                child: Image.network(\
                  profileImageUrl,\
                  width: 100,\
                  height: 100,\
                  fit: BoxFit.cover,\
                ),\
              ),\
            const SizedBox(height: 16),\
            Text(\
              fullName ?? '',\
              style: Theme.of(context).textTheme.headlineMedium,\
            ),\
            const SizedBox(height: 32),\
          ],
        ),
      ),
    );
}
}
`

And with that, we now have a basic working personalized application that utilizes Google sign-in.

![Flutter Google sign in app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fflutter-google-sign-in.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Conclusion [\#](https://supabase.com/blog/flutter-authentication\#conclusion)

In this post, we learned how to implement authentication in a Flutter application using Google sign-in and the Supabase SDK for Flutter. We also delved into the Open ID Connect functionality, which allows third-party sign-ins and the retrieval of personal information through identity tokens.

You can also check out the [Flutter reference documents](https://supabase.com/docs/reference/dart/installing) to see how you can use `supabase-flutter` to implement a Postgres database, Storage, Realtime, and more.

## More Flutter and Supabase resources [\#](https://supabase.com/blog/flutter-authentication\#more-flutter-and-supabase-resources)

- [supabase\_flutter package](https://pub.dev/packages/supabase_flutter)
- [Build a chat application using Flutter and Supabase](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
- [Securing your Flutter apps with Multi-Factor Authentication](https://supabase.com/blog/flutter-multi-factor-authentication)
- [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&t=Getting%20started%20with%20Flutter%20authentication)

[Last post\\
\\
**Supabase Launch Week 8 Hackathon** \\
\\
25 July 2023](https://supabase.com/blog/supabase-lw8-hackathon)

[Next post\\
\\
**pgvector 0.4.0 performance** \\
\\
13 July 2023](https://supabase.com/blog/pgvector-performance)

[flutter](https://supabase.com/blog/tags/flutter) [auth](https://supabase.com/blog/tags/auth)

On this page

- [Prerequisites](https://supabase.com/blog/flutter-authentication#prerequisites)
- [What is Open ID Connect?](https://supabase.com/blog/flutter-authentication#what-is-open-id-connect)
- [What we will build](https://supabase.com/blog/flutter-authentication#what-we-will-build)
- [Setup the Flutter project](https://supabase.com/blog/flutter-authentication#setup-the-flutter-project)
- [Configure Google sign-in on Supabase Auth](https://supabase.com/blog/flutter-authentication#configure-google-sign-in-on-supabase-auth)
- [Create the Login Screen](https://supabase.com/blog/flutter-authentication#create-the-login-screen)
- [Create the Profile Screen](https://supabase.com/blog/flutter-authentication#create-the-profile-screen)
- [Conclusion](https://supabase.com/blog/flutter-authentication#conclusion)
- [More Flutter and Supabase resources](https://supabase.com/blog/flutter-authentication#more-flutter-and-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&t=Getting%20started%20with%20Flutter%20authentication)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)