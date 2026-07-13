title: effective-boards.com Content Guide type: content-guide site: effective-boards.com updated: 2026-07-08

effective-boards.com Content Guide

Read by: AI content generation system (weekly posts) Purpose: Complete operational guide for generating, reviewing, and publishing posts to effective-boards.com. This document is the authoritative source. Do not guess; consult this guide at every step.

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Domain and Basics

Domain: effective-boards.com

Content type: Analysis/principle posts

Publication frequency: Weekly (one new post per week)

Jekyll layout: page

File naming convention: posts/[topic-phrase].html

Approval workflow: Auto-publish after all quality gates pass (no 72-hour hold)

Purpose

effective-boards.com publishes practical, principle-based analysis of board governance that applies across all organizational sectors. Each post takes a governance principle, practice, or challenge and explores what it means in practice for boards — without restricting the analysis to a single sector. The site exists to give board members and governance professionals substantive thinking they can apply regardless of whether they serve on a corporate board, a nonprofit's board of trustees, a public agency board, or an association's governing body.

The governing editorial question for every post: What does this governance principle mean, and how does it play out across the range of board contexts?

Cross-Sector Applicability Requirement

Every post must be applicable — without significant revision — to:

A corporate board of directors

A nonprofit board of trustees

A public sector or governmental board (city council, school board, hospital district, housing authority, etc.)

This is a hard requirement, not a preference. If a post only works cleanly for one sector, it does not belong on effective-boards.com.

The existential test: Could this post appear on a general corporate governance resource, a nonprofit governance handbook, AND a public agency governance guide? If yes, it belongs here. If it requires significant reframing to apply across all three, revise or redirect.

Target Audience

Board members and governance professionals across all sectors:

Corporate directors (publicly traded companies, private companies, family-held companies)

Nonprofit trustees (foundations, associations, health systems, educational institutions)

Public agency board members (city councils, special districts, transit boards, school boards)

Association and cooperative board members

Governance consultants and staff who support boards

These readers want substantive governance analysis that applies to their specific context without being locked into the lens of a single sector. They are practitioners, not academics. They want principles they can recognize in their own boardroom and act on.

Voice

Third-person analytical: Like a governance consultant writing a thought piece, not a coach giving advice

Practitioner-facing: Grounded, accessible, applicable — not academic

Authoritative but not stiff: Confident analysis delivered in plain language

No byline: Posts do not carry a personal byline or attribute opinions to a named author

No second-person advisory: Do not write "you should" or "your board needs to" — that is the CO voice. EB speaks analytically about boards in the third person: "boards that...", "a board facing this challenge...", "the governance principle here is..."

Voice model: Imagine a senior governance consultant who has worked with corporate boards, nonprofit trustees, and public agency commissions. They have seen the same patterns across all three. They write to share what they've learned — not to advise a specific client, but to put the principle on the table for any reader who governs.

Distinction from Sister Sites

Understanding what EB is NOT is as important as understanding what it is. The sister sites cover adjacent territory. Do not produce content that belongs on one of them.

When a topic is strong but the format is drifting into Q&A advisory, the content belongs on CO — not EB. When a topic requires citations to be credible, it belongs on EGB. When a topic is technology-specific, it belongs on GTF. When a topic is school-board-specific journalism, it belongs on SBR.

Content Goals

What a Successful Post Looks Like

A post succeeds when:

A corporate director reads it and finds the analysis directly applicable to their board's work

A nonprofit trustee reads the same post and finds the same analysis directly applicable to their context

A public agency board member reads the same post and recognizes the governance principle in their own experience

All three readers leave with a clearer understanding of how a board anchored to its mission should handle this governance challenge

No reader has to mentally translate the content out of a sector they don't belong to

What a Failed Post Looks Like

A post fails when:

It uses school-board-specific language throughout (superintendents, school districts, students) without generalizing to other sectors

It is written in Q&A advisory format (second-person, "your board should")

It primarily concerns a technology topic (belongs on GTF)

It requires formal academic citations to make its case (belongs on EGB)

