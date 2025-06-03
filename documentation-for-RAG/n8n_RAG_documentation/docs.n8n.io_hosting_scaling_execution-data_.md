---
url: "https://docs.n8n.io/hosting/scaling/execution-data/"
title: "Execution data | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/scaling/execution-data/#execution-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/scaling/execution-data.md "Edit this page")

# Execution data [\#](https://docs.n8n.io/hosting/scaling/execution-data/\#execution-data "Permanent link")

Depending on your executions settings and volume, your n8n database can grow in size and run out of storage.

To avoid this, n8n recommends that you don't save unnecessary data, and enable pruning of old executions data.

To do this, configure the corresponding [environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/executions/).

## Reduce saved data [\#](https://docs.n8n.io/hosting/scaling/execution-data/\#reduce-saved-data "Permanent link")

Configuration at workflow level

You can also configure these settings on an individual workflow basis using the [workflow settings](https://docs.n8n.io/workflows/settings/).

You can select which executions data n8n saves. For example, you can save only executions that result in an `Error`.

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>``` | ```<br># npm<br># Save executions ending in errors<br>export EXECUTIONS_DATA_SAVE_ON_ERROR=all<br># Save successful executions<br>export EXECUTIONS_DATA_SAVE_ON_SUCCESS=all<br># Don't save node progress for each execution<br>export EXECUTIONS_DATA_SAVE_ON_PROGRESS=false<br># Don't save manually launched executions<br>export EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br># Docker<br>docker run -it --rm \<br> --name n8n \<br> -p 5678:5678 \<br> -e EXECUTIONS_DATA_SAVE_ON_ERROR=all \<br> -e EXECUTIONS_DATA_SAVE_ON_SUCCESS=none \<br> -e EXECUTIONS_DATA_SAVE_ON_PROGRESS=true \<br> -e EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false \<br> docker.n8n.io/n8nio/n8n<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>``` | ```<br># Docker Compose<br>n8n:<br>    environment:<br>      - EXECUTIONS_DATA_SAVE_ON_ERROR=all<br>      - EXECUTIONS_DATA_SAVE_ON_SUCCESS=none<br>      - EXECUTIONS_DATA_SAVE_ON_PROGRESS=true<br>      - EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false<br>``` |

## Enable data pruning [\#](https://docs.n8n.io/hosting/scaling/execution-data/\#enable-data-pruning "Permanent link")

You can enable data pruning to automatically delete finished executions after a given time. If you don't set `EXECUTIONS_DATA_MAX_AGE`, 336 hours (14 days) is the default.

You can choose to prune finished executions data before the time set in `EXECUTIONS_DATA_MAX_AGE`, using `EXECUTIONS_DATA_PRUNE_MAX_COUNT`. This sets a maximum number of executions to store in the database. Once you reach the limit, n8n starts to delete the oldest execution records. This can help with database performance issues, especially if you use SQLite. The database size can still exceed the limit you set: old executions that haven't finished running don't get deleted, even if they would otherwise be subject to deletion.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br># npm<br># Activate automatic data pruning<br>export EXECUTIONS_DATA_PRUNE=true<br># Number of hours after execution that n8n deletes data<br>export EXECUTIONS_DATA_MAX_AGE=168<br># Number of executions to store<br>export EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>``` | ```<br># Docker<br>docker run -it --rm \<br> --name n8n \<br> -p 5678:5678 \<br> -e EXECUTIONS_DATA_PRUNE=true \<br> -e EXECUTIONS_DATA_MAX_AGE=168 \<br> docker.n8n.io/n8nio/n8n<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br># Docker Compose<br>n8n:<br>    environment:<br>      - EXECUTIONS_DATA_PRUNE=true<br>      - EXECUTIONS_DATA_MAX_AGE=168<br>	  	- EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000<br>``` |

SQLite

If you run n8n using the default SQLite database, the disk space of any pruned data isn't automatically freed up but rather reused for future executions data. To free up this space configure the `DB_SQLITE_VACUUM_ON_STARTUP` [environment variable](https://docs.n8n.io/hosting/configuration/environment-variables/database/#sqlite) or manually run the [VACUUM](https://www.sqlite.org/lang_vacuum.html) operation.

Binary data pruning

Binary data pruning operates on the active binary data mode. For example, if your instance stored data in S3, and you later switched to filesystem mode, n8n only prunes binary data in the filesystem. This may change in future.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top