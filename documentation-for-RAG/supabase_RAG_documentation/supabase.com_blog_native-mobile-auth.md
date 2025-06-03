---
url: "https://supabase.com/blog/native-mobile-auth"
title: "Native Mobile Auth Support for Google and Apple Sign in"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Native Mobile Auth Support for Google and Apple Sign in

27 Jun 2023

•

3 minute read

[![Stojan Dimitrovski avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fhf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Stojan DimitrovskiEngineering](https://github.com/hf)

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Native Mobile Auth Support for Google and Apple Sign in](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnative-mobile-auth%2Fnative-mobile-auth.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase supports OAuth logins with 17 providers including Apple, Google, Microsoft, GitHub, … But for native mobile apps, this meant that developers had to use a web browser to sign in. It’s not an ideal flow for users, who are already used to signing in with the operating system’s native dialogs when possible. Today, we are excited to announce full native support for Sign in with Apple and Google on iOS and Android. But this is not all! Supabase Auth now can now be used with one-tap sign in methods like: Sign in with Apple JS, Sign in with Google for Web or even in Chrome extensions.

## Native Sign in with Apple and Google [\#](https://supabase.com/blog/native-mobile-auth\#native-sign-in-with-apple-and-google)

Developers of native iOS and Android apps (using Flutter or React Native) can now take advantage of OS-provided authentication dialogs for Apple and Google. This is available on iOS, macOS, tvOS and watchOS apps in the Apple ecosystem, and all Android variants in the Google ecosystem.

In full transparency, this was always sort-of possible but there were some edge cases that were not covered well with Supabase Auth. We’ve since ironed out the developer experience and made this into a fully supported feature.

Behind the scenes, these native sign in methods use ID tokens. They’re a formalized version of a JWT that is issued by Apple or Google and contain profile information. Supabase Auth now can properly validate the ID tokens and create new or link to existing user accounts based on email similarity.

- Sign in with Apple \[ [Web](https://supabase.com/docs/guides/auth/social-login/auth-apple?platform=web) \| [React Native](https://supabase.com/docs/guides/auth/social-login/auth-apple?platform=react-native) \| [Flutter](https://supabase.com/docs/guides/auth/social-login/auth-apple?platform=flutter) \| [Swift](https://supabase.com/docs/guides/auth/social-login/auth-apple?platform=swift) \| [Kotlin](https://supabase.com/docs/guides/auth/social-login/auth-apple?platform=kotlin)\]
- Sign in with Google \[ [Web](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=web) \| [React Native](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=react-native) \| [Flutter](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=flutter) \| [Android](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=android) \| [Chrome Extensions](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=chrome-extensions)\]

## Sign in with Apple JS, Google One Tap and Chrome Extensions [\#](https://supabase.com/blog/native-mobile-auth\#sign-in-with-apple-js-google-one-tap-and-chrome-extensions)

Although sign in on native platforms was the focus of the team when working on this feature, incidentally we’ve added proper support for Sign in with Apple JS, Google’s One Tap and support for authenticating within Google Chrome extensions.

You can now take advantage of these web frameworks, most notably Google’s One Tap and Automatic Sign-in support for a frictionless onboarding experience for your users.

All you need to do is configure the web frameworks and use the `signInWithIdToken()` method to pass the ID token provided by the Google and Apple libraries.

For example, to use Google One tap you should first [generate an embed code for the Google Sign in Button](https://developers.google.com/identity/gsi/web/tools/configurator). Register this method as the callback that will receive the authentication response from the button:

`
async function handleSignInWithGoogle(response) {
const { data, error } = await supabase.auth.signInWithIdToken({
    token: response.credential,
    nonce: 'NONCE', // must be the same one as provided in data-nonce (if any)
})
}
`

## Resources [\#](https://supabase.com/blog/native-mobile-auth\#resources)

- [Login with Apple Guide](https://supabase.com/docs/guides/auth/social-login/auth-apple)
- [Login with Google Guide](https://supabase.com/docs/guides/auth/social-login/auth-google)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnative-mobile-auth&text=Native%20Mobile%20Auth%20Support%20for%20Google%20and%20Apple%20Sign%20in)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnative-mobile-auth&text=Native%20Mobile%20Auth%20Support%20for%20Google%20and%20Apple%20Sign%20in)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnative-mobile-auth&t=Native%20Mobile%20Auth%20Support%20for%20Google%20and%20Apple%20Sign%20in)

[Last post\\
\\
**Supabase Beta June 2023** \\
\\
6 July 2023](https://supabase.com/blog/supabase-beta-update-june-2023)

[Next post\\
\\
**Supabase Beta May 2023** \\
\\
9 June 2023](https://supabase.com/blog/supabase-beta-update-may-2023)

[auth](https://supabase.com/blog/tags/auth)

On this page

- [Native Sign in with Apple and Google](https://supabase.com/blog/native-mobile-auth#native-sign-in-with-apple-and-google)
- [Sign in with Apple JS, Google One Tap and Chrome Extensions](https://supabase.com/blog/native-mobile-auth#sign-in-with-apple-js-google-one-tap-and-chrome-extensions)
- [Resources](https://supabase.com/blog/native-mobile-auth#resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnative-mobile-auth&text=Native%20Mobile%20Auth%20Support%20for%20Google%20and%20Apple%20Sign%20in)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnative-mobile-auth&text=Native%20Mobile%20Auth%20Support%20for%20Google%20and%20Apple%20Sign%20in)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnative-mobile-auth&t=Native%20Mobile%20Auth%20Support%20for%20Google%20and%20Apple%20Sign%20in)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)