It is pegged to a current event or news cycle (not evergreen)

It describes a situation without identifying and analyzing the underlying governance principle

It states a principle so abstractly that no practitioner can connect it to their own boardroom

It only makes sense for one sector without substantial revision

Why-Based Governance Alignment

Every EB post is aligned to the premise that boards exist to serve a mission — a "why." This applies across all board types:

A hospital board's "why" is the health of the community it serves

A corporate board's "why" is value creation for shareholders and stakeholders within its mission

A nonprofit foundation's "why" is the cause it was formed to advance

A public housing authority board's "why" is the residents who depend on affordable housing

Every governance principle explored on EB should connect — explicitly or implicitly — to this question: When a board is anchored to its mission and purpose, how does it handle this governance challenge?

Do not name "why-based governance" as a branded framework. Do not reference AJ Crabill, ESB, or GOTB by name (except as permitted in the cross-site linking rules). The why-based alignment is a governing editorial philosophy, not a named product.

Content Format and Structure

Overall Structure

Hook paragraph (no H2, 1–2 paragraphs)

H2: [First analytical section]

H2: [Second analytical section]

H2: [Third analytical section]

H2: [Fourth analytical section — optional]

Conclusion paragraph (no H2, 1–2 paragraphs)

Total: 3–4 H2 sections. Total word count: 600–900 words.

Hook Requirements

The hook names the governance principle or challenge being explored — it does not back into it

The hook should establish why this principle matters across board contexts

Do not begin with "Boards often...", "Many boards...", or other slow openers that delay the principle

Do not begin with a rhetorical question (weak)

Do begin by naming the principle and its stakes: "The boundary between governing and managing is among the most consequential lines a board will draw..."

The hook should make a corporate director, a nonprofit trustee, and a public agency board member all feel: "This is about something I deal with."

H2 Section Structure

Each H2 section must advance the analysis — not just add more examples of the same point. Think of each section as a move in an argument:

Section 1: What the principle is (or what the challenge is)

Section 2: Why it's hard in practice / where boards typically fail

Section 3: What it looks like when done well / the governance behavior that reflects the principle

Section 4 (optional): A complication, edge case, or nuance that completes the picture

Do not use H2 sections as containers for parallel examples from different sectors (e.g., "H2: Corporate boards," "H2: Nonprofit boards"). The cross-sector dimension should be woven throughout, not siloed into separate sections.

Conclusion Requirements

The conclusion delivers a cross-sector practical takeaway

It should complete the argument, not summarize it

It should answer: What does this mean for any board that governs a mission-driven organization?

It should leave the reader with a principle they can name and carry into their own board context

Do not end with "By following these principles, boards can..." (generic slop ending)

Do not end with a list of bullet points masquerading as a conclusion

Language Conventions — CRITICAL

Use cross-sector language at all times:

Cross-sector framing language (preferred):

"a board governing a regional health system"

"a publicly traded company's board"

"a community foundation's trustees"

"a transit authority board"

"a board governing a membership association"

"the organization's chief executive" (covers CEO, ED, president, superintendent)

Organizational language:

Refer to the chief executive role using "the CEO," "the executive director," or "the chief executive" — not "superintendent," not "president" alone (which is ambiguous)

Refer to the staff side as "management," "the executive team," or "organizational leadership" — not "administration" (school-board specific)

Refer to governed entities as "the organization" — not "the district," "the company," "the school"

Front Matter

Every post must include the following Jekyll front matter:

---

layout: page

title: "[Post title — sentence case, descriptive of the principle]"

description: "[1–2 sentence description for SEO and social sharing — names the governance principle and its cross-sector relevance]"

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

No date field. No author field. No tags unless the site uses a defined tag taxonomy.

File Naming

posts/[topic-phrase].html

The topic phrase should:

Be 2–5 words

Be lowercase, hyphen-separated

Describe the governance principle, not the conclusion

Match or echo the post title in compressed form

Examples:

posts/board-ceo-boundary.html

posts/accountability-measurement.html

