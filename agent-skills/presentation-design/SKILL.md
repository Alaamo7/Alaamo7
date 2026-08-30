---
name: presentation-design
name_ar: مهارة تصميم العروض التقديمية التعليمية
version: 1.0.0
description: إرشادات عملية لإنشاء عروض تقديمية احترافية للدروس والكورسات، خاصة المحتوى التقني مثل التحليل الفني وPine Script وIT. تستخدم عند تصميم Slide Deck أو Slide Plan أو تحويل درس مكتوب إلى عرض تقديمي جذاب ومنظم.
---

# Presentation Design Skill

حوّل أي درس أو سكريبت أو محتوى تعليمي إلى عرض واضح، منظم، وقابل للتدريس أو التسجيل على OBS أو النشر على YouTube.

## المبادئ الأساسية

1. **فكرة واحدة لكل سلايد.**
2. **الوضوح قبل الجمال.** لا تجعل التصميم يطغى على الفكرة.
3. **التسلسل التعليمي:** لماذا الموضوع مهم → المفهوم → كيف يعمل → مثال → خطأ شائع → ملخص → تمرين.
4. **الشرح التفصيلي في Speaker Notes، وليس داخل السلايد.**
5. كل عنصر بصري يجب أن يشرح أو يوضح أو ينظم.

## الهيكل الافتراضي للدرس

1. Cover
2. Why this matters
3. Learning objectives
4. Core concepts
5. Visual/practical examples
6. Practical demo
7. Common mistakes
8. Recap
9. Exercise or task
10. Transition to the next lesson when relevant

## أنواع الشرائح

- **Concept Slide** — مفهوم واحد وتعريف مختصر ومثال.
- **Comparison Slide** — مقارنة بين مفهومين أو أكثر.
- **Process Slide** — خطوات أو Workflow.
- **Code Slide** — كود قصير ومقروء، مع إبراز الجزء المهم.
- **Chart Slide** — شارت بسيط ونقطة تركيز واضحة.
- **Recap Slide** — أهم الأفكار وسؤال مراجعة.

## قواعد الكتابة

- استخدم عناوين تخبر الطالب بالفكرة مباشرة.
- لا تزيد النقطة عن سطر واحد إن أمكن.
- لا تضع أكثر من 5 نقاط في السلايد غالبًا.
- تجنب الفقرات الطويلة.
- عند وجود كود، اعرض جزءًا واحدًا في كل مرة، ويفضل ألا يتجاوز 12–18 سطرًا في السلايد.

## RTL والمحتوى العربي

- المحاذاة من اليمين.
- اتجاه القراءة RTL.
- المصطلحات التقنية الإنجليزية تبقى بصيغتها الرسمية عند الحاجة.
- اعزل الكود والمصطلحات الإنجليزية بصريًا لتجنب مشاكل الاتجاه.

## عروض البرمجة وPine Script

كل درس برمجي يجب أن يحتوي غالبًا على:

- فكرة الكود
- الكود
- شرح السطور المهمة
- النتيجة على الشاشة
- خطأ شائع
- تمرين صغير

لـPine Script استخدم أسلوبًا تقنيًا واضحًا مع code blocks وcandlestick charts وواجهات شبيهة بـTradingView عند الحاجة، وتجنب الزحمة والمؤشرات الكثيرة.

## عروض IT والشبكات

كل درس IT يفضل أن يحتوي على:

- المشكلة الواقعية
- المفهوم النظري
- Diagram
- خطوات التطبيق
- Commands أو Settings
- Troubleshooting
- ملخص عملي

## الصور والمرئيات

- استخدم نفس نمط الأيقونات طوال العرض.
- لا تخلط أنماطًا بصرية متعارضة بدون سبب.
- لا تستخدم صورة عشوائية لا تخدم الشرح.
- استخدم Flowcharts وNetwork Diagrams وBefore/After وAnnotated Screenshots عند الحاجة.

## الحركة والانتقالات

استخدم الحركة بحذر:

- Fade
- Appear
- Morph عند شرح تطور شكل أو عملية

تجنب الحركات الاستعراضية التي تشتت الانتباه.

## قالب Slide Plan

```markdown
# Slide Plan — [Lesson Title]

## Lesson Info
- Course:
- Unit:
- Lesson:
- Duration:
- Audience:
- Visual Style:

## Learning Objectives
1. ...
2. ...
3. ...

## Slide 1 — Cover
- Purpose:
- Visual:
- On-slide text:
- Speaker notes:

## Slide 2 — Why This Matters
- Purpose:
- Visual:
- On-slide text:
- Speaker notes:
```

كرر نفس النموذج لكل الشرائح.

## قالب السلايد الواحد

```markdown
## Slide [Number]: [Title]

**Purpose:**
...

**Layout:**
Full image / Two columns / Comparison / Process / Code / Chart

**On-slide Text:**
- ...

**Visual Direction:**
...

**Speaker Notes:**
...

**Design Notes:**
...
```

## Checklist قبل التسليم

- فكرة واحدة لكل سلايد.
- النصوص مختصرة.
- الخط واضح على شاشة صغيرة.
- الألوان متناسقة.
- RTL سليم.
- الكود قابل للقراءة.
- الشارتات غير مزدحمة.
- يوجد ملخص وتطبيق.
- الهوية البصرية موحدة.
- العرض مناسب للتسجيل بالفيديو.

## Output formats

يمكن استخدام المهارة لإنتاج:

- Slide Plan Markdown
- PowerPoint/PPTX
- Google Slides structure
- Notion presentation page
- Speaker Notes
- Visual prompts
- OBS teaching scenario

## Naming convention

```text
CourseName_UnitXX_LessonXX_SlidePlan.md
CourseName_UnitXX_LessonXX_Presentation.pptx
CourseName_UnitXX_LessonXX_SpeakerNotes.md
CourseName_VisualStyleGuide.md
```
