---
url: "https://docs.browserless.io/browserql/recipes/multi-line-evaluate"
title: "Working with multi-line evaluate in BrowserQL | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#__docusaurus_skipToContent_fallback)

On this page

BrowserQL's `evaluate` mutation allows you to execute JavaScript in the browser's page environment. When working with more complex scripts, especially multi-line code, you need to understand how to properly format your code for BrowserQL.

## How evaluate works in BrowserQL [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#how-evaluate-works-in-browserql "Direct link to How evaluate works in BrowserQL")

When you use the `evaluate` mutation, BrowserQL automatically wraps your code in an async function like this:

```codeBlockLines_p187
(async() => {return YOUR_CODE_HERE})();

```

However, for multi-line code, you currently need to wrap your code in an IIFE (Immediately Invoked Function Expression) to ensure proper execution:

```codeBlockLines_p187
(()=>{
  // Your multi-line code here
  return result;
})()

```

This approach allows you to:

- Structure complex logic across multiple lines
- Use modern JavaScript features (like arrow functions, destructuring, etc.)
- Return values from your code execution
- Handle scoping properly within your evaluate blocks

## Single vs. Multi-line evaluation [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#single-vs-multi-line-evaluation "Direct link to Single vs. Multi-line evaluation")

- Single-line
- Multi-line (with IIFE)

For simple expressions, you can use single-line evaluation:

```codeBlockLines_p187
mutation SimpleEvaluate {
  goto(url:"https://www.example.com"){
    time
  }
  evaluate(content: "document.title") {
    value
  }
}

```

For multi-line scripts, use triple quotes ( `"""`) and wrap your code in an IIFE:

```codeBlockLines_p187
mutation MultiLineEvaluate {
  goto(url:"https://www.example.com"){
    time
  }
  evaluate(content: """
  (()=>{
    const title = document.title;
    const url = window.location.href;
    return { title, url };
  })()
  """) {
    value
  }
}

```

## Important syntax requirement [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#important-syntax-requirement "Direct link to Important syntax requirement")

When writing multi-line evaluate code in BrowserQL, you must wrap your code in an IIFE (Immediately Invoked Function Expression):

- Correct IIFE syntax (required)
- Incorrect approach (will not work - missing IIFE wrap)

```codeBlockLines_p187
mutation CorrectIIFE {
  goto(url:"https://www.example.com"){
    time
  }
  evaluate(content: """
  (()=>{
    const text = document.body.innerText;
    return text;
  })()
  """) {
    value
  }
}

```

```codeBlockLines_p187
mutation IncorrectApproach {
  goto(url:"https://www.example.com"){
    time
  }
  evaluate(content: """
    // ERROR: This code is missing the required IIFE wrapper
    // Correct version would be: (()=>{ ... code ... })()
    const text = document.body.innerText;
    return text;
  """) {
    value
  }
}

```

## Working with async operations [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#working-with-async-operations "Direct link to Working with async operations")

BrowserQL's evaluate implementation can handle promises when properly wrapped in an IIFE:

- Using async/await
- Using promises

```codeBlockLines_p187
mutation AsyncEvaluate {
  goto(url: "https://www.example.com") {
    time
  }
	evaluateData: evaluate(content: """
    (async () => {
      const response = await fetch('/api/data');
      const contentType = response.headers.get('content-type') || '';
      if (!contentType.includes('application/json')) {
        const text = await response.text();
        return JSON.stringify({ error: 'Unexpected response type', content: text.slice(0, 200) });
      }
      return await response.json();
    })();
  """) {
    value
  }
}

```

```codeBlockLines_p187
mutation PromiseEvaluate {
  goto(url: "https://www.example.com") {
  	time
  }
  evaluate(content: """
  (()=>{
    return new Promise(resolve => {
      setTimeout(() => {
        resolve('Operation completed after delay');
      }, 1500);
    });
  })()
  """) {
    value
    time
  }
}

```

## Common use cases [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#common-use-cases "Direct link to Common use cases")

### Extracting data from the DOM [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#extracting-data-from-the-dom "Direct link to Extracting data from the DOM")

Note that this is a sample to demonstrate evaluate's abilities, however if you'd like to extract data from the DOM in JSON format, you can also look into our MapSelector mutation.

