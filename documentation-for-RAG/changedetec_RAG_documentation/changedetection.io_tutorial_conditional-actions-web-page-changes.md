---
url: "https://changedetection.io/tutorial/conditional-actions-web-page-changes"
title: "Conditional actions on web page changes! | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/conditional-actions-web-page-changes#main-content)

# Conditional actions on web page changes!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 31 March, 2025



Topic

[How-To](https://changedetection.io/topic/how)

Starting with version **v0.49.9**, Changedetection.io introduces one of its most powerful features yet: **conditional actions**. This opens the door to much more precise and flexible monitoring.

It’s no longer just about detecting when content changes — now you can define exactly _what kind_ of change matters to you. For example, trigger an alert only when a product’s price drops below a certain threshold, or when a keyword appears in the updated content.

With full support for logic operators, you can create rich, rule-based conditions using logic like “greater than,” “less than,”, "contains", "not contains" and more.

So let's get on with a really great example - Monitor when temperatures in Berlin are "extreme" (less than -20c or greater than +38c)

### Let's add the web page we want to monitor for changes (Berlin Weather)

![Web page for conditional actions](https://changedetection.io/sites/changedetection.io/files/inline-images/image_109.png)

### Let's set-up our conditional change detection filter

Let the page fetch, then click **\[EDIT\]**

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_112.png)

Then, using the **Visual Filter Selector** tab, choose the number, in this case we will click on the current temperature, a balmy 9.2°C.  When the element is selected and click a **red border** will appear.

It's important to choose the right part of the web-page for change-detection, otherwise the number extractor wont know exactly which number is important to you.

![Web page for conditional actions, setting the actual content](https://changedetection.io/sites/changedetection.io/files/inline-images/image_113.png)

Then, hop on over to the **CONDITIONS** tab

![Setting up rules / conditions for web page changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_114.png)

Let's explain a little what we see here

- **"Match any of the following" -** This acts as 'OR', so _any_ rule will trigger on change
- **"Extracted number after 'Filters & Triggers"**\- We only want to look for a number inside of any filters we specified (This could be the Visual Selector, Text filters from other tabs etc)
- Using these two buttons we can then **add an extra** **\[  \+  \]**  rule after this one, or **remove it    \[  -  \]**

##### _**Testing the rules!**_

Since the page is already fetched, It's nice to know if the rule currently will pass or fail, for this we can press the "tick" button, this will verify that rule row only and report if it PASSES or FAILS.

If you look closely you can see that after pressing the "verify" tick button you can see the text **"extracted number value was 9.2"** below the rules, this lets us know what the situation is and so we know if the right value is being extracted

##### Other interesting checks

- Text contains (or does not contain)
- Text length is greater than (or shorter than)
- Text begins with (or doesnt begin with)
- Text equal (or does not equal)
- plus more!

#### Wrapping up

Of course now you can head over to the **Notifications** tab and setup your slack, email, discord or which ever format you and your team love the most.

This is how you can simply setup Conditional changes, this is just a simple example but there are so many other amazing ways to use this functionality, we encourage you to explore and play with this new tool :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.