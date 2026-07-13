title: schoolboardreview.com — Dynamic Content Creation Guide type: content-guide site: SBRV (schoolboardreview.com) updated: 2026-07-08

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

Domain and Content Type

Domain: schoolboardreview.com Abbreviated: SBRV Content type: Scored board meeting reviews Publication frequency: As board meetings occur and are reviewed; approximately monthly Jekyll layout: review

Purpose

schoolboardreview.com exists to evaluate real school board meetings against a consistent governance rubric and publish scored reviews. The site serves community members, board members, and governance advocates who want to know: how well is a specific board performing its governance function?

Every review answers a single core question: At this meeting, did this board govern effectively?

The answer is not a policy opinion. It is a governance assessment — a judgment about process, role, relationship, and accountability, measured against rubric criteria, grounded in observable evidence from the meeting materials.

Why Real District Names Are Used

SBRV is the only site in the network where real district names are used. Every other site in the network uses composite or hypothetical examples. SBRV does not.

This is intentional and non-negotiable. A governance review is meaningless without identifying the specific board being reviewed. The assessment is inherently tied to a specific institution, at a specific meeting, at a specific point in time. Anonymizing the district would render the review useless to the very audiences it serves.

When you are uncertain whether content belongs on SBRV, ask: Is this a scored evaluation of a real board meeting? If yes, it belongs here. If not, it belongs on a sister site.

What makes SBRV distinct from sister sites:

schoolboardreport.com analyzes patterns across boards or districts. SBRV evaluates one board at one meeting.

schoolboardresearch.com evaluates research about governance. SBRV evaluates actual governance practice.

SBRV is specific. That specificity is the entire point.

Target Audience

Community members who want to understand how their board is performing

Board members seeking an external assessment of their own board's practice

Governance advocates who track board performance across districts

Journalists covering school board governance or specific districts

Researchers tracking board behavior over time or across regions

Write as if you are being read by a thoughtful community member who cares about their district and wants to understand what happened at a board meeting — and by a board member who wants honest, fair, rubric-grounded feedback.

Voice

The SBRV voice is scoring-evaluative, rubric-anchored, observational, and analytical.

Think of a thoughtful referee: applying consistent criteria, noting what was seen, reaching a judgment. Not cheerleading. Not prosecuting. Not advocating.

The voice is not:

Adversarial or accusatory

Advocacy for any policy position

Praise or condemnation of board decisions based on their content

Personal or targeted at individuals

The voice is:

Grounded in observable evidence from meeting materials

Specific ("The board spent 47 minutes on the facilities update with no connection to student outcome goals" — not "The board seemed unfocused")

Consistent across districts (same behaviors earn similar scores regardless of which district is being reviewed)

Respectful but honest (a low score is a low score; do not soften scores that are not earned, and do not inflate scores to avoid discomfort)

Scoring Rubric Overview

Every SBRV review evaluates the board meeting across six governance dimensions. All six must appear in every review. None are optional.

Each dimension is scored on a 1–5 scale:

1 — Significant governance concern. Clear evidence of a governance failure in this dimension.

2 — Below adequate. Noticeable weaknesses; some governance functions present but incomplete.

3 — Adequate. The board performed this governance function at a functional level. No major concerns, no notable strengths.

4 — Strong. The board demonstrated clear governance competence in this dimension with identifiable strengths.

5 — Exemplary. Outstanding governance practice in this dimension; a model of what good looks like.

The overall governance score is the simple average of all six dimension scores, rounded to one decimal place.

The six dimensions:

Role Clarity — Did the board stay in governance territory, or did it drift into management and operations?

Outcome Focus — Did board discussion connect to student outcome goals?

Superintendent Relationship — Was the board-superintendent dynamic healthy and appropriate?

Public Participation Governance — Was public comment handled in a way that reflects the board's governance role?

Meeting Process — Was the meeting structured to enable effective governance?

Accountability and Transparency — Did the board communicate clearly about decisions, rationale, and outcomes?

Content Goals

What a Successful Review Looks Like

A successful SBRV review:

Accurately identifies the district, meeting date, meeting type, and quorum

Demonstrates that the reviewer engaged with the actual meeting materials (agenda, minutes, recording, or some combination)

Evaluates all six rubric dimensions with specific, observable evidence for each score

Assigns scores that are consistent with the narrative — if the narrative describes serious governance breakdowns, the score should reflect that, and vice versa

Maintains strict policy neutrality — evaluates how the board made decisions, never what it decided

Names the district but protects individuals, students, and staff from harmful identification

Reaches an overall score and verdict that accurately summarizes the six-dimension assessment

Is readable and useful to a community member who did not attend the meeting

What a Failed Review Looks Like

A failed SBRV review:

Advocacy disguised as evaluation — the review expresses an opinion on whether the board made the right policy call (e.g., "the board correctly prioritized safety" or "the board's decision to cut the arts program was shortsighted")

Incomplete rubric — one or more of the six dimensions is missing, underdeveloped, or assessed without evidence