```codeBlockLines_p187
mutation ExtractData {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }

  evaluate(content: """
  (()=>{
    const links = Array.from(document.querySelectorAll('a')).map(a => ({
      text: a.innerText,
      href: a.href
    }));

    const title = document.title;
    const metaDescription = document.querySelector('meta[name="description"]')?.content || '';

    return JSON.stringify({
      title,
      metaDescription,
      links,
      totalLinks: links.length
    });
  })()
  """) {
    value
  }
}

```

### Manipulating the page [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#manipulating-the-page "Direct link to Manipulating the page")

```codeBlockLines_p187
mutation ManipulatePage {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }

  evaluate(content: """
  (() => {
    // Remove <p> elements
    const popups = document.querySelectorAll('.popup','.modal','p');
    popups.forEach(p => p.remove());

    // Inject an input if it doesn't exist
    let searchInput = document.querySelector('input[type="search"]');
    if (!searchInput) {
      searchInput = document.createElement('input');
      searchInput.type = 'search';
      searchInput.placeholder = 'Search...';
      document.body.appendChild(searchInput);
    }

    // Click and focus the input
    searchInput.click();
    searchInput.focus();

    //Return that the DOM was modified and indicate whether the searchInput is the active element.
    const result = {
      modified: true,
      focused: document.activeElement === searchInput
    };

    return JSON.stringify(result);
  })()
  """) {
    value
    time
  }
}

```

### Working with multiple evaluate calls [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#working-with-multiple-evaluate-calls "Direct link to Working with multiple evaluate calls")

```codeBlockLines_p187
mutation MultipleEvaluates {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }

  prepare: evaluate(content: """
  (() => {
    // Set up the page
    window.__browserless_data = {
      startTime: Date.now()
    };

    // Return success
    return true;
  })()
  """) {
    value
  }

  performAction: evaluate(content: """
  (() => {
    // Simulate some user action
    const button = document.querySelector('.action-button');
    if (button) {
      button.click();
      return true;
    }
    return false;
  })()
  """) {
    value
  }

  collectResults: evaluate(content: """
  (() => {
    const endTime = Date.now();
    const startTime = window.__browserless_data?.startTime || 0;
    const result = {
      executionTime: endTime - startTime,
      success: document.querySelector('.success-message') !== null
    };
    return JSON.stringify(result);
  })()
  """) {
    value
  }
}

```

## Using the timeout parameter and exception handling [​](https://docs.browserless.io/browserql/recipes/multi-line-evaluate\#using-the-timeout-parameter-and-exception-handling "Direct link to Using the timeout parameter and exception handling")

For long-running scripts, you can specify a custom timeout (in milliseconds) and add try/catch blocks in case there's an exception inside your function:

```codeBlockLines_p187
mutation LongRunningScript {
  goto(url: "https://www.example.com") {
    time
  }

  evaluate(
    content: """
    (() => {
      return new Promise(resolve => {
        try {
          setTimeout(() => {
            try {
              const result = JSON.stringify({
                success: true,
                data: 'Completed after delay'
              });
              resolve(result);
            } catch (innerErr) {
              resolve(JSON.stringify({
                success: false,
                error: 'Error inside timeout: ' + (innerErr.message || 'Unknown')
              }));
            }
          }, 1000); // 1 second delay
        } catch (outerErr) {
          resolve(JSON.stringify({
            success: false,
            error: 'Outer error: ' + (outerErr.message || 'Unknown')
          }));
        }
      });
    })()
    """,
    timeout: 5000
  ) {
    value
    time
  }
}

```

By default, the timeout is 30 seconds (30000ms).

- [How evaluate works in BrowserQL](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#how-evaluate-works-in-browserql)
- [Single vs. Multi-line evaluation](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#single-vs-multi-line-evaluation)
- [Important syntax requirement](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#important-syntax-requirement)
- [Working with async operations](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#working-with-async-operations)
- [Common use cases](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#common-use-cases)
  - [Extracting data from the DOM](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#extracting-data-from-the-dom)
  - [Manipulating the page](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#manipulating-the-page)
  - [Working with multiple evaluate calls](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#working-with-multiple-evaluate-calls)
- [Using the timeout parameter and exception handling](https://docs.browserless.io/browserql/recipes/multi-line-evaluate#using-the-timeout-parameter-and-exception-handling)