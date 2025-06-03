---
url: "https://supabase.com/blog/oauth2-login-python-flask-apps"
title: "GitHub OAuth in your Python Flask app"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# GitHub OAuth in your Python Flask app

21 Nov 2023

•

5 minute read

[![Andrew Smith avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsilentworks.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Andrew SmithDevRel & DX](https://github.com/silentworks)

![GitHub OAuth in your Python Flask app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foauth2-login-python-flask-apps%2Fflask-supabase-auth.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

In this guide we'll learn how to quickly build an OAuth2.0 integration into a simple Flask app using Supabase-py. This will enable your users to login to your web app using their GitHub account.

## Prerequisites [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#prerequisites)

This article assumes you are familiar with creating an application in Flask. It also assumes that you have read the Supabase documentation and are familiar the with concept of [Authentication](https://supabase.com/docs/guides/auth).

We'll use the following tools:

- [Flask](https://flask.palletsprojects.com/en/3.0.x/) \- we used version 2.3.3 for this article
- Supabase Dashboard - [create an account](https://database.new/) if you don't have one already

## Getting started [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#getting-started)

To begin, inside your Flask application install the `supabase` library using the following command in the terminal:

`
pip install supabase
`

## Session storage [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#session-storage)

Open the project in your preferred code editor and create a file called `flask_storage.py` with the following content:

`
from gotrue import SyncSupportedStorage
from flask import session
class FlaskSessionStorage(SyncSupportedStorage):
    def __init__(self):
        self.storage = session
    def get_item(self, key: str) -> str | None:
        if key in self.storage:
            return self.storage[key]
    def set_item(self, key: str, value: str) -> None:
        self.storage[key] = value
    def remove_item(self, key: str) -> None:
        if key in self.storage:
            self.storage.pop(key, None)
`

In this file, we're extending the `SyncSupportedStorage` class from the `gotrue` library which comes bundled with the `supabase` library. Here we're telling the Supabase authentication library ( `gotrue`) how to retrieve, store and remove a session that will store our JSON Web Token (JWT).

## Initiate the client [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#initiate-the-client)

Create another file called `supabase_client.py` and in this file, we'll initiate our Supabase client.

`
import os
from flask import g
from werkzeug.local import LocalProxy
from supabase.client import Client, ClientOptions
from flask_storage import FlaskSessionStorage
url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")
def get_supabase() -> Client:
    if "supabase" not in g:
        g.supabase = Client(
            url,
            key,
            options=ClientOptions(
                storage=FlaskSessionStorage(),
                flow_type="pkce"
            ),
        )
    return g.supabase
supabase: Client = LocalProxy(get_supabase)
`

Let's focus on the `get_supabase` function. Here we are checking if we have an instance of the client stored in our global object `g`, if not we create the client and store it in the global object under the `supabase` name. You will notice in the `ClientOptions` that we are specifying the `FlaskSessionStorage` class we created earlier and we are also specifying a very important option that allows us to handle the OAuth flow on the server side, the `flow_type="pkce"`.

## Sign in with GitHub [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#sign-in-with-github)

Supabase Auth supports Sign in with GitHub on the web, native Android applications, and Chrome extensions.

For detailed set up and implementation instructions please refer to the [docs](https://supabase.com/docs/guides/auth/social-login/auth-github).

## Create sign-in route [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#create-sign-in-route)

Inside our application code `app.py`, we can create the sign-in route to trigger the OAuth sign-in request.

`
@app.route("/signin/github")
def signin_with_github():
    res = supabase.auth.sign_in_with_oauth(
        {
            "provider": "github",
            "options": {
	            "redirect_to": f"{request.host_url}callback"
	        },
        }
    )
    return redirect(res.url)
`

In this function `options` object we specify a `redirect_to` parameter which will point to the callback route we will create in the next step. This function will generate a url for us to use to redirect the user to, in this case we are using `github` as our OAuth provider so we will be redirected to the GitHub OAuth consent screen.

## Create callback route [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#create-callback-route)

Let's add another route to our `app.py` file for the callback endpoint we specified in our sign in route.

`
@app.route("/callback")
def callback():
    code = request.args.get("code")
    next = request.args.get("next", "/")
    if code:
        res = supabase.auth.exchange_code_for_session({"auth_code": code})
    return redirect(next)
`

Here we're getting the `code` query parameter from the request object, if this is available we then exchange the code for a session so that the user will be signed in. Under the hood the `supabase` python library will handle storing this session (JWT) into a cookie and sign the user in.

## Conclusion [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#conclusion)

In this post we explained how to setup a flask session storage to work with the Supabase python library, setting the `flow_type` to use Proof Key for Code Exchange (PKCE) and creating a sign in and a callback route to handle the user authentication.

## More Resources [\#](https://supabase.com/blog/oauth2-login-python-flask-apps\#more-resources)

- [supabase-py reference docs](https://supabase.com/docs/reference/python/installing)
- [supabase-py GitHub repo](https://github.com/supabase-community/supabase-py)
- [Deep Dive series on auth concepts in Supabase](https://supabase.com/docs/learn/auth-deep-dive/auth-deep-dive-jwts)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&t=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)

[Last post\\
\\
**Automatic CLI login** \\
\\
1 December 2023](https://supabase.com/blog/automatic-cli-login)

[Next post\\
\\
**Getting started with React Native authentication** \\
\\
16 November 2023](https://supabase.com/blog/react-native-authentication)

[python](https://supabase.com/blog/tags/python) [auth](https://supabase.com/blog/tags/auth)

On this page

- [Prerequisites](https://supabase.com/blog/oauth2-login-python-flask-apps#prerequisites)
- [Getting started](https://supabase.com/blog/oauth2-login-python-flask-apps#getting-started)
- [Session storage](https://supabase.com/blog/oauth2-login-python-flask-apps#session-storage)
- [Initiate the client](https://supabase.com/blog/oauth2-login-python-flask-apps#initiate-the-client)
- [Sign in with GitHub](https://supabase.com/blog/oauth2-login-python-flask-apps#sign-in-with-github)
- [Create sign-in route](https://supabase.com/blog/oauth2-login-python-flask-apps#create-sign-in-route)
- [Create callback route](https://supabase.com/blog/oauth2-login-python-flask-apps#create-callback-route)
- [Conclusion](https://supabase.com/blog/oauth2-login-python-flask-apps#conclusion)
- [More Resources](https://supabase.com/blog/oauth2-login-python-flask-apps#more-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&t=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)