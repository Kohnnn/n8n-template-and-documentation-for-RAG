---
url: "https://docs.n8n.io/advanced-ai/intro-tutorial/"
title: "Tutorial: Build an AI workflow in n8n | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/advanced-ai/intro-tutorial/#build-an-ai-chat-agent-with-n8n)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/intro-tutorial.md "Edit this page")

# Build an AI chat agent with n8n [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#build-an-ai-chat-agent-with-n8n "Permanent link")

Welcome to the introductory tutorial for building AI workflows with n8n. Whether you have used n8n before, or this is your first time, we will show you how the building blocks of AI workflows fit together and construct a working AI-powered chat agent which you can easily customize for your own purposes.

[!["Screenshot of the completed workflow"](https://docs.n8n.io/_images/advanced-ai/ai-intro01.png)](https://docs.n8n.io/_images/advanced-ai/ai-intro01.png)

Many people find it easier to take in new information in video format. This tutorial is based on one of n8n's popular videos, linked below. Watch the video or read the steps here, or both!

Building AI Agents: Chat Trigger, Memory, and System/User Messages Explained \[Part 1\] - YouTube

n8n

76.4K subscribers

[Building AI Agents: Chat Trigger, Memory, and System/User Messages Explained \[Part 1\]](https://www.youtube.com/watch?v=yzvLfHb0nqE)

n8n

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=yzvLfHb0nqE&embeds_referring_euri=https%3A%2F%2Fdocs.n8n.io%2F)

0:00

0:00 / 20:16
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=yzvLfHb0nqE "Watch on YouTube")

### What you will need [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#what-you-will-need "Permanent link")

- **n8n**: For this tutorial we recommend using the [n8n cloud](https://docs.n8n.io/manage-cloud/overview/) service - there is a free trial for new users! For a self hosted service, refer to the [installation pages](https://docs.n8n.io/hosting/installation/docker/).
- **Credentials for a chat model**: This tutorial uses OpenAI, but you can easily use DeepSeek, Google Gemini, Groq, Azure, and others (see the [sub-nodes documentation](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/) for more).

### What you will learn [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#what-you-will-learn "Permanent link")

- AI concepts in n8n
- How to use the AI Agent node
- Working with Chat input
- Connecting with AI models
- Customising input
- Observing the conversation
- Adding persistence

## AI concepts in n8n [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#ai-concepts-in-n8n "Permanent link")

If you're already familiar with AI, feel free to skip this section. This is a basic introduction to AI concepts and how they can be used in n8n workflows.

An [AI agent](https://docs.n8n.io/glossary/#ai-agent) builds on [Large Language Models (LLMs)](https://docs.n8n.io/glossary/#large-language-model-llm), which generate text based
on input by predicting the next word. While LLMs only process input to produce
output, AI agents add goal-oriented functionality. They can use [tools](https://docs.n8n.io/glossary/#ai-tool), process
their outputs, and make decisions to complete tasks and solve problems.

In n8n, the AI agent is represented as a node with some extra connections.

| Feature | LLM | AI Agent |
| --- | --- | --- |
| Core Capability | Text generation | Goal-oriented task completion |
| Decision-Making | None | Yes |
| Uses Tools/APIs | No | Yes |
| Workflow Complexity | Single-step | Multi-step |
| Scope | Generates language | Performs complex, real-world tasks |
| Example | LLM generating a paragraph | An agent scheduling an appointment |

By incorporating the AI agent as a node, n8n can combine AI-driven steps with traditional programming for efficient, real-world workflows. For instance, simpler tasks, like validating an email address, do not require AI, whereas a complex tasks, like processing the _content_ of an email or dealing with multimodal inputs (e.g., images, audio), are excellent uses of an AI agent.

## 1\. Create a new workflow [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#1-create-a-new-workflow "Permanent link")

When you open n8n, you'll see either:

- An empty workflow: if you have no workflows and you're logging in for the first time. Use this workflow.
- The **Workflows** list on the **Overview** page. Select the ![universal create resource icon](https://docs.n8n.io/_images/common-icons/universal-resource-button.png)**button** to create a new workflow.

## 2\. Add a trigger node [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#2-add-a-trigger-node "Permanent link")

Every workflow needs somewhere to start. In n8n these are called ['trigger nodes'](https://docs.n8n.io/glossary/#trigger-node-n8n). For this workflow, we want to start with a chat node.

1. Select **Add first step** or press `Tab` to open the node menu.

2. Search for **Chat Trigger**. n8n shows a list of nodes that match the search.

3. Select **Chat Trigger** to add the node to the canvas. n8n opens the node.

4. Close the node details view (Select **Back to canvas**) to return to the canvas.


More about the Chat Trigger node...

The trigger node generates output when there is an event causing it to trigger. In this case we want to be able to type in text to cause the workflow to run. In production, this trigger can be hooked up to a public chat interface as provided by n8n or embedded into another website. To start this simple workflow we will just use the built-in local chat interface to communicate, so no further setup is required.

[View workflow file](https://docs.n8n.io/_workflows//advanced-ai/tutorials/chat_01.json)

## 3\. Add an AI Agent Node [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#3-add-an-ai-agent-node "Permanent link")

The AI Agent node is the core of adding AI to your workflows.

1. Select the **Add node**![Add node icon](https://docs.n8n.io/_images/try-it-out/add-node-small.png) connector on the trigger node to bring up the node search.

2. Start typing "AI" and choose the **AI agent** node to add it.

3. The editing view of the **AI agent** will now be displayed.

4. There are some fields which can be changed. As we're using the **Chat Trigger** node, the default setting for the source and specification of the prompt don't need to be changed.


[View workflow file](https://docs.n8n.io/_workflows//advanced-ai/tutorials/chat_02.json)

## 4\. Configure the node [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#4-configure-the-node "Permanent link")

AI agents require a chat model to be attached to process the incoming prompts.

1. Add a chat model by clicking the plus ![Add node icon](https://docs.n8n.io/_images/try-it-out/add-node-small.png) button underneath the **Chat Model** connection on the **AI Agent** node (it's the first connection along the bottom of the node).

2. The search dialog will appear, filtered on 'Language Models'. These are the models with built-in support in n8n. For this tutorial we will use **OpenAI Chat Model**.

3. Selecting the **OpenAI Chat model** from the list will attach it to the **AI Agent** node and open the node editor. One of the parameters which can be changed is the 'Model'. Note that for the basic OpenAI accounts, only the 'gpt-4o-mini' model is allowed.


Which chat model?

As mentioned earlier, the LLM is the component which generates the text according to a prompt it is given. LLMs have to be created and trained, usually an intensive process. Different LLMS may have different capabilities or specialties, depending on the data they were trained with.

## 5\. Add credentials (if needed) [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#5-add-credentials-if-needed "Permanent link")

In order for n8n to communicate with the chat model, it will need some [credentials](https://docs.n8n.io/credentials/) (login data giving it access to an account on a different online service). If you already have credentials set up for OpenAI, these should appear by default in the credentials selector. Otherwise you can use the Credentials selector to help you add a new credential.

[![image showing the credentials dialog for OpenAI](https://docs.n8n.io/_images/advanced-ai/ai-tutorial-credentials.png)](https://docs.n8n.io/_images/advanced-ai/ai-tutorial-credentials.png)

1. To add a new credential, click on the text which says 'Select credential'. An option to add a new credential will appear
    [![Screenshot showing create a new credential button](https://docs.n8n.io/_images/advanced-ai/ai-tutorial-create-credential.png)](https://docs.n8n.io/_images/advanced-ai/ai-tutorial-create-credential.png)

2. This credential just needs an API key. When adding credentials of any type, check the text to the right-hand side. In this case it has a handy link to take you straight to your OpenAI account to retrieve the API key.

3. The API key is just one long string. That's all you need for this particular credential. Copy it from the OpenAI website and paste it into the **API key** section.


Keeping your credentials safe

Credentials are private pieces of information issued by apps and services to authenticate you as a user and allow you to connect and share information between the app or service and the n8n node. The type of information required varies depending on the app/service concerned. You should be careful about sharing or revealing the credentials outside of n8n.

## 6\. Test the node [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#6-test-the-node "Permanent link")

Now that the node is connected to the **Chat Trigger** and a chat model, we can test this part of the workflow.

1. Click on the 'Chat' button near the bottom of the canvas. This opens up a local chat window on the left and the AI agent logs on the right.

2. Type in a message and press `Enter`. You will now see the response from the chat model appear below your message.

3. The log window displays the inputs to and outputs from the AI Agent.
    [![image showing a chat session in progress](https://docs.n8n.io/_images/advanced-ai/ai-intro-chat.png)](https://docs.n8n.io/_images/advanced-ai/ai-intro-chat.png)


Accessing the logs...

You can access the logs for the AI node even when you aren't using the chat interface. Open up the **AI Agent** node and click on the **Logs** tab in the right hand panel.
[![screenshot showing the Logs tab in the AIAgent](https://docs.n8n.io/_images/advanced-ai/ai-intro-logs.png)](https://docs.n8n.io/_images/advanced-ai/ai-intro-logs.png)

## 7\. Changing the prompt [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#7-changing-the-prompt "Permanent link")

The logs in the previous step reveal some extra data - the system prompt. This is the default message that the **AI Agent** primes the chat model with. From the log you can see this is set to "You are a helpful assistant". We can however change this prompt to alter the behavior of the chat model.

1. Open the **AI Agent** node. In the bottom of the panel is a section labeled 'Options' and a selector labeled 'Add Option'. Use this to select 'System message'

2. The system message is now displayed. This is the same priming prompt we noticed before in the logs. Change the prompt to something else to prime the chat model in a different way. You could try something like "You are a brilliant poet who always replies in rhyming couplets" for example.

3. Close the node and return to the chat window. Repeat your message and notice how the output has changed.
    [![image showing changed text for chat, now it rhymes; if you can believe that](https://docs.n8n.io/_images/advanced-ai/ai-intro-poet.png)](https://docs.n8n.io/_images/advanced-ai/ai-intro-poet.png)


## 8\. Adding persistence [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#8-adding-persistence "Permanent link")

The chat model is now giving us useful output, but there is something wrong with it which will become apparent when you try to have a conversation.

1. Use the chat and tell the chat model your name, for example "Hi there, my name is Nick".

2. Wait for the response, then type the message "What's my name?". The AI will not be able to tell you, however apologetic it may seem. The reason for this is we are not saving the context. The AI Agent has no [memory](https://docs.n8n.io/glossary/#ai-memory).
    [![image showing a conversation illustrating the above](https://docs.n8n.io/_images/advanced-ai/ai-intro-memory.png)](https://docs.n8n.io/_images/advanced-ai/ai-intro-memory.png)

3. In order to remember what has happened in the conversation, the AI Agent needs to preserve context. We can do this by adding memory to the **AI Agent** node. On the canvas click on the ![Add node icon](https://docs.n8n.io/_images/try-it-out/add-node-small.png) on the bottom of the **AI Agent** node labeled "Memory".

4. From the panel which appears, select "Simple Memory". This will use the memory from the instance running n8n, and is usually sufficient for simple usage. The default value of 5 interactions should be sufficient here, but remember where this option is if you may want to change it later.

5. Repeat the exercise of having a conversation above, and see that the AI Agent now remembers your name.


## 9\. Saving the workflow [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#9-saving-the-workflow "Permanent link")

Before we leave the workflow editor, remember to save the workflow or all your changes will be lost.

1. Click on the "Save" button in the top right of the editor window. Your workflow will now be saved and you can return to it later to chat again or add new features.

## Congratulations! [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#congratulations "Permanent link")

You have taken your first steps in building useful and effective workflows with AI. In this tutorial we have investigated the basic building blocks of an AI workflow, added an **AI Agent** and a chat model, and adjusted the prompt to get the kind of output we wanted. We also added memory so the chat could retain context between messages.

[View workflow file](https://docs.n8n.io/_workflows//advanced-ai/tutorials/chat_complete.json)

## Next steps [\#](https://docs.n8n.io/advanced-ai/intro-tutorial/\#next-steps "Permanent link")

Now you have seen how to create a basic AI workflow, there are plenty of resources to build on that knowledge and plenty of examples to give you ideas of where to go next:

- Learn more about AI concepts and view examples in [Examples and concepts](https://docs.n8n.io/advanced-ai/examples/introduction/).
- Browse AI [Workflow templates](https://n8n.io/workflows/?categories=25).
- Find out how to [enhance the AI agent with tools](https://docs.n8n.io/advanced-ai/examples/understand-tools/).