---
url: "https://docs.browserless.io/ai-integrations/vercel-ai-sdk"
title: "Vercel AI SDK Integration | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#__docusaurus_skipToContent_fallback)

On this page

This guide demonstrates how to build a fully functional AI-powered browser automation application using Browserless.io, Vercel AI SDK, and Next.js. The application allows AI agents to control browsers through natural language instructions, enabling tasks like web scraping, form filling, and content extraction.

## Introduction [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#introduction "Direct link to Introduction")

This integration combines three powerful technologies:

- **Browserless.io**: A headless browser service that provides browser automation capabilities
- **Vercel AI SDK**: A toolkit for building AI-powered applications
- **Next.js**: A React framework for building web applications

Together, these technologies enable you to create applications where AI can understand and execute browser automation tasks through natural language.

## Prerequisites [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#prerequisites "Direct link to Prerequisites")

- Node.js 18 or higher
- Vercel account
- Browserless.io API token
- OpenAI API key (or other supported LLM provider)

## Step 1: Project Setup [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#step-1-project-setup "Direct link to Step 1: Project Setup")

### Create a Next.js Project [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#create-a-nextjs-project "Direct link to Create a Next.js Project")

```codeBlockLines_p187
npx create-next-app@latest browserless-ai
cd browserless-ai

```

### Install Required Packages [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#install-required-packages "Direct link to Install Required Packages")

```codeBlockLines_p187
npm install @vercel/ai @browserless/ai puppeteer-core openai zod prettier

```

### Configure Environment Variables [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#configure-environment-variables "Direct link to Configure Environment Variables")

Create a `.env.local` file in your project root:

```codeBlockLines_p187
BROWSERLESS_API_KEY=your_browserless_api_key
OPENAI_API_KEY=your_openai_api_key

```

## Step 2: Core Components [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#step-2-core-components "Direct link to Step 2: Core Components")

### Browser Service [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#browser-service "Direct link to Browser Service")

Create `src/lib/browser.ts`:

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';
import { z } from 'zod';

// Schema for browser settings
const BrowserSettingsSchema = z.object({
  viewport: z.object({
    width: z.number().default(1920),
    height: z.number().default(1080),
  }),
  userAgent: z.string().optional(),
  timeout: z.number().default(30000),
});

export type BrowserSettings = z.infer<typeof BrowserSettingsSchema>;

export class BrowserlessService {
  private static instance: BrowserlessService;
  private browser: puppeteer.Browser | null = null;
  private settings: BrowserSettings;

  private constructor(settings: Partial<BrowserSettings> = {}) {
    this.settings = BrowserSettingsSchema.parse(settings);
  }

  static getInstance(settings?: Partial<BrowserSettings>): BrowserlessService {
    if (!BrowserlessService.instance) {
      BrowserlessService.instance = new BrowserlessService(settings);
    }
    return BrowserlessService.instance;
  }

  async getBrowser(): Promise<puppeteer.Browser> {
    if (!this.browser) {
      this.browser = await puppeteer.connect({
        browserWSEndpoint: `wss://production-sfo.browserless.io?token=${process.env.BROWSERLESS_API_KEY}`,
        defaultViewport: this.settings.viewport,
      });
    }
    return this.browser;
  }

  async close() {
    if (this.browser) {
      await this.browser.close();
      this.browser = null;
    }
  }
}

```

### AI Route Handler [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#ai-route-handler "Direct link to AI Route Handler")

Create `src/app/api/chat/route.ts`:

```codeBlockLines_p187
import { OpenAIStream, StreamingTextResponse } from 'ai';
import { BrowserlessService } from '@/lib/browser';
import OpenAI from 'openai';
import { z } from 'zod';

