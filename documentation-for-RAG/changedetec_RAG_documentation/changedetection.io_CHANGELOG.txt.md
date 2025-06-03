---
url: "https://changedetection.io/CHANGELOG.txt"
title: undefined
---

```
    _                          _     _          _   _            _
 __| |_  __ _ _ _  __ _ ___ __| |___| |_ ___ __| |_(_)___ _ _   (_)___
/ _| ' \/ _` | ' \/ _` / -_) _` / -_)  _/ -_) _|  _| / _ \ ' \ _| / _ \
\__|_||_\__,_|_||_\__, \___\__,_\___|\__\___\__|\__|_\___/_||_(_)_\___/
                  |___/

HEAD / 2025-05-28 14:11:11 +0200:
 - Code - Fix dep warning (#3221)
 - Realtime UI - Reducing log output
 - UI - Reword restock detector plugin description
 - UI - Remove incorrect error text

0.49.18 / 2025-05-26 20:35:46 +0200:
 - 0.49.18
 - Realtime UI updates via WebSocket (#3183)
 - Update to Apprise 1.9.3 - BlueSky, Resend support (#3216)
 - UI - Update 'Browser Steps' UI text
 - Code - Remove unused f-strings (#3209)
 - Use logger.debug for playwright console logs (#3201)

0.49.17 / 2025-05-12 10:47:27 +0200:
 - 0.49.17
 - Resolve warnings of bs4 library (#3187)
 - Revert memory strategy change for html_to_text (Was hanging under high concurrency setups)

0.49.16 / 2025-05-03 16:43:04 +0200:
 - 0.49.16
 - Fixes to ensure proxy errors are handled correctly (#3168)
 - UI - Custom headers should have validation (#3172)
 - Update selenium library (#3170)
 - Restock detection - adding new string
 - Conditions - Levenshtein text similarity plugin - adding test, fixing import, fixing check for watches with 1 snapshot history (#3161)
 - Restock detection - Use cleaner logic for limiting elements to scan, refactor, improve tests (#3158)
 - pyppeteer fast puppeteer fetch - be sure viewport is set to --window-size if --window-size is set (#3157)
 - Improved global ignore test (#3140)
 - Update docker-compose.yml (#3149)
 - Small fix for xpath element scraper (#3145)
 - Plugins for conditions (and include Similarity / Levenshtein, wordcount conditions) Re #3108
 - Browser Steps - <Select> by Option Text - #1224, #1228 (#3138)
 - Browser Steps - error reporting and session shutdown improvements (#3137)

0.49.15 / 2025-04-18 14:57:28 +0200:
 - 0.49.15
 - Visual Selector & Browser Steps - Always recheck if the data/screenshot is ready under "Visual Selector" tab after using Browser Steps (#3130)
 - App logs - Send TRACE and INFO logs to stdout (#3051)
 - Development: introduce Ruff as linter/formatter (#3039)
 - Updating restock texts (#3124)
 - Only add screenshot warning if capture was greater than trim size (#3123)

0.49.14 / 2025-04-16 23:23:18 +0200:
 - 0.49.14
 - Small fix for multiprocessing start on Mac OS (#3121 #3115)
 - docs: Update reference URL (#3119)
 - UI - Fix to edit and groups template
 - Updating API documentation
 - Undo forced selenium headless mode, small refactor (#3112)
 - Playwright + Puppeteer fix for when page is taller than viewport but less than screenshot step_size (#3113)
 - Memory management -  Run HTML to text in sub process, a few more cleanups  to playwright (#3110)
 - UI Edit/Stats - Add levenshtein distance info, explains how "different" the last two snapshot are (#3109)

0.49.13 / 2025-04-11 13:46:58 +0200:
 - 0.49.13
 - API - Added notifications API endpoints (#3103)
 - Fetcher - Use bigger screenshot chunks to speed up page screenshot (#3107)
 - App memory - Apprise import only when needed - saves ~50Mb RAM if you dont have any notifications enabled (#3106)
 - Fetching - Small improvement memory handling in detecting price information (saves ~10Mb)
 - Refactor image saving with forked process to reduce memory usage, improvements to xpath scraper handling (#3099)
 - Update other methods to use updated screenshot handler (#3098)
 - Memory fixes for large playwright screenshots (#3092)
 - Filters - Support multi line regex  (#2889)
 - UI - Add UI options tab and setting to disable opening diff in a new tab (#3071)
 - README.md update - Including blurb about 'conditions'
 - Requests fetcher - Remove old screenshot when watch was in a different fetcher type (#3097)
 - Make chrome browser headless when checking the site with selenium (#3095)
 - UI - Field name update - Keyword triggers - Trigger/wait for text (#3088)
 - UI - "Recheck all" should also queue most overdue first  (same like automatic scheduler) (#3087)
 - Groups - Including "Extract text", "Text to ignore", "Trigger text" and "Text that should not be present" filters

0.49.12 / 2025-04-04 09:30:24 +0200:
 - 0.49.12

0.49.11 / 2025-04-03 18:54:20 +0200:
 - 0.49.11

0.49.10 / 2025-04-03 11:17:14 +0200:
 - 0.49.10
 - Update README.md
 - UI - "Conditions" section, making the Conditions setup table work better on mobile/responsive
 - Adding a GC memory cleanup (releases cached libxml memory and others) (#3079)
 - Python 3.11 container base (#3077)
 - Use lowercase static asset filenames
 - Restock detection - Add Indonesian phrases for out-of-stock detection (#3075)
 - Regession - Shared history/diff page with anonymous access turned on should allow screenshot access (#3076)
 - Update edit.html - linking to tutorial
 - Code - Tidy up lint errors (#3074)
 - UI - Update edit.html- xPath support text for 1 & 2
 - Text/fetching - Small fix for when last fetched was zero bytes and special options (removals/additions/changes) was set (#3065)
 - Notifications backend - Refactor + tests for Apprise custom integration (#3057)
 - UI - Watch edit - "Clone" Should be "Clone & Edit" without watch history, redirect to the new edit page (#3063 #2782)
 - UI - Conditions - Offer some information about what the filter/condition/trigger saw (#3062)
 - UI - Tidy up support links
 - UI - Set a graph % of ETA time completed of checking the watch (#3060)

0.49.9 / 2025-03-26 16:30:08 +0100:
 - 0.49.9
 - RSS Fixes and improvements - Ability to set "RSS Color HTML Format" in Settings, detect and filter content with bad content that could break RSS (#3055)

0.49.8 / 2025-03-25 22:59:56 +0100:
 - 0.49.8
 - Server - Path blueprint fixes and moving code blueprint to fix RSS forward slash on url (#3054)
 - API - Adding "Search" API (#3052)
 - Fetching - Upgrading to pyppeteer-ng 2.0.0rc8 (more modern pyee requirements)

0.49.7 / 2025-03-23 16:50:21 +0100:
 - 0.49.7
 - Adding Tags/Groups API (#3049)

0.49.6 / 2025-03-23 02:01:32 +0100:
 - 0.49.6
 - API Access should still work even when UI Password is enabled (#3046) #3045

0.49.5 / 2025-03-22 22:51:33 +0100:
 - 0.49.5
 - Template tidyup & UI Fixes (#3044)
 - Watch history -  Ensure atomic/safe history data disk writes (#3042 #3041)
 - Testing - Replace Linux only 'resource' library with cross-platform 'psutil' library (#3037)
 - Refactor code layout, add extra tests
 - New major functionality CONDITIONS - Compare values, check numbers within range, etc

0.49.4 / 2025-03-13 12:06:50 +0100:
 - 0.49.4
 - Datastore - Always use utf-8 encoding for error text output storage
 -  Restock detection - Adding french keywords for out of stock items
 - Browser Steps - Should use the Watch URL/link after any Jinja2 type templates are applied
 - BrowserSteps - Speed up scraping, refactor screenshot handling for very long pages (#2999)
 - Browser Steps - Added new "Make all child elements visible" action
 - Browser Steps - Added new "Remove elements" action
 - UI - Browser Steps - "Click X,Y" should focus on the input field also
 - UI - Browser Steps - Improving Browser Steps usability on mobile

0.49.3 / 2025-02-22 10:24:44 +0100:
 - 0.49.3
 - UI - Reverting JS change to tabs (the better fix was the W3C HTML validation)

0.49.2 / 2025-02-19 16:01:01 +0100:
 - 0.49.2
 - UI - Make the setup and error messages for Visual Selector and Browser Steps a lot more meaningful (#2977)
 - Update docker-compose.yml
 - UI - More W3C HTML validation fixes
 - UI - More W3C validation fixes (#2973)
 - UI - Tweaks for HTML validation
 - Filter - "Unique lines" could possibly crash if history was empty or cleared on the disk
 - UI - Sometimes the DOM wasnt ready when tab selection triggered via CSS, which displayed empty tabs on some browsers
 - Removing deprecated docker-compose.yml version attribute (#2967)
 - Update settings.html
 - Browser Steps - Increasing timeout for actions and unifying timeout values
 - Browser Steps - Fixing 'Uncheck checkbox' #2958
 - UI - "Browser Steps" tab should be always available with helpful info (evenwhen playwright is not configured) (#2955)
 - Adding `browser_steps` JSON Schema rule for API updates (#2957)
 - UI - Fix mute/unmute alt/title label alt/title text in watch overview (#2951)

0.49.1 / 2025-02-08 10:14:19 +0100:
 - 0.49.1
 - Update stock-not-in-stock.js - Italian (#2948)
 - Re #2945 - Handle/Strip UTF-8 ByteOrderMark in JSON strings correctly (fixes `"Exception: No parsable JSON found in this document" ` error) (#2947)
 - Add major and minor tags for Docker release workflow (#2938)
 - Adding jinja2/browsersteps test (#2915)
 - Header handling - Fix header parsing to split on the first colon only (headers where the value contained :// type may have been broken) (#2929)

0.49.0 / 2025-01-21 13:40:01 +0100:
 - 0.49.00
 - Update README.md
 - Build/Libraries - Pin `referencing` library which breaks due to out-dated flask_expects_json, remove pip upgrade in test(#2912)
 - Notifications - Custom POST:// GET:// etc endpoints - returning 204 and other 20x responses are OK (don't show an error was detected)(#2897)

0.48.06 / 2025-01-09 23:02:29 +0100:
 - 0.48.06
 - Restock -  Add test for new lower/higher price notification Re #2715 (#2892)
 - Update integration test for "linuxserver" test build (#2891)
 - Notifications - Update Apprise to 1.9.2 - Fixes custom posts:// gets:// etc URL's being double-encoded, fixes chantify:// notifications (#2868) (#2875)  (#2870)
 - Custom posts:// get:// notifications etc - Be sure our custom extensions are imported (#2890)
 - "Send test notification" button - Easier to understand test send results, Improved error handling, code refactor (#2888)
 - Improve `last_checked` vs `last_changed` time information precision (#2883)
 - Update Apprise to 1.9.1 (#2876)
 - Builder/Docker - Remove PUID and PGID ( they were not used ) (#2852)
 - UI - Fix diff not starting from last viewed snapshot (#2744) (#2856)

0.48.05 / 2024-12-27 11:24:56 +0100:
 - 0.48.05
 - Fixing test for CVE-2024-56509 (#2864)
 - CVE-2024-56509 - Stricter file protocol checking pre-check ( Improper Input Validation Leading to LFR/Path Traversal when fetching file:.. )

0.48.04 / 2024-12-16 21:50:53 +0100:
 - 0.48.04
 - Windows was sometimes missing timezone data (#2845 #2826)

0.48.03 / 2024-12-16 16:14:03 +0100:
 - 0.48.03
 - 0.48.02
 - 0.48.02
 - Notifications - "Send test" was not always following "System default notification format" (#2844)
 - Notifications - "Send test" was not always following "System default notification format"

0.48.02 / 2024-12-16 16:07:11 +0100:
 - 0.48.02
 - Notifications - "Send test" was not always following "System default notification format"
 - Notifications - Default notification format (for new installs) now "HTML color" (#2843)
 - Notification - `HTML Color` format notification colors should be same as UI, `{{diff_full}}` token should also get HTML colors ( #2842 #2554 )
 - Notifcations - Adding "HTML Color" notification format option (#2837)
 - UI - Make 'tag' sticky - redirect to current tag on edit or add watch (#2824 #2785)
 - Notifications - Support for commented out notification URLs (#2825 #2769)
 - Docs - Adding information to README.md about the new scheduler

0.48.01 / 2024-12-03 18:44:20 +0100:
 - 0.48.01
 - UI - Fixing scheduler options

0.48.00 / 2024-12-03 14:26:01 +0100:
 - 0.48.00
 - Fix HIDE_REFERER env option for hiding changedetection.io from referer headers (#2787)
 - New functionality - Time (weekday + time) scheduler / duration (#2802)
 - Add Turkish phrases for out-of-stock detection (#2809)
 - UI - Always use UTC timezone for storing data, show local timezone (#2799)
 - Update stock-not-in-stock.js
 - Python 3.13 compatibility (#2791)
 - Code - Update .gitignore and .dockerignore (#2797)
 - VisualSelector - Use 'deflate' for storing elements.json, 90% file size reduction (#2794)
 - UI - Show local timezone info in settings (for future functionality) #2793
 - Notification - Locking paho-mqtt:// version fix
 - Update COMMERCIAL_LICENCE.md
 - Ability to disable version check (set `DISABLE_VERSION_CHECK=true`) Re #2773 (#2775)
 - Minor improvement for queue management
 - Update bug_report.md

0.47.06 / 2024-11-07 20:10:02 +0100:
 - Security - Fix test
 - Security check - improve test
 - 0.47.06
 - CVE-2024-51998 - file:/ path traversal access should not be allowed to access a file without ALLOW_FILE_URI set
 - Update docker-compose.yml (#2767)
 - Price tracker - fix for sites that supply an empty additional price (#2758)
 - Testing - Pinning werkzeug (#2757)

0.47.05 / 2024-10-31 22:51:03 +0100:
 - 0.47.05
 - CVE-2024-51483 - Fix for limiting access to file:// via source:file:///tmp/file.txt when using webdriver/playwright
 - Backups - Hide incomplete/running backups from being downloaded
 - Backups - Backups now operate in the background, provide a nice UI to access/download previous backups (#2755)
 - Filters - Process all CSS and XPath 'subtract' selectors in a single pass to prevent index shifting and reference loss during DOM manipulation. (#2754)

0.47.04 / 2024-10-29 08:25:05 +0100:
 - 0.47.04
 - Do not recheck 'paused' watches on edit/save (Re #2747 #2750)
 - Notification post:// get:// etc - Fixing URL encoding of headers so that '+' in URL is correctly parsed as ' ' (and other url-encodings) (#2745)
 - #2502 - Add jinja2 template handling to request body and headers (#2740)
 - Restock detection - Add additional out-of-stock detection for PT language (#2738)
 - "Send test notification" in "Restock" mode was not working correclty when restock tokens "{{restock.price}}" were in the notification body (#2737)
 - #2727 Notifications - Fix "send test notification" on empty list, includes test (#2731)
 - UI - Fix mobile styling inconsistencies and resolve diff page overflow issue (#2716)
 - Filters - "Block change detection when text exists" should not trigger a change when the original text returns
 - UI - More work on tab buttons hiding behind menu/header  :-)

0.47.03 / 2024-10-11 17:33:00 +0200:
 - 0.47.03
 - Remove same checksum skip check - saved a little CPU but added a lot of complexity (#2700)
 - UI - Fix scroll offset / tab buttons hiding behind menu/header
 - 0.47.02
 - UI - Fix scroll offset / tab buttons hiding behind menu/header

0.47.02 / 2024-10-11 15:35:36 +0200:
 - 0.47.02
 - UI - Fix scroll offset / tab buttons hiding behind menu/header

0.47.01 / 2024-10-11 15:02:17 +0200:
 - 0.47.01
 - Adding missing `apprise_plugin` for pypi/pip based installs

0.47.00 / 2024-10-11 13:04:56 +0200:
 - 0.47.00
 - Restock multiprice improvements (#2698)
 - Test - Simple test for live preview
 - Adding test for proxy checker/scanner (#2697)
 - Fixing proxy checker (#2696)
 - UTF-8 handling fixes, Improvements to whitespace filtering (#2691)
 - Testing - Tidyup (#2693)
 - Filters & Text - Preview refactor/improvements (#2689)
 - Build - Add image source label to Dockerfile (Better Renovate and others support) (#2690)
 - Custom JSON/POST Notifications - Log when it could not apply the application/json content-type header
 - UI - Filters live preview - improvements to layout
 - Restock - Use the scraped 'Not in stock' product status over the metadata version (many website lie in the metadata) (#2684)
 - UI - Better 40x error message (#2685)
 - Visual Selector - Including <button> (#2686)
 - Stock/not-in-stock scraper - slight reliability improvement (#2687)
 - Code - Small improvements in logging
 - UI - CSS - Fix on sorting row wrapping issue (#2680)
 - UI - Live filters preview - Better handling of watch preferences
 - UI - "Diff" button in overview list is now "History" button (#2679)
 - UI - Improve error handling when a module is missing when editing a URL/link (#2678)
 - UI - Live filters preview - Make it sticky in the viewport so its easier to build nice filters
 - UI - Live filters preview - dark mode improvements
 - UI - Improvements to text preview on mobile
 - UI - Improvements to live preview of Filters text
 - UI - Misc fixes for mobile styling (#2669)
 - Update docker-compose.yml - Adding example for enabling change detection on local files
 - UI - Live preview - misc improvements (Adding test, fixes to filters) (#2663)
 - UI - "Filters & Triggers" - Live preview of text filters (Preview the output of the filters section in realtime) (#2612)
 - Reversing subprocess execution - saved a little memory but used a LOT more CPU (#2659)
 - [test] Use local data instead of reaching out to changedetection when testing (#2660)
 - Restock monitor - Only try to process restock information (like scraping for "out of stock" keywords) if the page was actually rendered correctly. (#2645)
 - Text filters - Adding filters "Trim whitespace" and "Remove duplicate lines"
 - Browser Steps - UI - Use a better flexbox layout
 - Filters - Add support for also removing HTML elements using XPath selectors (#2632)
 - Update AppRise notification library to 1.9.0 (#2624)
 - browser_steps: add "click element containing text if exists" (#2629)
 - Testing - Fixing Restock test #2641
 - Testing - Fix false filter missing check alerts
 - Restock/Price detection - Fix duplicated prices with different data type on single page product #2636 (#2638)
 - Memory management improvements - LXML and other libraries can leak allocation, wrap in a sub-process (#2626)
 - Small memory allocation fixes (#2625)
 - Testing - locale fix for test (#2623)
 - Testing/Code - Improving test reliability (#2617)
 - UI - Hiding noisy info under 'show advanced help' button (#2609)

0.46.04 / 2024-09-04 13:55:18 +0200:
 - 0.46.04
 - Fixing restock monitor tests and tweaking docker default config example,
 - Container name should be 'sockpuppetbrowser' because its not just playwright that uses it
 - Restock/Price detection - Better catching of errors when parsing metadata documents for restock/price check (#2602)
 - Restock - updating texts and text offsets
 - Build - Unpin jsonschema for faster builds (#2583)
 - Price detection/scraping - Adding extra element training data (#2582)

0.46.03 / 2024-08-19 17:22:13 +0200:
 - 0.46.03
 - Watch 'Download last snapshot' link/button should give last, not first snapshot (#2576)
 - Price and restock scraping - small price fix scraper (#2575)
 - Browser Steps UI - Interactive UI wasn't sending headers but was when the check ran  (#2551)
 - Set encoding type for scraper script reader (#2574 #2568)
 - Handle zero-byte/empty content responses with "`[ ] Empty pages are a change`" option, the same as when the HTML doesnt render any useful text (#2530)

0.46.02 / 2024-07-27 20:28:04 +0200:
 - 0.46.02
 - Adding test for #1995 UTF-8 encoding in POST request body and post:// notifications (#2525)
 - Updating Apprise notification library , Splunk/VictorOps, Africas Talking, Microsoft Power Automate / Workflows, SociÃ©tÃ© FranÃ§aise du RadiotÃ©lÃ©phone (SFR) Support (#2524)
 - Encode POST style requests and notifications as UTF-8 if it has no encoding/basic string (#2523)
 - VisualSelector+BrowserSteps - When scraping elements, check for null results (#2517)
 - Use #!/usr/bin/env to support virtualenv (#2518)
 - Update README.md
 - UI - Adding "Download latest HTML snapshot" from Edit Watch > Stats page for easier debugging (#2513)

0.46.01 / 2024-07-19 13:53:00 +0200:
 - 0.46.01
 - UI - Fixing up 'test notification' bug from main settings and tag settings pages #2510 (#2511)

0.46.00 / 2024-07-18 14:13:06 +0200:
 - 0.46.00
 - Restock/Price detection - Improving text information snapshot value
 - Restock - Tweaking storage of "original price"
 - Fixing file:// file pickup  - for change detection of local files (#2505)
 - Adding Apple M1 Pro type arm64/v8 support docker image (#2507)
 - Dropping older ARM v6 support due to dependencies not having support (#2506)
 - Ability to use restock and price amounts in notifications as tokens (for example {{restock.price}} ) (#2503)
 - Restock & Price detection - Ability to set up a tag/group that applies to all watches with price + restock limits
 - Fixing problematic tag assigning via UI which caused watches to not accept new settings
 - Fixing first history/preview save issue (First version after an error, on the first check, wasnt available) (#2494)
 - UI - Restock/price following text cleanups
 - UI - Extract <title> as title should work on all processors (#2490)
 - Restock & Price monitor -  Huge refactor, set upper and lower price alert limits, set % change, follow the prices and restock amounts directly in the watch-overview list
 - Product checks - Just a basic string check is far more efficient for suggestion price/restock check plugin (#2488)
 - Update COMMERCIAL_LICENCE.md
 - Update README.md - Adding link to COMMERCIAL_LICENCE.md for those interested in reselling the software
 - Adding COMMERCIAL_LICENCE.md
 - Testing - Adding simple memory usage test (#2483)
 - Bugfix - Watches with BrowserSteps should recreate the data-dir if it was missing (in the case that you deleted/migrated) (#2484)

0.45.26 / 2024-07-11 13:52:13 +0200:
 - 0.45.26
 - Code - Fixing deprecation warning (#2477)
 - UI - Visual Selector should still update when elements were not found (#2476)
 - Code - Update/modernise diff.py (#2471)
 - UI - Visual Selector - Multiple selections (refactor) (#2475)
 - UI - Visual Selector now supports Shift+Click for multiple selections!
 - UI - Visual Selector - Show/visualise all/any matching filter elements from all filters in "CSS/JSONPath/JQ/XPath Filters" include filters (#2440)
 - UI - Visual Selector graphics should be centred
 -  Snapshot count from history was not updated in watch after using [clear history] (#2459)
 - Fixing 'tags'' field from old installs (0.43.0+) could have wrong data-type causing crash

0.45.25 / 2024-07-03 19:27:23 +0200:
 - 0.45.25
 - UI - Fixing preview/diff "ignore text" highlight button (refactor, didnt work in "preview" mode) (#2455)
 - Restock detection - Updating detection texts
 - UI - Mobile - Hiding empty columns
 - UI - Mobile - Watch overview table - Sort/order buttons were not being shown correctly
 - Update docker-compose.yml - fix indentation re #2447
 - Restock detection - Added extra out-of-stock phrases for DE (#2442)
 - Restock detection - updating texts
 - UI - Fixing double punctuation in 'unpaused' message #2435
 - Build - Bump docker/build-push-action from 5 to 6 in the all group (#2436)
 - Now saving last two HTML snapshots for future reference, refactor, dont write screenshots and xpath to disk when no change detected (saves disk IO) (#2431)
 - Filters - Implement jqraw: filter  (use this to output nicer JSON format when selecting/filtering by JSON) (#2430)
 - Build - fixing build warnings
 - Upgrade to Python 3.11 from 3.10, add faster prebuilt "wheels" for rPi devices, upgrade cryptography security library
 - Prefer pythons built in "importlib" over pkg_resources+setuptools (#2424)
 - Security/dependabot - Bump urllib3 from 1.26.18 to 1.26.19 (#2423)

0.45.24 / 2024-06-17 13:27:11 +0200:
 - 0.45.24
 - Update eventlet ( Fixes SSL error on Python 3.12 ) (#2419)
 - Filter failure/not found notification threshold - Counter should be reset when editing a watch, clear watch errors on 'save' (#2413)
 - Bump dnspython from 2.3.0 to 2.6.1 (#2306)
 - Improve testing for Python 3.10, 3.11 and 3.12
 - UI - Add space around checkbox operation buttons so they work better in mobile #2393
 - RSS - Setting to hide muted watches in RSS feed (default ON) (#2411)
 - Fetching/Requests - Fixing  user agent header overrides per-watch of global settings (#2409)
 - Code - improving unique key fix for history database handler (#2402)
 - UI - 'Mark all viewed' button should not show when all viewed (#2399)
 - Fixing build test - Adding small delay (#2397)
 - Code - Bump eventlet from 0.33.3 to 0.35.2 (#2305)
 - UI - Mobile CSS/layout fix wrapping on empty list text #2393
 - UI - Preview single snapshot - Date and button fixes (#2389)
 - Build - PIL/pillow package not used, probably shouldnt be installed/required (#2382)

0.45.23 / 2024-05-22 00:01:50 +0200:
 - 0.45.23
 - RSS - Only insert feed header if app_rss_token is set (should be only shown in index/overview page) (#2381)
 - Fetcher - Using pyppeteerstealth with puppeteer fetcher (#2203)
 - Fix overflowing text
 - RSS and tags/groups - Fixes use active_tag_uuid, fixes broken RSS link in page html (#2379)
 - Ability to set default User-Agent for either fetching types directly in the UI (#2375)
 - Testing - Fixing JSON test
 - UI - Mobile - quick watch form element fixes
 - UI - CSS - Remove gradient border, it did not add much to the design #2377
 - RSS - Muted watches should not show in RSS feed (#2374 #2304)
 - Notifications -  Fixing truncated notifications when tgram:// or discord:// is used with other notification methods (#2372 #2299)
 - UI - Ability to preview/view single changes by timestamp using keyboard or select box(#1916)
 - Browser Steps - Fixing "goto site" step #2330 #2337 (#2364)
 - Crash on older CPU -  Setting LXML version to any version without the known modern-CPU-only CPU flags (#2365 #2328 )
 - Notifications - Update Apprise notification library to 1.8.0 (#2363 #2324) fixes mailto:// with IP as server endpoint
 - UI - Refactor of the Recheck Time Settings, Added "Use default recheck time" checkbox and refactor/simplify system handling (#2362)
 - UI - Search should scan/search error messages (#2353)
 - UI - 'stats' tab should show what the server-type detected is ( #2348 )
 - Update README.md
 - Notifications - Setting set minimum version for mqtt:// library notifications (#2334 / #2333)

0.45.22 / 2024-05-02 12:09:45 +0200:
 - 0.45.22

0.45.21 / 2024-04-25 22:29:38 +0200:
 - 0.45.21
 - UI - Wrap tag names in solid background to make it easier to read when theres multiple tags
 - UI - Error text on exception should contain the word Exception (#2322)

0.45.20 / 2024-04-18 11:55:46 +0200:
 - 0.45.20
 - Bug fix - further work on  lxml filter extract (#2313 #2312 #2317)

0.45.19 / 2024-04-17 20:01:35 +0200:
 - 0.45.19
 - Bug fix for newer lxml module - module 'lxml.etree' has no attribute '_ElementStringResult' - reimplement _ElementStringResult (#2313 #2312)

0.45.18 / 2024-04-16 18:50:14 +0200:
 - 0.45.18
 - UI - Adding UI notice if watch has group options set (#2311 #2307)
 - dependabot - automatically follow apprise
 - "Send Test Notification" - In "Group" settings form it should not fallback to the system wide notifications when sending a test if nothing is set.
 - "Send Test Notification" - Now provides better feedback and works with the actual values in system settings form
 - Code - Getting ready for newer python versions - packing our own strtobool (#2291)
 - UI - BrowserSteps - Show step screenshot/pic should use absolute URL #2243
 - UI - Remove unique check for URLs entered on the "quick watch add" form ( #2286 #2292 )
 - UI - Improvements to tag/groups page, show number of watches under each group, link group name to list (#2290)
 - "Send Test Notification" button  from watch form edit should respect global settings and tag/group settings ( #2289, #2263 )

0.45.17 / 2024-03-31 16:35:44 +0200:
 - 0.45.17
 - UI - Add helper note
 - UI Text - Adding helper text to VisualSelector to explain what the connection is with the CSS/xPath filters
 - Update contributing documentation for discontinuation of `dev` branch (#2272)
 - Updating pyppeteer-ng (mainly newer pillow release) (#2247)
 - Notifications - Updating apprise version, pinning  mqtt:// to compatible version (#2242)

0.45.16 / 2024-03-08 21:07:08 +0100:
 - 0.45.16
 - Pip build - content fetchers package was missing

0.45.15 / 2024-03-08 19:00:37 +0100:
 - 0.45.15
 - Updating restock detection texts
 - Adding CORS module - Solves Chrome extension API connectivity (#2236)
 - UI - Overview list shortcut button - Ability to reset any previous errors
 - Chrome Extension - Adding link and install information from the API page
 - Chrome Extension - Adding link in README.md to the webstore
 - Chrome Extension - Adding callout to UI
 - Import - Fixed "Include filters" option (fixed typo on select) (#2232)
 - Updating restock detection texts
 - Restock detection - Improving test for restock IN STOCK -> OUT OF STOCK (#2219)
 - Puppeteer - remove debug hook
 - Custom headers fix in Browser Steps and Playwright/Puppeteer fetchers ( #2197 )
 - text_json_diff/fix: Keep an order of filter and remove duplicated filters. 2 (#2178)
 - Fetching - restock detecting and visual selector scraper - Fixes scraping of elements that are not visible
 - BrowserSteps UI - Avoid selecting very large elements that are likely to be the page wrapper
 - Fetching - Puppeteer - Adding more debug/diagnostic information
 - Update stock-not-in-stock.js
 - UI - Sorted alphabetical tag list and list of tags in groups setting (#2205)
 - Code - Remove whitespaces in visual selector elements config
 - Build fix - Pinning package versions and Custom browser endpoints should not have a proxy set (#2204)
 - Update stock-not-in-stock.js
 - Fetching pages - Custom browser endpoints should not have default proxy info added
 - Puppeteer - fixing wait times
 - Puppeteer - more improvements to proxy and authentication
 - Puppeteer - client fixes for proxy and caching (#2181)
 - dependabot - Bump the all group with 1 update (artifact store) (#2180)
 - Puppeteer fetch - fixing exception names
 - Code - Split content fetcher code up (playwright, puppeteer and requests), fix puppeteer direct chrome support (#2169)
 - Alpine linux build - adding JPEG development headers to fix build errors
 - Plawright content fetcher - Fixes for status codes and screenshot info (#2168)
 - Fetching - Prefer to use SockPuppetBrowser (#2163)

0.45.14 / 2024-02-07 12:43:23 +0100:
 - 0.45.14
 - Bug fix -  fix missing default var (#2162/ #2118/ #2122 )
 - Fix - Pinning elementpath xPath filter library to 4.1.5 (#2164)
 - Restock detection - Update stock-not-in-stock.js (NL)
 - New text filter - Sort text alphabetically filter (#2153)
 - Filtering - include_filters in group and watch settings should not duplicate (#2151 #1845)
 - Record notification count and show in [stats] tab (#2150)
 - Restock - Update stock-not-in-stock.js Italian translation (#2149)
 - UI - Show error/warning when trying to compare the same version
 - Fetching - Make an obvious error when using BrowserSteps with the simple text fetcher (#2145)
 - Fix for switching to price-data-follower mode (when page has JSON price data), only needs to be queued once. Re #1565
 - Fetching - Always record `server` software reply headers (will be used in the future) (#2143)
 - Testing - General test workflow improvements (#2144)
 - RSS - Include link to the watched URL in the feed (#2139 #2131 and #327)
 - Notifications - skip empty notification URLs from being processed (#2138)
 - UI - Filters & Triggers - Adding example for keyword matching in a line
 - RSS - Adding performance stats
 - Notification - logging - adding performance information for processing time of notifications #327
 - UI - Adding icon to show which watch has Browser Steps enabled (#2137)
 - Logging - Adding extra debug logging to change detection (#2136)
 - Fetcher -  Improve status_code logging (#2130 #2122)
 - Notifications - Bugfix: Notification format not being set correct (HTML emails being sent as plaintext and other problems) (#2129)
 - Restock tweaks - use a single regex, tidy up height detection (#2125)
 - Notification - Templates - Adding an example of how to use URL encoding with tokens
 - Notification - Templates - Adding an example of how to use |tojson for JSON payloads
 - Build maintenance  - dependabot - Bump the all build helpers (#2121)
 - Enable dependabot for github-actions (#2119)
 - Update docker-compose.yml

0.45.13 / 2024-01-19 10:24:47 +0100:
 - 0.45.13
 - Security update - Adding API token secure check for API endpoint `/api/v1/watch/<uuid>/history` @rozpuszczalny
 - Test - tidy up backup test (#2117)
 - Adding contributors section (#2116)
 - Logging loguru output tweaks (#2112)
 - Support Loguru as a logger (#2036)
 - Update stock-not-in-stock.js texts
 - Test - Adding extra test for HTML output in emails ( #2103 )
 - Update README.md
 - Restock detection - Check all elements for text to get stock status from, only consider elements inside the viewport, only consider elements more than 100px from the top (avoid menu) , trim any text returned (#2040)
 - Notifications - When any in a list of notifications fails, the others should still work (#2106)
 - Browser Steps - Fixing "'Response' object is not subscriptable" where quotes were used in connection URL   - Quote wrapped URL for browserstep url was breaking the connection #1627 #1823 #2099 (#2100)
 - Added OPTIONS HTTP method (#2094)
 - API Docs - Examples should use port 5000 (same as the docker-compose default installation and other documentation)

0.45.12 / 2024-01-05 20:17:14 +0100:
 - 0.45.12
 - 0.45.11
 - Notification fixes - error on mailto:// when no format was specified, fixing default body and title of notifications to respect global settings (#2085)
 - Update README.md
 - Removing heroku support as its no longer free
 - PyPi package build fixes (#2084)
 - Adding PyPi pip package publisher script

0.45.10 / 2024-01-05 14:51:35 +0100:
 - 0.45.10
 - Update README.md - Remove deprecated docker-compose (now docker compose)
 - Browser Steps - General error handling improvements (#2083)
 - Browser Steps - Fix for correct tokens/information in browser step failure notification (#2066)
 - UI - [Send test notification] - Refactor to use all tokens  like a real watch and Notification Body+Title from UI value (#2079)
 - Notifications upgrade - Upgrade to Apprise 1.7.1 - Emojis support, Telegram topics support, Discord support for user and role @ping support.  (#2075)
 - Restock detection - "In stock" should be None/"Not yet checked" by default (#2069)
 - Restock detection - updating texts
 - Fetching - Custom browser on experimental/puppeteer fetcher - Don't switch to custom puppeteer mode if external browser URL is active (#2068)

0.45.9 / 2023-12-20 15:30:58 +0100:
 - 0.45.9
 - Restock detection - Update stock-not-in-stock.js strings (Dutch translations)
 - Testing: Improve application signal handling test coverage (#2052)
 - Update docker-compose.yml
 - Restock detection - Update stock-not-in-stock.js strings (#2032)
 - API - Updating documentation
 - Update README.md
 - API - Ability to add/import bulk list of watches as a line-feed separated list (#2021)
 - Notifications - Fixing support for headers in custom post://, posts:// notifications, ability to include HTTP headers when making custom notifications (#2018)
 - Improve handling of SIGTERM shutdown in containers, remove unnecessary multi-process handler for pip installs, tidy up modules (#2014)
 - UI - Extra Browsers - Adding links and more resources on how to connect a fingerprint/scraping browser

0.45.8.1 / 2023-11-30 20:01:40 +0100:
 - 0.45.8.1
 - PDF Fetcher for change detection - Always use plain requests for PDF because otherwise we cant access the embed PDF in the browser (#2020)
 - UI - Fix - Edit Watch 'Show advanced options' should fire at page load to show you whats possible

0.45.8 / 2023-11-29 10:25:11 +0100:
 - 0.45.8
 - Restock detector - adding more detection strings
 - UI - remove incorrect label
 - UI - "Add new watch" URL at main input box should always grow to match the viewport
 - UI - Tidy-up for advanced settings under watch edit, HTML validation fixes (#2011)
 - UI - 'Request body' section disappears after switching from 'Playwright' to 'System settings default' and back on 'Request' tab - Fixed #1449
 - Browser Steps - Adding validation for "Click X,Y" step
 - API - Make sure the watch "is viewed" attribute is correctly represented in the API output (#2009)
 - Update playwright fetcher library and API calls
 - Testing - Improve PDF text change detection tests (#1992)
 - UI - Clicking the "[Diff]" link should take you to the difference starting at the relative time to when you last viewed the difference page (#1989)
 - Visual Selector - xPath handling misc fixes (#1976)
 - Fix build issue
 - feature: Support XPath2.0 to 3.1 (#1774)
 - New functionanlity - Selectable browser / ability to add extra browser connections (good for using "scraping browsers"/  etc) (#1943)
 - API/UI - Button to regenerate API key (#1975 / #1967)
 - Code refactor for fetchers (#1941)

0.45.7.3 / 2023-11-12 12:05:54 +0100:
 - 0.45.7.3
 - Build - update docker container cache setup

0.45.7.2 / 2023-11-12 00:29:35 +0100:
 - 0.45.7.2
 - UI - Cleanup fonts better display in firefox, request CSS according to version (#1968)
 - Revert "Build - Add piwheels support for ARMv6 and ARMv7 machines (rPi etc) (#1814)" (#1964)

0.45.7.1 / 2023-11-11 20:42:16 +0100:
 - 0.45.7.1
 - Build: python libraries - pinning more libraries (#1962)
 - Build: python libraries - eventlet + dnspython dep problems were fixed (#1963)
 - Pip builder - ignore proxy test data if it exists

0.45.7 / 2023-11-10 17:39:49 +0100:
 - 0.45.7
 - UI - Fixing issue where search box JS interfered with page render when logged out

0.45.6 / 2023-11-10 17:32:21 +0100:
 - 0.45.6
 - UI - Adding support-us widget <3 (#1956)
 - Visual Selector - Small fix, Improving elements fetcher reliability (#1947)
 - Update README.md - Adding import information
 - Upgrade playwright browser library (#1942)
 - Update docker-compose.yml - playwright version should be the same as in the automated tests
 - Import - Improved Wachete Excel XLS import support for "dynamic wachet" (sets correct state of using chrome browser or not) column (#1934)
 - Refactor Excel / wachete import, extend tests (#1931)
 - Build - Upgrading pip packages (#1915)
 - Ability to Import from Wachete XLSX (or any XLSX) - Wachete alternative made easy (#1921)
 - Docker build - upgrade image to "bookworm" debian version - fix glibc mismatch (#1918)
 - Fetcher - experimental puppeteer fetch - dont rewrite the proxy protocol (fixes socks5 bug)
 - Nice format stats (comma sep)
 - Selenium fetcher - Test was on `4.14.1` but documentation was not, change both to `4` (#1912)

0.45.5 / 2023-10-28 20:20:24 +0200:
 - 0.45.5
 - BrowserSteps - Wrong text taken from browser steps  (#1911)

0.45.4 / 2023-10-28 16:48:10 +0200:
 - 0.45.4
 - Code cleanup - Browser Steps
 - Fetching - Browser Step enabled watches should also identify 404/non-200 status situations (#1907)
 - Text Filters - "Extract Text" filter was not being error checked properly when using a RegEx (#1902)
 - Fetching/BrowserSteps - Going to a page was using slightly logic to the main way - make them use the same methods (#1890)
 - UI - "With errors" tag/button should always show the current tag error count
 - Build - Add piwheels support for ARMv6 and ARMv7 machines (rPi etc) (#1814)
 - Upgrade selenium to 4.14.0 (latest) (#1783)
 - UI - Don't show search icon when logged out (#1896)
 - UI - Adding handy "limit to watches with errors" button (#1886)
 - UI - Viewing text differences - Tweaks to "Jump to next change" button
 - UI - BrowserSteps - Show the screenshot of an error if it happened on a step, highlight which step had the error to make it easier to find out why the step didnt work, minor fixes to timeouts(#1883)
 - UI - Visual Selector should be the same page-size as Browser Steps (fit inside the browser viewport)
 - Packaging - Enable jq query for filters package installation for darwin (mac) #1868
 - UI - Adding [stats] tab to watch Edit page (#1880)
 - Bugfix - [Clear history] button was not clearing all metadata (#1881)
 - RSS fetch - RSS field <title> was not rendering as text correctly, added workaround #1879
 - PDF Fetching - Handle when the PDF is given as inline content without a proper mime header (#1875)
 - Notification library - Bump Apprise notification library to 1.6.0 (#1867)
 - RSS Fetching - Handle CDATA (commented out text) in RSS correctly, generally handle RSS better (#1866)
 - UI - Adding mouseover/title to show absolute date/time of a last-change or last-checked date #1860
 - UI - Difference text viewer - fixing jump to new difference on changing word/line/etc style
 - Testing - Improve xPath tests (#1863)
 - UI - Fixing jump to next difference button after refactor
 - UI - Updating proxy tip link
 - UI - Adding watch label/title to [edit] page title (#1858)
 - Documentation - Add note that playwright is not supported on ARM type devices #1856
 - UI - Difference page - added 'title' to each change for nice mouse-over information about when the change occured
 - UI - Difference page - Tweak 'preview' page invite text
 - UI - Ability to select between any difference date ( from / to ) and minor UI cleanup for differences page (#1855)
 - UI - Difference page, make the button to find the preview page for triggers and ignored text easier to find
 - System - No need to run updates on fresh installs (#1854)
 - UI - Proxy configuration helper notes improvements
 - Preview/Difference page - When sharing the preview/difference page, highlight-to-ignore should login should be required (#1852)
 - Fetching - Clarifying how fetchers work with SOCKS5 proxies

0.45.3 / 2023-10-05 12:29:59 +0200:
 - 0.45.3
 - Update README-pip.md
 - Update README.md
 - LD JSON Price followers - Handle incorrectly created LD-JSON price structures better (#1837)
 - Dockerfile/fix: Update builder and runner to Python 3.11 (#1781)
 - Backend - Regular expression / string filtering refactor for Python 3.11 and deprecation warnings since Python 3.6 (#1786)
 - Update README.md
 - UI - BrowserSteps - Browser Steps interface screen should resize relative to the browser
 - BrowserSteps - <input> of type 'number' should use 'enter text in field'
 - Restock detect - bumping texts for restock detection
 - UI - Proxy Scanner tool should also understand when a filter is empty or contains only an image
 - UI + Fetching - Improving helper message when filter contains only an image (adding link to more help)
 - UI + Fetching - Be more helpful when a filter contains no text, suggest ways to deal with images in filters (#1819)
 - Building application - Upgrade test workflows to latest versions (#1817)
 - Page fetching - Fixed possible incorrect browser user-agent header in playwright/puppeteer/browserless fetchers (#1811)
 - UI - Add extra validation help for notification body with Jinja2 markup (#1810)
 - UI - More precise text to describe "current_snapshot" notification token

0.45.2 / 2023-09-22 09:45:55 +0200:
 - 0.45.2
 - Code/Test - Improve testing for creating backups
 - UI - Re-order notification field settings
 - UI - Notifications - Tidyup - Hide the notification tokens but show with a button/link
 - UI - Notifications - Tweak discord help text
 - RSS feeds - Fixing broken links from RSS index in some environments, refactor code (#152, #148, #1684, #1798)
 - UI - "recheck all" button should ignore blank/empty "tag" setting when set
 - Update README.md
 - UI - Fix spelling error
 - UI - Make tgram:// and discord:// examples in notification settings link to how-to pages (#1785)
 - Catch possible crash scenario for listing watches - `date_created` was missing on add (#1787)
 - Ability to select "No proxy" for a watch when you have proxy's configured
 - Updating notification library - Adds support for Pushy, PushDeer, PushMe and Matrix attachment support (screenshots)
 - Update README.md
 - UI - Fixing update for sort by "date created" or "#" in watch overview table ( #1775 )
 - Add 'diff_patch' notification body token - This will allow the diff to be generated in the "unified patch format." (#1765)
 - README/docs: Clarifying xpath version changedetection.io uses (#1773)

0.45.1 / 2023-09-06 12:27:56 +0200:
 - 0.45.1
 - UI - Fixing open/broken HTML which was causing some buttons to not display

0.45 / 2023-09-06 09:46:27 +0200:
 - 0.45
 - Adding Oxylabs proxy recommendation to proxy config page (#1756)
 - Fix - Link in the RSS feed was showing the path twice (when used in reverse proxy)
 - Fix - Regular Expression text in  `ignore` and `trigger` were not processing correctly, also refactored for lower CPU usage (#1747)
 - Fix typo in README.md (#1759)
 - UI - "Test notification" button in "Group Tag" settings page was broken due to missing variable #1753
 - UI - Clicking 'ignore text' when highlighting text should clear the preview text button/area. #1754
 - Update documentation - How to set number of concurrent fetchers

0.44.2 / 2023-08-28 19:01:59 +0200:
 - 0.44.2
 - UI - Ability to highlight text and have it offered as a ignore-text option, really nice easy way to set ignores on changing text (#1746)
 - Update README.md
 - Enable ARMv8 builds (for RaspberryPi and other portable devices) (#1733)
 - Updating in app links
 - Updating URL validation library, ability to block access to simple (no dot) hostnames like "localhost" with BLOCK_SIMPLEHOSTS setting (#1732)
 - Re-enable ARMv6 builds (for Raspberry and other portable devices) (#1724)

0.44.1 / 2023-08-02 08:55:07 +0200:
 - 0.44.1
 - Re-enable ARMv7 builds (for Raspberry and other portable devices)
 - UI - Fixing darkmode switch icon

0.44 / 2023-07-17 18:03:42 +0200:
 - 0.44
 - Updating AppRise notification library, Improved pover, ntfy support, whatsapp updates, Pagertree support, Voip.ms support, Misskey support, plus many fixes and improvements.
 - API - Updating API description for handling a single watch
 - Removing docker build for RaspberryPi (armv6/armv7) for now due to packaging problems
 - Proxy scan improvements - handle custom proxies, dont restart when a scan is already running (#1689)
 - Browser Steps - When cleaning up old screenshots, check the file exists
 - Scan/Recheck proxies - Report filter not found as "OK" but with warning
 - Bug fix - Previously encountered fetch errors were sometimes not being cleared (#1687)
 - New feature - Helper button to trigger a scan/access test of all proxies for a particular watch (#1685)

0.43.2 / 2023-06-30 22:57:05 +0200:
 - 0.43.2
 - Bug - SMTP mailto:// Notification content-type (HTML/Text) fix and add CI tests (#1660)
 - Fix - Watches werent falling back to global default formats correctly when required (#1656)

0.43.1 / 2023-06-27 18:28:18 +0200:
 - 0.43.1
 - Bug fix - Notification settings were not cascading from global -> tags -> watch correctly in some cases (#1654)
 - Bug - Fix watch clone (#1647)
 - UI - Dont allow empty tag names (#1641)

0.43 / 2023-06-21 14:35:08 +0200:
 - 0.43
 - UI - Watch Table - Clicking anywhere on the watch list row table also activates the operations buttons and checkbox
 - UI/Functionality - Ability to manage/apply filters and notifications across tags/groups
 - UI - Fixes to dark mode toggle (#1629)
 - Docker container updates - use specific debian version (libssl1 vs libssl3) (#1630)
 - Code - Adding CI test for search (#1626)

0.42.3 / 2023-06-12 15:28:51 +0200:
 - 0.42.3
 - Bug fix - Fixed crash when deleting watch from UI when watch was already manually deleted from datadir (#1623)
 - README - Update links to new website
 - Fetcher / Parser - Automatically attempt to extract JSON from document when document contains JSON but could be wrapped in HTML (#1593)
 - Test improvement - Also test that custom request headers works with Playwright/Browserless (#1607)
 - Fetching - Be sure that content-type detection works when the headers are a mixed case (#1604)
 - UI/Fetching - Update "Filter not found" message to be more explanatory/helpful (#1602)
 - Restock monitor - Updating texts for tickets available/unavailable restock detection
 - Docs - Update README.md (Changed LXML re:math reference to re:match) (#1594)

0.42.2 / 2023-05-25 16:47:30 +0200:
 - 0.42.2
 - UI - Configurable pager size #1599 #1598
 - Fetcher - Ability to specify headers from a textfile per watch, global or per tag ( https://github.com/dgtlmoon/changedetection.io/wiki/Adding-headers-from-an-external-file )
 - Restock detection - Better reporting when it fails (#1584)
 - Fetcher - Puppeteer experimental fetcher wasn't returning the status-code (#1585)
 - Update README.md

0.42.1 / 2023-05-21 14:20:23 +0200:
 - 0.42.1
 - Fetcher fix - Clear any fetch error when the fetched document was the same (clear any error that occurred between fetching a document that was the same)

0.42 / 2023-05-18 22:10:10 +0200:
 - 0.42
 - UI - "Search List" also works for 'Title' field
 - UI - New "Search List" icon and functionality (#1580)
 - VisualSelector - Add message when first version cannot be found
 - UI - update link to official project page
 - BrowserSteps - Dont highlight elements that are the full page width (body, wrappers etc)
 - BrowserSteps - Support for float seconds (0.5 etc)
 - BrowserSteps - Session keep alive timer countdown fix
 - BrowserSteps - adding setup check
 - BrowserSteps - Refactored to re-use playwright context which should solve some errors
 - BrowserSteps - Be sure to select the most appropriate input/button/a when an input element is wrapped in a <div> or other
 - Fetcher - Experimental fetcher - dont cache embedded data URLs
 - Fetcher - Experimental fetcher improvements (Code TidyUp, Improve tests, revert to old playwright when using BrowserSteps for now) (#1564)
 - BrowserSteps - Include nice big start button SVG
 - BrowserSteps - Remove unreliable method for detecting if the element has a "click" listener and default to click (switch to 'Click X,Y' will return the right co-ords anyway)
 - Puppeteer fetcher, adding disk cache and other fixes (#1563)
 - UI - Adding shortcut list select button for "clear/reset history"
 - Fetcher - Experimental fetcher fixes, now only enabled with 'USE_EXPERIMENTAL_PUPPETEER_FETCH' env var (default off) (#1561)
 - UI - Adding shortcut list select button for "clear/reset history"
 - Element scraper - wrap offset detection in try/catch
 - BrowserSteps - BrowserSteps was not always following proxy information
 - BrowserSteps - remove minor delay
 - Fetcher - playwright/browserless - Use builtin node puppeteer handler in browserless, scales way better, and is faster (#1559)
 - UI - Fix back navigation / browser history (#1556)
 - UI - HTML validation improvements for edit forms (#1553)
 - UI - Various minor HTML validation fixes
 - UI - pagination - use count including tag filter for pagination display
 - UI - Notifications - Adding icon to "Add Email" button
 - UI - Adding pagination to watch list (#1549)
 - UI - Set selected watches as 'viewed' (#1550)
 - UI - Fix missing </span> in watch list when using restock detection
 - UI - Make sort order and type sticky in cookies, ability to sort by watch created time (#1519)
 - Notifications - Send test notification should use system defaults for body and title if not set in watch (#1547 #1503)
 - Adding generic changedetection.io SVG icon #1527
 - Tests - error test - be sure to clear results from other test parts
 - Update README.md
 - Tests - Add test to check that low level fetch errors are cleared on next check
 - Restock alerts - adding extra detection texts
 - Restock monitor - Identify the cases where the product is also definitely in stock (#1489)
 - Automated CI test for ensuring pypi package was built correctly (#1488)

0.41.1 / 2023-03-22 10:40:49 +0100:
 - GitHub container build - 'provenance' was disabled
 - 0.41.1
 - Fix for pip installations

0.41 / 2023-03-21 20:30:21 +0100:
 - 0.41
 - Notifications - Include triggered text token as  `{{triggered_text}}` in notifications, so you can send just the content that matches. (#1485)
 - Notification tokens - add comment that the {{tokens}} can be used in the URLs also
 - Quick add form - adjust font size and rename stock recheck
 - Ability to set which text to process triggers on (added, removed, changed) according to the difference (#1483)
 - Restock / stock / out of stock monitor - bumping detection texts
 - Use brotli for reducing the size of the text snapshots (#1482)
 - Notification screenshots - now PNG only for now to save disk space (no point creating two images) (#1481)
 - New feature - Restock / stock / out of stock monitor option/mode
 - UI - Clone/copy watch - A paused watch should not be checked when copied/cloned #1471.
 - Update README.md
 - Code - Abstract out the diff fetch types to make it easier to integrate new ones (#1467)
 - BrowserSteps - Adding `Goto URL` step
 - Fixing bad linebreak definition `</br>` in notifications and UI (#1465)
 - Notification Improvements - New tokens `{{diff_added}}` and  `{{diff_removed}}`, removed whitespace around `added` and `into`  ( Issue #905 ) (#1454)
 - Update README.md

0.40.3 / 2023-02-28 18:04:58 +0100:
 - Bug - False change alerts - code cleanups Re #962 (#1444)
 - Update README.md
 - Be sure that `process_changedetection_results` is off after PageUnloadable and EmptyReply exceptions from fetcher - Re #962 (#1439)
 - False change alerts fix - Don't reset watch checksum when a fetch error happens, adjust test to not test for fluctuating filter (#1437)
 - Library update - Replace bs4 with beautifulsoup4 (#1433)
 - API - Including `last_changed` timestamp in watch API info (#1436)
 - Update apprise to 1.3.0 (#1430)
 - API documentation - improving example for list watches
 - API documentation - improving example for snapshot history
 - API - Adding current version to 'System Information' endpoint, bumping API docs, Re #1429
 - Further improving API documentation Re #1426
 - Improving API documentation Re #1426
 - Browser Steps - Adding "Wait for text" and "Wait for text in element" Re #1427
 - Re #1382 - UI fix - sorting now works with selected tag
 - Dont rewrite/resave snapshot when its the same data, just bump the history index, saves disk space. (#1414)
 - Fetching - False alerts issue #962 - be sure to avoid triggering changedetection when checksums were the same  (#1410)
 - Deleting a watch now removes the entire watch storage directory (#1408)
 - Use year/date in the backup snapshot zip filename instead of epoch seconds (#1377 #1407)
 - PDF text conversion - fix bug where it detected a site as a PDF file incorrectly Re #1392 #1393
 - Remove unused code (#1394)
 - UI - preview page - Fix bug where playwright/chrome was system default and [preview] didnt show snapshot
 - Adding example docker-compose.yml config to ignore errors from self-signed certs #1389

0.40.2 / 2023-02-03 19:20:13 +0100:
 - 0.40.2
 - Code cleanup - remove unused import
 - UI fix - Fix logic for showing screenshot on diff page (#1379)
 - Re #1365 - Playwright - Browser "Service Workers" should be enabled by default but unset via env var PLAYWRIGHT_SERVICE_WORKERS=block (#1367)
 - New setting to allow passwordless access to your 'diff' page - perfect for sharing your diff page securely, refactored login code (#1357)
 - Security - Possible stored XSS in watch list - Only permit HTTP/HTTP/FTP by default - override with env var `SAFE_PROTOCOL_REGEX` (#1359)
 - Playwright - Removing old bug fix where playwright needed screenshot called twice to make the full screen screenshot be actually fullscreen (#1356)
 - Fetch backend UI default fixes for VisualSelector and BrowserSteps (#1344)
 - Fix fetch UI default fetch backend option icon (#1343)
 - Docker container build - docker container buildx version change causing errors with watchtower and others (#1336)

0.40.1.1 / 2023-01-22 13:03:15 +0100:
 - 0.40.1.1
 - Re #1328 - add `-6` flag to enable IPv6 (#1329)

0.40.1.0 / 2023-01-21 15:38:54 +0100:
 - 0.40.1.0
 - Update README.md
 - Setting docker-compose.yml version to 3.2 so it works with portainer and others #1306 #1144 #1079
 - UI - Fix wrong logic when dealing with webdriver/playwright watch screenshot settings (#1325)
 - Ability for watch to use a more obvious system default fetcher (#1320)
 - Update README.md
 - pip - eventlet doesnt support dnspython >=2.3.0 (Fixes build error)
 - Reliability fix - Remove loop that could cause app to stop checking if data changes (#1313)
 - API - Improvements, support PUT for updating existing watch, set muted state, set paused state, see https://changedetection.io/docs/api_v1/index.html (#1213)
 - Data storage - Don't recreate DB if its corrupt, exit with error cleanly so operator can look into the problem (#1296)
 - UI: Updating queued success message (#1285)
 - README.md - Fix release link (#1277)
 - Notifications: updating apprise (slack notification fixes and others) (#1272)
 - Remove docker-compose version so it works on any modern version #1144 (#1268)
 - Update the docker compose file to any version (#1079) (#1144)
 - IPv6 support for listening on (#1267)
 - Test improvements (#1264)

0.40.0.4 / 2022-12-25 18:25:45 +0100:
 - 0.40.0.4
 - UI - Suggest adding proxy for watch when 403 access denied is reached (#1260)
 - Filters & Notifications - fixed tokens in filter not found notification
 - UI - Fix broken html tags in settings page
 - Proxy Settings in UI - TidyUp BrightData text
 - Ability to configure extra proxies via the UI (#1235)
 - Docker container updates - use Python 3.10, remove unused packages
 - Tidy up list icons a bit (#1250)
 - PDF File change detection - Initial PDF fetcher support with basic text extraction (#1244)
 - Testing - Run test as fully built docker container (#1245)
 - Dark mode - system setting var is not required (its cookie based)

0.40.0.3 / 2022-12-19 12:41:52 +0100:
 - 0.40.0.3
 - Visual Selector - Select smallest/most precise element first, better filtering of zero size elements
 - Fetching - Check the most overdue watch first (#1242)
 - Overview list - Checkbox action "Recheck"
 - Playwright - Better error reporting and re-try fetch on fail once (#1238)
 - Fetching - Always sort the key order of JSON content for less false alerts  (May cause an alert on upgrade, but will be better going forwards) #1219
 - Fetcher + VisualSelector - xPath filter with attribute filter was breaking the element finder
 - Fetcher - CPU usage - Skip processing if the previous checksum and the just fetched one was the same (#925)
 - Playwright+BrowserSteps - Fetch changes - Fetch simply after page starts rendering + delay seconds, disable service workers
 - Improve ARM/rust build comment
 - README.md - Improving JSONPath example for LD+JSON product data

0.40.0.2 / 2022-12-08 22:36:59 +0100:
 - 0.40.0.2
 - Price follower - Dont scan for ldjson data when 'no' was clicked on the suggestion (#1207)
 - Adding missing parts for pip build Re #1206

0.40.0 / 2022-12-08 20:09:42 +0100:
 - 0.40.0
 - VisualSelector - Exclude items that are not interactable or visible
 - Automatically offer to track LD+JSON product price data (#1204)
 - UI - favicon callback no longer needed
 - Test cleanups (#1196)
 - Update runtime.txt (#1198)
 - Dark mode - HTML template tidy up (#1197)
 - UI - watch tags also known as watch tag / label
 - Notification templates - bug in update, was updating the main system instead of the watch notification_title incorrectly
 - Extract data - minor improvement to example
 - Darkmode - Pause/Mute notification colour fix, re #1195
 - Notification - Support for standard API calls post:// posts:// get:// gets:// delete:// deletes:// put:// puts:// (#1194)
 - Notifications - tokens/jinja2 templating (#1184)
 - Dark mode - more colour fixes
 - Test improvement - improving notification error network test
 - Extract text as CSV - Extra validation (#1192)
 - Dark mode - make watch list easier to read when theres 'unviewed' entries
 - New feature - Simple extract data by regex from all historical watch text into CSV (#1191)
 - UI - Cursor over labels should be pointer
 - Dark mode - Make watches with errors easier to read
 - Dark mode - cookie path should be all site
 - Tweaks - adding hover/title to dark mode button
 - UI - Dark Mode (#1187)
 - docker-compose - Add playwright/selenium container dependencies example (#1178)
 - BrowserSteps - Can be shared by the watch share link
 - UI - Make tabs hoverable
 - Favicon multiplatform and path fix/update (#1176)
 - BrowserSteps - Cleanup interface on shutdown
 - BrowserSteps - More work on cleaner shutdowns of browser session
 - BrowserSteps - Forcefully shutdown playwright to prevent any race-conditions waiting for it to shutdown
 - BrowserSteps - Make the UI require an extra step so it doesnt slow down the experience when clicking through the tabs (#1175)
 - BrowserSteps - Use correct mimetype for screenshot update
 - BrowserSteps - Faster screenshot updates and enable gzip compression for all content replies in the UI (#1171)
 - BrowserSteps - Add 'Execute JS' step
 - BrowserSteps - Also try to find clickable div/spans
 - Update README.md
 - Update README.md
 - BrowserSteps - Element finder filter (offpage) should also calculate top scroll offset
 - Visual Selector and BrowserSteps - More accurate element detection when the page auto-scrolls on load Re #1169
 - Extra validation for URLs with template markup (#1166)
 - Browser Steps - adding 'please wait' text while loading
 - Re #1163 psutil missing from pip requirements
 - Update README.md
 - Update README.md
 - VisualSelector & BrowserSteps - Scraper improvements, remove duplicate code
 - Bumping VisualSelector example animation
 - Remove dupe xpath finder prep code
 - Browsersteps 'Beta' label image path fix
 - Configurable "Browser Steps" when Playwright/Chrome is configured  (enter text, scroll, wait for text, click button etc) (#478)
 - Update README.md -  Make docker instructions easier to follow on Windows  (#1158)

0.39.22.1 / 2022-11-22 18:09:25 +0100:
 - 0.39.22.1
 - Notification screenshot/JPEG was not being regenerated correctly (#1149)
 - Re #1148 - Notification screenshot/JPEG was not being regenerated correctly
 - Update README.md
 - Update README.md

0.39.22 / 2022-11-20 16:29:16 +0100:
 - 0.39.22
 - Fix dangling HTML tag from screenshot notification
 - Notification screenshot option should only be available to webdriver/playwright watches, screenshot sent as JPEG to save bandwidth, Simplify the logic around screenshot,  (#1140)
 - Minor test improvements
 - Option to attach screenshot to notification (#1127)
 - VisualFilter - check previously set filters were set before highlighting
 - Add diff view option for JSON compare (comparing the fields defined on each. The order of fields, etc does not matter in this comparison.)
 - Update visual text difference library, add option to ignore whitespace when viewing diff (#1137)
 - Make VisualSelector show first available multiple selector, refactor to make more maintainable (#1132)
 - Make link to notification debug log easier to find (#1130)
 - Bump notification library (#1128)
 - Re #1126 HIDE_REFERER setting had wrong default
 - Test: Re-test under HIDE_REFERER condition, use strtobool so you can use 'False' (#1121)
 - Stability fix related to the new watch check count (#1113)
 - Use deepcopy to stop possible data corruption (#1108)
 - Code- Use dict .get instead of key
 - Adding a check counter to watch fetching (#1099)
 - Update README.md
 - HIDE_REFERER incompatible with password based login, added comment to code #996
 - Update README.md
 - Filters can now accept a list/multiple filters (#1064) #623

0.39.21.1 / 2022-11-02 23:48:10 +0100:
 - 0.39.21.1
 - Playwright extension added back to Dockerfile to resolve conditional fix Alpine (musl) based systems (#1087)

0.39.21 / 2022-11-02 15:12:33 +0100:
 - 0.39.21
 - Disable version check when pytest is running (#1084)
 - Removing unused code (#1070)
 - Docker & python - Jq conditional pip requirements.txt include (Don't install in Windows because theres no Windows library/wheel)
 - Docker & python - Use pip conditional requirements to not install playwright for ARM (unsupported on ARM) (#1067)
 - UI - Make fetch error more readable (#1038)
 - Update README.md
 - Re #1052 - Watch 'open' link should use any dynamic/template info (#1063)
 - Remove accidental files
 - Backups and Snapshots - Data directory now fully portable, (all paths are relative) , refactored backup zip export creation
 - Re #1052 - Dynamic URLs, use variables in the URL (such as the current date, the date in a month, and other logic see https://github.com/dgtlmoon/changedetection.io/wiki/Handling-variables-in-the-watched-URL ) (#1057)
 - API - system info - allow 5 minutes grace before watch is considered 'overdue'
 - API - Adding basic system info/system state API (#1051)
 - Build - Fix syntax in container build test (#1050)
 - Building - Test container build on PR
 - Testing - Use same version of playwright while running tests as in production builds (#1047)
 - update path for validation in the CONTRIBUTING.md (#1046)
 - History index safety check - Be sure that only valid history index lines are read (#1042)
 - Option to Hide the Referer header from monitored websites. (#996)

0.39.20.4 / 2022-10-17 18:36:47 +0200:
 - 0.39.20.4
 - Better cross platform file handling in diff and preview (#1034)

0.39.20.3 / 2022-10-17 17:43:35 +0200:
 - 0.39.20.3
 - Windows - diff file handling improvements (#1031)
 - Also include tests in pip build
 - Update README.md

0.39.20.2 / 2022-10-12 09:53:59 +0200:
 - 0.39.20.2
 - Windows - JQ - Make library optional so it doesnt break Windows pip installs (#1009)
 - Adding test - Test the 'execute JS before changedetection' (#1006)

0.39.20.1 / 2022-10-09 23:05:35 +0200:
 - 0.39.20.1
 - Code - check containers build when Dockerfile or requirements.txt changes (#1005)
 - Adding `make` to Dockerfile build as required by jq for ARM devices
 - Dont use default Requests `user-agent` and `accept` headers in playwright+selenium requests, breaks sites such as united.com. (#1004)

0.39.20 / 2022-10-09 16:13:32 +0200:
 - 0.39.20
 - Adds support for jq JSON path querying engine (#1001)
 - Adding link to BrightData Proxy info (#1003)
 - Remove quotationspage default watch
 - Notification library: Bump apprise to 1.1.0 (signal, opsgenie, pagerduty, bark and mailto fixes, adds support for BulkSMS and SMSEagle) (#1002)
 - Selenium fetcher - screenshot should be taken after 'wait' time, not before #873
 - Upgrade Playwright to 1.26
 - Render Extract Configurable Delay Seconds should also apply after executing any JS #958
 - Re #958 - remove change screensize, should be in 1280x720 default, was causing "Unable to retrieve content because the page is navigating and changing the content." on some sites
 - Tidy up proxies.json logic, adding tests (#955)
 - Update README.md - Include BrightData suggestion
 - Improve Proxy minimum time debug output
 - Default proxy settings fixes
 - Use proxies.json instead of proxies.txt - see wiki Proxies section (#945)
 - Upgrade Playwright to 1.25
 - Update README.md

0.39.19.1 / 2022-09-11 09:23:43 +0200:
 - 0.39.19.1
 - Notification - code tidyup
 - Watch list & notification - Adding extra list batch operations for Mute, Unmute, Reset-to-default
 - Notification - Reset defaults button should be on edit page only
 - Notification watch settings - add button to make watch use defaults (empties the settings)
 - Notification system update - set watch to use defaults if it is the same as the default
 - Fix typo (#924)

0.39.19 / 2022-09-08 20:16:35 +0200:
 - 0.39.19
 - Update README.md
 - Tweaks to python PIP readme
 - Use play and pause separate icons (#919)
 - Further notification settings refinement (#910)
 - Reliability improvement - Check watch UUID exists when reporting missing path (#915)
 - repair pip readme
 - Test improvement - Visual selector data loads as JSON (#895)
 - Cleaner separation of watch/global notification settings (#894)
 - Code maintenance - Removing old function (#875)
 - Show screenshot age in [preview]
 - Update README.md
 - Update README.md
 - Update README.md
 - Update bug_report.md
 - Update bug_report.md
 - Update README.md

0.39.18 / 2022-08-19 11:37:26 +0200:
 - 0.39.18
 - More data saving pre-checks (#863)
 - Update screenshot
 - Checkbox operations - reorder buttons for safety
 - UI feature - Basic checkbox/group operations (#861)
 - Bug fix - automatically queued watch checks weren't always being processed sequentially
 - Playwright - Support proxy auth mechanisms (#859)
 - Update README.md
 - Update README.md
 - Skip processing when watch was deleted
 - Playwright fetcher didn't report low level HTTP errors correctly (like Connection Refused) (#852)
 - Be sure visual-selector data is set when xPath/CSS filter is not yet found (#851)
 - Visual selector data not being saved by refactor
 - 'Save chrome screenshot' checkbox never used, removing, we always save the screenshot. (#844)
 - Crash fix: Data store sub-directories werent always being created when needed (#842)
 - Make the table header easier to understand when sorting (#840)
 - Column sorting (#838)
 - Update README.md
 - Revert "don't process paused entries after queue", so we can still manually recheck a paused watch
 - Remove 'last-changed' from url-watches.json and always calculate from history index (#835)
 - Massive improvements to error handling - show separate output for non HTTP 200 status replies
 - Execute JS should happen after waiting seconds
 - Upgrade playwright python driver (#834)
 - Crash protection - handle the case where watch was deleted while being checked (#833)
 - Don't process a watch if it was paused after being queued (#825)
 - Notification Library Update (fixes for Home Assistant) - update requirements.txt (#818)
 - Remove social links for now

0.39.17.2 / 2022-08-05 15:53:09 +0200:
 - 0.39.17.2
 - Test fix - Remove debug from test
 - Security update -  Password could be unset from settings form unexpectedly (#808)
 - Disable SIGCHLD Handler for now - keeping SIGTERM for DB writes
 - Handle SIGTERM for cleaner shutdowns (#737)
 - Remove [save & preview] button, the preview is not updated live so it can lead to confusion (#801)
 - Feature - priority queue - edited and added watches should get checked before automatically queued watches (#799)
 - [preview current] cleanup code and add test
 - Feature - mute notifications (#791)
 - Test improvement - remove unnecessary step

0.39.17.1 / 2022-07-29 10:13:29 +0200:
 - 0.39.17.1
 - Bug fix: Filter failure detection notification was interfering with change-detection results, added test case (#786)
 - README.md - new Discord invite link

0.39.17 / 2022-07-28 13:07:51 +0200:
 - 0.39.17
 - Add https://discord.com/api notification hook to the automatic truncation due to Discords 2000 char limit
 - UI Feature - Add watch in "paused" state, saving then unpauses (#779)
 - Enhancement - support xPath text() function filter, for example "//title/text()" in RSS feeds (#778)
 - Bug fix - Filter "Only trigger when new lines appear" should check all history, not only the first item (#777)
 - Visual Selector direct element finder fix
 - Update README.md
 - Update README.md links
 - Filter failure notification send default enable now controlled by setting Env var
 - Refactor of extract text filter - Regex, support Regex (groups) and all python regex flags via /something/aiLmsux (#773)
 - Update README.md - adding LinkedIn link
 - Update README.md - Adding Discord and YouTube links
 - Bug fix for alerting when xPath based filters are no longer present (#772)
 - Send notification when CSS/xPath filter is missing after more than 6 (configurable) attempts (#771)
 - mailto plaintext handling fix for 'plaintext' apprise integration
 - Minor code cleanups
 - Notifications - email - Correctly send plaintext notification email with plaintext header (#767)
 - Form text tweak - Regex clarification (#766)
 - Update README.md
 - Handle simple obfuscations - HomeDepot.com style price obfuscation (#764)
 - Fixing docker-compose.yml PLAYWRIGHT_DRIVER_URL example URL
 - Notifications fix - Discord - added discord webhook base url to truncation rules (#753)
 - Update Playwright URI Env example with stealth setting and CORS workaround (more reliable fetching)
 - remove extra file
 - removing package-lock.json - not required to be in git
 - Share-icon cleanups
 - Test improvement: Extract text should return all matches
 - Bug fix: RSS Feed should also announce utf-8 charset
 - Regex extract filter: Return all regex results instead of first match (#730)
 - Ability to specify JS before running change-detection (#744)
 - Playwright - log console errors to output
 - UI Improvement - Clarifying "Visual Filter" tool as "Visual Selector Filter"
 - Use environment variables to override new watch settings defaults (user-agent, timeout, workers) (#742)
 - Update docker-compose.yml  - Remove duplicate environment variables from playwright-chrome sample config in docker-compose.yml (#738)

0.39.16 / 2022-07-05 16:14:57 +0200:
 - 0.39.16
 - Fix notification apprise application name to changedetection.io #731
 - Update README.md
 - [new filter] Filter option - Trigger only when NEW content (lines) are detected ( compared to earlier text snapshots ) (#685)
 - Playwright - Use HTTP Request Headers override (Cookie, etc)
 - lang: prefer 'clear (snap) history' to 'scrub' (#721)
 - Minor diff page improvements - list should be sorted 'newest first' and no need to include the current version to compare against (#716)
 - bug fix: `last_changed` was being set on the first fetch, should only be set on the change after the first fetch #705
 - Update README.md
 - Improve docker-compose.yml browserless docker container example, add env var for STEALTH and BLOCK_ADS (#701)
 - New filter - Block change-detection if text matches - for example, block change-detection while the text "out of stock" is on the page, know when the text is no longer on the page (#698)
 - Docker containers - :latest is now stable release, :dev is now master/nightly
 - Trigger filters improvement- it's possible some changes weren't getting detected because the previous checksum only recorded when an event occurred (#697)
 - Some changes werent getting triggered because the previous checksum only recorded when an event occured
 - Notifications regression bug in 0.39.15 - only sent the first notification URL
 - Playwright screenshots - no need for high-res "bug workaround" screenshot, use lower quality/faster configurable image quality env var
 - Adding extra check when updating DB on ReplyWithContentButNoText
 - Notifications log - log what was sent after applying all cleanups
 - Re #555 - tgram:// notifications - strip added HTML tag which is not supported by Telegram
 - Give more helpful error message when a page doesnt load
 - Tweaks to playwright fetch code - better timeout handling
 - Re #580 - New functionality - Random "jitter" delay to requests (#681)

0.39.15 / 2022-06-12 14:05:34 +0200:
 - 0.39.15
 - Watch overview list - adding spinner to make it easier to see whats currently being 'Checked'
 - Preview section - add helpful check
 - Send test notification - improved handling of errors
 - Notification log - also log normal requests and make the log easier to find
 - Update bug_report.md
 - Use correct RSS CDATA handling (#662)
 - Improve logging (#671)
 - New [scrub] button when editing a watch - scrub single watch history (#672)
 - Diff + Preview - Hide date selector widget when viewing screenshots as its not yet possible to compare screenshots (but will be soon!)
 - Diff + Preview - Fixing screenshot behaviour after preference change
 - Screenshot handling on the diff/preview section refactor (#630)
 - Shared watches - include "Extract text" filter
 - Improve error message when filter not found in page result (#666)
 - "Extract text" filter - improve placeholder example
 - Visual selector - 'clear selection' button should clear the filter also
 - New feature - "Extract text" filter ability (#624)
 - Fixing RSS feed HTML content formatting (#662)
 - Update notification library - Improving telegram support
 - 'Mark all viewed' button was missing in this version, added test also. (#652)
 - Content fetcher - Handle when a page doesnt load properly
 - Playwright - Correctly close browser context/sessions on exceptions
 - Move history data to a textfile, improves memory handling (#638)
 - Update feature_request.md
 - Remove UK Covid news
 - Visual Selector fix: Firefox compatibility - Visual Selector (#646)
 - Remove group tag arbitrary length limit (#645)
 - Distill.io import bug fix when no tags assigned to a watch (#557)
 - Ignore whitespace on by default
 - Visual Selector - clear events when changing tabs
 - Minor code cleanup
 - Re #616 - content trigger - adding extra test (#620)
 - README.md update Visual Selector tool - tidy up screenshots, improve text
 - Playwright - ByPass CSP for more reliable JS scraping, disable accept downloads
 - VisualSelector - Better handling of filter targets that are no longer available in the HTML
 - Update bug_report.md
 - 0.39.14.1

0.39.14.1 / 2022-05-24 00:21:30 +0200:
 - 0.39.14.1
 - pip build fix - include API module
 - Visual Selector - be more resilient when sites interfere with the xPath scraping
 - Adding new Visual Selector for choosing the area of the webpage to monitor - playwright/browserless only (#566)

0.39.14 / 2022-05-23 14:40:26 +0200:
 - 0.39.14
 - Fix encoding errors with XPath filters from UTF-8 responses (#619)
 - API Interface (#617)
 - Add note that changedetection is not performed on the screenshot just yet (WIP https://github.com/dgtlmoon/changedetection.io/pull/419 )
 - Fixing edit template HTML
 - Proxy settings on watch should have a "[ ] default" option (#610)
 - Input field tidyup (#611)
 - Update wiki link for 'More info' about sharing a watch and its configuration
 - Option to control if pages with no renderable content are a change (example: JS webapps that dont render any text sometimes) (#608)
 - Playwright - raise EmptyReply on empty reply, no need to process further
 - Re #214 - configurable wait extra seconds for webdriver requests before extracting text (#606)
 - Fix PLAYWRIGHT_DRIVER_URL default value (cf. #587) (#599)
 - Update PIP readme.md

0.39.13.1 / 2022-05-10 22:45:08 +0200:
 - Fixing Pip install problem - Update MANIFEST to include model/ subdir, improving imports (#593)

0.39.13 / 2022-05-10 17:24:38 +0200:
 - 0.39.13
 - Distill.io JSON export file importer (#592)
 - Ability to specify a list of proxies to choose from, always using the first one by default, See wiki (#591)
 - Improving Playwright docs (#588)
 - Playwright - code fix
 - Playwright fetcher - more reliable by just waiting arbitrary seconds after the last network IO
 - Make proxy configuration more consistent - see https://github.com/dgtlmoon/changedetection.io/wiki/Proxy-configuration (#585)
 - Playwright fetcher - use the correct default User-Agent
 - Toggle visibility of extra requests options/settings when not in use (#584)
 - Add new fetch method: Playwright Chromium (Selenium/WebDriver alternative)  (#489)
 - Simplify scrub operation (simply cleans all) (#575)
 - Bugfix - dont update record when deleted during check
 - Improving support info in README.md
 - Handle deletions better (#570)
 - Data storage bug fix #569
 - Upgrade notifications library - fixing marketup in email subject
 - Ability to 'Share' a watch by a generated link, this will include all filters and triggers - see Wiki (#563)
 - Upgrade notifications library Re #555 - fixing telegram HTML markup in notification title
 - Unify MINIMUM_SECONDS_RECHECK_TIME env var variable to 60 seconds
 - Seconds/minutes/hours/days between checks form field upgrade from 'minutes' only (#512)
 - Form styling improvements
 - Form field handling improvements - fixing field list handler for empty lines
 - Fix "Add email" button in main global notification settings
 - Test notification button fixed in main settings (#556)
 - tgram:// be sure total notification size is always under their 4096 size limit
 - Shows which items are already in the queue, disables adding to the queue if already in the recheck queue (#552)
 - Notifications - Signal API support, Ntfy support, hotmail, matrix, Gotify API fixes
 - Discord:// notification size limit - also includes the notification title
 - Fix spelling errors
 - Update README.md
 - Update README.md
 - Import speed improvements, and adding an import URL batch size of 5,000 to stop accidental CPU overload (#549)
 - Ability to set the default fetch mode via the DEFAULT_FETCH_BACKEND variable
 - Refactor form handling (#548)
 - Adding support for change detection of HTML source-code via "source:https://website.com" prefix (#540)
 - Re-label the quick-add widget placeholder 'tag' to 'watch group'
 - HTTP Fetcher code improvements
 - Adding RSS metadata auto-discovery
 - Upgrade WTforms form handler to v3 (#523)

0.39.12 / 2022-04-09 14:16:30 +0200:
 - 0.39.12
 - Miscellaneous settings form visual improvements (#535)
 - Option to render links as [Some Text ](/link), adds the ability to change-detect on hyperlink changes
 - Specify our Discord avatar_url as default avatar_url
 - Minor git updates
 - Fix screenshot tab name
 - Discord:// notifications should be cut to 2000 chars or Discord will not process them. (#531 + #323)
 - Make long reports in the notification error log easier to read
 - [Add email] button in notification settings with a prefix set from NOTIFICATION_MAIL_BUTTON_PREFIX env variable when defined. (#528)
 - Update README.md
 - Skip processing a watch into the RSS feed if there's not enough data to examine (fixes Internal Server Error when accessing the RSS feed) (#521)
 - Introduce an AJAX button for sending test notifications instead of the checkbox (#519)
 - Make text tab always available at default
 - When fetching a snapshot via Chrome, make the most recent screenshot available on the Diff and Preview pages (#516)
 - Remove 'unviewed' status in watch table when Diff link clicked (#514)
 - RSS feed CDATA should contain difference output
 - Fix - {diff} and {diff_full} notifications tokens were not always including the full output
 - Update README.md
 - Update README.md
 - Minor UI cleanups (mobile tabs, font sizing) (#503)
 - Fix typo in Filters & Triggers settings. (#495)
 - Add autofocus attribute to password login field (#496)

0.39.11 / 2022-03-23 09:42:51 +0100:
 - 0.39.11
 - Microsoft Windows installation fixes (#492)
 - GitHub tweak - container tags should be CSV list (Fix ghcr.io not building)
 - GitHub tweak - build containers also on push to master
 - Allow changedetector to ignore status codes as a per-site setting (#479) (#485)
 - Security update - Use CSRF token protection for forms, make "remove password" use HTTP Post (#484)
 - Security update - Protect against file:/// type access by webdriver/chrome. (#483)
 - Only build container on GitHub releases, not tests
 - Also change container names to help stop some DNS issues
 - Detect byte-encoding when the server mishandles the content-type header reply (#472)
 - Improving form/edit example markup
 - JSON diff/preview should use utf-8 encoding where possible (#465)
 - Fix typo in settings form
 - Add python venv to .gitignore

0.39.10 / 2022-03-12 17:28:30 +0100:
 - 0.39.10
 - Add filter to remove elements by CSS rule from HTML before change detection is run (#445)
 - Minor updates to filters form text
 - Re #448 - Dont use changedetection.io as the container name and hostname, fix problems fetching from the real changedetection.io webserver :)
 - Testing - Refactor HTTP Request Type test (#453)
 - Make table header font size the same as content
 - Adjust background colours
 - Handle the case where the visitor is already logged-in and tries to login again (#447)
 - Make the Request Override settings easier to understand
 - Minor tweak to notification token table
 - Style tweak to watch form
 - Login form style fixes
 - Upgrade apprise notification engine to 0.9.7 (important telegram fixes)
 - Remove pytest from production release pip requirements
 - Style fix for background image relative to X-Forwarded-Prefix when running via reverse proxy subdirectory
 - Re-arranging primary links so the important ones are easier to find on mobile
 - Set authentication cookie path relative to X-Forwarded-Prefix when running via reverse proxy subdirectory (#446)
 - Upgrade inscriptis HTML converter to version 2.2~ (#434)
 - Better text/plain detection and refactor tests (#443)
 - Tweak support tabs and text (#440)
 - Include link to changedetection.io hosted option (#439)
 -  Improved CPU usage around the loop responsible for what sites needs to be checked
 - Update README.md with hosting options

0.39.9 / 2022-02-24 17:02:50 +0100:
 - 0.39.9
 - Minor reliability upgrade for large datasets - retry deepcopy (#436)
 - "Recheck" button should work when entry is in paused state
 - Better file exception handling on saving index JSON
 - Fix small issue in highlight trigger/ignore preview page with setting the background colours, add test
 - Ensure string matching on the ignore filter is always case-INsensitive
 - Ability to visualise trigger and filter rules against the current snapshot on the preview page
 - Update README.md
 - XPath RegularExpression support
 - better checking of JSON type
 - Make system level errors from the HTTP fetchers easier to find (#421)
 - Bump node-sass from 6.0.1 to 7.0.0 in /changedetectionio/static/styles (#415)
 - Dont allow redirect on login, it's safer and more reliable this way (#414)
 - When using Env. FETCH_WORKERS or WEBDRIVER_DELAY_BEFORE_CONTENT_READY , it should be type int

0.39.8 / 2022-02-08 18:56:10 +0100:
 - 0.39.8
 - Number of fetching workers can be overriden by Env "FETCH_WORKERS" (#413)
 - Adding Env var "WEBDRIVER_DELAY_BEFORE_CONTENT_READY" to wait n seconds before extracting the text from the browser
 - Language fix "watches are rechecking." it actually puts them into an internal queue "watches are QUEUED for rechecking"
 - Use flask url_for() for webdriver chrome icon instead of relative path
 - Fix typo in the startup create-directory command suggestion (#405)
 - Introduce -h option to allow listening not on 0.0.0.0. (#406)
 - Refactor tests for notification error log handler (#404)
 - Notification error log handler (#403)
 - Add notification note - tgram:// bots cant send messages to other bots, so you should specify chat ID of non-bot user.
 - fixed the reference to wiki for rpi section (#402)
 - /preview format doesnt need <pre> - fixing too many returnlines in content on diff/preview page
 - Update README.md
 - Update README - Fix docker section
 - Update README - Tidy up sections
 - Offer instance on Lemonade Tidy README
 - Ability to use a generated salted password in deployments as env var SALTED_PASS (#397)
 - #323 Adding note about discord:// 2000 char limit (#392)
 - plaintext mime type fix - Don't attempt to extract HTML content from plaintext, this will remove lines and break changedetection (#391)
 - .add_watch() can accept empty tag Use https://changedetection.io/CHANGELOG.txt as a nice default page to watch
 - Add option for tags on import (#377)
 - Update CONTRIBUTING.md
 - Update README.md
 - Fix bug where diff and diff_full were switched in notification templates. (#380)
 - Closes #378

0.39.7 / 2022-01-15 23:21:06 +0100:
 - 0.39.7
 - Scrub watch snapshot fixes
 - Simple HTTP auth (#372)
 - Adding note about JS pages
 - Notification settings defaults and validation (#361)
 - Filters settings helper text tidy-up
 - Add test for low-level network error text handling
 - Add API endpoint for current snapshot (#359)
 - Clarify notice/messages around changing ignore text

0.39.6 / 2022-01-05 19:13:42 +0100:
 - 0.39.6
 - Heroku tweaks (backup download) (#356)
 - XPath support (#355)
 - Better handling of EmptyReply exception, always bump 'last_checked' in the case of an error (#354)
 - Adding note in comments for working arm64 chrome with rPi-4 (#336)
 - fix typo in README.md (#350)
 - Re #348 - Add test for backup, use proper datastore path
 - Update README.md
 - Be sure that documents returned with a application/json header are not parsed with inscriptis (#337)
 - Re #340 - snapshot should not be modified by ignore text (#344)
 - Re #133 Option for ignoring whitespacing (#345)
 - Re #342 notification encoding (#343)
 - Update README.md
 - Adding global ignore text (#339)
 - Adding new proxyType to selenium mappings
 - Use selenium 4.1.0
 - Bumping selenium version re https://github.com/dgtlmoon/changedetection.io/pull/331#issuecomment-1003323594
 - Add socksVersion mapping (#331)
 - Fix broken RSS link fields
 - RSS Link links you back to the difference UI/JS page, RSS Description is the page you're watching, and RSS Title is the page you're watching
 - Unify Filters and Triggers tabs into a single tab
 - Move 'request type' field to the new 'Requests' tab
 - Aligning call signatures #325
 - Extend Request Parameters to add Body & Method (#325)
 - Update README.md
 - Create CONTRIBUTING.md
 - Update README.md
 - Re #267 - Pass settings for the proxy setup for webdriver (#326)
 - Update README.md
 - Update README.md
 - Update README.md

0.39.5 / 2021-12-27 23:46:29 +0100:
 - 0.39.5
 - Update feature_request.md
 - Update issue templates
 - Update bug_report.md
 - Update issue templates
 - W3C HTML validation issue around RSS icon
 - Closes #323 adds link to wiki
 - Update README.md
 - Update README.md
 - improve theming docs
 - Update README.md
 - Update README.md
 - Closes #315 - Include library apprise Notify_mqtt
 - Re #80, sets SECLEVEL=1 in openssl.conf to allow monitoring sites with weak/old cipher suites (#312)
 - Go back to docker hub
 - RSS allow access via token (#310)
 - Adding deploy to Heroku button
 - Adding heroku app.json app
 - Tweak runtime Heroku version
 - Tweaking heroku Procfile
 - Adjust buildpacks on Heroku
 - Adding heroku python3 runtime config
 - Try simpler heroku recipe
 - -C option to create a datadir if it doesnt exist
 - Re #308 - Adding test and including settings in clone operation (#309)
 - fixing too small font in diff UI (#260)
 - Update README.md
 - Send diff in notifications (#296)
 - Fix scrub form theme
 - Scrub dates: Fix date regex limit handler parsing
 - Wait 60 seconds or until stop_thread is set
 - Check that a notification URL is set when sending the test notification (#300)
 - Flask 2 (#299)
 - Re #269 - Show current/correct BASE_URL information (#271)
 - Re #269 - Fix env var comment name
 - Enable Markdown and HTML notifications. (#288)

0.39.4 / 2021-12-02 22:54:38 +0100:
 - 0.39.4 release
 - Re #286 - Solving lost data/corrupted data - Tweak timing and try to write to a temp file first (#292)
 - Fix element paths when using reverse proxy subfolder (#272)

0.39.3 / 2021-10-28 11:32:33 +0200:
 - 0.39.3 release
 - Re #264 - fixing clone watch operation
 - Re #265 - extended jsonpath support (#266)
 - Re #265 - wasnt catching the jsonpath exception due to invalid jsonpath expressions properly
 - Re #257 - Handle bool val of json path better (#263)
 - Re #249 - Add EXPOSE 5000 to Dockerfile
 - Provide better combination of chardet and urllib3
 - Prefer GHCR.io over DockerHub (#245)
 - Limit branches/tags of container build
 - Re #213 - Adding screensize examples to selenium container
 - Be more specific about tagged release builds
 - Fix :latest release worflow syntax check
 - Form helper - explain where the webdriver setting comes from
 - Rename workflow name
 - Just 'published' and 'edited' package release is enough (remove 'created')

0.39.2 / 2021-10-06 08:49:33 +0200:
 - Fixing workflow tag syntax issues
 - fix broken workflow syntax
 - add step for metadata debug, see if it runs by checking workflow tag name
 - Container build/push doesnt need to be so specific
 - Oops on/release was in the wrong block
 - release also on edited, published
 - Run workflow on release
 - Use a better switch mechanism for build type
 - version 0.39.2
 - Configurable BASE_URL (#228)
 - Split python pip builder to its own release based workflow
 - remove accidental syntax add
 - Re #242 - app was treating notification field defaults as the field value (#244)
 - attempt to re-enable docker layer cache
 - Forgot GHCR tag with version
 - Limit container build to releases and master
 - Fix GHCR login
 - Use the same workflow for tag and release
 - Drop redundant build workflow
 - try :latest and :tag in same workflow run
 - Separate workflows
 - Docker image build issues (#243)
 - Re #239 - Individual GUID for watch+changeevent (#241)
 - Update README.md
 - Re #232 - Use a copy of the datastore incase it changes while we iterate through it (#234)
 - Setting for Extract <title> as title option on individual watches (#229)
 - GitHub repo build platforms: linux/amd64,linux/arm64,linux/arm/v6,linux/arm/v7
 - GitHub container repo (#227)
 - Remove extra build step
 - push github container master also
 - Tidy up workflow names
 - Attempt to setup GitHub Container Registry

0.39.1 / 2021-09-17 18:40:16 +0200:
 - v0.39.1
 - Re #185 - [feature] Custom notifications templates per watch (#226)
 - Bump tar from 6.1.6 to 6.1.9 in /changedetectionio/static/styles (#209)
 - Re #225 - Notifications refactor token replacement fix possible missing value for watch_title
 - Re #42 - Notifications refactor token replacement fix possible missing value for watch_title
 - Bump tar from 6.1.6 to 6.1.9 in /changedetectionio/static/styles (#209)
 - Adds 'Create Copy' feature to clone a watch (#184)
 - adding specific test (#205)
 - New notification tokens - watch_uuid, watch_title, watch_tag, (#201)
 - Re #203 - validate tokens (#204)
 - No point hiding the notifications customisation area because it's now in its own tab
 - Update README.md
 - Test - prove that notifications are not being sent when content does not change
 - remove quotes from env vars
 - Re https://github.com/dgtlmoon/changedetection.io/discussions/189 A note to not use quotes in env parts
 - WebDriver fetcher - settings - when an alternative one is configured, show it in the label
 - Update README.md

0.39 / 2021-08-16 15:24:37 +0200:
 - Installation via pip (#186)
 - Update README.md
 - Trigger text/wait (#187)
 - Reword group tag - more obvious name
 - Fix img alt/title accesibility for pause icon
 - Let the fetcher throw an exception which will be caught and handed to the operator anyway
 - Example placeholder was pushed out
 - Move fetcher tab back to general - save space on mobile
 - WebDriver test fetch should use environment var too
 - Add fetch option to each watch
 - Chrome/Webdriver support for Javascript websites (#114)
 - Fixing tar npm security issue npm install  "tar@>=6.1.2"

0.38.2 / 2021-08-07 14:18:28 +0200:
 - tag 0.38.2
 - Re #172 - be sure that we are non-greedy matching the first : when splitting the headers so we dont break "Cookie" header (#175)
 - Update heroku.yml
 - Re #156 - PORT should always be an Integer
 - Re #159 - Adding env var example to docker-config.yml
 - Add Heroku Deployment Support (#159)
 - Re #154 - Handle missing JSON better
 - high res
 - higher res screenshot
 - Update screenshot
 - Assert that html_tools.JSONNotFound is correctly raised
 - Re #154 Ldjson extract parse (#158)
 - Responsive fix for input field on mobile
 - Re #148 - Always set something for {base_url} so we dont send possibly an empty body/title notification which could break some services.
 - Add medium-size-desktop class to notification custom title
 - Notification default: Make sure to use atleast some text here, a blank notification body could be problematic for some services
 - Re #150 - stop using 'size' across all elements and rely on CSS for a better mobile experience (stops fields from pushing out)
 - fix: setting overflow in mobile view (#150)
 - Re #121, #123 - Show the current base_url value
 - Re #149 - allow empty timestamp limit for scrub operation
 - Dont show "new version available" message when password is enabled and user is logged out
 - test fix - dont trigger notifications in header test
 - Strengthen the notification tests
 - Re #137 - Adding test to confirm that headers are not repeated
 - Add debug output to notify loop
 - Add note to field
 - Cleanup test helper data before and after running
 - Improve debug info

0.38.1 / 2021-07-20 17:57:27 +1000:
 - 0.38.1 tag
 - Re #143 - Remove old notification test code, fix form handler (#145)
 - Update README.md
 - Re #135 - refactor the quick add widget (#136)
 - Partially revert 47e5a7cf0990bc958061ce57de8ae88f3fbd39aa (#138)

0.38 / 2021-07-16 16:24:01 +1000:
 - use a github action for getting the tag
 - rename tag build runner
 - fix tag
 - build and push tag
 - Re #76 - Fixing links
 - Cleaner is to let flexbox overflow and scroll on the X where needed
 - #76 app path prefix when behind proxy_pass (#91)
 - Settings: Remove password link fix
 - Make sure right menu is still visible when URL is long
 - 0.38 release
 - Re #132 - Make a list of the JSONpath results instead of using only the first value
 - Customisable notifications (#123)
 - Re #117 - dont re-encode single value types, looks better in the diff
 - Usability tweak - [edit] on diff page should go back to diff page
 - Update README.md
 - Adding text about JSON API Monitoring
 - Re #117 Jsonpath based JSON change detection filter (#125)
 - Update README.md
 - Update README.md
 - Use right sticky for version
 - Re #118 - Make 'show current version' more obvious
 - Diff page - use the document title in <title> for better bookmarking
 - node-sass 6.0.1 works with node-sass watch way better
 - Updating inscriptis/text/html library to 1.2
 - Update readme with the branch link for javascript support
 - Updating trim-newlines packages

0.37 / 2021-07-02 20:19:26 +1000:
 - 0.37 release
 - #110 global recheck time (#113)
 - Re #106 - handling empty title with gettr cleanup (#107)
 - Update README.md
 - Auto extract html title as title (#102)
 - Bug fix - Check 'minutes_between_check' is set
 - tweak <pre> text wrapping when displaying diff
 - CSS Filter - Smarter is to just extract the HTML blob and continue with inscriptus, so we have almost the same output as not using the filter
 - CSS Filter - restore nicer linefeeds
 - @todo Comment - BS4's element.get_text() seems to lose the indentation format no-matter what
 - CSS Filter - strip text of whitespacing, preserve new lines where applicable, remove extra newlines
 - Include statistics for number of watches
 - Set edit-form for settings+watch to always be wide

0.36 / 2021-06-22 10:33:27 +1000:
 - Update README.md
 - 0.36
 - Re #42 - dont use blank titles
 - Re #100 - Fixing storage of minutes_between_check and adding automated test for field storage

0.35 / 2021-06-22 00:28:41 +1000:
 - 0.35
 - Time between rechecks is always stored as minutes
 - Ability to reset app password by placing a file called removepassword.lock into your data directory and restarting the instance
 - Adding tests for password control handling
 - Remove unused field (removepassword is actually a link)

0.34 / 2021-06-21 22:13:14 +1000:
 - 0.34
 - Be sure not to use blank passwords as the password
 - Re #42 - custom title (#98)
 - Re #92 - Re-use existing [preview] function for viewing current (#97)

0.33 / 2021-06-21 20:07:04 +1000:
 - 0.33
 - #81 - Regex support (#90)
 - Use wtforms handler (#96)
 - Re #95 - Include PUID/PGID example
 - re-enable tests
 - On settings submit, display saved message
 - Use flasks' built in 'flash' method instead of a custom message/notices (#94)
 - Adding rPi support info
 - Re #92 Adding link to CSS selector help in wiki
 - Re #93 - tweak build packages
 - Re #93, #79 - docker image multistage build lost the packages required for rPi etc
 - Strip surrounding whitespace from elements (#89)
 - Queue an entry for immediate recheck after [edit]
 - Adding helper method to remove text files that are not in the index
 - Fix typo
 - Re #88 - placeholder text on CSS rule
 - Re #86 - fix typo

0.32 / 2021-06-15 09:50:24 +1000:
 - 0.32 release
 - Sassify the diff page
 - "Sassify" the theme, easier to manage
 - Mobile fixes (#87)
 - Re #86 - Refactor scrub date limit code
 - Tweak comments
 - Re #77 - Repair and refactor time threshold check code
 - Modifies Dockerfile to use multistage builds (#79)
 - Bumping to 0.31

0.31 / 2021-06-03 10:51:18 +1000:
 - Re #75 - Adding test to confirm watched URL appears in RSS feed
 - CSS selector filter (#73)
 - Fixing var name
 - Include release metadata during github build
 - Update README.md
 - Re #40 Ability to set individual timers (#72)
 - Update README.md
 - Improvements for backup (#70)
 - Update README.md
 - Disable image layer cache service
 - Re-enable ARM v6/v7 builds
 - Install requirements, remove rust and dev packages that are no longer needed, hopefully for a smaller docker layer size
 - Remove rust build comments
 - Arm build fixes (#68)
 - Re #65 - Append BASE_URL env var to the notification if it is set (#66)
 - Update README.md
 - Adding BTC support instructions
 - Switch to just amd64 for now due to apprise not building on ARM
 - Fixing syntax
 - Re #49 Re #60 - Adding more information about proxy setup to README.md
 - Add socks proxy support (#60)
 - Created docker-compose file (#55)
 - Re #58 - reduce to 1 minute (a small rewrite is required to change the backend to store in 'seconds' instead of minutes)
 - 56 - Fix notification test
 - Update README.md
 - Update README.md
 - Adding rust compiler :(
 - trying without libssl and only libffi
 - Adding extra libs required for build
 - Cleanup docs
 - Tweak workflow (tests)

0.30 / 2021-05-08 11:33:46 +1000:
 - Security update
 - Apprise notifications (#43)
 - Fixing security update
 - Also detect pytest in the environ (for local debug)
 - Prepend 'test-' when runnning under pytest to guid
 - - Relabel login button - misc test cleanup
 - Re #46 - Add note to README.md about Javascript support
 - Bumping version
 - Re #45 - Set datastore path in app.config
 - Re #44 - Broke the menu by accident, adding tests and fixing.
 - bump to 0.29

0.29 / 2021-04-30 16:54:07 +1000:
 - docker-compose for dev not needed (use venv etc)
 - Password protection / login support (#34)
 - Update FUNDING.yml
 - Skip using tag limit on pause when no tag is being viewed
 - Pause/Unpause should respect limit tag on redirect
 - Validate duplicate URLs
 - Chdir is not needed because we add the file from the full path, but make it 'relative' in the Zip
 - Fix backup generation on relative paths (like when run outside docker, under venv, etc)
 - Adding noopener per CodeQL, stop pages from knowing the referer etc
 - Create codeql-analysis.yml
 - yarl not needed, lock requests version
 - dev packages needed, drop apt cache
 - See if we get a clean buildx without dev packages
 - Tweaking build size thanks to https://github.com/hadolint/hadolint
 - Adding dockerignore
 - Re #18 - Show "preview" of the page when only one revision exists (#33)
 - Update README.md
 - Update README.md
 - Also check that the watch is not paused before putting it into the checking queuex
 - revert c60be562718d23972d7d43821bb6b87f2add3256
 - remove extra packages (#32)

0.28 / 2021-04-01 14:43:46 +0200:
 - Bumping version to 0.28
 - Docker push amd64 rpi etc (#28)
 - Open [diff] links into their own window
 - Fix auto jump on viewing the diff
 - Re #30 - Delete history watch snapshots (#31)
 - Slow down the DB write interval and catch the case that it changed during write
 - Immediately 'jump' to the change
 - Tweak to hover pause icon
 - Stop runtime error on dict changing during write/init at start (#27)
 - Re #22 - ability to pause
 - Re #23 - always check value of interval time, not just on start
 - Update README.md
 - Use absolute image links so the screenshots work from docker hub
 - Update README.md
 - Updating screenshot
 - Reuse the GUID if we have one

0.27 / 2021-03-01 15:50:25 +0100:
 - Dont show 'empty' tag, it will be in the [ALL] list
 - Adding RSS feed icon
 - Generic object sync should use private method
 - Add missing urllib3
 - Add missing pytz
 - Check for new version
 - Fix import form flow logic
 - Code tidy/lint
 - Tidy up thread logic and version check
 - Add missing dep
 - Remove todos
 - Add icon for RSS, RSS should show only unviewed entries
 - Issue #7 - RSS feeds
 - Always override tag version (load from disk in future, so we can add it at build time)
 - next dev is 0.27
 - Tweak to tests
 - Move logic
 - Remove erroneous extra liveserver setup
 - When new ignore text is specified, reprocess the checksum
 - Adding filter and log output to pytest
 - Fix edit action link
 - Minor lint cleanup
 - Clean up after test case
 - Remove liveserver, doesnt belong here
 - Fix syntax, Triggers the workflow on push or pull request events
 - Activate workflow on all branches
 - Issue #14 - Tweaks to edit, create ignore text, tests for ignore text, integrate ignore text
 - Validation of added headers, should contain key/val (2 parts)
 - Issue #12 include version for easy reference.
 - Bring dev environment inline
 - Tidying up requirements.txt

0.26 / 2021-02-24 09:56:29 +0100:
 - Handle the case of someone supplying a bad link
 - Adding jump to next change diff widget
 - Moving nice screenshot to above the fold :)
 - Adding docker hub badge for tag information

0.25 / 2021-02-22 08:53:04 +0100:
 - Bumping schema tag to 0.25
 - Issue #5 - Remove arbitrary '600' minutes limit
 - Add test delay for github action test
 - Add wait for threads in test
 - Extending tests to cover resetting the diff/unviewed status correctly
 - Tidy up return logic
 - Code tidy
 - Fix docker app files paths
 - Tweaking Dockerfile for new eventlet wrapper
 - Create LICENSE
 - Adding docker pulls counter badge
 - Use master branch for badge
 - Removing unused import
 - Fixing a few more easy lint wins
 - Linting fixups
 - Update README.md
 - Add badge under pytest branch
 - Create python-app.yml
 - Create the test datastore
 - Minor cleanup
 - Just use the current/previous md5
 - Finalse pytest methods
 - Port should be an integer
 - Tweaking client
 - remove unused imports
 - Use session/client fixture
 - Addingmissing files
 - hack of pytest implementation - doesnt work yet
 - Tidy up a few broken datastore paths
 - WIP, separate out the Flask from everything else, get pytest working
 - Make records in the overview that have a difference that have not been viewed in the [diff] tab bold

0.24 / 2021-02-05 18:46:00 +0100:
 - Adding 0.24 tag
 - Avoid accidently using Python's objects that are copied - but land as a 'soft reference', need to use a better dict struct in the future #6
 - Minor fix to 'last changed' field, simplify template and logic
 - Remove debug print

0.23 / 2021-02-04 12:38:48 +0100:
 - Use a thread locker and cleaner separation of concerns between main thread and site status fetch

0.22 / 2021-02-03 22:28:37 +0100:
 - Adding tag to json
 - Adding SEND_FILE_MAX_AGE_DEFAULT to ensure backups etc dont get old
 - Minor fix - load extra stylesheet only once
 - Minor tweaks for development setup
 - Provide named containers and remove all existing
 - Adding new [Scrub All Version History] button under [settings] (But keep your URL list)
 - Flag for immediate sync of index after adding new watch
 - Sometimes it seems .update wasnt thread safe and isnt used here, just add a clean new dict member
 - Adding ARG to Dockerfile
 - Include the triggered build SHA as part of the backup info, when built in docker hub.
 - Add cache busting var to style sheets
 - Slightly more bulletproof instructions
 - Updating screenshot
 - Push newly created watches directly into the update check Queue.
 - Adding checkall
 - Easily download a full backup
 - Show the date/time of the current/most up to date version
 - Use a pool of thread workers, better for huge lists of watchers
 - Code cleanup edit submit handler can be the same function
 - Add update howto
 - Refactor slightly confusing difference build function
 - Version comparison had the wrong order
 - https://github.com/psf/requests/issues/4525 - brotli compression is not yet supported in requests, be sure that users cant accidently use this content type encoding in the headers

0.21 / 2021-02-01 21:56:18 +0100:
 - Include the current URL in the page when viewing the version diff
 - Include a selfcheck/diagnosis routine
 - On manual recheck request, redirect to same tag listing
 - Set default diff type to 'lines', faster for starters.
 - Supply different versions to browse
 - Fix heading
 - Update README.md
 - Adding diff screenshot
 - Add more start-up examples
 - Tweak theming
 - Use a even simpler run command
 - improve the wording
 - Add basic settings page (so far just recheck time in minutes)
 - Updating README
 - Updating screenshot (new diff button)
 - Trigger write index after edit of a watch
 - Add [diff] mechanism
 - Use a single thread for writing the sync json
 - Use existing tag
 - When all items showed, show which tag it belongs to
 - Sort tag list
 - Set active tag selection
 - Support for comma separated tags
 - Tweak styling for 'new watch' form
 - Remove import for old lib
 - Switch to inscriptis prepare config backend struct
 - Support for custom headers per watch
 - Going back to larger PNG screenshot, looks better in Github :)
 - Fix alt text in markup
 - Adding new screenshot binary
 - Updating screenshot
 - Moving start text to a more visible part
 - Tweak messages
 - Change message text
 - Fixing messages styling
 - Basic tag browse buttons
 - Bulk import
 - Tidy up 'last_checked' date handling
 - Dev environment setup
 - Dev docker tweaks
 - Remove messy text
 - Tweaking text
 - Fixing checkall hook
 - Use requests's r.text so we dont have to deal with charsets
 - Add note
 - Fix bad copy command
 - Oops left out the image name

0.12 / 2021-01-29 12:33:42 +0100:
 - Fix build setup for the docker hub image https://hub.docker.com/r/dgtlmoon/changedetection.io
 - Update screenshot

0.11 / 2021-01-29 10:49:05 +0100:
 - Add more start-up examples
 - Tweak theming
 - Use a even simpler run command
 - improve the wording
 - Add basic settings page (so far just recheck time in minutes)
 - Updating README
 - Updating screenshot (new diff button)
 - Trigger write index after edit of a watch
 - Add [diff] mechanism
 - Use a single thread for writing the sync json
 - Use existing tag
 - When all items showed, show which tag it belongs to
 - Sort tag list
 - Set active tag selection
 - Support for comma separated tags
 - Tweak styling for 'new watch' form
 - Remove import for old lib
 - Switch to inscriptis prepare config backend struct
 - Support for custom headers per watch
 - Going back to larger PNG screenshot, looks better in Github :)
 - Fix alt text in markup
 - Adding new screenshot binary
 - Updating screenshot
 - Moving start text to a more visible part
 - Tweak messages
 - Change message text
 - Fixing messages styling
 - Basic tag browse buttons
 - Bulk import
 - Tidy up 'last_checked' date handling
 - Dev environment setup
 - Dev docker tweaks
 - Remove messy text
 - Tweaking text
 - Fixing checkall hook
 - Use requests's r.text so we dont have to deal with charsets
 - Add note
 - Fix bad copy command
 - Oops left out the image name
 - Fix build setup for the docker hub image https://hub.docker.com/r/dgtlmoon/changedetection.io
 - Update screenshot

0.2 / 2021-02-01 10:24:29 +0100:
 - Add more start-up examples
 - Tweak theming
 - Use a even simpler run command
 - improve the wording
 - Add basic settings page (so far just recheck time in minutes)
 - Updating README
 - Updating screenshot (new diff button)
 - Trigger write index after edit of a watch
 - Add [diff] mechanism
 - Use a single thread for writing the sync json
 - Use existing tag
 - When all items showed, show which tag it belongs to
 - Sort tag list
 - Set active tag selection
 - Support for comma separated tags
 - Tweak styling for 'new watch' form
 - Remove import for old lib
 - Switch to inscriptis prepare config backend struct
 - Support for custom headers per watch
 - Going back to larger PNG screenshot, looks better in Github :)
 - Fix alt text in markup
 - Adding new screenshot binary
 - Updating screenshot
 - Moving start text to a more visible part
 - Tweak messages
 - Change message text
 - Fixing messages styling
 - Basic tag browse buttons
 - Bulk import
 - Tidy up 'last_checked' date handling
 - Dev environment setup
 - Dev docker tweaks
 - Remove messy text
 - Tweaking text
 - Fixing checkall hook
 - Use requests's r.text so we dont have to deal with charsets
 - Add note
 - Fix bad copy command
 - Oops left out the image name
 - Fix build setup for the docker hub image https://hub.docker.com/r/dgtlmoon/changedetection.io
 - Update screenshot
 - Add edit UI Move to keyed structure instead of list
 - Fixes to CSS
 - Add method to launch a full recheck of all @note - needs to be converted to a python Queue threads
 - Tweaks to docker layout
 - Remove actual :// links, dont consider these as part of the changes, often they include variables/trackingscript ref etc
 - Create FUNDING.yml

0.1 / 2021-01-28 11:17:12 +0100:
 - Specify image name in docker files to avoid a confusing build/run
 - Tidy up devel docker
 - Tweak comments
 - Avoid recasting the type
 - Store a history of changes, used for future lookup/diff/explore changes UI
 - Update README.md
 - Show the backend error in the table if there is one
 - Include screenshot
 - Fix branch name
 - Tweak todo
 - Adding README amd docker info
 - Add missing file
 - Primitive support for extra headers
 - remove debug
 - Handle titles and links
 - Fix base definition of the watcher
 - sort by last changed
 - fix button size
 - Store the html2text version too
 - fix favicon
 - small fixes
 - Handle errors better, use the plaintext output
 - Workon threads
 - WIP
 - Remove nocache experimental
 - Initial commit

```