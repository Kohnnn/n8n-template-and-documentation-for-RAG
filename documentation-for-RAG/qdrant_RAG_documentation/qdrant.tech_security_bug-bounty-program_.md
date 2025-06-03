---
url: "https://qdrant.tech/security/bug-bounty-program/"
title: "Bug Bounty Program - Qdrant"
---

# Bug Bounty Program Overview

We prioritize user trust and adhere to the highest privacy and security standards. This is why we actively invite security experts to identify vulnerabilities and commit to collaborating with them to resolve issues swiftly and effectively.
Qdrant values the security research community and supports the responsible disclosure of vulnerabilities in our products and services. Through our bug bounty program, we reward researchers who help enhance the security of our platform.

## Responsible Disclosure Program Rules

- Include detailed, reproducible steps in your reports. We will not reward issues you cannot reproduce.
- Submit one vulnerability per report unless you need to chain multiple vulnerabilities to demonstrate impact.
- In cases of duplicate reports, we will reward only the first reproducible report.
- We will consider vulnerabilities stemming from the same root cause as a single issue and award only one bounty.
- We strictly prohibit social engineering attacks (e.g., phishing, vishing, smishing).
- Interact only with accounts you own or have explicit permission to access. Do not test using Qdrant employee accounts or internal tools.
- Before you run automated scanners, please check with us first.

### In Scope

The Bug Bounty program covers the following areas:

- \*.cloud.qdrant.io Qdrant Cloud Application
- [qdrant.tech](http://qdrant.tech/) Website

In most cases, we will only reward the following types of vulnerabilities:

- Arbitrary code execution and OS Command Injection
- Stored Cross-Site Scripting (Stored XSS)
- SQL injection
- File Upload
- Authentication bypass and privilege escalation (authentication / authorization circumvention)
- Significant Sensitive Data Exposure
- Server-Side Request Forgery (SSRF)
- Critical Business Logic Flaws

### Out of Scope

We always exclude the following areas:

- Findings related to intended functionality or accepted business risks
- Qdrant support system on [https://support.qdrant.io](https://support.qdrant.io/)
- Third-party applications or websites
- Staging or test environments
- Social engineering attacks
- DoS/DDoS attacks
- User/email enumeration
- Brute-force attacks
- Physical security issues
- Reports from automated tools or scanners
- Generic information disclosure, such as the `Server` or `X-Powered-By` headers
- Email security: DMARC, DKIM, SPF, etc.
- Spamming that rate limiting techniques can prevent
- Missing DNSSEC
- CSRF for Login, Logout and Signup pages
- Cross-site scripting that requires full control of a http header, such as Referer, Host etc.
- Clickjacking and Tabnabbing

## Severity Levels and Rewards

- We assess reported bugs based on their risk and other relevant factors; our response may take some time.
- We tend to award higher rewards for submissions that include detailed remediation steps or recommendations.
- We determine bounty amounts based on multiple factors, including the vulnerability’s impact, the ease of exploitation, and the quality of the report. Please note that we may not award a bounty for very low-risk issues.
- We use the CVSS v4 framework to evaluate the criticality of issues and ensure a consistent risk assessment.
- We aim to reward similar vulnerabilities with comparable compensation; however, we also consider factors such as the time and effort required to discover the issue. Keep in mind that we may not match previous compensations for future reports.

## Disclosure Policy

Contact us at [security@qdrant.com](mailto:security@qdrant.com) to report vulnerabilities. Our security team will provide an initial response within 5 business days and triage the issue within 5-7 business days. We vary fix implementation timelines based on severity, and we process bounty payments after verifying the fix.

Follow these guidelines when disclosing vulnerabilities to us:

- Report any potential security vulnerabilities immediately upon discovery, as we commit to resolving issues swiftly.
- Maintain strict confidentiality regarding discovered vulnerabilities. Obtain explicit authorization from the Qdrant security team before publicly disclosing any vulnerabilities.
- Exercise caution to prevent data loss, privacy breaches, or service disruptions while conducting security research.
- Limit testing to your own accounts or those for which you have received explicit permission. Report any accidental access to unauthorized data immediately.
- **Safe Harbor:** We support ethical security research and promise not to initiate legal action against researchers who report vulnerabilities in good faith and comply with this disclosure policy. Ensure that your testing remains non-disruptive and respects the outlined guidelines so you qualify for Safe Harbor protections.

### Contact

For questions about the program or to report security issues, contact:

- Email: [security@qdrant.com](mailto:security@qdrant.com)
- PGP Key Fingerprint: [07E3 6646 E0D0 A3BF 0AFC B302 26C5 016B 97EB 804B](https://qdrant.tech/misc/qdrant-security-public-key.asc)

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