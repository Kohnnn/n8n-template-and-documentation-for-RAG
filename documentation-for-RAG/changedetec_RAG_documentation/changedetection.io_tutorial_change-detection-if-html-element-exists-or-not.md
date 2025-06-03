---
url: "https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not"
title: "Change detection if a HTML element exists or not | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not#main-content)

# Change detection if a HTML element exists or not

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 8 January, 2024



Topic

[How-To](https://changedetection.io/topic/how)

Sometimes you are not quite interested in content change notifications for the entire web page, and maybe not even content change notification for a element on the website - _**actually you want to know if an element exists at all or not.**_

So in this quick tutorial I'll show you how to setup changedetection.io to alert if you a HTML element exists or not

Using "xPath" (Like CSS selectors except different :) ) we can simply write the filter rule

`xpath:if (count(//item) >0 ) then "Yes it exists!" else "no sorry not here"`

![Setting alert if an element exists or not](https://changedetection.io/sites/changedetection.io/files/inline-images/image_66.png)

So then the change difference would look something like

![Example alert text if the item exists](https://changedetection.io/sites/changedetection.io/files/inline-images/image_67.png)

What is also cool is that because changedetection.io supports xPath2/3 by default, you can also just output the value of **count(),** which means you could get a notification if the number of items changes

`xpath:count(//item)`

Where _**//item**_ is the is the HTML xPath to follow

So perhaps one real world example could be that you want to know if the number of offers listed drops to less than 5

(imagine that the page has a list of special offers, where each **div** is  ' `<div class="special-offers">`..\`

`xpath:if (count(//div[contains(@class, 'special-offers')) <5 ) then "Less than 5 special offiers" else "All ok, more than 5 offers"`\
\
Simple as that :) The service will let you know/alert you (depending on your notification setup) if less than 5 offers are shown or not.\
\
All the best and have fun!\
\
- [Continue with\\
    and](https://changedetection.io/checkout)\
\
$8.99/Month Easy Subscription\
\
\
Cancel anytime, 5,000 URL watches included.