---
url: "https://docs.browserless.io/bql-schema/operations/mutations/pdf"
title: "pdf | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/pdf#__docusaurus_skipToContent_fallback)

On this page

Generates a PDF of the page with the print CSS media type

Example:

```codeBlockLines_p187
mutation PDF {
  goto(url: "https://example.com", waitUntil: firstMeaningfulPaint) {
    status
  }

  simple: pdf {
    base64
  }

  customArgs: pdf(
    format: a5
    displayHeaderFooter: true
    headerTemplate: "<span style=\"font-size: 16pt;\">Hello World</span>"
  ) {
    base64
  }
}

```

```codeBlockLines_p187
pdf(
  displayHeaderFooter: Boolean
  format: PDFPageFormat
  footerTemplate: String
  generateDocumentOutline: Boolean
  generateTaggedPDF: Boolean
  landscape: Boolean
  printBackground: Boolean
  scale: Float
  timeout: Float
  width: FloatOrString
  headerTemplate: String
  height: FloatOrString
  marginBottom: FloatOrString
  marginLeft: FloatOrString
  marginRight: FloatOrString
  marginTop: FloatOrString
  pageRanges: String
  preferCSSPageSize: Boolean
  transferMode: String
): PDFResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#arguments "Direct link to Arguments")

#### [`pdf.displayHeaderFooter`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfdisplayheaderfooterboolean- "Direct link to pdfdisplayheaderfooterboolean-")

Display header and footer. Defaults to false

#### [`pdf.format`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`PDFPageFormat`](https://docs.browserless.io/bql-schema/types/enums/pdfpage-format) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfformatpdfpageformat- "Direct link to pdfformatpdfpageformat-")

The page format to use for the PDF

#### [`pdf.footerTemplate`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdffootertemplatestring- "Direct link to pdffootertemplatestring-")

HTML template for the print footer. Should use the same format as the `headerTemplate`.

#### [`pdf.generateDocumentOutline`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfgeneratedocumentoutlineboolean- "Direct link to pdfgeneratedocumentoutlineboolean-")

Whether or not to embed the document outline into the PDF

#### [`pdf.generateTaggedPDF`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfgeneratetaggedpdfboolean- "Direct link to pdfgeneratetaggedpdfboolean-")

Whether or not to generate tagged (accessible) PDF. Defaults to embedded choice

#### [`pdf.landscape`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdflandscapeboolean- "Direct link to pdflandscapeboolean-")

Paper orientation. Defaults to false

#### [`pdf.printBackground`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfprintbackgroundboolean- "Direct link to pdfprintbackgroundboolean-")

Print background graphics. Defaults to false

#### [`pdf.scale`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfscalefloat- "Direct link to pdfscalefloat-")

Scale of the webpage rendering. Defaults to 1

#### [`pdf.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdftimeoutfloat- "Direct link to pdftimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the PDF to be generated. Default timeout is 30 seconds, or 30000.

#### [`pdf.width`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`FloatOrString`](https://docs.browserless.io/bql-schema/types/scalars/float-or-string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfwidthfloatorstring- "Direct link to pdfwidthfloatorstring-")

Width in inches or CSS unit. Defaults to 8.5 inches

#### [`pdf.headerTemplate`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfheadertemplatestring- "Direct link to pdfheadertemplatestring-")

HTML template for the print header. Should be valid HTML markup with following
classes used to inject printing values into them:

- `date`: formatted print date
- `title`: document title
- `url`: document location
- `pageNumber`: current page number
- `totalPages`: total pages in the document

For example, `<span class=title></span>` would generate span containing the title

#### [`pdf.height`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`FloatOrString`](https://docs.browserless.io/bql-schema/types/scalars/float-or-string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfheightfloatorstring- "Direct link to pdfheightfloatorstring-")

Height in inches or CSS unit. Defaults to 11 inches

#### [`pdf.marginBottom`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`FloatOrString`](https://docs.browserless.io/bql-schema/types/scalars/float-or-string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfmarginbottomfloatorstring- "Direct link to pdfmarginbottomfloatorstring-")

Bottom margin in inches or CSS unit. Defaults to 1cm (~0.4 inches).

#### [`pdf.marginLeft`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`FloatOrString`](https://docs.browserless.io/bql-schema/types/scalars/float-or-string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfmarginleftfloatorstring- "Direct link to pdfmarginleftfloatorstring-")

Left margin in inches or CSS unit. Defaults to 1cm (~0.4 inches).

#### [`pdf.marginRight`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`FloatOrString`](https://docs.browserless.io/bql-schema/types/scalars/float-or-string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfmarginrightfloatorstring- "Direct link to pdfmarginrightfloatorstring-")

Right margin in inches or CSS unit. Defaults to 1cm (~0.4 inches).

#### [`pdf.marginTop`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`FloatOrString`](https://docs.browserless.io/bql-schema/types/scalars/float-or-string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfmargintopfloatorstring- "Direct link to pdfmargintopfloatorstring-")

Top margin in inches or CSS unit. Defaults to 1cm (~0.4 inches).

#### [`pdf.pageRanges`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfpagerangesstring- "Direct link to pdfpagerangesstring-")

Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are
printed in the document order, not in the order specified, and no
more than once. Defaults to empty string, which implies the entire document is printed.
The page numbers are quietly capped to actual page count of the
document, and ranges beyond the end of the document are ignored.
If this results in no pages to print, an error is reported.
It is an error to specify a range with start greater than end

#### [`pdf.preferCSSPageSize`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfprefercsspagesizeboolean- "Direct link to pdfprefercsspagesizeboolean-")

Whether or not to prefer page size as defined by css. Defaults to false,
in which case the content will be scaled to fit the paper size

#### [`pdf.transferMode`](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdftransfermodestring- "Direct link to pdftransfermodestring-")

Return as stream (PrintToPDFRequestTransferMode enum)

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#type "Direct link to Type")

#### [`PDFResponse`](https://docs.browserless.io/bql-schema/types/objects/pdfresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/pdf\#pdfresponse- "Direct link to pdfresponse-")

The response returned after generating a PDF

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/pdf#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/pdf#type)