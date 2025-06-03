---
url: "https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire"
title: "How to get alerts when certain keywords appear on PR Newswire? | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire#main-content)

# How to get alerts when certain keywords appear on PR Newswire?

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 13 June, 2023



Topic

[How-To](https://changedetection.io/topic/how)

[PR Newswire](https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100) is a news distribution service. By monitoring keywords on PR Newswire, you gain insights, track brand reputation, discover media opportunities, make informed investments, and identify crisis risks.

By monitoring specific keywords on the PR Newswire website, you can achieve the following:

1. **Market Trends and Competitor Analysis**: If you're a business operating in a particular industry, you can track relevant keywords related to your products or services. This helps you stay informed about market trends, monitor your competitors' activities, and identify emerging opportunities or threats in the industry.
2. **Brand Reputation Management**: Monitoring your brand name and related keywords allows you to track mentions and sentiments about your company. This way, you can proactively manage your brand reputation, address any negative feedback or misconceptions, and leverage positive news to enhance your brand image.
3. **Media Outreach and Public Relations**: For PR professionals, tracking keywords relevant to their clients or industry can help in identifying potential media opportunities. By keeping an eye on relevant news stories and trends, they can reach out to journalists and influencers at the right time, increasing the chances of media coverage.
4. **Investment and Financial Insights**: Investors can monitor keywords related to financial results, mergers, acquisitions, or industry-specific terms. This helps them stay updated on the financial health of companies they are interested in, assess potential investment opportunities, and make informed decisions.
5. **Content Discovery and Story Ideas**: Journalists and content creators can track trending keywords to discover emerging news stories and topics that are gaining traction. This allows them to develop timely and relevant content, keeping their audience engaged.
6. **Crisis Management and Risk Assessment**: Monitoring keywords associated with crises or potential risks in your industry enables you to respond quickly to adverse events, mitigate potential damage, and communicate effectively with stakeholders.

Overall, monitoring specific keywords on PR Newswire offers valuable insights and opportunities to stay ahead in the competitive landscape, engage with your audience effectively, and make well-informed business decisions.

So in this article, I'll show you a quick recipe for a scenario where we want a track when a list of our favourite stock exchange codes has appeared in the news, this could mean that something interesting is happening and that we may need to buy or sell (for example)

So let's setup a simple watch to know when our favourite stock codes have appeared in the news, they are;

- _GOOGL_
- _AMZN_
- _NVDA_

#### Step 1.  Add the PR Newswire page that contains the list of news as a watch

We will watch the URL [https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100](https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100), this page usually contains all the latest news, however you could choose a different page if you like, but in this page there is plenty of fresh content which could include the  important keywords we are after.

Add the URL to the top input box, then click **Edit > Watch**

![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_2.png)

#### Step 2.  Configure the keyword rules

Another super cool feature of changedetection.io is its ability to monitor for keywords, either that have been **added** or **removed**\- In our case we want to know when certain keywords appear in the text (not when they have been removed)

Simply click on over to **Filters & Triggers,** then scroll down to **Text filtering**

![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_3.png)

Down at **Text filtering**, it's important to select only **"Added lines"** and **"Replaced/changed lines"** this means that you will only get notifications when the page has new content matching the list of keywords you added.

Sometimes content can be regarded as "changed" when it's moved down a list of articles for example.

#### ![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_5.png)

Then ofcourse, click **Save**

And that's it! super easy keyword notification!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.