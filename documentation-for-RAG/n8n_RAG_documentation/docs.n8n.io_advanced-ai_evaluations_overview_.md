---
url: "https://docs.n8n.io/advanced-ai/evaluations/overview/"
title: "Evaluations | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/evaluations/overview/#overview)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/evaluations/overview.md "Edit this page")

# Overview [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#overview "Permanent link")

## What are evaluations? [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#what-are-evaluations "Permanent link")

Evaluation is a crucial technique for checking that your AI workflow is reliable. It can be the difference between a flaky proof of concept and a solid production workflow. It's important both in the building phase and after deploying to production.

The foundation of evaluation is running a test dataset through your workflow. This dataset contains multiple test cases. Each test case contains a sample input for your workflow, and often includes the expected output(s) too.

Evaluation allows you to:

- **Test your workflow over a range of inputs** so you know how it performs on edge cases
- **Make changes with confidence** without inadvertently making things worse elsewhere
- **Compare performance** across different models or prompts

The following video explains what evaluations are, why they're useful, and how they work:

n8n Evaluation quickstart - YouTube

n8n

76.4K subscribers

[n8n Evaluation quickstart](https://www.youtube.com/watch?v=5LlF196PKaE)

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

[Watch on](https://www.youtube.com/watch?v=5LlF196PKaE&embeds_referring_euri=https%3A%2F%2Fdocs.n8n.io%2F)

0:00

0:00 / 3:15
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=5LlF196PKaE "Watch on YouTube")

## Why is evaluation needed? [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#why-is-evaluation-needed "Permanent link")

AI models are fundamentally different than code. Code is deterministic and you can reason about it. This is difficult to do with LLMs, since they're black boxes. Instead, you must _measure_ LLM output by running data through them and observing the output.

You can only build confidence that your model performs reliably after you have run it over multiple inputs that accurately reflect all the edge cases that it will have to deal with in production.

## Two types of evaluation [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#two-types-of-evaluation "Permanent link")

### Light evaluation (pre-deployment) [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#light-evaluation-pre-deployment "Permanent link")

Building a clean, comprehensive dataset is hard. In the initial building phase, it often makes sense to generate just a handful of examples. These can be enough to iterate the workflow to a releasable state (or a proof of concept). You can visually compare the results to get a sense of the workflow's quality, without setting up formal metrics.

### Metric-based evaluation (post-deployment) [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#metric-based-evaluation-post-deployment "Permanent link")

Once you deploy your workflow, it's easier to build a bigger, more representative dataset from production executions. When you discover a bug, you can add the input that caused it to the dataset. When fixing the bug, it's important to run the whole dataset over the workflow again as a [regression test](https://en.wikipedia.org/wiki/Regression_testing) to check that the fix hasn't inadvertently made something else worse.

Since there are too many test cases to check individually, evaluations measure the quality of the outputs using a metric, a numeric value representing a particular characteristic. This also allows you to track quality changes between runs.

### Comparison of evaluation types [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#comparison-of-evaluation-types "Permanent link")

|  | Light evaluation (pre-deployment) | Metric-based evaluation (post-deployment) |
| --- | --- | --- |
| **Performance improvements**<br>**with each iteration** | Large | Small |
| **Dataset size** | Small | Large |
| **Dataset sources** | Hand-generated<br>AI-generated<br>Other | Production executions<br>AI-generated<br>Other |
| **Actual outputs** | Required | Required |
| **Expected outputs** | Optional | Required (usually) |
| **Evaluation** **metric** | Optional | Required |

## Learn more [\#](https://docs.n8n.io/advanced-ai/evaluations/overview/\#learn-more "Permanent link")

- [Light evaluations](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/): Perfect for evaluating your AI workflows against hand-selected test cases during development.
- [Metric-based evaluations](https://docs.n8n.io/advanced-ai/evaluations/metric-based-evaluations/): Advanced evaluations to maintain performance and correctness in production by using scoring and metrics with large datasets.
- [Tips and common issues](https://docs.n8n.io/advanced-ai/evaluations/metric-based-evaluations/): Learn how to set up specific evaluation use cases and work around common issues.