title: "SchoolBoardAnswers.com — Content Generation Guide" type: content-guide site: schoolboardanswers.com updated: 2026-07-08

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

ESB Language, Terminology & Mechanics (binding)

This section is binding for all generated content. Where anything below conflicts with older instructions in this guide, this section wins. The full standard is esb_writing_style_guide.md in the canonical guides folder.

Mechanics. No em-dashes. Where an em-dash would go, use a spaced double-hyphen ("--"), sparingly, or split the sentence. No en-dashes (use a hyphen, including in ranges like "1-2"). No semicolons in body prose. Straight quotes only. Oxford comma. No horizontal rules.

ESB terminology, never Policy Governance terms. Goals, not Ends. Guardrails, not Executive Limitations. Governing, not Governance Process. Delegation, not Board-Management Delegation. Never describe ESB as built on or adopted from Policy Governance. It is grounded in "principles of a policy-based approach to governance." Never write "SOFG," "Student Outcomes Focused Governance," "Policy Governance," "PG," "Lone Star Governance," or "LSG" (exception: SOFG only when intentionally contrasting with ESB). Use "board chair," not "board president." Use "Practitioner," not "coach," for the certified role. Spell out "Any Reasonable Interpretation" (never "ARI"). Use "own conduct," not "own-conduct." Four board-adopted policy types only: Goals, Guardrails, Delegation, Governing (no "Policies About X" category). ESB is prioritized (1-3 policies) in Goals and Guardrails and exhaustive in Delegation and Governing. A Goal is always a student outcome.

