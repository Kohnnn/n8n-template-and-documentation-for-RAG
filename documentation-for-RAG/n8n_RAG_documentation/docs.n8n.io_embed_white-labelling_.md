---
url: "https://docs.n8n.io/embed/white-labelling/"
title: "White labelling | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/embed/white-labelling/#white-labelling)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/embed/white-labelling.md "Edit this page")

# White labelling [\#](https://docs.n8n.io/embed/white-labelling/\#white-labelling "Permanent link")

Feature availability

Embed requires an embed license. For more information about when to use Embed, as well as costs and licensing processes, refer to [Embed](https://n8n.io/embed/) on the n8n website.

White labelling n8n means customizing the frontend styling and assets to match your brand identity. The process involves changing two packages in n8n's source code [github.com/n8n-io/n8n](https://github.com/n8n-io/n8n):

- [packages/design-system](https://github.com/n8n-io/n8n/tree/master/packages/design-system): n8n's [storybook](https://storybook.js.org/) design system with CSS styles and Vue.js components
- [packages/editor-ui](https://github.com/n8n-io/n8n/tree/master/packages/editor-ui): n8n's [Vue.js](https://vuejs.org/) frontend build with [Vite.js](https://vitejs.dev/)

## Prerequisites [\#](https://docs.n8n.io/embed/white-labelling/\#prerequisites "Permanent link")

You need the following installed on your development machine:

- [git](https://git-scm.com/downloads)
- Node.js and npm. Minimum version Node 18.17.0. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).

Create a fork of [n8n's repository](https://github.com/n8n-io/n8n) and clone your new repository.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>git clone https://github.com/<your-organization>/n8n.git n8n<br>cd n8n<br>``` |

Install all dependencies, build and start n8n.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>npm install<br>npm run build<br>npm run start<br>``` |

Whenever you make changes you need to rebuild and restart n8n. While developing you can use `npm run dev` to automatically rebuild and restart n8n anytime you make code changes.

## Theme colors [\#](https://docs.n8n.io/embed/white-labelling/\#theme-colors "Permanent link")

To customize theme colors open [packages/design-system](https://github.com/n8n-io/n8n/tree/master/packages/design-system) and start with:

- [packages/design-system/src/css/\_tokens.scss](https://github.com/n8n-io/n8n/blob/master/packages/design-system/src/css/_tokens.scss)
- [packages/design-system/src/css/\_tokens.dark.scss](https://github.com/n8n-io/n8n/blob/master/packages/design-system/src/css/_tokens.dark.scss)

At the top of `_tokens.scss` you will find `--color-primary` variables as HSL colors:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>@mixin theme {<br>	--color-primary-h: 6.9;<br>	--color-primary-s: 100%;<br>	--color-primary-l: 67.6%;<br>``` |

In the following example the primary color changes to #0099ff. To convert to HSL you can use a [color converter tool](https://www.w3schools.com/colors/colors_converter.asp).

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>@mixin theme {<br>	--color-primary-h: 204;<br>	--color-primary-s: 100%;<br>	--color-primary-l: 50%;<br>``` |

[![Example Theme Color Customization](https://docs.n8n.io/_images/embed/white-label/color-transition.gif)](https://docs.n8n.io/_images/embed/white-label/color-transition.gif)

## Theme logos [\#](https://docs.n8n.io/embed/white-labelling/\#theme-logos "Permanent link")

To change the editor’s logo assets look into [packages/editor-ui/public](https://github.com/n8n-io/n8n/tree/master/packages/editor-ui/public) and replace:

- favicon-16x16.png
- favicon-32x32.png
- favicon.ico
- n8n-logo.svg
- n8n-logo-collapsed.svg
- n8n-logo-expanded.svg

Replace these logo assets. n8n uses them in Vue.js components, including:

- [MainSidebar.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/MainSidebar.vue): top/left logo in the main sidebar.
- [Logo.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/Logo.vue): reused in other components.

In the following example replace `n8n-logo-collapsed.svg` and `n8n-logo-expanded.svg` to update the main sidebar's logo assets.

[![Example Logo Main Sidebar](https://docs.n8n.io/_images/embed/white-label/logo-main-sidebar.png)](https://docs.n8n.io/_images/embed/white-label/logo-main-sidebar.png)

If your logo assets require different sizing or placement you can customize SCSS styles at the bottom of [MainSidebar.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/MainSidebar.vue).

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>``` | ```<br>.logoItem {<br>	display: flex;<br>	justify-content: space-between;<br>	height: $header-height;<br>	line-height: $header-height;<br>	margin: 0 !important;<br>	border-radius: 0 !important;<br>	border-bottom: var(--border-width-base) var(--border-style-base) var(--color-background-xlight);<br>	cursor: default;<br>	&:hover, &:global(.is-active):hover {<br>		background-color: initial !important;<br>	}<br>	* { vertical-align: middle; }<br>	.icon {<br>		height: 18px;<br>		position: relative;<br>		left: 6px;<br>	}<br>}<br>``` |

## Text localization [\#](https://docs.n8n.io/embed/white-labelling/\#text-localization "Permanent link")

To change all text occurrences like `n8n` or `n8n.io` to your brand identity you can customize n8n's English internationalization file: [packages/editor-ui/src/plugins/i18n/locales/en.json](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/plugins/i18n/locales/en.json).

n8n uses the [Vue I18n](https://kazupon.github.io/vue-i18n/) internationalization plugin for Vue.js to translate the majority of UI texts. To search and replace text occurrences inside `en.json` you can use [Linked locale messages](https://kazupon.github.io/vue-i18n/guide/messages.html#linked-locale-messages).

In the following example add the `_brand.name` translation key to white label n8n's [AboutModal.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/AboutModal.vue).

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br>{<br>	"_brand.name": "My Brand",<br>	//replace n8n with link to _brand.name<br>	"about.aboutN8n": "About @:_brand.name",<br>	"about.n8nVersion": "@:_brand.name Version",<br>}<br>``` |

[![Example About Modal Localization](https://docs.n8n.io/_images/embed/white-label/about-modal.png)](https://docs.n8n.io/_images/embed/white-label/about-modal.png)

### Window title [\#](https://docs.n8n.io/embed/white-labelling/\#window-title "Permanent link")

To change n8n's window title to your brand name, edit the following:

- [packages/editor-ui/index.html](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/index.html)
- [packages/editor-ui/src/components/mixins/titleChange.ts](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/mixins/titleChange.ts)

The following example replaces all occurrences of `n8n` and `n8n.io` with `My Brand` in `index.html` and `titleChange.ts`.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br><!DOCTYPE html><br><html lang="en"><br><head><br>	<!-- Replace html title attribute --><br>	<title>My Brand - Workflow Automation</title><br></head><br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>$titleSet(workflow: string, status: WorkflowTitleStatus) {<br>	// replace n8n prefix<br>	window.document.title = `My Brand - ${icon} ${workflow}`;<br>},<br>$titleReset() {<br>	// replace n8n prefix<br>	document.title = `My Brand - Workflow Automation`;<br>},<br>``` |

[![Example Window Title Localization](https://docs.n8n.io/_images/embed/white-label/window-title.png)](https://docs.n8n.io/_images/embed/white-label/window-title.png)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top