---
url: "https://docs.n8n.io/code/ai-code/"
title: "AI coding | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/ai-code/#ai-coding-with-gpt)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/ai-code.md "Edit this page")

# AI coding with GPT [\#](https://docs.n8n.io/code/ai-code/\#ai-coding-with-gpt "Permanent link")

Not available on self-hosted.

Python isn't supported.
///

## Use AI in the Code node [\#](https://docs.n8n.io/code/ai-code/\#use-ai-in-the-code-node "Permanent link")

Feature availability

AI assistance in the Code node is available to Cloud users. It isn't available in self-hosted n8n.

AI generated code overwrites your code

If you've already written some code on the **Code** tab, the AI generated code will replace it. n8n recommends using AI as a starting point to create your initial code, then editing it as needed.

To use ChatGPT to generate code in the Code node:

1. In the Code node, set **Language** to **JavaScript**.
2. Select the **Ask AI** tab.
3. Write your query.
4. Select **Generate Code**. n8n sends your query to ChatGPT, then displays the result in the **Code** tab.

## Usage limits [\#](https://docs.n8n.io/code/ai-code/\#usage-limits "Permanent link")

During the trial phase there are no usage limits. If n8n makes the feature permanent, there may be usage limits as part of your pricing tier.

## Feature limits [\#](https://docs.n8n.io/code/ai-code/\#feature-limits "Permanent link")

The ChatGPT implementation in n8n has the following limitations:

- The AI writes code that manipulates data from the n8n workflow. You can't ask it to pull in data from other sources.
- The AI doesn't know your data, just the schema, so you need to tell it things like how to find the data you want to extract, or how to check for null.
- Nodes before the Code node must execute and deliver data to the Code node before you run your AI query.
- Doesn't work with large incoming data schemas.
- May have issues if there are a lot of nodes before the code node.

## Writing good prompts [\#](https://docs.n8n.io/code/ai-code/\#writing-good-prompts "Permanent link")

Writing good prompts increases the chance of getting useful code back.

Some general tips:

- Provide examples: if possible, give a sample expected output. This helps the AI to better understand the transformation or logic you’re aiming for.
- Describe the processing steps: if there are specific processing steps or logic that should apply to the data, list them in sequence. For example: "First, filter out all users under 18. Then, sort the remaining users by their last name."
- Avoid ambiguities: while the AI understands various instructions, being clear and direct ensures you get the most accurate code. Instead of saying "Get the older users," you might say "Filter users who are 60 years and above."
- Be clear about what you expect as the output. Do you want the data transformed, filtered, aggregated, or sorted? Provide as much detail as possible.

And some n8n-specific guidance:

