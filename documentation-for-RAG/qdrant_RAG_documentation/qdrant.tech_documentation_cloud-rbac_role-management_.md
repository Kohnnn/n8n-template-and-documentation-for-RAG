---
url: "https://qdrant.tech/documentation/cloud-rbac/role-management/"
title: "Role Management - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud rbac](https://qdrant.tech/documentation/cloud-rbac/)
- Role Management

# [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#role-management) Role Management

> 💡 You can access this in **Access Management > User & Role Management** _if available see [this page for details](https://qdrant.tech/documentation/cloud-rbac/)._

A **Role** contains a set of **permissions** that define the ability to perform or control specific actions in Qdrant Cloud. Permissions are accessible through the Permissions tab in the Role Details page and offer fine-grained access control, logically grouped for easy identification.

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#built-in-roles) Built-In Roles

Qdrant Cloud includes some built-in roles for common use-cases. The permissions for these built-in roles cannot be changed.

There are three types:

- The **Base Role** is assigned to all users, and provides the minimum privileges required to access Qdrant Cloud.
- The **Admin Role**  has all available permissions, except for account write permissions.
- The **Owner Role** has all available permissions assigned, including account write permissions. There can only be one Owner per account currently.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/built-in-roles.png)

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#custom-roles) Custom Roles

An authorized user can create their own custom roles with specific sets of permissions, giving them more control over who has what access to which resource.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/custom-roles.png)

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#creating-a-custom-role) Creating a Custom Role

To create a new custom role, click on the **Add** button at the top-right corner of the **Custom Roles** list.

- **Role Name**: Must be unique across roles.
- **Role Description**: Brief description of the role’s purpose.

Once created, the new role will appear under the **Custom Roles** section in the navigation.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/create-custom-role.png)

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#editing-a-custom-role) Editing a Custom Role

To update a specific role’s permissions, select it from the list and click on the **Permissions** tab. Here, you’ll find logically grouped options that are easy to identify and edit as needed. Once you’ve made your changes, save them to apply the updated permissions to the role.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/update-permission.png)

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#renaming-deleting-and-duplicating-a-custom-role) Renaming, Deleting and Duplicating a Custom Role

Each custom role can be renamed, duplicated or deleted via the action buttons located to the right of the role title bar.

- **Rename**: Opens a dialog allowing users to update both the role name and description.
- **Delete**: Triggers a confirmation prompt to confirm the deletion. Once confirmed, this action is irreversible. Any users assigned to the deleted role will automatically be unassigned from it.
- **Duplicate:** Opens a dialog asking for a confirmation and also allowing users to view the list of permissions that will be assigned to the duplicated role

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/role-actions.png)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/role-management.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/role-management.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574366152&cv=11&fst=1748574366152&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Frole-management%2F&hn=www.googleadservices.com&frm=0&tiba=Role%20Management%20-%20Qdrant&npa=0&pscdl=noapi&auid=1085708009.1748574366&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574366119&cv=11&fst=1748574366119&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Frole-management%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Role%20Management%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1085708009.1748574366&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=650e0b66-7461-4f21-9b30-36868f2851f4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5ff688dd-cf82-4429-b043-cca7fbec643e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Frole-management%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=650e0b66-7461-4f21-9b30-36868f2851f4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5ff688dd-cf82-4429-b043-cca7fbec643e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud-rbac%2Frole-management%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)