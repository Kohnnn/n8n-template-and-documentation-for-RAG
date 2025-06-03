---
url: "https://supabase.com/features/mcp-server"
title: "MCP Server | Supabase Features"
---

[Previous feature](https://supabase.com/features/logs-analytics) [Next feature](https://supabase.com/features/management-api)

Stage:

Public Alpha

Available on self-hosted:

Yes

The MCP Server bridges the gap between AI tools and your Supabase projects, enabling natural language commands and agent-like experiences for database management. It standardizes how Large Language Models (LLMs) communicate with platforms like Supabase, allowing AI tools such as Cursor, Claude, and Windsurf to spin up projects, design tables, query data, and manage configurations—all through a unified protocol.

With the MCP Server, you can:

- Create and manage Supabase projects directly from your AI tool.
- Design tables, generate migrations, and manage schema.
- Query data and run reports using SQL.
- Manage branches, configurations, and TypeScript types.
- Retrieve logs for debugging and troubleshooting.
- Automate repetitive tasks and streamline AI-assisted development workflows.

The MCP Server simplifies the integration of AI tools with Supabase, enabling a seamless development experience without the need for custom APIs or wrappers.

## Key benefits

1. AI-native development: Let AI tools like Cursor or Claude manage your Supabase projects with natural language commands.
2. Standardized tool ecosystem: MCP standardizes how tools interact with Supabase, enabling a plug-and-play experience for AI-powered workflows.
3. Streamlined workflows: Build faster by offloading repetitive tasks like schema design and configuration management to your AI assistant.
4. Extensive toolset: Access over 20 tools for database design, data querying, and project management.
5. Evolving capabilities: MCP continues to evolve, with upcoming support for native OAuth authentication, Edge Function deployment, and advanced schema discovery.

The MCP Server empowers developers to build AI-native applications, accelerating productivity and reducing the complexity of working across multiple tools.

## Use Cases for MCP Server

The MCP Server unlocks new possibilities for AI-assisted development across various teams:

- Frontend developers. Use tools like Cursor to scaffold Next.js apps backed by Supabase, configure environment files, and manage schema without leaving the IDE.
- Backend engineers. Automate tasks like table creation, migrations, and TypeScript generation directly from AI tools.
- AI engineers. Build custom AI agents that interact with Supabase databases, enabling dynamic and responsive AI-powered applications.
- Educators & learners. Explore modern AI development practices by combining LLMs and databases in real-world projects.

## Integration capabilities with Supabase MCP Server

The MCP Server integrates seamlessly with popular AI tools and the broader Supabase ecosystem:

- Cursor. Connect your IDE directly to Supabase for AI-driven development workflows.
- Claude. Use Claude desktop and code tools to interact with Supabase resources and services.
- Windsurf (Codium). Configure the MCP Server to manage Supabase projects directly within Codium's AI assistant.
- Visual Studio Code (Copilot). Leverage AI capabilities to query data, generate types, and manage projects within VS Code.
- Cline (VS Code extension). Connect Cline to Supabase through the MCP Server for AI-assisted database operations.

These integrations empower developers to streamline workflows, reduce manual effort, and enhance productivity in AI-driven environments.

## FAQs about the MCP Server

Below are answers to common questions about the MCP Server, covering its functionality, compatibility, and setup requirements.

### What is the Model Context Protocol (MCP)?

MCP is a standard that defines how AI tools and platforms communicate. It enables AI tools to interact with Supabase by calling functions, retrieving data, and executing tasks through a common protocol.

### Do I need a personal access token (PAT) to use the MCP Server?

Yes, you'll need to create a PAT in your Supabase settings to authenticate the MCP Server. Future versions of MCP will support OAuth login flows for simpler authentication.

### Can I use the MCP Server with self-hosted Supabase instances?

No, the official Supabase MCP Server connects directly to Supabase Cloud. For local instances, you can use the Postgres MCP Server instead.

### Which AI tools are compatible with the MCP Server?

The MCP Server works with popular AI tools like Cursor, Claude, Windsurf, Visual Studio Code (CoPilot), and Cline. More tools will be supported as they adopt the MCP standard.

### Can the MCP Server modify my database schema or data?

Yes, the MCP Server can perform actions like creating tables, running queries, and managing branches. Use best practices like branching and access controls to protect production data.

[Read Documentation](https://supabase.com/docs/guides/getting-started/mcp)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fmcp-server&text=MCP%20Server%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fmcp-server&text=MCP%20Server%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fmcp-server&t=MCP%20Server%20%7C%20Supabase%20Features)

[Logs & Analytics](https://supabase.com/features/logs-analytics) [Management API](https://supabase.com/features/management-api)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)