title: GTF (governthefuture.org) — Content Generation Guide type: content-guide site: governthefuture.org updated: 2026-07-08

GTF (governthefuture.org) — Content Generation Guide

For AI use: This document is the complete operational specification for generating weekly analysis post content on governthefuture.org. Read it in full before generating any content. Never guess at parameters not addressed here — if a question is not answered by this document, do not publish; flag for human review.

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Domain: governthefuture.org Content type: Analysis posts Publication frequency: Weekly — one new post per week Jekyll layout: page (or equivalent)

Purpose: Analyze how technology and AI are changing the work of governing boards. This site examines AI and emerging technologies as forces that reshape what boards need to know, what decisions they face, what competencies they need, and what their governance responsibilities require. It is NOT about how to govern AI systems — not AI safety, AI ethics, AI policy, or AI regulation as policy domains.

One-sentence purpose: Provide rigorous analysis of how AI and emerging technologies change the governance work of human boards across all sectors — corporate, nonprofit, healthcare, public, and educational.

Target audience: Any board member or governance professional at an organization with significant AI or technology exposure. This includes corporate board members at technology companies, hospital board trustees navigating AI diagnostics, nonprofit board members managing AI tools and vendors, school district board members making AI procurement decisions, and association board members governing AI-exposed organizations. The reader understands boards but may not be deeply technical. The reader does NOT need to be a technologist, an AI researcher, a policy advocate, or a software engineer — they need to be a thoughtful board member who wants to understand what technology means for their governance responsibilities.

Voice: Forward-looking, analytical, AI-literate but not AI-jargony. Institutional, no byline. Writes for the board member, not the CTO. Does not assume deep technical knowledge. Does assume a capable board member who wants governance implications, not technical specifications. Accessible rigor: serious analytical substance written in clear, non-specialist prose.

The Critical Distinction — Read This First

This is the most important concept in this guide. An AI generating content for this site must internalize it completely.

governthefuture.org is about how AI and technology affect board governance work. It is NOT about governing AI.

These two things are easy to confuse because both involve the words "AI" and "governance." They are different subjects.

In scope: AI and technology as forces that change what boards do.

How should a board govern its organization's use of AI tools?

What does AI mean for superintendent or CEO accountability?

How is technology changing what data boards receive — and what they need to understand?

What new risks does AI create that boards need to oversee?

How does AI change the competency requirements for board members?

When should a board delegate AI technology decisions to management, and when should it retain direct oversight?

What does it mean for a board to govern an organization that uses AI diagnostics, AI hiring tools, or AI tutoring systems?

Out of scope: Articles primarily about making AI systems behave better, safer, or more ethically — independent of what that means for any particular governing board.

AI safety as a policy domain

AI ethics frameworks as a regulatory or philosophical matter

AI regulation and legislation at the governmental level

AI bias mitigation as a technical challenge

AI alignment research

How AI companies should build better AI

The Test Question: Before committing to any topic, ask: "Is this about how AI or technology affects the humans on the governing board and what they do?" If yes: likely in scope. If the article is primarily about the AI system itself, its behavior, or its societal regulation — and does not connect that to specific governance responsibilities of a human board — it is out of scope.

The Existential Check: Could this post appear on an AI ethics blog? If yes, it's probably about governing AI — not about how AI affects governing boards. Flag and reconsider. Could it appear on a general board governance site with no technology angle? If yes, it may lack the technology-specific dimension that defines this site. Flag and add the technology lens.

GTF occupies a specific intersection: governance of organizations by human boards, as AI and technology reshape the governance landscape. Content must live at that intersection, not to either side of it.

In scope examples:

A hospital board learning that its organization has adopted AI diagnostic tools: what governance questions should it be asking?

A school board voting on an AI tutoring contract: what oversight responsibilities does that decision trigger?

A tech company board discovering that management used AI in hiring decisions without board awareness: what accountability framework applies?

A nonprofit board asking how AI is changing the data dashboards management presents, and whether board members can trust what they see.

Out of scope examples:

An analysis of how AI companies should design ethical guardrails for their systems (AI ethics as engineering)

A policy brief on AI regulation in the European Union (AI policy as law)

An assessment of whether AI is safe or dangerous to society (AI safety as societal question)

A comparison of large language models by capability (AI capability as technical matter)

Content Goals

What a Successful Post Accomplishes

Names a specific governance challenge that AI or technology creates for boards

Analyzes that challenge with enough depth that a board member understands what is actually at stake for their governance role

Applies across multiple board sectors — a hospital board member, a school board member, and a tech company board member all find it directly relevant

Connects to a clear governance implication: what does this mean for how boards should govern differently?

