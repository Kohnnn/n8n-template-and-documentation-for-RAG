---
url: "https://supabase.com/blog/flutter-multi-factor-authentication"
title: "Securing your Flutter apps with Multi-Factor Authentication"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Securing your Flutter apps with Multi-Factor Authentication

04 May 2023

•

50 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Securing your Flutter apps with Multi-Factor Authentication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fflutter-mfa-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Multi-factor authentication or MFA is an essential part of security for any kind of app.

We will take a look at an example app where a user has to sign in via MFA in order to view the contents of the app to demonstrate how easy it is to get started with MFA on Flutter.

## What is Multi-Factor Authentication? [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#what-is-multi-factor-authentication)

Multi-factor authentication (MFA), sometimes called two-factor authentication (2FA), is an additional security layer on top of traditional login methods such as email and password login.

There are several forms of MFA, such as with an SMS or through using an authenticator app such as Google Authenticator. It is considered a best practice to use MFA whenever possible because it protects users against weak passwords or compromised social accounts.

## Why Multi-Factor Authentication matters for Flutter apps [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#why-multi-factor-authentication-matters-for-flutter-apps)

In the context of Flutter apps, MFA is important because it helps protect sensitive user data and prevent unauthorized access to user accounts. By requiring users to provide an additional factor, MFA adds an extra layer of security that makes it harder for attackers to gain access to user accounts.

Given how Flutter is widely used MFA might be a requirement rather than a nice-to-have. Implementing MFA in a Flutter app can improve overall security and give users peace of mind knowing that their data is better protected.

## Building the App [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#building-the-app)

