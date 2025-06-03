---
url: "https://qdrant.tech/documentation/guides/running-with-gpu/"
title: "Running with GPU - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Running with GPU

# [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#running-qdrant-with-gpu-support) Running Qdrant with GPU Support

Starting from version v1.13.0, Qdrant offers support for GPU acceleration.

However, GPU support is not included in the default Qdrant binary due to additional dependencies and libraries. Instead, you will need to use dedicated Docker images with GPU support ( [NVIDIA](https://qdrant.tech/documentation/guides/running-with-gpu/#nvidia-gpus), [AMD](https://qdrant.tech/documentation/guides/running-with-gpu/#amd-gpus)).

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#configuration) Configuration

Qdrant includes a number of configuration options to control GPU usage. The following options are available:

```yaml
gpu:
    # Enable GPU indexing.
    indexing: false
    # Force half precision for `f32` values while indexing.
    # `f16` conversion will take place
    # only inside GPU memory and won't affect storage type.
    force_half_precision: false
    # Used vulkan "groups" of GPU.
    # In other words, how many parallel points can be indexed by GPU.
    # Optimal value might depend on the GPU model.
    # Proportional, but doesn't necessary equal
    # to the physical number of warps.
    # Do not change this value unless you know what you are doing.
    # Default: 512
    groups_count: 512
    # Filter for GPU devices by hardware name. Case insensitive.
    # Comma-separated list of substrings to match
    # against the gpu device name.
    # Example: "nvidia"
    # Default: "" - all devices are accepted.
    device_filter: ""
    # List of explicit GPU devices to use.
    # If host has multiple GPUs, this option allows to select specific devices
    # by their index in the list of found devices.
    # If `device_filter` is set, indexes are applied after filtering.
    # By default, all devices are accepted.
    devices: null
    # How many parallel indexing processes are allowed to run.
    # Default: 1
    parallel_indexes: 1
    # Allow to use integrated GPUs.
    # Default: false
    allow_integrated: false
    # Allow to use emulated GPUs like LLVMpipe. Useful for CI.
    # Default: false
    allow_emulated: false

```

It is not recommended to change these options unless you are familiar with the Qdrant internals and the Vulkan API.

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#standalone-gpu-support) Standalone GPU Support

For standalone usage, you can build Qdrant with GPU support by running the following command:

```bash
cargo build --release --features gpu

```

Ensure your device supports Vulkan API v1.3. This includes compatibility with Apple Silicon, Intel GPUs, and CPU emulators. Note that `gpu.indexing: true` must be set in your configuration to use GPUs at runtime.

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#nvidia-gpus) NVIDIA GPUs

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#prerequisites) Prerequisites

To use Docker with NVIDIA GPU support, ensure the following are installed on your host:

- Latest NVIDIA drivers
- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

Most AI or CUDA images on Amazon/GCP come pre-configured with the NVIDIA container toolkit.

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#docker-images-with-nvidia-gpu-support) Docker images with NVIDIA GPU support

Docker images with NVIDIA GPU support use the tag suffix `gpu-nvidia`, e.g., `qdrant/qdrant:v1.13.0-gpu-nvidia`. These images include all necessary dependencies.

To enable GPU support, use the `--gpus=all` flag with Docker settings. Example:

```bash
# `--gpus=all` flag says to Docker that we want to use GPUs.
# `-e QDRANT__GPU__INDEXING=1` flag says to Qdrant that we want to use GPUs for indexing.
docker run \
	--rm \
	--gpus=all \
	-p 6333:6333 \
	-p 6334:6334 \
	-e QDRANT__GPU__INDEXING=1 \
	qdrant/qdrant:gpu-nvidia-latest

```

To ensure that the GPU was initialized correctly, you may check it in logs. First Qdrant prints all found GPU devices without filtering and then prints list of all created devices:

```text
2025-01-13T11:58:29.124087Z  INFO gpu::instance: Found GPU device: NVIDIA GeForce RTX 3090
2025-01-13T11:58:29.124118Z  INFO gpu::instance: Found GPU device: llvmpipe (LLVM 15.0.7, 256 bits)
2025-01-13T11:58:29.124138Z  INFO gpu::device: Create GPU device NVIDIA GeForce RTX 3090

```

Here you can see that two devices were found: RTX 3090 and llvmpipe (a CPU-emulated GPU which is included in the Docker image). Later, you will see that only RTX was initialized.

This concludes the setup. Now, you can start using this Qdrant instance.

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#troubleshooting-nvidia-gpus) Troubleshooting NVIDIA GPUs

If your GPU is not detected in Docker, make sure your driver and `nvidia-container-toolkit` are up-to-date.
If needed, you can install latest version of `nvidia-container-toolkit` from it’s GitHub Releases [page](https://github.com/NVIDIA/nvidia-container-toolkit/releases)

Verify Vulkan API visibility in the Docker container using:

```bash
docker run --rm --gpus=all qdrant/qdrant:gpu-nvidia-latest vulkaninfo --summary

```

The system may show you an error message explaining why the NVIDIA device is not visible.
Note that if your NVIDIA GPU is not visible in Docker, the Docker image cannot use libGLX\_nvidia.so.0 on your host. Here is what an error message could look like:

```text
ERROR: [Loader Message] Code 0 : loader_scanned_icd_add: Could not get `vkCreateInstance` via `vk_icdGetInstanceProcAddr` for ICD libGLX_nvidia.so.0
WARNING: [Loader Message] Code 0 : terminator_CreateInstance: Failed to CreateInstance in ICD 0. Skipping ICD.

```

To resolve errors, update your NVIDIA container runtime configuration:

```bash
sudo nano /etc/nvidia-container-runtime/config.toml

```

Set `no-cgroups=false`, save the configuration, and restart Docker:

```bash
sudo systemctl restart docker

```

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#amd-gpus) AMD GPUs

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#prerequisites-1) Prerequisites

Running Qdrant with AMD GPUs requires [ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/detailed-install.html) to be installed on your host.

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#docker-images-with-amd-gpu-support) Docker images with AMD GPU support

Docker images for AMD GPUs use the tag suffix `gpu-amd`, e.g., `qdrant/qdrant:v1.13.0-gpu-amd`. These images include all required dependencies.

To enable GPU for Docker, you need additional `--device /dev/kfd --device /dev/dri` flags. To enable GPU for Qdrant you need to set the enable flag. Here is an example:

```bash
# `--device /dev/kfd --device /dev/dri` flags say to Docker that we want to use GPUs.
# `-e QDRANT__GPU__INDEXING=1` flag says to Qdrant that we want to use GPUs for indexing.
docker run \
	--rm \
	--device /dev/kfd --device /dev/dri \
	-p 6333:6333 \
	-p 6334:6334 \
	-e QDRANT__LOG_LEVEL=debug \
	-e QDRANT__GPU__INDEXING=1 \
	qdrant/qdrant:gpu-amd-latest

```

Check logs to confirm GPU initialization. Example log output:

```text
2025-01-10T11:56:55.926466Z  INFO gpu::instance: Found GPU device: AMD Radeon Graphics (RADV GFX1103_R1)
2025-01-10T11:56:55.926485Z  INFO gpu::instance: Found GPU device: llvmpipe (LLVM 17.0.6, 256 bits)
2025-01-10T11:56:55.926504Z  INFO gpu::device: Create GPU device AMD Radeon Graphics (RADV GFX1103_R1)

```

This concludes the setup. In a basic scenario, you won’t need to configure anything else.

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#known-limitations) Known limitations

- **Platform Support:** Docker images are only available for Linux x86\_64. Windows, macOS, ARM, and other platforms are not supported.

- **Memory Limits:** Each GPU can process up to 16GB of vector data per indexing iteration.


Due to this limitation, you should not create segments where either original vectors OR quantized vectors are larger than 16GB.

For example, a collection with 1536d vectors and scalar quantization can have at most:

```text
16Gb / 1536 ~= 11 million vectors per segment

```

And without quantization:

```text
16Gb / 1536 * 4 ~= 2.7 million vectors per segment

```

The maximum size of each segment can be configured in the collection settings.
Use the following operation to [change](https://qdrant.tech/documentation/concepts/collections/#update-collection-parameters) on your existing collection:

```http
PATCH collections/{collection_name}
{
  "optimizers_config": {
    "max_segment_size": 1000000
  }
}

```

Note that `max_segment_size` is specified in KiloBytes.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/running-with-GPU.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/running-with-GPU.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575512379&cv=11&fst=1748575512379&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Frunning-with-gpu%2F&hn=www.googleadservices.com&frm=0&tiba=Running%20with%20GPU%20-%20Qdrant&npa=0&pscdl=noapi&auid=648442939.1748575512&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575512359&cv=11&fst=1748575512359&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Frunning-with-gpu%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Running%20with%20GPU%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=648442939.1748575512&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ae097ed1-aa62-4125-bcd1-bb44b4316766&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3cc34605-ea26-48f2-9e2e-b95548a83c01&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Frunning-with-gpu%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ae097ed1-aa62-4125-bcd1-bb44b4316766&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3cc34605-ea26-48f2-9e2e-b95548a83c01&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Frunning-with-gpu%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575513585&cv=11&fst=1748575513585&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Frunning-with-gpu%2F&hn=www.googleadservices.com&frm=0&tiba=Running%20with%20GPU%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=648442939.1748575512&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)