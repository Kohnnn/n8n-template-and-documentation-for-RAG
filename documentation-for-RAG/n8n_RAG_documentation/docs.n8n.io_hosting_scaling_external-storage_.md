---
url: "https://docs.n8n.io/hosting/scaling/external-storage/"
title: "External storage for binary data | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/hosting/scaling/external-storage/#external-storage)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/scaling/external-storage.md "Edit this page")

# External storage [\#](https://docs.n8n.io/hosting/scaling/external-storage/\#external-storage "Permanent link")

Feature availability

- Available on Self-hosted Enterprise plans
- If you want access to this feature on Cloud Enterprise, [contact n8n](https://n8n-community.typeform.com/to/y9X2YuGa).

n8n can store binary data produced by workflow executions externally. This feature is useful to avoid relying on the filesystem for storing large amounts of binary data.

n8n will introduce external storage for other data types in the future.

## Storing n8n's binary data in S3 [\#](https://docs.n8n.io/hosting/scaling/external-storage/\#storing-n8ns-binary-data-in-s3 "Permanent link")

n8n supports [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) as an external store for binary data produced by workflow executions. You can use other S3-compatible services like Cloudflare R2 and Backblaze B2, but n8n doesn't officially support these.

Enterprise-tier feature

You will need an [Enterprise license key](https://docs.n8n.io/license-key/) for external storage. If your license key expires and you remain on S3 mode, the instance will be able to read from, but not write to, the S3 bucket.

### Setup [\#](https://docs.n8n.io/hosting/scaling/external-storage/\#setup "Permanent link")

Create and configure a bucket following the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html). You can use the following policy, replacing `<bucket-name>` with the name of the bucket you created:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>{<br> "Version": "2012-10-17",<br> "Statement": [<br>  {<br>   "Sid": "VisualEditor0",<br>   "Effect": "Allow",<br>   "Action": ["s3:*"],<br>   "Resource": ["arn:aws:s3:::<bucket-name>", "arn:aws:s3:::<bucket-name>/*"]<br>  }<br> ]<br>}<br>``` |

Set a bucket-level lifecycle configuration so that S3 automatically deletes old binary data. n8n delegates pruning of binary data to S3, so setting a lifecycle configuration is required unless you want to preserve binary data indefinitely.

Once you finish creating the bucket, you will have a host, bucket name and region, and an access key ID and secret access key. You need to set them in n8n's environment:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>export N8N_EXTERNAL_STORAGE_S3_HOST=... # example: s3.us-east-1.amazonaws.com<br>export N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME=...<br>export N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION=...<br>export N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY=...<br>export N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET=...<br>``` |

No region

If your provider doesn't require a region, you can set `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` to `'auto'`.

Tell n8n to store binary data in S3:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>export N8N_AVAILABLE_BINARY_DATA_MODES=filesystem,s3<br>export N8N_DEFAULT_BINARY_DATA_MODE=s3<br>``` |

Auth autodetection

To automatically detect credentials to authenticate your S3 calls, set `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` to `true`. This will use the default [credential provider chain](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html#credchain).

Restart the server to load the new configuration.

### Usage [\#](https://docs.n8n.io/hosting/scaling/external-storage/\#usage "Permanent link")

After you enable S3, n8n writes and reads any new binary data to and from the S3 bucket. n8n writes binary data to your S3 bucket in this format:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>workflows/{workflowId}/executions/{executionId}/binary_data/{binaryFileId}<br>``` |

n8n continues to read older binary data stored in the filesystem from the filesystem, if `filesystem` remains listed as an option in `N8N_AVAILABLE_BINARY_DATA_MODES`.

If you store binary data in S3 and later switch to filesystem mode, the instance continues to read any data stored in S3, as long as `s3` remains listed in `N8N_AVAILABLE_BINARY_DATA_MODES` and your S3 credentials remain valid.

Binary data pruning

Binary data pruning operates on the active binary data mode. For example, if your instance stored data in S3, and you later switched to filesystem mode, n8n only prunes binary data in the filesystem. This may change in future.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top