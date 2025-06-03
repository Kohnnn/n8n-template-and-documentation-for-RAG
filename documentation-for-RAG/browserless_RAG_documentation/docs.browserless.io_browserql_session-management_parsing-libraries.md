---
url: "https://docs.browserless.io/browserql/session-management/parsing-libraries"
title: "Parsing Libraries | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/session-management/parsing-libraries#__docusaurus_skipToContent_fallback)

On this page

You can use BrowserQL to retrieve HTML content from any website, and use this content with any parsing libraries, such as Scrapy, Beaultiful Soup, or Cheerio.

With BQL, you'll navigate to the desired page, do the actions you require, like verifying or solving a captcha, and finally, retrieve the HTML you need to parse.

tip

Use [BQL Editor](https://account.browserless.io/bql) to create and test your queries before integrating it to your code.

## Example [​](https://docs.browserless.io/browserql/session-management/parsing-libraries\#example "Direct link to Example")

As an example, the code below accesses [https://browserless.io/](https://browserless.io/), clicks on the **Try it Free** button, and retrieves the HTML content from the pricing page.

```codeBlockLines_p187
mutation RetrieveHTML {
  goto(url: "https://browserless.io/") {
    status
  }

  click(selector: ".button-group a.button.w-button") {
    time
  }

  html {
    html
  }
}

```

Now, you can integrate this query into your code, using BQL to retrieve the HTML, and integrating it with your preffered library to parse this content:

- Beautiful Soup
- Scrapy
- Cheerio

```codeBlockLines_p187
import requests
from bs4 import BeautifulSoup

url = 'https://browserless.io/'
token = 'YOUR_API_TOKEN_HERE'
timeout = 5 * 60 * 1000

query = '''
mutation RetrieveHTML($url: String!) {
    goto(url: $url) {
        status
    }
    click(selector: ".button-group a.button.w-button") {
        time
    }
    html {
        html
    }
}
'''

variables = {"url": url}
endpoint = f'https://production-sfo.browserless.io/chromium/bql?timeout={timeout}&token={token}'

headers = {'content-type': 'application/json'}
payload = {"query": query, "variables": variables}

response = requests.post(endpoint, json=payload)
response_data = response.json()

# Extract HTML content
html_content = response_data['data']['html']['html']

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
plans = [tag.text.strip() for tag in soup.find_all('div', class_='tag_price margin-bottom margin-large')]

print(plans)

```

```codeBlockLines_p187
import requests
from scrapy.selector import Selector

url = 'https://browserless.io/'
token = 'YOUR_API_TOKEN_HERE'
timeout = 5 * 60 * 1000

query = '''
mutation RetrieveHTML($url: String!) {
    goto(url: $url) {
        status
    }
    click(selector: ".button-group a.button.w-button") {
        time
    }
    html {
        html
    }
}
'''

variables = {"url": url}
endpoint = f'https://production-sfo.browserless.io/chromium/bql?timeout={timeout}&token={token}'

headers = {'content-type': 'application/json'}
payload = {"query": query, "variables": variables}

response = requests.post(endpoint, json=payload)
response_data = response.json()

# Extract HTML content
html_content = response_data['data']['html']['html']

# Parse HTML with Scrapy
selector = Selector(text=html_content)
plans = selector.css('.tag_price.margin-bottom.margin-large::text').getall()

print(plans)

```

```codeBlockLines_p187
const fetch = require('node-fetch');
const cheerio = require('cheerio');

const url = 'https://browserless.io/';
const token = 'YOUR_API_TOKEN_HERE';
const timeout = 5 * 60 * 1000;

const queryParams = new URLSearchParams({
  timeout,
  token,
}).toString();

const query = `
  mutation RetrieveHTML($url: String!) {
    goto(url: $url) {
      status
    }
    click(selector: ".button-group a.button.w-button") {
      time
    }
    html {
      html
    }
  }
`;

const variables = { url };
const endpoint = `https://production-sfo.browserless.io/chromium/bql?${queryParams}`;

const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json',
  },
  body: JSON.stringify({
    query,
    variables,
  }),
};

(async () => {
  try {
    const response = await fetch(endpoint, options);
    const { data } = await response.json();

    // Extract HTML content
    const htmlContent = data.html.html;

    // Parse HTML with Cheerio
    const $ = cheerio.load(htmlContent);
    const plans = [];
    $('.tag_price.margin-bottom.margin-large').each((_, element) => {
      plans.push($(element).text().trim());
    });

    console.log(plans);
  } catch (error) {
    console.error('Error fetching or parsing HTML:', error);
  }
})();

```

- [Example](https://docs.browserless.io/browserql/session-management/parsing-libraries#example)