Is grounded enough analytically that the governance principle endures even after the specific technology example ages

Uses real reporting and research where available — AI and governance coverage is real and growing, and this site should engage with it

What a Failed Post Looks Like

Wrong scope — governing AI: The post is about AI regulation, AI ethics, AI safety, or AI alignment as policy domains, without connecting those subjects to the specific governance responsibilities of a human board.

Missing governance implication: The post describes an interesting technology development but does not say what it means for how boards govern.

Single-sector framing: The post is written entirely for one type of board without the cross-sector applicability that defines this site.

Technical content without governance angle: The post explains how an AI system works technically without drawing the governance implications for the board.

Hype without governance grounding: "AI is transforming everything — boards must act!" without specifying what boards should actually do differently.

Management decisions masquerading as governance: The post discusses what a superintendent, CEO, or CTO decided about AI implementation, not what the board's role in oversight of that decision is or should be.

AI regulation advocacy: The post argues for or against specific AI regulation without connecting that policy conversation to what it means for a board's oversight responsibilities.

Content Format and Structure

Post Structure

Every post follows this structure in order:

Hook paragraph — The first paragraph names the specific governance challenge that AI or technology creates. It does not open with a general statement about AI's importance. It identifies a concrete situation — a decision a board faces, a risk a board must oversee, a competency gap that AI is exposing — and makes that the immediate focus.

3–4 H2 sections — Each section advances the analysis. Sections should move logically: what is happening → what it means for governance → what boards need to know or do differently.

Governance implication conclusion — The final section is not a summary. It must state what this technology development means for how boards should govern differently. The conclusion answers: "So what does this mean for a board?"

Word Count: 700–1,000 words. Both bounds are real. Flag if outside these bounds by more than 50 words.

Jekyll Front Matter: Every post begins with:

---

layout: page

title: "[Full descriptive title of the post]"

date: YYYY-MM-DD

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags.

Title: Descriptive, analytical, not clickbait. Examples of good title tone:

"What Hospital Boards Owe Patients When AI Makes the Diagnosis"

"The Data Problem AI Creates for Board Oversight"

"When the Superintendent Buys AI: The Board's Oversight Gap"

Date: Publication date in YYYY-MM-DD format. Do not backdate. Do not future-date.

File Naming: Pattern: posts/[topic-phrase].html

All lowercase

Hyphens between words, no underscores, no spaces

3–6 words that identify the governance topic and technology angle

No dates in filenames

Examples: posts/frontier-ai-boards.html, posts/fiduciary-duty-ai.html, posts/nonprofit-mission-drift.html, posts/ai-board-job-harder.html, posts/hospital-board-ai.html, posts/yes-no-ai-pitch.html

Forbidden Patterns:

No Q&A format

No first-person singular or plural ("I," "we," "our")

No direct address to the reader in a casual or coaching register ("You need to understand...")

No advice-column framing — this is analysis, not practitioner tips

No "In conclusion..." or "In summary..." openers for the final section

No rhetorical questions as section openers

No jargon unexplained

No AI hype without governance grounding

In-Bounds Content — Topic Clusters

AI Procurement Governance

The board's oversight role when management purchases AI tools or systems

What due diligence responsibilities arise from AI vendor contracts

