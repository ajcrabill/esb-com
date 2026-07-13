title: "Content Generation Guide — CO (creatingoutcomes.org)" type: content-guide site: creatingoutcomes.org updated: 2026-07-08

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Core Parameters

Purpose

creatingoutcomes.com answers specific, practical governance questions for leaders of ALL types of governing bodies. The site is not school-board-specific. It is not nonprofit-only. It is for anyone who sits on a governing board — hospital systems, community foundations, professional associations, nonprofits, libraries, housing authorities, public agencies, and any other entity governed by a board.

The site's core premise: all governing bodies, regardless of sector, face the same fundamental governance challenge. They must stay connected to mission while delegating management. Every Q&A on CO answers a governance question through that lens.

Cross-Sector Applicability — The Prime Directive

Before any article is drafted, it must pass the three-board test:

Would a hospital board trustee, a community foundation board member, AND a nonprofit association board member all find this answer directly useful and applicable to their situation?

If the answer to all three is yes, the article belongs on CO. If the answer only works for one type of board, the article needs revision — not rejection, revision.

This is the single most important constraint on CO content. Every decision about framing, language, examples, and practical steps flows from this requirement.

Target Audience

Primary: Board members and trustees of any governing body — nonprofit board members, foundation trustees, association board officers, hospital board members, housing authority trustees, library board members, public agency board members, and any other person who sits on a governing board and has a specific governance question.

Default framing: The site leans nonprofit/philanthropic in its examples and framing. When in doubt, reach for a nonprofit or foundation example rather than a hospital or public agency example. But always confirm the answer also applies to those other contexts, and acknowledge that applicability in the text.

Reader posture: The reader has arrived with a specific question. They are not browsing abstractly. They want an answer they can act on today. They are experienced enough to find condescension insulting and inexperienced enough to need plain language, not academic governance theory.

Voice

Tone: Advisory, direct, collegial. Never condescending.

Person: 2nd person throughout. "Your board," "you'll want to," "when your board faces this," "consider whether your organization…"

Register: Plain-language practitioner advice. Not academic. Not hedged into uselessness. Not cheerleader-positive.

Byline: None.

Examples: Default to nonprofit/foundation framing. Acknowledge applicability across board types. Never frame an example as if only one type of board would face this situation.

Prohibited register: Academic (citing studies by name, using "research suggests" as a crutch), lawyerly (hedge every sentence), cheerleader ("every board can do this!").

Distinction from Sister Sites

CO is one of a family of governance sites. The lines between them must be maintained precisely.

CO vs. SBA — the critical distinction:

SBA is exclusively school-board-specific. CO covers all governing body types. A CO article on goal-setting applies to a hospital board trustee, a nonprofit ED's board, a foundation, and a school board member. An SBA article on goal-setting would be specifically about school boards setting student outcome goals.

