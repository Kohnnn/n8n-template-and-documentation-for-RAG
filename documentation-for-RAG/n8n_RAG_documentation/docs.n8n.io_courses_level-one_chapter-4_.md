---
url: "https://docs.n8n.io/courses/level-one/chapter-4/"
title: "Designing the workflow | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-4/#designing-the-workflow)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-4.md "Edit this page")

# Designing the Workflow [\#](https://docs.n8n.io/courses/level-one/chapter-4/\#designing-the-workflow "Permanent link")

Now that we know what Nathan wants to automate, let's consider the steps he needs to take to achieve his goals:

1. Get the relevant data (order id, order status, order value, employee name) from the data warehouse
2. Filter the orders by their status (Processing or Booked)
3. Calculate the total value of all the Booked orders
4. Notify the team members about the Booked orders in the company's Discord channel
5. Insert the details about the Processing orders in Airtable for follow-up
6. Schedule this workflow to run every Monday morning

Nathan's workflow involves sending data from the company's data warehouse to two external services:

- Discord
- Airtable

Before that, the data has to be wrangled with general functions (conditional filtering, calculation, scheduling).

n8n provides integrations for all these steps, so Nathan's workflow in n8n would look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/finished.json)

You will build this workflow in eight steps:

1. [Getting data from the data warehouse](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.1/)
2. [Inserting data into Airtable](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/)
3. [Filtering orders](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/)
4. [Setting values for processing orders](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.4/)
5. [Calculating booked orders](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.5/)
6. [Notifying the team](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.6/)
7. [Scheduling the workflow](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/)
8. [Activating and examining the workflow](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.8/)

To build this workflow, you will need the credentials found in the email you received from n8n when you signed up for this course. If you haven't signed up already, you can do it [here](https://n8n-community.typeform.com/to/PDEMrevI?typeform-source=127.0.0.1). If you haven't received a confirmation email after signing up, [contact us](mailto:help@n8n.io).

[Start building!](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.1/)