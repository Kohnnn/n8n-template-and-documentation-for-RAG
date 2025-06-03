---
url: "https://docs.n8n.io/hosting/logging-monitoring/logging/"
title: "Logging | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/logging-monitoring/logging/#logging-in-n8n)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/logging-monitoring/logging.md "Edit this page")

# Logging in n8n [\#](https://docs.n8n.io/hosting/logging-monitoring/logging/\#logging-in-n8n "Permanent link")

Logging is an important feature for debugging. n8n uses the [winston](https://www.npmjs.com/package/winston) logging library.

Log streaming

n8n Self-hosted Enterprise tier includes [Log streaming](https://docs.n8n.io/log-streaming/), in addition to the logging options described in this document.

## Setup [\#](https://docs.n8n.io/hosting/logging-monitoring/logging/\#setup "Permanent link")

To set up logging in n8n, you need to set the following environment variables (you can also set the values in the [configuration file](https://docs.n8n.io/hosting/configuration/environment-variables/))

| Setting in the configuration file | Using environment variables | Description |
| --- | --- | --- |
| n8n.log.level | N8N\_LOG\_LEVEL | The log output level. The available options are (from lowest to highest level) are error, warn, info, and debug. The default value is `info`. You can learn more about these options [here](https://docs.n8n.io/hosting/logging-monitoring/logging/#log-levels). |
| n8n.log.output | N8N\_LOG\_OUTPUT | Where to output logs. The available options are `console` and `file`. Multiple values can be used separated by a comma ( `,`). `console` is used by default. |
| n8n.log.file.location | N8N\_LOG\_FILE\_LOCATION | The log file location, used only if log output is set to file. By default, `<n8nFolderPath>/logs/n8n.log` is used. |
| n8n.log.file.maxsize | N8N\_LOG\_FILE\_SIZE\_MAX | The maximum size (in MB) for each log file. By default, n8n uses 16 MB. |
| n8n.log.file.maxcount | N8N\_LOG\_FILE\_COUNT\_MAX | The maximum number of log files to keep. The default value is 100. This value should be set when using workers. |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>``` | ```<br># Set the logging level to 'debug'<br>export N8N_LOG_LEVEL=debug<br># Set log output to both console and a log file<br>export N8N_LOG_OUTPUT=console,file<br># Set a save location for the log file<br>export N8N_LOG_FILE_LOCATION=/home/jim/n8n/logs/n8n.log<br># Set a 50 MB maximum size for each log file<br>export N8N_LOG_FILE_MAXSIZE=50<br># Set 60 as the maximum number of log files to be kept<br>export N8N_LOG_FILE_MAXCOUNT=60<br>``` |

### Log levels [\#](https://docs.n8n.io/hosting/logging-monitoring/logging/\#log-levels "Permanent link")

n8n uses standard log levels to report:

- `silent`: outputs nothing at all
- `error`: outputs only errors and nothing else
- `warn`: outputs errors and warning messages
- `info`: contains useful information about progress
- `debug`: the most verbose output. n8n outputs a lot of information to help you debug issues.

## Development [\#](https://docs.n8n.io/hosting/logging-monitoring/logging/\#development "Permanent link")

During development, adding log messages is a good practice. It assists in debugging errors. To configure logging for development, follow the guide below.

### Implementation details [\#](https://docs.n8n.io/hosting/logging-monitoring/logging/\#implementation-details "Permanent link")

n8n uses the `LoggerProxy` class, located in the `workflow` package. Calling the `LoggerProxy.init()` by passing in an instance of `Logger`, initializes the class before the usage.

The initialization process happens only once. The [`start.ts`](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) file already does this process for you. If you are creating a new command from scratch, you need to initialize the `LoggerProxy` class.

Once the `Logger` implementation gets created in the `cli` package, it can be obtained by calling the `getInstance` convenience method from the exported module.

Check the [start.ts](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) file to learn more about how this process works.

### Adding logs [\#](https://docs.n8n.io/hosting/logging-monitoring/logging/\#adding-logs "Permanent link")

Once the `LoggerProxy` class gets initialized in the project, you can import it to any other file and add logs.

Convenience methods are provided for all logging levels, so new logs can be added whenever needed using the format `Logger.<logLevel>('<message>', ...meta)`, where `meta` represents any additional properties desired beyond `message`.

In the example above, we use the standard log levels described [above](https://docs.n8n.io/hosting/logging-monitoring/logging/#log-levels). The `message` argument is a string, and `meta` is a data object.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>// You have to import the LoggerProxy. We rename it to Logger to make it easier<br>import {<br>	LoggerProxy as Logger<br>} from 'n8n-workflow';<br>// Info-level logging of a trigger function, with workflow name and workflow ID as additional metadata properties<br>Logger.info(`Polling trigger initiated for workflow "${workflow.name}"`, {workflowName: workflow.name, workflowId: workflow.id});<br>``` |

When creating new loggers, some useful standards to keep in mind are:

- Craft log messages to be as human-readable as possible. For example, always wrap names in quotes.
- Duplicating information in the log message and metadata, like workflow name in the above example, can be useful as messages are easier to search and metadata enables easier filtering.
- Include multiple IDs (for example, `executionId`, `workflowId`, and `sessionId`) throughout all logs.
- Use node types instead of node names (or both) as this is more consistent, and so easier to search.

## Front-end logs [\#](https://docs.n8n.io/hosting/logging-monitoring/logging/\#front-end-logs "Permanent link")

As of now, front-end logs aren't available. Using `Logger` or `LoggerProxy` would yield errors in the `editor-ui` package. This functionality will get implemented in the future versions.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top