Test for CO vs. SBA: If the question or answer uses "superintendent" — it may belong on SBA, not CO (unless you're discussing the superintendent role as one example of a CEO-equivalent among many). If the answer requires knowledge of specific state education law, state board structures, or K-12 metrics — it belongs on SBA, not CO.

CO vs. EGB — the critical distinction:

EGB uses formal citation formats, academic register, and is written for researchers and policymakers who want documented evidence. CO is plain-language advisory Q&A for practitioners who want actionable answers now. If you find yourself adding an APA citation, you're in EGB territory, not CO.

CO vs. EB — the critical distinction:

EB publishes analytical posts without Q&A format. CO always uses the Q&A format — a question that a reader would actually type into a search engine, followed by a direct answer. If there's no question header, it's not CO content.

Content Goals

What a Successful CO Article Looks Like

A successful CO article:

Has a question header that a real board member would actually search or ask.

Answers the question directly in the first paragraph — no throat-clearing, no "this is a great question," no four paragraphs of setup before the answer appears.

Elaborates on the answer with enough depth that the reader understands the reasoning, not just the conclusion.

Provides practical steps that a board can implement without hiring a consultant.

Works equally well for a hospital board trustee, a foundation board member, and a community nonprofit board member.

Anchors the answer to mission/purpose — what does a board focused on its "why" do in this situation?

Uses governing-body-neutral language throughout.

What a Failed CO Article Looks Like

A failed CO article:

Only works for school board members — too specific to K-12 context, uses "superintendent" without context, assumes state education law.

Only works for nonprofits — assumes 501(c)(3) structure, uses nonprofit-specific jargon without acknowledging other contexts.

Answers the question so abstractly that no one can act on it — "boards must align resources with mission" is not an answer; it's a platitude.

Buries the answer. If a reader has to read three paragraphs before finding out what to actually do, the article has failed the format.

Uses school-board-specific terminology ("district," "superintendent," "students" as the default constituency) without flagging these as one type of board context.

Reads like an academic paper — citations, passive voice, hedged conclusions.

Addresses management, not governance — the question is about something the CEO/executive director should decide, not the board.

Content Format and Structure

Article Format

Every CO article follows this structure, in this order:

1. Question Header (H1) The question as a reader would ask it. Plain language. Specific. Applicable across board types.

Examples of well-formed question headers:

"How should our board evaluate the executive director?"

"What's the difference between governing and managing?"

"How do we set goals that actually hold us accountable?"

"When should a board member recuse themselves?"

"What does a healthy board-CEO relationship look like?"

Examples of poorly-formed question headers (do not use):

"Effective Goal-Setting for Nonprofit Boards" — not a question; too sector-specific

"Superintendent Evaluation Best Practices" — school-board-specific; wrong site

"The Role of Governance in Modern Organizations" — too abstract; not a real question

2. Direct Answer (Paragraph 1) The first paragraph answers the question. Not sets it up. Not introduces context. Answers it. A reader who reads only the first paragraph should know what to do.

3. Elaboration (2–4 paragraphs) Explain the reasoning behind the answer. Address common variations or complications. Use examples drawn from multiple governing body types — "a community foundation board might handle this by…; a regional health system board often approaches it differently…; in both cases, the governing principle is the same." Make the cross-sector applicability visible, not just implied.

4. Practical Steps (final section) Concrete actions the board can take. Not "consider aligning your resources" but "at your next meeting, bring the budget side-by-side with your stated organizational priorities and ask whether the numbers reflect the mission." Steps should be actionable within a single board meeting or planning cycle.

Language Conventions

These substitutions are mandatory. Do not use the left-column term when the right-column term is available:

When school boards are mentioned as one example among several: This is permitted and often valuable. "Whether you're on a hospital board, a library board, or a school board, the dynamic is the same…" is fine. The prohibition is on defaulting to school board context as if it's the only board type.

Governing-body-neutral phrasing patterns:

"Your organization" not "your district"

"Your chief executive" or "your executive director" not "your superintendent"

"Those your organization serves" not "your students"

"Your board's accountability framework" not "your evaluation rubric"

"Regulatory and legal requirements" not "state board requirements"

"In a hospital system, a foundation, or a community association" as example openers — rotate through board types

Front Matter Fields

Every CO article requires the following Jekyll front matter:

---

layout: qa

title: "[The question, as it appears in the H1]"

description: "[One-sentence summary of the answer, 150 characters max]"

permalink: /qa/[topic-phrase]/

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

Permalink / file naming rules:

Use hyphens, not underscores

Lowercase only

3–6 words

Describes the topic, not the question form (e.g., ceo-evaluation-process not how-to-evaluate-your-ceo)

No dates in the filename (evergreen)

Forbidden Patterns

These patterns must be caught and corrected before publication:

Throat-clearing opener: "This is a question many boards face…" / "Governance is complex…" / "There's no one-size-fits-all answer, but…" — Delete. Start with the answer.

Buried lede: The actual answer appears in paragraph 3 or later. Restructure so paragraph 1 contains the answer.

School-board default: Any sentence that only makes sense if the reader is a school board member. Revise to cross-sector.

Platitude without action: "Boards must remain focused on mission" — this is not an answer. Add what that means in practice.

Condescension: "Even the most experienced boards sometimes struggle with…" / "It's important to remember that…" — rewrite as peer-to-peer advisory.

Fabricated specificity: "Studies show that 73% of boards…" — never invent statistics. Remove the statistic or ground it in observable governance patterns without a number.

Management territory: The answer tells the board what operational decisions to make. Redirect to the governing question: "Your board's role here is to…" not "Your organization should…"

In-Bounds Content

Approved Topic Areas

All topics must be applicable across at least three distinct governing body types. The following topic areas are in bounds:

Governing vs. Managing The boundary between board oversight and executive management. What decisions belong to the board, what belongs to the CEO/executive director, and how to maintain that clarity over time. How to respond when the line gets blurry. Applicable to every governing body type — this is perhaps the most universal governance challenge.

CEO/Executive Director Evaluation How boards evaluate their chief executive. What a fair, rigorous, and mission-aligned evaluation process looks like. How to set expectations at the start of the year. How to separate performance from relationship. Applicable across all board types (hospital boards evaluate their CEO; foundation boards evaluate their executive director; nonprofit boards evaluate their ED).

Goal-Setting and Mission Focus How boards set meaningful goals. How to distinguish outcome-level goals (board) from operational goals (management). How to ensure goals connect to the organization's mission and purpose — its "why." How to track progress without micromanaging. Applicable across board types.

Budget Governance and Resource Alignment How boards fulfill their financial oversight role. How to read and engage a budget as a governance document — does it reflect the mission? How to ask the right questions without getting into management-level financial detail. Applicable across all board types.

Board-CEO Relationship and Role Clarity What a healthy partnership between the board and its chief executive looks like. How to build trust, set clear expectations, and maintain open communication without blurring governance and management roles. Applicable across board types.

Monitoring and Accountability How boards monitor organizational performance. What accountability means at the governance level. How to respond when goals aren't being met. How to distinguish between accountability and micromanagement. Applicable across board types.

Board Composition, Term Limits, Diversity How boards think about their own membership. Term limits and their tradeoffs. How to pursue diversity in board composition. How to recruit and onboard new members. Applicable across board types.

Conflict of Interest What constitutes a conflict of interest. How to establish and enforce a conflict-of-interest policy. When board members should recuse themselves. How to handle conflicts that arise unexpectedly. Applicable across all board types.

Succession Planning How boards plan for leadership transitions — both board leadership (chair, officers) and executive leadership (CEO/ED succession). Applicable across board types.

Meeting Conduct and Effectiveness How to run a board meeting that produces decisions, not just discussion. Consent agendas, executive sessions, committee structures. How to get board members engaged rather than passive. Applicable across board types.

Public Accountability and Transparency How governing boards of public and quasi-public entities maintain accountability to the communities they serve. What transparency looks like in practice. Applicable particularly (but not exclusively) to public agency boards, hospital boards, and publicly funded nonprofits.

Board Self-Evaluation How boards assess their own performance. Why self-evaluation matters. What a rigorous but practical self-evaluation process looks like. Applicable across board types.

Stakeholder Engagement How boards engage with the communities and stakeholders they serve — without crossing into management territory. The distinction between the board's engagement role and the staff's engagement role. Applicable across board types.

How to Frame Questions in Governing-Body-Neutral Language

The question header should use language that any board member could recognize as their question. Test the question by reading it from the perspective of:

A hospital board trustee

A community foundation board member

A housing authority board member

A professional association board officer

If any of these readers would say "that's not my question — that's a school board question," the framing needs revision.

Neutral framing patterns:

"How should our board…" (not "how should our school board…")

"What does the board's role look like when…" (not "what does the school board's role…")

"When the executive director…" (not "when the superintendent…")

"Our organization's mission…" (not "our district's mission…")

Multi-Board Examples Within a Single Answer

The most effective CO articles demonstrate cross-sector applicability explicitly within the body of the answer. Techniques:

Parallel examples: "A community foundation board might handle this by establishing a written policy at the beginning of each term. A hospital board often builds this into its governance committee charter. In either case, the governing principle is the same…"

Sector pivot: "Regardless of whether your board serves a nonprofit, a public institution, or a private entity, this dynamic plays out the same way."

Explicit acknowledgment: "This applies whether you're on a library board, a housing authority, or a national professional association — any time a governing board has a chief executive, this question comes up."

Why-Based Governance Alignment

Every CO article should anchor its answer to purpose/mission — the organization's "why."

What this means in practice:

When answering a goal-setting question, the answer should connect to how goals express mission — boards that are anchored to their why set goals at the outcome level, not the activity level.

When answering a budget governance question, the answer should surface the mission-alignment test — does the budget reflect what the organization says it exists to do?

When answering an evaluation question, the answer should connect to how effective execution of the mission is the core standard against which the CEO is measured.

What this does NOT mean:

Do not use the phrase "why-based governance" — that is proprietary terminology. Do not name the framework.

Do not name AJ Crabill, ESB, GOTB, or any associated brand.

The alignment is conceptual, not terminological. The article should embody the principle without naming it.

The CO premise in plain language (for AI generation reference, not for publication): All governing boards should be anchored to a clear mission — a reason they exist. The board's job is to ensure the organization makes meaningful progress toward that mission and to delegate everything else to the chief executive. Every governance question is ultimately a question about how the board stays connected to mission while staying out of management.

Out-of-Bounds Content

Hard Exclusions

The following topics and content types are never appropriate for CO:

School-board-specific content that doesn't generalize:

State education law requirements (these are school-board-specific)

Student outcome metrics and accountability systems (K-12-specific)

The superintendent-board dynamic framed as if it's unique to schools (it's not — frame it as a board-CEO dynamic)

