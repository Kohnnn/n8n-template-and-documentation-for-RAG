---
url: "https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.6/"
title: "Notifying the team | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.6/#6-notifying-the-team)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-5/chapter-5.6.md "Edit this page")

# 6\. Notifying the Team [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.6/\#6-notifying-the-team "Permanent link")

In this step of the workflow, you will learn how to send messages to a Discord channel using the [Discord node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/). After this step, your workflow should look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/chapter-5/chapter-5.6.json)

Now that you have a calculated summary of the booked orders, you need to notify Nathan's team in their Discord channel. For this workflow, you will send messages to the [n8n server](https://discord.gg/G98WXzsjky) on Discord.

Before you begin the steps below, use the link above to connect to the n8n server on Discord. Be sure you can access the `#course-level-1` channel.

Communication app nodes

You can replace the Discord node with another communication app. For example, n8n also has nodes for [Slack](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/) and [Mattermost](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mattermost/).

In your workflow, add a Discord node connected to the Code node.

When you search for the Discord node, look for **Message Actions** and select **Send a message** to add the node.

In the Discord node window, configure these parameters:

- **Connection Type**: Select **Webhook**.
- **Credential for Discord Webhook**: Select **\- Create New Credential -**.
  - Copy the **Webhook URL** from the email you received when you signed up for this course and paste it into the **Webhook URL** field of the credentials.
  - Select **Save** and then close the credentials dialog.
- **Operation**: Select **Send a Message**.
- **Message**:
  - Select the **Expression** tab on the right side of the Message field.
  - Copy the text below and paste it into the **Expression** window, or construct it manually using the **Expression Editor**.



    |     |     |
    | --- | --- |
    | ```<br>1<br>``` | ```<br>This week we've {{$json["totalBooked"]}} booked orders with a total value of {{$json["bookedSum"]}}. My Unique ID: {{ $('HTTP Request').params["headerParameters"]["parameters"][0]["value"] }}<br>``` |

Now select **Execute step** in the Discord node. If all works well, you should see this output in n8n:

[![Discord node output](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-6-discord-output.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-6-discord-output.png) _Discord node output_

And your message should appear in the Discord channel #course-level-1:

[![Discord message](https://docs.n8n.io/_images/courses/level-one/chapter-two/discord-output.png)](https://docs.n8n.io/_images/courses/level-one/chapter-two/discord-output.png) _Discord message_

## What's next? [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.6/\#whats-next "Permanent link")

**Nathan 🙋**: Incredible, you've saved me hours of tedious work already! Now I can execute this workflow when I need it. I just need to remember to run it every Monday morning at 9 AM.

**You 👩‍🔧**: Don't worry about that, you can actually schedule the workflow to run on a specific day, time, or interval. I'll set this up in the next step.