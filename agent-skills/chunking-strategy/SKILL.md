---
name: chunking-strategy
status: restored
description: Design chunking strategies for retrieval systems that preserve semantic coherence, document structure, source references, and useful overlap without bloating context.
---

# Chunking Strategy Skill

Use this skill to split documents into retrieval units that are coherent enough to answer questions while remaining small enough for precise retrieval.

## Core principles

1. Chunk by meaning and structure, not character count alone.
2. Preserve section/page/source identifiers.
3. Keep tables, code blocks, procedures, and lists intact when possible.
4. Use overlap only where it materially protects context continuity.
5. Avoid chunks so large that retrieval becomes vague or so small that meaning is lost.

## Strategy options

- Heading/section-aware chunks
- Paragraph-aware chunks
- Sliding windows
- Semantic segmentation
- Code/function-aware chunks
- Table-aware chunks
- Conversation/message-aware chunks

## Selection factors

Consider:

- Document type
- Query style
- Average answer granularity
- Embedding model limits
- Reranker behavior
- Citation requirements
- Expected context budget

## Validation

Test chunk quality using representative queries. Inspect whether the returned chunk contains enough context to support the intended answer and whether important context is split across boundaries unnecessarily.
