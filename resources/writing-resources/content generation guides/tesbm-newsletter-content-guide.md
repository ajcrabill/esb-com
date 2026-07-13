title: TESBM Newsletter — Content Creation Guide type: content-guide site: TESBM (newsletter) updated: 2026-07-08

For AI use and reviewer use: This document is the complete operational specification for generating and reviewing weekly newsletter issues of The Effective School Board Member (TESBM). Read it in full before generating or approving any issue. Never deviate from parameters defined here — if a question is not answered by this document, do not publish; flag for human review.

ESB Language, Terminology & Mechanics (binding)

This section is binding for all generated content. Where anything below conflicts with older instructions in this guide, this section wins. The full standard is esb_writing_style_guide.md in the canonical guides folder.

Mechanics. No em-dashes. Where an em-dash would go, use a spaced double-hyphen ("--"), sparingly, or split the sentence. No en-dashes (use a hyphen, including in ranges like "1-2"). No semicolons in body prose. Straight quotes only. Oxford comma. No horizontal rules.

ESB terminology, never Policy Governance terms. Goals, not Ends. Guardrails, not Executive Limitations. Governing, not Governance Process. Delegation, not Board-Management Delegation. Never describe ESB as built on or adopted from Policy Governance. It is grounded in "principles of a policy-based approach to governance." Never write "SOFG," "Student Outcomes Focused Governance," "Policy Governance," "PG," "Lone Star Governance," or "LSG" (exception: SOFG only when intentionally contrasting with ESB). Use "board chair," not "board president." Use "Practitioner," not "coach," for the certified role. Spell out "Any Reasonable Interpretation" (never "ARI"). Use "own conduct," not "own-conduct." Four board-adopted policy types only: Goals, Guardrails, Delegation, Governing (no "Policies About X" category). ESB is prioritized (1-3 policies) in Goals and Guardrails and exhaustive in Delegation and Governing. A Goal is always a student outcome.