- Think about the input data: make sure ChatGPT knows which pieces of the data you want to access, and what the incoming data represents. You may need to tell ChatGPT about the availability of n8n's built-in methods and variables.
- Declare interactions between nodes: if your logic involves data from multiple nodes, specify how they should interact. "Merge the output of 'Node A' with 'Node B' based on the 'userID' property". if you prefer data to come from certain nodes or to ignore others, be clear: "Only consider data from the 'Purchases' node and ignore the 'Refunds' node."
- Ensure the output is compatible with n8n. Refer to [Data structure](https://docs.n8n.io/data/data-structure/) for more information on the data structure n8n requires.

### Example prompts [\#](https://docs.n8n.io/code/ai-code/\#example-prompts "Permanent link")

These examples show a range of possible prompts and tasks.

#### Example 1: Find a piece of data inside a second dataset [\#](https://docs.n8n.io/code/ai-code/\#example-1-find-a-piece-of-data-inside-a-second-dataset "Permanent link")

To try the example yourself, [download the example workflow](https://docs.n8n.io/_workflows/ai-code/find-a-piece-of-data.json) and import it into n8n.

In the third Code node, enter this prompt:

> The slack data contains only one item. The input data represents all Notion users. Sometimes the person property that holds the email can be null. I want to find the notionId of the Slack user and return it.

Take a look at the code the AI generates.

This is the JavaScript you need:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>const slackUser = $("Mock Slack").all()[0];<br>const notionUsers = $input.all();<br>const slackUserEmail = slackUser.json.email;<br>const notionUser = notionUsers.find(<br>  (user) => user.json.person && user.json.person.email === slackUserEmail<br>);<br>return notionUser ? [{ json: { notionId: notionUser.json.id } }] : [];<br>``` |

#### Example 2: Data transformation [\#](https://docs.n8n.io/code/ai-code/\#example-2-data-transformation "Permanent link")

To try the example yourself, [download the example workflow](https://docs.n8n.io/_workflows/ai-code/data-transformation.json) and import it into n8n.

In the **Join items** Code node, enter this prompt:

> Return a single line of text that has all usernames listed with a comma. Each username should be enquoted with a double quotation mark.

Take a look at the code the AI generates.

This is the JavaScript you need:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>const items = $input.all();<br>const usernames = items.map((item) => `"${item.json.username}"`);<br>const result = usernames.join(", ");<br>return [{ json: { usernames: result } }];<br>``` |

#### Example 3: Summarize data and create a Slack message [\#](https://docs.n8n.io/code/ai-code/\#example-3-summarize-data-and-create-a-slack-message "Permanent link")

To try the example yourself, [download the example workflow](https://docs.n8n.io/_workflows/ai-code/summarize-data.json) and import it into n8n.

In the **Summarize** Code node, enter this prompt:

> Create a markdown text for Slack that counts how many ideas, features and bugs have been submitted. The type of submission is saved in the property\_type field. A feature has the property "Feature", a bug has the property "Bug" and an idea has the property "Bug". Also, list the five top submissions by vote in that message. Use "" as markdown for links.

Take a look at the code the AI generates.

This is the JavaScript you need:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>``` | ```<br>const submissions = $input.all();<br>// Count the number of ideas, features, and bugs<br>let ideaCount = 0;<br>let featureCount = 0;<br>let bugCount = 0;<br>submissions.forEach((submission) => {<br>  switch (submission.json.property_type[0]) {<br>    case "Idea":<br>      ideaCount++;<br>      break;<br>    case "Feature":<br>      featureCount++;<br>      break;<br>    case "Bug":<br>      bugCount++;<br>      break;<br>  }<br>});<br>// Sort submissions by votes and take the top 5<br>const topSubmissions = submissions<br>  .sort((a, b) => b.json.property_votes - a.json.property_votes)<br>  .slice(0, 5);<br>let topSubmissionText = "";<br>topSubmissions.forEach((submission) => {<br>  topSubmissionText += `<${submission.json.url}|${submission.json.name}> with ${submission.json.property_votes} votes\n`;<br>});<br>// Construct the Slack message<br>const slackMessage = `*Summary of Submissions*\n<br>Ideas: ${ideaCount}\n<br>Features: ${featureCount}\n<br>Bugs: ${bugCount}\n<br>Top 5 Submissions:\n<br>${topSubmissionText}`;<br>return [{ json: { slackMessage } }];<br>``` |

### Reference incoming node data explicitly [\#](https://docs.n8n.io/code/ai-code/\#reference-incoming-node-data-explicitly "Permanent link")

If your incoming data contains nested fields, using dot notation to reference them can help the AI understand what data you want.

[!["Screenshot of an n8n code node, highlighting how to reference data with dot notation in an AI query"](https://docs.n8n.io/_images/code/ai-code/reference-data-dot-notation.png)](https://docs.n8n.io/_images/code/ai-code/reference-data-dot-notation.png)

To try the example yourself, [download the example workflow](https://docs.n8n.io/_workflows/ai-code/reference-incoming-data-explicitly.json) and import it into n8n.

In the second Code node, enter this prompt:

> The data in "Mock data" represents a list of people. For each person, return a new item containing personal\_info.first\_name and work\_info.job\_title.

This is the JavaScript you need:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>``` | ```<br>const items = $input.all();<br>const newItems = items.map((item) => {<br>  const firstName = item.json.personal_info.first_name;<br>  const jobTitle = item.json.work_info.job_title;<br>  return {<br>    json: {<br>      firstName,<br>      jobTitle,<br>    },<br>  };<br>});<br>return newItems;<br>``` |

### Related resources [\#](https://docs.n8n.io/code/ai-code/\#related-resources "Permanent link")

Pluralsight offer a short guide on [How to use ChatGPT to write code](https://www.pluralsight.com/blog/software-development/how-use-chatgpt-programming-coding), which includes example prompts.

## Fixing the code [\#](https://docs.n8n.io/code/ai-code/\#fixing-the-code "Permanent link")

The AI-generated code may work without any changes, but you may have to edit it. You need to be aware of n8n's [Data structure](https://docs.n8n.io/data/data-structure/). You may also find n8n's built-in methods and variables useful.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top