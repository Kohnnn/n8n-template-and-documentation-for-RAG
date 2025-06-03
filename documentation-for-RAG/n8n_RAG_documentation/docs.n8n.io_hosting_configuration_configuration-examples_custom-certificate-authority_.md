---
url: "https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority/"
title: "Configure n8n to use your own certificate authority | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority/#configure-n8n-to-use-your-own-certificate-authority-or-self-signed-certificate)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/configuration-examples/custom-certificate-authority.md "Edit this page")

# Configure n8n to use your own certificate authority or self-signed certificate [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority/\#configure-n8n-to-use-your-own-certificate-authority-or-self-signed-certificate "Permanent link")

You can add your own certificate authority (CA) or self-signed certificate to n8n. This means you are able to trust a certain SSL certificate instead of trusting all invalid certificates, which is a potential security risk.

Available in version 1.42.0

This feature is only available in version 1.42.0+.

To use this feature you need to place your certificates in a folder and mount the folder to `/opt/custom-certificates` in the container.

## Docker [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority/\#docker "Permanent link")

The examples below assume you have a folder called `pki` that contains your certificates in either the directory you run the command from or next to your docker compose file.

### Docker CLI [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority/\#docker-cli "Permanent link")

When using the CLI you can use the `-v` flag from the command line:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>docker run -it --rm \<br> --name n8n \<br> -p 5678:5678 \<br> -v ./pki:/opt/custom-certificates \<br> docker.n8n.io/n8nio/n8n<br>``` |

### Docker Compose [\#](https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority/\#docker-compose "Permanent link")

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>name: n8n<br>services:<br>    n8n:<br>        volumes:<br>            - ./pki:/opt/custom-certificates<br>        container_name: n8n<br>        ports:<br>            - 5678:5678<br>        image: docker.n8n.io/n8nio/n8n<br>``` |

You should also give the right permissions to the imported certs. You can do this once the container is running (assuming n8n as the container name):

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>docker exec --user 0 n8n chown -R 1000:1000 /opt/custom-certificates<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top