![Multi-factor Authentication with Flutter](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fmfa.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We are building a simple app where users register with an email and password. After completing the registration process, the users will be asked to set up MFA using an authenticator app. Once verifying the identity via the authenticator app, the user can go to the home page where they can view the main content.

Login works similarly, where after an email and password login, they are asked to enter the verification code to complete the login process.

The app will have the following directory structure, where `auth` contains any basic auth-related pages, `mfa` contains enrolling and verifying the MFA, and we have some additional pages for us to see that MFA is working correctly.

You can find the complete code created in this article [here](https://github.com/supabase/supabase/tree/master/examples/auth/flutter-mfa).

![Directory Structure of the app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fdirectory.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Step 1: Setup the scenes [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#step-1-setup-the-scenes)

Let’s start with the `flutter create` command.

`
flutter create mfa_app
`

Also, if you do not have a Supabase project yet, create one by heading to [database.new](https://dstabase.new/). Within a few minutes, you will have a new Supabase project.

### Step 2: Add the dependencies [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#step-2-add-the-dependencies)

Install the [supabase\_flutter](https://pub.dev/packages/supabase_flutter) package by running the following command in your terminal.

`
dart pub add supabase_flutter
`

Then update your `lib/main.dart` file to initialize Supabase in the main function. You should be able to find your Supabase URL and AnonKey from the `settings -> api` section of your dashboard. We will also extract the `SupabaseClient` for easy access to our Supabase instance.

`
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
void main() async {
await Supabase.initialize(
    url: 'SUPABASE_URL',
    anonKey: 'SUPABASE_ANONKEY',
);
runApp(const MyApp());
}
/// Extract SupabaseClient instance in a handy variable
final supabase = Supabase.instance.client;
`

Also, add [go\_router](https://pub.dev/packages/go_router) to handle our routing and redirects.

`
dart pub add go_router
`

We will set up the routes towards the end when we have created all the pages we need. With this, we are ready to jump into creating the app.

Also, if we want to support iOS and Android, we need to set up deep links so that a session can be obtained upon clicking on the confirmation link sent to the user’s email address.

We will configure it so that we can open the app by redirecting to `mfa-app://callback` .

For iOS, open `ios/Runner/info.plist` file and add the following deep link configuration.

`
<!-- ... other tags -->
<plist>
<dict>
    <!-- ... other tags -->
		<!-- Deep Links -->
		<key>FlutterDeepLinkingEnabled</key>
		<true/>
    <key>CFBundleURLTypes</key>
    <array>
      <dict>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
        <key>CFBundleURLSchemes</key>
        <array>
          <string>mfa-app</string>
        </array>
      </dict>
    </array>
		<!-- Deep Links -->
    <!-- ... other tags -->
</dict>
</plist>
`

For Android, open `android/app/src/main/AndroidManifest.xml` file and add the following deep link configuration.

`
<manifest ...>
    <!-- ... other tags -->
    <application ...>
      <activity ...>
        <!-- ... other tags -->
        <!-- Deep Links -->
				<meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
        <intent-filter>
          <action android:name="android.intent.action.VIEW" />
          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />
          <data
            android:scheme="mfa-app"
            android:host="callback" />
        </intent-filter>
        <!-- END Deep Links -->
      </activity>
    </application>
</manifest>
`

After, we will add the deep link as one of the redirect URLs in our Supabase dashboard.

Go to `Authentication > URL Configuration` and add `mfa-app://callback/*` as a redirect URL. Make sure you don’t add any extra slashes or anything because if you do, deep linking will not work properly.

![Supabase Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fsupabase-dashboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Lastly, we will add the `flutter_svg` package. This package will later be used to display a QR code to scan with their authentication app.

`
dart pub add flutter_svg
`

That is all the dependencies that we need. Let’s dive into coding!

### Step 3: Create the signup flow [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#step-3-create-the-signup-flow)

![Register flow](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fregister.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Let’s first create a signup flow. Again, the user will register with the app using email and password, and after confirming their email address, they will enroll in MFA using an authenticator app.

The register page contains a form with an email and password field for the user to create a new account. We are just calling the [.signUp()](https://supabase.com/docs/reference/dart/auth-signup) method with it.
As you can see in the code below at `emailRedirectTo` option of the `.signUp()` method, upon clicking on the confirmation link sent to the user, they will be taken to MFA enrollment page, which we will implement later.

Create a `lib/pages/auth/signup_page.dart` file and add the following. There will be some errors, but that is because we haven’t created some of the files yet. The errors will go away as we move on, so ignore them for now.

`
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mfa_app/main.dart';
import 'package:mfa_app/pages/auth/login_page.dart';
import 'package:mfa_app/pages/mfa/enroll_page.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class RegisterPage extends StatefulWidget {
static const route = '/auth/register';
const RegisterPage({super.key});
@override
State<RegisterPage> createState() => _RegisterPageState();
}
class _RegisterPageState extends State<RegisterPage> {
final _emailController = TextEditingController();
final _passwordController = TextEditingController();
bool _isLoading = false;
@override
void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Register')),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
        children: [\
          TextFormField(\
            controller: _emailController,\
            decoration: const InputDecoration(\
              label: Text('Email'),\
            ),\
          ),\
          const SizedBox(height: 16),\
          TextFormField(\
            controller: _passwordController,\
            decoration: const InputDecoration(\
              label: Text('Password'),\
            ),\
            obscureText: true,\
          ),\
          const SizedBox(height: 16),\
          ElevatedButton(\
            onPressed: () async {\
              try {\
                setState(() {\
                  _isLoading = true;\
                });\
                final email = _emailController.text.trim();\
                final password = _passwordController.text.trim();\
                await supabase.auth.signUp(\
                  email: email,\
                  password: password,\
                  emailRedirectTo:\
                      'mfa-app://callback${MFAEnrollPage.route}', // redirect the user to setup MFA page after email confirmation\
                );\
                if (mounted) {\
                  ScaffoldMessenger.of(context).showSnackBar(\
                      const SnackBar(content: Text('Check your inbox.')));\
                }\
              } on AuthException catch (error) {\
                ScaffoldMessenger.of(context)\
                    .showSnackBar(SnackBar(content: Text(error.message)));\
              } catch (error) {\
                ScaffoldMessenger.of(context).showSnackBar(\
                    const SnackBar(content: Text('Unexpected error occurred')));\
              }\
              if (mounted) {\
                setState(() {\
                  _isLoading = false;\
                });\
              }\
            },\
            child: _isLoading\
                ? const SizedBox(\
                    height: 24,\
                    width: 24,\
                    child: Center(\
                        child: CircularProgressIndicator(color: Colors.white)),\
                  )\
                : const Text('Register'),\
          ),\
          const SizedBox(height: 16),\
          TextButton(\
            onPressed: () => context.push(LoginPage.route),\
            child: const Text('I already have an account'),\
          )\
        ],
      ),
    );
}
}
`

We can then create the enrollment page for MFA. This page is taking care of the following.

- Retrieve the enrollment secret from the server via `supabase.auth.mfa.enroll()` method.
- Displaying the secret and its QR code representation and prompts the user to add the app to their authenticator app
- Verifies the user with a TOTP

The QR code and the secret will be displayed automatically when the page loads. When the user enters the correct 6-digit TOTP, they will be automatically redirected to the home page.

Create `lib/pages/mfa/enroll_page.dart` file and add the following.

`
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:go_router/go_router.dart';
import 'package:mfa_app/main.dart';
import 'package:mfa_app/pages/auth/register_page.dart';
import 'package:mfa_app/pages/home_page.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class MFAEnrollPage extends StatefulWidget {
static const route = '/mfa/enroll';
const MFAEnrollPage({super.key});
@override
State<MFAEnrollPage> createState() => _MFAEnrollPageState();
}
class _MFAEnrollPageState extends State<MFAEnrollPage> {
final _enrollFuture = supabase.auth.mfa.enroll();
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Setup MFA'),
        actions: [\
          TextButton(\
            onPressed: () {\
              supabase.auth.signOut();\
              context.go(RegisterPage.route);\
            },\
            child: Text(\
              'Logout',\
              style: TextStyle(color: Theme.of(context).colorScheme.onPrimary),\
            ),\
          ),\
        ],
      ),
      body: FutureBuilder(
        future: _enrollFuture,
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return Center(child: Text(snapshot.error.toString()));
          }
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }
          final response = snapshot.data!;
          final qrCodeUrl = response.totp.qrCode;
          final secret = response.totp.secret;
          final factorId = response.id;
          return ListView(
            padding: const EdgeInsets.symmetric(
              horizontal: 20,
              vertical: 24,
            ),
            children: [\
              const Text(\
                'Open your authentication app and add this app via QR code or by pasting the code below.',\
                style: TextStyle(\
                  fontWeight: FontWeight.bold,\
                ),\
              ),\
              const SizedBox(height: 16),\
              SvgPicture.string(\
                qrCodeUrl,\
                width: 150,\
                height: 150,\
              ),\
              const SizedBox(height: 16),\
              Row(\
                children: [\
                  Expanded(\
                    child: Text(\
                      secret,\
                      style: const TextStyle(\
                        fontWeight: FontWeight.bold,\
                        fontSize: 18,\
                      ),\
                    ),\
                  ),\
                  IconButton(\
                    onPressed: () {\
                      Clipboard.setData(ClipboardData(text: secret));\
                      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(\
                          content: Text('Copied to your clip board')));\
                    },\
                    icon: const Icon(Icons.copy),\
                  ),\
                ],\
              ),\
              const SizedBox(height: 16),\
              const Text('Enter the code shown in your authentication app.'),\
              const SizedBox(height: 16),\
              TextFormField(\
                decoration: const InputDecoration(\
                  hintText: '000000',\
                ),\
                style: const TextStyle(fontSize: 24),\
                textAlign: TextAlign.center,\
                keyboardType: TextInputType.number,\
                onChanged: (value) async {\
                  if (value.length != 6) return;\
                  // kick off the verification process once 6 characters are entered\
                  try {\
                    final challenge =\
                        await supabase.auth.mfa.challenge(factorId: factorId);\
                    await supabase.auth.mfa.verify(\
                      factorId: factorId,\
                      challengeId: challenge.id,\
                      code: value,\
                    );\
                    await supabase.auth.refreshSession();\
                    if (mounted) {\
                      context.go(HomePage.route);\
                    }\
                  } on AuthException catch (error) {\
                    ScaffoldMessenger.of(context)\
                        .showSnackBar(SnackBar(content: Text(error.message)));\
                  } catch (error) {\
                    ScaffoldMessenger.of(context).showSnackBar(const SnackBar(\
                        content: Text('Unexpected error occurred')));\
                  }\
                },\
              ),\
            ],
          );
        },
      ),
    );
}
}
`

### Step 4: Creating the login flow [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#step-4-creating-the-login-flow)

![Login flow](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Flogin.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now that we have created a registration flow, we can get to the login flow for returning existing users. Again, the login page has nothing fancy going. We are just collecting the user’s email and password, and calling the good old [.signInWithPassword()](https://supabase.com/docs/reference/dart/auth-signinwithpassword) method. Upon signing in, the user will be taken to a verify page where the user will then enter their verification code from their authenticator app.

Create `lib/pages/auth/login_page.dart` and add the following.

`
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mfa_app/main.dart';
import 'package:mfa_app/pages/mfa/verify_page.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class LoginPage extends StatefulWidget {
static const route = '/auth/login';
const LoginPage({super.key});
@override
State<LoginPage> createState() => _LoginPageState();
}
class _LoginPageState extends State<LoginPage> {
final _emailController = TextEditingController();
final _passwordController = TextEditingController();
@override
void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Login')),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
        children: [\
          TextFormField(\
            controller: _emailController,\
            decoration: const InputDecoration(\
              label: Text('Email'),\
            ),\
          ),\
          const SizedBox(height: 16),\
          TextFormField(\
            controller: _passwordController,\
            decoration: const InputDecoration(\
              label: Text('Password'),\
            ),\
            obscureText: true,\
          ),\
          const SizedBox(height: 16),\
          ElevatedButton(\
            onPressed: () async {\
              try {\
                final email = _emailController.text.trim();\
                final password = _passwordController.text.trim();\
                await supabase.auth.signInWithPassword(\
                  email: email,\
                  password: password,\
                );\
                if (mounted) {\
                  context.go(MFAVerifyPage.route);\
                }\
              } on AuthException catch (error) {\
                ScaffoldMessenger.of(context)\
                    .showSnackBar(SnackBar(content: Text(error.message)));\
              } catch (error) {\
                ScaffoldMessenger.of(context).showSnackBar(\
                    const SnackBar(content: Text('Unexpected error occurred')));\
              }\
            },\
            child: const Text('Login'),\
          ),\
        ],
      ),
    );
}
}
`

Once a returning user logs in, they are taken to the verification page where they are asked to enter the TOTP from their authenticator app.

This verification page has the same text field as the enrollment page, and upon entering the code, they are taken to the home page.

Create a `lib/pages/mfa/verify_page.dart` file and add the following.

`
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mfa_app/main.dart';
import 'package:mfa_app/pages/auth/register_page.dart';
import 'package:mfa_app/pages/home_page.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class MFAVerifyPage extends StatefulWidget {
static const route = '/mfa/verify';
const MFAVerifyPage({super.key});
@override
State<MFAVerifyPage> createState() => _MFAVerifyPageState();
}
class _MFAVerifyPageState extends State<MFAVerifyPage> {
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Verify MFA'),
        actions: [\
          TextButton(\
            onPressed: () {\
              supabase.auth.signOut();\
              context.go(RegisterPage.route);\
            },\
            child: Text(\
              'Logout',\
              style: TextStyle(color: Theme.of(context).colorScheme.onPrimary),\
            ),\
          ),\
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.symmetric(
          horizontal: 20,
          vertical: 24,
        ),
        children: [\
          Text(\
            'Verification Required',\
            style: Theme.of(context).textTheme.titleLarge,\
          ),\
          const SizedBox(height: 16),\
          const Text('Enter the code shown in your authentication app.'),\
          const SizedBox(height: 16),\
          TextFormField(\
            decoration: const InputDecoration(\
              hintText: '000000',\
            ),\
            style: const TextStyle(fontSize: 24),\
            textAlign: TextAlign.center,\
            keyboardType: TextInputType.number,\
            onChanged: (value) async {\
              if (value.length != 6) return;\
              // kick off the verification process once 6 characters are entered\
              try {\
                final factorsResponse = await supabase.auth.mfa.listFactors();\
                final factor = factorsResponse.totp.first;\
                final factorId = factor.id;\
                final challenge =\
                    await supabase.auth.mfa.challenge(factorId: factorId);\
                await supabase.auth.mfa.verify(\
                  factorId: factorId,\
                  challengeId: challenge.id,\
                  code: value,\
                );\
                await supabase.auth.refreshSession();\
                if (mounted) {\
                  context.go(HomePage.route);\
                }\
              } on AuthException catch (error) {\
                ScaffoldMessenger.of(context)\
                    .showSnackBar(SnackBar(content: Text(error.message)));\
              } catch (error) {\
                ScaffoldMessenger.of(context).showSnackBar(\
                    const SnackBar(content: Text('Unexpected error occurred')));\
              }\
            },\
          ),\
        ],
      ),
    );
}
}
`

### Step 5: Add a home page with secure contents [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#step-5-add-a-home-page-with-secure-contents)

![Home Page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fhome.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The home page is where the “secure” contents are displayed. We will create a dummy table with some dummy secure contents for demonstration purposes.

First, we create dummy content. Run the following SQL to create the table and add some content.

`
-- Dummy table that contains "secure" information
create table
if not exists public.private_posts (
    id int generated by default as identity primary key,
    content text not null
);
-- Dmmy "secure" data
insert into
public.private_posts (content)
values
('Flutter is awesome!'),
('Supabase is awesome!'),
('Postgres is awesome!');
`

Now, we can add some [row security policy](https://supabase.com/docs/guides/auth/row-level-security) to lock those data down so that only users who have signed in using MFA can view them.

Run the following SQL to secure our data from malicious users.

`
-- Enable RLS for private_posts table
alter table
public.private_posts enable row level security;
-- Create a policy that only allows read if they user has signed in via MFA
create policy "Users can view private_posts if they have signed in via MFA" on public.private_posts for
select
to authenticated using ((select auth.jwt() - >> 'aal') = 'aal2');
`

`aal` here stands for [Authenticator Assurance Level](https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/), and it will be `aal1` for users who have only signed in with 1 sign-in method, and `aal2` for users who have completed the MFA flow. Checking the `aal` inside RLS policy ensures that the data cannot be viewed by users unless they complete the entire MFA flow.

The nice thing about RLS is that it gives us the flexibility to control how users can interact with the data. In this particular example, we are mandating MFA to view the data, but you could easily create layered permissions where for example a user can view the data with 1 factor, but can edit the data when signed in with MFA. You can see more examples in our official MFA guide [here](https://supabase.com/docs/guides/auth/auth-mfa).

Now that we have the secure data in our Supabase instance, all we need to do is to display them in the HomePage. We can simply query the table and display it using a `FutureBuilder`.

Create a `lib/pages/home_page.dart` file and add the following.

`
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mfa_app/main.dart';
import 'package:mfa_app/pages/auth/register_page.dart';
import 'package:mfa_app/pages/list_mfa_page.dart';
class HomePage extends StatelessWidget {
static const route = '/';
const HomePage({super.key});
@override
Widget build(BuildContext context) {
    final privatePostsFuture = supabase.from('private_posts').select();
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home'),
        actions: [\
          PopupMenuButton(\
            itemBuilder: (context) {\
              return [\
                PopupMenuItem(\
                  child: const Text('Unenroll MFA'),\
                  onTap: () {\
                    context.push(ListMFAPage.route);\
                  },\
                ),\
                PopupMenuItem(\
                  child: const Text('Logout'),\
                  onTap: () {\
                    supabase.auth.signOut();\
                    context.go(RegisterPage.route);\
                  },\
                ),\
              ];\
            },\
          )\
        ],
      ),
      body: FutureBuilder<List<Map<String, dynamic>>>(
        future: privatePostsFuture,
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return Center(child: Text(snapshot.error.toString()));
          }
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }
          // Display the secure private content upon retrieval
          final data = snapshot.data!;
          return ListView.builder(
            itemCount: data.length,
            itemBuilder: (context, index) {
              return ListTile(title: Text(data[index]['content']));
            },
          );
        },
      ),
    );
}
}
`

Because we have set the RLS policy, any user without going through the MFA flow will not see anything on this page.

One final page to add here is the **unenrollment** page. On this page, users can remove any factors that they have added. Once a user removes the factor, the user’s account will no longer be associated with the authenticator app, and they would have to go through the enrollment steps again.

Create `lib/pages/list_mfa_page.dart` file and add the following.

`
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mfa_app/main.dart';
import 'package:mfa_app/pages/auth/register_page.dart';
/// A page that lists the currently signed in user's MFA methods.
///
/// The user can unenroll the factors.
class ListMFAPage extends StatelessWidget {
static const route = '/list-mfa';
ListMFAPage({super.key});
final _factorListFuture = supabase.auth.mfa.listFactors();
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('List of MFA Factors')),
      body: FutureBuilder(
        future: _factorListFuture,
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return Center(child: Text(snapshot.error.toString()));
          }
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }
          final response = snapshot.data!;
          final factors = response.all;
          return ListView.builder(
            itemCount: factors.length,
            itemBuilder: (context, index) {
              final factor = factors[index];
              return ListTile(
                title: Text(factor.friendlyName ?? factor.factorType.name),
                subtitle: Text(factor.status.name),
                trailing: IconButton(
                  onPressed: () {
                    showDialog(
                        context: context,
                        builder: (context) {
                          return AlertDialog(
                            title: const Text(
                              'Are you sure you want to delete this factor? You will be signed out of the app upon removing the factor.',
                            ),
                            actions: [\
                              TextButton(\
                                onPressed: () {\
                                  context.pop();\
                                },\
                                child: const Text('cancel'),\
                              ),\
                              TextButton(\
                                onPressed: () async {\
                                  await supabase.auth.mfa.unenroll(factor.id);\
                                  await supabase.auth.signOut();\
                                  if (context.mounted) {\
                                    context.go(RegisterPage.route);\
                                  }\
                                },\
                                child: const Text('delete'),\
                              ),\
                            ],
                          );
                        });
                  },
                  icon: const Icon(Icons.delete_outline),
                ),
              );
            },
          );
        },
      ),
    );
}
}
`

### Step 6: Putting the pieces together with go\_router [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#step-6-putting-the-pieces-together-with-go_router)

Now that we have all the pages, it’s time to put it all together with the help of [go\_router](https://pub.dev/packages/go_router).

go\_router, as you may know, is a routing package for Flutter, and its redirect feature is particularly helpful for implementing the complex requirement this app had. Particularly, we wanted to make sure that a user who has not yet set up MFA is redirected to the MFA setup page, and only users who have signed in land on the home page.

Another helpful feature of go\_router comes when using deep links, and it automatically redirects the users to the correct path of the deep link. Because of this, we can ensure that user lands on the MFA setup page upon confirming their email address.

We will add the router in our `lib/main.dart` file. Your `main.dart` file should now look like this.

`
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mfa_app/pages/auth/login_page.dart';
import 'package:mfa_app/pages/auth/register_page.dart';
import 'package:mfa_app/pages/home_page.dart';
import 'package:mfa_app/pages/list_mfa_page.dart';
import 'package:mfa_app/pages/mfa/verify_page.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:mfa_app/pages/mfa/enroll_page.dart';
void main() async {
await Supabase.initialize(
    url: 'YOUR_SUPABASE_URL',
    anonKey: 'YOUR_ANON_KEY',
);
runApp(const MyApp());
}
/// Extract SupabaseClient instance in a handy variable
final supabase = Supabase.instance.client;
final _router = GoRouter(
routes: [\
    GoRoute(\
      path: HomePage.route,\
      builder: (context, state) => const HomePage(),\
    ),\
    GoRoute(\
      path: ListMFAPage.route,\
      builder: (context, state) => ListMFAPage(),\
    ),\
    GoRoute(\
      path: LoginPage.route,\
      builder: (context, state) => const LoginPage(),\
    ),\
    GoRoute(\
      path: RegisterPage.route,\
      builder: (context, state) => const RegisterPage(),\
    ),\
    GoRoute(\
      path: MFAEnrollPage.route,\
      builder: (context, state) => const MFAEnrollPage(),\
    ),\
    GoRoute(\
      path: MFAVerifyPage.route,\
      builder: (context, state) => const MFAVerifyPage(),\
    ),\
],
redirect: (context, state) async {
    // Any users can visit the /auth route
    if (state.location.contains('/auth') == true) {
      return null;
    }
    final session = supabase.auth.currentSession;
    // A user without a session should be redirected to the register page
    if (session == null) {
      return RegisterPage.route;
    }
    final assuranceLevelData =
        supabase.auth.mfa.getAuthenticatorAssuranceLevel();
    // The user has not setup MFA yet, so send them to enroll MFA page.
    if (assuranceLevelData.currentLevel == AuthenticatorAssuranceLevels.aal1) {
      await supabase.auth.refreshSession();
      final nextLevel =
          supabase.auth.mfa.getAuthenticatorAssuranceLevel().nextLevel;
      if (nextLevel == AuthenticatorAssuranceLevels.aal2) {
        // The user has already setup MFA, but haven't login via MFA
        // Redirect them to the verify page
        return MFAVerifyPage.route;
      } else {
        // The user has not yet setup MFA
        // Redirect them to the enrollment page
        return MFAEnrollPage.route;
      }
    }
    // The user has signed invia MFA, and is allowed to view any page.
    return null;
},
);
class MyApp extends StatelessWidget {
const MyApp({super.key});
// This widget is the root of your application.
@override
Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'MFA App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData.light().copyWith(
        inputDecorationTheme: const InputDecorationTheme(
          border: OutlineInputBorder(),
        ),
      ),
      routerConfig: _router,
    );
}
}
`

## Conclusions and future iterations [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#conclusions-and-future-iterations)

We looked at how to incorporate Multi-Factor Authentication into a Flutter app with a complete enrollment and verification flow for new and existing users. We saw how we are able to control how the users can interact with the data using their MFA status.

Another common use case is to make MFA optional and allow the user to opt-in whenever they are ready. Optionally enrolling in MFA will require some tweaks in the code, but might be a fun one to try out.

## More Flutter content [\#](https://supabase.com/blog/flutter-multi-factor-authentication\#more-flutter-content)

- [Flutter Tutorial: building a Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
- [Flutter Authentication and Authorization with RLS](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls)
- [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
- [Write backend code using Dart Edge](https://supabase.com/docs/guides/functions/dart-edge)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&t=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)

[Last post\\
\\
**Supabase Beta April 2023** \\
\\
9 May 2023](https://supabase.com/blog/supabase-beta-update-april-2023)

[Next post\\
\\
**Next steps for Postgres pluggable storage** \\
\\
1 May 2023](https://supabase.com/blog/postgres-pluggable-strorage)

[flutter](https://supabase.com/blog/tags/flutter) [auth](https://supabase.com/blog/tags/auth)

On this page

- [What is Multi-Factor Authentication?](https://supabase.com/blog/flutter-multi-factor-authentication#what-is-multi-factor-authentication)
- [Why Multi-Factor Authentication matters for Flutter apps](https://supabase.com/blog/flutter-multi-factor-authentication#why-multi-factor-authentication-matters-for-flutter-apps)
- [Building the App](https://supabase.com/blog/flutter-multi-factor-authentication#building-the-app)
- [Conclusions and future iterations](https://supabase.com/blog/flutter-multi-factor-authentication#conclusions-and-future-iterations)
- [More Flutter content](https://supabase.com/blog/flutter-multi-factor-authentication#more-flutter-content)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&t=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)