---
name: ai-video-creator
status: restored
description: Convert an idea, lesson, article, or brief into a production-ready video workflow including concept, script, storyboard, shot plan, visual prompts, voiceover guidance, recording plan, edit plan, QA, and publishing assets.
---

# AI Video Creator Skill

Transform content into a complete video production plan rather than only generating a script.

## Core rules

1. Define the audience, platform, goal, duration, and format before production planning.
2. Keep factual claims traceable to authorized sources.
3. Separate narration, on-screen text, visuals, B-roll, screen recording, and editing instructions.
4. Do not invent screenshots, demonstrations, or product behavior that has not been verified.
5. Optimize for clarity and pacing, not maximum visual effects.
6. Respect copyright and licensing constraints for media assets.

## Workflow

### 1. Creative brief

Determine:

- Topic
- Audience
- Video objective
- Platform
- Target duration
- Aspect ratio
- Tone
- Presenter/no-presenter format
- Available assets
- Required tools

### 2. Story structure

Use an appropriate structure such as:

`Hook → Problem → Explanation → Demonstration → Result → Recap → CTA`

For educational content:

`Why it matters → Concept → Example → Demo → Common mistake → Exercise → Recap`

### 3. Script

Write the spoken script with:

- Natural narration
- Short sentences
- Clear transitions
- Technical terms explained when first introduced
- Visual cues embedded separately from narration

Do not overload the spoken script with text that should appear on screen.

### 4. Storyboard

For each scene provide:

```markdown
## Scene [Number]
- Duration:
- Narration:
- On-screen text:
- Main visual:
- B-roll / screen recording:
- Camera / framing:
- Transition:
- Audio notes:
```

### 5. Visual prompts

When generative visuals are needed, define:

- Subject
- Environment
- Composition
- Camera/framing
- Lighting
- Style
- Aspect ratio
- Important exclusions

Keep recurring characters, interfaces, and brand elements consistent across scenes.

### 6. Recording plan

For presenter-led or tutorial videos, specify:

- Camera/mobile position
- Lighting
- Microphone source
- OBS scene structure when relevant
- Screen resolution
- Cursor/highlight behavior
- Retake markers

### 7. Editing plan

Include:

- Rough-cut order
- Dead-air removal
- Jump-cut policy
- Screen zooms/callouts
- Captions/subtitles
- Music only when useful
- SFX only when useful
- Intro/outro policy
- Loudness consistency
- Export settings appropriate to the platform

### 8. Quality assurance

Verify:

- Hook matches the video's actual content.
- No unsupported factual claim remains.
- On-screen text is readable on mobile.
- Visuals match narration timing.
- Demonstrations are technically accurate.
- Audio is intelligible and consistent.
- Captions reflect the spoken words.
- The video delivers the promised outcome.

## Output package

Depending on the request, produce:

- Creative brief
- Final script
- Scene-by-scene storyboard
- Visual-generation prompts
- Screen-recording plan
- OBS scene plan
- Voiceover instructions
- Editing checklist
- Thumbnail concept
- Title/description ideas
- Chapter markers
- Subtitle/transcript plan

## Naming convention

```text
ProjectName_Brief.md
ProjectName_Script.md
ProjectName_Storyboard.md
ProjectName_VisualPrompts.md
ProjectName_EditPlan.md
ProjectName_QA.md
```