Governance language to avoid (describe the specific behavior instead): "micromanage," "rubberstamp," "stay in your lane," "good/bad/right/wrong" as judgment (even affirmatives like "the right framing"), power-over framings, "district"/"school district" (say "school system" in reader-facing content -- a questioner's own words, direct quotes, and operational or data references to a specific entity may keep it), "equity" as a bare term, "achievement gap," politically-coded terms, and "non-essential activities" for what a board could otherwise do.

Section 3 — Site Context

Document purpose: This guide governs all AI-generated Q&A content for schoolboardanswers.com. Every rule here is a hard rule unless explicitly marked as a guideline. When in doubt, apply the more restrictive interpretation. This document is the complete authority — do not supplement it with general web writing conventions unless they are consistent with everything stated here.

Applies to: Weekly Q&A content generation cycle

Domain and Content Type

Domain: schoolboardanswers.com

Content type: Q&A articles — one question, one direct and complete answer

Publication frequency: Weekly (one new Q&A article per week)

One-Sentence Purpose

SchoolBoardAnswers.com exists to give sitting school board members a direct, actionable answer to the specific governance question they are facing right now — so they can leave the page knowing what to do, not just knowing more about the problem.

Target Audience

The reader is an active school board member — either newly elected (less than two years on the board) or experienced (two or more years, returning with a harder question). They have a specific situation in front of them: a difficult superintendent relationship, a monitoring report they do not know how to read, a board member who keeps derailing meetings, a budget they do not know how to evaluate. They are not reading to learn theory. They are reading because something is happening and they need to know what to do about it.

Assume the reader:

Knows basic board vocabulary (superintendent, executive session, public comment, board policy) but may not know governance-specific terminology

Is in the middle of a situation, not studying for the future

Will skim the first paragraph to decide if this is worth reading — the answer must be in the first paragraph

Has limited time — they are a volunteer serving the public alongside a job and family

Wants respect, not a lecture — they are capable adults making hard decisions in public life

Does not know they are reading something aligned with any particular governance framework — they just Googled their question

Voice and Persona

Write as a knowledgeable colleague who has worked closely with many school boards and has seen this exact situation play out before. The voice is:

2nd person throughout: "your board," "you'll want to," "when your superintendent does X"

Advisory, not academic: "Here's what tends to work" not "Research shows that boards should consider"

Direct: The first sentence of the answer states the answer. Not background. Not context. The answer.

Plain language: No jargon the reader would not already know. No governance theory vocabulary unless it is briefly explained.

Non-condescending: The reader is a peer, not a student. Never explain things they obviously know.

Warm but not soft: This is not therapy or cheerleading. It is practical advice delivered with care.

No byline, no author, no attribution: The site has no named human voice. The advice comes from the site itself, not from a person.

Tone reference: think of a trusted former board chair who calls you back when you're stuck. They don't lecture. They ask one question to make sure they understand, then tell you what they would do and why. That's the register.

What Makes This Site Distinct From the Other 8 Sister Sites

The 9-site network covers school board governance from multiple angles. Each site has a distinct lane. Confusion about which lane this site occupies will produce the wrong content.

SchoolBoardAnswers.com vs. schoolboardreport.com: The Report analyzes trends and patterns across districts — it takes a step back and describes what is happening in the field. SchoolBoardAnswers.com is the opposite: it zooms into a single practitioner's situation and gives them the specific answer. The Report might publish "Monitoring Reports Are Being Misused Across the Country." SchoolBoardAnswers.com publishes "What do I do when my board keeps getting monitoring reports but nothing changes?" One is journalism; the other is an advice column.

SchoolBoardAnswers.com vs. effectivegoverningboards.com: EffectiveGoverningBoards.com produces research-backed policy briefs written for researchers, policy advocates, and governance scholars. The language is formal, citations are common, the reader is a professional studying the field. SchoolBoardAnswers.com speaks to a working board member in plain language with no citations. The same topic — say, goal-setting — would appear as a policy brief with evidence review on EGB and as a "here's how to do it at your next meeting" piece on SBA.

SchoolBoardAnswers.com vs. creatingoutcomes.com: CreatingOutcomes.com covers all governing body types: school boards, city councils, nonprofit boards, hospital boards. SchoolBoardAnswers.com is exclusively school-board-specific. If an article could apply to a city council without editing, it belongs on CreatingOutcomes.com, not here. Every piece of advice on SBA must be grounded in the school board context — the superintendent relationship, the student outcome mission, the public accountability structure, the specific dynamics of publicly elected oversight of a public school system.

SchoolBoardAnswers.com vs. schoolboardresearch.com: SchoolBoardResearch.com reviews and synthesizes academic research. SchoolBoardAnswers.com does not engage with research. No citations, no literature reviews, no "studies show." SBA's authority comes from the quality and specificity of its practical advice, not from academic backing.

SchoolBoardAnswers.com vs. schoolboardreview.com: SchoolBoardReview.com evaluates governance tools, frameworks, and professional development programs. SBA does not review things — it answers questions.

SchoolBoardAnswers.com vs. schoolboardweekly.com: SchoolBoardWeekly.com covers current events and timely news relevant to school board members. SBA is entirely evergreen — no current events, no news analysis, no date-specific content.

SchoolBoardAnswers.com vs. governthefuture.com and effective-boards.com: These sites serve broader or forward-looking governance audiences. SBA is sharply focused: a sitting school board member with a specific question today.

The defining test for this site: Would a sitting school board member type this exact question into a search engine, with the word "school board" or an implicit school board context baked into the query? If yes, it may belong here. Then apply the existential test (Section 8g): could this article appear on any other governance site without changes? If yes, it fails.

Content Goals

Primary Goal Give the reader a complete, actionable answer to the governance question they came with — so they leave knowing what to do, not just knowing more about the problem. The test: after reading this article, does the board member know something they can do or say or decide at their next meeting or in their next conversation with the superintendent? If yes, the piece succeeded. If they feel informed but still stuck, it failed.

Secondary Goals

Build credibility as the go-to practical resource for school board members with specific governance questions (organic search and return visits)

Provide consistent coverage across the full range of board governance situations so that over time, the site becomes a comprehensive reference

Demonstrate implicitly — never explicitly — that board governance rooted in student outcomes produces better results than procedural or political governance

What a Successful Piece Looks Like

The first paragraph contains the direct answer to the question — a reader who only reads the first paragraph leaves with the key takeaway

The advice is specific enough that the reader can use it without further research — it names what to do, when to do it, and what to expect

The scenario and framing would be recognizable to a real board member — it sounds like the situation they are actually in, not a sanitized hypothetical

The piece could remain accurate and useful five years from now without edits — it contains nothing tied to current events, current laws in a specific jurisdiction, or named individuals

What a Failed Piece Looks Like

The answer is buried behind several paragraphs of background, context, or throat-clearing — the reader has to work to find what they came for

The advice is so hedged or general that it gives the reader no clearer direction than they had before reading — "it depends on your situation," "work with your legal counsel," "every board is different" as the primary takeaway

The piece lectures about what boards should do rather than advising this reader on what to do — it reads as a policy position rather than personal advice

The topic is a management question disguised as a governance question — it tells the board member what the superintendent or staff should do, rather than what the board member should do

Content Format and Structure

Format Description Each article is a single question with a complete answer. The question appears as a header or page title. The answer fills the body of the article. There is no sidebar content, no author bio, no related articles section within the article body itself. The structure is lean: question, answer, done.

Required Structural Elements, In Order

1. The Question (title / H1) The question must be written in plain practitioner language — the way a real board member would type it into a search engine. It should be specific enough to signal the exact scenario, but not so narrow that it only applies to one district's situation. It is always phrased as a question. Do not editorialize or add governance terminology to the question that the reader would not naturally use.

Examples of good question titles:

"What do I do when my superintendent pushes back on my questions?"

"How often should my board monitor student outcome goals?"

"Can my board set goals without the superintendent's agreement?"

"What does it mean when our monitoring reports keep showing the same problems?"

Examples of bad question titles:

"How Can Boards Apply Goal-Setting Theory to Improve Governance?" (academic, not practitioner)

"The Role of the School Board in Monitoring" (not a question)

"Why Boards Should Focus on Outcomes, Not Operations" (editorial, not a question)

2. The Direct Answer (First Paragraph) The first paragraph delivers the answer. Not background. Not "this is a common question." Not context about why this matters. The answer.

The reader should be able to read only the first paragraph and have the core takeaway. Everything after elaborates, deepens, and makes it actionable — but the answer itself is in paragraph one.

Format: prose, not bullets. 3–5 sentences. State what the board member should do or understand, and why it works.

3. The Elaboration Body (2–4 paragraphs) This section deepens the answer. It may:

Explain the underlying governance principle that makes the advice work

Distinguish between common mistakes and the right approach

Describe what this looks like in practice (use a brief composite scenario if helpful)

Acknowledge a common complication and address it directly

Each paragraph should move the reader forward — no paragraph should just restate what came before. This is not an essay; it is an answer with depth.

4. Practical Steps (final section) Close with 3–5 concrete steps the reader can take. These must be specific enough to act on. "Talk to your superintendent" is not a step. "At your next one-on-one with your superintendent, ask directly: 'What would you need from the board to make this goal achievable?'" is a step.

Steps may be presented as numbered items or as prose with clear sequential logic. Do not use bullets for steps — the order matters and bullets suggest optionality.

The closing step should leave the reader with forward motion, not a tidy resolution ("and then everything will be fine"). Reality is messy. The closing should acknowledge that this is an ongoing practice, not a one-time fix.

Do not add:

A concluding summary paragraph that restates the answer

A "final thoughts" section

A call to action to subscribe, share, or visit other sites

An author attribution

Forbidden Structural Patterns

Listicle structure: Do not write "7 Things Board Members Should Know About X." The format is Q&A — one question, one answer. Lists within the body are acceptable only for the practical steps section and only when the items are genuinely sequential or parallel.

Long introductions: Do not spend the opening paragraph establishing that this is a common question, that governance is complex, or that different boards approach this differently. Start with the answer.

The hedge-first structure: Do not open with "It depends" or "Every situation is different." Those phrases may appear later in context, but they cannot be the answer to the question.

The summary sandwich: Do not end by restating the opening answer. The conclusion should add something — a forward-looking implication, a next step, an honest acknowledgment of ongoing difficulty — not recap.

Academic structure (thesis → evidence → conclusion): This is advisory writing, not an essay. The structure is: answer → elaboration → action.

Passive voice as a hedge device: "It is often recommended that boards consider..." is forbidden. Write "Your board should consider..." or "Consider..."

Word Count Range and Pacing

Target: 700–850 words

Minimum: 600 words (below this, the answer lacks sufficient depth)

Maximum: 900 words (above this, the piece is overexplaining or padding)

Pacing: The answer should feel dense, not padded. Every sentence should carry information. No filler transitions, no padding phrases.

In-Bounds Content

Core Topic Areas, Organized by ESB Practice

The ESB 5 practices — Focus, Clarify, Monitor, Align, Communicate — are the organizing framework for content coverage. These terms should never appear in the published article, but internally, every article should map to one or more of these practices. Track coverage across all five to avoid over-indexing on one or two.

Focus: The board focuses on student outcomes, not operations

What is and is not the board's job (governance vs. management distinctions)

How to redirect a board that keeps drifting into operational decisions

How to handle a board member who wants to manage staff

How to evaluate whether an agenda item is a governance question or a management question

What to do when the superintendent crosses into board territory

How to stay focused on outcomes when the community is loud about a non-outcome issue

Clarify: The board sets clear, measurable student outcome goals

How to set student outcome goals (what makes a goal good, what makes a goal bad)

How many goals to set

How to get the board to agreement on goals when there is conflict

What to do when the superintendent resists proposed goals

How to write goals that are measurable

How to distinguish outcome goals from process goals

What to do when goals are set but not followed

Monitor: The board monitors progress against goals regularly

How often to monitor

What a good monitoring report looks like vs. a bad one

What to do when monitoring reports show no progress

How to ask questions about a monitoring report without crossing into management

What to do when the superintendent controls the data pipeline

How to read data you did not ask for and do not understand

What to do when the board receives data but does not use it

Align: The board ensures resources align to goals

What is the board's role in budget review (not management — oversight)

How to evaluate whether proposed spending aligns with board goals

What to do when the budget does not reflect the stated priorities

How to ask resource alignment questions without directing operations

What to do when you disagree with a budget recommendation

Communicate: The board communicates results transparently

How to communicate board decisions to the community

How to handle community pressure that conflicts with board direction

What to say when the community is angry about a board decision

How to be transparent without undermining the superintendent

How to manage public comment sessions

How to communicate as one voice when the board is divided

Cross-cutting topics (relevant to multiple practices)

Board self-evaluation

Board professional development

Executive session rules and boundaries

Board member role clarity (individual vs. collective)

Navigating conflict between board members

Navigating conflict between the board and superintendent

New board member orientation and role understanding

What "In-Bounds Treatment" Looks Like

An in-bounds piece approaches its topic from the board member's perspective, in the board member's role. It answers: what does a board member do? Not: what should the superintendent do? Not: what does research say? Not: what is the policy position on this?

Every answer should implicitly demonstrate that a board focused on student outcomes handles this situation differently than a board focused on compliance, politics, or adult preferences. This demonstration should be in the advice itself — not stated as a principle.

Composite scenarios are encouraged when they make the advice concrete. A brief 1–2 sentence scenario ("Imagine your board has been receiving quarterly monitoring reports for two years, and the same three indicators keep showing red...") is appropriate when it sharpens the advice. The scenario must never use real districts, real names, or real identifiable situations.

Structural and Stylistic Models — Existing Articles

The following existing articles establish the site's standards. Each generation cycle should use these as calibration references.

qa/governance-vs-management.html — Model for: drawing clear, non-condescending distinctions between the board's role and the superintendent's role. Note how the line is explained through practical examples rather than definitional statements.

qa/goal-setting-process.html — Model for: walking the reader through a process without turning the piece into a manual. The steps feel natural, not procedural.

qa/how-often-monitor-goals.html — Model for: giving a specific, defensible answer to a question that feels like it could only be answered with "it depends" — and then explaining why this answer works in most situations.

qa/superintendent-pushback-on-questions.html — Model for: addressing a sensitive interpersonal dynamic with directness and without demonizing either party. The advice is clear without being punitive or naive.

qa/we-review-data-but-nothing-changes.html — Model for: acknowledging that the reader is already doing something right (reviewing data) while redirecting them toward what is missing. This is the "you're close, here's the step you're skipping" structure.

qa/redirect-off-topic-board-member.html — Model for: advice on board interpersonal dynamics that respects the collective governance structure without being evasive about the real difficulty of the situation.

The Question Every Piece Must Answer

Before finalizing any article, ask: "What does a school board member focused on student outcomes do when [the exact situation in the question]?" If the article answers this question with specificity, it passes. If the article describes the situation, explains the theory, but never clearly answers this question, it fails.

Out-of-Bounds Content

Forbidden Topic Areas

Management questions disguised as governance questions. The test: is the answer about what the board should do, or about what the superintendent or staff should do? If the actionable advice is for the superintendent, it is a management topic and does not belong here.

Examples of forbidden topics:

How should a superintendent communicate with staff during a budget cut?

What does good curriculum alignment look like?

How should a principal handle a discipline situation?

What makes an effective teacher evaluation process?

How should the district handle a student safety incident?

These are all legitimate topics for educators. None of them belong on a site that advises board members about their governance role.

Generic governance advice not specific to school boards. If the answer would work for a city council, a nonprofit board, or a hospital board without editing, it does not belong here. School board governance is distinct: the superintendent-board relationship has unique legal and professional norms, the mission (student outcomes) is specific, the public accountability structure is specific, the elected nature of the board is specific.

News analysis and current events. No piece should be tied to a specific legislative action, a recent court ruling, a current event, or anything that would become dated. If an article requires the reader to know about something currently in the news to understand the advice, it is out of bounds.

Research reviews. No "according to a study by..." structures. No literature synthesis. No academic framing.

Advocacy pieces. No piece should advocate for a governance philosophy as a position. The advice should demonstrate effective governance through its specificity, not argue for it.

Anything requiring jurisdiction-specific legal advice. "You should consult your district's legal counsel" is acceptable as a side note when genuinely relevant. It cannot be the primary answer. Do not write pieces whose primary answer is "check your state law" — that is not useful advice.

Topics That Belong on Sister Sites Instead

Forbidden Framings

Treating board decisions as optional when they are not. Do not write "some boards choose to monitor more frequently" as if frequency is purely a style preference. When there is a defensible position, take it.

Treating oversight as secondary to the superintendent relationship. The board's accountability role is primary. Do not frame oversight questions as potential threats to a healthy superintendent relationship. A healthy relationship includes rigorous oversight.

Treating politics as the main driver of board decisions. Board decisions should be anchored to student outcomes. Do not give political dynamics more weight than the outcome mission.

Treating procedure as governance. Following Robert's Rules correctly, having a properly formatted agenda, approving minutes — these are procedural necessities, not governance. Do not conflate them.

The both-sides frame on clarity questions. When the answer is clear (e.g., the board should not hire teachers — that is management), do not present it as a matter of perspective.

The Overlap Rule: How SBA Differs From Nearest Sister Sites

The nearest overlapping sites are creatingoutcomes.com and effectivegoverningboards.com. Both cover governance territory that SBA also covers. The differences are non-negotiable:

vs. creatingoutcomes.com: SBA is school-board-exclusive. CO is multi-sector. If the advice requires understanding of the school board's specific accountability structure, student outcome mission, or superintendent relationship norms, it belongs on SBA. If it generalizes, it belongs on CO.

vs. effectivegoverningboards.com: EGB is formal and research-grounded. SBA is practical and advisory. EGB's reader is studying the field; SBA's reader is in the field. If the piece uses citations, formal language, or is written to inform a policy position, it belongs on EGB. If it is written to help someone decide what to do at their next meeting, it belongs on SBA.

Citation and Sourcing Requirements

No Citations Required SchoolBoardAnswers.com does not use formal citations. No footnotes, no endnotes, no in-text citations, no "according to [organization]" attribution, no links to research papers.

How to Ground Factual Claims Without Citations All claims must be grounded in real governance patterns — things that actually happen in school board governance — but they do not need to be sourced. Use these approaches:

Describe patterns: "Most boards that struggle with monitoring have the same problem: they receive data but never ask what would change if the data were different."

Reference experience without naming it: "Boards that set fewer goals tend to make more progress on each one."

Use specificity as its own authority: "Three goals is almost always the right number. Fewer, and you've missed something important. More, and nothing gets the attention it needs."

Acknowledge complexity honestly: "This rarely resolves in one conversation. Plan for it to take several months."

Hard Rule: No Invented Statistics Never write a statistic that was not derived from real data. "Studies show that boards with clear goals are 40% more effective" is the exact kind of invented authority that makes content untrustworthy. Do not do this.

Never write "research shows," "studies indicate," or "according to experts" unless there is a specific, real source being cited — and citations are not used on this site. Therefore: never write these phrases.

Never invent a named authority. Do not create a fictional researcher, organization, or expert to lend credibility to a claim.

All authority on this site comes from the specificity and quality of the practical advice, not from invented external validation.

Section 4 — Grounding Document

Source: Great on Their Behalf (3rd edition) by AJ Crabill Access: Google Drive ID: 1KwiTQKLZlRDnTCzDmHaleeU3IVj_cHbsmA2s6nORdkE (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: a — pre-draft only

Pre-draft only: Before drafting, read the relevant sections of the grounding document. Use it to calibrate the frame, vocabulary, and core claims before writing begins. It is a framing calibrator, not a citation source.

Section 5 — Voice Register

Register: ajc-long Fidelity: MODERATE

Author blend:

Gladwell 35% — narrative specificity, scene-setting, counterintuitive reframes, accessibility

Collins 30% — precision, structured argument, clean declarative assertion

Sinek 20% — purpose-grounding, why-first framing, practitioner motivation

Gawande 15% — practitioner honesty, process complexity, earned humility

Sentence and paragraph targets:

Average sentence length: ~23 words

Paragraph length: 4–8 sentences

No extended run (3+ consecutive) of sentences under 8 words

Structural invariants:

Oxford comma always (a, b, and c)

Straight quotes only — no curly quotes

Contractions used naturally (don't, it's, we've, you'll)

No exclamation marks anywhere in the piece

No ellipses

No voice hedging: no "I feel/think/believe" as epistemic hedges

No sentence-initial transitions: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately

Register in practice: Advisory, 2nd person throughout ("your board," "you'll want to"). Direct assertion, not hedged claim. The voice is a knowledgeable colleague, not a scholar, not a cheerleader, not a policy analyst. It has seen this situation before and knows what tends to work.

Section 6 — NEVER Rules

Never open with background, context, or "this is a common question" — the first sentence states the answer

Never use 3rd person where 2nd person applies ("the board should" → "your board should")

Never write invented statistics or fabricated research references

Never write "research shows," "studies indicate," or "according to experts" — no citations on this site

Never use real names: people, districts, organizations by name in content

Never use governance framework terminology that would not be natural to the reader without brief explanation

Never end with a tidy resolution — the close should acknowledge ongoing practice, not promise a fix

Never write a management answer to a governance question — the actionable advice must be for the board member, not the superintendent or staff

Never name ESB, Effective School Boards, AJ Crabill, GOTB, or "why-based governance" by name in published content (exception: within a list of 3+ resources, and only 1–2 times per year across the network)

Never use the ESB 5 practice labels (Focus, Clarify, Monitor, Align, Communicate) in published content — these are internal scaffolding only

Never write content tied to current events, legislation, or anything that will date the article

Never write jurisdiction-specific legal advice as the primary answer

Never include a publication date in the visible post content or meta div — the <div class="meta"> date field must be omitted (left empty or removed entirely) from the generated HTML; these are evergreen reference articles and dates make them feel stale

Never describe monitoring reports as requiring "one page per goal" — the correct specification is 1–5 pages total per report

Never write goal monitoring frequency as "twice per year" or "annually" — the floor is at least 4 times per year

Never write goal quantity as "three to five" or "three to seven" — the target is 1–3, the hard ceiling is 5

Never write goal deadlines as a year alone ("by 2028") — always specify a month and year ("by June 2028")

Never write guardrails in affirmative form — always use negation: "The superintendent will not..."

Never attribute interim goal drafting to the board — the superintendent drafts interim goals; the board calibrates against them

Never describe the board's personnel authority as extending beyond the superintendent — hiring, evaluating, and replacing the superintendent are the full scope

Never link to sister sites except within a list of 3+ links, maximum 1–2 times per year across all SBA content

Section 7 — Generation Process

Each step must be completed in order. Do not skip steps. Do not combine steps. Pass/fail criteria are binary — a step either passes or it does not.

Step 1 — Gap Analysis

Model/method: Deterministic (no AI generation in this step)

Inputs:

Complete list of all existing qa/ slugs from the site directory

What to do:

Pull the complete list of existing slugs

Categorize each slug by ESB practice (Focus, Clarify, Monitor, Align, Communicate) and by topic cluster

Count articles per practice area and per cluster

Identify the 3 most underrepresented areas

Generate 5–8 candidate questions from underrepresented areas, each in practitioner language

Pass criteria:

At least 5 candidate questions generated

Each candidate addresses a real gap (not a topic with 3+ existing articles)

Each candidate is phrased as a question in practitioner language

Fail criteria:

Fewer than 5 candidates

Candidates duplicate existing articles

Candidates fail the practitioner-language test

Step 2 — Question Framing and Validation

Model/method: Deterministic (rule application, no generation)

Inputs:

Candidate questions from Step 1

What to do: For each candidate question, apply:

Practitioner-language test: Would a board member phrase it this way?

Existential test: Could this appear on a sister site without changes? (If yes, eliminate.)

In-bounds test: Is this a governance question, not a management question? (If management, eliminate.)

Duplicate test: Does this semantically duplicate an existing article? (If yes, eliminate.)

Select the one candidate that passes all tests and addresses the most significant gap.

Pass criteria:

One question selected that passes all four tests

Question is phrased in final form (how it will appear as the article title)

Fail criteria:

No candidate passes all four tests (return to Step 1 with revised gap analysis)

Question is ambiguous about whether it is governance or management

Step 3 — Structural Brief Generation

Model/method: AI-assisted (primary model or fallback)

Inputs:

Final selected question

ESB practice area and topic cluster

List of existing articles to use as calibration references

What to do: Generate a structural brief containing:

The direct answer (1–3 sentences — this becomes the core of paragraph 1)

3 elaboration points (each a key dimension of the answer to develop in the body)

3–5 practical steps (specific actions the reader can take)

A note on what common mistake this answer corrects

A note on what knowledge the reader can be assumed to have (so the draft does not over-explain)

Pass criteria:

Direct answer is genuinely direct — states what to do, not what the situation is

Elaboration points are distinct from each other

Practical steps are specific enough to act on

Common mistake is real, not manufactured

Knowledge assumption is reasonable for the target reader

Fail criteria:

Direct answer is hedged or describes the situation rather than answering it

Elaboration points overlap significantly

Steps are vague ("talk to your superintendent")

Step 4 — Draft Generation

Primary model: the configured write model Fallback model (if the configured write model unavailable): Claude Opus 4.8

Inputs:

Structural brief from Step 3

Voice description from Section 5

Structural requirements from Section 3

Word count target (700–850 words)

Existing articles as calibration references

Grounding document (Great on Their Behalf, 3rd edition) — read relevant sections before drafting to calibrate frame, vocabulary, and core claims

What to do: Generate a complete first draft using the structural brief as the scaffold. The draft must:

Open with the direct answer (not background)

Use 2nd person throughout

Follow the required structure: direct answer → elaboration → practical steps

Stay within 600–900 words

Use no citations, no invented statistics

Use no real names (people, districts)

Use no governance framework terminology that would not be natural to the reader

Pass criteria:

Article opens with the answer, not background

Word count is 600–900 words

No citations, no invented statistics

No real names of any kind

2nd person throughout

Fail criteria:

Article opens with background, context, or "this is a common question"

Word count outside range

Any real name present (district, person, organization by name)

Any invented statistic or fabricated research reference

Step 5 — ESB Framework Alignment Check

Model/method: Rule application against draft

Inputs:

Draft from Step 4

ESB practice area identified in Step 2

What to do: Verify that the article, through its advice, demonstrates effective governance anchored to student outcomes. Check:

Does the advice in this article reflect what a board focused on student outcomes would do? (If the advice would be identical for a board focused on political standing, it fails.)

Is the advice consistent with the board's governance role (oversight, not management)?

Does the article implicitly demonstrate the relevant ESB practice through the quality of its advice? (Never name the ESB framework or any named governance approach.)

Does any passage treat operational decisions as board decisions? (Fail if yes.)

Does any passage suggest that oversight should yield to relationship preservation? (Fail if yes.)

Pass criteria: All 5 checks pass.

Fail criteria: Any check fails — return to Step 4 with specific revision instructions.

Step 6 — Voice and Specificity Pass

Model/method: DeepSeek V4 Flash via OpenRouter → fallback OpenRouter Free tier

Inputs:

Draft from Step 4 (revised if Step 5 required changes)

Voice description from Section 5

Calibration articles from Section 3

What to do: Read the draft against the voice requirements and flag any passages that violate them. Specifically check:

Register: Does it sound like a knowledgeable colleague giving advice, or like a policy document, a textbook, or a cheerleader?

Person: Is 2nd person used throughout? Flag any 3rd person ("boards should") that should be 2nd person ("your board should").

Directness: Are there hedges that weaken the advice without adding honest nuance? (vs. honest acknowledgment of complexity, which is fine)

Condescension: Does any passage over-explain something the reader clearly already knows?

Specificity: Is the advice concrete enough to act on, or is it still at the level of principle?

ajc-long rhythm check: Sentences average ~23 words; paragraphs 4–8 sentences; no extended run of 3+ consecutive sentences under 8 words.

Author-blend audit: Is the Gladwell/Collins/Sinek/Gawande blend present in register and structure?

Revise any flagged passages. Do not merely flag — fix them.

Pass criteria: Draft reads as advisory, 2nd person, direct, specific, and non-condescending throughout. Rhythm and register consistent with ajc-long.

Fail criteria: 3 or more passages require significant revision (return to Step 4 with voice-specific brief).

Step 7 — Quality Checks

Run all quality checks from Section 8 in order: 8a Anti-Slop Scan, 8b Voice Check, 8c ESB Governance Language Check, 8d Site-Specific Checks. For each check, identify failing passages, fix them in the draft, and confirm the fix before moving on.

Pass criteria: All quality checks in Section 8 pass with zero flagged passages remaining.

Fail criteria: Any flagged passage not resolved before this step is marked complete.

Step 8 — Red-Team Adversarial Checks

Run red-team checks from Section 8 in order: 8e Primary Red-Team, 8f Council Red-Team, 8g Existential Voice Test. For each check, identify any failure and either fix the draft or, if the issue is fundamental, return to the relevant earlier step.

Pass criteria: All red-team checks in Section 8 pass.

Fail criteria: Any check fails. Fundamental failures (wrong topic, wrong voice, fails existential test) return to Step 2 or 3. Surface failures (specific passage fixes) are corrected and re-checked.

Step 9 — Technical Filing and Front Matter Check

Model/method: Deterministic rule application

Inputs:

Final draft from Step 8

File naming rules from Section 9

Front matter requirements from Section 9

What to do:

Generate the slug: 3–7 word verb-noun phrase, all lowercase, hyphens, no punctuation

Confirm the slug does not duplicate any existing slug (exact and semantic check)

Generate front matter: layout = qa, title = the article's question, category = appropriate value from Section 9 list

Confirm HTML file is correctly formatted for Jekyll

Place file in qa/ directory

Run Jekyll build check (dry run)

Confirm build succeeds with no errors

Pass criteria:

Slug is unique and follows naming convention

Front matter is complete and correct

Jekyll build succeeds

Fail criteria:

Slug duplicates an existing article

Front matter is missing or incorrect

Jekyll build fails

Section 8 — Quality Checks

Quality Check Failure Protocol

This protocol governs every check in Section 8 (8a through 8h, including all site-specific gates in 8d).

On any failure at any check:

Identify the specific violation — which rule, which tier, which gate, and exactly what was wrong

Revise only the affected portion of the draft to address that specific failure

Re-run the check that failed (not the full Section 8 — just the failing check)

Track the attempt count per check

Retry limit: 3 revision-and-retry cycles per check. If a check passes on retry, continue to the next check normally.

Ultimate Failure: if a check still fails after 3 retries, declare an ULTIMATE FAILURE for that check. Stop all further quality checks immediately. Do not publish, commit, or submit the draft. Proceed to ultimate failure reporting (below), then preserve the draft and full failure log — including stage name, attempt count, nature of each failure, and each revision attempt — in a dated file for AJ's review.

Ultimate Failure Reporting — SBA: Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (SBA), question answered, which check failed, attempt count, nature of each failure, and the draft. Mark status as FAILED. Do not publish.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any em-dash (no em-dashes; use a spaced double-hyphen "--" where an em-dash would go)

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (schoolboardanswers.com):

The following words and phrases are also flagged as anti-slop for SBA content specifically. Flag and delete or rewrite wherever they appear:

"truly," "really," "very," "quite," "actually," "essentially," "fundamentally," "absolutely," "certainly," "clearly" (when used to assert rather than describe), "importantly," "significantly" (when not quantified)

"robust," "comprehensive," "strategic" (when used as a vague intensifier), "meaningful" (when not followed by a concrete description), "impactful," "powerful," "key" (as an adjective), "crucial," "vital," "critical" (unless something will literally fail if it is not done)

"in today's world," "in today's landscape," "more than ever"

"In conclusion," "In summary," "To summarize," "It's important to remember," "Let's explore," "Let's dive in," "Let's take a closer look," "This is a great question," "Navigating [any noun]" as a standalone gerund phrase, "The good news is," "The bad news is," "That said," "Having said that," "Simply put," "In essence," "At its core," "As mentioned earlier," "As noted above," "Moving forward," "Going forward," "On the same page," "Unpack" (as in "let's unpack this"), "Deep dive," "Game changer" or "game-changing"

"Stakeholders" → use specific terms: "community members," "parents," "staff"

"Empower" or "empowering"

"Leverage" (as a verb: "leverage this approach")

"Ecosystem" (when not used literally), "Bandwidth" (when not used literally), "Circle back," "Touch base"

8b. Voice Check

Voice Check — Moderate Fidelity (ajc-long)

Run a moderate voice check. No formal scoring threshold — use judgment. If a colleague would describe this as reading like AI output, revise before proceeding.

Core NEVER rules (must be clean):

No Tier 1 anti-slop words (already checked in 8a)

No sentence-initial transitions: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately

No exclamation marks anywhere in the piece

No ellipses

No curly quotes

No voice hedging: no "I feel/think/believe" as epistemic hedges

Fingerprints (must be present):

Oxford comma: always (a, b, and c)

Straight quotes only (no curly quotes)

Contractions used naturally (don't, it's, we've)

Rhythm check:

Sentences average ~23 words; paragraphs 4–8 sentences

No extended run (3+ consecutive) of sentences under 8 words

Reading level appropriate for a practitioner audience

SBA-specific voice checks:

Register: Does it sound like a knowledgeable colleague giving advice, or like a policy document, a textbook, or a cheerleader?

Person: Is 2nd person used throughout? Flag any 3rd person ("boards should") that should be 2nd person ("your board should").

Directness: Are there hedges that weaken the advice without adding honest nuance?

Condescension: Does any passage over-explain something the reader clearly already knows?

Specificity: Is the advice concrete enough to act on, or is it still at the level of principle?

8c. ESB Governance Language Check

ESB Governance Language Check

Reference: Google Drive ID 13O3_qNxtRVHsTDyDMXdotPLOhIMTyRe0J_1yQ9tzhOQ

Banned phrases — any occurrence fails:

"micromanage" / "micromanaging" → describe the specific behavior (is the board operating within its governance role or directing implementation?)

"rubberstamping" / "rubber stamp" → describe whether the board exercised informed judgment

"stay in your lane" → reference governing policies or board/superintendent role distinction

"good/bad/right/wrong" as personal moral judgment → frame around effectiveness and outcomes

Banned framings — restructure any instance found:

Board as passive recipient: any suggestion that the board should simply receive, defer, or accept without agency

Board as obstacle: any framing that board involvement is a problem to manage around

Expertise as authority: any framing that professional staff have more legitimate authority than elected board members

Conflict as dysfunction: any framing that disagreement among board members is inherently bad

Efficiency as primary goal: any framing that speed or non-disruption is the board's primary objective

Education terms — replace with specific language:

"school district" or "district" → "school system"

"equity" → describe the specific gap or outcome with data (reserve the term only for direct statutory quotation)

"achievement gap" → describe the system failure directly with specific data

Politically-coded terms → describe the specific concept: DEI, anti-racist, woke, "parents' rights" (as contested framing), SEL (as wedge term)

8d. Site-Specific Checks

The following checks are unique to schoolboardanswers.com. All must pass before the draft advances to red-team.

Gate: Generic Opener Detection

Flag any opening sentence or paragraph that:

States that the question is common, understandable, or frequently asked

Provides background or context before delivering the answer

Begins with "Many board members find themselves..." or "It's not uncommon for..." or "School board governance can be..."

Opens with a definition of a term the reader clearly already knows

Begins with the word "When" followed by a restatement of the question without answering it

How to fix: Delete the opener. The first sentence should state the answer. Draft a replacement that begins with the core takeaway.

Example flagged opener: "Many school board members struggle with understanding the line between governance and management. This is one of the most common questions boards face, and it's understandable why — the line isn't always obvious."

Example fixed opener: "When you find yourself thinking about how the curriculum is structured or whether a particular teacher should be reassigned, you've crossed the line into management territory — and your job is to step back."

Gate: Vague Claim Detection

Flag these patterns:

Claims that "research shows" or "studies indicate" without a specific source (forbidden entirely — no citations on this site)

Claims that use percentages, statistics, or numerical ranges without a real source ("boards with clear goals are 40% more effective")

Claims that use "many," "most," "some," "often," "frequently," or "typically" without enough specificity to be meaningful — remove them if they are just padding hedges

Claims that attribute a general truth to a named authority that was not actually named ("governance experts agree")

Claims that a practice "works" or "doesn't work" without explaining why

How to fix:

Delete invented statistics entirely

Replace vague quantifiers with honest specificity: "expect this to take three to six months"

Replace attributed claims with direct claims: "governance experts agree that..." → "boards that do this tend to..."

Add a "because" clause to unsupported effectiveness claims

Gate: Structure Uniformity Check

What to look for:

All paragraphs are the same length (sign of padding or compression)

Practical steps are all the same level of specificity (some too vague, some too detailed — should feel graduated)

Every section ends with the same rhetorical pattern (mix up the patterns)

The article is a mirror image of the structural brief — elaboration points not developed into paragraphs but merely expanded into longer versions of the brief's bullets

How to fix:

Vary paragraph length intentionally — some short (2–3 sentences for emphasis), some longer for complexity

Graduate the steps from "first, do this immediately" to "over time, watch for"

Vary closing patterns within sections

If elaboration points are just expanded bullets, rewrite them as paragraphs that develop an idea

Gate: Tidy Resolution Detection

What to flag:

Any closing sentence that implies the problem is now solved if the reader follows the steps

Any phrase like "with these steps, your board will be well-positioned to..."

Any promise of a specific outcome ("within six months, you'll find that...")

Any motivational closing that sounds like a pep talk

Any closing that restates the article's main answer as if it is a conclusion

How to fix: Endings should leave the reader with forward motion, not false comfort. Acknowledge that governance is ongoing. The last sentence should imply that this is a practice, not a fix.

Example flagged ending: "By following these steps, your board will develop a strong monitoring culture that keeps everyone accountable and drives real results for students."

Example fixed ending: "This won't resolve itself in one cycle. Plan to revisit how the board is using monitoring data every six months — the goal is to build a reflex, not to solve it once."

Gate: Over-Explanation Detection

What to flag:

Any passage that explains something the target reader clearly already knows (e.g., explaining what a board meeting is, explaining what a superintendent does in general terms, explaining that the board is elected)

Any passage that re-explains the same concept twice in different words

Any passage that treats the reader as unfamiliar with basic governance vocabulary (public comment, executive session, board policy, consent agenda)

How to fix: Delete the over-explanation. Trust the reader. If a less common concept needs a brief clarification, a single parenthetical is enough.

Gate: False Specificity Scan

What to flag:

Invented composite scenarios that include suspiciously round numbers ("In one district, test scores improved by 25%...")

Scenarios that are so specific they appear to reference a real district or real people, but the details were invented

Steps that sound specific but are actually vague when examined closely

How to fix:

Remove invented statistics from scenarios entirely

Make scenarios clearly hypothetical without suspiciously precise invented numbers

Replace false-specific steps with genuinely specific steps (what data, what question, what meeting)

Gate: Answer-Avoidance Detection Flag any article where the answer to the question is never actually stated — where the article gives process ("here's how to think about it," "here are the questions to ask yourself") without ever stating what the board member should do. The article should answer the question, not help the reader find their own answer.

Gate: Lecture-Instead-of-Advise Detection Flag any passage that states what boards should do as a principle without connecting it to what this reader should do in their situation. "Boards must maintain clear role boundaries" is a lecture. "When your superintendent questions why you're asking about curriculum choices, your response is..." is advice. Every principle in the article should be connected to an action the reader can take.

Gate: Excessive Hedging Detection SBA answers are direct. Flag any article where the practical steps section contains more hedges than actions. "It may be helpful to consider asking..." should be "Ask." "Depending on your board's culture, you might..." should be "Your board should..." followed by an honest note about variation if it genuinely matters.

Gate: Domain Expert Test

Ask: Would a practicing school board member with 10 years of experience read this article and find the advice sound and useful?

Specifically:

Is the advice consistent with how effective school board governance actually works?

Does it reflect real dynamics (board-superintendent, board-community, intra-board) rather than idealized or oversimplified dynamics?

Would an experienced board member recognize the scenario being described?

Is there any advice that an experienced practitioner would immediately know to be wrong or naive?

Pass: An experienced practitioner would find the advice useful, or at minimum defensible. Fail: The advice contradicts how governance actually works, or is naively optimistic about difficult dynamics.

Gate: Credibility Risk Scan

Ask: Is there anything in this article that could embarrass the site if a reporter, a school board association, or a governance scholar read it?

Specifically:

Any invented statistics or fabricated research?

Any advice that could be characterized as encouraging board overreach?

Any advice that could be characterized as undermining the superintendent's professional authority in an inappropriate way?

Any scenario that could be misread as describing a real district?

Any claim that is legally or factually incorrect?

Pass: Nothing in the article creates a credibility risk. Fail: Any invented data, legally incorrect claim, or scenario that reads as a real district. Fix and re-check.

Gate: Voice Consistency Test

Compare the draft against three existing SBA articles. Specifically:

Does the draft use the same register (advisory, 2nd person, direct)?

Does the draft maintain the same assumed knowledge level?

Does the draft feel like it comes from the same "voice" as the calibration articles?

Pass: A reader who had read three other SBA articles would find this article consistent in voice. Fail: The draft sounds significantly different in register, formality, or directness from the calibration articles.

Gate: Brand Risk Check

Ask: Does this article do anything that could harm the site's credibility, reputation, or relationship with the school board governance community?

Specifically:

Any content that names real people in a negative light (forbidden categorically — but check anyway)

Any content that could be read as partisan or politically aligned

Any content that takes a position on a specific policy issue (curriculum, school choice, etc.) rather than a governance question

Any content that names ESB, AJ Crabill, GOTB, or why-based governance by name (forbidden except in a list of 3+ references, and only 1–2 times per year across the network)

Pass: No brand risks identified. Fail: Any of the above present. Fix before publication.

Gate: Cross-Site Coherence Check

Ask: Does this article contradict anything published on the other 8 sister sites?

This is especially important for:

Positions on board-superintendent role clarity (check against creatingoutcomes.com and effectivegoverningboards.com treatment)

Claims about governance effectiveness (check against schoolboardresearch.com's research-based positions)

Descriptions of ESB practices or why-based governance (check for consistency without naming the frameworks)

Pass: No contradictions with sister site content. Fail: Article contradicts established positions. Resolve the contradiction — do not publish a position that contradicts network-wide standards.

Gate: Uniqueness Check

Ask: Could this article appear on any general governance advice site — BoardSource, National School Boards Association publications, a general leadership blog — without changes?

Pass: The article is meaningfully distinct from what appears on general governance sites. The school board specificity, the ESB practice orientation, and the advisory directness make it unique. Fail: The article is generic enough that it could appear anywhere. Revise to add specificity grounded in school board governance.

Gate: Answers the Question Actually Asked Read the title of the article. Then read the article. Does the article answer the specific question in the title? Not a related question, not the underlying principle behind the question — the actual question.

If the article title asks "What do I do when monitoring data shows no progress?" but the article explains how to set up a good monitoring system, it has answered a different question. Return to Step 3.

Gate: Knowledge Calibration Test Read the article for assumed knowledge. Does it assume too much? (The reader won't know what a "monitoring cadence" means without context.) Does it assume too little? (It shouldn't explain what a board meeting is.)

The target knowledge level: a board member who has served 6–24 months, knows basic vocabulary, has attended governance training but has not done deep independent study. Calibrate accordingly.

Gate: Prescription Test For every section of the article that describes a problem or a dynamic, ask: does the article then prescribe what the reader should do about it?

If the article describes a dynamic accurately but does not prescribe an action — or if the prescription is too vague to act on — it fails. Every described problem must have a prescribed response.

8e. Primary Red-Team (the configured write model)

Primary Red-Team — Single Adversarial Pass (the configured write model)

Run the draft through the configured write model with an adversarial prompt instructing it to:

Challenge every major claim: is this actually supported? Where could a knowledgeable reader push back?

Find logical gaps: does the argument hold together from premise to conclusion?

Flag unsupported assertions: any claim that needs evidence and doesn't have it

Identify reader-hostile moments: where would a skeptical reader stop reading?

Surface structural problems: does the piece earn its conclusion or merely assert it?

Fails if: any major claim is undefended; the argument contains a logical gap; or more than 2 reader-hostile moments are identified. Revise and re-run before proceeding.

8f. Council Red-Team (multi-LLM panel)

Council Red-Team — Multi-LLM Adversarial Panel

Spawn these 4 free OpenRouter models in parallel, each with a distinct adversarial persona. Apply the Section 8 failure protocol: if the council fails, revise the flagged section(s), re-run only the personas that flagged a problem (not all 4), up to 3 retries.

Persona prompts:

Skeptical Practitioner (Gemini): "You are reviewing this piece as a school board practitioner who has seen a lot of governance advice fail in practice. Would this actually work in a real school system? Is this grounded in how governance actually operates, or does it assume conditions that rarely exist? List every claim that feels untested or idealistic, quoting the exact passage."

Hostile Reader (Llama): "You are looking for something to object to. What is the weakest claim? What is most poorly supported? What would make you stop reading? Be specific — quote the exact passage and state the exact objection."

Rival Author (DeepSeek): "Is this saying anything the field does not already know? Is there a genuinely new insight here, or is this a repackaging of received wisdom in different words? What would need to change for this piece to be worth reading over existing work on this topic?"

Editor (Qwen): "Is the argument tight? Are there redundant sections? Does the structure serve the argument or fight it? Is the opening strong enough? Does the conclusion earn its landing? Would you accept this piece as submitted, or send it back with notes?"

Passing criteria: 3 of 4 models must find no major problems. If 2 or more models independently flag the same specific passage or claim, that passage fails regardless of overall score.

8g. Existential Voice Test

Existential Voice Test

Ask: "Would this content appear unchanged on another governance education site, practitioner blog, or AI-generated newsletter?"

If yes: the voice is not distinctive enough. The piece is competent but not AJ's. Identify 2–3 specific passages that read generic and revise them until they could not have been written by anyone else.

Indicators of failure:

Opens with a general statement rather than a specific scene, claim, or reframe

Uses hedged language ("it's important to consider") instead of direct assertion

Could be published without attribution and no one would notice the absence of a byline

SBA-specific existential test: The article must pass a second layer — not just "is this distinctive enough to be AJ's voice?" but "could this article appear only on schoolboardanswers.com?" The specific question, the specific framing, the specific advice, and the specific implied reader must only make sense for a sitting school board member who needs practical help right now.

Pass: Yes — only a school board member asking this specific question in their specific role would find this article. The piece could not appear on creatingoutcomes.com, effectivegoverningboards.com, or any general governance site without changes. Fail: The article would make equal sense for a board member of any type (city council, nonprofit, hospital). Return to Step 2.

This test is subjective. If you would not be surprised to see this exact piece on a competitor site, it fails.

Section 9 — Technical Filing

Jekyll Front Matter

Every article must include the following front matter block at the top of the HTML file, inside a YAML block:

---

layout: qa

title: "[The question, as phrased in the title]"

category: "[one of the approved category values — see below]"

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

layout: Always qa. Do not change this value.

title: The question exactly as it appears as the article header. Include the question mark. Do not truncate.

category: One value from the approved category list below. Choose the most specific applicable category.

Approved Category Values

board-superintendent-relationship

goal-setting

monitoring

budget-and-resources

meeting-conduct

board-member-behavior

board-self-evaluation

community-communication

role-clarity

conflict-navigation

If a new category is genuinely needed (a topic cluster that fits none of these), flag it for AJ review before using it.

File Naming Convention

Directory: qa/

Format: [verb-noun-phrase].html

Rules:

All lowercase

Hyphens between words, no underscores, no spaces

No question marks, no punctuation

Begin with a verb or interrogative word that signals the action or question type

Length: 3–7 words in the slug

Must be unique — check all existing slugs before assigning

Examples:

qa/when-superintendent-pushes-back.html

qa/how-to-read-a-monitoring-report.html

qa/setting-goals-without-consensus.html

qa/redirect-off-topic-board-member.html

qa/governance-vs-management.html

qa/board-role-in-budget-review.html

Not acceptable:

qa/what-should-a-school-board-do-when-the-superintendent-pushes-back-on-questions.html (too long)

qa/tips-for-board-members.html (no verb, too generic)

qa/monitoring_goals.html (underscores)

Directory Placement

File goes in: qa/[slug].html

Do not place in root, subdirectories of qa/, or any other location.

Jekyll Build Check

After filing, run a Jekyll dry build (jekyll build --dry-run or equivalent). Confirm:

No front matter parse errors

No layout errors

No broken internal links

File appears in the expected output path

Commit Format

Commit message format:

Add Q&A: [question title, abbreviated to ~60 chars]

Category: [category value]

Slug: qa/[slug].html

ESB practice: [Focus|Clarify|Monitor|Align|Communicate]

Example:

Add Q&A: What do I do when monitoring data shows no progress?

Category: monitoring

Slug: qa/monitoring-data-shows-no-progress.html

ESB practice: Monitor

Evergreen Standard

Every article on this site must be as useful five years from now as it is today. This means:

No dates. Do not write "as of 2025" or "in recent years" or "increasingly" when referring to trends. Do not mention any year.

No date in the meta div. The <div class="meta"> element in the post header must have its date field omitted or left empty. Do not populate it with a publication date. The Jekyll filename requires a date prefix for ordering, but the template must not display it visually.

No current events. Do not reference specific legislation, court rulings, news stories, or public figures. If a governance situation is related to a recent policy trend, describe the underlying governance dynamic, not the trend.

No jurisdiction-specific law. Do not cite statutes by number, don't say "under [State] law," don't describe legal requirements that vary by state. If legal requirements are relevant, advise the reader to consult their district's legal counsel and move on.

No named current tools or platforms. Do not reference specific software, platforms, or tools that may not exist in a few years.

Present tense for advice. Write "Your board should..." not "Your board will need to begin..."

Duplicate Content Check

Before publishing, perform both checks:

Exact slug check: Confirm the new slug does not exist in qa/

Semantic duplicate check: Confirm no existing article answers the same core question. Search for articles in the same topic cluster and category. If an existing article covers the same ground — even if phrased differently — do not publish. Revise the question to address a genuinely distinct sub-question or gap.

Cross-Site Linking Rules

The 9 sister sites (schoolboardanswers.com, effectivegoverningboards.com, schoolboardreport.com, schoolboardresearch.com, schoolboardreview.com, schoolboardweekly.com, creatingoutcomes.com, governthefuture.com, effective-boards.com) are not promoted as a network in content.

When linking to sister sites:

Maximum 1–2 times per year across all SBA content

Must be embedded naturally in content, never promoted as "related sites" or "our network"

Must appear within a list of 3 or more links — never singled out

The link should be unremarkable — a reader should not notice they are being directed to a related property

When referencing effectiveschoolboards.com or whybasedboards.com:

Same rules: maximum 1–2 times per year

Only within a list of 3+ links

Never singled out, never promoted

ESB / Why-Based Reference Rules

Never name in content:

ESB (the organization)

Effective School Boards (the program name)

AJ Crabill (by name in published content)

GOTB (Governing to Outcomes Boards)

"why-based governance" (as a named framework)

Exception: These may appear in a list of 3 or more resources/references. They may never be singled out as a singular recommendation or authority.

The ESB 5 practices (Focus, Clarify, Monitor, Align, Communicate) are internal scaffolding for content organization. They are never mentioned in published content.

Content Aging Policy

Do not write year references of any kind

Do not write "current" or "today's" when describing governance norms — write "a board in this situation" not "a board today"

Do not use "increasingly," "growing," or "emerging" to describe trends — describe the underlying pattern instead

Do not reference "post-pandemic" or any other event-era reference

Aim for advice that would read as sensible in any decade of school board governance

Section 10 — Independent Review Protocol

Approval flow: Auto-publish

This site uses auto-publish. There is no AJ approval step. The article is published after all quality gates in Section 8 pass. If any gate fails, the generation cycle restarts from the relevant step. Do not publish an article that failed any gate, even if it passed most of them.

If the primary red-team model (the configured write model) is unavailable: Fall back to DeepSeek V4 Flash for the red-team pass. If DeepSeek V4 Flash is also unavailable, hold the article and retry within 72 hours — do not skip the red-team step or substitute a weaker check. After 72 hours without model availability, escalate to the configured write model retry before considering any alternative path.

Section 11 — Learned Rules

Rules derived from post-publication review — patterns found when comparing AI-generated drafts against corrections made during the June 2026 audit of 33 Q&A posts. Each rule represents a recurring error that the generation process should avoid going forward.

LR-001 [2026-06-23] — Use second-person "your board," not third-person "the board" or "boards"

Category: voice Pattern observed: Drafts consistently referred to the reader's board in third person: "boards that drift into management," "the board should ask," "boards face this challenge." This creates a lecture posture rather than a direct address. Rule: Write directly to the reader using "your board" throughout. Replace "the board" with "your board," "boards" with "your board" or "boards like yours," and "board members" with "you" or "your board members" wherever the reference is to the reader's own board. Exception: when describing boards generically as a category ("some boards struggle with…"), third person is acceptable. Frequency: 33/33

LR-002 [2026-06-23] — Every post must end with a "Practical steps" section of 3–5 numbered steps

Category: structure Pattern observed: The vast majority of posts ended with a concluding paragraph or thematic section but no concrete action list. Readers were left with analysis but no operational entry point. Rule: Every Q&A post must end with a section titled "Practical steps" (or "Steps to take") containing 3–5 numbered, concrete steps the reader can act on. Steps should be specific enough to perform — not "improve your monitoring" but "draft a 60-month monitoring calendar that assigns each goal to at least four board meeting months per year." The steps section is the last thing in the post. Frequency: 30/33

LR-003 [2026-06-23] — Goals must be monitored at least 4 times per year, not twice or annually

Category: framework-fact Pattern observed: Multiple drafts stated that goals should be reviewed "at least twice per year," "quarterly or annually," or that "two monitoring cycles is the floor." One draft said goals are reviewed "at least annually." These are all incorrect. Rule: The correct ESB framework frequency for student outcome goal monitoring is at least 4 times per year. Write "at least four times per year" when describing monitoring frequency for goals. Never write "twice per year," "annually," or "once a year" as the standard for goal monitoring. The monitoring calendar should span 60 months (five years, matching the goal timeframe). Frequency: 9/33

LR-004 [2026-06-23] — Monitoring reports have four required elements, not three

Category: framework-fact Pattern observed: Several drafts described monitoring reports as requiring three elements: the goal, current results, and an on-track judgment. This is incorrect — the fourth element (evidence and plan) is required and was consistently omitted. Rule: A monitoring report must include exactly four elements: (1) The Goal — the specific measurable target the board adopted; (2) The Data — results for the three prior reporting periods plus the current period, shown on a line graph with both the annual target and deadline target visible; (3) The Interpretation — the superintendent's judgment of whether the system is on track, off track, or at risk; (4) The Evidence and Plan — supporting documentation behind the interpretation, and if off track, a specific corrective plan with urgency appropriate to the gap. Always write "four required elements" when describing monitoring report structure. Frequency: 8/33

LR-005 [2026-06-23] — Data in monitoring reports must show 3 prior periods on a line graph, plus both targets

Category: framework-fact Pattern observed: Drafts described the data element as "the most recent result alongside the target and prior year" — one year of comparison. This is incorrect. A single comparison period doesn't show trend direction. Rule: The data element of a monitoring report must show results for the three previous reporting periods plus the current period, preferably on a line graph. The graph must also show both the annual target and the deadline target — not just the most recent number. When describing what data a monitoring report should contain, always specify "three prior periods plus current, on a line graph, with both annual and deadline targets marked." Frequency: 5/33

LR-006 [2026-06-23] — Monitoring report length is 1–5 pages, not "one page per goal"

Category: framework-fact Pattern observed: Drafts described monitoring reports as "one page per goal" or "a one-page summary for each goal." The correct specification is a total length of 1–5 pages per report. Rule: When specifying monitoring report length, write "one to five pages" — not "one page per goal" and not "one page." This is the total length of the report for a given goal. Never describe monitoring reports as a per-goal page multiplier. Frequency: 4/33

LR-007 [2026-06-23] — Goal quantity is 1–3 ideal, 5 absolute maximum — never "3–7" or "3–5"

Category: framework-fact Pattern observed: Multiple drafts stated the ideal number of board goals as "three to five" or even "three to seven." Several posts described five goals as a reasonable outer range rather than an absolute ceiling. Rule: The correct ESB framework position on goal quantity is: 1–3 goals is the right range for most boards; five is the hard outer limit. Never write "three to five," "three to seven," or "five to seven" as a recommended range. Write "one to three" as the target and "five" as the ceiling that should never be exceeded. Any post discussing goal quantity must reflect this hierarchy. Frequency: 5/33

LR-008 [2026-06-23] — Guardrails must use negation language: "The superintendent will not…"

Category: framework-fact Pattern observed: Drafts wrote guardrails as affirmative policies ("The district shall maintain…," "The superintendent shall ensure…," "The board will provide…"). Multiple posts failed to use negation form at all, or used "shall not" instead of "will not." Rule: Guardrails must always be written in negation language using the form "The superintendent will not…" — not "The district shall not…," not "The board will require…," not "The superintendent shall ensure…." When providing examples of guardrails, use this exact form. When describing what guardrails are, include the phrase "negation language" or "stated in negation form." The consistent use of "will not" (not "shall not") is part of the correct framework language. Frequency: 8/33

LR-009 [2026-06-23] — In goal-setting step 4, the superintendent drafts interim goals — not the board

Category: framework-fact Pattern observed: At least one post described step 4 of the goal-setting process as the board drafting interim goals. This is incorrect. The superintendent drafts interim goals; the board calibrates against them. Rule: In the ESB goal-setting process, step 4 (Interim Goal Drafting) is performed by the superintendent, not the board. The superintendent drafts three interim goals per proposed goal — SMART, predictive of the main goal, and influenceable by the superintendent. The board's role in this step is to receive and calibrate against the superintendent's drafts, not to write them. Any description of the goal-setting process must attribute interim goal drafting to the superintendent. Frequency: 2/33

LR-010 [2026-06-23] — Monitoring calendar must span 60 months, not one year

Category: framework-fact Pattern observed: Several posts described building an annual monitoring calendar or a calendar covering "the school year." The correct scope is 60 months — the full five-year goal horizon. Rule: When describing how to build or structure a monitoring calendar, specify that it spans 60 months (five years), matching the length of the board's student outcome goals. A one-year calendar is insufficient. Write "60-month monitoring calendar" as the standard. The calendar covers both goals (at least 4x/year) and constraints/guardrails (at least 1x/year) for the full goal period. Frequency: 4/33

LR-011 [2026-06-23] — Guardrails and goals have different monitoring frequencies and agenda placement rules

Category: framework-fact Pattern observed: Several drafts treated guardrail monitoring and goal monitoring identically — same frequency (4x/year) and no distinction in how they appear on the meeting agenda. This is incorrect on both counts. Rule: Student outcome goals are monitored at least 4 times per year and must always appear as full agenda items — never on the consent agenda. Guardrails (constraints) are monitored at least once per year and may be placed on the consent agenda. Any post discussing monitoring frequency or agenda structure must distinguish between these two types: goal monitoring = 4x/year, full agenda item; guardrail monitoring = 1x/year, may be consent agenda. Frequency: 5/33

LR-012 [2026-06-23] — Goal deadlines must be a specific month and year, not just a year

Category: framework-fact Pattern observed: Drafts wrote goal deadlines as "by 2027" or "by 2028." The correct form requires a specific month: "by June 2028." Rule: Always express goal deadlines as a specific month and year — "by June 2028," not "by 2028." When providing example goals, include the month. When describing what makes a goal time-bound, specify that "the deadline should be a month and year, not just a year." This applies to interim goals as well as main goals. Frequency: 6/33

LR-013 [2026-06-23] — Board personnel authority covers only the superintendent — not all staff

Category: framework-fact Pattern observed: A draft implied that the board has personnel authority over staff generally, or suggested the board could direct personnel responses beyond its legitimate scope. Rule: The board's personnel authority is limited to three actions regarding the superintendent: hiring, evaluating, and (if necessary) replacing. All other personnel decisions — assignment, discipline, termination of any other staff — belong to the superintendent. When a post discusses what the board can and cannot do about staff situations, state this explicitly: "Your board's only personnel authority is hiring, evaluating, and if necessary replacing the superintendent." Frequency: 2/33

LR-014 [2026-06-23] — Budget and resource alignment discussions must reference both goals and guardrails

Category: framework-fact Pattern observed: Many budget-related posts described alignment only in terms of goals — "does the budget advance our goals?" — omitting the guardrail side. Budget alignment under the ESB framework requires both: goals shape what resources pursue; guardrails constrain how. Rule: Any post discussing budget alignment, resource allocation, or program evaluation must reference both goals and guardrails. Write "goals and guardrails" rather than just "goals" when describing what the budget should be built against. The guardrail question for budgets is: does the spending honor the superintendent's constraints, not just advance outcome targets? Include this framing in posts about budget alignment, goal-budget sequencing, and program inventories. Frequency: 11/33

LR-015 [2026-06-23] — Do not open with hollow framing sentences that delay the actual answer

Category: anti-slop Pattern observed: Several drafts opened with sentences that restate the problem without advancing the answer: "This is one of the most common governance challenges," "There are usually two root causes," "The good news is that this is solvable." These delay the useful content and signal AI-generated text. Rule: Begin every post with a sentence that answers or directly addresses the question — not a sentence about how common, difficult, or solvable the question is. "Redirect with a question, not a correction" is a good opener. "This is one of the most common governance challenges" is not. The first sentence should tell the reader something they can use. Frequency: 12/33

LR-016 [2026-06-23] — Do not invent statistics or precise timeframes without a grounded source

Category: anti-slop Pattern observed: Some drafts included specific percentages ("boards spend 60–80% of time on operations"), research references ("governance research suggests…"), and precise timeframes ("within 18 months") that were not grounded in verifiable sources or ESB framework facts. Rule: Do not write invented statistics, precise percentages, or specific timeframes unless they are verifiable ESB framework facts (e.g., "at least four times per year," "1–5 pages," "1–3 goals"). Avoid phrases like "research shows," "studies suggest," or "governance research indicates" unless the claim is from the ESB framework itself. When a claim requires a number that isn't in the framework, express it qualitatively: "most boards," "often," "typically" — not a fabricated percentage. Frequency: 7/33

LR-017 [2026-06-23] — Use governance-precise language; avoid "strategy" for board-level structures

Category: voice Pattern observed: Several posts used "strategy" to describe what the ESB framework calls specific structures: "communication strategy" for an accountability obligation, "community engagement strategy" where the framework calls for a guardrail, "monitoring strategy" where the framework calls for a monitoring calendar. Rule: In governance contexts, prefer specific framework language over generic "strategy": use "guardrail" not "policy or strategy"; use "monitoring calendar" not "monitoring strategy"; use "accountability obligation" not "communication strategy." Reserve "strategy" for the superintendent's operational domain — how the superintendent plans to achieve goals is a strategy; the board's governance structures are not called strategies. Frequency: 5/33

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"