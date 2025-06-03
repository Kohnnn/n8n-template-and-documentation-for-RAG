---
url: "https://qdrant.tech/documentation/guides/security/"
title: "Security - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Security

# [Anchor](https://qdrant.tech/documentation/guides/security/\#security) Security

Please read this page carefully. Although there are various ways to secure your Qdrant instances, **they are unsecured by default**.
You need to enable security measures before production use. Otherwise, they are completely open to anyone

## [Anchor](https://qdrant.tech/documentation/guides/security/\#authentication) Authentication

_Available as of v1.2.0_

Qdrant supports a simple form of client authentication using a static API key.
This can be used to secure your instance.

To enable API key based authentication in your own Qdrant instance you must
specify a key in the configuration:

```yaml
service:
  # Set an api-key.
  # If set, all requests must include a header with the api-key.
  # example header: `api-key: <API-KEY>`
  #
  # If you enable this you should also enable TLS.
  # (Either above or via an external service like nginx.)
  # Sending an api-key over an unencrypted channel is insecure.
  api_key: your_secret_api_key_here

```

Or alternatively, you can use the environment variable:

```bash
docker run -p 6333:6333 \
    -e QDRANT__SERVICE__API_KEY=your_secret_api_key_here \
    qdrant/qdrant

```

For using API key based authentication in Qdrant Cloud see the cloud
[Authentication](https://qdrant.tech/documentation/cloud/authentication/)
section.

The API key then needs to be present in all REST or gRPC requests to your instance.
All official Qdrant clients for Python, Go, Rust, .NET and Java support the API key parameter.

bashpythontypescriptrustjavacsharpgo

```bash
curl \
  -X GET https://localhost:6333 \
  --header 'api-key: your_secret_api_key_here'

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(
    url="https://localhost:6333",
    api_key="your_secret_api_key_here",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  url: "http://localhost",
  port: 6333,
  apiKey: "your_secret_api_key_here",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.eu-central.aws.cloud.qdrant.io:6334")
    .api_key("<paste-your-api-key-here>")
    .build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder(
                "xyz-example.eu-central.aws.cloud.qdrant.io",
                6334,
                true)
            .withApiKey("<paste-your-api-key-here>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  https: true,
  apiKey: "<paste-your-api-key-here>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.eu-central.aws.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<paste-your-api-key-here>",
	UseTLS: true,
})

```

### [Anchor](https://qdrant.tech/documentation/guides/security/\#read-only-api-key) Read-only API key

_Available as of v1.7.0_

In addition to the regular API key, Qdrant also supports a read-only API key.
This key can be used to access read-only operations on the instance.

```yaml
service:
  read_only_api_key: your_secret_read_only_api_key_here

```

Or with the environment variable:

```bash
export QDRANT__SERVICE__READ_ONLY_API_KEY=your_secret_read_only_api_key_here

```

Both API keys can be used simultaneously.

### [Anchor](https://qdrant.tech/documentation/guides/security/\#granular-access-control-with-jwt) Granular access control with JWT

_Available as of v1.9.0_

For more complex cases, Qdrant supports granular access control with [JSON Web Tokens (JWT)](https://jwt.io/).
This allows you to create tokens which restrict access to data stored in your cluster, and build [Role-based access control (RBAC)](https://en.wikipedia.org/wiki/Role-based_access_control) on top of that.
In this way, you can define permissions for users and restrict access to sensitive endpoints.

To enable JWT-based authentication in your own Qdrant instance you need to specify the `api-key` and enable the `jwt_rbac` feature in the configuration:

```yaml
service:
  api_key: you_secret_api_key_here
  jwt_rbac: true

```

Or with the environment variables:

```bash
export QDRANT__SERVICE__API_KEY=your_secret_api_key_here
export QDRANT__SERVICE__JWT_RBAC=true

```

The `api_key` you set in the configuration will be used to encode and decode the JWTs, so –needless to say– keep it secure. If your `api_key` changes, all existing tokens will be invalid.

To use JWT-based authentication, you need to provide it as a bearer token in the `Authorization` header, or as an key in the `Api-Key` header of your requests.

httppythontypescriptrustjavacsharpgo

```http
Authorization: Bearer <JWT>

// or

Api-Key: <JWT>

```

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    "xyz-example.eu-central.aws.cloud.qdrant.io",
    api_key="<JWT>",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  apiKey: "<JWT>",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.eu-central.aws.cloud.qdrant.io:6334")
    .api_key("<JWT>")
    .build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder(
                "xyz-example.eu-central.aws.cloud.qdrant.io",
                6334,
                true)
            .withApiKey("<JWT>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  https: true,
  apiKey: "<JWT>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.eu-central.aws.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<JWT>",
	UseTLS: true,
})

```

#### [Anchor](https://qdrant.tech/documentation/guides/security/\#generating-json-web-tokens) Generating JSON Web Tokens

Due to the nature of JWT, anyone who knows the `api_key` can generate tokens by using any of the existing libraries and tools, it is not necessary for them to have access to the Qdrant instance to generate them.

For convenience, we have added a JWT generation tool the Qdrant Web UI under the 🔑 tab, if you’re using the default url, it will be at `http://localhost:6333/dashboard#/jwt`.

- **JWT Header** \- Qdrant uses the `HS256` algorithm to decode the tokens.



```json
{
    "alg": "HS256",
    "typ": "JWT"
}

```

- **JWT Payload** \- You can include any combination of the [parameters available](https://qdrant.tech/documentation/guides/security/#jwt-configuration) in the payload. Keep reading for more info on each one.



```json
{
    "exp": 1640995200, // Expiration time
    "value_exists": ..., // Validate this token by looking for a point with a payload value
    "access": "r", // Define the access level.
}

```


**Signing the token** \- To confirm that the generated token is valid, it needs to be signed with the `api_key` you have set in the configuration.
That would mean, that someone who knows the `api_key` gives the authorization for the new token to be used in the Qdrant instance.
Qdrant can validate the signature, because it knows the `api_key` and can decode the token.

The process of token generation can be done on the client side offline, and doesn’t require any communication with the Qdrant instance.

Here is an example of libraries that can be used to generate JWT tokens:

- Python: [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
- JavaScript: [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)
- Rust: [jsonwebtoken](https://crates.io/crates/jsonwebtoken)

#### [Anchor](https://qdrant.tech/documentation/guides/security/\#jwt-configuration) JWT Configuration

These are the available options, or **claims** in the JWT lingo. You can use them in the JWT payload to define its functionality.

- **`exp`** \- The expiration time of the token. This is a Unix timestamp in seconds. The token will be invalid after this time. The check for this claim includes a 30-second leeway to account for clock skew.



```json
{
    "exp": 1640995200, // Expiration time
}

```

- **`value_exists`** \- This is a claim that can be used to validate the token against the data stored in a collection. Structure of this claim is as follows:



```json
{
    "value_exists": {
      "collection": "my_validation_collection",
      "matches": [\
        { "key": "my_key", "value": "value_that_must_exist" }\
      ],
    },
}

```



If this claim is present, Qdrant will check if there is a point in the collection with the specified key-values. If it does, the token is valid.

This claim is especially useful if you want to have an ability to revoke tokens without changing the `api_key`.
Consider a case where you have a collection of users, and you want to revoke access to a specific user.



```json
{
    "value_exists": {
      "collection": "users",
      "matches": [\
        { "key": "user_id", "value": "andrey" },\
        { "key": "role", "value": "manager" }\
      ],
    },
}

```



You can create a token with this claim, and when you want to revoke access, you can change the `role` of the user to something else, and the token will be invalid.

- **`access`** \- This claim defines the [access level](https://qdrant.tech/documentation/guides/security/#table-of-access) of the token. If this claim is present, Qdrant will check if the token has the required access level to perform the operation. If this claim is **not** present, **manage** access is assumed.

It can provide global access with `r` for read-only, or `m` for manage. For example:



```json
{
    "access": "r"
}

```



It can also be specific to one or more collections. The `access` level for each collection is `r` for read-only, or `rw` for read-write, like this:



```json
{
    "access": [\
      {\
        "collection": "my_collection",\
        "access": "rw"\
      }\
    ]
}

```



You can also specify which subset of the collection the user is able to access by specifying a `payload` restriction that the points must have.



```json
{
    "access": [\
      {\
        "collection": "my_collection",\
        "access": "r",\
        "payload": {\
          "user_id": "user_123456"\
        }\
      }\
    ]
}

```



This `payload` claim will be used to implicitly filter the points in the collection. It will be equivalent to appending this filter to each request:



```json
{ "filter": { "must": [{ "key": "user_id", "match": { "value": "user_123456" } }] } }

```


### [Anchor](https://qdrant.tech/documentation/guides/security/\#table-of-access) Table of access

Check out this table to see which actions are allowed or denied based on the access level.

This is also applicable to using api keys instead of tokens. In that case, `api_key` maps to **manage**, while `read_only_api_key` maps to **read-only**.

**Symbols:** ✅ Allowed \| ❌ Denied \| 🟡 Allowed, but filtered

| Action | manage | read-only | collection read-write | collection read-only | collection with payload claim (r / rw) |
| --- | --- | --- | --- | --- | --- |
| list collections | ✅ | ✅ | 🟡 | 🟡 | 🟡 |
| get collection info | ✅ | ✅ | ✅ | ✅ | ❌ |
| create collection | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete collection | ✅ | ❌ | ❌ | ❌ | ❌ |
| update collection params | ✅ | ❌ | ❌ | ❌ | ❌ |
| get collection cluster info | ✅ | ✅ | ✅ | ✅ | ❌ |
| collection exists | ✅ | ✅ | ✅ | ✅ | ✅ |
| update collection cluster setup | ✅ | ❌ | ❌ | ❌ | ❌ |
| update aliases | ✅ | ❌ | ❌ | ❌ | ❌ |
| list collection aliases | ✅ | ✅ | 🟡 | 🟡 | 🟡 |
| list aliases | ✅ | ✅ | 🟡 | 🟡 | 🟡 |
| create shard key | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete shard key | ✅ | ❌ | ❌ | ❌ | ❌ |
| create payload index | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete payload index | ✅ | ❌ | ✅ | ❌ | ❌ |
| list collection snapshots | ✅ | ✅ | ✅ | ✅ | ❌ |
| create collection snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete collection snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| download collection snapshot | ✅ | ✅ | ✅ | ✅ | ❌ |
| upload collection snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| recover collection snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| list shard snapshots | ✅ | ✅ | ✅ | ✅ | ❌ |
| create shard snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete shard snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| download shard snapshot | ✅ | ✅ | ✅ | ✅ | ❌ |
| upload shard snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| recover shard snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| list full snapshots | ✅ | ✅ | ❌ | ❌ | ❌ |
| create full snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete full snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| download full snapshot | ✅ | ✅ | ❌ | ❌ | ❌ |
| get cluster info | ✅ | ✅ | ❌ | ❌ | ❌ |
| recover raft state | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete peer | ✅ | ❌ | ❌ | ❌ | ❌ |
| get point | ✅ | ✅ | ✅ | ✅ | ❌ |
| get points | ✅ | ✅ | ✅ | ✅ | ❌ |
| upsert points | ✅ | ❌ | ✅ | ❌ | ❌ |
| update points batch | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete points | ✅ | ❌ | ✅ | ❌ | ❌ / 🟡 |
| update vectors | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete vectors | ✅ | ❌ | ✅ | ❌ | ❌ / 🟡 |
| set payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| overwrite payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| clear payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| scroll points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| query points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| search points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| search groups | ✅ | ✅ | ✅ | ✅ | 🟡 |
| recommend points | ✅ | ✅ | ✅ | ✅ | ❌ |
| recommend groups | ✅ | ✅ | ✅ | ✅ | ❌ |
| discover points | ✅ | ✅ | ✅ | ✅ | ❌ |
| count points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| version | ✅ | ✅ | ✅ | ✅ | ✅ |
| readyz, healthz, livez | ✅ | ✅ | ✅ | ✅ | ✅ |
| telemetry | ✅ | ✅ | ❌ | ❌ | ❌ |
| metrics | ✅ | ✅ | ❌ | ❌ | ❌ |
| update locks | ✅ | ❌ | ❌ | ❌ | ❌ |
| get locks | ✅ | ✅ | ❌ | ❌ | ❌ |

## [Anchor](https://qdrant.tech/documentation/guides/security/\#tls) TLS

_Available as of v1.2.0_

TLS for encrypted connections can be enabled on your Qdrant instance to secure
connections.

First make sure you have a certificate and private key for TLS, usually in
`.pem` format. On your local machine you may use
[mkcert](https://github.com/FiloSottile/mkcert#readme) to generate a self signed
certificate.

To enable TLS, set the following properties in the Qdrant configuration with the
correct paths and restart:

```yaml
service:
  # Enable HTTPS for the REST and gRPC API
  enable_tls: true

# TLS configuration.
# Required if either service.enable_tls or cluster.p2p.enable_tls is true.
tls:
  # Server certificate chain file
  cert: ./tls/cert.pem

  # Server private key file
  key: ./tls/key.pem

```

For internal communication when running cluster mode, TLS can be enabled with:

```yaml
cluster:
  # Configuration of the inter-cluster communication
  p2p:
    # Use TLS for communication between peers
    enable_tls: true

```

With TLS enabled, you must start using HTTPS connections. For example:

bashpythontypescriptrust

```bash
curl -X GET https://localhost:6333

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(
    url="https://localhost:6333",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ url: "https://localhost", port: 6333 });

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

```

Certificate rotation is enabled with a default refresh time of one hour. This
reloads certificate files every hour while Qdrant is running. This way changed
certificates are picked up when they get updated externally. The refresh time
can be tuned by changing the `tls.cert_ttl` setting. You can leave this on, even
if you don’t plan to update your certificates. Currently this is only supported
for the REST API.

Optionally, you can enable client certificate validation on the server against a
local certificate authority. Set the following properties and restart:

```yaml
service:
  # Check user HTTPS client certificate against CA file specified in tls config
  verify_https_client_certificate: false

# TLS configuration.
# Required if either service.enable_tls or cluster.p2p.enable_tls is true.
tls:
  # Certificate authority certificate file.
  # This certificate will be used to validate the certificates
  # presented by other nodes during inter-cluster communication.
  #
  # If verify_https_client_certificate is true, it will verify
  # HTTPS client certificate
  #
  # Required if cluster.p2p.enable_tls is true.
  ca_cert: ./tls/cacert.pem

```

## [Anchor](https://qdrant.tech/documentation/guides/security/\#hardening) Hardening

We recommend reducing the amount of permissions granted to Qdrant containers so that you can reduce the risk of exploitation. Here are some ways to reduce the permissions of a Qdrant container:

- Run Qdrant as a non-root user. This can help mitigate the risk of future container breakout vulnerabilities. Qdrant does not need the privileges of the root user for any purpose.

  - You can use the image `qdrant/qdrant:<version>-unprivileged` instead of the default Qdrant image.
  - You can use the flag `--user=1000:2000` when running [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/).
  - You can set [`user: 1000`](https://docs.docker.com/compose/compose-file/05-services/#user) when using Docker Compose.
  - You can set [`runAsUser: 1000`](https://kubernetes.io/docs/tasks/configure-pod-container/security-context) when running in Kubernetes (our [Helm chart](https://github.com/qdrant/qdrant-helm) does this by default).
- Run Qdrant with a read-only root filesystem. This can help mitigate vulnerabilities that require the ability to modify system files, which is a permission Qdrant does not need. As long as the container uses mounted volumes for storage ( `/qdrant/storage` and `/qdrant/snapshots` by default), Qdrant can continue to operate while being prevented from writing data outside of those volumes.

  - You can use the flag `--read-only` when running [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/).
  - You can set [`read_only: true`](https://docs.docker.com/compose/compose-file/05-services/#read_only) when using Docker Compose.
  - You can set [`readOnlyRootFilesystem: true`](https://kubernetes.io/docs/tasks/configure-pod-container/security-context) when running in Kubernetes (our [Helm chart](https://github.com/qdrant/qdrant-helm) does this by default).
- Block Qdrant’s external network access. This can help mitigate [server side request forgery attacks](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery), like via the [snapshot recovery API](https://api.qdrant.tech/api-reference/snapshots/recover-from-snapshot). Single-node Qdrant clusters do not require any outbound network access. Multi-node Qdrant clusters only need the ability to connect to other Qdrant nodes via TCP ports 6333, 6334, and 6335.

  - You can use [`docker network create --internal <name>`](https://docs.docker.com/reference/cli/docker/network/create/#internal) and use that network when running [`docker run --network <name>`](https://docs.docker.com/reference/cli/docker/container/run/#network).
  - You can create an [internal network](https://docs.docker.com/compose/compose-file/06-networks/#internal) when using Docker Compose.
  - You can create a [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) when using Kubernetes. Note that multi-node Qdrant clusters [will also need access to cluster DNS in Kubernetes](https://github.com/ahmetb/kubernetes-network-policy-recipes/blob/master/11-deny-egress-traffic-from-an-application.md#allowing-dns-traffic).

There are other techniques for reducing the permissions such as dropping [Linux capabilities](https://www.man7.org/linux/man-pages/man7/capabilities.7.html) depending on your deployment method, but the methods mentioned above are the most important.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/security.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/security.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)

## Privacy Preference Center

Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.


[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)

Allow All

### Manage Consent Preferences

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575241184&cv=11&fst=1748575241184&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fsecurity%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Security%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=478168294.1748575241&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575241297&cv=11&fst=1748575241297&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fsecurity%2F&hn=www.googleadservices.com&frm=0&tiba=Security%20-%20Qdrant&npa=0&pscdl=noapi&auid=478168294.1748575241&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=404e6628-01ae-496d-a62b-13df53ce6e10&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=be25d026-8129-4d20-abe0-fd4af2b0b0a7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fsecurity%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=404e6628-01ae-496d-a62b-13df53ce6e10&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=be25d026-8129-4d20-abe0-fd4af2b0b0a7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fsecurity%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575242741&cv=11&fst=1748575242741&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fsecurity%2F&hn=www.googleadservices.com&frm=0&tiba=Security%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=478168294.1748575241&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)