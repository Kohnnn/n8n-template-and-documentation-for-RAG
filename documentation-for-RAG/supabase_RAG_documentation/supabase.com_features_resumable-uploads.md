---
url: "https://supabase.com/features/resumable-uploads"
title: "Resumable uploads | Supabase Features"
---

[Previous feature](https://supabase.com/features/reports-and-metrics) [Next feature](https://supabase.com/features/role-based-access-control)

Stage:

General Availability

Available on self-hosted:

Yes

Supabase's Resumable Uploads feature enables reliable transfer of large files, allowing uploads to be paused and resumed, particularly useful for files exceeding 6MB or in unstable network conditions.

## Key features

1. TUS protocol implementation: Utilizes the open protocol for resumable uploads.
2. Progress tracking: Provides upload progress events for better user feedback.
3. Chunk-based uploads: Uses 6MB chunks for efficient transfer and resumption.
4. Retry mechanism: Implements automatic retries with customizable delay intervals.
5. Metadata support: Allows setting of bucket name, object name, content type, and cache control.
6. Upsert option: Provides the ability to overwrite existing files if needed.
7. Flexible integration: Compatible with tus-js-client and other TUS-supporting libraries like Uppy.

## Benefits:

- Reliability: Successfully upload large files even with unstable internet connections.
- User experience: Allow users to pause and resume uploads at their convenience.
- Bandwidth efficiency: Avoid re-uploading already transferred parts of a file after an interruption.
- Large file support: Confidently handle uploads of very large files without worrying about timeouts.

## Resumable uploads are valuable for:

- Cloud storage applications handling large file transfers
- Video sharing platforms dealing with high-quality video uploads
- Backup and sync services ensuring data integrity during transfers
- Content creation tools handling large media files
- Any application where users need to upload sizeable files in potentially unstable conditions

Supabase's Resumable Uploads feature significantly improves the reliability and user experience of file uploads, especially for large files or in scenarios with unpredictable network conditions.

[Read Documentation](https://supabase.com/docs/guides/storage/uploads/resumable-uploads)

Share

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fresumable-uploads&text=Resumable%20uploads%20%7C%20Supabase%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fresumable-uploads&text=Resumable%20uploads%20%7C%20Supabase%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Ffeatures%2Fresumable-uploads&t=Resumable%20uploads%20%7C%20Supabase%20Features)

[Reports & Metrics](https://supabase.com/features/reports-and-metrics) [Role-Based Access Control (RBAC)](https://supabase.com/features/role-based-access-control)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)