posts/governance-process-traceable.html

posts/succession-planning-governance.html

posts/conflict-of-interest-design.html

In-Bounds Content

Governance Domain Areas

The following topic areas are in-bounds for EB. Every topic must be presented as applicable across board types (corporate, nonprofit, public sector).

Board-Executive Relationship

Role clarity between the board and the CEO/executive director

What the board governs vs. what management manages

How boards delegate authority without abdicating oversight

Board overreach into operational decisions

How boards evaluate the chief executive

The conditions under which boards should override management judgment

Accountability and Oversight

How boards define and measure organizational performance

Using data to govern without micromanaging

What accountability looks like at the governance level vs. the management level

Board reporting structures: what information boards actually need

When governance-level accountability is being avoided or displaced

Board Composition and Roles

What qualifications a board actually needs (vs. what it often prioritizes)

Individual board member roles vs. the board as a collective body

How boards recruit and onboard new members

The authority of an individual director vs. the authority of the board as a whole

When a board member's outside expertise creates conflict vs. value

Conflict of Interest and Ethics

How boards design conflict-of-interest policies that work in practice

The difference between a conflict of interest and an appearance of one

Governance-level ethics policies vs. management-level compliance

When fiduciary duty conflicts with stakeholder relationships

Strategic Oversight

The board's role in setting direction vs. approving a management-developed plan

How boards distinguish between governing the strategy and managing the strategy

Strategic plan adoption vs. ongoing strategic oversight

Mission alignment as a governance practice

Board Meeting Design and Effectiveness