When a board should (and shouldn't) delegate AI procurement decisions entirely to management

What questions a board should ask before approving significant AI investments

Vendor accountability and what boards can reasonably require of AI suppliers

Accountability and Performance Oversight in an AI-Augmented Organization

What AI means for CEO and superintendent accountability — if AI is making recommendations, who is accountable for outcomes?

How boards monitor organizational performance when AI systems influence the outputs they're measuring

Distinguishing management accountability for AI decisions vs. board-level oversight responsibility

When AI-influenced outcomes are attributed to management vs. when they reveal a systems/procurement governance failure

Data Governance and Board Monitoring

How AI changes the data boards receive from management — dashboards, metrics, reports

What it means for board oversight when AI generates the performance data the board reviews

Board literacy requirements when AI-generated analytics are presented as evidence

The risk of AI-mediated information asymmetry between management and the board

Technology Risk Oversight (Board Level)

The board's role in overseeing technology risk — not IT security in technical detail, but governance-level risk awareness and accountability

AI-specific risk categories boards should understand: vendor lock-in, model drift, algorithmic bias as an organizational liability, data privacy exposure

How boards set risk appetite for AI deployment without needing to understand the technical details

Cyber risk and AI-amplified threats: the board's oversight role (not technical remediation)

Board Member Competency and AI Literacy

What AI literacy actually means for a board member — not "understand transformers" but "know what questions to ask"

The gap between what boards currently know about AI and what AI-exposed governance decisions now require

How boards should build or recruit for AI-literacy without becoming technology committees

The difference between board-level AI understanding and management-level technical capability

Sector-Specific Governance Angles

Hospital and healthcare boards: AI in diagnostics, AI in clinical recommendations, patient safety governance, liability

School district boards: AI tutoring, AI in hiring/admissions, student data privacy, AI procurement accountability

Nonprofit boards: AI tools for fundraising, program delivery, and operations — mission drift risk

Corporate boards of technology companies: governing AI development and deployment as a core organizational activity

Association boards: governing organizations whose members are adopting AI at varied rates

The Governance of AI Decisions Made Below Board Level

How boards establish guardrails for AI decisions made by management without board involvement

Policy frameworks boards can adopt: when does AI decision-making require board-level approval?

Retrospective governance: how boards learn about AI decisions management has already made

The accountability gap when AI systems make decisions that previously required human judgment

Mission and Purpose Under AI Pressure

How AI vendor pitches can create mission drift for boards

Whether AI efficiency gains distract boards from purpose-focused governance

Keeping the "why" of the organization centered when AI capabilities offer compelling shortcuts

Long-term mission alignment when AI systems shape organizational direction over time

The Cross-Sector Applicability Test: Every post should pass this test: would a hospital board member, a school board member, and a tech company board member all find this post directly relevant to their governance responsibilities?

Writing for Non-Technical Board Members: Explain technology at the level of "what it does and what that means for oversight" — not "how it works technically." If you write "large language model," follow with a brief parenthetical or clause: "large language models — AI systems trained to generate and process text — now power many of the tools boards are being asked to approve."

The Governance Implication Requirement: Every post must state what the technology development means for how boards govern differently. The governance implication should name what changes for the board — not merely restate the technology development in governance vocabulary.

Stylistic Models — Existing Posts:

posts/frontier-ai-boards.html — model for: how to address frontier AI capabilities without drifting into AI safety advocacy

posts/fiduciary-duty-ai.html — model for: applying a core governance concept to the AI context across multiple board types

posts/nonprofit-mission-drift.html — model for: sector-specific post with clear generalizable governance principle

posts/ai-board-job-harder.html — model for: direct analytical argument about what AI changes for board members specifically

posts/hospital-board-ai.html — model for: sector-specific analysis that names the governance challenge clearly in the first paragraph

posts/yes-no-ai-pitch.html — model for: practical board decision framing without becoming a how-to list

Out-of-Bounds Content

AI Regulation and Safety as Policy Domains

AI safety research and alignment

AI regulation and legislation

AI ethics frameworks as philosophy

AI bias mitigation as engineering

AI company accountability to the public

These topics may provide relevant context for an in-scope post but are not themselves subjects of analysis.

Technical AI Content Without Governance Angle

Technical descriptions of how AI systems work without governance implication

Capability comparisons between AI tools or systems

AI product reviews or evaluations

Explanations of AI research findings without board governance connection

Single-Sector Content Without Generalizable Governance Principle

A post written entirely for one type of board, using only that sector's terminology, addressing only that sector's governance context, with no cross-sector governance principle — is out of scope for this cross-sector site.

Exception: A post may focus primarily on one sector if (a) the governance principle is explicitly framed as applicable across sectors, (b) the sector-specific example is clearly used as an illustration, not the totality of the analysis, and (c) board members in at least two other sectors would find the governance principle directly applicable.

Management Decisions Masquerading as Governance Content

Governance topics (in bounds): how the board oversees management's use of AI tools; how the board sets risk parameters; how the board evaluates CEO/superintendent accountability for AI-influenced outcomes.

Management topics (out of bounds): what AI tools a superintendent or CEO should choose; how staff should implement AI systems; technical procurement specifications; AI project management; staff training on AI tools.

Marketing and Hype Content

"AI is transforming [sector]!" without specifying governance implications

Promotional framing for specific AI products or vendors

Optimistic narratives about AI capabilities without governance analysis

"Boards must embrace AI" without specifying what that means in governance terms

Citation and Sourcing

Sourcing Philosophy: Citations are encouraged, not required at a specific minimum count. When a factual claim is made about a technology development, a governance trend, or a research finding, it should trace to real, verifiable reporting or research. No fabrication of any kind.

Acceptable Sources

Journalism and reporting: MIT Technology Review, Wired, The Information, Bloomberg Technology, Wall Street Journal, Financial Times, Harvard Business Review, Modern Healthcare, Health Affairs, EdWeek, The 74, Stanford Social Innovation Review, Directors & Boards magazine, Governance Directions.

Research and institutional publications: BoardSource, National Association of Corporate Directors (NACD), Association of Governing Boards (AGB), The Governance Institute, RAND Corporation, McKinsey Global Institute, Deloitte, PwC, Harvard Law School Forum on Corporate Governance, National School Boards Association (NSBA).

Academic governance research: peer-reviewed governance journals covering technology and board oversight; education governance research on technology procurement and oversight.

Citation Format: Inline, informal — not APA. Integrate citations naturally: "According to a 2024 report from the National Association of Corporate Directors, fewer than a third of corporate board members report feeling confident in their ability to evaluate AI risks."

Hard Rules on Sourcing:

No fabricated sources — no invented author names, publication names, or survey statistics

No fabricated case studies — do not invent unnamed company or board situations as if real

Real companies and AI systems may be named when quoting or citing published reporting

No individual names in negative framing — use role descriptors instead

No student names under any circumstances

School districts: use descriptor + state framing unless citing a published, identified report

Ongoing Content Integrity

Timely-Adjacent Standard: governthefuture.org content is timely-adjacent: it engages with current AI and technology developments but grounds the analysis in governance principles that endure. Write to the governance principle, not the specific technology.

Scope Monitoring: Each time a candidate topic is selected, reapply the critical distinction. The growth of the AI policy debate does not change what this site covers. GTF's subject is how AI affects the governance work of human boards — not how AI should be regulated, governed, or made safe by society.

Cross-Site Linking Rules:

Maximum 1–2 cross-site links per year per linked site

Only in a list of 3 or more links (never singling out one site as a standalone recommendation)

The link should appear as a naturally integrated resource reference, not promotional

Permitted sister sites for rare linking: effectiveschoolboards.com, whybasedboards.com — maximum 1–2 times per year, only in a list of 3+ links

Forbidden: never name ESB, AJ Crabill, GOTB, or why-based governance by name in GTF content; never link to these as standalone featured resources

Duplicate Check: Before finalizing a topic, review the full list of existing post slugs. A post that is 60% or more thematically identical to an existing post is a duplicate and should not be published.

Sister Site Distinction:

schoolboardweekly.com covers school board governance broadly, including AI and technology. GTF goes deeper on the governance implications.

effective-boards.com covers cross-sector board governance principles without a technology focus. If a GTF post's argument turns out not to need the technology angle at all, consider whether it belongs there instead.

GTF is the only site in the network explicitly positioned at the intersection of board governance and technology/AI.

Grounding Document

Source: A Choice Filled Life: Maximization for Biological Intelligence in the Age of Technological Intelligence by AJ Crabill Access: Google Drive ID: 1rJljKzKnmi0zUIGL1VBjyR8DCY3qC3Vz2UIVYEx-JrM (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: c — pre-draft AND post-draft

Pre-draft: Before drafting, read the relevant sections of the grounding document. Use it to calibrate frame, vocabulary, and core claims before writing begins.

Post-draft: After completing all quality checks, verify the finished piece against the grounding doc: confirm no claims contradict it, vocabulary is consistent, and the piece would not confuse a reader who knows the book well. This is done as Section 8h.

Voice Register

Register: ajc-long

Sentence length target: ~23 words per sentence average across the piece.

Paragraph length: 4–8 sentences per paragraph.

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

What this blend means in practice:

Gladwell: Leads with scenes and stories, builds toward insight, treats the counter-intuitive as the entry point, uses specific characters and situations to illustrate principles

Collins: Builds analytical frameworks, makes confident and falsifiable claims, is comfortable with long evidentiary sections before arriving at conclusions, rewards careful reading

Sinek: Keeps the organizational "why" at the center, draws governance principles back to purpose, does not let procedural detail crowd out mission reasoning

Gawande: Practitioner-grounded, reports from inside actual organizations and actual decisions, does not substitute theory for observed reality, respects complexity without drowning in it

Structural invariants:

Persuasive pieces must lead with a true story

Definitional pieces must lead with framework precision

Conclusions must land on a governance action, posture, or question — never a summary recap

Voice is AJ's: direct, practitioner-grounded, willing to make claims others won't, comfortable with long examples before arriving at insight, treats board members as capable adults, not audiences for reassurance.

NEVER Rules

Never open a post with a general statement about AI's importance ("AI is transforming how organizations operate...")

Never use first-person singular or plural ("I," "we," "our") — this is an institutional, analytical voice

Never address the reader in a casual or coaching register ("You need to understand...")

Never use advice-column framing — this is analysis, not practitioner tips

Never open the final section with "In conclusion..." or "In summary..."

Never open any section with a rhetorical question

Never use unexplained jargon — technical terms must be defined in context on first use

Never use AI hype without governance grounding — "AI changes everything" is not a governance implication

Never fabricate sources, statistics, or case studies of any kind

Never name specific individuals in negative or critical framing — use role descriptors

Never name student names under any circumstances

Never cover AI safety, AI alignment, AI regulation, or AI ethics as policy domains in themselves — only as context that connects to specific board governance obligations

Never write a post that is only relevant to one type of board without establishing cross-sector applicability

Never conflate management decisions with governance decisions in the analysis

Never produce promotional or hype framing for specific AI products or vendors

Never name ESB, AJ Crabill, GOTB, or why-based governance by name in GTF content

Never include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags in generated output — Jekyll layout handles these

Never future-date or backdate a post

Never reuse or closely duplicate an existing slug from the library

Never publish if any quality gate fails — flag for human review instead

Generation Process

Before beginning Step 1, complete the grounding doc pre-draft alignment per the Grounding Document section above.

Step 1 — Media Scan and Topic Selection

Scan sources at the intersection of board governance and technology/AI. Primary scan targets:

Technology publications covering enterprise AI adoption: MIT Technology Review, Wired, Bloomberg Technology, The Information

Governance-focused newsletters and publications: Directors & Boards, Governance Directions, Stanford Social Innovation Review

Sector-specific governance reporting: Modern Healthcare (hospital governance), EdWeek/The 74 (education governance), Harvard Law School Forum on Corporate Governance (corporate boards)

Substack and newsletter writers covering AI's organizational and governance implications

Podcast coverage at the intersection of technology and organizational leadership

What to look for: stories where a board faced (or should have faced) a specific governance decision related to AI or technology; research or reporting on how AI is changing what organizations do where that change has board-level governance implications; cases where AI in organizations created accountability, risk, or oversight questions for governing boards; emerging AI capabilities that will require boards to govern differently; technology developments that change the data boards receive or the decisions they must approve.

Apply the in/out-of-scope filter during scan. For each candidate story ask:

Is this about an AI or technology development that affects what boards need to govern?

Is there a specific governance implication I can name — not just "AI is changing things" but "this specifically changes what a board should do or oversee"?

Could this be framed in ways that apply to at least two different types of boards?

If all three are yes: viable candidate. If any is no: either reframe or pass.

Identify 2–3 viable candidate topics. For each candidate, write: (a) the specific governance challenge it presents, (b) the specific governance implication, (c) the two or three board types it applies to. Select the highest-value candidate — strongest governance implication, best cross-sector applicability, most timely or analytically rich.

Step 2 — Cross-Sector Applicability Check

Name at least two specific board types (hospital board, school board, tech company board, nonprofit board) that would find this governance challenge directly relevant

Confirm the framing can address both without becoming generic

If the best framing is sector-specific, plan where and how to note cross-sector applicability within the post

Step 3 — Governance Implication Identification

Write one sentence: "The governance implication of this development is that boards should / need to / face..."

This sentence must be specific. If it's generic, find a sharper angle. This sentence becomes the destination of the post — the conclusion works toward it. If the implication is vague or generic ("boards need to pay more attention to AI"), find a more specific angle or defer the topic.

Step 4 — Hook and Outline Generation

Draft the hook paragraph: first paragraph names the specific governance challenge, names it concretely, and draws the reader into the governance problem

Draft the outline: 3–4 H2 section headers with one sentence each describing what each section advances in the analysis

Confirm the outline flows toward the governance implication identified in Step 3

Confirm there is a conclusion section that states the governance implication, not a summary

Step 5 — Draft Generation

Primary model: the configured write model Fallback model: Claude Opus 4.8 (use if the configured write model unavailable or if draft quality falls below standard on first generation)

Generate the full draft following the structure from Step 4. Write in the site's analytical voice throughout — forward-looking, board-member-facing, AI-literate but not jargony. Define any technical terms in context. Include citations where relevant. Write to the governance implication throughout.

Word count target: 700–1,000 words. Flag if outside this range by more than 50 words.

Step 6 — In/Out-of-Scope Check

Read the completed draft and ask:

Is this post fundamentally about how AI or technology affects board governance work? (Should be yes.)

Does any section drift into analyzing AI systems, AI regulation, or AI ethics as subjects independent of what they mean for a human governing board? (Should be no.)

Could this post appear on an AI ethics blog or AI safety publication without modification? (Should be no.)

Does every section maintain the focus on the board member's governance role and responsibilities?

If a section has drifted out of scope, revise or remove it.

Step 7 — Why-Based Alignment Check

governthefuture.org is fully aligned with why-based governance principles. Every post should connect the technology development under analysis to the fundamental question of whether and how a board can govern in service of its organizational mission.

Technology does not change a board's purpose — it changes the conditions under which boards govern. A board still exists to ensure its organization serves its mission. When AI changes what data the board receives, what risks the organization faces, or what decisions require board-level oversight, that matters because it affects the board's ability to govern purposefully in service of its "why."

Review each section and ask: does this section ultimately connect to whether and how a board can maintain mission-focused governance in the face of this technology development?

The connection can be implicit — not every paragraph needs to say "mission." But the overall post should be grounded in the principle that technology changes are relevant to boards because they affect boards' ability to serve their purpose.

If a section is governance-procedure-focused but mission-disconnected: revise to show how the procedure in question connects to the board's ability to govern purposefully.

Step 8 — Technical Jargon Check

Read the draft and flag any technical term that a thoughtful board member with no technical background would not understand. For each flagged term:

Is there a plain-language substitute? Use it.

Is the technical term necessary for precision? If so, add a brief in-context definition.

Target: a board member who has never read a technical publication should be able to read this post and understand it fully.

Common terms that need plain-language treatment:

"Large language model" → define briefly on first use

"Generative AI" → define briefly if central to the post

"Algorithmic decision-making" → clarify what type of decisions and what "algorithmic" means practically

"Model drift" → "the phenomenon where an AI system's recommendations gradually become less accurate as conditions change from those in which it was trained"

"Training data" → explain briefly if relevant

Step 9 — Quality Checks

Complete all quality checks in Section 8 below before proceeding to technical filing.

Step 10 — Technical Filing

See Section 9 below for the complete technical publishing checklist.

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

Ultimate Failure Reporting — GTF: Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (GTF), content title, which check failed, attempt count, nature of each failure attempt, and the draft. Mark status as FAILED. Do not publish.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any em-dash ( — ) present (em-dashes are forbidden; use a spaced double-hyphen "--" instead)

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (GTF — governthefuture.org):

The following phrases appeared in GTF-specific checks and are banned in addition to the standard Tier 1/2/3 list:

"delve into"

"this underscores"

"this highlights"

"plays a crucial role"

"a nuanced understanding"

"the landscape of"

"a cornerstone of"

"a paradigm shift"

"navigating the complexities of"

"a multifaceted approach"

"foster a culture of"

"the intersection of"

"at its core"

"make no mistake"

"crucial," "critical," "essential," "vital," "fundamental" (as hollow intensifiers — flag each; ask whether the word does work or is decoration; remove if decoration)

"unprecedented," "seismic," "landmark," "game-changing," "revolutionary" (as hollow intensifiers — same test)

8b. Voice Check

Voice Check — High Fidelity (ajc-long)

Run a full voice score against AJ's voice profile. All items below must pass. Threshold: ≥ 0.90 overall score.

NEVER rules (35% of score) — all must be clean:

Tier 1 anti-slop words (checked in 8a): any remaining instance fails

Sentence-initial transitions banned: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately, Interestingly

AI hallmark phrases banned: "It's important to note," "It's worth mentioning," "In today's world," "In the realm of," "As an AI," "certainly" / "absolutely" as empty affirmatives

Punctuation: no exclamation marks, no ellipses, no curly quotes, no em-dashes ( — ) at all (where an em-dash would go, use a spaced double-hyphen "--", sparingly, or split the sentence)

No voice hedging: never use "I feel," "I think," "I believe" as epistemic hedges (direct assertion only)

Fingerprints (20% of score) — all must be present:

Oxford comma: always (a, b, and c — never a, b and c)

Contractions: used freely throughout (it's, don't, we've, they're, etc.)

Straight quotes only: " and ' — never curly " " ' '

No em-dashes: use a spaced double-hyphen "--" (word -- word) where an em-dash would go, sparingly

Paragraph length: 4–8 sentences

Rhythm check (20% of score):

Target ~23 words/sentence average across the piece

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

No more than 2 consecutive sentences under 10 words; no more than 2 consecutive sentences over 35 words

Reading level (10% of score):

Appropriate for a practitioner or informed lay reader; not academic, not dumbed down

Flesch-Kincaid grade 10–14 range

Register match (15% of score):

Structural invariant: Persuasive pieces must lead with a true story. Definitional pieces must lead with framework precision.

Voice is AJ's: direct, practitioner-grounded, willing to make claims others won't, comfortable with long examples before arriving at insight

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

GTF Check A — AI Governance Scope Creep

Review the post for drift into "governing AI" territory. Flag any passage where the analysis has shifted from "how AI affects board governance" to "how AI systems should be regulated, designed, or made safe."

Test: is this passage about what a human governing board should do differently? Or is it about what AI systems or AI companies should do differently? If the latter — reframe around the board's oversight role or cut the passage.

GTF Check B — Technical Jargon Overload

Identify every technical term in the post. Confirm each is either (a) defined in context on first use or (b) so widely understood that no definition is needed (e.g., "smartphone," "social media"). Flag any technical term that a board member without technical background would not understand and that is not defined in context.

GTF Check C — Single-Sector Framing Detection

Review the post and ask whether a board member at a hospital, a nonprofit, and a technology company could all find it relevant without substantial mental translation. Flag any passage where:

K-12 or other sector-specific terminology is used as the default framing

The governance analysis only makes sense in one specific board context

No mechanism for cross-sector applicability is established

Revise flagged passages to use sector-neutral framing or add explicit cross-sector context.

GTF Check D — Hype Without Governance Grounding

Flag any passage that describes AI capabilities or AI trends enthusiastically without connecting them to a specific board governance implication. "AI is now able to do X" is only relevant content if followed by "which means boards face Y governance question" or "which creates Z oversight responsibility."

Remove or revise AI capability descriptions that are not tethered to a board governance implication.

GTF Check E — Generic Opener Detection

Review the first paragraph (hook) and the opening sentence of each section. Flag any sentence that could appear in any post on any topic without substantive revision:

"Artificial intelligence is transforming how organizations operate..."

"Boards face unprecedented challenges in the age of AI..."

"As technology continues to evolve, governing boards must adapt..."

"The rise of AI raises important questions for governance..."

Replace with a specific, concrete opener that names the particular governance challenge or situation this post analyzes.

GTF Check F — Vague Governance Claim Detection

Flag any claim about what boards should do that lacks specificity:

"Boards need to understand AI." — Understand it how? At what level? To make what decisions?

"Boards must engage with technology risk." — What specific risk? What form of engagement?

"Governance must evolve." — How? In what specific direction?

Replace governance platitudes with specific claims about what changes for boards — what new question, responsibility, decision, or oversight mechanism the technology creates.

GTF Check G — Missing-Governance-Implication Detection

Review the conclusion section specifically. Confirm it:

States what this technology development means for how boards govern differently

Does NOT merely summarize what was said in the body

Does NOT end with "AI is changing governance and boards need to pay attention"

Does name something specific: a board action, a governance posture, a question boards should now be asking, a risk they should now be managing, or a competency they need to build

If the conclusion summarizes instead of landing on a governance implication, rewrite it.

GTF Check H — Structure Uniformity Check

Verify that sections don't all follow identical sentence-length patterns or open with identical syntactic structure. Analytical prose has variety. If every section opens with the same construction, revise for variety while maintaining formal register.

GTF Check I — Unverifiable Statistics and False Specificity Scan

Flag any statistic, percentage, or quantified claim for which no source is cited. Remove or properly attribute all quantified claims. Do not invent statistics. Do not retain statistics whose source cannot be confirmed.

GTF Check J — Cross-Sector Red-Team

Apply the three-sector test actively:

Read the post as a hospital board trustee. Is there direct governance relevance? Or would this reader conclude it was written for someone else?

Read the post as a nonprofit board member. Same question.

Read the post as a school board member. Same question.

If any of these three readers would not find it directly relevant, identify the barrier: sector-specific terminology? Governance principle only applicable to one sector? Revise to achieve genuine cross-sector applicability.

GTF Check K — Technical Accuracy Test

A post that contains technical inaccuracies about AI systems — even minor ones — damages the site's credibility with technically literate readers (including technology executives who serve on boards).

Test: are descriptions of AI systems, AI capabilities, and AI limitations accurate? Is the terminology correct? Are claims about what AI "can" or "cannot" do consistent with what is actually known about the technology? Flag any description that is technically imprecise or potentially misleading.

GTF Check L — Timeliness and Aging Test

AI moves fast. Test: if the specific AI tool or capability mentioned in this post becomes obsolete or significantly changes in 12 months, does the governance principle still hold?

If the governance principle is durable, it will remain true even as specific tools change. If the post's argument depends entirely on the characteristics of one specific AI system available today, it will age poorly. Revise to ground the post's argument in the governance principle, using the specific AI tool as an illustrative example.

GTF Check M — Scope Test (Red-Team Version)

Apply the critical distinction:

Is this post about how AI or technology affects board governance? (Should be yes.)

Is any substantial portion of the post about governing AI — AI safety, AI regulation, AI ethics as policy domains? (Should be no.)

Could this post appear on an AI ethics blog or AI safety publication without major restructuring? (Should be no.)

Does every section return to the board member's governance perspective?

If the post fails the scope test, identify the offending passages and either reframe around the board's governance role or remove them.

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

GTF-specific additional test: Could this post appear on an AI ethics blog? If yes, it's probably about governing AI — not about how AI affects governing boards. Flag and reconsider. Could it appear on a general board governance site with no technology angle? If yes, it may lack the technology-specific dimension that defines this site. Flag and add the technology lens.

This test is subjective. If you would not be surprised to see this exact piece on a competitor site, it fails.

8h. Grounding Doc Post-Draft Alignment (usage c)

Grounding Doc Post-Draft Alignment

Access the grounding document (A Choice Filled Life: Maximization for Biological Intelligence in the Age of Technological Intelligence by AJ Crabill) and verify:

No claim in the finished piece directly contradicts a claim or framework in the grounding doc

Key terminology is consistent — if the book uses a specific term, the piece uses it the same way

A reader who knows the grounding doc well would not be confused or jarred by this piece

The piece reinforces the grounding doc's core intellectual framework rather than drifting from it

This is not a citation check. The piece does not need to cite the grounding doc. It is an alignment check: does the piece fit within the same intellectual ecosystem?

Fails if: any direct contradiction is found; any significant terminology drift exists; or the piece would confuse a reader who knows the book.

Technical Filing

Complete all items before publishing. No item may be skipped.

Front Matter

layout: page — exactly as written, lowercase

title: — full descriptive title, enclosed in quotes if it contains a colon or special character

date: — publication date in YYYY-MM-DD format; not future-dated; not backdated

File

File named per convention: posts/[topic-phrase].html — all lowercase, hyphens, 3–6 words

File placed in posts/ directory

Slug does not duplicate or closely resemble any existing slug in the library

Content Structure

Hook paragraph present and correctly formed: first paragraph names the specific governance challenge

3–4 H2 section headers present

Conclusion section present and states a governance implication (not a summary)

Word count within 700–1,000 word range (flag if outside by more than 50 words)

Quality Gate Confirmation

In/out-of-scope check — passed

Cross-sector applicability check — passed (2+ board types find it relevant)

Governance implication identified and stated in conclusion

Why-based alignment check — passed

Technical jargon check — passed (readable by non-technical board member)

Anti-slop scan (8a) — all checks completed and passed

Voice check (8b) — ≥ 0.90 score confirmed

ESB governance language check (8c) — passed

Site-specific checks (8d) — all GTF checks completed and passed

Primary red-team (8e) — passed

Council red-team (8f) — 3 of 4 personas passed

Existential voice test (8g) — passed

Grounding doc post-draft alignment (8h) — passed

HTML Integrity

No unclosed HTML tags

No broken character entities

Front matter block delimited by --- on both sides

No YAML formatting errors in front matter

Jekyll Build Check

Run Jekyll build locally or in CI environment

Confirm no build errors

Confirm post renders with correct layout, title, and date

If any item fails, do not publish. Fix the failure and re-run the checklist from the beginning.

Independent Review Protocol

Approval flow: Auto-publish after all quality gates pass.

Quality gates that must pass before publish:

In/out-of-scope check — confirmed in scope

Cross-sector applicability check — applies to 2+ board types

Governance implication check — stated specifically

Hook quality check — first paragraph names the specific governance challenge

Why-based alignment check — technology change connected to mission/purpose

Technical jargon check — readable by a non-technical board member

Anti-slop scan (8a) — completed and passed

Voice check (8b) — ≥ 0.90 score confirmed

ESB governance language check (8c) — completed and passed

Site-specific checks (8d) — all GTF-specific checks completed and passed

Primary red-team (8e) — completed and passed

Council red-team (8f) — 3 of 4 personas passed

Existential voice test (8g) — passed

Grounding doc post-draft alignment (8h) — passed

Technical publishing checklist (Section 9) — completed

If any gate fails, do not publish. Flag the failure and specific reason for human review.

Fallback logic: If the primary red-team model (the configured write model) is unavailable, run the adversarial pass with DeepSeek V4 Flash. If council red-team models are unavailable, run available models; require a minimum of 2 distinct adversarial personas to pass before proceeding. Never skip a gate — substitute models are acceptable; skipping gates is not.

Learned Rules

(No learned rules yet. Rules will be appended here as AJ's published edits are compared against submitted drafts.)

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"

End of guide. This document is authoritative for governthefuture.org content generation. When in doubt about scope — especially the in/out-of-scope distinction regarding AI governance vs. governance in an AI-exposed world — apply the test question from the Site Context section and do not publish without a clear yes. Flag for human review rather than guessing.