State board of education oversight structures

Specific K-12 accountability frameworks (ESSA, IDEA, etc.)

Instructional leadership topics

Curriculum governance

Sector-exclusive content:

Content that only applies to 501(c)(3) organizations without acknowledging other board types

Hospital-specific regulatory content (Joint Commission, CMS) framed as universal governance

Content that only makes sense for public-sector boards

Format violations:

Research reviews (that is EGB/SBRS territory)

Formal policy briefs with numbered citations (that is EGB territory)

Analytical posts without a Q&A format (that is EB territory)

Listicles without a governing question

Management topics:

How to hire staff

Operational program design

HR policies and procedures

Financial management (distinct from financial oversight/governance)

Technology implementation decisions

Vendor selection

Day-to-day organizational operations

Any content tied to current events or dates:

"In the current environment…"

"Given recent events…"

"This year's [anything]…"

References to specific laws or regulations that may change

Overlap Rules: How to Distinguish CO from SBA and EGB

CO vs. SBA overlap test:

Ask: Is this question school-board-specific, or is it a governance question that school boards share with all other governing boards?

"How should our board evaluate the superintendent?" → SBA (school-board-specific) unless reframed as "How should our board evaluate the CEO/executive director?" → CO

"How should school boards approach goal-setting for student outcomes?" → SBA

