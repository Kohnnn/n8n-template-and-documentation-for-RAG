---
url: "https://supabase.com/features/image-transformations"
title: "Image transformations | Supabase Features"
---

[Previous feature](https://supabase.com/features/foreign-key-selector) [Next feature](https://supabase.com/features/log-drains)

Stage:

General Availability

Available on self-hosted:

Yes

Supabase’s Image Transformations feature enables developers to dynamically manipulate images stored in Supabase Storage. This functionality is ideal for applications requiring responsive design, efficient media delivery, and streamlined image management.

## Key features

1. Dynamic resizing: Adjust image dimensions using width and height parameters to suit various display requirements.
2. Quality control: Set image quality on a scale from 20 to 100 to balance visual fidelity and file size.
3. Resize modes: Choose from ‘cover’, ‘contain’, or ‘fill’ to control how images fit within specified dimensions.
4. Automatic format optimization: Automatically convert images to WebP format for supported browsers, enhancing load times and reducing bandwidth usage.
5. Flexible implementation: Utilize with public URLs, signed URLs, or direct downloads to fit various access control needs ( [Server-side Auth](https://supabase.com/features/server-side-auth)).
6. [Next.js integration](https://supabase.com/nextjs): Leverage a custom loader for optimized image handling in Next.js applications.
7. Self-hosting option: Deploy your own image transformation service using Imgproxy for greater control and customization.

## Benefits:

- Performance optimization: Reduce bandwidth usage and improve load times with optimized images.
- Storage efficiency: Store a single high-quality version and generate variants as needed.
- Responsive design support: Serve appropriately sized images for different devices and layouts.
- Simplified workflow: Automate image processing tasks, reducing the need for manual intervention and third-party tools.

## Image transformations are valuable for:

- Responsive web applications: Deliver images optimized for various screen sizes and resolutions.
- Ecommerce platforms: Showcase product images in multiple sizes without storing redundant files.
- Content management systems (CMS): Adapt images for different layouts and templates dynamically.
- Mobile applications: Optimize images for devices with varying bandwidth and display capabilities.
- High-volume image handling: Efficiently manage and serve large quantities of images in diverse contexts with [resumable uploads](https://supabase.com/features/resumable-uploads).

Supabase's Image Transformations feature enables you to efficiently manage and serve optimized images, improving your application's performance and user experience while saving time and resources.

## Integration capabilities

Supabase’s Image Transformations seamlessly integrate within its ecosystem and with external tools:

- Supabase Storage: Directly apply transformations to images stored in Supabase buckets, streamlining media management.
- Next.js compatibility: Utilize a custom loader to integrate image transformations within Next.js applications, enhancing performance and user experience.
- Self-hosting with Imgproxy: Deploy your own image transformation service using Imgproxy, offering greater control and customization options.
- API access: Leverage RESTful APIs to programmatically apply transformations, enabling automation and integration with various workflows.

These integration options provide flexibility, allowing developers to tailor image transformation processes to their specific project requirements.
For a deeper understanding and step-by-step guidance on using Image Transformations, please refer to our [documentation](https://supabase.com/docs/guides/storage/image-transformations).

## FAQs about image transformations with Supabase

Below are answers to common questions about Supabase Image Transformations.

### What image formats are supported by Supabase Image Transformations?

Supabase Image Transformations primarily support common web-friendly formats such as JPEG, PNG, and WebP. When using the automatic format optimization feature, images can be converted to WebP for supported browsers to enhance performance.

### Can I apply multiple transformations to a single image request?

Yes, you can chain multiple transformation parameters in a single request. For example, you can resize an image and adjust its quality simultaneously by specifying the appropriate query parameters in the image URL.

### How do I implement transformations in my Next.js application?

Supabase provides a custom loader for Next.js, allowing seamless integration of Image Transformations. By configuring the loader, you can optimize images on-the-fly within your Next.js project.

### Are there any limitations on image size or dimensions?

While Supabase does not impose strict limits on image sizes, it’s recommended to optimize images for web use to ensure faster load times and better performance. Large images may consume more bandwidth and affect loading speeds.

### How does automatic format optimization work?

Automatic format optimization detects the capabilities of the user’s browser and serves the most efficient image format supported, such as WebP. This enhances loading times and reduces bandwidth usage without compromising image quality.

[Read Documentation](https://supabase.com/docs/guides/storage/image-transformations)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fimage-transformations&text=Image%20transformations%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fimage-transformations&text=Image%20transformations%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fimage-transformations&t=Image%20transformations%20%7C%20Supabase%20Features)

[Foreign Key Selector](https://supabase.com/features/foreign-key-selector) [Log Drains](https://supabase.com/features/log-drains)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)