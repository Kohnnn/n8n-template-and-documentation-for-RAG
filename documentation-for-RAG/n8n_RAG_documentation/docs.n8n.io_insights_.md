---
url: "https://docs.n8n.io/insights/"
title: "Insights | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/insights/#insights)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/insights.md "Edit this page")

# Insights [\#](https://docs.n8n.io/insights/\#insights "Permanent link")

Insights gives instance owners and admins visibility into how workflows perform over time. This feature consists of three parts:

- [**Insights summary banner**](https://docs.n8n.io/insights/#insights-summary-banner): Shows key metrics about your instance from the last 7 days at the top of the overview space.
- [**Insights dashboard**](https://docs.n8n.io/insights/#insights-dashboard): A more detailed visual breakdown with per-workflow metrics and historical comparisons.
- [**Time saved (Workflow ROI)**](https://docs.n8n.io/insights/#setting-the-time-saved-by-a-workflow): For each workflow, you can set the number of minutes of work that each production execution saves you.

Feature availability

The insights summary banner displays activity from the last 7 days for all plans. The insights dashboard is only available on Pro (with limited date ranges) and Enterprise plans.

## Insights summary banner [\#](https://docs.n8n.io/insights/\#insights-summary-banner "Permanent link")

n8n collects several metrics for both the insights summary banner and dashboard. They include:

- Total production executions (not including sub-workflow executions or manual executions)
- Total failed production executions
- Production execution failure rate
- Time saved (when set on at least one or more active workflows)
- Run time average (including wait time from any wait nodes)

## Insights dashboard [\#](https://docs.n8n.io/insights/\#insights-dashboard "Permanent link")

Those on the Pro and Enterprise plans can access the **Insights** section from the side navigation. Each metric from the summary banner is also clickable, taking you to the corresponding chart.

The insights dashboard also has a table showing individual insights from each workflow including total production executions, failed production executions, failure rate, time saved, and run time average.

## Insights time periods [\#](https://docs.n8n.io/insights/\#insights-time-periods "Permanent link")

By default, the insights summary banner and dashboard show a rolling 7 day window with a comparison to the previous period to identify increases or decreases for each metric. On the dashboard, paid plans also display data for other date ranges:

- Pro: 7 and 14 days
- Enterprise: 24 hours, 7 days, 14 days, 30 days, 90 days, 6 months, 1 year

## Setting the time saved by a workflow [\#](https://docs.n8n.io/insights/\#setting-the-time-saved-by-a-workflow "Permanent link")

For each workflow, you can set the number of minutes of work a workflow saves you each time it runs. You can configure this by navigating to the workflow, selecting the three dots menu in the top right and selecting settings. There you can update the **Estimated time saved** value and save.

This setting helps you calculate how much time automating a process saves over time vs the manual effort to complete the same task or process. Once set, n8n calculates the amount of time the workflow saves you based on the number of production executions and displays it on the summary banner and dashboard.

## Disable or configure insights metrics collection [\#](https://docs.n8n.io/insights/\#disable-or-configure-insights-metrics-collection "Permanent link")

If you self-host n8n, you can disable or configure insights and metrics collection using [environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/insights/).

## Insights FAQs [\#](https://docs.n8n.io/insights/\#insights-faqs "Permanent link")

### Which executions do n8n use to calculate the values in the insights banner and dashboard? [\#](https://docs.n8n.io/insights/\#which-executions-do-n8n-use-to-calculate-the-values-in-the-insights-banner-and-dashboard "Permanent link")

n8n insights only collects data from production executions (for example, those from active workflows triggered on a schedule or a webhook) from the main (parent) workflow. This means that it doesn't count manual (test) executions or executions from sub-workflows or error workflows.

### Does n8n use historic execution data when upgrading to a version with insights? [\#](https://docs.n8n.io/insights/\#does-n8n-use-historic-execution-data-when-upgrading-to-a-version-with-insights "Permanent link")

n8n only starts collecting data for insights once you update to the first supported version (1.89.0). This means it only reports on executions from that point forward and you won't see execution data in insights from prior periods.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top