// Schema for chat messages
const MessageSchema = z.object({
  role: z.enum(['user', 'assistant', 'system']),
  content: z.string(),
});

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export async function POST(req: Request) {
  try {
    const { messages } = await req.json();

    // Validate messages
    const validatedMessages = z.array(MessageSchema).parse(messages);

    const browserService = BrowserlessService.getInstance();
    const browser = await browserService.getBrowser();
    const page = await browser.newPage();

    // Process the message and perform browser actions
    const response = await openai.chat.completions.create({
      model: 'gpt-4-turbo',
      stream: true,
      messages: [\
        {\
          role: 'system',\
          content: `You are a browser automation assistant. You can:\
          1. Navigate to URLs\
          2. Extract information from pages\
          3. Fill out forms\
          4. Take screenshots\
          5. Click elements\
          6. Type text\
          Always respond with clear instructions for the browser.`\
        },\
        ...validatedMessages,\
      ],
    });

    const stream = OpenAIStream(response, {
      async onCompletion(completion) {
        try {
          // Process the AI's response and perform browser actions
          if (completion.includes('navigate to')) {
            const url = completion.match(/navigate to (https?:\/\/[^\s]+)/)?.[1];
            if (url) {
              await page.goto(url, { waitUntil: 'networkidle0' });
            }
          }

          if (completion.includes('click')) {
            const selector = completion.match(/click "([^"]+)"/)?.[1];
            if (selector) {
              await page.click(selector);
            }
          }

          if (completion.includes('type')) {
            const [selector, text] = completion.match(/type "([^"]+)" into "([^"]+)"/)?.slice(1) || [];
            if (selector && text) {
              await page.type(selector, text);
            }
          }

          // Add more action handlers as needed
        } catch (error) {
          console.error('Error executing browser action:', error);
        }
      },
    });

    return new StreamingTextResponse(stream);
  } catch (error) {
    console.error('Error processing request:', error);
    return new Response(
      JSON.stringify({ error: 'Failed to process request' }),
      { status: 500 }
    );
  }
}

```

### Chat Interface [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#chat-interface "Direct link to Chat Interface")

Create `src/app/page.tsx`:

```codeBlockLines_p187
'use client';

import { useChat } from 'ai/react';
import { useState } from 'react';

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat();
  const [isProcessing, setIsProcessing] = useState(false);

  return (
    <div className="flex flex-col w-full max-w-2xl mx-auto p-4">
      <div className="flex-1 overflow-y-auto mb-4">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`p-4 mb-4 rounded-lg ${
              message.role === 'user'
                ? 'bg-blue-100 ml-auto'
                : 'bg-gray-100 mr-auto'
            }`}
          >
            <div className="whitespace-pre-wrap">{message.content}</div>
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          className="flex-1 p-2 border border-gray-300 rounded-lg"
          value={input}
          placeholder="Ask the AI to perform browser actions..."
          onChange={handleInputChange}
          disabled={isLoading || isProcessing}
        />
        <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded-lg disabled:opacity-50"
          disabled={isLoading || isProcessing}
        >
          Send
        </button>
      </form>
    </div>
  );
}

```

## Step 3: Advanced Features [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#step-3-advanced-features "Direct link to Step 3: Advanced Features")

### Session Management [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#session-management "Direct link to Session Management")

Create `src/lib/session.ts`:

```codeBlockLines_p187
import { BrowserlessService } from './browser';
import puppeteer from 'puppeteer-core';

export class BrowserSession {
  private static sessions: Map<string, {
    page: puppeteer.Page;
    lastActive: number;
  }> = new Map();
  private static readonly SESSION_TIMEOUT = 30 * 60 * 1000; // 30 minutes

  static async getSession(sessionId: string): Promise<puppeteer.Page> {
    const session = this.sessions.get(sessionId);

    if (session && Date.now() - session.lastActive < this.SESSION_TIMEOUT) {
      session.lastActive = Date.now();
      return session.page;
    }

    const browser = await BrowserlessService.getInstance().getBrowser();
    const page = await browser.newPage();

    this.sessions.set(sessionId, {
      page,
      lastActive: Date.now(),
    });

    return page;
  }

  static async cleanup() {
    const now = Date.now();
    for (const [sessionId, session] of this.sessions.entries()) {
      if (now - session.lastActive > this.SESSION_TIMEOUT) {
        await session.page.close();
        this.sessions.delete(sessionId);
      }
    }
  }
}

```

### Error Handling Middleware [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#error-handling-middleware "Direct link to Error Handling Middleware")

Create `src/middleware.ts`:

```codeBlockLines_p187
import { NextResponse } from 'next/server';
import { z } from 'zod';

export async function middleware(request: Request) {
  try {
    // Add rate limiting
    const ip = request.headers.get('x-forwarded-for') || 'unknown';
    // Implement your rate limiting logic here

    // Validate request body
    if (request.method === 'POST') {
      const body = await request.json();
      // Add your validation logic here
    }

    return NextResponse.next();
  } catch (error) {
    console.error('Middleware error:', error);
    return new NextResponse(
      JSON.stringify({ error: 'Internal server error' }),
      { status: 500 }
    );
  }
}

