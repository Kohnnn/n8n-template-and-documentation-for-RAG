---
url: "https://qdrant.tech/documentation/cloud-rbac/permission-reference/"
title: "Permission Reference - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud rbac](https://qdrant.tech/documentation/cloud-rbac/)
- Permission Reference

# [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#permission-reference)**Permission Reference**

This document outlines the permissions available in Qdrant Cloud.

* * *

> 💡 When enabling `write:*` permissions in the UI, the corresponding `read:*` permission will also be enabled and non-actionable. This guarantees access to resources after creating and/or updating them.

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#identity-and-access-management)**Identity and Access Management**

Permissions for users, user roles, management keys, and invitations.

| Permission | Description |
| --- | --- |
| `read:roles` | View roles in the Access Management page. |
| `write:roles` | Create and modify roles in the Access Management page. |
| `delete:roles` | Remove roles in the Access Management page. |
| `read:management_keys` | View Cloud Management Keys in the Access Management page. |
| `write:management_keys` | Create and manage Cloud Management Keys. |
| `delete:management_keys` | Remove Cloud Management Keys in the Access Management page. |
| `write:invites` | Invite new users to an account and revoke invitations. |
| `read:invites` | View pending invites in an account. |
| `delete:invites` | Remove an invitation. |
| `read:users` | View user details in the profile page.<br>\- Also applicable in User Management and Role details (User tab). |
| `delete:users` | Remove users from an account.<br>\- Applicable in User Management and Role details (User tab). |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#cluster)**Cluster**

Permissions for API Keys, backups, clusters, and backup schedules.

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#api-keys)**API Keys**

| Permission | Description |
| --- | --- |
| `read:api_keys` | View Database API Keys for managed clusters. |
| `write:api_keys` | Create new Database API Keys. |
| `delete:api_keys` | Remove Database API Keys. |

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#backups)**Backups**

| Permission | Description |
| --- | --- |
| `read:backups` | View backups in the **Backups page** and **Cluster details > Backups tab**. |
| `write:backups` | Create backups from the **Backups page** and **Cluster details > Backups tab**. |
| `delete:backups` | Remove backups from the **Backups page** and **Cluster details > Backups tab**. |

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#clusters)**Clusters**

| Permission | Description |
| --- | --- |
| `read:clusters` | View cluster details. |
| `write:clusters` | Modify cluster settings in the Cluster details page. |
| `delete:clusters` | Delete a cluster from the **Danger Zone** in the Clusters page. |

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#backup-schedules)**Backup Schedules**

| Permission | Description |
| --- | --- |
| `read:backup_schedules` | View backup schedules in the **Backups page** and **Cluster details > Backups tab**. |
| `write:backup_schedules` | Create backup schedules from the **Backups page** and **Cluster details > Backups tab**. |
| `delete:backup_schedules` | Remove backup schedules from the **Backups page** and **Cluster details > Backups tab**. |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#hybrid-cloud)**Hybrid Cloud**

Permissions for hybrid cloud environments.

| Permission | Description |
| --- | --- |
| `read:hybrid_cloud_environments` | View hybrid cloud details. |
| `write:hybrid_cloud_environments` | Modify hybrid cloud settings. |
| `delete:hybrid_cloud_environments` | Remove a hybrid cloud cluster. |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#payment--billing)**Payment & Billing**

Permissions for payment methods and billing information.

| Permission | Description |
| --- | --- |
| `read:payment_information` | View payment methods and billing details. |
| `write:payment_information` | Modify or remove payment methods and billing details. |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#account-management)**Account Management**

Permissions for managing user accounts.

| Permission | Description |
| --- | --- |
| `read:account` | View account details that the user is a part of. |
| `write:account` | Modify account details such as:<br>\- Editing the account name<br>\- Setting an account as default<br>\- Leaving an account<br>**(Only available to Owners)** |
| `delete:account` | Remove an account from:<br>\- The **Profile page** (list of user accounts).<br>\- The **active account** (if the user is an owner/admin). |

* * *

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/permission-reference/\#profile)**Profile**

Permissions for accessing personal profile information.

| Permission | Description |
| --- | --- |
| `read:profile` | View the user’s own profile information.<br>**(Assigned to all users by default)** |

* * *

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/permission-reference.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/permission-reference.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574463814&cv=11&fst=1748574463814&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Fpermission-reference%2F&hn=www.googleadservices.com&frm=0&tiba=Permission%20Reference%20-%20Qdrant&npa=0&pscdl=noapi&auid=1574372192.1748574464&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574463785&cv=11&fst=1748574463785&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Fpermission-reference%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Permission%20Reference%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1574372192.1748574464&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=834d0e4f-46e1-46d3-8da7-e569b99949b0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=50f20572-7cf2-4292-86af-4137a5f8e7e2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Fpermission-reference%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=834d0e4f-46e1-46d3-8da7-e569b99949b0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=50f20572-7cf2-4292-86af-4137a5f8e7e2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Fpermission-reference%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574465110&cv=11&fst=1748574465110&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Fpermission-reference%2F&hn=www.googleadservices.com&frm=0&tiba=Permission%20Reference%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1574372192.1748574464&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)