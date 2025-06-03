---
url: "https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts"
title: "Pre-fill dynamic form \"date\" fields and get web page change alerts | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts#main-content)

# Pre-fill dynamic form "date" fields and get web page change alerts

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 20 January, 2025



Topic

[How-To](https://changedetection.io/topic/how)

A common situation is when you need to pre-fill / fill-in some data in a web page form such as the "current date", this an example would be when booking a trailor or reserving a car-parking space.

![Pre-fill date field before web page change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_95.png)

Obviously, entering the current date directly is going to be a lot more easier to configure than using the calendar that the web page comes with (which are often really hard to navigate, even by humans!)

One really great feature of changedetection.io is that we try to support "Jinja2" macros where-ever possible, so this means you can insert the current date/time in whatever format you like using Browser Steps

So let's get to it!

## Automatically enter he current date in an input box

- Activate the **Browser Steps** for the webpage you are monitoring for changes, give it a few moments to connect.
- Mouse over the input field (highlighted in red) and click it.
- The software will identify the element as an input/text box and ask you to enter some text, this is where the magic happens.


![Setting the current date in a field before web page change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_93.png)

Now the website automatically prefills the date with next months date, but we want to be sure we enter todays date when ever the web page change detection runs, so that we could perhaps see if any car parking places are available today.

- Enter `{% now  'Europe/Berlin', '%d-%m-%Y' %}`  in the " _**value**_" field under the " **Enter text in field**" box on the right.
- Click **Apply** to see the changes take affect.

![Automatically set the date on web page change detection form](https://changedetection.io/sites/changedetection.io/files/inline-images/image_94.png)

Now you can see that the field is correctly set to today's date ( _20-1-2025)_ According to the "Europe/Berlin" timezone)

Entering a timezone is super important, because the server may run in a different timezone than yourself, you can choose any timezone from [https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

As always, Happy web page change detection :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.