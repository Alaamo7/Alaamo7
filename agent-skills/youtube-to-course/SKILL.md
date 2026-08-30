---
name: youtube-to-course
status: restored
description: Convert a YouTube video, playlist, transcript, or other long-form educational video source into a structured course with modules, lessons, learning objectives, examples, exercises, quizzes, summaries, and a final project. Use only content the user is authorized to access and do not invent missing source material.
---

# YouTube to Course Skill

Turn long-form video content into a teachable course instead of producing a loose summary.

## Core rules

1. Use only authorized source material.
2. Preserve the source meaning; do not invent facts or quotations.
3. Separate source-derived material from added teaching examples or exercises.
4. Do not claim a video was watched or transcribed unless the source was actually accessed.
5. Keep timestamps or source references when available so important claims remain traceable.
6. Prefer learning progression over mirroring the raw video order when restructuring improves understanding.

## Workflow

### 1. Source intake

Collect available inputs:

- Video/playlist title
- Transcript or captions
- Description and chapters
- Supporting files or links
- Target audience
- Desired course level
- Target duration
- Output format

### 2. Source map

Identify:

- Main topic
- Prerequisites
- Core concepts
- Demonstrations
- Examples
- Repeated ideas
- Missing context
- Claims that require external verification

### 3. Course architecture

Create:

- Course title
- Audience level
- Learning outcomes
- Prerequisites
- Modules
- Lessons per module
- Estimated lesson duration
- Practice activities
- Quiz checkpoints
- Final project

### 4. Lesson conversion

Each lesson should contain:

1. Lesson objective
2. Why it matters
3. Core explanation
4. Example or demonstration
5. Common mistake
6. Practice task
7. Recap
8. Optional quiz
9. Source references/timestamps when available

## Content compression

Remove:

- Repetition
- Filler
- Off-topic conversation
- Sponsor segments unless relevant
- Duplicate examples

Keep:

- Definitions
- Processes
- Important caveats
- Demonstrations
- Real examples
- Source-specific insights

## Exercise generation

Exercises may be newly created for teaching value, but clearly treat them as course activities rather than source claims.

Use a progression such as:

- Recall
- Explain
- Apply
- Diagnose
- Build

## Quiz generation

For each module, generate a short quiz when useful:

- Multiple choice
- True/false only when the statement is unambiguous
- Short-answer questions
- Scenario questions

Always provide an answer key separately.

## Final project

The project should combine the major course outcomes. Include:

- Goal
- Scenario
- Required deliverables
- Constraints
- Evaluation criteria
- Optional stretch goals

## Output structure

```markdown
# Course Title

## Course Overview
- Audience:
- Level:
- Prerequisites:
- Estimated duration:

## Learning Outcomes
1. ...

## Module 1 — ...
### Lesson 1.1 — ...
- Objective:
- Explanation:
- Example:
- Practice:
- Recap:
- Source reference:

## Module Quiz
...

## Final Project
...
```

## Verification checklist

Before delivery verify:

- Course claims are source-backed or clearly labeled as added teaching material.
- No important caveat from the source was removed.
- Module order is pedagogically coherent.
- Learning outcomes match the lessons.
- Exercises are actually solvable from the taught material.
- The final project does not require knowledge never introduced in the course.