"How should our board set goals that connect to mission?" → CO

"What does state law require of school board members?" → SBA

"What fiduciary duties do board members generally have?" → CO

Rule: If the answer would be materially different for a hospital board than for a school board, it belongs on SBA (or needs to be reframed to address that difference).

CO vs. EGB overlap test:

Ask: Is this a practitioner advisory answer, or a research-grounded policy brief?

Advisory answer in plain language: CO

Formal analysis with citations and literature review: EGB

If you're tempted to add "as Smith and Jones (2019) found…" — you're in EGB territory. Remove the citation and write it as observed governance practice, or move the topic to EGB.

Citation Requirements

Policy

Citations are not required on CO. No formal citation format (APA, MLA, Chicago) should appear in CO articles.

If Referencing Research

If an article references a study, report, or body of research, do so informally:

Acceptable:

"Research on board effectiveness consistently shows that…"

"Governance practitioners generally find that…"

"Most studies of board self-evaluation suggest…"

Not acceptable:

"Smith, J., & Jones, R. (2019). Board effectiveness in nonprofit organizations. Journal of Governance, 14(2), 45–67."

"According to a 2022 BoardSource survey, 68% of boards…" (unless this statistic is verified and the publication year will remain accurate indefinitely — generally avoid dated statistics)

No Fabrication

Never invent statistics, studies, findings, or named organizations to support a claim. If you cannot ground a claim in observable governance patterns without a specific citation, do one of the following:

Reframe the claim as observable practice: "Boards that go through this process typically find that…"

Remove the claim and rely on the reasoning

Flag the claim for human review before publication

Grounding Claims

All factual claims about governance should be grounded in patterns that are true across many real governing bodies. The question to ask: "Is this something I could observe in practice across multiple sectors?" If yes, it can be stated as a governance pattern. If no, remove it.

Ongoing Content Integrity

Evergreen Standard

CO articles must remain useful and accurate across years, not months. Apply the following rules to maintain evergreen status:

No date references:

Never reference "this year," "recently," "currently," "in 2026," or similar temporal markers.

Never reference specific legislative sessions, elections, or current events.

Write as if the article will be read today and three years from now.

No current-events ties:

If a governance topic is prompted by a current event (a high-profile board scandal, a legislative change), write about the underlying governance principle — not the event. The principle will outlast the event.

Durable claim language: Instead of "many boards are moving toward…" (implies a trend in progress), write "boards that adopt this approach find…" (describes an observable pattern without tying it to a moment in time).

