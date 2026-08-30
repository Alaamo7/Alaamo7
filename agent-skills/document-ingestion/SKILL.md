---
name: document-ingestion
status: restored
description: Ingest documents into an AI knowledge system while preserving source identity, structure, metadata, permissions, extraction quality, and duplicate detection.
---

# Document Ingestion Skill

Use this skill to bring PDFs, docs, notes, web pages, spreadsheets, and other knowledge sources into a retrieval system safely and consistently.

## Workflow

```text
Discover source
  ↓
Validate access and permissions
  ↓
Identify format
  ↓
Extract text/structure
  ↓
Normalize encoding/layout
  ↓
Attach metadata
  ↓
Detect duplicates/versions
  ↓
Run quality checks
  ↓
Hand off to chunking/indexing
```

## Required metadata

Preserve when available:

- Source title
- Source URI/path
- Author/owner
- Creation/update date
- Version/revision
- Page/section identifiers
- Document type
- Language
- Access classification
- Ingestion timestamp

## Quality controls

Check for:

- Empty extraction
- Broken character encoding
- Missing pages/sections
- Table flattening errors
- Header/footer noise
- Duplicate content
- OCR errors when OCR was required
- Lost source references

## Permissions

Do not ingest content into a shared index when source permissions would not allow downstream users to access it.

## Output

Each ingested item should include content, provenance, structural markers, metadata, and an explicit quality status.