What effective board meetings govern (and what they don't)

Consent agendas and routine business management

How boards use meeting time for governance work vs. reporting

Board committee structures and their governance purpose

The board meeting as a governance mechanism, not a management review

Board Self-Assessment and Improvement

How boards evaluate their own governance effectiveness

Board self-assessment design and follow-through

Governance improvement as a continuous practice

When boards recognize they need to change how they govern

Succession Planning

Succession planning for the chief executive (governance-level oversight)

Board succession: member recruitment, onboarding, and renewal

Emergency succession planning as a governance responsibility

Public Accountability and Stakeholder Engagement

How boards serving public or community missions handle accountability to stakeholders

Transparency as a governance principle

When stakeholder input is a governance obligation vs. a management function

Board access vs. public access to organizational information

Risk Oversight

Governance-level risk oversight (not operational risk management)

How boards identify and monitor organizational-level risk

The board's role when management has managed risk poorly

Distinguishing between risks the board must govern and risks management must manage

Governance Process Design

How boards design governance processes that are durable and traceable

A policy-based approach to governance vs. ad hoc governance

Documentation and institutional memory as governance tools

How governance processes should adapt over time

Cross-Sector Framing Requirement

Every topic must be framed and explored in cross-sector terms. When developing content:

Identify the underlying governance principle (not the sector-specific symptom)

Frame the principle in language that works for corporate, nonprofit, and public sector boards

Use composite examples from multiple sectors within the post — not just one

Ensure the analytical sections reflect patterns recognizable across board types

How to Use Multi-Sector Examples

When including examples within a post:

Use hypothetical composites only: "a regional hospital board," "a publicly traded company's audit committee," "a community foundation"

Never use real organization names

Never use real individual names

Draw examples from at least two different sectors within any single post (ideally three)

Distribute sector examples across the H2 sections — don't cluster all examples in one place

Why-Based Governance Alignment

Every post connects the governance principle being analyzed to the underlying question: How does a board anchored to its mission and purpose handle this?

This alignment is editorial, not promotional. It does not require naming any framework or branded approach. It simply means:

Every governance principle should be connected to the board's reason for existing

When analyzing where boards fail, the failure should be traceable to a loss of mission clarity or mission alignment

When describing governance done well, the why-based alignment should be implicit: the board acts in service of its purpose, not its own preferences or convenience

Existing Posts as Stylistic Models

Study these existing posts for tone, structure, and cross-sector applicability:

posts/board-ceo-boundary.html — Model for role-clarity content. How it draws the line between governance and management without being prescriptive or sector-specific.

posts/accountability-measurement.html — Model for performance/accountability content. How it handles the complexity of measuring organizational success at the governance level.

posts/governance-process-traceable.html — Model for governance process content. How it connects process design to governance effectiveness without being technical.

posts/nonprofit-governance-advantage.html — NOTE: Despite the title, study how it applies principles across sector lines even when starting from a nonprofit context.

posts/one-question-every-meeting.html — Model for board meeting design content. How it distills a practical governance insight into an actionable principle.

posts/strategic-plan-vs-governing.html — Model for strategic oversight content. How it distinguishes between the plan (management artifact) and governing (board function).

Out-of-Bounds Content

Absolute Exclusions

The following content types must not appear on effective-boards.com under any circumstances:

School-board-specific framing without cross-sector generalization Content that uses school-board terminology throughout (superintendent, school district, students, academic outcomes, graduation rates, curriculum) without generalizing to governance principles applicable across sectors. If the underlying principle is genuinely cross-sector, reframe it in cross-sector language. If it is inherently school-board-specific, it belongs on SBR or is out-of-scope for EB.

Technology-specific content Content where the primary focus is a technology, technology system, or AI. This belongs on governthefuture.com (GTF). Governance of technology use is a GTF topic. Risk oversight that happens to include technology risk is acceptable only if the post is substantively about governance-level risk oversight, not about the technology itself.

Q&A format Any post structured as a question answered by an expert or advisor. Any post written in second-person advisory voice throughout ("your board should," "you need to"). This is the CO format. EB posts analyze governance principles in third-person.

Formal academic citations Posts that require APA, MLA, or Chicago-style citations to support their claims. If a post's credibility depends on formal citations, it belongs on EGB, which is the citations-required site. EB allows informal references to research but does not use formal citation format.

News analysis or current events Content that is primarily analysis of a specific news event, regulatory change, or current situation. EB is evergreen. Posts should not require the reader to know about a specific recent event to understand the content.

Management topics Content about how organizational management (the CEO, the executive team, the staff) should operate. EB governs governance — the board's function. Content about what management should do is out of scope. Content about what the board should understand about management, or how the board governs management, is in scope.

Single-sector content without cross-sector applicability Content that only makes sense for one board type without significant revision. Apply the existential test: does this work for corporate, nonprofit, AND public sector boards? If not, revise or redirect.

Sister-Site Overlap Rules

Citation Requirements

No Formal Citations Required

EB posts do not require formal academic citations. Do not format citations in APA, MLA, Chicago, or any other academic style. Do not include a references section or footnotes.

Informal Research References — Permitted

When drawing on research to support a claim, reference it informally within the prose:

"Research on board effectiveness consistently finds that..."

"Studies of governance failures in the nonprofit sector suggest..."

"Governance researchers have long noted..."

Do not fabricate statistics. If a specific statistic is claimed, it must be real and verifiable. When in doubt, express the finding qualitatively rather than inventing a number.

Cross-Sector Examples — Composite and Hypothetical Only

All examples used in posts must be hypothetical composites. Never use:

Real organization names

Real individual names (board members, executives, governance consultants)

Identifiable organizations even without naming them

Acceptable composite example framing:

"a regional hospital system's board of trustees"

"a publicly traded manufacturer's board"

"a community foundation serving a mid-sized metropolitan area"

"a transit authority board in a large urban region"

"a professional association's elected board"

"a housing authority commission"

The composite example should be specific enough to be illustrative but generic enough that it cannot be traced to any real organization.

Grounding Document

Source: Why-Based Governing Boards: How Boards Fail, How Yours Can Become Effective by AJ Crabill Access: Google Drive ID: 1VZ76e4NNc6Spd6M6jAZ3gQvO3SVxOvZTri7QfkrRXhg (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: a — pre-draft only

Pre-draft only: Before drafting, read the relevant sections of the grounding document. Use it to calibrate the frame, vocabulary, and core claims before writing begins. It is a framing calibrator, not a citation source.

Voice Register

Register: ajc-long Fidelity: MODERATE

Blend targets:

Gladwell 35% — opens with a scene or specific case before the principle; uses narrative momentum; grounds abstractions in concrete situations

Collins 30% — analytical rigor; precise language; distinguishes between what works and what merely seems to work; willing to make a counterintuitive claim and hold it

Sinek 20% — connects governance behavior to purpose; traces what boards do back to why they exist; the "why" is always present even when not named

Gawande 15% — practitioner specificity; the clinical eye; describes what actually happens in the room rather than what should happen in theory

Sentence-length target: ~23 words per sentence average. Not every sentence is 23 words — the rhythm varies — but the average over any 5-sentence stretch should land near there. Short sentences are fine as punctuation; extended runs of short sentences are not.

Paragraph structure: 4–8 sentences per paragraph. Paragraphs shorter than 4 sentences read as underdeveloped. Paragraphs longer than 8 sentences lose the reader.

Structural invariants:

Third-person analytical throughout — no "you," no "your board," no "we"

No rhetorical questions as openers

Oxford comma always

Straight quotes only (no curly quotes)

Contractions used naturally (don't, it's, we've)

No exclamation marks anywhere

No ellipses

No voice hedging: no "I feel/think/believe" as epistemic hedges

NEVER Rules

Never use school-board-specific terminology without cross-sector generalization: "superintendent," "school district," "students" as the default beneficiary, "administration" (as staff side), "board of education," "district" (standalone) — replace with cross-sector equivalents at all times.

Never write in second-person advisory voice: "your board should," "you need to," "consider whether your board" — rewrite in third-person analytical voice. EB analyzes governance patterns; CO gives advice to a specific board.

Never open with a rhetorical question.

Never begin with a slow opener: "Boards often...", "Many boards...", "In today's governance environment...", "As boards navigate...", "Governance is increasingly...", "Board governance is a complex..."

Never end with a summary conclusion: The conclusion does not restate the H2 sections as bullet points. It completes the argument and delivers the cross-sector takeaway as a principle.

Never use real organization or individual names in composite examples.

Never generate a full HTML document: Output is front matter + body HTML only. No <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags.

Never name "why-based governance," "AJ Crabill," "ESB," or "GOTB" in a post except within a permitted list of 3 or more cross-site links.

Never include a date field or author field in Jekyll front matter.

Never include a publication date in the visible post content or meta div — the <div class="meta"> date field must be omitted (left empty or removed entirely) from the generated HTML. EB posts are evergreen reference material; visible publication dates undermine that. Jekyll may infer a date from the filename for ordering, but the template must not display it visually.

Never publish with a technology-primary focus — that content belongs on GTF.

Never publish content that requires formal citations to be credible — that content belongs on EGB.

Never publish news analysis or current-event-pegged content — EB is evergreen.

Generation Process

Follow these steps in order. Do not skip steps. Each step is a gate — if a step fails, resolve the failure before proceeding.

Step 1 — Pre-Draft Grounding Document Read

Read the relevant sections of the grounding document (Why-Based Governing Boards by AJ Crabill; Google Drive ID: 1VZ76e4NNc6Spd6M6jAZ3gQvO3SVxOvZTri7QfkrRXhg via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content). Identify the sections most relevant to the governance principle being explored. Use the grounding document to calibrate framing, vocabulary, and core claims. This is a framing calibrator, not a citation source — do not quote or cite it directly in the post.

Step 2 — Gap Analysis

Review all existing published post topics

Map each post to a governance domain area

Identify governance domain areas with no coverage or thin coverage

Produce a short list of candidate topics from underrepresented areas

Step 3 — Principle Identification

From the candidate topic list, identify the specific governance principle or challenge to explore

State the principle in one clear sentence

Confirm the principle is at governance level (not management level)

Confirm the principle is about boards (not about the CEO, the staff, or the organization's operations)

Step 4 — Cross-Sector Applicability Check

Apply the three-sector test: corporate / nonprofit / public sector

Confirm the principle applies clearly to all three

If it fails for any sector, revise the principle framing before proceeding

Note which sectors and board types will serve as the best illustrative examples

Step 5 — Hook and Outline Generation

Draft a hook that names the principle and its stakes (2–3 sentences)

Draft 3–4 H2 section titles that advance the analytical argument

Confirm each section makes a distinct analytical move (not just more examples of the same point)

Draft a one-sentence summary of the cross-sector takeaway for the conclusion

Step 6 — Draft Generation

Primary model: the configured write model

Fallback model: Claude Opus 4.8

Generate full draft from hook + outline

Target word count: 600–900 words

Write in third-person analytical voice throughout

Step 7 — Why-Based Alignment Check

Read the draft and confirm: does the post connect the governance principle to the board's mission and purpose?

The connection does not need to be explicit or branded — it should be implicit in how the principle is framed

If the post analyzes a governance behavior without connecting it to why boards exist, revise to add that dimension

A post that describes what boards do without asking why the board's mission requires it has not passed this gate

Step 8 — Language Review

Scan for sector-specific terminology (flag list: superintendent, school district, students, administration, district office, board of education)

Replace all sector-specific terms with cross-sector equivalents (see Language Conventions)

Confirm the post uses "CEO," "executive director," or "chief executive" — not "superintendent"

Confirm the post uses "the organization" — not "the district," "the school," "the company"

Confirm the post uses "management" or "the executive team" — not "administration"

Step 9 — Cross-Sector Example Check

Confirm the post includes composite examples from at least two different sectors

Confirm no example references a real organization or real individual

Confirm examples are distributed across H2 sections (not clustered)

Confirm each composite example is described specifically enough to be illustrative

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

Ultimate Failure Reporting — EB: Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (EB), article title, which check failed, attempt count, nature of each failure, and the draft. Mark status as FAILED. Do not publish.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any unicode em-dash ( — ) or en-dash ( – ) anywhere (the required form is a spaced double-hyphen "--", used sparingly); more than 1 spaced double-hyphen in a single paragraph is a flag

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (effective-boards.com):

Also flag and eliminate these EB-specific slop patterns before proceeding:

Weak openings: "In today's...", "As boards navigate...", "Governance is increasingly...", "Many boards find...", "Board governance is a complex..." — replace with an opener that names the principle directly.

Empty transitions: "It is important to note that...", "It should be said that...", "Of course...", "Certainly...", "Indeed..." — remove entirely.

Filler conclusions: Conclusions that restate the H2 sections as bullet points — replace with a synthesized principle that completes the argument.

Generic claims without grounding: "Boards sometimes struggle with..." is acceptable only if the struggle is then described specifically enough to be recognizable. Generic claims with no grounding fail.

Passive voice as evasion: "Accountability should be established" — by whom? Make governance roles explicit. Passive voice that avoids naming who does what is a slop signal.

False balance: Posts that present every governance approach as equally valid without analytical judgment are weak. EB posts make analytical claims. A post that only describes options without analyzing which governance behaviors reflect stronger principles is not doing its job.

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

Cross-sector test — mandatory for every post:

Read the post as a corporate director serving on a publicly traded company's board. Does the analysis apply directly to their experience? Is the language accessible without translation? Does anything ring false or inapplicable?

Read the same post as a nonprofit trustee serving on a hospital system's or foundation's board. Same questions.

Read the same post as a housing authority board member, a transit authority commissioner, or a city council member. Same questions.

If ANY of these readers would find the post inapplicable without significant mental translation, revise before publishing.

ESB/SBR overlap test:

Is the post so focused on school-board governance that it would fit more naturally on SBR or on a school-board-specific resource? If yes, generalize the principle to cross-sector framing or redirect.

Does the post use K-12 educational outcomes (test scores, graduation rates, student performance) as the primary frame for governance accountability? If yes, generalize to organizational performance outcomes across sectors.

CO overlap test:

Is the post written in second-person advisory voice throughout? If yes, rewrite in third-person analytical voice.

Is the post structured as an implicit Q&A (question posed, answer given)? If yes, restructure as analysis of a governance principle.

Does the post tell "your board" what to do more than it analyzes what effective boards do? If yes, shift the framing from advisory to analytical.

GTF overlap test:

Is the primary subject of the post a technology, platform, AI system, or digital tool? If yes, this belongs on GTF, not EB. Redirect.

Is the governance principle only accessible through a technology lens? If yes, same answer.

EGB overlap test:

Does the post's credibility depend on formal citations? If yes, either add citations and move to EGB, or reframe the claims qualitatively and keep on EB.

EB-specific slop patterns — additional site-specific checks:

Sector-specific terminology drift: Automatically flag and replace: "superintendent" → "CEO," "executive director," or "chief executive"; "school district" → "the organization," "the institution"; "students" as the default beneficiary → "the people served," "the community served," "beneficiaries," "those the organization exists to serve"; "administration" (as staff side) → "management," "the executive team," "organizational leadership"; "board of education" → "the board"; "district" (standalone) → "the organization."

Single-sector framing: If a paragraph only makes sense for one board type, it has drifted into single-sector framing. Revise to connect the point to cross-sector governance patterns.

Missing governance principle: If the post describes a governance situation without identifying and analyzing the underlying governance principle, the post has failed its core function. Every situation described must be connected to an analytical claim about governance.

Over-abstraction: Principles stated so broadly they connect to nothing practitioners recognize ("Boards must be accountable to their mission") without any grounding in specific governance behavior are useless. Every abstract principle must be grounded in at least one composite example.

CO-style drift: If any section has drifted into second-person advisory voice ("your board should," "you need to," "consider whether your board..."), rewrite in third-person analytical voice.

GTF-drift: If any section is primarily about a technology or technology system, remove it or redirect the post to GTF.

Conclusion-as-summary: If the conclusion only restates what the H2 sections said, it has not earned its place. The conclusion should complete the argument and deliver the cross-sector takeaway as a principle the reader can name.

Universal red-team questions — site-specific gate: Before proceeding to 8e, confirm all of the following:

Is the hook immediate? Does the first sentence name the governance principle? If not, cut the warm-up.

Does each H2 section advance the argument? Or does it repeat the same point with different examples? If the latter, restructure.

Is there at least one moment where a practitioner could say "I've seen this exact dynamic"? If the post is entirely abstract, it has failed.

Does the conclusion deliver a principle, not a summary? A summary conclusion is slop. A principle conclusion is a governance insight the reader can carry forward.

Is every claim grounded in real governance patterns? Are there any invented statistics or unsupported assertions of fact? If so, remove or reframe qualitatively.

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

Complete every item before publishing. Do not publish with any unchecked item.

Front Matter Checklist

layout: page (or confirmed equivalent) is present

title: field is present and descriptive of the governance principle (sentence case)

description: field is present (1–2 sentences, names the principle and cross-sector relevance)

No date field in front matter

No author field

<div class="meta"> date field omitted or left empty in the rendered output — do not display a publication date visually

Content Structure Checklist

Hook paragraph names the governance principle or challenge (does not back into it)

3–4 H2 sections present

Each H2 section makes a distinct analytical move

Conclusion delivers a cross-sector practical takeaway (not a summary)

Word count is within 600–900 words

Language Checklist

No sector-specific terminology present (superintendent, school district, students as default, administration, board of education)

Chief executive referred to as "CEO," "executive director," or "chief executive"

Organization referred to as "the organization" (not "the district," "the company," "the school")

Staff side referred to as "management," "the executive team," or "organizational leadership"

Third-person analytical voice throughout (no second-person advisory drift)

Cross-Sector Requirements Checklist

Post passes three-sector test (corporate + nonprofit + public sector)

At least two sectors represented in composite examples

No real organization names

No real individual names

Composite examples are specific enough to be illustrative

Why-Based Alignment Checklist

Post connects the governance principle to the board's mission and purpose

No explicit mention of "why-based governance," "AJ Crabill," "ESB," or "GOTB" (unless in permitted cross-site link list of 3+)

Quality Gates Checklist

Anti-slop scan complete (8a) — score below 1.5 or revision complete

Voice check complete (8b)

ESB governance language check complete (8c)

Site-specific checks complete (8d)

Primary red-team complete (8e)

Council red-team complete (8f) — 3 of 4 personas passed

Existential voice test passed (8g)

Technical Checklist

File named posts/[topic-phrase].html

File placed in correct directory

Jekyll build runs without errors

No broken links in post

File Naming Convention

posts/[topic-phrase].html

The topic phrase should:

Be 2–5 words

Be lowercase, hyphen-separated

Describe the governance principle, not the conclusion

Match or echo the post title in compressed form

Examples:

posts/board-ceo-boundary.html

posts/accountability-measurement.html

posts/governance-process-traceable.html

posts/succession-planning-governance.html

posts/conflict-of-interest-design.html

Independent Review Protocol

Approval flow: Auto-publish after all quality gates pass. No 72-hour editorial hold. No manual approval step. Quality gate completion is the publication trigger.

All quality gates (8a through 8g) must be completed and passed before publication. The generation process steps (1 through 9) must be completed in order before entering quality checks. Publication is triggered by the completion of the Technical Filing checklist with all items checked.

Learned Rules

Ongoing Content Integrity

Evergreen Standard

EB posts do not reference current events, specific news items, recent regulatory changes, or specific dates

Content should be as valid in five years as it is today

If a draft references "recent" events or "current" trends as the hook, reframe around the underlying governance principle, which is timeless

Do not write "in today's governance environment" or similar temporal framing

Cross-Sector Balance Over Time Monitor the body of published posts to maintain cross-sector balance:

Over any rolling six-month period, the composite examples across posts should represent all three sectors (corporate, nonprofit, public sector)

No single sector should dominate the example library

If corporate examples have been heavy recently, actively include nonprofit and public-sector composite examples in the next several posts

Cross-Site Linking Rules

EB may link to sister sites (creatingoutcomes.com, effectivegoverningboards.com, schoolboardreport.com, governthefuture.com, effectiveschoolboards.com, whybasedboards.com) at a rate of no more than 1–2 times per year

Cross-site links must appear only in a list of 3 or more resources — never as a standalone recommendation

Cross-site links must be introduced with extreme subtlety — not "our sister site" or "another resource from the same publisher"

Never name ESB, AJ Crabill, GOTB, or "why-based governance" as a branded framework in any EB post except within a permitted list of 3+ cross-site links

Do not link to effectiveschoolboards.com or whybasedboards.com more than 1–2 times per year total

Duplicate Check Before publishing any new post, confirm the governance principle has not already been explored in a published post:

Check by governance domain area

Check by the specific principle being explored

A new post may revisit a domain area, but must explore a distinct principle within that area

If the new post makes substantially the same analytical argument as an existing post with different examples, it is a duplicate — select a different topic

Terminology Consistency Maintain consistent cross-sector terminology across all posts. If a term has been used one way in a published post, use it the same way in subsequent posts:

"Chief executive" when referring to the role generically

"The organization" when referring to the governed entity generically

"Management" when referring to the staff/executive side of the governance relationship

"The board" when referring to the governing body

"Board members" or "directors" or "trustees" — use contextually, but be consistent within a single post and conscious of which term has been used in recent posts

Post Quality Audit At approximately quarterly intervals, review the last 12 published posts for:

Cross-sector balance (sector representation in examples)

Governance domain coverage (are any domain areas being neglected?)

Analytical depth (are posts making genuine governance arguments, or drifting toward description?)

Voice consistency (is the third-person analytical voice holding?)

Flag any systemic drift for correction in subsequent posts.

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"

This document is the authoritative guide for all effective-boards.com content generation. When in doubt about any editorial decision, return to the core question: Does this post explore a governance principle in a way that is directly applicable to a corporate board, a nonprofit board, and a public agency board — all three? If yes, proceed. If no, revise.