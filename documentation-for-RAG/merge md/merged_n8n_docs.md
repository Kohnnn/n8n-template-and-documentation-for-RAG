Run this script to merge documentation:

powershell -ExecutionPolicy Bypass -File .\merge_docs.ps1

Some documentation index is way too large for llms so break it down to equal chunk or use embbeding to codebase for better RAG retrival