Governance language to avoid (describe the specific behavior instead): "micromanage," "rubberstamp," "stay in your lane," "good/bad/right/wrong" as judgment (even affirmatives like "the right framing"), power-over framings, "district"/"school district" (say "school system" in reader-facing content -- a questioner's own words, direct quotes, and operational or data references to a specific entity may keep it), "equity" as a bare term, "achievement gap," politically-coded terms, and "non-essential activities" for what a board could otherwise do.

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Publication name: The Effective School Board Member (TESBM) Platform: beehiiv (draft staging); human must approve before beehiiv publishes Content type: Weekly email newsletter Generation cadence: Pipeline runs Thursday, Sunday, Tuesday — each run produces one issue targeted ~28 days out Effective publication cadence: Weekly

Purpose: Provide practicing school board members with practical, ESB-framework-aligned coaching delivered as an actionable weekly newsletter. Each issue helps board members distinguish governance from management, anchor their work to student outcomes, and build habits of effective oversight — via Q&A, curated reads, board meeting analysis, and governance resources.

One-sentence purpose: Coach school board members toward more effective governance through weekly Q&A, curated resources, and real board meeting analysis grounded entirely in the ESB (Effective School Boards) framework.

Target audience: Active and aspiring school board members across the United States. Readers are practitioners, not researchers. They have limited time, real governance decisions to make, and often confuse governance with management. Many are newer board members; some are experienced chairs. The newsletter must be useful to both without being condescending to either.

Voice: Coach's voice — direct, practical, conversational without being casual, ESB-framework-aligned. Uses contractions. Uses Oxford comma. Uses no em-dashes; where an em-dash would go, use a spaced double-hyphen ("--") for parenthetical thoughts, sparingly, or split the sentence. No bullet lists or numbered lists in Q&A answers. Speaks to the reader as a thinking professional, not as a student. Never preachy. Never academic. Never editorial on non-governance topics.

What distinguishes TESBM from sister sites:

effectivegoverningboards.com (EGB) publishes academic policy briefs with APA citations for governance researchers — TESBM is practitioner-focused, school-board-specific, and written in a coach's voice with no citation apparatus

schoolboardanswers.com (SBA) is a static Q&A library in plain language — TESBM is a live weekly newsletter with curated current content, board meeting analysis, and a coaching relationship embedded in tone

creatingoutcomes.com (CO) covers outcome-focused governance in Q&A format — TESBM covers all ESB framework dimensions, not just outcomes, and additionally provides current governance news, curated reads, and real meeting analysis

schoolboardweekly.com (SBW) is a journalism-style newsletter covering school board governance news nationally — TESBM is a coaching newsletter; SBW reports what boards are doing, TESBM coaches boards on what to do

TESBM is ESB-framework-specific — sister content sites are not ESB-branded

Critical framing to internalize: TESBM exists inside a coaching relationship. The voice is that of a trusted coach speaking to a board member who wants to improve. Every element of the newsletter — from Q&A answers to board meeting analysis — should reinforce this relationship. The reader should finish each issue feeling more capable of doing their governance work well.

Content Goals

What a successful issue accomplishes:

Answers 3–5 practical governance questions in the coach's voice, grounded in ESB framework principles, at a level of specificity that gives the reader something they can actually apply

Provides 4 curated reads, listens, or watches that a board member would genuinely find useful and that pass the governance-only filter

Includes a board meeting analysis from a real recent meeting that models good governance observation and coaching

Surfaces one upcoming webinar or professional development opportunity relevant to board members

Offers bonus materials (eval PDF, video, ESB resource picks) gated for paid subscribers

Leaves the reader feeling that reading this newsletter made them better at their job

What a failed issue looks like:

Voice failure: Answers use bullet lists, numbered lists, academic language, or a lecturing tone. The coaching relationship is absent — the reader feels informed but not coached.

Governance drift: Q&A answers or news items address curriculum, teacher compensation, building projects, or other management/operational topics rather than governance. The governance/management line is not actively maintained.

ESB fidelity failure: Q&A answers contradict or ignore ESB framework principles. The answer tells a board member to do something the ESB framework explicitly prohibits, or fails to acknowledge ESB NEVER rules when they apply.

Slop contamination: Q&A answers contain AI-tell phrases, hollow intensifiers, or mechanical-sounding constructions that break the coaching voice.

Reframe failure: Q&A answers open with a direct response to the question as framed rather than reframing the question first. Every ESB-framework answer should reposition how the board member is thinking about the problem, not just answer the problem as presented.

Geographic stagnation: Multiple consecutive issues feature the same state or region for board meeting analysis. The geographic rotation is not being honored.

Dedup failure: Q&A questions substantially duplicate questions answered in the past 6 months. Fresh framing on an old issue may be acceptable after 6+ months; essentially the same question within 6 months is a failure.

Rough draft not labeled: The assembled newsletter HTML does not begin with "Rough Draft - " in the title. AJ must edit before publishing; an unlabeled draft may be mistaken for a final issue.

Content Format and Structure

Every issue follows this structure in this order:

1. Q&A Section

3–5 Q&A pairs (pipeline generates 5–7 candidates; AJ cuts to 3 before publishing)

Each answer: 150–250 words

No bullets, no numbered lists, prose only

Optional ACTION ITEMS block at end of each answer: ACTION ITEMS: [item] | [item] | [item]

Questions are drawn from governance-only news filtered through the ESB framework

2. Interesting Reads & Listens

4 items (pipeline generates 10 candidates; AJ cuts to 4 before publishing)

Mix: articles (Education Week, The 74, Chalkbeat, NASB, etc.), podcasts, YouTube videos

Governance-only filter: no curriculum, no teacher compensation, no building projects

Each item: title, source, brief description of why a board member would care

3. Board Meeting Analysis

Real, verified school board meeting from the geographic region assigned to this run day

Time use analysis: agenda items classified by governance category

Stats table: time breakdown by category

Coach Celebrates / Coach Recommends: 2–3 items each

District identified by state only in the public newsletter (district name in pipeline data only)

Analysis generated from actual meeting transcript via audio extraction + LLM analysis

4. Upcoming Opportunities

1 webinar or professional development event relevant to board members

Date is always the 2nd Friday of the next calendar month

Registration link included

5. Bonus Materials (paid subscribers only)

Meeting Analysis PDF (formatted board evaluation document)

Link to meeting video

Agenda link

Strategic plan link

2–3 ESB guidance PDF picks from the catalog

Eval request link for board self-evaluation

6. Free Section

Same four bonus items as plain text without links (for free subscribers)

Delimited by HTML comments for the beehiiv tier logic

Title Format:

Rough Draft - {DayName} {Month} {D} {Year}

Examples:

Rough Draft - Thursday June 26 2026

Rough Draft - Sunday June 29 2026

The "Rough Draft - " prefix is mandatory. This is a hard safety requirement. AJ must review and edit each issue before publishing. An issue without this prefix should be treated as a generation error.

Word Counts:

Q&A answer: 150–250 words (hard range; flag if outside)

Board Meeting Analysis newsletter summary: ~230 words

Reads/listens descriptions: 1–2 sentences each

Opportunity description: 2–3 sentences

Forbidden Patterns:

No bullet lists in Q&A answers

No numbered lists in Q&A answers

No academic citations or footnotes

No first-person plural ("we," "our") in Q&A answers

No second-person plural ("you all," "your board") — address the individual reader

No preachy moralizing on non-governance topics

No curriculum, personnel, or operational content framed as governance

No unicode em-dashes ( — ) — where an em-dash would go, use a spaced double-hyphen ("--"), sparingly, or split the sentence

No curly/smart quotes — must be straight quotes in HTML

No ESB NEVER rule violations (see NEVER Rules below)

In-Bounds Content

Governance-Only Filter

Every Q&A question, every news item, and every curated read must pass the governance-only filter. TESBM covers what boards should be doing as boards — not what schools should be doing operationally.

In-bounds governance topics:

Board goal setting: how boards set, monitor, and report on student outcome goals

Superintendent evaluation: how boards conduct evaluations, what criteria belong in evaluations, how to separate evaluation from micromanagement

Board conduct: member conduct, decorum, conflicts of interest, executive session rules, public comment management

Board-superintendent relationship: role clarity, appropriate channels of communication, authority boundaries

Strategic planning: board's role in establishing direction vs. superintendent's role in implementation

Community engagement policy: how boards receive public input, how boards communicate decisions

Board self-assessment: boards evaluating their own governance effectiveness

Board governance training and professional development

Transparency and public records: board obligations, not staff obligations

Board meeting management: consent agendas, work sessions, special meetings, executive sessions

Board elections and candidate preparation (governance framing only)

State and federal policy with direct board governance implications

Borderline — acceptable only with governance framing:

Budget: the board's role in approving and monitoring the budget at a strategic level, not budget line-item detail

Staff compensation: only in the context of the board setting compensation policy at a strategic level, not individual salary decisions

Academic programs: only when the board is evaluating outcome data, not when the board is making instructional decisions

The test for borderline topics: Is this about what the board does as a governing body, or is this about what the school system does operationally? If the latter, it is out of bounds. The board sets direction and monitors outcomes; staff implements.

ESB Framework Alignment

All Q&A content must be grounded in or at minimum consistent with the Effective School Boards (ESB) framework. Key ESB framework principles that appear frequently in Q&A:

Student outcome goals: Boards set specific, measurable goals tied to student learning outcomes (not activities, not inputs, not engagement)

Governance vs. management: The board governs; the superintendent manages. Boards do not direct staff, select curriculum, or make operational decisions.

Superintendent evaluation: Boards evaluate the superintendent on progress toward board-established student outcome goals — not on personality, relationships, or activities

Board-superintendent relationship: Communication through the superintendent, not around the superintendent; no individual board member directives to staff

Boards speak through policy: Boards act through adopted policy, not through individual member action

Community as values source, not as decision authority: Boards gather community input on values and priorities; the community does not vote on governance decisions

Geographic Rotation

Board meeting analysis rotates across three geographic regions tied to pipeline run day:

Thursday: West & Southwest

Sunday: Midwest & South Central

Tuesday: Northeast & Southeast

No district should appear in the meeting analysis more than once every 90 days. Districts from the previous two runs in the same region should be avoided. This rotation ensures national coverage over time.

Out-of-Bounds Content

Management Disguised as Governance

The single most common failure mode. These topics are out of bounds regardless of how they are framed:

Hard out-of-bounds:

Curriculum selection, adoption, or review (instruction is management)

Teacher hiring, evaluation, or compensation (HR is management)

School building projects, construction, facilities decisions (operations)

DEI program design or implementation (program design is management)

Discipline policy implementation (implementation is management)

Extracurricular activities, sports programs (operations)

Budget line-item decisions (line items are management; total budget adoption is governance)

Test: If the superintendent could make this decision without the board, it is management. If the decision requires board action by law or policy, it may be governance. If a board member asking about this topic is really trying to direct staff action, it is management disguised as governance.

Non-Governance News

News items for the Reads & Listens section must pass the same governance-only filter. The following are out of bounds for the news search:

Curriculum debates or book challenges

Teacher strikes, contract negotiations, salary disputes

Building projects, bond elections (unless the governance angle is the board's fiduciary role)

DEI controversy (unless the controversy involves board conduct specifically)

Student achievement data as a standalone story (unless the story is about how the board is using or failing to use the data)

The test: would an education journalist cover this as a story about a school board doing its governance job? If the story is really about what a school is doing — not what a board is doing — it is out of bounds.

Source and Research Standards

News and Reads Sources

Perplexity (sonar-pro) is the primary source for:

Current governance-only school board news (2-week lookback)

Reads, listens, and watches recommendations

Acceptable article sources for curated reads:

Education Week

The 74

Chalkbeat

NASB (National Association of School Boards)

AASA (School Superintendents Association)

RAND Corporation reports

Brookings Education (governance angle only)

State school board association publications

University-based education policy centers

Acceptable podcast sources:

School board governance podcasts

Education leadership podcasts with governance angle

Public sector governance podcasts

Unacceptable sources:

Opinion/advocacy pieces on curriculum, DEI, or political topics

Teacher union materials

Individual district newsletters or blogs

Social media (Twitter/X, Facebook, etc.)

ESB Source Documents

Q&A answers draw on the ESB source document corpus available to the pipeline. Key documents:

Board Work vs. Superintendent Work

Inputs, Outputs, and Outcomes

Effective Goal Setting Policy

Effective Goal Monitoring

Effective Superintendent Evaluation Process

Q&A answers must be consistent with these documents. When an answer touches on a topic covered in these documents, it should reflect the ESB framework's position, not a generic governance position.

Board Meeting Video Verification

The meeting used for the Board Meeting Analysis section must be:

A real, verifiable school board meeting (Granicus/Swagit listing or YouTube)

Recent (within the past 2–3 weeks)

From the geographic region assigned to this run day

From a district not used in the past 90 days

Reachable via URL (verified before transcript extraction)

Meeting verification uses the Granicus/Swagit listing page scrape + fallback to known listings. A meeting that cannot be verified as real or recent must not be used — fall back to a known listing from the same region.

ESB PDF Catalog

2–3 ESB guidance PDFs from the static catalog are selected each issue based on relevance to the week's Q&A topics and reads. The selection logic uses DeepSeek Flash to match catalog items to the week's themes. If catalog Drive IDs are unpopulated, the pipeline falls back to two default items.

Grounding Document

Source: Great on Their Behalf (3rd edition) by AJ Crabill Access: Google Drive ID: 1KwiTQKLZlRDnTCzDmHaleeU3IVj_cHbsmA2s6nORdkE (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: c — pre-draft AND post-draft

Pre-draft: Before drafting, read the relevant sections of the grounding document. Use it to calibrate frame, vocabulary, and core claims before writing begins.

Post-draft: After completing all quality checks, verify the finished piece against the grounding doc: confirm no claims contradict it, vocabulary is consistent, and the piece would not confuse a reader who knows the book well. This is done as Section 8h.

Voice Register

Register: ajc-short — ~14 words/sentence average, 2–4 sentence paragraphs, Sinek 30% / Gawande 30% / Collins 20% / Gladwell 20%

The Coach's Voice

TESBM operates inside a coaching relationship. Every Q&A answer is written as if a trusted, experienced governance coach is speaking directly to a board member who asked a good-faith question. The voice has these properties:

Direct without being dismissive. The question is always taken seriously, even when the framing needs to be challenged.

Practical. The answer should give the board member something they can do differently on Monday.

ESB-framework-aligned. The answer doesn't just tell the board member what to do — it connects the advice to governance principles they can internalize.

Contractions. "You're" not "you are." "It's" not "it is." "Don't" not "do not."

Oxford comma. Always.

No em-dashes. When setting off a parenthetical -- like this -- use a spaced double-hyphen ("--"), sparingly, or split the sentence. No unicode em-dashes ( — ).

Straight quotes in HTML. Not curly/smart quotes.

No bullets or numbered lists in answers. Coaching conversations do not come in bullet points.

Corpus-Validated Reframe Patterns

Every Q&A answer must open with a reframe of the question before answering it. The reframe repositions how the board member is thinking about the problem. Approved reframe patterns (must open with one of these or a close variant):

"It depends on what you mean by..."

"Your framing of X is well-intended, but it can have unintended consequences..."

"The question assumes X, but the more useful question is..."

"There are actually two different things being asked here..."

"The real issue isn't X — it's..."

"Before I answer that, I want to name something..."

"That's a question I hear a lot, and the short answer is yes — but the way you do it matters enormously..."

Why reframing is required: Most governance mistakes happen because board members are asking the wrong question. A coach's first job is to help the board member see the question differently before advising on the answer. An answer that takes the question as-given and responds to it literally is not coaching — it is answering a test question.

Mechanical Voice Rules

These are enforced by the pre-gate scanner before LLM quality gates run:

AI-tell phrases that trigger a rewrite flag:

"delve into"

"in conclusion" / "in summary" as answer openers

"it is worth noting that"

"it is important to note"

"this underscores" / "this highlights"

"plays a crucial role"

"a nuanced understanding"

"the landscape of"

"a cornerstone of"

"navigating the complexities of"

"a multifaceted approach"

"foster a culture of"

"it's important to remember"

"at the end of the day" (trite)

Hollow intensifiers that must be replaced with specific language:

"crucial," "critical," "essential," "vital," "fundamental" used as pure decoration

"robust," "comprehensive," "transformative," "impactful"

NEVER Rules

The following positions appear in ESB source documents as explicit prohibitions. Q&A answers must never advise a board member to do these things, and must actively redirect if a question assumes they are acceptable:

NEVER direct staff. Board members do not give instructions to staff members other than the superintendent.

NEVER micromanage. Board members do not make operational decisions, select programs, or second-guess implementation choices.

NEVER make individual board member decisions. Individual board members have no governance authority — authority rests with the board as a body, through votes.

NEVER evaluate the superintendent on non-outcome criteria. Character, likability, effort, or relationship quality are not legitimate evaluation criteria.

NEVER set goals for activities or inputs. Board goals must connect to student learning outcomes, not to program activities or resource deployment.

When a question implicitly assumes one of these things is okay, the Q&A answer must reframe before answering. The answer cannot validate the false premise.

Generation Process

Before beginning Step 1, complete the grounding doc pre-draft alignment per the Grounding Document section above.

Step 1 — Video Discovery

Find a real, verified school board meeting from the region assigned to this run day.

Phase A: Query Perplexity for the district's Granicus/Swagit listing page (not a specific video URL — the listing page is stable)

Phase B: Scrape the listing page to extract the most recent non-cancelled clip URL; verify URL is reachable

Fallback: use known Granicus/Swagit listing from the KNOWN_LISTINGS regional dict

Check geographic log: avoid districts used in the past 90 days

Record successful district in geographic log

Step 1b — District Link Collection

Run three parallel searches for the selected meeting:

Agenda URL (scraped from Granicus listing page near the clip ID)

Strategic plan URL (Perplexity search for district's strategic plan document)

YouTube URL (Perplexity search for YouTube recording of the same meeting)

Returns: agenda_url, strategic_plan_url, strategic_plan_title, youtube_url, video_url.

Step 1c — Eval PDF Upload

Fetch the eval PDF from esby-portal (which converts eval docx on the fly) and push it to schoolboardreview.com/evals/ via git commit. Returns eval_pdf_url.

Step 2 — Time Use Analysis

Extract the meeting transcript via yt-dlp + faster-whisper audio extraction. Run 3-stage LLM analysis:

Extract agenda items from transcript

Classify each item by governance category (using the Time Use Classification Guide)

Compute totals + generate coaching reflections (Coach Celebrates / Coach Recommends)

Generate ~230-word HTML summary for the newsletter using DeepSeek Flash:

<h3>Board Meeting Analysis</h3>

Stats table (time by category)

Coach Celebrates section

Coach Recommends section

District name is replaced by state name only in the public newsletter.

Classification accuracy is critical. Common misclassification error: categorizing activities as goal-focused when they are not. Goal-focused means the board is reviewing student learning outcome data against its adopted goals. A board discussing attendance reports, benchmark data, or program updates is not doing goal-focused work unless those items are tied to explicit adopted student outcome goals. Consult the Time Use Classification Guide for all close calls.

Step 3 — News Search

Query Perplexity for 20 governance-only school board news stories from the past 2 weeks.

Strict governance-only filter (must apply, cannot be relaxed):

In-bounds: board policy, goal setting, superintendent evaluations, board conduct, transparency, community engagement policy, strategic planning, board elections, board-superintendent relationship

Out-of-bounds: curriculum debates, teacher salaries, building projects, DEI implementation debates, student activity stories

Fallback: if Perplexity fails, use DeepSeek Flash to synthesize governance news from its training data (clearly marked as non-current in pipeline data).

Step 4 — Question Refinement

Transform news items into actionable governance questions phrased as what a board member might ask their coach. Batch in groups of 10 using DeepSeek Flash.

Prioritize questions that reference states in this week's geographic region (same region as the board meeting analysis). Return up to 15 candidate questions.

Each question should be:

Specific enough to have a real answer

Phrased from the board member's perspective ("Should I..." "How do I..." "What should our board do when...")

Actually about something a board does, not what a school does

Step 5 — Deduplication

Check candidates against the past 12 months of published Q&As in the TESBM database.

Dedup rules:

Same core governance issue within the past 6 months: skip

Same core governance issue 6–12 months ago: skip unless the new question has a meaningfully different angle (new law, new context, different aspect of the same issue)

Questions from 12+ months ago are eligible for fresh treatment

Use DeepSeek Flash for semantic similarity assessment (not just string matching). Return up to 7 non-duplicate questions.

Step 6 — Q&A Writing

Write answers for the surviving candidate questions. Apply full quality gate protocol (see Site-Specific Checks in the Quality Checks section below).

Model sequence: MiniMax M2.5 (attempt 1) → Claude Opus 4.8 (attempts 2 and 3, with accumulated gate feedback).

Enforce for each answer:

150–250 words

Opens with corpus-validated reframe pattern (see Voice Register section)

No bullets, no numbered lists

No em-dashes (use a spaced double-hyphen "--", sparingly), straight quotes, contractions, Oxford comma

Optional ACTION ITEMS block: ACTION ITEMS: [item] | [item] | [item]

Pipeline writes 5–7 answers. AJ cuts to 3 before publishing.

Step 7 — Reads, Listens, Watches

Query Perplexity for 10 governance-related reads/listens/watches. Avoid region used for the board meeting analysis this week.

Mix requirements:

4–5 articles from governance-approved sources

2–3 podcasts

2–3 YouTube videos

All items pass the governance-only filter (see Site Context section). All items are from current week or recent past (not evergreen library items).

Fallback: DeepSeek Flash synthesis if Perplexity unavailable.

Pipeline generates 10. AJ cuts to 4 before publishing.

Step 8 — ESB PDF Selection

Select 1–3 ESB guidance PDFs from the static catalog most relevant to this week's Q&A topics and reads topics. Use DeepSeek Flash to match catalog items to week's themes.

Catalog includes:

Board Work vs. Superintendent Work

Effective Goal Setting Policy

Effective Goal Monitoring

Effective Superintendent Evaluation Process

Inputs, Outputs, and Outcomes

Other ESB source documents (catalog populated after indexing)

If selection fails or Drive IDs are unpopulated: fall back to two default items.

Step 9 — Webinar Opportunity

Generate one webinar or professional development opportunity relevant to board members based on the week's hottest Q&A or reads topic. Use DeepSeek Flash.

Date: always the 2nd Friday of the next calendar month (computed at runtime). Fallback: goal-monitoring webinar.

Step 10 — Assembly

Assemble the full newsletter HTML in this order:

Q&A section (5–7 Q&As, note to AJ to cut to 3 before publishing)

Interesting Reads & Listens (10 candidates, note to AJ to cut to 4)

Board Meeting Analysis (Step 2 HTML, state name only for district)

Upcoming Opportunities (webinar with registration link)

Bonus Materials/paid section (eval PDF, video, agenda, strategic plan, ESB PDF picks, eval request link)

Free section (same four items as plain text, no links, delimited by HTML comments)

Title: Rough Draft - {DayName} {Month} {D} {Year}

Step 11 — Queue

Save the assembled newsletter to the esby-portal approval queue (newsletter_drafts table in pipeline.db). Scheduled 28 days from run date. Also record in TESBM database (beehiiv_posts table, status queued).

Hard safety check: title must start with "Rough Draft - ". If this check fails, abort and log the error. Do not save a newsletter without this prefix.

Does NOT post to beehiiv. Does NOT publish automatically. Human approval required.

Quality Checks

Quality Check Failure Protocol

This protocol governs every check in Section 8 (8a through 8h, including all site-specific gates in 8d).

On any failure at any check:

Identify the specific violation — which rule, which tier, which gate, and exactly what was wrong

Revise only the affected portion of the draft to address that specific failure

Re-run the check that failed (not the full Section 8 — just the failing check)

Track the attempt count per check

Retry limit: 3 revision-and-retry cycles per check. If a check passes on retry, continue to the next check normally.

Ultimate Failure: if a check still fails after 3 retries, declare an ULTIMATE FAILURE for that check. Stop all further quality checks immediately. Do not publish, commit, or submit the draft. Proceed to ultimate failure reporting (below), then preserve the draft and full failure log — including stage name, attempt count, nature of each failure, and each revision attempt — in a dated file for AJ's review.

Ultimate Failure Reporting — TESBM: Do NOT send to beehiiv or advance for AJ approval. Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (TESBM), question/topic, which gate or check failed, attempt count, failure details, and the draft. Mark status as FAILED. AJ will review and decide whether to intervene manually.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Satisfied by Pre-Gate + Gate 3 in Section 8d. See site-specific checks below. The Pre-Gate mechanical scan catches regex-flagged AI-tell phrases before LLM gates run, and Gate 3 LLM slop/AI-tell scan catches remaining AI-tell patterns not caught mechanically. Together these two gates constitute the full anti-slop requirement for TESBM.

8b. Voice Check

Satisfied by Gate 1 in Section 8d. Gate 1 runs a full High Fidelity voice score including NEVER rules, fingerprints, rhythm, reading level, and register match against the ajc-short profile. Threshold: ≥ 0.90.

8d. Site-Specific Checks

TESBM uses a four-gate quality system with a mechanical pre-gate scan. All gates apply to Q&A answers. Run the pre-gate scan first, then all four gates.

Pre-Gate: Mechanical Slop Scan

Run regex-based scan against the Q&A bank before submitting to LLM gates. Flags AI-tell phrases (see Voice Register — Mechanical Voice Rules). Any flagged answer proceeds to LLM gates with the flag noted — if the LLM gates score it highly despite the flagged phrase, a human reviewer should make the final call on that specific phrase.

Also run the following cleanup checks at pre-gate before LLM gates:

Check: Reframe Pattern Presence Verify every Q&A answer opens with a corpus-validated reframe pattern (see Voice Register section). If an answer opens with a direct response to the question as framed, it has failed this check regardless of the quality of the rest of the answer. Flag for rewrite.

Check: List Detection Flag any Q&A answer containing:

A bullet-point list

A numbered list

A dashed list (using hyphens as list markers)

A lettered list (a. b. c.)

Replace with prose. Lists are a hard fail in TESBM Q&A answers.

Check: Hollow Intensifier Scan Flag all instances of: "crucial," "critical," "essential," "vital," "fundamental," "robust," "comprehensive," "transformative," "impactful" used decoratively. Replace with specific language. Ask: what is actually being said here? Say that instead.

Check: Action Items Formatting If action items are present, verify format: ACTION ITEMS: [item] | [item] | [item]. No line breaks within the action items block. No bullets. Each item is a short, concrete action the board member can take. Not observations — actions.

Gate 1: Voice Score (≥ 0.90)

LLM evaluator assesses whether the answer sounds like an experienced governance coach speaking conversationally. This gate constitutes the full voice check requirement (see Section 8b). Penalizes:

Bullet lists or numbered lists (hard fail if present)

Academic or bureaucratic register

Absence of contractions

Missing or weak reframe at the opening

Preachy or lecturing tone

Register mismatch against the ajc-short profile (Sinek 30% / Gawande 30% / Collins 20% / Gladwell 20%)

Failure to honor NEVER rules in tone

Sentence rhythms that do not conform to ~14 words/sentence average

Reading level that drifts too academic or too simplistic for practicing board members

An answer that opens with the question's literal premise, then provides a listicle of advice, will fail this gate regardless of the accuracy of the advice. Threshold: score ≥ 0.90.

Voice Consistency (across the Q&A bank): Read the Q&A bank as a set, not individual items. Ask: does this sound like the same coach speaking in each answer? Voice consistency across answers matters. If one answer is notably more formal or more casual than the others, flag for tone normalization.

Gate 2: ESB Fidelity

LLM evaluator checks the answer against ESB framework principles and NEVER rules. Hard fails:

Answer advises a board member to take individual action that bypasses the superintendent

Answer validates micromanagement of staff or programs

Answer frames activity-based goals as acceptable board goals

Answer suggests the superintendent should be evaluated on criteria other than student outcome goal progress

Answer does not redirect when the question assumes an ESB NEVER rule is acceptable

Answer is technically correct but fails to connect the advice to why it matters for student outcomes

An answer can be factually accurate and still fail ESB fidelity if it answers in a framework-agnostic way.

TESBM-Specific ESB Check A — Geographic Reference Accuracy: If a Q&A answer references a specific state, law, or policy context, verify that the reference is accurate. State-specific governance laws vary significantly. Inaccurate state references are a credibility failure.

TESBM-Specific ESB Check B — Board vs. Member Distinction: Flag any answer that conflates "the board" (a collective body that speaks through votes) with "a board member" (an individual with no independent authority). Common error: "You should ask the superintendent to..." — this is fine if it means asking at a board meeting; it is a governance error if it means contacting the superintendent directly as an individual.

TESBM-Specific ESB Check C — ESB NEVER Rule Compliance: Flag any Q&A answer that, upon plain reading, would leave a board member thinking:

It is acceptable to direct staff other than the superintendent

Individual board members have authority to act alone

Superintendents should be evaluated on activity, effort, or likability

Board goals about programs or activities are acceptable substitutes for student outcome goals

These are ESB NEVER rule violations. Flag and rewrite to correct.

Gate 3: Slop/AI-Tell Scan

LLM evaluator identifies remaining AI-tell phrases not caught by the pre-gate and assesses whether the answer sounds like it was written by a machine trying to sound authoritative. This gate, together with the Pre-Gate mechanical scan, satisfies the full anti-slop requirement (see Section 8a). Specific targets:

Generic governance platitudes with no specificity

Vague claims about "research" or "evidence" without any specific grounding

Sentences that are structurally correct but semantically empty

Repetition of the question's premise back to the reader as if it were an insight

Gate 4: Source Document Fidelity

LLM evaluator checks whether the answer is consistent with the ESB source documents available in the pipeline (Board Work vs. Superintendent Work, Inputs-Outputs-Outcomes, Effective Goal Monitoring, Effective Goal Setting, Effective Superintendent Evaluation Process, etc.). Specific checks:

Answer does not contradict ESB source doc definitions

Answer correctly applies the governance/management distinction as defined in ESB sources

If the answer cites or implies an ESB principle, it states that principle correctly

Model Sequence for Gate Failures:

First attempt: MiniMax M2.5

Second attempt (if Gate 1 or 2 fails): Claude Opus 4.8, with Gate 1 and Gate 2 failure feedback woven into the prompt

Third attempt (if second attempt fails): Claude Opus 4.8, with all gate feedback from both prior attempts accumulated in the prompt

After three failed attempts: Question is dropped from the candidate pool for this issue. A note is added to the quality log.

Quality score threshold: all four gates at passing level. An answer that passes Gates 2, 3, 4 but fails Gate 1 (voice) is not publishable — voice is foundational to the coaching relationship.

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

This test is subjective. If you would not be surprised to see this exact piece on a competitor site, it fails.

8h. Grounding Doc Post-Draft Alignment (usage c)

Grounding Doc Post-Draft Alignment

Access the grounding document (Great on Their Behalf (3rd edition) by AJ Crabill) and verify:

No claim in the finished piece directly contradicts a claim or framework in the grounding doc

Key terminology is consistent — if the book uses a specific term, the piece uses it the same way

A reader who knows the grounding doc well would not be confused or jarred by this piece

The piece reinforces the grounding doc's core intellectual framework rather than drifting from it

This is not a citation check. The piece does not need to cite the grounding doc. It is an alignment check: does the piece fit within the same intellectual ecosystem?

Fails if: any direct contradiction is found; any significant terminology drift exists; or the piece would confuse a reader who knows the book.

Technical Filing

Pre-Publish Checklist (Pipeline)

Title begins with "Rough Draft - " — hard safety gate; abort if missing

All Q&A answers passed all 4 quality gates

Board Meeting Analysis uses state name only (no district name in public content)

Board meeting URL verified as reachable before transcript extraction

Geographic log updated with this run's district

Scheduled_for date is 28 days from run date (not current week)

Saved to newsletter_drafts table in pipeline.db with status pending

Recorded in TESBM database with status queued

Does NOT post to beehiiv — human approval required

Reviewer Checklist (Admin Portal)

When reviewing a TESBM draft in the content approval portal, check:

Title starts with "Rough Draft - " followed by correct date format

Q&A answers open with a reframe, not a direct answer

No Q&A answer contains bullet lists or numbered lists

Voice sounds like a coach, not an academic or a bureaucrat

Board Meeting Analysis identifies only the state, not the district name

Reads/listens items are governance-related (not curriculum, not teacher issues)

No ESB NEVER rules are violated in any Q&A answer

Webinar opportunity date is the 2nd Friday of the next month

Bonus materials section is present and properly gated

Free section is present and delimited

Approval Triggers Beehiiv Upload

When a reviewer approves a newsletter draft in the admin portal:

The draft content is uploaded to beehiiv as a draft post (not immediately sent)

AJ must then log in to beehiiv to:

Edit down Q&As to 3 before publishing

Edit down reads to 4 before publishing

Review and finalize the complete issue

Schedule or manually trigger the send

Approval in the portal ≠ published newsletter. It means: this draft is ready for AJ's final edit in beehiiv.

beehiiv Technical Requirements

Status on upload: draft

Audience: free (beehiiv handles tier gating for paid content sections)

Authors: empty array (newsletter is unattributed in beehiiv)

Content format: content_html

Ongoing Content Integrity

Deduplication Policy

The TESBM Q&A bank is checked against 12 months of published questions before each issue. The dedup policy:

0–6 months: Same core governance issue → skip. Even if the framing is slightly different, the board member who read the prior answer will not benefit from this one.

6–12 months: Same core governance issue → skip unless there is a meaningfully new angle (new legislation, new ESB guidance, a governance crisis type that was not the focus of the earlier answer).

12+ months: Eligible for fresh treatment. Governance principles are enduring but board member cohorts turn over; a board member who wasn't reading the newsletter 12 months ago needs access to foundational ESB coaching.

Dedup is done semantically (LLM-assessed similarity), not by keyword matching. Two questions that ask the same thing in different words should be caught. Two questions that use the same words but address different governance principles should not be flagged.

Geographic Rotation

Board meeting analysis must rotate across all three regions. Monitor the geographic log to ensure:

No region appears more than twice in five consecutive issues

No single state appears in back-to-back issues

No single district appears within 90 days

If a region's Granicus/Swagit listings are exhausted or unavailable, use the known-listings fallback. If the fallback fails, flag for human selection of a meeting.

Issue Quality Tracking

Track per-issue:

Number of Q&A candidates generated

Number passing all 4 gates

Number of gate failures by gate number

Models used for each Q&A (which attempt succeeded)

Whether the board meeting video was verified or fell back to known listing

Whether Perplexity was available (vs. DeepSeek fallback used)

Gate 2 (ESB fidelity) failures accumulate signal about prompt weaknesses. High Gate 2 failure rates on a particular governance topic type indicate the writing prompts need calibration.

Prompt Maintenance

When gate failures cluster around a particular topic type or framing, the generation prompts should be updated to address the pattern. For example: if Gate 2 repeatedly fails on superintendent evaluation questions because answers keep validating relationship-based criteria, the Step 6 writing prompt needs to more explicitly front-load the ESB evaluation framework definition before the Q&A generation.

Prompt updates should be documented with the date, the failure pattern they address, and the change made.

Content Update Policy

TESBM is a current-events-grounded newsletter, not an evergreen library. Content does not require update once published — each issue is of its moment. The Q&A dedup policy handles freshness across issues.

However: if ESB framework positions change (new ESB source documents, revised guidance), the Step 6 writing prompts must be updated before the next generation run, and the quality gates must be recalibrated to reflect the updated framework.

Independent Review Protocol

Approval Flow: AJ must approve before beehiiv send.

The pipeline does not post to beehiiv automatically. The assembled draft is saved to the esby-portal approval queue with status pending. Approval in the portal uploads the draft to beehiiv as a draft post — not a sent newsletter. AJ must then log in to beehiiv to make final edits (cutting Q&As to 3, cutting reads to 4, reviewing the full issue) and schedule or manually trigger the send.

No issue is published without AJ's explicit action in beehiiv.

Learned Rules

(No site-specific learned rules recorded yet. Rules are appended here as AJ edits diverge from submitted drafts.)

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"

End of guide. This document is authoritative for TESBM newsletter content generation and review. When in doubt, do not publish — flag for human review.