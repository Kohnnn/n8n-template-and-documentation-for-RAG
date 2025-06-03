---
url: "https://supabase.com/blog/react-native-authentication"
title: "Getting started with React Native authentication"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Getting started with React Native authentication

16 Nov 2023

•

13 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Getting started with React Native authentication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-16-react-native-authentication%2Freact-native-authentication-supabase.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Authentication is the process of verifying the identity of a user who is attempting to access a system, application, or online service. In this blog post, you will learn about React Native authentication, including native mobile specific login mechanisms like "Sign in with Apple" and "Google One Tap sign-in", as well as SMS & WhatsApp based authentication.

At the end of this blog post, you will have all the components needed to create the ideal authentication experience for your mobile app users.

## Prerequisites [\#](https://supabase.com/blog/react-native-authentication\#prerequisites)

This article assumes you are comfortable with writing a basic application in React Native. No knowledge of Supabase is required.

We will use the following tools

- [Expo](https://docs.expo.dev/get-started/create-a-new-app/) \- we used Expo SDK version 49.0.0 (React Native version 0.72)
- Supabase - create your account [here](https://database.new/) if you do not have one
- IDE of your choosing

Note: We're using Expo as that's the [recommended](https://reactnative.dev/docs/environment-setup) way of getting started with React Native. However, the fundamental approach here applies to bare React Native applications as well.

## Set up supabase-js for React Native [\#](https://supabase.com/blog/react-native-authentication\#set-up-supabase-js-for-react-native)

Using [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction) is the most convenient way of leveraging the full power of the Supabase stack as it conveniently combines all the different services (database, auth, realtime, storage, edge functions) together.

### Install supabase-js and dependencies [\#](https://supabase.com/blog/react-native-authentication\#install-supabase-js-and-dependencies)

After you have created your [Expo project](https://docs.expo.dev/get-started/create-a-project), you can install `supabase-js` and the required dependencies using the following command:

`
npx expo install @supabase/supabase-js @react-native-async-storage/async-storage react-native-url-polyfill
`

### Authentication storage [\#](https://supabase.com/blog/react-native-authentication\#authentication-storage)

By default, supabase-js uses the browser's `localStorage` mechanism to persist the user's session but can be extended with platform specific storage implementations. In React Native we can build native mobile and web applications with the same code base, so we need a storage implementation that works for all these platforms: [react-native-async-storage](https://github.com/react-native-async-storage/async-storage#supported-platforms).

We need to pass an instance of `react-native-async-storage` to supabase-js to make sure authentication works reliably across all react native platforms:

lib/supabase.ts

`
import 'react-native-url-polyfill/auto'
import AsyncStorage from '@react-native-async-storage/async-storage'
import { createClient } from '@supabase/supabase-js'
const supabaseUrl = YOUR_REACT_NATIVE_SUPABASE_URL
const supabaseAnonKey = YOUR_REACT_NATIVE_SUPABASE_ANON_KEY
export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
auth: {
    storage: AsyncStorage,
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: false,
},
})
`

You can find your URL and anon key in the [API credentials section](https://supabase.com/dashboard/project/_/settings/api) of the Supabase dashboard.

### Encrypting the user session [\#](https://supabase.com/blog/react-native-authentication\#encrypting-the-user-session)

If you wish to encrypt the user's session information, you can use `aes-js` and store the encryption key in [Expo SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore). The [`aes-js` library](https://github.com/ricmoo/aes-js) is a reputable JavaScript-only implementation of the AES encryption algorithm in CTR mode. A new 256-bit encryption key is generated using the `react-native-get-random-values` library. This key is stored inside Expo's SecureStore, while the value is encrypted and placed inside AsyncStorage.

Please make sure that:

- You keep the `expo-secure-storage`, `aes-js` and `react-native-get-random-values` libraries up-to-date.
- Choose the correct [`SecureStoreOptions`](https://docs.expo.dev/versions/latest/sdk/securestore/#securestoreoptions) for your app's needs. E.g. [`SecureStore.WHEN_UNLOCKED`](https://docs.expo.dev/versions/latest/sdk/securestore/#securestorewhen_unlocked) regulates when the data can be accessed.
- Carefully consider optimizations or other modifications to the above example, as those can lead to introducing subtle security vulnerabilities.

Install the necessary dependencies in the root of your Expo project:

`
npm install @supabase/supabase-js
npm install @rneui/themed @react-native-async-storage/async-storage react-native-url-polyfill
npm install aes-js react-native-get-random-values
npx expo install expo-secure-store
`

Implement a `LargeSecureStore` class to pass in as Auth storage for the `supabase-js` client:

lib/supabase.ts

`
import 'react-native-url-polyfill/auto'
import { createClient } from '@supabase/supabase-js'
import AsyncStorage from '@react-native-async-storage/async-storage'
import * as SecureStore from 'expo-secure-store'
import * as aesjs from 'aes-js'
import 'react-native-get-random-values'
// As Expo's SecureStore does not support values larger than 2048
// bytes, an AES-256 key is generated and stored in SecureStore, while
// it is used to encrypt/decrypt values stored in AsyncStorage.
class LargeSecureStore {
private async _encrypt(key: string, value: string) {
    const encryptionKey = crypto.getRandomValues(new Uint8Array(256 / 8))
    const cipher = new aesjs.ModeOfOperation.ctr(encryptionKey, new aesjs.Counter(1))
    const encryptedBytes = cipher.encrypt(aesjs.utils.utf8.toBytes(value))
    await SecureStore.setItemAsync(key, aesjs.utils.hex.fromBytes(encryptionKey))
    return aesjs.utils.hex.fromBytes(encryptedBytes)
}
private async _decrypt(key: string, value: string) {
    const encryptionKeyHex = await SecureStore.getItemAsync(key)
    if (!encryptionKeyHex) {
      return encryptionKeyHex
    }
    const cipher = new aesjs.ModeOfOperation.ctr(
      aesjs.utils.hex.toBytes(encryptionKeyHex),
      new aesjs.Counter(1)
    )
    const decryptedBytes = cipher.decrypt(aesjs.utils.hex.toBytes(value))
    return aesjs.utils.utf8.fromBytes(decryptedBytes)
}
async getItem(key: string) {
    const encrypted = await AsyncStorage.getItem(key)
    if (!encrypted) {
      return encrypted
    }
    return await this._decrypt(key, encrypted)
}
async removeItem(key: string) {
    await AsyncStorage.removeItem(key)
    await SecureStore.deleteItemAsync(key)
}
async setItem(key: string, value: string) {
    const encrypted = await this._encrypt(key, value)
    await AsyncStorage.setItem(key, encrypted)
}
}
const supabaseUrl = YOUR_REACT_NATIVE_SUPABASE_URL
const supabaseAnonKey = YOUR_REACT_NATIVE_SUPABASE_ANON_KEY
const supabase = createClient(supabaseUrl, supabaseAnonKey, {
auth: {
    storage: new LargeSecureStore(),
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: false,
},
})
`

## Email and password authentication in React Native [\#](https://supabase.com/blog/react-native-authentication\#email-and-password-authentication-in-react-native)

Once we've set up the storage mechanism, building an email and password sign in flow becomes pretty straight forward. Install [`@rneui/themed`](https://reactnativeelements.com/) to get some nice cross platform button and input fields:

`
npm install @rneui/themed
`

Set up a simple email form component:

components/EmailForm.tsx

`
import React, { useState } from 'react'
import { Alert, StyleSheet, View } from 'react-native'
import { supabase } from '../lib/supabase'
import { Button, Input } from '@rneui/themed'
export default function EmailForm() {
const [email, setEmail] = useState('')
const [password, setPassword] = useState('')
const [loading, setLoading] = useState(false)
async function signInWithEmail() {
    setLoading(true)
    const { error } = await supabase.auth.signInWithPassword({
      email: email,
      password: password,
    })
    if (error) Alert.alert(error.message)
    setLoading(false)
}
async function signUpWithEmail() {
    setLoading(true)
    const {
      data: { session },
      error,
    } = await supabase.auth.signUp({
      email: email,
      password: password,
    })
    if (error) Alert.alert(error.message)
    if (!session) Alert.alert('Please check your inbox for email verification!')
    setLoading(false)
}
return (
    <View style={styles.container}>
      <View style={[styles.verticallySpaced, styles.mt20]}>
        <Input
          label="Email"
          leftIcon={{ type: 'font-awesome', name: 'envelope' }}
          onChangeText={(text) => setEmail(text)}
          value={email}
          placeholder="email@address.com"
          autoCapitalize={'none'}
        />
      </View>
      <View style={styles.verticallySpaced}>
        <Input
          label="Password"
          leftIcon={{ type: 'font-awesome', name: 'lock' }}
          onChangeText={(text) => setPassword(text)}
          value={password}
          secureTextEntry={true}
          placeholder="Password"
          autoCapitalize={'none'}
        />
      </View>
      <View style={[styles.verticallySpaced, styles.mt20]}>
        <Button title="Sign in" disabled={loading} onPress={() => signInWithEmail()} />
      </View>
      <View style={styles.verticallySpaced}>
        <Button title="Sign up" disabled={loading} onPress={() => signUpWithEmail()} />
      </View>
    </View>
)
}
const styles = StyleSheet.create({
container: {
    marginTop: 40,
    padding: 12,
},
verticallySpaced: {
    paddingTop: 4,
    paddingBottom: 4,
    alignSelf: 'stretch',
},
mt20: {
    marginTop: 20,
},
})
`

Note, by default Supabase Auth requires email verification before a session is created for the users. To support email verification you need to implement deep link handling which is outlined in the next section.

While testing, you can disable email confirmation in your [project's email auth provider settings](https://supabase.com/dashboard/project/_/auth/providers).

## OAuth, magic links and deep-linking [\#](https://supabase.com/blog/react-native-authentication\#oauth-magic-links-and-deep-linking)

As you saw above, we specified `detectSessionInUrl: false` when initializing supabase-js. By default, in a web based environment, supabase-js will automatically detect OAuth and magic link redirects and create the user session.

In native mobile apps, however, OAuth callbacks require a bit more configuration and the setup of [deep linking](https://supabase.com/docs/guides/auth/native-mobile-deep-linking).

To link to your development build or standalone app, you need to specify a custom URL scheme for your app. You can register a scheme in your app config (app.json, app.config.js) by adding a string under the `scheme` key:

`
{
"expo": {
    "scheme": "com.supabase"
}
}
`

In your project's [auth settings](https://supabase.com/dashboard/project/_/auth/url-configuration) add the redirect URL, e.g. `com.supabase://**`.

Finally, implement the OAuth and linking handlers. See the [supabase-js reference](https://supabase.com/docs/reference/javascript/initializing?example=react-native-options-async-storage) for instructions on initializing the supabase-js client in React Native.

./components/Auth.tsx

`
import { Button } from 'react-native'
import { makeRedirectUri } from 'expo-auth-session'
import * as QueryParams from 'expo-auth-session/build/QueryParams'
import * as WebBrowser from 'expo-web-browser'
import * as Linking from 'expo-linking'
import { supabase } from 'app/utils/supabase'
WebBrowser.maybeCompleteAuthSession() // required for web only
const redirectTo = makeRedirectUri()
const createSessionFromUrl = async (url: string) => {
const { params, errorCode } = QueryParams.getQueryParams(url)
if (errorCode) throw new Error(errorCode)
const { access_token, refresh_token } = params
if (!access_token) return
const { data, error } = await supabase.auth.setSession({
    access_token,
    refresh_token,
})
if (error) throw error
return data.session
}
const performOAuth = async () => {
const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'github',
    options: {
      redirectTo,
      skipBrowserRedirect: true,
    },
})
if (error) throw error
const res = await WebBrowser.openAuthSessionAsync(data?.url ?? '', redirectTo)
if (res.type === 'success') {
    const { url } = res
    await createSessionFromUrl(url)
}
}
const sendMagicLink = async () => {
const { error } = await supabase.auth.signInWithOtp({
    email: 'example@email.com',
    options: {
      emailRedirectTo: redirectTo,
    },
})
if (error) throw error
// Email sent.
}
export default function Auth() {
// Handle linking into app from email app.
const url = Linking.useURL()
if (url) createSessionFromUrl(url)
return (
    <>
      <Button onPress={performOAuth} title="Sign in with Github" />
      <Button onPress={sendMagicLink} title="Send Magic Link" />
    </>
)
}
`

For the best user experience, it is recommended to use universal links which require a more elaborate setup. You can find the detailed setup instructions in the [Expo docs](https://docs.expo.dev/guides/deep-linking/).

## Native mobile login mechanisms [\#](https://supabase.com/blog/react-native-authentication\#native-mobile-login-mechanisms)

![Sign in with Apple Demo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-16-react-native-authentication%2Fsign_in_with_apple_google.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Some native mobile operating systems, like iOS and Android, offer a built-in identity provider for convenient user authentication.

For iOS, apps that use a third-party or social login service to set up or authenticate the user’s primary account with the app must also offer Sign in with Apple as an equivalent option.

There are several benefits and reasons why you might want to add social login to your applications:

- **Improved user experience**: Users can register and log in to your application using their existing app store accounts, which can be faster and more convenient than creating a new account from scratch. This makes it easier for users to access your application, improving their overall experience.

- **Better user engagement**: You can access additional data and insights about your users, such as their interests, demographics, and social connections. This can help you tailor your content and marketing efforts to better engage with your users and provide a more personalized experience.

- **Increased security**: Social login can improve the security of your application by leveraging the security measures and authentication protocols of the social media platforms that your users are logging in with. This can help protect against unauthorized access and account takeovers.


### Sign in with Apple [\#](https://supabase.com/blog/react-native-authentication\#sign-in-with-apple)

Supabase Auth supports using [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) on the web and in native apps for iOS, macOS, watchOS, or tvOS.

For detailed setup and implementation instructions please refer to the [docs](https://supabase.com/docs/guides/auth/social-login/auth-apple) and the [video tutorial](https://youtu.be/-tpcZzTdvN0).

### Sign in with Google [\#](https://supabase.com/blog/react-native-authentication\#sign-in-with-google)

Supabase Auth supports Sign in with Google on the web, native Android applications, and Chrome extensions.

For detailed set up and implementation instructions please refer to the [docs](https://supabase.com/docs/guides/auth/social-login/auth-google) and the [video tutorial](https://youtu.be/vojHmGUGUGc).

## One time passwords [\#](https://supabase.com/blog/react-native-authentication\#one-time-passwords)

Supabase supports various forms of passwordless authentication:

- [Email Magic Link](https://supabase.com/docs/guides/auth/passwordless-login/auth-magic-link)
- [Email one-time password (OTP)](https://supabase.com/docs/guides/auth/passwordless-login/auth-email-otp)
- [SMS & WhatsApp one-time password (OTP)](https://supabase.com/docs/guides/auth/phone-login) (watch the [video tutorial](https://youtu.be/Hca4CKE17I0?feature=shared))

Passwordless login mechanisms have similar benefits as the native mobile login options mentioned above.

## Conclusion [\#](https://supabase.com/blog/react-native-authentication\#conclusion)

In this post, we learned various authentication mechanisms we can use in React Native applications to provide a delightful experience for our users across native mobile and web.

## More React Native and Supabase resources [\#](https://supabase.com/blog/react-native-authentication\#more-react-native-and-supabase-resources)

- [Watch our React Native video tutorials](https://youtube.com/playlist?list=PL5S4mPUpp4OsrbRTx21k34aACOgpqQGlx&si=Ez-0S4QhBxtayYsq)
- [React Native file upload with Supabase Storage](https://supabase.com/blog/react-native-storage)
- [Offline-first React Native Apps with WatermelonDB](https://supabase.com/blog/react-native-offline-first-watermelon-db)
- [Send push notifications from edge functions](https://supabase.com/docs/guides/functions/examples/push-notifications)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-authentication&text=Getting%20started%20with%20React%20Native%20authentication)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-authentication&text=Getting%20started%20with%20React%20Native%20authentication)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-authentication&t=Getting%20started%20with%20React%20Native%20authentication)

[Last post\\
\\
**GitHub OAuth in your Python Flask app** \\
\\
21 November 2023](https://supabase.com/blog/oauth2-login-python-flask-apps)

[Next post\\
\\
**Supabase Beta October 2023** \\
\\
6 November 2023](https://supabase.com/blog/beta-update-october-2023)

[react-native](https://supabase.com/blog/tags/react-native) [auth](https://supabase.com/blog/tags/auth)

On this page

- [Prerequisites](https://supabase.com/blog/react-native-authentication#prerequisites)
- [Set up supabase-js for React Native](https://supabase.com/blog/react-native-authentication#set-up-supabase-js-for-react-native)
  - [Install supabase-js and dependencies](https://supabase.com/blog/react-native-authentication#install-supabase-js-and-dependencies)
  - [Authentication storage](https://supabase.com/blog/react-native-authentication#authentication-storage)
  - [Encrypting the user session](https://supabase.com/blog/react-native-authentication#encrypting-the-user-session)
- [Email and password authentication in React Native](https://supabase.com/blog/react-native-authentication#email-and-password-authentication-in-react-native)
- [OAuth, magic links and deep-linking](https://supabase.com/blog/react-native-authentication#oauth-magic-links-and-deep-linking)
- [Native mobile login mechanisms](https://supabase.com/blog/react-native-authentication#native-mobile-login-mechanisms)
  - [Sign in with Apple](https://supabase.com/blog/react-native-authentication#sign-in-with-apple)
  - [Sign in with Google](https://supabase.com/blog/react-native-authentication#sign-in-with-google)
- [One time passwords](https://supabase.com/blog/react-native-authentication#one-time-passwords)
- [Conclusion](https://supabase.com/blog/react-native-authentication#conclusion)
- [More React Native and Supabase resources](https://supabase.com/blog/react-native-authentication#more-react-native-and-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-authentication&text=Getting%20started%20with%20React%20Native%20authentication)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-authentication&text=Getting%20started%20with%20React%20Native%20authentication)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-authentication&t=Getting%20started%20with%20React%20Native%20authentication)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)