Terminology Glossary (Governing-Body-Neutral)

Maintain consistency in governing-body-neutral terminology across all CO articles:

Cross-Site Linking Rules

CO may link to sister sites under the following conditions:

Frequency: No more than 1–2 cross-site links per year per site.

Context: Links must appear in a list of 3 or more links — never as a standalone endorsement.

Subtlety: No "check out our sister site" language. Links should appear naturally as additional resources within a broader list.

Permitted links: effectiveschoolboards.com, whybasedboards.com, effectivegoverningboards.com. Do not link to these more than 1–2 times per year total.

Prohibited: Any link that names AJ Crabill, ESB, GOTB, or that positions any proprietary framework as the source of CO's approach.

Duplicate Check

Before finalizing a topic, confirm no existing CO article already answers the same question.

A duplicate is not just an identical question — it is a question whose answer would be substantially the same as an existing article's answer. If an existing article already covers the substance, either:

Select a more specific sub-question that fills a real gap

Select a different topic entirely

Content Audit Cadence

Conduct a content audit of all published CO articles every six months:

Are any articles using deprecated terminology (pre-glossary language)?

Are any articles making date-specific claims that now feel stale?

Are any articles that were published early (before these standards were established) failing the three-board test?

Flag articles for revision as needed. Do not delete — revise in place.

Grounding Document

