---
url: "https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages"
title: "Slack Consolidate: a slackbot built with Python and Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Slack Consolidate: a slackbot built with Python and Supabase

09 Aug 2022

•

15 minute read

[![Rodrigo Mansueli avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmansueli.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Rodrigo MansueliSupport Engineer](https://github.com/mansueli)

![Slack Consolidate: a slackbot built with Python and Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2Fslackbot-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase is a platform-as-a-service built on top of PostgreSQL and [many other amazing open-source tools](https://supabase.com/docs/guides/getting-started/architecture). It’s a fantastic option to create data-intensive apps and tooling. Taking advantage of the community-made [Python SDK](https://github.com/supabase-community/supabase-py) and [Slack's Python SDK](https://slack.dev/python-slack-sdk/), you can automate tasks and build apps for several use cases.

## Prerequisites [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#prerequisites)

Before we dive in, let’s look at some prerequisites you'll need:

- [Supabase Client](https://pypi.org/project/supabase/)
  - The SDK only supports Python > 3.7. You can download a supported Python version from [here](https://www.python.org/downloads/).
    `pip install supabase`
- [Python dotenv](https://pypi.org/project/python-dotenv/) to handle API keys without exposing them in the code
  - This is optional, but it will avoid issues of package dependencies and version conflicts.
    **`pip install python-dotenv`**
- [Slack SDK](https://pypi.org/project/slack-sdk/) for Python
  - This is needed to create the Slack bot
    **`pip install slack-sdk`**

### Creating the App in Slack [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#creating-the-app-in-slack)

Now, it is time to create the bot in Slack and get the API Keys (after granting the required scopes)

[https://api.slack.com/apps](https://api.slack.com/apps)

![Green arrow pointing to the ‘Create New App’ button.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F00_create_new_app.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Green arrow pointing to the ‘Create New App’ button.

Then, select to create an app from a manifest (this will already set the required permissions) for the app:

![Green arrow pointing to the option ‘From an app manifest’ inside the “Create an app” menu.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F01_create_an_slack_app.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Green arrow pointing to the option ‘From an app manifest’ inside the “Create an app” menu.

Select the Slack workspace to deploy:

![The picture shows a dropdown UI with Supabase selected as the workspace.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F02_pick_workspace.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The picture shows a dropdown UI with Supabase selected as the workspace.

`Manifest.yaml`

`
display_information:
name: SlackConsolidate
features:
bot_user:
display_name: SlackConsolidate
always_online: false
oauth_config:
scopes:
user:
  - channels:history
  - channels:read
  - channels:write
  - chat:write
  - links:read
  - users:read
  - groups:history
  - groups:read
  - mpim:history
  - im:history
bot:
  - channels:history
  - channels:read
  - links:read
  - chat:write.public
  - chat:write
  - channels:join
settings:
org_deploy_enabled: false
socket_mode_enabled: false
token_rotation_enabled: false
`

Enter the manifest above when asked:

![The picture shows the place where you have to paste the manifest file included in the repo.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F03_enter_manifest.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The picture shows the place where you have to paste the manifest file included in the repo.

Then, confirm to create the bot:

![You can see a summary screen to confirm the creation of the bot and the scopes assigned.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F04_confirm_window.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can see a summary screen to confirm the creation of the bot and the scopes assigned.

## Granting access to the bot: [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#granting-access-to-the-bot)

Install the app on the workspace:

![The picture shows the button to Install the App to the Slack Workspace.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F05_install_workspace.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The picture shows the button to Install the App to the Slack Workspace.

Inviting the bot to the channels, it will post messages on:

The command to invite the bot is below:

`/invite @SlackConsolidate`

![The picture shows the command /invite @Slackbot in the channel #team-support.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F06_invite_bot_to_channel.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The picture shows the command /invite @Slackbot in the channel #team-support.

Now, we are done with Slack for now. Let's create some buffer tables in Supabase.

## Creating Tables in Supabase [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#creating-tables-in-supabase)

Create an account [here](https://supabase.com/dashboard/) (if you don't have one yet).

We will be using Supabase's [database](https://supabase.com/docs/guides/database) and the Python [client Libraries](https://supabase.com/docs/guides/client-libraries#managing-data). First, we will create one table to store the channels that are being watched and where they are going to send the message which works analogously to a multiplexer circuit. Since you may want to watch several channels but split them into a smaller buffer e.g VIP / Enterprise, etc.

Go to the SQL Editor and run this:

`
CREATE TABLE slack_channels (
    id SERIAL PRIMARY KEY,
    channel text,
    channel_id text,
    p_level text DEFAULT ''::text NOT NULL,
    dest_channel text,
    dest_channel_id text,
    private int DEFAULT '0'::int NOT NULL
);
CREATE TABLE slack_watcher (
    channel_name text,
    channel_id text NOT NULL,
    message text,
    ts timestamp with time zone NOT NULL,
    ts_ms text NOT NULL,
    CONSTRAINT pk_slackwatcher PRIMARY KEY (channel_id, ts, ts_ms)
);
`

## Adding channels to the watch list and setting the destination channel: [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#adding-channels-to-the-watch-list-and-setting-the-destination-channel)

You may want to call [conversations.list](https://api.slack.com/methods/conversations.list) to dump all the channels and channel IDs into a CSV file, then use it to populate the table `slack_channels`. You can also manually get the data, but copying the links to messages in the channels:

![After right-clicking a message in Slack, you can see the option to select the link.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F07_copy_msg_link.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

After right-clicking a message in Slack, you can see the option to select the link.

Slack links have the following format:

https://ORGANIZATION.slack.com/archives/
channel\_id/pmessage\_id

Organization: subdomain used in Slack

Channel ID: It is the string that you'll need to enter
in slack channels as the channel id e.g C0000ABC02DE

The name of the channel is not needed. But it is recommended to set, it so you can filter and find this information later on if needed. You can ignore everything else when setting the table for `slack_channels`

### Examples of adding data to the channel's list: [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#examples-of-adding-data-to-the-channels-list)

**Method 1:**

Using Supabase UI (easier):

![The green arrow points to insert row button inside Supabase.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F08_insert_row.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The green arrow points to insert row button inside Supabase.

Then, enter the information as needed:

![The picture shows the UI in Supabase to insert a new row to the database table.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F09_insert_row_b.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The picture shows the UI in Supabase to insert a new row to the database table.

**Method 2:**

Go to [SQL Editor](https://supabase.com/dashboard/project/_/sql) and run insert commands:

Inserting a public channel named #support-channel to be monitored:

`
insert into slack_channels
(channel, channel_id, p_level, dest_channel, dest_channel_id, private)
values
('support-channel', 'C0000ABC02DE', 'Support msgs', 'all_them_messages', 'C0000ABC02DF', 0);
`

Inserting a **private** channel named #support-enterprise to be monitored:

`
insert into slack_channels
(channel, channel_id, p_level, dest_channel, dest_channel_id, private)
values
(
    'support-enterprise',
    'C0000ABC02DC',
    'Enterprise Support msgs',
    'all_them_messages',
    'C0000ABC02DF',
    1
);
`

Notes:

`p_level` is an optional message that will be included in with the message e.g **VIP customer.**

`private` is an integer field that should be set to 1 if the channel has a 🔒padlock before the name (not a public channel).

`channel_id` is the source channel ID and `dest_channel_id` is the ID of the channel where the bot will post the message.

## Setting up the environment File: [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#setting-up-the-environment-file)

You need to get the supabase URL and API keys from here:

[https://supabase.com/dashboard/project/\_/settings/api](https://supabase.com/dashboard/project/_/settings/api)

![The picture illustrates where to get the URL and the service key to setup the environment variables.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F10_copy_supabase_apis.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The picture illustrates where to get the URL and the service key to setup the environment variables.

Slack environment variables:

Then, copy the bot and person API Tokens for the bot:

![The picture has arrows pointing to the tokens that will be used as environment variables from Slack.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fslackbot-consolidate%2F11_copy_slack_apis.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The picture has arrows pointing to the tokens that will be used as environment variables from Slack.

Now, you have everything needed to set up the environment file. Please note that Slack ORG is the subdomain of your slack organization i.e supabase for supabase.slack.com

The environment file:

`
SUPABASE_URL=https://XXXX.supabase.co
SUPABASE_KEY=eyJhbGc_SUP4N4CH0_IkpXVCJ9.SUPAKEY_*
SLACK_TOKEN=xoxp-Slack_PERSON_TOKEN
SLACK_BOT_TOKEN=xoxb-Slack_BOT_TOKEN
SLACK_ORG=slack_sub_domain
`

## Now, we can run the bot: [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#now-we-can-run-the-bot)

It works in a similar fashion to Arduino / PIC processors of an infinity loop looking for new data and performing tasks.

`
import time
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from supabase import create_client, Client
from datetime import datetime
from dotenv import dotenv_values
logger = logging.getLogger(__name__)
config = dotenv_values(".env")
bot_client = WebClient(token=config['SLACK_BOT_TOKEN'])
client = WebClient(token=config['SLACK_TOKEN'])
SUPABASE_URL=config['SUPABASE_URL']
SUPABASE_KEY=config['SUPABASE_KEY']
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
SLACK_ORG = config['SLACK_ORG']
SLACK_ORG_LINK = f"https://{SLACK_ORG}.slack.com/archives/"
############
# Config:
############
# 1.4 seconds should be the minimum to avoid passing Slack API limits.
# https://api.slack.com/docs/rate-limits#tier_t3
POOLING_DELAY = 1.4
# Check if new channels were added each hour.
SCAN_CHANNELS_DELAY = 3600.0
BUFFER_SIZE = 20
class SlackChannel:
def __init__(self, id, name, p_level, dest_channel_id, dest_channel, private):
    """_summary_
      Args:
          id (str): Slack channel ID from the source channel
          name (str): Name of the source channel (used in logging)
          p_level (str): (Optional message) added when posting
          dest_channel_id (str): Slack channel ID for the destination channel
          dest_channel (str): Name of the destination channel (used in logging)
          private (int): Integer to check if the channel is private (private==1) or public channel
      Returns:
          SlackChannel: object
    """
    self.id = id
    self.name = name
    self.p_level = p_level
    self.dest_channel = dest_channel
    self.dest_channel_id  = dest_channel_id
    self.private  = private
def setup():
    """_summary_
        Fetches the list of channels from Supabase and returns them in a dict()
    Returns:
        dict: Dictionary with SlackChannel objects.
    """
    channels = dict()
    data = supabase.from_("slack_channels").select("channel_id, channel, p_level, dest_channel, dest_channel_id, private").execute().data
    data_dic = data
    for row in data_dic:
        channels[row['channel_id']] = SlackChannel(id = row['channel_id'],
        name = row['channel'],
        p_level = row['p_level'],
        dest_channel = row['dest_channel'],
        dest_channel_id = row['dest_channel_id'],
        private = row['private'])
    return channels
def post(src_channel, link, message):
    """_summary_
        Post a message from a source channel into the destination channel
    Args:
        src_channel (SlackChannel): SlackChannel object
        link (_type_): The link of the message in slack
        message (_type_): _description_
    Returns:
        _type_: _description_
    """
    try:
        aux_text = ""
        if src_channel.private != 1:
            aux_text = ("Message on <#"+src_channel.id+
                ">. "+src_channel.p_level+" \n"+link)
        else:
            aux_text = ("Message on <#"+src_channel.id+
                ">."+src_channel.p_level+" \n"+message+" \n"+link)
        result = bot_client.chat_postMessage(
                channel= src_channel.dest_channel_id,
                text=aux_text
                )
        logger.info(result)
    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")
def ts_to_strtime(ts):
    """_summary_
        Converts the UNIX time in timestamp to ISO format.
    Args:
        ts (int): TS datetime
    Returns:
        str: ISO format datetime string for compatibility with Postgres.
    """
    aux_ts = int(ts)
    return str(datetime.utcfromtimestamp(aux_ts).isoformat())
def loop_through_channels(channels):
    """_summary_
        Loop through the channels and post messages on postgres if they aren't cached.
    Args:
        channels (dict): dict() with SlackChannel objects
    """
    for channel_id in channels:
        channel = channels[channel_id]
        conversation_history = []
        try:
            result = client.conversations_history(channel=channel.id, limit = BUFFER_SIZE)
            conversation_history = result["messages"]
            logger.info("{} messages found in {}".format(len(conversation_history), id))
        except SlackApiError as e:
            logger.error("Error creating conversation: {}".format(e))
        for message in conversation_history:
            try:
                msg_dic = dict()
                msg_dic['channel_name'] = channel.name
                msg_dic['channel_id'] = channel.id
                aux_msg = "<@"+message['user']+"> wrote: \n"
                msg_dic['message'] = aux_msg + message['text']
                ts_aux  = message['ts'].split(".")
                msg_dic['ts'] = ts_to_strtime(ts_aux[0])
                msg_dic['ts_ms'] = ts_aux[1]
                supabase.table("slack_watcher").insert(msg_dic).execute()
                auxint = ts_aux[0]+ts_aux[1]
                auxint = auxint.replace(".","")
                link = SLACK_ORG_LINK+channel.id+"/p"+auxint
                post(channel, link, msg_dic['message'])
            except Exception as e:
                pass
        time.sleep(POOLING_DELAY)
def main():
    """_summary_
        Main loop to infinitely keep pooling data from channels and posting on Slack.
        It also checks for new channels every hour.
    """
    channels = setup()
    start = time.time()
    while True:
        end = time.time()
        if ((end - start) > SCAN_CHANNELS_DELAY):
            start = time.time()
            channels = setup()
        else:
            loop_through_channels(channels)
if __name__ == '__main__':
    main()
`

Of course, we aren't doing a proper Python example if we don't make a test notebook available:

[Open in Colab](https://colab.research.google.com/github/mansueli/SlackConsolidate/blob/main/SlackConsolidate_bot.ipynb)

## Conclusion [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#conclusion)

Using Supabase and Slack SDK, it is very easy to create a bot that consolidates data according to the rules set. It just takes some steps to get started with the Python SDK and you can even run a demo directly in [Google Colab](https://colab.research.google.com/drive/1-sM23eQPE1Me4vl10KKoa9xzLYIgkgyQ?usp=sharing).

If you have any questions please reach out via [Twitter](https://twitter.com/supabase) or join our [Discord](https://discord.supabase.com/).

## More Python and Supabase resources [\#](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages\#more-python-and-supabase-resources)

- [Python data loading with Supabase](https://supabase.com/blog/loading-data-supabase-python)
- [Visualizing Supabase Data using Metabase](https://supabase.com/blog/visualizing-supabase-data-using-metabase)
- [Supabase-py (Database) on Replit](https://replit.com/@Supabase/Supabase-py-Database?v=1)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fslack-consolidate-slackbot-to-consolidate-messages&text=Slack%20Consolidate%3A%20a%20slackbot%20built%20with%20Python%20and%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fslack-consolidate-slackbot-to-consolidate-messages&text=Slack%20Consolidate%3A%20a%20slackbot%20built%20with%20Python%20and%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fslack-consolidate-slackbot-to-consolidate-messages&t=Slack%20Consolidate%3A%20a%20slackbot%20built%20with%20Python%20and%20Supabase)

[Last post\\
\\
**Launch Week 5 Hackathon** \\
\\
10 August 2022](https://supabase.com/blog/launch-week-5-hackathon)

[Next post\\
\\
**Supabase Beta July 2022** \\
\\
3 August 2022](https://supabase.com/blog/supabase-beta-update-july-2022)

[slack](https://supabase.com/blog/tags/slack) [python](https://supabase.com/blog/tags/python) [api](https://supabase.com/blog/tags/api) [automation](https://supabase.com/blog/tags/automation)

On this page

- [Prerequisites](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#prerequisites)
  - [Creating the App in Slack](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#creating-the-app-in-slack)
- [Granting access to the bot:](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#granting-access-to-the-bot)
- [Creating Tables in Supabase](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#creating-tables-in-supabase)
- [Adding channels to the watch list and setting the destination channel:](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#adding-channels-to-the-watch-list-and-setting-the-destination-channel)
  - [Examples of adding data to the channel's list:](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#examples-of-adding-data-to-the-channels-list)
- [Setting up the environment File:](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#setting-up-the-environment-file)
- [Now, we can run the bot:](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#now-we-can-run-the-bot)
- [Conclusion](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#conclusion)
- [More Python and Supabase resources](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages#more-python-and-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fslack-consolidate-slackbot-to-consolidate-messages&text=Slack%20Consolidate%3A%20a%20slackbot%20built%20with%20Python%20and%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fslack-consolidate-slackbot-to-consolidate-messages&text=Slack%20Consolidate%3A%20a%20slackbot%20built%20with%20Python%20and%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fslack-consolidate-slackbot-to-consolidate-messages&t=Slack%20Consolidate%3A%20a%20slackbot%20built%20with%20Python%20and%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)