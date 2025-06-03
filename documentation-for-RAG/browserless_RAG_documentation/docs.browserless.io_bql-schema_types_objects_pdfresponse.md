---
url: "https://docs.browserless.io/bql-schema/types/objects/pdfresponse"
title: "PDFResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/pdfresponse#__docusaurus_skipToContent_fallback)

On this page

The response returned after generating a PDF

```codeBlockLines_p187
type PDFResponse {
  base64: String
  size: Float
  time: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#fields "Direct link to Fields")

#### [`PDFResponse.base64`](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#pdfresponsebase64string- "Direct link to pdfresponsebase64string-")

Base64 encoded PDF content

#### [`PDFResponse.size`](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#pdfresponsesizefloat- "Direct link to pdfresponsesizefloat-")

The size of the resulting PDF in bytes

#### [`PDFResponse.time`](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#pdfresponsetimefloat- "Direct link to pdfresponsetimefloat-")

The time it took to generate the PDF

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/pdfresponse\#returned-by "Direct link to Returned By")

[`pdf`](https://docs.browserless.io/bql-schema/operations/mutations/pdf) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/pdfresponse#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/pdfresponse#returned-by)