Score-narrative mismatch — the score says 4 but the narrative describes a board that barely functioned; or the score says 2 but the narrative praises the board's performance

Individual naming in negative framing — a board member is named in connection with a criticism or failure

Student identification — any student is named or described in identifiable terms

Vague observation — "the board seemed engaged" or "there was some discussion" without specific reference to what actually happened

Score inflation — giving 4s and 5s across all dimensions for a meeting that did not earn them, to avoid the discomfort of a low score

Sourcing opacity — the review does not indicate what materials it is based on

Content Format and Structure

File Naming

Pattern: reviews/[district-slug]-[mon-year].html

Examples:

reviews/jefferson-city-sd-may-2026.html

reviews/bellevue-sd-may-2026.html

reviews/seattle-public-schools-dec2025-may2026.html

Slug rules:

Lowercase, hyphen-separated

Use the district's common abbreviated name if one is widely recognized (e.g., seattle-public-schools, not seattle-public-schools-district)

Include sd (school district) as needed to disambiguate

For reviews spanning multiple meetings, use the date range (e.g., dec2025-may2026)

Month abbreviations: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec

Front Matter Fields

---

layout: review

title: "[District Name] Board Meeting Review — [Month Year]"

district: "[Full District Name]"

date_display: "[Month Day, Year]"

review_date: "[YYYY-MM-DD]"

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

Example:

---

layout: review

title: "Jefferson City School District Board Meeting Review — May 2026"

district: "Jefferson City School District"

date_display: "May 15, 2026"

review_date: "2026-05-15"

---

Document Structure

1. Meeting Introduction (approximately 150–200 words)

Open with the district name, meeting date, meeting type (regular session, special session, work session, emergency meeting, etc.), and whether quorum was established. Briefly describe what was on the agenda — not an exhaustive list, but enough to orient a reader who was not there. Note the primary governance topics (e.g., budget adoption, superintendent evaluation, policy first reading).

Do not editorialize in the introduction. This section is orientation, not assessment.

2. Rubric Sections — Six Scored Dimensions (approximately 100–175 words each)

Each dimension gets its own H2-level section. The format for each section:

## [Dimension Name]

**Score: [X]/5**

[Narrative: 100–175 words of specific, evidence-grounded assessment]

Order the sections consistently in every review:

Role Clarity

Outcome Focus

Superintendent Relationship

Public Participation Governance

Meeting Process

Accountability and Transparency

3. Overall Score and Summary Verdict (approximately 150–200 words)

Present the overall governance score (average of six dimensions, to one decimal place). A brief score summary table helps readability:

| Dimension                       | Score |

|---------------------------------|-------|

| Role Clarity                    | X/5   |

| Outcome Focus                   | X/5   |

| Superintendent Relationship     | X/5   |

| Public Participation Governance | X/5   |

| Meeting Process                 | X/5   |

| Accountability and Transparency | X/5   |

| **Overall Governance Score**    | **X.X/5** |

Follow the table with a 150–200 word summary verdict: what this score means for this board, what the most notable governance strengths were, and what the most significant governance gaps were. Do not re-evaluate policy content here. Do not name individuals. Do not soften a low score that was earned.

4. Sources and Transparency Note

Every review must include a brief transparency note identifying what materials the review is based on:

This review is based on [the board's public meeting agenda / meeting minutes / public video recording / combination of the foregoing], all of which are publicly available through the district's official website. [If materials were incomplete or unavailable, note specifically what was missing and how that affected the review.]

Word count target: 1,000–1,500 words total (excluding front matter and scoring table).

In-Bounds Content

What to Evaluate

SBRV evaluates governance process — how the board did its work. This includes:

Whether board discussion stayed in governance territory (setting direction, monitoring outcomes, making policy) or crossed into management territory (operational details, staffing decisions, program implementation)

Whether board questions and discussion connected to student outcome goals

Whether the board's relationship with the superintendent was functional and appropriate — the board setting direction, the superintendent implementing

How public comment was handled as a governance matter

The quality of the meeting's structure and use of time

The board's communication about what it decided and why

What NOT to Evaluate

SBRV does not evaluate the substance of policy decisions. Specifically:

Do not assess whether the board made the right call on curriculum, calendar, budget line items, hiring decisions, or any other policy matter

Do not evaluate the quality of district programs — only whether the board's discussion of those programs connected to governance functions

Do not assess the superintendent's professional performance — only whether the board's interaction with the superintendent reflects appropriate board-superintendent relationship dynamics

Budget governance process is in-bounds; budget line items are out-of-bounds. You can evaluate whether the board asked outcome-focused questions during budget discussion. You cannot evaluate whether specific budget allocations were wise.

In-bounds: "The board's budget discussion lasted 90 minutes but produced no connection to the district's stated student outcome goals. Board members asked primarily operational questions about cost line items rather than governance-level questions about whether resources were allocated in service of outcomes."

Out-of-bounds: "The board's decision to increase the transportation budget was the right call given the district's geography." Or: "Cutting the arts program was a mistake."

How to Describe Board Member Behavior Without Naming Individuals

Individual board member names should almost never appear in negative or critical contexts. Use role-based descriptions:

"a board member" (for general reference)

"one board member" / "another board member" (when distinguishing between members)

"the board chair" (for the presiding officer -- role-based, not name-based; use "board chair," not "board president")

"the majority" / "a board minority" (when describing vote dynamics)

"a member who voted against the motion" (describing vote without naming)

Exception: Attribution is acceptable when:

The action is a formal vote (votes are public record)

The statement is an official, public statement the member made in their official capacity

The action is documented in official minutes as attributed to a named member

Even when attribution is acceptable, ask: does naming this individual add meaningful information to the governance assessment? If not, default to role description.

When in doubt, use role description.

Rubric Deep-Dive: What to Look For in Each Dimension

DIMENSION 1: ROLE CLARITY Did the board stay in governance territory or drift into management/operations?

What governance looks like:

Board sets direction through policy, then delegates implementation to the superintendent

Board questions are about outcomes, goals, strategy, and accountability — not operational details

Board members do not direct staff (other than the superintendent)

Board action items produce policy or governance decisions, not operational directives

What role drift looks like:

Board members asking staff directly about operational details (how many buses? which vendor? what curriculum materials?)

Board members suggesting specific operational solutions during discussion

Board spending significant agenda time on operational items (purchasing, staffing, facilities maintenance, program implementation details)

Board members accepting reports that detail operational activity without connecting it to governance functions

Board directing the superintendent's work at an operational level of detail

Scoring guidance:

1 — Board consistently operated in management territory; governance function was largely absent from the meeting

2 — Significant role drift on one or more major agenda items; some governance-appropriate behavior but outweighed by drift

3 — Mix of appropriate and inappropriate behavior; board generally understood its role but crossed into management territory at times

4 — Board largely stayed in governance territory; occasional minor drift that didn't significantly undermine the governance function

5 — Board demonstrated clear, consistent role clarity throughout; discussions stayed at governance altitude; no meaningful drift

DIMENSION 2: OUTCOME FOCUS Did board discussion connect to student outcome goals?

What outcome focus looks like:

Board references the district's stated student outcome goals during discussion

Board members ask: "How does this connect to what we're trying to achieve for students?"

Reports to the board include outcome data, not just activity data

Board accepts or rejects agenda items based on their relationship to outcome priorities

Budget discussion, facility discussion, and policy discussion are anchored to outcome goals

What lack of outcome focus looks like:

Discussions proceed without reference to student outcomes

Board accepts activity reports ("we did this thing") without asking about impact ("did it work for students?")

Board asks operational questions but not outcome questions

Outcome goals are mentioned in passing but don't drive discussion or decision

Scoring guidance:

1 — No meaningful connection to student outcomes appeared in any substantive board discussion

2 — Outcome references were token or formulaic; discussion did not genuinely connect to outcomes

3 — Some agenda items connected to outcomes; others did not; inconsistent but not absent

4 — Most discussion maintained some connection to outcomes; board regularly referenced its outcome goals

5 — Outcome focus was consistent, substantive, and visibly drove board discussion and decision-making throughout the meeting

DIMENSION 3: SUPERINTENDENT RELATIONSHIP Was the board-superintendent dynamic healthy and appropriate?

What a healthy relationship looks like:

Board sets direction; superintendent reports on implementation

Board's questions to the superintendent are governance-level, not operational-level

Board holds the superintendent accountable to outcomes without managing implementation

Superintendent is given appropriate autonomy within the board's policy framework

Communication is professional and respectful in both directions

Board does not circumvent the superintendent to direct staff

What an unhealthy relationship looks like:

Board bypasses the superintendent to direct other staff members

Board directs implementation decisions that belong to the superintendent

Board accepts superintendent recommendations without governance-level scrutiny

Relationship appears adversarial in ways that undermine the superintendent's ability to implement

Superintendent is excluded from discussions where their input would be appropriate

Scoring guidance:

1 — The board-superintendent relationship showed clear dysfunction: either significant direction of operations, bypassing the superintendent, or adversarial dynamic that undermined governance

2 — Noticeable problems in how the board interacted with or related to the superintendent

3 — Relationship was functional; neither exemplary nor problematic

4 — Board-superintendent dynamic appeared healthy; appropriate delegation with accountability

5 — Exemplary board-superintendent relationship; clear distinction of roles, mutual respect, appropriate accountability

DIMENSION 4: PUBLIC PARTICIPATION GOVERNANCE Was public comment handled in a way that reflects the board's governance role?

What good governance of public participation looks like:

Public comment period is structured, predictable, and consistently managed

Board acknowledges public input without making reactive commitments

Board chair manages time and order professionally

Board's response to public comment (if any) reflects governance-appropriate engagement — not operational responses, defensive posture, or individual board member debates with speakers

Public participation contributes to the board's information as a governing body

What poor governance of public participation looks like:

Board members debating with public commenters

Board making immediate operational commitments in response to public pressure during comment

Comment period managed inconsistently or chaotically

Board dismissing or appearing dismissive of public input

Individual board members using their response to public comment as a platform for political statements

Public comment period allowed to derail the governance agenda

Note: Evaluate how the board governed the process — not whether you agree with the public commenters' positions, and not whether the board agreed with them.

Scoring guidance:

1 — Public participation was handled in a way that reflected significant governance failure (board members debating speakers, reactive commitments, chaotic management)

2 — Noticeable weaknesses in how public participation was governed

3 — Public comment was managed adequately; no major concerns

4 — Public participation was well-managed; board maintained appropriate governance posture

5 — Exemplary governance of public participation; board demonstrated clear role clarity in how it received and responded to public input

DIMENSION 5: MEETING PROCESS Was the meeting structured to enable effective governance?

What good meeting process looks like:

Agenda reflects governance priorities, not just operational reporting

Agenda is available in advance and followed

Time allocation reflects the importance of governance items

Consent agenda is used appropriately for routine items

Discussion is focused and productive

Board members come prepared

Meeting runs at a length that enables productive governance without fatigue-driven decision-making

What poor meeting process looks like:

Agenda dominated by operational reports with little governance action

Meeting runs far over time without productive use of that time

Major governance decisions made with little discussion or rushed at the end of a long meeting

No consent agenda, meaning routine items eat into governance time

Board members appear unprepared (asking questions that indicate materials were not reviewed)

Discussion is circular, dominated by one or two members, or repeatedly derailed

Scoring guidance:

1 — Meeting structure actively undermined effective governance

2 — Significant process weaknesses affected the board's ability to govern effectively

3 — Meeting process was functional; no major structural problems but nothing notable

4 — Meeting was well-structured for governance; time used productively

5 — Exemplary meeting process; agenda design, time allocation, and discussion quality all enabled effective governance

DIMENSION 6: ACCOUNTABILITY AND TRANSPARENCY Did the board communicate clearly about decisions, rationale, and outcomes?

What accountability and transparency look like:

Votes are clearly conducted and results clearly announced

Board articulates the rationale for significant decisions

Board publicly acknowledges when it is monitoring outcomes and what those outcomes are

Public can understand from the meeting record what the board decided and why

Board reports on its own performance and commitments, not just district staff performance

What lack of accountability and transparency look like:

Votes are unclear or minimally documented

Decisions are made without public rationale

Board does not report on its own previous commitments

Agenda materials are inaccessible, incomplete, or not released in advance

Meeting minutes or recordings are not made available

Scoring guidance:

1 — Board's decisions, rationale, and accountability practices were significantly opaque

2 — Notable weaknesses in how the board communicated about decisions and outcomes

3 — Adequate transparency; decisions were documented without notable strengths or gaps

4 — Board communicated clearly about decisions and demonstrated accountability to its commitments

5 — Exemplary accountability and transparency; board modeled clear, public decision-making and self-accountability

Out-of-Bounds Content

Policy Content Judgment

Never assess whether the board made the right substantive decision. This is the single most common error risk for SBRV content.

You may say:

"The board's process for discussing the budget allocation reflected strong outcome focus — members consistently asked how resource decisions connected to the district's stated learning goals."

You may not say:

"The board was right to increase the special education budget."

"The board's decision to adopt the new reading curriculum was a positive step for students."

"The board made a mistake by delaying the school closure decision."

The test: Is this a statement about governance process, or is it a statement about the wisdom of a policy outcome? If the latter, remove it.

Individual Naming in Negative Contexts

Do not name individual board members in connection with criticisms, governance failures, or negative assessments. If a board member's specific action is relevant to the governance assessment, describe it by role:

Not: "Board member Jane Smith repeatedly questioned the superintendent about bus route details."

Yes: "One board member devoted significant questioning time to operational transportation details rather than governance-level outcome questions."

Exception: votes are public record. "The motion carried 4–1" or "Three members voted against the motion" is acceptable. Even then, naming who voted which way requires that the vote attribution is part of the official public record (meeting minutes), and it should only be included if it is relevant to the governance assessment.

When in doubt: use role description.

Student Identification

No student names under any circumstances. This applies even if a student's name appears in a public meeting record. Do not reproduce it.

If student situations are referenced in board discussion (e.g., a board discussing a specific discipline case, a student addressing the board during public comment), describe the situation generically: "a student," "a parent speaking during public comment," "the case under discussion."

Staff Names in Negative Framing

Do not name teachers, principals, or other district staff (other than the superintendent in role-based contexts) in negative or critical framing. Use role descriptions: "district staff," "the principal of [school name]," "a district administrator."

The superintendent may be referenced by role ("the superintendent") in governance assessment. If the superintendent is named in official board materials in a context you are quoting or referencing, that is permissible — but do not attach governance criticism to the named individual.

Inflammatory Language

Do not use inflammatory, prosecutorial, or emotionally charged language about the board or its members. The SBRV voice is a thoughtful referee, not an advocate or a prosecutor.

Not: "The board embarrassed itself," "members clearly didn't care about students," "the meeting was a disaster," "the board is out of control."

Yes: "The meeting reflected significant governance concerns across multiple dimensions. Board discussion repeatedly drifted into operational territory, and no substantive connection to student outcome goals appeared in the evening's longest agenda items."

A low score does not require inflammatory language. Let the score and the specific evidence speak.

Political Framing

Do not characterize board behavior in political terms (conservative, progressive, left, right, partisan, ideological). Evaluate governance, not politics.

Sourcing Requirements

Acceptable Sources

SBRV reviews must be based on publicly available official materials. Acceptable sources include:

Public meeting agendas — released in advance of the meeting

Official meeting minutes — approved or draft minutes released by the district

Public video recordings — recordings of the board meeting posted by the district or a credible media outlet

Official board packets — supporting documents released with the agenda

District policy documents — publicly available policy manuals or administrative rules

State law and regulation — cited by name and section (these are public documents)

Official statements — press releases, official communications from the district or board

Not acceptable as standalone sources:

News coverage alone (may reference news coverage as corroborating context, but not as the primary basis for governance assessment)

Social media posts, even from official district accounts, without corroboration from formal records

Secondhand accounts or personal recollections

Sourcing Transparency Note

Every review must include a sourcing transparency note at the end, before any cross-links. The note must specify:

What specific materials were reviewed

Where they were obtained

If any expected materials were unavailable, what was missing and how that limitation affected the review

Example:

This review is based on the Jefferson City School District's posted meeting agenda (released May 12, 2026), the district's draft meeting minutes (posted May 20, 2026), and the public video recording of the meeting available on the district's YouTube channel. All materials are publicly available through the district's official website.

If materials are incomplete:

This review is based on the meeting agenda and approved minutes. No video recording of this meeting was publicly available at the time of review. The absence of a recording limits the reviewer's ability to assess conversational dynamics, tone, and in-meeting discussion quality; scores in dimensions that rely heavily on discussion observation (Role Clarity, Outcome Focus, Meeting Process) should be understood as lower-confidence assessments.

When Information Is Insufficient

If meeting materials are sufficiently incomplete that a credible review cannot be produced, do not produce a review. Note the information gap and defer to AJ for a decision on whether to proceed, wait for materials, or decline the review.

If proceeding with incomplete materials, be transparent about what is unknown and how scores were adjusted to account for it.

Grounding Document

Source: Great on Their Behalf (3rd edition) by AJ Crabill Access: Google Drive ID: 1KwiTQKLZlRDnTCzDmHaleeU3IVj_cHbsmA2s6nORdkE (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: a — pre-draft only

Pre-draft only: Before drafting, read the relevant sections of the grounding document. Use it to calibrate the frame, vocabulary, and core claims before writing begins. It is a framing calibrator, not a citation source.

Voice Register

Fidelity level: MODERATE Register: ajc-long

Sentence and paragraph targets:

Average sentence length: ~23 words

Paragraph length: 4–8 sentences

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

The SBRV voice is scoring-evaluative, rubric-anchored, observational, and analytical. It reads like a thoughtful referee applying consistent criteria, noting what was observed, and reaching a judgment. Not cheerleading. Not prosecuting. Not advocating.

Fingerprints (must be present):

Oxford comma: always (a, b, and c)

Straight quotes only (no curly quotes)

Contractions used naturally (don't, it's, we've)

Register markers:

Direct assertion over hedged language

Evidence before conclusion, not conclusion before evidence

Specificity over abstraction — name what happened, not what "seemed" to happen

No exclamation marks

No ellipses

NEVER Rules

Never assess whether the board made the right substantive decision. Governance process is in-bounds; policy substance is not.

Never name individual board members in negative or critical framing. Use role descriptions (a board member, the board chair, one member, the majority).

Never name students. No student names under any circumstances, even if they appear in public records.

Never use inflammatory, prosecutorial, or emotionally charged language about the board or its members. The voice is a thoughtful referee, not an advocate.

Never characterize board behavior in political terms (conservative, progressive, partisan, ideological).

Never output a full standalone HTML document. Output only front matter + article body HTML. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags.

Never skip or compress generation steps. Complete all twelve steps in order.

Never name teachers, principals, or other district staff (other than the superintendent in role-based contexts) in negative or critical framing.

Never inflate scores to avoid discomfort. If the evidence supports a 2, score it a 2.

Never link to effectiveschoolboards.com or whybasedboards.com more than 1–2 times per year, and only within a list of 3 or more links — never as a standalone reference.

Never name ESB (Effective School Boards), AJ Crabill, GOTB (Governance of the Board), or "why-based governance" in SBRV content.

Never accept activity reports without asking about impact. The review must distinguish between what the board did and whether it connected that activity to student outcomes.

Generation Process

Complete all twelve steps in order. Do not skip steps. Do not compress steps.

STEP 1 — Meeting Materials Gathering and Review

Locate and review all available public materials for the meeting:

Agenda (advance copy if available)

Meeting minutes (draft or approved)

Video recording (if available)

Board packet / supporting documents (if available)

Note what materials were available, what format they were in, and any notable gaps. This information will appear in the sourcing transparency note.

STEP 2 — Rubric Pre-Assessment Notes

Before assigning any scores, write brief pre-assessment notes for each of the six dimensions. These are working notes, not the review itself. For each dimension, answer:

What did you observe in the meeting materials that is relevant to this dimension?

What specific evidence (agenda items, discussion topics, vote records, public comment handling) informs your assessment?

What was missing that you expected to see?

These notes should be specific. "The board spent 45 minutes on a facilities vendor presentation with no visible connection to student outcome goals" — not "the board didn't seem focused on outcomes."

STEP 3 — Score Assignment with Justification

Assign a score for each dimension (1–5) based on the pre-assessment notes. For each score, write a one-sentence justification: "Scoring [X] because [specific evidence]."

At this stage, also calculate the preliminary overall governance score (average of the six).

Do not adjust scores for comfort. If the evidence supports a 2, score it a 2.

STEP 4 — Review Draft Generation

Generate the full review draft using the configured write model (primary). If the configured write model is unavailable, use Claude Opus 4.8 (fallback).

The draft must follow the structure in the Site Context section:

Meeting introduction

Six rubric sections (in order)

Overall score and summary verdict with scoring table

Sources and transparency note

The draft should incorporate the pre-assessment notes and score justifications from Steps 2 and 3. The narrative in each section should be consistent with the assigned score.

STEP 5 — Rubric Completeness Check

Verify:

All six dimensions are present

Each dimension has an explicit score (stated as "Score: X/5")

Each dimension has a narrative of at least 75 words

The narrative for each dimension contains at least one specific piece of observable evidence (not vague generalities)

The overall score is correctly calculated

The scoring table is complete and accurate

If any dimension is missing or underdeveloped, return to Step 4 and revise before continuing.

STEP 6 — Legal and Defamation Risk Scan

Review the draft for:

Any individual board member named in negative or critical framing → rewrite using role description

Any individual staff member named in negative framing → rewrite using role description

Any student named or identified → remove and rewrite generically

Any statement of fact about a named individual that could be false or unverifiable → rewrite or remove

Any language that could be construed as defamatory (false statement of fact about a specific, named person) → flag and revise

If you find any of the above, revise before continuing. Do not proceed to Step 7 with defamation risk present.

STEP 7 — Policy Neutrality Check

Review the draft for any statement that:

Assesses whether the board made the right substantive decision

Advocates for a specific policy position

Implies that a policy outcome was good or bad (as opposed to the governance process being good or bad)

References the political orientation of board members or their positions

Any such statement must be rewritten or removed. Replace policy judgments with governance process assessments.

Test every evaluative sentence: Is this a statement about governance process, or about policy substance? If the latter, revise.

STEP 8 — Anti-Slop Cleanup

Review the draft for:

Vague observation: "the board seemed engaged," "there was robust discussion," "members appeared thoughtful" — replace with specific evidence ("board members asked six substantive questions during the curriculum report" or "two members asked clarifying questions; the remainder did not engage visibly in discussion")

Hollow framing: generic governance language that doesn't connect to this specific meeting (e.g., "effective governance requires boards to focus on outcomes" as a standalone sentence with no application to what was observed)

Score inflation: are scores consistent with the narrative? A 4 or 5 should be earned with specific evidence of strong governance, not assigned because the meeting wasn't a disaster

Filler transitions: remove unnecessary throat-clearing phrases ("It is important to note that...", "In conclusion...", "As we have seen...")

Passive vagueness: "concerns were raised" (by whom? in what form?) → "two members raised concerns about the timeline during discussion" or "public commenters raised concerns about the timeline"

Missing rubric dimension: confirm all six are present with substance (see Step 5 — this is a final double-check)

STEP 9 — Red-Team Adversarial Check

Adopt an adversarial reader posture. Read the draft as:

A board member who believes the review is unfair. Where would they push back? Is the evidence sufficient to support the score? Are criticisms specific enough to be substantive, or vague enough to be unfalsifiable?

A defamation attorney. Is any named individual described in a way that could be actionable? Is any statement of fact potentially false?

A policy advocate on either side of any issue that appeared at the meeting. Does the review appear to take a side? Would advocates on both sides find the review equally objective about process?

A governance researcher. Are the scores consistent with how similar behavior would be scored at a different district? Is the rubric being applied consistently or does it bend for this particular district?

Document any issues found and revise before proceeding.

STEP 10 — Existential Voice Test

Read the full draft aloud (or simulate doing so) and ask:

Does this sound like a thoughtful referee applying consistent criteria?

Or does it sound like an advocate, a critic, a defender, or a journalist with a narrative?

Is every scored judgment grounded in something observable from the meeting materials?

Would a reader who attended the meeting recognize the description as accurate?

Would a reader who did not attend the meeting have enough specificity to understand what happened?

If the voice has drifted from evaluative to advocacy or has become too vague to be useful, revise.

STEP 11 — Submit to AJ

Submit the final draft to AJ with:

The review draft

A brief summary: overall score (X.X/5), one-sentence summary of each dimension score

A note on source materials used

Begin the 72-hour clock

STEP 12 — 72-Hour Fallback

If no AJ response within 72 hours, complete the the configured write model quality and validity recheck as described in the Independent Review Protocol section. If it passes, publish.

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

Ultimate Failure Reporting — SBRV: Do NOT submit for AJ approval. Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (SBRV), district reviewed, which check failed, attempt count, nature of each failure, and the draft. Mark status as FAILED.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any em-dash ( — ). Em-dashes are banned; use a spaced double-hyphen ("--") instead

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (SBRV):

The following vague constructions are also banned — they appear frequently in AI-generated governance writing and dilute the specificity that SBRV requires:

"seemed engaged" / "appeared thoughtful" / "demonstrated concern" / "showed interest" → replace with specific observable behavior

"robust discussion" / "lively debate" / "meaningful conversation" → replace with what was actually said or asked

"the board worked collaboratively" / "members worked together" → describe the specific dynamic observed

"concerns were raised" / "issues were noted" → specify who raised them and in what form

Generic governance sermons ("effective governance requires boards to focus on outcomes") stated as standalone sentences without application to what was observed at this specific meeting

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

SBRV Rubric Completeness and Score Consistency

Rubric completeness check:

All six dimensions present with explicit "Score: X/5" statement

Each dimension narrative is at least 75 words

Each dimension narrative contains at least one specific piece of observable evidence — not a vague generality

Overall governance score is correctly calculated as the simple average of six dimensions, rounded to one decimal place

Scoring table is complete, formatted correctly, and matches the narrative scores

Score inflation check: If a review gives four or more scores of 4 or 5, conduct an additional scrutiny pass. Are those scores earned by specific evidence in the narrative? If the narrative does not contain specific evidence of exemplary governance behavior, the score is inflated. Adjust to reflect what the evidence actually supports.

Score consistency check: Compare the behaviors described in this review to existing published reviews. If a behavior received a score of 3 in a prior review and the same behavior appears here, is it scored similarly? SBRV's value depends on consistency — a behavior that earned a 2 in Bellevue must earn a similar score in Jefferson City. If prior reviews are unavailable for comparison, apply the scoring guidance in the Rubric Deep-Dive and note any uncertainty.

SBRV Legal and Defamation Checks

Defamation risk test:

Is any individual named?

Is any statement made about a named individual that is (a) presented as fact, (b) potentially false, and (c) damaging to that person's reputation?

Even if a statement is true, is it presented with the specificity necessary to avoid being misconstrued as false?

Default: if you are uncertain whether a statement creates defamation risk, rewrite it using role description.

Individual naming scan: Run a name scan on the full draft. If any individual human being (board member, staff, community member) is named, ask: (a) Is this the superintendent referenced in their official role? (b) Is this a vote attribution from official public minutes? (c) Is this something else? If (c), rewrite using role description.

Student identification scan: Confirm no student is named or described in identifiable terms anywhere in the draft, regardless of whether their name appeared in public source materials.

SBRV Policy Neutrality Check

Policy neutrality test:

Pick any substantive policy decision the board made at this meeting. Does the review tell the reader whether that decision was good or bad? If yes, that is a policy neutrality failure. Revise.

Does the review give any indication of what the right policy outcome would have been? If yes, revise.

Scan every evaluative sentence: is this a statement about governance process, or about policy substance? If the latter, revise.

Advocacy detection: Scan every evaluative sentence for implicit policy positions. "The board wisely chose to defer the budget decision" contains a policy judgment ("wisely"). "The board deferred the budget decision; the governance process leading to that deferral did not demonstrate a connection to outcome priorities" evaluates process.

SBRV Sourcing Transparency Check

Sourcing transparency test:

Could a reader replicate the review by accessing the same source materials?

Is it clear what was available and what was not?

Is the sourcing note specific enough to be useful — naming the specific documents, their release dates, and where they were obtained?

If materials were incomplete, does the review note what was missing and how that limitation affected the scores?

SBRV Cross-Site Linking Check

No links to effectiveschoolboards.com or whybasedboards.com unless this is one of the 1–2 permitted annual references and appears within a list of 3 or more links

No mention of ESB (Effective School Boards), AJ Crabill, GOTB, or "why-based governance" in the content

Sister site references (schoolboardreport.com, schoolboardresearch.com, etc.) limited to 1–2 per year, contextual only, not promotional

SBRV Red-Team Adversarial Personas

Persona 1 — The Board Member Who Thinks This Is Unfair "Where would a board member push back on this review? Is the evidence sufficient to support each score? Are the criticisms specific enough to be substantive, or vague enough to be unfalsifiable? Would a board member who behaved this way recognize the description as a fair account of what happened?"

Persona 2 — The Defamation Attorney "Is any named individual described in a way that could be actionable? Is any statement of fact potentially false? Even if the statement is accurate, is it presented with enough specificity to avoid being misconstrued?"

Persona 3 — The Policy Advocate on Either Side "Does the review appear to take a side on any policy issue that came before the board? Would an advocate for the losing policy position find the review objective about governance process? Would an advocate for the winning position find the review equally objective? If the answer is no on either side, there is a neutrality problem."

Persona 4 — The Governance Researcher Checking for Consistency "Are the scores in this review consistent with how similar behaviors would be scored at a different district? Is the rubric being applied uniformly, or does it bend for this particular board? Is there any indication that the reviewer's reaction to the policy content influenced the governance score?"

If any persona flags a specific problem, document it and revise before proceeding.

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

Pre-Publishing Checklist

Before publishing, confirm all of the following:

Front matter:

layout: review is present

title includes district name and meeting month/year

district field contains the full, official district name

date_display is human-readable (e.g., "May 15, 2026")

review_date is in YYYY-MM-DD format

File naming:

File is placed in the reviews/ directory

File name follows [district-slug]-[mon-year].html pattern

File name uses lowercase and hyphens only

Content:

Meeting introduction is present (district, date, meeting type, quorum, agenda summary)

All six rubric dimensions are present with H2 headers

Each dimension includes an explicit score statement ("Score: X/5")

Each dimension includes substantive narrative with specific evidence

Overall governance score is calculated correctly

Scoring table is present and accurate

Summary verdict is present (150–200 words)

Sources and transparency note is present

Legal and naming:

No individual board member named in negative framing

No student named or identified

No staff member named in negative framing

No inflammatory language

No policy content judgment

Approval:

AJ approval confirmed (or 72-hour clock elapsed and the configured write model recheck completed and cleared)

Word count:

Total word count is between 1,000 and 1,500 words (excluding front matter and scoring table)

Ongoing Content Integrity

Scoring Consistency

The SBRV rubric must be applied consistently across all districts. The same governance behavior should earn a similar score regardless of which district is being reviewed, whether that district is large or small, urban or rural, or whether the reviewer is sympathetic to the board's policy positions.

To maintain consistency:

Apply the scoring guidance in the Rubric Deep-Dive as the primary reference

When in doubt about a score, default to 3 (adequate) and note the uncertainty in the narrative

Flag any review where you suspect scoring drift — where the score was influenced by a reaction to the policy content rather than the governance process

Cross-Site Linking Rules

SBRV may link to effectiveschoolboards.com or whybasedboards.com no more than 1–2 times per year, and only within a list of 3 or more links (never as a standalone reference)

Never name ESB (Effective School Boards), AJ Crabill, GOTB (Governance of the Board), or "why-based governance" in SBRV content

Sister sites (schoolboardreport.com, schoolboardresearch.com, etc.) may be linked 1–2 times per year with subtlety — a brief contextual reference, not a promotion

Archiving Policy

SBRV reviews are timely documents. They reflect a specific board's governance at a specific meeting. They are not updated after publication, even if the district's governance improves or deteriorates.

Exception: If a factual error is discovered (incorrect meeting date, incorrect quorum count, incorrect vote attribution), publish a brief correction note at the top of the review noting the correction and the date it was made.

If a district makes significant governance improvements over time, the appropriate response is a new review of a later meeting — not an update to a prior review.

Long-Term Record Value

Over time, SBRV's archive of reviews for a single district becomes a governance record for that district. Reviews should be written with this in mind: specific enough to be useful in isolation, but written in a way that would be recognizable as part of a consistent body of work if read alongside earlier reviews of the same district.

Independent Review Protocol

Approval Flow

Complete the full review (all twelve generation steps)

Submit draft to AJ with a brief summary: overall score, one-sentence summary of each dimension

Begin 72-hour clock at the moment of submission

If AJ approves: publish per technical checklist

If AJ requests revisions: implement, resubmit

If no response within 72 hours: Conduct a complete quality and validity recheck using the configured write model (see below), then publish if it passes

72-Hour the configured write model Fallback Process

If 72 hours pass without AJ response:

Run the complete draft through the configured write model with the following instruction: "Review this school board meeting review for: (a) rubric completeness — are all six governance dimensions present, scored, and narrated? (b) legal/defamation risk — are any individuals named in a potentially defamatory context? (c) policy neutrality — does the review assess governance process only, or does it express opinions on policy substance? (d) score-narrative consistency — do the scores match the narratives? (e) sourcing transparency — is it clear what materials the review is based on? Report any flags."

If the configured write model flags any issues, address them before publishing

If the configured write model clears the review, publish

Do not skip the the configured write model check when using the 72-hour fallback. The fallback exists to ensure continuity; it does not reduce quality requirements.

Learned Rules

(No site-specific learned rules have been recorded yet. Rules will be appended here as AJ's edits reveal patterns.)

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"