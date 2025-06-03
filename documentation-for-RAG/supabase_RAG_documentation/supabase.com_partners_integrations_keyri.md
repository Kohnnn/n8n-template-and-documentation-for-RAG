---
url: "https://supabase.com/partners/integrations/keyri"
title: "Keyri | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_logo.jpeg&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Keyri

![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_og1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_og2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_og3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

Keyri is an authentication company, providing customers with a simple and secure form of passwordless MFA. Our platform transforms every login into a one-step biometrics-based process that provides a seamless user experience while strengthening account security. Users simply scan a QR code on your login page with their smartphone and pass biometrics in your mobile app to log into your web app.

Incorporating Keyri QR login into your Supabase-based authentication system is a matter of sending the user's `refreshToken` from your mobile app to your web app via the Keyri mobile SDK and web Widget. On the mobile side, just load the `refreshToken` string as the payload into the Keyri method you're using in your app. On the web side, extract the refreshToken string from the payload that the Widget outputs and load it into the setSession method provided by the Supabase JS SDK.

## Documentation

Keyri can be used to incorporate sign-in-with-QR functionality into your Supabase app, allowing users to scan a QR code on your web app with your mobile app and be instantly logged into the web app without having to input any credentials.

Configuration is split into Web and Mobile components. On web, the Keyri QR Widget needs to be installed along with an event listener, and in your mobile app, install the Keyri SDK and pass into it the user's refresh token when sign-in-with-QR is initiated. When the refresh token lands in your web app, it's passed into Supabase's `setSession()` method.

# Sign up for Keyri

First make a free account on the Keyri dashboard ( [https://app.keyri.com](https://app.keyri.com/)). On Add Your Application, set a name and input the domain on which your app will eventually be deployed. You can create multiple application in Keyri to account for your development, staging, and production environments

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/keyri/documentation/HvTIja3KfgKUIMiNVKAqP_screen-shot-2022-10-13-at-21524-pm.png)

Note your application key from the Keys and Credentials section - this will be used in the Mobile portion of the implementation

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/keyri/documentation/KnD6LkWs-PUDtTS1sT9Rz_screen-shot-2022-10-13-at-21746-pm.png)

# Web

Supabase & Keyri \| Web Integration Overview - YouTube

Keyri

8 subscribers

[Supabase & Keyri \| Web Integration Overview](https://www.youtube.com/watch?v=jrjrcpc2PFQ)

Keyri

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

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

[Watch on YouTube](https://www.youtube.com/watch?v=jrjrcpc2PFQ "Watch on YouTube")

For your web app, first download KeyriQR.html (available [here](https://raw.githubusercontent.com/Keyri-Co/library-keyri-connect/main/KeyriQR.html)) and save it to a public directory.

Next, embed KeyriQR.html in your login page as an iFrame within the desired div. This serves as the widget that displays the dynamic QR code and connects with the Keyri API.

`
<div>
    <iframe
        title='KeyriQR'
        src='/KeyriQR.html'
        id='qr-frame'
        height='300'
        width='300'
        scrolling='no'
        style={{ border: 'solid 5px white' }}
      ></iframe>
</div>
`

Next, for the same login view, set up an event listener to pick up the session token that the iFrame emits when the QR code is scanned by your app.

``
useEffect(() => {
    window.addEventListener('message', async (evt) => {
      if (evt.data.keyri && evt.data.data && document.location.origin == evt.origin) {
        const { data } = evt;
        if (!data.error) {
          let refresh_token = JSON.parse(data.data).refreshToken;
          await handleQrLogin(refresh_token);
        } else if (data.error) {
          console.log(`Keyri error: ${data.message}`);
        }
      }
});
``

That's it!

# Mobile

Supabase & Keyri \| Mobile Integration Overview - YouTube

Keyri

8 subscribers

[Supabase & Keyri \| Mobile Integration Overview](https://www.youtube.com/watch?v=oGMsSKyh6tc)

Keyri

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

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

[Watch on YouTube](https://www.youtube.com/watch?v=oGMsSKyh6tc "Watch on YouTube")

### Install Flutter

First, install the Flutter SDK, found at flutter.dev

Make sure to add Flutter to your PATH, for example:

``
export PATH="$PATH:`pwd`/flutter/bin"
``

### Apple - initial setup

Download the latest version of Xcode from the Mac App Store. Make sure the Xcode provided simulator is using a 64-bit device (iPhone 5s or later). You can check the device by viewing the settings in the simulator’s **Hardware > Device** or **File > Open Simulator** menus.

### Android - initial setup

Download the latest version of [Android Studio](https://developer.android.com/studio). Install Android SDK and needed emulator(s).

### Create Project

Run this command in your terminal/shell at the desired location for your new project

`
$ flutter create my_app
`

You can then CD into the new directory, and run the test app with

`
flutter run
`

This is a good test - if things are configured correctly so far you should see the default Flutter test app deployed.

### Add dependencies (Keyri and Supabase)

Open your Pubspec.yaml file, which should be at the top level directory in your new project

Add Keyri and Supabase under **dependencies**

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/keyri/documentation/jlAfOTEchuZpBq8TeXhJZ_screen-shot-2022-09-29-at-060908.png)

One can now access Supabase and Keyri sdks in their Flutter code

### Utilize the two together

1. Make a request to Supabase to authenticate the user
2. Parse the response to extract the token
3. Authenticate using Keyri
1. Below, we show how to utilize the EasyKeyriAuth function, which takes the user through scanning the code, creating the session, displaying the confirmation screen, and finalizing the payload transmission
      - Note - you can find your App Key in the Keyri Developer Portal​
2. Alternatively, intermediate functions in the Keyri SDK, discussed in the mobile docs, can provide control over displaying a custom QR Scanner and/or Confirmation screen

`
// Sign in user with email and password
// Alternatively one can utilize the Supabase API to accomplish the same thing
final response = await client.auth.signIn(email: 'email', password: 'password');
if (response.error != null) {
// Error
    print('Error: ${response.error?.message}');
} else {
    // Success
    final session = response.data;
    // This is the payload that needs to be send through Keyri
    final refreshToken = session.refreshToken
    // EasyKeyriAuth guides the user through scanning and parsing the QR, confirming the session, and configuring the payload
    // One can also use the initiateQRSession method to use the Keyri Scanner with a custom Confirmation screen
    // Or the ProcessLink method if you have your own scanner or are using deep linking
    await keyri
        .easyKeyriAuth([App Key],
            '{"refreshToken":"$refreshToken"}', [email])
        .then((authResult) => _onAuthResult(authResult))
        .catchError((error, stackTrace) => _onError(error));
}
`

## Details

DeveloperKeyri

Category [Auth](https://supabase.com/partners/integrations#auth)

Website [keyri.com](https://keyri.com/?utm_source=supabase-partner-gallery)

Documentation [Learn](https://docs.keyri.com/supabase?utm_source=supabase-partner-gallery)

Third-party integrations and docs are managed by Supabase partners.