```

## Step 4: Testing [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#step-4-testing "Direct link to Step 4: Testing")

### Local Testing [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#local-testing "Direct link to Local Testing")

1. Start the development server:

```codeBlockLines_p187
npm run dev

```

2. Test the API endpoints:

```codeBlockLines_p187
curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Navigate to example.com"}]}'

```

### Production Testing [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#production-testing "Direct link to Production Testing")

1. Deploy to Vercel:

```codeBlockLines_p187
vercel

```

2. Test the deployed endpoints:

```codeBlockLines_p187
curl -X POST https://your-app.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Navigate to example.com"}]}'

```

## Step 5: Deployment [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#step-5-deployment "Direct link to Step 5: Deployment")

### Vercel Deployment [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#vercel-deployment "Direct link to Vercel Deployment")

1. Push your code to GitHub
2. Import the project in Vercel
3. Add your environment variables:
   - `BROWSERLESS_API_KEY`
   - `OPENAI_API_KEY`
4. Deploy!

### Environment Configuration [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#environment-configuration "Direct link to Environment Configuration")

Configure your Vercel project settings:

```codeBlockLines_p187
{
  "buildCommand": "next build",
  "outputDirectory": ".next",
  "framework": "nextjs",
  "installCommand": "npm install",
  "regions": ["sfo1"]
}

```

## Best Practices [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#best-practices "Direct link to Best Practices")

1. **Resource Management**
   - Always close browser pages when done
   - Implement session timeouts
   - Clean up unused resources
2. **Error Handling**
   - Implement comprehensive error handling
   - Log errors appropriately
   - Provide meaningful error messages
3. **Security**
   - Validate all inputs
   - Implement rate limiting
   - Use environment variables for sensitive data
4. **Performance**
   - Use appropriate timeouts
   - Implement caching where possible
   - Optimize browser operations
5. **Monitoring**
   - Set up error tracking
   - Monitor API usage
   - Track performance metrics

## Troubleshooting [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#troubleshooting "Direct link to Troubleshooting")

### Common Issues [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#common-issues "Direct link to Common Issues")

1. **Connection Errors**
   - Check your Browserless.io API key
   - Verify network connectivity
   - Check firewall settings
2. **Timeout Errors**
   - Increase timeout values
   - Optimize browser operations
   - Implement retry logic
3. **Rate Limit Errors**
   - Implement proper rate limiting
   - Monitor API usage
   - Consider upgrading your plan

### Debugging Tips [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#debugging-tips "Direct link to Debugging Tips")

1. Enable verbose logging:

```codeBlockLines_p187
process.env.DEBUG = 'browserless:*';

```

2. Use the Browserless.io dashboard to monitor sessions

3. Implement request logging:


```codeBlockLines_p187
console.log('Request:', {
  url: request.url,
  method: request.method,
  headers: Object.fromEntries(request.headers),
});

```

## Additional Resources [​](https://docs.browserless.io/ai-integrations/vercel-ai-sdk\#additional-resources "Direct link to Additional Resources")

- [Browserless.io Documentation](https://docs.browserless.io/)
- [Vercel AI SDK Documentation](https://sdk.vercel.ai/docs)
- [Next.js Documentation](https://nextjs.org/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

- [Introduction](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#introduction)
- [Prerequisites](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#prerequisites)
- [Step 1: Project Setup](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#step-1-project-setup)
  - [Create a Next.js Project](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#create-a-nextjs-project)
  - [Install Required Packages](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#install-required-packages)
  - [Configure Environment Variables](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#configure-environment-variables)
- [Step 2: Core Components](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#step-2-core-components)
  - [Browser Service](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#browser-service)
  - [AI Route Handler](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#ai-route-handler)
  - [Chat Interface](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#chat-interface)
- [Step 3: Advanced Features](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#step-3-advanced-features)
  - [Session Management](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#session-management)
  - [Error Handling Middleware](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#error-handling-middleware)
- [Step 4: Testing](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#step-4-testing)
  - [Local Testing](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#local-testing)
  - [Production Testing](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#production-testing)
- [Step 5: Deployment](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#step-5-deployment)
  - [Vercel Deployment](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#vercel-deployment)
  - [Environment Configuration](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#environment-configuration)
- [Best Practices](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#best-practices)
- [Troubleshooting](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#troubleshooting)
  - [Common Issues](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#common-issues)
  - [Debugging Tips](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#debugging-tips)
- [Additional Resources](https://docs.browserless.io/ai-integrations/vercel-ai-sdk#additional-resources)