Source: Why-Based Governing Boards: How Boards Fail, How Yours Can Become Effective by AJ Crabill Access: Google Drive ID: 1VZ76e4NNc6Spd6M6jAZ3gQvO3SVxOvZTri7QfkrRXhg (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: a — pre-draft only

Pre-draft only: Before drafting, read the relevant sections of the grounding document. Use it to calibrate the frame, vocabulary, and core claims before writing begins. It is a framing calibrator, not a citation source.

Voice Register

Register: ajc-long

Sentence and paragraph targets:

Average sentence length: ~23 words

Paragraph length: 4–8 sentences

Author blend:

Gladwell 35%: concrete scene-setting, narrative hooks, counterintuitive reframes

Collins 30%: rigorous structure, evidence-backed assertions, deliberate cadence

Sinek 20%: purpose-first framing, "why" as organizing principle

Gawande 15%: practitioner-voice specificity, observational precision

Voice conventions:

Tone: Advisory, direct, collegial. Never condescending.

Person: 2nd person throughout. "Your board," "you'll want to," "when your board faces this," "consider whether your organization…"

Register: Plain-language practitioner advice. Not academic. Not hedged into uselessness. Not cheerleader-positive.

Byline: None.

Examples: Default to nonprofit/foundation framing. Acknowledge applicability across board types. Never frame an example as if only one type of board would face this situation.

Prohibited register: Academic (citing studies by name, using "research suggests" as a crutch), lawyerly (hedge every sentence), cheerleader ("every board can do this!").

NEVER Rules

Never use "why-based governance" or name the framework — alignment is conceptual, not terminological.

Never name AJ Crabill, ESB, GOTB, or any associated brand in CO content.

Never default to school-board framing — every sentence must be applicable across governing body types.

Never use "superintendent" as a generic term for a chief executive without explicitly noting it as one example.

Never use "school district" or "district" as a generic term for an organization.

Never use "students" as the default constituency — use "those the organization serves," "clients," "beneficiaries," or "constituents."

Never bury the answer — paragraph 1 answers the question.

Never invent statistics, studies, or named organizations.

Never use formal citation formats (APA, MLA, Chicago) — this is CO, not EGB.

Never include date references or tie content to current events.

Never address management-level decisions — redirect to the governance question.

Never include a publication date in the visible post content or meta div — the <div class="meta"> date field must be omitted (left empty or removed entirely) from the generated HTML; these are evergreen reference articles and dates make them feel stale.

Never produce a full standalone HTML document — output front matter + body only, no <!DOCTYPE html>, <html>, <head>, <body> tags.

Never link to sister sites more than 1–2 times per year per site; never as standalone endorsements.

Never use "board of education" as a generic term.

Never use "curriculum," "instructional staff," or K-12-specific accountability framework names (ESSA, IDEA, Title I, etc.) in general governance discussion.

Generation Process

Step 1 — Gap Analysis on Existing Q&A Topics

Pull the list of all published CO Q&A articles. Map to topic areas. Identify gaps. Select the topic area to address in the new article. Select a specific question within that topic area.

Secondary prioritization factors:

Topics that are likely to generate search traffic from board members across multiple sectors

Topics where the answer is genuinely helpful and not obvious

Topics where governing-body-neutral framing is achievable

Output: Selected topic area and candidate question.

Step 2 — Question Framing (Governing-Body-Neutral Language)

Draft the question header. Apply the language conventions from the Site Context section. Apply the three-board test.

If the question fails the three-board test, revise until it passes or select a different question.

Hospital board trustee would ask this question

Foundation board member would ask this question

Nonprofit association board member would ask this question

If any box is unchecked, revise the question framing before proceeding to draft.

Output: Approved question header.

Step 3 — Cross-Sector Applicability Check

Confirm the question applies to hospital boards, foundation boards, AND nonprofit association boards. If the answer would be materially different for any of these, the question is either (a) too specific and needs to be broadened, or (b) belongs on SBA, not CO.

Output: Confirmed applicability, or revised question.

Step 4 — Pre-Draft Grounding Document Read

Read the relevant sections of Why-Based Governing Boards: How Boards Fail, How Yours Can Become Effective (Google Drive ID: 1VZ76e4NNc6Spd6M6jAZ3gQvO3SVxOvZTri7QfkrRXhg, via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content). Use it to calibrate the frame, vocabulary, and core claims before writing begins. Do not cite it in the article — use it as a framing calibrator only.

Output: Calibration notes (internal; not included in the draft).

Step 5 — Structural Brief

Generate a structural brief before drafting:

Question: [exact question header as it will appear in H1]

Direct answer: [one-paragraph answer that paragraph 1 will contain]

Elaboration points: [3–5 bullet points covering the most important nuance, variations, or common mistakes]

Practical steps: [3–5 specific, actionable steps a board can take]

Cross-sector examples: [which board types will be used as examples; confirm at least two distinct board types are represented]

Why-based alignment: [how does this answer connect to mission/purpose?]

Confirm:

The direct answer is concise enough to fit in one paragraph

The elaboration points address genuine complexity, not filler

The practical steps are specific enough to implement without a consultant

At least two distinct board types are represented in planned examples

The why-based alignment is clear

Output: Approved structural brief.

Step 6 — Draft Generation

Primary model: the configured write model Fallback model: Claude Opus 4.8

Generate the full draft using the structural brief. Apply all language conventions. Target 600–900 words.

Front matter must be included in the output.

Output: First draft with front matter.

Step 7 — Why-Based Alignment Check

Read the draft and confirm:

The answer anchors to mission/purpose at least once — explicitly connecting governance practice to what the board exists to do

The practical steps support a mission-focused board, not just a procedurally compliant one

The article does not treat governance as an end in itself (compliance, process) but as a means to organizational purpose

If alignment is weak, revise to strengthen the mission connection. Do not add proprietary terminology.

Output: Alignment confirmed, or revision notes.

Step 8 — Quality Checks

Run all quality checks in order per Section 8 below. The draft must pass each check before proceeding to the next.

Step 9 — Technical Filing

Confirm front matter is complete and accurate

Confirm permalink matches file naming convention

Confirm layout is qa

Confirm word count is 600–900 words

File at qa/[topic-phrase].html

Trigger Jekyll build check

Auto-publish

Output: Published article URL.

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

Ultimate Failure Reporting — CO: Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (CO), article title, which check failed, attempt count, nature of each failure, and the draft. Mark status as FAILED. Do not publish.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any unicode em-dash ( — ) or en-dash ( – ); the required form is a spaced double-hyphen ("--"), used sparingly (more than 1 "--" in a single paragraph is a flag)

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (CO (creatingoutcomes.org)):

The following patterns are CO-specific slop — they break the site's cross-sector premise and must be caught and eliminated regardless of the universal tiers above:

School-board defaults: Every instance of "superintendent," "school district," "district," or "students" as the default constituency. These are content errors, not style preferences — they break the cross-sector premise of the site.

Single-sector framing: Any paragraph that only makes sense for nonprofit boards, or only for hospital boards. Either make it applicable across sectors or explicitly name the sector and acknowledge the parallel in other contexts.

Abstract governance language without practical application: Any sentence that describes what good governance looks like without explaining what a board should actually do. CO's audience is practitioners who need to do something — add the practical step.

Throat-clearing openers: "This is a question many boards struggle with." / "Governance can be complex, especially when…" / "There's no one-size-fits-all answer, but…" / "Understanding this issue requires some background." Delete. Start with the answer.

Buried lede: If the answer to the question appears after the second sentence of paragraph 1, restructure. Paragraph 1 = the answer. Paragraph 2+ = elaboration.

Platitudes without action: "Boards must align resources with mission." → Add: "In practice, this means comparing your budget line-by-line with your strategic priorities and asking: does this number reflect what we say matters most?" If a sentence states a governance truism without explaining what it means in practice, add the practical meaning or delete the sentence.

Hedging that undercuts advice: "Some boards may find it useful to perhaps consider exploring whether…" is not advice. "Consider asking your board chair to…" is advice.

Fabricated specificity: Any statistic, study finding, or named organization that cannot be verified. Replace with observable governance pattern language.

Filler elaboration: Any paragraph that restates something already said without adding new information or nuance. Cut it.

Passive voice where active is available: "It is important that boards consider…" → "Your board should consider…" / "Evaluation processes are often overlooked…" → "Many boards overlook the evaluation process…"

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

8c. ESB Governance Language Check

ESB Governance Language Check

Reference: Google Drive ID 13O3_qNxtRVHsTDyDMXdotPLOhIMTyRe0J_1yQ9tzhOQ

Banned phrases — any occurrence fails:

"micromanage" / "micromanaging" → describe the specific behavior (is the board operating within its governance role or directing implementation?)

"rubberstamping" / "rubber stamp" → describe whether the board exercised informed judgment

"stay in your lane" → reference governing policies or the board vs. chief-executive role distinction

"good/bad/right/wrong" as personal moral judgment → frame around effectiveness and outcomes

Banned framings — restructure any instance found:

Board as passive recipient: any suggestion that the board should simply receive, defer, or accept without agency

Board as obstacle: any framing that board involvement is a problem to manage around

Expertise as authority: any framing that professional staff have more legitimate authority than elected board members

Conflict as dysfunction: any framing that disagreement among board members is inherently bad

Efficiency as primary goal: any framing that speed or non-disruption is the board's primary objective

Sector-specific terms — replace with cross-sector language:

"school district" or "district" → "the organization"

"equity" → describe the specific gap or outcome with data (reserve the term only for direct statutory quotation)

"achievement gap" → describe the system failure directly with specific data

Politically-coded terms → describe the specific concept: DEI, anti-racist, woke, "parents' rights" (as contested framing), SEL (as wedge term)

8d. Site-Specific Checks

CO Language Review — Governing-Body-Neutral Terminology Scan

Scan every sentence for the following and replace before proceeding:

"superintendent" → replace with "CEO," "executive director," or "chief executive"

"school district" / "district" → replace with "organization"

"students" as default constituency → replace with "clients," "beneficiaries," "constituents," or "those the organization serves"

"board of education" → replace with "board" or "governing board"

Any other school-board-specific terminology not caught in earlier steps

Also check:

All examples reference at least two distinct governing body types

No example assumes a nonprofit-only context without acknowledgment

No example assumes a school-board-only context

CO Cross-Sector Red-Team (mandatory before red-team phases)

Read the entire draft from the perspective of a hospital board trustee who has never worked in education or nonprofits.

Does it answer their question?

Is there any language that is confusing or inapplicable to their context?

If the article uses examples, do any examples feel foreign to their experience?

If this reader would feel the article "isn't really for me," the article needs revision before proceeding.

Repeat the exercise from the perspective of a housing authority trustee.

CO-Specific Overlap Tests

SBA overlap test: Read the article and ask — could this run on schoolboardanswers.com without any changes? If yes, it is too school-board-specific. It either needs to be generalized to pass the CO cross-sector test, or it should be moved to SBA.

EGB overlap test: Read the article and ask — does this read like a formal policy brief? Are there citations? Is the register academic rather than advisory? If yes, revise to advisory register. Remove citations or convert them to informal references.

Management creep test: Read the article and ask — is any part of this article telling the board how to do management-level work? If yes, revise to redirect to the governance question. The board's role is to set direction, establish accountability, and monitor outcomes — not to decide how those outcomes are achieved.

CO Technical Filing Checks

Before proceeding to publication, confirm all of the following:

Front matter:

layout: qa is present

title: matches the H1 question header exactly

description: is present, under 150 characters, and summarizes the answer (not the question)

permalink: follows /qa/[topic-phrase]/ format

No date field in front matter (evergreen content)

Language conventions:

No instances of "superintendent" without appropriate context

No instances of "school district" or "district" as a generic term

No instances of "students" as the default constituency

No instances of "board of education" as a generic term

All examples reference at least two distinct governing body types

No fabricated statistics or named studies

Format:

Question formatted as H1

First paragraph contains the answer (not setup or context)

Article has elaboration section (at least 2 paragraphs)

Article has practical steps section

Word count is 600–900 words

Filing:

File is saved at qa/[topic-phrase].html

Filename uses hyphens, not underscores

Filename is lowercase

Filename does not contain a date

Jekyll build runs without errors

No broken links in the article

Quality gates:

Anti-slop cleanup complete (8a)

Voice check complete (8b)

ESB governance language check complete (8c)

CO language review complete (8d)

Cross-sector applicability confirmed (three-board test passed)

Why-based alignment confirmed (mission/purpose anchoring present)

No names of any kind (individuals, organizations, districts, institutions)

No references to current events or specific dates

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

Technical Filing

File Location and Naming

File at: qa/[topic-phrase].html

Use hyphens, not underscores

Lowercase only

3–6 words in the topic phrase

Describes the topic, not the question form (e.g., ceo-evaluation-process not how-to-evaluate-your-ceo)

No dates in the filename (evergreen)

Required Front Matter

---

layout: qa

title: "[The question, as it appears in the H1]"

description: "[One-sentence summary of the answer, 150 characters max]"

permalink: /qa/[topic-phrase]/

---

No date field. No other custom fields required. The <div class="meta"> date field in the post header must also be omitted or left empty — do not display a publication date visually anywhere in the rendered page.

Output Format

The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout.

Jekyll Build

After filing, trigger Jekyll build check. Confirm no build errors before auto-publish.

Publishing Pipeline

Approval workflow: Auto-publish after all quality gates pass. No manual review step is required if all gates pass.

Independent Review Protocol

Approval flow: Auto-publish after all quality gates pass.

If a quality gate cannot be resolved by the automated process (e.g., the anti-slop scan identifies a structural problem that requires content judgment, or the red-team raises a claim that cannot be supported without external verification), flag for human review before publishing. Do not auto-publish articles with unresolved quality gate failures.

If the configured write model is unavailable for the primary red-team (8e), wait up to 72 hours for availability, then fall back to Claude Opus 4.8 for that step only. Document the fallback in the article's generation log.

Learned Rules

Appendix: Reference Articles

The following published articles illustrate CO's format, voice, and cross-sector approach. Use these as calibration references when assessing whether a new article meets the standard.

https://creatingoutcomes.com/qa/governing-vs-managing.html

https://creatingoutcomes.com/qa/ceo-evaluation-process.html

https://creatingoutcomes.com/qa/measurable-goals.html

https://creatingoutcomes.com/qa/types-of-boards.html

https://creatingoutcomes.com/qa/board-role-in-budget.html

https://creatingoutcomes.com/qa/transparency-about-failure.html

When assessing a new draft, ask: would this article sit comfortably alongside these examples in terms of format, tone, scope, and cross-sector applicability?

Appendix: Quick Reference — The Three-Board Test

Before any article is published, confirm it passes all three checks:

Board 1: Hospital board trustee Would this person, who has never worked in education, find this article directly useful and applicable to their situation on a hospital governing board?

Board 2: Community foundation board member Would this person, who governs a grantmaking foundation, find this article directly useful and applicable to their situation?

Board 3: Nonprofit association board officer Would this person, who serves on the board of a regional professional association or membership nonprofit, find this article directly useful and applicable to their situation?

If all three pass: the article belongs on CO. If any one fails: revise the framing, language, or examples until all three pass — or select a different topic.

Appendix: Quick Reference — Forbidden Terms

The following terms are forbidden as generic governance language in CO articles. They may appear only when explicitly discussed as one type of board context among several.

Superintendent

School district / district (as a generic term)

Board of education (as a generic term)

Students (as the default constituency)

State board (when referring to state education agency oversight)

Curriculum

Instructional staff

Principal (when used as an analogy without context)

Academic outcomes

Test scores / assessment results

ESSA / IDEA / Title I / Title II (or any federal education law reference)

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"

End of Content Generation Guide — CO (creatingoutcomes.org) This document is the authoritative reference for AI-assisted content generation. No inference or interpretation should substitute for the explicit rules contained here.