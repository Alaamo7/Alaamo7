---
name: rag-pipeline
status: restored
description: Design retrieval-augmented generation pipelines covering ingestion, indexing, retrieval, grounding, citation, refresh, and quality control with explicit provenance and verification.
---

# RAG Pipeline Skill

Use this skill to design or review a retrieval-augmented generation workflow that answers from trusted knowledge rather than model memory alone.

## Pipeline

```text
Source discovery
  ↓
Document ingestion
  ↓
Normalization + metadata
  ↓
Chunking
  ↓
Indexing / embeddings
  ↓
Query understanding
  ↓
Retrieval
  ↓
Ranking / filtering
  ↓
Grounded generation
  ↓
Citations
  ↓
Answer verification
  ↓
Feedback + refresh
```

## Core rules

1. Preserve source identity and provenance through the entire pipeline.
2. Retrieval quality is not measured only by semantic similarity.
3. Prefer authoritative and current sources when the domain requires freshness.
4. Do not generate unsupported factual claims when evidence is insufficient.
5. Keep retrieved context bounded and task-relevant.
6. Distinguish source truth from model synthesis.

## Design checklist

Define:

- Source systems
- Document formats
- Metadata schema
- Chunk strategy
- Embedding/index strategy
- Retrieval method
- Ranking/filtering rules
- Context budget
- Citation format
- Freshness policy
- Quality metrics
- Failure behavior

## Retrieval methods

Possible approaches:

- Dense semantic retrieval
- Keyword/BM25 retrieval
- Hybrid retrieval
- Metadata filtering
- Reranking
- Query decomposition
- Multi-query retrieval

Choose based on corpus shape and task requirements rather than defaulting to a single technique.

## Failure modes

Watch for:

- Missing relevant source
- Stale source
- Poor chunk boundaries
- Duplicate chunks
- Similar but wrong document
- Over-retrieval
- Citation mismatch
- Unsupported synthesis
- Metadata loss
- Retrieval dominated by low-authority content

## Verification

A RAG answer should be reviewable against retrieved evidence. If the evidence does not support the claim, mark the answer incomplete or retrieve again rather than guessing.
