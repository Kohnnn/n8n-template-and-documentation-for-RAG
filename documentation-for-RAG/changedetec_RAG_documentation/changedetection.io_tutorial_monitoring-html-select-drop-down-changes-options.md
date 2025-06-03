---
url: "https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options"
title: "Monitoring HTML \"SELECT\" drop down for changes to options | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options#main-content)

# Monitoring HTML "SELECT" drop down for changes to options

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 11 October, 2024



Topic

[How-To](https://changedetection.io/topic/how)

changedetection.io will automatically show any changes to <select><option> values, infact it renders them out ready for change detection on the fly

_**For example if we had..**_

`<select name="cars" id="cars"> `

` <option value="volvo">Volvo</option> `

` <option value="saab">Saab</option> `

` <option value="mercedes">Mercedes</option> `

` <option value="audi">Audi</option> `

`</select>`

So this would appear by default in the " **Preview**"( or notification text )  as `"Volve Saab Mercedes Audio"`, however if you really wanted to see what changed you can also switch to _**HTML Source mode**_

changedetection.io can also monitor the HTML source of a web-page by simply prepending the " `source:`" keyword to the start of a page, for example below ;

(more on [monitoring changes to HTML sourcecode here](https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code))

![Adding a URL for web page change detection of select element](https://changedetection.io/sites/changedetection.io/files/inline-images/image_86.png)

Then we can skip over to **Filters & Triggers** and add `select`, this way we can just focus on the `<select>` element for monitoring changes

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_87.png)

After a quick recheck, we can now see that "skoda" was added to the dropdown select element list items ( and if we configured notifications, we could get a notification via Discord, slack, email etc)

![HTML Select with changes ready for alerts](https://changedetection.io/sites/changedetection.io/files/inline-images/image_88.png)

Happy change detecting :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.