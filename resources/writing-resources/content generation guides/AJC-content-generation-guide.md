title: "AJ Crabill / ESB — Content Generation Guide for Book-Length and Long-Form Content" type: content-guide author: AJ Crabill (via Loriah) updated: 2026-07-10

AJ Crabill / ESB — Content Generation Guide for Book-Length and Long-Form Content

Read by: Loriah (AI content generation system — the intelligence layer between AJ's intent and finished deliverables) Purpose: Complete operational guide for generating, reviewing, and publishing book-length and long-form ESB content (book chapters, full books, workbooks, guidance docs, newsletter articles, and blog posts). This document is authoritative. Do not guess; consult this guide at every step.

This guide is designed to sit alongside the site-specific content guides in the canonical folder. Those guides govern weekly/short-form pipeline content. This guide governs everything longer than 2,500 words — anything that requires sustained argument, narrative arc, or systematic treatment of an ESB framework topic.

Table of Contents

LLM Configuration & Model Registry

Content Format Definitions

ESB Language, Terminology & Mechanics (Binding)

The Quality Measurement Framework

The Testing Regimen

Architecture by Format

Voice — AJ's Register by Format

ESB Glossary Cross-Reference Index

Anti-Slop — Calibrated for Book-Length Content

Quality Gates — The Screen (Pre-Release Checklist)

Council Review Architecture (Book-Length Only)

1. LLM Configuration & Model Registry

1.1 Model Roles

Books and book-length content require a more deliberate model assignment than short-form pipeline work. Define four fixed roles, each with a specific model assignment:

For best results, inject the ESB context document (esb-context-injection.md) into every drafting prompt. This document contains all ESB terminology, voice rules, banned words, and structural conventions — tested to lift models to 9.0+ quality.

Routing note: All four run through OpenRouter (provider: openrouter in config.yaml). No custom provider needed — the model slug is the ID.

1.2 When to Use What — Decision Table

1.3 Model Testing History

This section documents empirical results from the testing regimen (see Section 5). Updated as new configurations are tested.

2. Content Format Definitions

The ESB content ecosystem spans six formats, each with distinct length, voice, and structural requirements:

2.1 Guidance Doc (~2,500–4,000 words)

Purpose: Practical, standalone topic coverage that answers "how do we do this?" for ESB coaches, practitioners, and board members.

Canonical example: "Effective Agenda Design," "Effective Goal Monitoring"

Structure:

Title in "Effective [Topic] [Aspect]" pattern

No subtitle, no source-attribution line

Opens with the grounding "why" (school systems exist to improve student outcomes)

3–5 H2 sections, each a component of the topic

Ends by bringing it back to student outcomes

Voice: Guidance/webinar register — instructional and definitional. ~14–16 words/sentence. Second person ("your board"). "We recommend."

Production:

Draft: Sonnet 5 (single pass, ~5 min)

Review: Mechanical anti-slop scan + voice check

Output: ESB-formatted DOCX (0.5" margins, 18pt title, 14pt headers, 11pt body, single-spaced)

2.2 Newsletter Article (~400–800 words)

Purpose: Weekly Q&A or standalone article for the 9-site network.

Structure (Q&A): Reframe in first paragraph → direct answer → supporting reasoning → return to student outcomes. Structure (standalone): Open with an unexpected contradiction → develop → close.

Voice: Newsletter register — ~14 words/sentence. Second person, direct, 2–4 sentence paragraphs.

Production: Governed by the site-specific canonical guides. Not the primary subject of this document, but included for completeness — the quality measurement framework applies here too.

2.3 Blog Post (~800–2,500 words)

Purpose: Analysis or principle exploration. Longer than a newsletter, shorter than a book chapter. Medium-form content for ESB's owned channels.

Structure:

Hook paragraph naming the principle

3–5 H2 analytical sections

No citations (unlike EGB format)

Cross-sector where applicable

Voice: Analytical third-person for effective-boards.com; advisory second-person for ESB-owned channels.

Production:

Draft: Sonnet 5

Review: Anti-slop scan + site-voice check

Can be output as HTML body + YAML frontmatter (Jekyll-compatible) or straight markdown

2.4 Book Chapter (~3,000–8,000 words)

Purpose: A self-contained unit of argument within a longer book. Each chapter advances the book's thesis while being readable standalone.

Architecture (nonfiction, ESB register):

Opening move (match to register: story for persuasive, direct for definitional, pattern-recognition for taxonomy)

Body: advance the argument in sequential sections

Closing: bridge to next chapter + return to student outcomes

Architecture (book register): ~23 words/sentence. Story-led for persuasive chapters, direct for definitional ones.

Production:

Outline: GPT-5.6 Sol

Draft: Sonnet 5 (delegate_task per chapter, up to 3 in parallel)

Council review: Critic (structural) + Reader (persona) on 4-chapter sample

Anti-slop: full mechanical scan + manual targeted pass

2.5 Workbook (~8,500–10,000 words)

Purpose: Practical companion with tables, checklists, self-assessments, exercises. Bridges story-to-practice.

Structure:

Heavy tables (checklists, templates, self-assessments with 0–4 scoring)

Short imperative paragraphs

Every section has 2–4 tables minimum

Callout boxes (Coach's Tip, Common Pitfall, Red Flag)

Part One: chapter-by-chapter reflection/application

Part Two: framework reference templates

Part Three: action plans (90-day plan, workshop guide, book club guide)

Voice: Second-person practical facilitator ("you"), like a workshop leader. Not the fiction voice, not the author's professional voice — neutral teaching voice.

Production: Skip full Council pipeline. One pass of consistency check sufficient.

2.6 Full Book (~40,000–80,000 words)

Purpose: Complete book-length treatment. Subtypes:

Production (full pipeline):

PHASE 0: Input normalization (notes → idea graph → gap detection)

PHASE 1: Foundation (voice extraction → book architecture → thesis + outline)

PHASE 2: Chapter planning (per-chapter hook, sections, transitions, target word count)

PHASE 3: Drafting via delegate_task (Sonnet 5, up to 3 chapters at a time)

PHASE 4: Council revision loop (Critic + Reader scoring, revise to ≥ 9/10)

PHASE 5: Coherence check → anti-slop final pass → DOCX export

3. ESB Language, Terminology & Mechanics (Binding)

This section is binding for all generated content. Where anything below conflicts with older instructions in this guide or the site-specific guides, this section wins. The full standard is esb_writing_style_guide.md in the canonical guides folder.

3.1 The One Conviction

Write from one place: Student outcomes don't change until adult behaviors change. Every document reflects this, opens near it, and ends by bringing it home to students.

3.2 The Grounding Opener (Required for Guidance Docs)

Open by stating why school systems and school boards exist, then connect to the topic:

School systems exist to improve student outcomes. This is the only reason school systems exist. School boards, in pursuit of this singular purpose, exist to represent the vision and values of their community. This is the only reason school boards exist. To [do the topic], boards must...

Vary the wording, keep the move. The opening carries NO header — no "Why this document exists," no "Introduction." It sits right under the title as plain prose.

Openers by format:

Guidance doc: Grounding "why" (above)

Newsletter Q&A: The reframe IS the opener

Newsletter standalone: Unexpected contradiction

Book, persuasive chapter: True story → "I share this because it illustrates..."

Book, definitional chapter: Direct — precision is the hook

Book, taxonomy/archetype chapter: Pattern-recognition hook → work each type

3.3 Mechanics

No em dashes. Use -- (spaced double-hyphen), sparingly, or split the sentence.

No en dashes. Use a hyphen (including in ranges like "1-2").

No semicolons in body prose. Use a period.

No ellipses. No exclamation marks (at most one per ~4,000 words).

Straight quotes only. Never curly/smart quotes.

Oxford comma always in lists of three or more.

Contractions where natural ("it's," "doesn't," "you'll").

Capitalize after a colon when it introduces a complete sentence; lowercase for a list fragment.

Sentence-initial "But," "And," "So" are fine and characteristic.

No italics for emphasis. Carry emphasis with sentence structure and word choice.

No horizontal rules (---) anywhere.

3.4 ESB Vocabulary (Never Policy Governance Terms)

Never describe ESB as built on or adopted from Policy Governance. It is grounded in "principles of a policy-based approach to governance."

Never write "SOFG," "Student Outcomes Focused Governance," "Policy Governance," "PG," "Lone Star Governance," or "LSG" — exception: SOFG only when intentionally contrasting with ESB.

Use "board chair," not "board president."

Use "Practitioner," not "coach," for the certified role.

Spell out "Any Reasonable Interpretation" — never "ARI."

Write "own conduct" as two words — never "own-conduct."

3.5 The Distinctions That Matter

Draw these cleanly. Missing them means it does not sound like AJ:

Adult inputs vs. student outcomes. Inputs are what adults invest; outcomes are what students know and can do.

Board work vs. superintendent work. The board governs (Goals and Guardrails, monitoring). The superintendent manages.

Monitoring vs. managing. The board monitors results after the fact. The superintendent manages the process.

Clarifying priorities vs. monitoring progress. First clarify, then monitor.

Project management vs. progress monitoring. PM tracks steps; PMo tracks results against Goals.

Listening vs. deciding. The community gives voice; the board gives judgment.

Issues vs. values. Issues are specific; values are durable commitments.

Pretraining vs. retraining. Pretraining sets up; retraining fixes drift.

Owners vs. customers. Same people, different roles by how they show up.

Goals vs. Guardrails vs. Initiatives. Goals = outcomes; Guardrails = boundaries; Initiatives = strategies.

Support vs. surrender. Board holds the what, superintendent holds the how.

3.6 Governance Language to Avoid

Never use these in ESB content. Describe the specific behavior instead:

"Micromanage / micromanaging" — reference board work vs. superintendent work.

"Rubberstamp / rubber stamp" — describe whether the board is exercising informed judgment.

"Stay in your lane" — reference governing policies or the board/supt distinction.

"Good / bad / right / wrong" as judgment — frame as effective vs. ineffective.

Power-over framings — passive board, board as obstacle, expertise as authority, conflict as dysfunction, efficiency as primary goal.

"District / school district" — say "school system" (carve-out: questioner's own words, direct quotes, operational references to a specific entity).

"Equity" — describe specifically (reading-rate gaps, resource disparity, etc.).

"Achievement gap" — describe the gap with data or name the system failure.

Politically-coded terms — DEI, anti-racist, woke, parents' rights, social-emotional learning (as wedge). ESB is non-partisan. Name the concrete concept.

"Non-essential activities" — that's a board's judgment to make, not ours.

3.7 NEVER Words (AI-Tell Words)

Tier 1 — Kill on sight, rewrite the sentence: delve, utilize, facilitate, elucidate, endeavor, encompass, embark, pivotal, tapestry, realm (metaphorical), beacon, harness, underscore, bolster, multifaceted, foster, seamless, transformative, revolutionize, testament (as in "a testament to"), paradigm, synergy, synergize, holistic, catalyze, catalyst, juxtapose, myriad, plethora, nuanced (as filler)

Tier 2 — Suspicious in clusters. Rewrite the paragraph if 3+ land in one: comprehensive, cutting-edge, innovative, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer

Provisional — AJ uses at low frequency, grounded context only. Cut them anywhere else: "leverage" (monitoring context only), "robust" (once per piece max), "illuminate" ("illuminates options" context), "navigate" ("navigate conflict" only)

Sentence-initial transitions — never start a sentence with: Moreover, Furthermore, Additionally, Notably, Consequently, Ultimately, Therefore, Indeed, Thus, Subsequently, Nonetheless, However, Nevertheless, Meanwhile, In conclusion, In summary

AI-hallmark / filler phrases — never: "provides valuable insights," "plays a crucial role," "in today's digital age," "in the fast-paced world," "at its core," "that being said," "it's worth noting," "it's important to note," "importantly," "interestingly," "a nuanced understanding," "opens new avenues," "paves the way," "stands as a testament," "a rich tapestry," "a beacon of," "dive into," "let's dive into," "let's explore," "as we can see," "as mentioned earlier," "at the end of the day," "it goes without saying," "without further ado," "when it comes to," "in the realm of," "one might argue that"

4. The Quality Measurement Framework

Quality is measured across four dimensions. Each dimension has a 1–10 scale with anchored descriptors. Passing threshold is ≥ 9 on every dimension for final ship; ≥ 7 on every dimension for draft acceptance.

4.1 Dimension 1: Fidelity to ESB Framework & Glossary (Weight: 30%)

Measures alignment with the ESB governance framework as defined in the glossary and style guide. Does the content use ESB terms correctly? Are distinctions drawn cleanly? Are PG terms absent?

4.2 Dimension 2: Fidelity to AJ Crabill's Voice (Weight: 25%)

Measures how well the prose matches AJ's established voice — the rhythms, register, signature moves, and NEVER rules compliance.

4.3 Dimension 3: Accuracy / Factuality (Weight: 25%)

Measures factual correctness: ESB framework claims match the glossary and source documents, claims about board governance are accurate, no fabricated sources or data.

4.4 Dimension 4: Fulfillment of Writing Intention (Weight: 20%)

Measures whether the content accomplishes its stated purpose. Was the brief met? Does it do what it set out to do?

4.5 Composite Score

Composite = (Fidelity_to_ESB × 0.30) + (Voice_Fidelity × 0.25) + (Accuracy × 0.25) + (Fulfillment × 0.20)

Passing threshold: Composite ≥ 9.0 with no single dimension below 8.0. Draft acceptance threshold: Composite ≥ 7.0.

4.6 Scoring Procedure

Scoring should be done by the model best suited for evaluation:

Critic scoring (structural/analytical): GPT-5.6 Sol (highest intelligence index)

Voice scoring (stylistic judgment): Claude Fable (best creative judgment)

ESB framework scoring (esoteric domain knowledge): Claude Sonnet 5 (most balanced)

For each scoring run, provide the scorer with:

The content being scored

The specific scoring rubric for that dimension

The relevant reference documents (ESB glossary, style guide, or voice profile)

5. The Testing Regimen

This section defines the empirical approach for identifying which model configuration(s) consistently produce the highest quality results. The regimen is designed to be run as a batch of automated subagent tasks.

5.1 The Test Harness

Each test consists of:

A fixed prompt — the same writing task given to every model configuration being tested

A fixed reference set — the same ESB glossary + style guide + voice profile excerpts provided as context to every model

The output — each model's raw output, scored on the 4-dimension rubric

The comparison — scores tabulated and ranked

5.2 Test Matrix

Run every model configuration through the same test prompt. A "configuration" is a specific model in a specific role (e.g., "Sonnet 5 as Drafter"). Tests are:

Round 1: Drafting Quality (one-shot)

Score all outputs on the 4-dimension rubric. Rank.

Round 2: Drafting Quality (with ESB context injection)

This separates model-native ESB knowledge from context-prompted performance.

Round 3: Chapter Drafting (book-length sample)

Round 4: Council Configuration (quality scoring accuracy)

Measure: does the scorer reliably detect known issues? Does it consistently rank good above bad?

5.3 The Standard Test Prompt

The following prompt is used for all Round 1 and Round 2 tests:

Write a guidance document titled "Effective Goal Monitoring" following the ESB framework.

The document should:

1. Open with the grounding "why" (school systems exist to improve student outcomes)

2. Define goal monitoring in ESB terms

3. Explain the four elements of an effective monitoring report

4. Distinguish monitoring from managing

5. Describe the board's role in monitoring conversations

6. Include what strategic questions look like in practice

7. End by returning to student outcomes

Target: ~2,500 words

Reading level: 8th grade or below

Voice: "we recommend," second person ("your board"), advisory but not condescending

No em dashes, no semicolons, no NEVER words

When testing with ESB context injection (Round 2), prepend the full ESB glossary and style guide.

5.4 Scoring Protocol

For each test output:

Run mechanical anti-slop scan (capture raw penalty)

Have GPT-5.6 Sol score Dimensions 1 (ESB fidelity) and 3 (Accuracy)

Have Claude Fable score Dimension 2 (Voice fidelity)

Self-score Dimension 4 (Fulfillment of intention — did it follow the brief?)

Record all scores in a comparison table

Calculate composite

5.5 Comparison Table Template

Test | Model | Config | ESB Fid | Voice | Accuracy | Fulfill | Composite | Slop

-----|-------|--------|---------|-------|----------|---------|-----------|-----

T1.1 | Sonnet 5 | solo   | 8.5     | 9.0   | 9.0      | 9.0     | 8.88      | 0.8

T1.2 | GPT-5.6 | solo   | 7.0     | 6.5   | 8.0      | 9.0     | 7.53      | 4.2

...

5.6 Initial Configuration (Default Until Testing Proves Otherwise)

Pending test results, the default configuration is:

This assumes Sonnet 5 will perform best on ESB voice (it has the strongest track record with AJ's material). If testing proves otherwise, update Section 1.1 accordingly.

6. Architecture by Format

6.1 Guidance Doc Architecture

Title: "Effective [Topic] [Aspect]" (18pt, centered, bold, no subtitle)

[Grounding opener — no header]

School systems exist to improve student outcomes... [connect to topic]

H2: What Is [Topic]?

Definition in ESB terms. Distinctions drawn.

H2: Why [Topic] Matters

Connect to the conviction: student outcomes don't change until adult behaviors change.

H2: How to [Do the Topic] — A Framework

3–5 concrete steps or components. Use scannable structures.

H2: Common Mistakes / What to Watch For

Pattern recognition. Frame problems as patterns, not incidents.

H2: Bringing It Back to Student Outcomes

[Closing paragraph — no header]

6.2 Book Chapter Architecture (Nonfiction)

[Opening move — match to register]

- Persuasive: True story → "I share this because it illustrates..."

- Definitional: Direct, precision-as-hook

- Taxonomy: Pattern-recognition hook → identify/strategy/trap

[Body — 3–5 sequential sections]

Each section advances the argument. Sections are moves, not containers.

[Closing — return to student outcomes + bridge to next chapter]

6.3 Full Book Architecture

Front Matter (title page, copyright, dedication, table of contents, foreword/preface)

Part One: Diagnosis

Chapter 1–X: Framing the problem, the why, the evidence that something must change

Part Two: The Framework

Chapter X+1–Y: What the ESB framework is, how it works, the distinctions

Part Three: Implementation

Chapter Y+1–Z: How to apply it, case studies, patterns of success

Part Four: Sustaining

Chapter Z+1–End: How to keep it going, continuous improvement, the long game

Back Matter (appendices, glossary, acknowledgments, about the author)

6.4 Workbook Architecture

Part One: Chapter-by-Chapter Application

For each chapter of the companion book:

  Summary (2–3 sentences)

  Key Framework (the governance concept taught)

  Reflect (Individual) — 3–5 journaling questions

  Discuss (Group) — 3–5 book club questions

  Act — one specific action exercise

Part Two: Framework Reference Templates

Goals template, Guardrails template, Monitoring template

One-page reference sheets

Part Three: Action Plans

90-Day Individual Plan

2-Day Board Team Workshop Agenda

6-Session Book Club Facilitator Guide

7. Voice — AJ's Register by Format

7.1 Register Reference

7.2 AJ's Signature Moves

These moves mark AJ's voice. Use them naturally, never forced:

"The board's job isn't to [X] — it's to [Y]" — the most AJ move. Use sparingly and only when the contrast is real.

"Here's what often happens..." — setup for a pattern, then the alternative.

"We recommend" — collective voice. Never "I recommend."

"It depends on what you mean by..." — the disarming reframe.

"The first step is clarifying..." — most problems are clarity problems.

"This is a critical distinction" — signpost that says pay attention.

"Predictable systems create stronger feedback loops than informal conversations" — reach for it when structure vs. conversation.

"Not X, but Y" — signature contrastive negation. Grounded in specifics.

"Diagnose, then prescribe" — structural rhythm.

"End by bringing it back to student outcomes" — every piece.

7.3 Voice for Book-Length Prose (Book Register)

Book register differs from guidance/doc register in key ways:

Longer sentences: ~23 words/sentence (guidance: ~14–16)

Paragraphs: 4–8 sentences (guidance: 2–4)

Story-led openings: True stories, not framework statements (for persuasive chapters)

First person: "I" and "we" used naturally (guidance: "we recommend" only)

Dialogue: Coaching conversations can include dialogue (guidance: no dialogue)

Emotional range: Wider — humor, tension, vulnerability (guidance: professional neutral)

Research: Woven into narrative, never footnoted (guidance: no citations)

The NEVER rules (Section 3.7) still apply to book register. Book register exempt from: sentence-length caps, paragraph-length caps, second-person requirement, and the grounding "why" opener.

8. ESB Glossary Cross-Reference Index

Every generated piece of content should be checked against these key ESB terms. If your content uses one of these, ensure the definition matches the ESB glossary, not a generic meaning.

Core Framework Terms

Assessment Types

Failure Types

9. Anti-Slop — Calibrated for Book-Length Content

9.1 Two-Pass System

Book-length content requires a two-pass anti-slop system:

Pass 1: Mechanical (zero-cost, automated) Run the anti-slop scanner from anti-slop-skill/anti-slop-scanner.py on every chapter/section immediately after drafting:

Tier 1 word scan (kill on sight)

Tier 2 cluster detection (3+ in a paragraph)

Tier 3 filler phrase scan

Em-dash/en-dash density (banned)

Transition over-opener check

Average sentence length (proxy for reading level)

Thresholds:

≤ 1.5: Clean

1.5–3.0: Flag for review

3.0: Voice re-alignment pass required

Pass 2: Structural (manual targeted — any single model can do this) Read for patterns the regex scanner misses:

"felt something [verb] in [body part]" variants

"[X] landed like [Y]" constructions repeated

"let out a breath [they] didn't realize [they] were holding"

"a sense of" / "the weight of" / "a wave of X washed over"

Repeated rhetorical structures across chapters

Over-explained silences

9.2 Book-Length Specific Concerns

Book-length content introduces anti-slop issues that short-form content does not:

10. Quality Gates — The Screen (Pre-Release Checklist)

Every piece of content runs through this screen before it ships. Run the screen as a final subagent task with the complete manuscript/document as context.

The 10-Point Screen

Conviction + opener: Does it open by grounding the reader in why school systems and boards exist, then connect to the topic? (Book chapters: match opener to register — story, direct, or pattern.

Reading level: 8th grade or below, never above 10th? (Book register exempt from the 8th-grade floor — 8th–10th is acceptable — but never above 10th.)

Distinctions: Are the ESB lines drawn cleanly and correctly? (Board vs. superintendent work, monitoring vs. managing, Goals/Guardrails/Initiatives, owners vs. customers.)

Ending: Does it bring it home to student outcomes? (Every piece. The reader should finish thinking "this is about kids.")

Voice: "We recommend," not "I" or "you must"? Confident, not hedgy? No "I feel/think/believe"? Matches the register for the format?

ESB terminology: ESB words not PG words. "Practitioner" not "coach"? "Board chair" not "board president"? "Any Reasonable Interpretation" spelled out? No "SOFG," "PG," or "LSG"? (Section 3.4–3.5.)

Mechanics: No horizontal rules, no em dashes (use --), no semicolons, no ellipses, straight quotes, Oxford comma? (Doc/PDF export: 18pt centered bold title, 14pt bold left headers, 11pt body, 0.5" margins, single-spaced.)

NEVER words/phrases: Any AI-tell words, sentence-initial transitions, or AI-hallmark phrases? (Section 3.7.)

Avoided language: Any banned governance term or power-over framing? (Section 3.6.)

No named organizations: CGCS or any individual school system? Genericize. No rival frameworks named ("SOFG," "PG," "LSG") unless intentionally contrasting.

Gate Status

All 10 pass: Ship

1–2 fails: Fix flagged items, re-check, ship

3+ fails: Return for revision loop. Do not ship.

Pre-Ship Validation for Books

For full books, add these checks:

Chapter continuity: Does each chapter's ending hook into the next chapter's opening?

Thread consistency: Are core metaphors introduced properly, referenced consistently, called back meaningfully?

Framework consistency: Every mention of Goals, Guardrails, Three A's uses the same vocabulary and definition order.

Voice drift check: Any pockets where the voice shifts from the established register?

Character/name consistency (if applicable): Cross-check ALL names across ALL chapters.

Part boundary integrity: Part One stays in diagnosis mode. Part Two teaches the framework. Part Three shows the payoff.

11. Council Review Architecture (Book-Length Only)

For books (not guidance docs, workbook, or blog posts), convene a quality council:

Council Members

Scoring Protocol

Each council member scores every chapter on the dimensions they cover (1–10 scale)

The Critic chairs: collects scores, identifies consensus themes, flags conflicting assessments

Any chapter below 8.0 on any dimension enters the revision loop

Revision: delegate the specific fix to the appropriate model (structural issues → GPT-5.6 Sol, voice issues → Claude Fable, terminology fixes → Kimi)

Re-score after revision

Plateau detection: 3 rounds with < 0.3 gain → accept best version

Batch Revision Pattern

When the Council returns 5–10 specific fixes across multiple chapters, delegate them as parallel subagent tasks rather than applying sequentially:

delegate_task(tasks=[

    {"goal": "Fix Ch3: compress preamble + add dramatic tension", "toolsets": ["file"]},

    {"goal": "Fix Ch7: voice drift toward academic register", "toolsets": ["file"]},

    {"goal": "Anti-slop scan Ch1-10, fix flags", "toolsets": ["file", "terminal"]},

])

When to Skip the Council

Guidance docs: Skip Council. Run only the 10-point screen.

Workbooks: Skip Council. One consistency check.

Blog posts / newsletter articles: Skip Council. Site-specific pipeline handles quality.

First draft of a new book: Skip Council until after human reading. Present compiled draft for AJ's feedback first.

Revisions after AJ's feedback: Run Council on the post-feedback draft.

Philosophical memoir: Sample Council on 4 representative chapters (opening, heart, middle, closing) rather than full manuscript.

Appendix A: Quick Reference — Format Selection

Appendix B: Related Documents