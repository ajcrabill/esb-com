title: School Board Weekly — Content Generation Guide type: content-guide site: schoolboardweekly.com updated: 2026-07-08

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

Purpose: School Board Weekly is a curated, editorial-voice briefing on what matters in school board governance each week. It is not a news roundup or aggregator. The defining question for every issue: What happened in school board governance this week, and why does it matter for how boards govern?

The Lead must take an editorial stance. Three Things must give real answers. Featured District must be concrete and instructive. Research Note must be grounded in real, citable research. Every section earns its place by being useful to a board member sitting down Monday morning.

Domain: schoolboardweekly.com Content type: Weekly newsletter issues (HTML pages, subscribe-by-email delivery) Publication frequency: Every Monday morning Jekyll layout: issue Front matter fields: layout, title, issue_number, date_display File naming: issues/issue-[NNN].html (zero-padded to three digits; current series continues from issue-008; next issue is issue-009, then issue-010, etc.)

The Four-Section Format

School Board Weekly publishes exactly four sections per issue, every time. No exceptions. The sections, their anchors, and their word count targets are fixed:

Total target: approximately 1,300 words. Word counts are guidelines, not hard caps — a section should not be padded to hit its number, and a genuinely compelling Lead is not truncated just because it runs 430 words. But significant deviations (50+ words over or under) should be flagged.

Target Audience

School board members and governance watchers who subscribe to receive a weekly briefing. They are practitioners and close observers — not education-policy generalists. They want to stay current on governance issues without drowning in the full volume of education news. They trust the editorial voice to have filtered for what matters in governance specifically.

They are not looking for curriculum news, operational district news, or superintendent performance coverage. They are looking for board work — how boards are governing, where governance is working, where it's breaking down, and what they can learn from it.

Voice

AJ Crabill's editorial voice. This is the only site in the network where the voice is personal and opinionated.

What this means in practice:

AJ is a practitioner and expert in school board governance — he has a point of view and expresses it

The Lead is not a neutral description of events; it is an informed, substantive take on what the events mean for governance

It is appropriate to say "this matters," "this is a problem," "boards that do X tend to see Y," and "the governance question here is..."

The voice is direct and confident — not hedging, not both-sidesing every claim, not retreating into academic distance

The voice is occasionally wry but never snarky; warm but never folksy; expert but never condescending

Every section should feel like it was written by a specific person who has spent years in this work and has opinions about it

Think: a trusted governance expert writing a Monday morning newsletter to a community of practice — not a journalist maintaining strict objectivity, and not an academic writing for peer review

Voice failure modes to flag:

Institutional/journalistic drift: language that sounds like an NSBA staff publication rather than AJ's voice

Hedge-piling: "it's complicated," "there are many perspectives," "reasonable people disagree" without actually taking a position

Generic expertise: the kind of thing anyone could write after reading the same article, without the practitioner lens

What Makes SBW Distinct from Sister Sites

The closest sister site is schoolboardreport.com (SBR), which is institutional and analytical with a staff byline. The distinction:

SBR analyzes patterns in depth, usually with a research or data anchor, institutional voice, longer format

SBW is AJ's editorial voice, opinionated, weekly, four-section format designed to be read in 10 minutes

SBW scans current governance news and finds the governance angle; SBR goes deep on patterns over time

SBW is a newsletter first — designed for email delivery and quick Monday morning reading

SBW is the only site in the network with a persistent editorial persona (AJ's)

A story that SBR would handle with a 2,000-word analytical piece might appear in SBW's Lead as a 400-word editorial take on the governance implications. They complement each other — they do not duplicate.

What a Successful Issue Looks Like

A subscriber reads the issue Monday morning and finishes it feeling:

Informed — they know what matters in governance right now, not just what happened

Equipped — they have at least one good question to bring to their next board meeting, or one concept to watch for

Trusted — the editorial voice filtered well; they didn't wade through noise to find the signal

Grounded — the Research Note gave them something real and citable to stand behind in a conversation

The test: would a board member finishing this issue on Monday morning feel like they got the governance briefing they were looking for? If yes, the issue works.

What a Failed Issue Looks Like

News summary without editorial frame: describes what happened, never says why it matters for governance

Management coverage instead of governance coverage: covers curriculum decisions, scheduling, hiring, or other operational matters instead of board work

Angle repetition: covers the same governance angle as an issue published in the past six months

Toothless Three Things: Q&A where the answers hedge rather than answer, or the questions are too vague to be useful to a specific board member

Generic Featured District: composite scenario that is so vague it could describe any district facing any challenge; no specificity, no instructive detail

Fabricated Research Note: cites a study or report that does not exist, or misrepresents what a real source actually says

Voice drift: sounds like an institutional publication, not AJ's editorial voice

Content Format and Structure

Front Matter: Every issue file must open with this front matter block:

---

layout: issue

title: "[Issue headline — substantive, specific, not generic]"

issue_number: [NNN]

date_display: "Month DD, YYYY"

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

layout is always issue

title should be the headline of The Lead — specific and substantive, not generic ("Boards and Budgets" is bad; "When Budget Cuts Reach Governance: How Boards Lose Their Policy Role" is good)

issue_number is a zero-padded integer matching the filename (issue-009 → 009)

date_display is the Monday publication date in long format ("June 23, 2026")

File Naming Convention: issues/issue-[NNN].html where NNN is zero-padded to three digits.

issue-009.html, issue-010.html, issue-011.html, etc.

Never omit leading zeros

Series continues from issue-008; issue-009 is next

Section Anchors: The four sections must use these exact anchor IDs. index.html links to them directly:

#lead — The Lead section

#three-things — Three Things section

#district — Featured District section

#research — Research Note section

Each section header element must carry the corresponding ID attribute. Example:

<h2 id="lead">The Lead</h2>

The Lead (~400 words)

Purpose: The main governance story of the week. Deep-ish analysis, editorial voice, the "why this matters for how boards govern" angle.

Requirements:

Must connect to something happening currently in school board governance — a recent news story, a pattern that has emerged, a decision that set a precedent, a conflict that surfaced a governance question

Must take an editorial stance — not "here is what happened" but "here is what this means for how boards govern"

Must have an explicit governance angle — the story is chosen because of what it reveals about how boards work (or fail to work), not because it's a big education story generally

Must ask the ESB-aligned question: what does this governance pattern mean for student outcomes? The answer should be present in the editorial analysis, not just implied

Opens with a hook — a specific observation, a surprising fact, a concrete scenario — not a generic throat-clearing sentence

Closes with a clear takeaway: what should a board member reading this do differently, watch for, or think about?

Structure (flexible, not rigid):

Hook — specific, concrete, grabs the practitioner's attention

Context — what's happening and where

The governance angle — why this is a board governance question, not just a news story

Analysis — what it means, why it matters, what the pattern reveals

Takeaway — what a board member should do, think, or watch for

Tone: Confident, direct, expert. The Lead is where AJ's editorial voice is most present. It may disagree with conventional wisdom. It may say something is a problem. It may name a governance failure pattern. It should never feel like it was written to offend no one.

What The Lead is NOT:

A news summary without editorial interpretation

A coverage of management or operational decisions (curriculum, hiring, scheduling)

A story about superintendent performance (unless the governance question is specifically about board oversight)

A repeat of a governance angle covered in the past six months

Three Things (~300 words total)

Purpose: Three specific governance questions — formatted as Q&A. Real questions a board member might ask this week. Direct answers.

Format:

Exactly three Q&A pairs

Each Q&A: one question, one answer (roughly 75-100 words per pair)

Questions are formatted in bold or as question headers

Answers are direct — no hedging, no "it depends" without immediately answering what it depends on

Question requirements:

Each question must be something a real board member might genuinely ask this week — grounded in the week's governance context

Questions should feel practical, not academic: "What does our board do when..." or "How should we handle..." or "Is it governance or management when..."

Not all three need to connect to The Lead topic, but at least one should; the others may address other current governance questions

Answer requirements:

Answer the question directly, in the first sentence if possible

Provide enough context that the answer is useful, not just technically correct

ESB-aligned where relevant: anchor answers to board purpose (student outcomes) and the five practices (Focus, Clarify, Monitor, Align, Communicate)

If the answer is "it depends," say what it depends on and then answer both cases

Never end an answer without having actually answered the question

Tone: Practical, direct, collegial. Like a trusted governance expert answering a colleague's question at a coffee meeting — no jargon without explanation, no dodge, no lecture.

Failure modes:

Question is too vague to be practically useful

Answer hedges without actually answering

Three questions all cover the same theme (variety is expected)

Questions feel fabricated rather than drawn from the week's governance context

Featured District (~350 words)

Purpose: A fictional/composite district case that describes how one district navigated a governance challenge. Concrete, specific, instructive.

The composite district rule:

NEVER use a real district name in this section

Use a fictional composite name — "Ridgeline School District," "Clearwater Unified," "Prairie Lakes School District," or similar names that sound plausible but are clearly not associated with a specific real place

The scenario may be inspired by real patterns or cases, but the specific district, board, and characters must be fictional

Composite means drawing from multiple real situations to create a representative scenario — not inventing a scenario with no grounding in reality

What makes a good Featured District scenario:

A specific governance challenge — not "the board had communication problems" but "the board chair was fielding media calls independently and making policy statements without board authorization"

Concrete context — the board had X members, the superintendent had been in place for Y months, the issue arose when Z happened

A real tension or conflict — not a smooth success story but a situation that required genuine governance work

A resolution that is instructive — what the board actually did, why it worked (or why it was a partial success), what the governance lesson is

A clear takeaway — what another board facing this challenge could draw from this scenario

What makes a bad Featured District scenario:

Vague enough to describe any district anywhere ("The board was struggling with trust issues...")

Unrealistically smooth resolution (real governance challenges have friction)

No identifiable governance lesson

Scenario that is actually about management, not governance

Real district thinly veiled with a changed name

Tone: Case study style, but readable — not academic. Describes the situation, the challenge, the process, and the outcome. Third person. Past tense unless describing a lesson that is ongoing.

Research Note (~250 words)

Purpose: A brief synthesis of one relevant piece of research or data, connected to the week's governance theme.

Citation requirements (non-negotiable):

Every Research Note must cite a real, verifiable source

Citation format: Author Last Name, First Initial. (Year). Title. Publication/Organization.

Example: Grissom, J. A., & Blissett, R. S. L. (2017). Superintendent evaluation and the role of school boards. Educational Administration Quarterly.

If the source is an organizational report (not a journal article): Organization Name. (Year). Report Title.

Example: RAND Corporation. (2021). District Governance and Student Achievement: What the Evidence Shows.

If the source is paywalled: cite it fully and note "(paywalled — abstract available at [URL])" if the abstract URL is publicly accessible

If the source has no single author but a named organization: use the organization as author

What counts as a citable source:

Peer-reviewed journal articles

Published research reports from recognized education research organizations (RAND, Brookings, CCSSO, NSBA, state education agencies, university research centers)

Published books with identifiable authors and publication information

Government data reports (NCES, state education agencies)

NOT citable: blog posts without research basis, anonymous web content, AI-generated summaries of research, paraphrases of paraphrases

Fabrication rule: If a study or report cannot be verified as real and accurately described, do not cite it. A Research Note with no citation is better than a Research Note with a fabricated citation. Flag for human review rather than fabricate.

Structure:

One-sentence description of what the research is and why it's relevant to this week's governance theme

Two to three key findings from the research, described accurately

One-sentence connection to the governance implication for boards

Tone: Clear and accessible — translate research language into practitioner language. No jargon without explanation. But don't oversimplify findings or strip important caveats.

In-Bounds Content

SBW covers school board governance — the work of the board as a governing body. The test: is this about what the board, as a collective governing body, decides, oversees, or communicates?

In-bounds topics:

Board governance patterns and structural questions (how boards make decisions, set policy, exercise oversight)

Board-superintendent relationship dynamics (including when boards overstep into management or fail to provide sufficient oversight)

Board accountability mechanisms — to whom are boards accountable, and how is that accountability exercised?

Governance structure questions: term limits, board size, election vs. appointment, open meetings compliance

How specific board behaviors connect to student outcome patterns

Governance implications of policy debates — not the policy content itself but the governance process by which boards engage, decide, and communicate about policy

Board communication with the public, community, and internal stakeholders — when boards communicate well or poorly

Executive session practices, conflict of interest disclosures, ethics questions at the board level

Board professional development and governance capacity

Superintendent searches and transitions as governance processes

How boards use data (or fail to) in governance decisions

Governance failures: when boards destabilize districts, micromanage, fragment, or lose sight of purpose

Legislative and legal changes that affect how boards govern (not the policy content, the governance process effect)

The Governance Angle vs. The News Description

This is the most critical distinction in topic selection. Many education news stories have a governance angle buried in them. The job is to find and foreground that angle.

Example of news description (NOT what SBW does): "A school district in Texas approved a new reading curriculum over community objections."

Example of governance angle (what SBW does): "When community objections reach the board chamber, how boards manage public comment, respond to organized advocacy, and still govern by evidence rather than noise is a live governance test. A Texas board's curriculum vote this week surfaces the question: what does good governance look like when the community is divided?"

The difference: the news description covers what happened. The governance angle asks what the board's role is, how it should function, and what the implications are for board governance more broadly.

Out-of-Bounds Content

The following content does not belong in SBW under any circumstances. If a topic falls in this category, do not generate a draft around it — select a different topic.

Management and Operational Topics: Board governance is NOT:

Curriculum design, content selection, or instructional approach (unless the governance question is how boards set policy vs. make operational decisions about curriculum)

Teacher or principal hiring decisions

Budget line-item decisions that are administrative rather than policy

Scheduling, facilities operations, or district logistics

Student discipline policies at the operational level

Food service, transportation, or other operational functions

The test: Is this a decision the board makes as a governing body (setting policy, approving budgets at the policy level, hiring/evaluating the superintendent)? Or is this a decision made by the superintendent and staff? If it's the latter, it's management — out of bounds.

Superintendent Performance as a Subject: Superintendent performance is out of bounds as a subject — unless the governance question is specifically about how the board oversees the superintendent. The distinction:

"Superintendent X made poor decisions about Y" — out of bounds (management topic, personnel)

"How boards conduct superintendent evaluation and what good oversight looks like" — in bounds (governance topic)

Topics Covered in the Last 6 Months: If the same governance angle was covered in a SBW Lead within the past six months, it is out of bounds for this issue's Lead. (Three Things and Research Note may touch adjacent topics, but the Lead must be fresh.)

AI Governance of AI Systems: "AI governance" in the sense of governing AI systems — policies for how AI is used, AI ethics frameworks, AI regulations — belongs to the GovernanceTodayForum (GTF) property, not SBW.

SBW may cover AI-adjacent topics only when the question is specifically about how AI or technology tools are changing how boards govern — e.g., how boards evaluate AI-generated reports, whether AI tools affect how boards conduct oversight, how AI in the classroom changes the board's policy role. The test: is this about the board's governance function, or is it about AI itself?

Neutral Summary Without Editorial Frame: A neutrally written summary of education news, without editorial interpretation or governance angle, is not an SBW issue. Every Lead must take a stance. Every Three Things must give direct answers. Coverage without analysis is a failed issue.

Citation and Sourcing (Research Note)

Peer-reviewed research:

Journal articles in education administration, educational policy, school leadership, or adjacent fields

Published and peer-reviewed books

Dissertations (use with caution — cite organization and note it's a dissertation)

Organizational research reports:

RAND Corporation, Brookings Institution, Thomas B. Fordham Institute, CCSSO, NSBA, state education agencies

University research centers (University of Wisconsin, Vanderbilt, Stanford, etc.)

NCES data reports and statistical publications

What does NOT qualify:

Blog posts without research basis

Anonymous web content

AI-generated summaries of research

Press releases describing research (cite the underlying research, not the press release)

Paraphrases of paraphrases where original source cannot be verified

Citation Format:

Author-based sources:

Last, F. I. (Year). Title of work. Journal Name or Publisher.

Organization-based sources:

Organization Name. (Year). Title of report.

For paywalled sources:

Last, F. I. (Year). Title of work. Journal Name. [Paywalled — abstract available at URL]

The No-Fabrication Rule: If a research source cannot be verified as real and accurately described, do not cite it. This is absolute. If the generation process cannot identify a real, verifiable source for the Research Note:

Flag the issue for human review

Do not substitute a fabricated citation

Do not proceed to publish without a verified citation

A note that says "Research Note: Source verification pending — [description of research needed]" is acceptable as a draft flag

Accuracy of Research Description: Citations must describe what the research actually found — not a paraphrase that overstates, reverses, or strips important caveats from findings. If a study found a correlation, the Research Note says correlation. If a study found a result in a limited context, the Research Note says so.

Connecting Research to the Week's Theme: The Research Note is not a random interesting study — it should connect to the governance theme of the issue. The connection should be made explicit in the opening sentence. If the research does not connect to any of the week's governance themes, select different research or select different themes.

Cross-Site Linking Rules

Sister sites (schoolboardreport.com, effectiveschoolboards.com, whybasedboards.com, GovernanceTodayForum, etc.) may be linked from SBW only under these conditions:

Links to effectiveschoolboards.com or whybasedboards.com: maximum 1–2 times per year, and only when appearing in a list of 3 or more links

Links to other sister sites: same rule

Never link to a sister site as the only link in a section, or as the primary recommendation

Never name ESB, AJ Crabill, GOTB, or "why-based governance" by name in an issue (the editorial stance is ESB-aligned, but the site does not advertise the affiliation explicitly)

Grounding Document

Source: Great on Their Behalf (3rd edition) by AJ Crabill Access: Google Drive ID: 1KwiTQKLZlRDnTCzDmHaleeU3IVj_cHbsmA2s6nORdkE (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: a — pre-draft only

Pre-draft only: Before drafting, read the relevant sections of the grounding document. Use it to calibrate the frame, vocabulary, and core claims before writing begins. It is a framing calibrator, not a citation source.

Voice Register

Fidelity: MODERATE Register: ajc-short

Average sentence length: ~14 words

Paragraph length: 2–4 sentences

Author blend: Sinek 30% / Gawande 30% / Collins 20% / Gladwell 20%

Author blend in practice:

Sinek (30%): Starts from why — frames everything in terms of purpose, meaning, and reason before moving to what or how. The editorial voice leads with the governance reason, not the news hook.

Gawande (30%): Concrete, practitioner-grounded, specific. Draws on real situations (even when composite). Trusts the reader to follow complexity without oversimplifying.

Collins (20%): Disciplined, rigorous, willing to make hard claims about what separates effective from ineffective. The editorial voice does not hedge on what good governance looks like.

Gladwell (20%): Counterintuitive, reframing. Surfaces the governance question the reader hadn't thought to ask. Finds the angle that is not the obvious one.

Structural invariants:

Oxford comma: always

Straight quotes only (no curly quotes)

Contractions used naturally (don't, it's, we've)

No sentence-initial transitions: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately

No exclamation marks anywhere in the piece

No ellipses

No voice hedging: no "I feel/think/believe" as epistemic hedges

NEVER Rules

Never output a full standalone HTML document — the file contains ONLY front matter + body HTML (no <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags)

Never use a real district name in the Featured District section

Never mention individual student names anywhere in an issue

Never mention individual board member, superintendent, or staff names outside of direct quotes from published sources

Never fabricate a research citation — if a source cannot be verified as real and accurately described, flag for human review and do not proceed

Never cover the same governance angle in the Lead that was covered in the past six months

Never write a Lead that is a neutral news summary without editorial interpretation

Never write a Three Things answer that hedges without actually answering the question

Never cover management or operational matters as the primary subject (curriculum selection, teacher hiring, scheduling, facilities, etc.)

Never cover superintendent performance as a subject unless the governance question is specifically about board oversight

Never link to a sister site as the only link in a section or as the primary recommendation

Never name ESB, AJ Crabill, GOTB, or "why-based governance" by name in an issue

Never use Tier 1 anti-slop words (see Section 8a)

Never open a paragraph with a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Never use em-dashes; where an em-dash would go, use a spaced double-hyphen ("--"), sparingly, or split the sentence (unicode em-dashes — are forbidden)

Never write "this week" without specifying what week — use "in June 2026" or "following the [event] in spring 2026"

Never refer to "recent" events without specifying when they occurred

Never generate AI governance content (governing AI systems, AI ethics frameworks, AI regulations) — this belongs to GovernanceTodayForum

Generation Process

The following steps must be completed in order. No step may be skipped.

Step 1 — Pre-Draft: Read Grounding Document

Before any other work, read the relevant sections of Great on Their Behalf (3rd edition) via Google Drive ID: 1KwiTQKLZlRDnTCzDmHaleeU3IVj_cHbsmA2s6nORdkE using mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content.

Focus on sections relevant to the week's potential governance themes. Use the grounding document to calibrate: ESB frame, vocabulary, five practices (Focus, Clarify, Monitor, Align, Communicate), and core claims about what effective governance looks like. This is a framing calibrator — it does not get cited in the issue.

Deliverable: a one-paragraph note on which grounding concepts are most relevant to this week's content.

Step 2 — Weekly Media Scan

Scan governance-focused media sources. Sources to monitor:

News outlets and publications:

Education Week (governance coverage specifically)

The 74 Million

Chalkbeat (multi-city)

State-level education news outlets (EdSource CA, Chalkbeat CO/IN/NY/TN, etc.)

Local newspaper education beats (for board governance stories that have national pattern relevance)

Governance-specific publications:

NSBA publications (American School Board Journal, governance resources)

State school board association newsletters and publications

CCSSO governance resources

AASA (where governance intersects with superintendent-board relations)

Research and analysis:

Brookings Institution education governance content

RAND Corporation education governance content

Fordham Institute

University research center publications (Vanderbilt Peabody, Stanford CEPA, Wisconsin WCER, etc.)

Substacks, blogs, and commentary:

Education governance-focused Substacks

Governance commentators with practitioner expertise

Podcasts:

Education governance-focused podcasts (where transcripts or summaries are available)

What to look for in the scan:

Stories about what boards are doing or failing to do

Patterns across multiple districts that reveal something about how boards govern

Legal or legislative changes that affect board governance processes

Research published that is relevant to board governance effectiveness

Conflicts or controversies that surface governance questions

Examples of governance done well (not just failures)

What to skip in the scan:

Curriculum stories without a board governance angle

Superintendent performance stories without a governance angle

Student outcome stories without a board governance connection

Politics in education coverage that is about the political content rather than the governance process

Deliverable: list of candidate stories with one-sentence governance angle for each.

Step 3 — 6-Month Recency Check

Review the past six months of SBW issues (approximately 26 issues). For each recent issue, record: Lead topic + specific angle.

Cross-reference with the candidate stories from Step 2. Eliminate candidates where the angle duplicates a recent issue. Flag candidates where the angle is adjacent but potentially fresh.

Two issues may address the same general topic if the angle is materially different. But covering "board-superintendent relations" twice in six months requires that the two angles are genuinely distinct — not the same analysis attached to a different news hook.

Deliverable: confirmed list of candidate stories with recency notes.

Step 4 — Topic and Angle Selection for The Lead

Select the strongest Lead topic from the confirmed candidate list. The selection criteria:

Current and timely (connected to something happening now)

Has a clear governance angle (not just a news hook)

Has not been covered at this angle in the past six months

Lends itself to an editorial stance AJ would stake out

Connects to ESB-aligned governance principles

Document the selection with: topic, angle, why now, what stance The Lead will take.

Step 5 — Three Things Questions Identification

Identify three specific governance questions that board members are likely asking this week. At least one should connect to The Lead topic. The other two may address other current governance questions from the media scan.

Test each question: would a real board member ask this at a governance training, in a peer conversation, or at a board meeting this week? If not, revise.

Step 6 — Featured District Scenario Development

Develop a fictional composite district scenario. Steps:

Identify a governance challenge that is concrete, specific, and instructive

Give the composite district a fictional name (Ridgeline School District, Clearwater Unified, Prairie Lakes School District, Westford Community Schools, etc.)

Develop the context: board composition, timeline, what triggered the challenge

Develop the resolution: what the board did, why it worked or partially worked

Identify the governance lesson: what another board should draw from this

Verify: is there a real district thinly veiled here? If yes, create more distance or start with a different scenario.

Step 7 — Research Note Source Identification and Verification

Identify one real, verifiable research source that connects to the week's governance theme. Verify:

The source exists (author, year, title, publication all confirmable)

The source says what you intend to describe (not a paraphrase of a paraphrase)

The citation is in correct format

The connection to the week's theme is genuine

If no verifiable source is available, flag the issue for human review before proceeding. Do not proceed to Step 8 without a verified Research Note source.

Step 8 — Issue Draft Generation

Generate the full draft using the configured write model as primary model. If the configured write model is unavailable, use Claude Opus 4.8 as fallback.

Generate all four sections in order. Include all front matter. Use correct section anchor IDs.

Step 9 — Four-Section Completeness Check

Verify:

All four sections are present (The Lead, Three Things, Featured District, Research Note)

All four section anchor IDs are present and correct (#lead, #three-things, #district, #research)

Word counts are within acceptable range (~400/~300/~350/~250; flag significant deviations)

Front matter is complete (layout, title, issue_number, date_display)

File is named correctly (issue-NNN.html, zero-padded)

Step 10 — Research Note Citation Verification

Verify (separate pass from Step 7):

Author/year/title/publication are all confirmed real and accurate

The description of the research accurately reflects what the research found

No fabrication, no overstatement, no stripped caveats

Citation format is correct

If any element cannot be verified, flag and halt publication pending human review.

Step 11 — Index.html and Archive.html Update Drafts

Generate the updated sections for both files:

index.html: four This Issue items (one per section, with anchor links) + new row in Previous Issues table

archive.html: new top row in the issues table

Verify that headlines in both files exactly match the headline in the issue file's front matter.

Step 12 — Quality Checks (Section 8 below)

Apply all quality checks in Section 8 in order: anti-slop scan (8a), voice check (8b), site-specific checks (8d), primary red-team (8e), council red-team (8f), existential voice test (8g). Fix all flagged issues before proceeding.

Step 13 — Submit to AJ

Submit draft for AJ approval. Record submission timestamp. 72-hour clock begins.

Include in submission:

Issue draft (all files: issue HTML, index.html update, archive.html update)

Brief topic summary (Lead topic + angle, Three Things topics, Featured District challenge, Research Note source)

Any flags or notes from quality checks

Step 14 — 72-Hour Fallback

If AJ does not respond within 72 hours:

Conduct full quality and validity recheck using the configured write model

the configured write model must check: voice authenticity, governance filter, research citation verification, anti-slop protocol, existential voice test

Document the configured write model findings

Fix any issues the configured write model flags

Publish all three files (issue, updated index.html, updated archive.html)

Log the publish with note: "Published via 72hr fallback — the configured write model verified [date/time]"

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

Ultimate Failure Reporting — SBW: Do NOT submit for AJ approval. Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (SBW), edition topic, which check failed, attempt count, nature of each failure, and the draft. Mark status as FAILED.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any em-dash (unicode — is forbidden; use a spaced double-hyphen "--" instead, sparingly, or split the sentence)

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (schoolboardweekly.com): The following additional phrases and constructions are banned for SBW specifically:

"at the end of the day" (already in Tier 3, but flag with high priority for SBW — AJ has explicitly struck this)

"moving the needle"

"robust" (already in Tier 2 — treat as Tier 1 for SBW)

"holistic" (already in Tier 1)

Throat-clearing openers: any sentence that begins with "School boards across the country..." or equivalent broad generalization as the opening line

Passive constructions in editorial positions: "It has been observed that..." instead of "Boards that..."

Attribution to "experts say" without specificity

8b. Voice Check

Voice Check — Moderate Fidelity (ajc-short)

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

Sentences average ~14 words; paragraphs 2–4 sentences

No extended run (3+ consecutive) of sentences under 8 words

Reading level appropriate for a practitioner audience

8d. Site-Specific Checks

Newsletter voice drift check: Does the writing drift into institutional/journalistic mode instead of AJ's editorial voice? Signs of drift:

Passive constructions where active editorial voice belongs ("It has been observed that..." instead of "Boards that...")

Attribution to "experts say" without specificity

Both-sidesing without taking a position

Language that sounds like a press release or staff report

If any of these patterns appear, revise before proceeding.

Management creep check: Does any section discuss operational school matters instead of board governance?

Check The Lead: is the main subject board governance, or is it what the superintendent/staff did?

Check Three Things: are the questions about board member roles and responsibilities, or are they about management decisions?

Check Featured District: is the governance challenge actually a governance challenge, or is it a management problem the board is getting involved in?

If any section has crept into management territory, revise to refocus on board governance

Toothless Three Things check: Do the Three Things answers actually answer the questions?

Read each Q&A: does the answer state a position in the first sentence?

Is there any question where the answer is essentially "it depends" without resolving what it depends on?

Is there any answer that a knowledgeable person would disagree with — not because it's wrong, but because it takes a real stance? (If not, it may be too hedged.)

Generic Featured District check: Is the composite district scenario specific and instructive, or vague and generic?

Does the scenario have a specific trigger event (not just "the board faced challenges")?

Does the scenario have specific context (board composition, timeline, what was said or done)?

Does the resolution describe what actually happened (concrete actions) or just that things "improved"?

Is there a governance lesson that is specific enough to be actionable for another board?

Research Note fabrication check (final pass):

Can the author, year, title, and publication all be confirmed independently?

Does the description of findings match what the research actually reports?

Is the connection to the week's theme genuine and accurate?

Governance filter test: Is every section genuinely about board governance, or has management/operational content slipped in?

Look specifically for places where the framing sounds like governance but the substance is management

Example of slippage: "The board should ensure teachers are using high-dosage tutoring effectively" — this is management direction disguised as governance language

Recency test:

Has this specific governance angle appeared in a recent SBW Lead?

Has the same research been cited in a recent Research Note?

Is the Featured District scenario substantially similar to a recent Featured District?

Naming violation check:

Are any real district names used outside of citations? (Should be zero.)

Are any student names mentioned? (Should be zero, always.)

Are any individual board member, superintendent, or staff names used outside of direct quotes from published sources? (Should be zero unless quoting a published source.)

Publication-ready check:

Is the front matter complete and accurate?

Are all four section anchors present and correctly formatted?

Does the headline in the front matter match what will appear in index.html and archive.html?

Is the file named correctly?

Are index.html and archive.html updates complete and consistent?

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

SBW-specific indicators of failure:

Could this exact issue (content and voice) appear in Education Week, NSBA's newsletter, or a state school board association publication? If yes, the issue is not distinctively SBW — the editorial voice or governance filter is not strong enough. Revise.

Does The Lead have an editorial angle the author is willing to stake out — a position that someone could disagree with? If no, the Lead is too hedged. Revise.

Are the Three Things answers genuinely direct, or do they hedge? If hedged, revise.

This test is subjective. If you would not be surprised to see this exact piece on a competitor site, it fails.

Technical Filing

Issue File

Front matter present and complete: layout, title, issue_number, date_display

layout is issue

issue_number matches file name (zero-padded)

date_display is the Monday publication date in long format

File is named issue-[NNN].html with correct zero-padded number

All four sections present: The Lead, Three Things, Featured District, Research Note

All four section anchor IDs present and correct: #lead, #three-things, #district, #research

Word counts within acceptable range (~400/~300/~350/~250)

Research Note citation present, complete, and verified

No individual names (except in direct quotes from published sources)

No student names

No real district names in body (fictional composite name in Featured District only)

File is output as front matter + body HTML only — no full HTML document structure

Index.html

"This Issue" section updated with four items linking to new issue's section anchors

Each item is a brief description of that section's content

Each item links correctly to the section anchor in the new issue file

New issue added to "Previous Issues" table

Headline in index.html exactly matches headline in issue file front matter

Archive.html

New row added at the top of the issues table (newest first)

Row includes: issue number, date, headline, link to issue file

Headline in archive.html exactly matches headline in issue file front matter

Ongoing Content Integrity

6-Month Recency Rule: Maintain a running record of recent Lead topics and angles. This record is checked at Step 3 of every generation cycle. The record should contain:

Issue number and date

One-sentence Lead topic summary

One-sentence angle description (what stance the Lead took)

When the six-month window advances, drop the oldest issues from the active recency check list. But maintain the full archive — if a question arises about whether a topic was covered, the full archive is the reference.

Timely Content That Ages Well: SBW covers timely governance issues, but issues are archived and may be read months or years later. Guidelines:

Do not write "this week" without specifying what week — use "in June 2026" or "following the [event] in spring 2026"

Do not refer to "recent" events without specifying when they occurred

Do not make predictions that will obviously age poorly

Do not write as if the reader knows what is happening in the news the moment they read it — provide enough context that the issue reads coherently six months later

Archive Consistency: The headline in the issue file's front matter must match the headline displayed in:

index.html (both in the "This Issue" section, if applicable, and in the "Previous Issues" table)

archive.html (in the issues table)

If a headline is revised after initial publication, all three files must be updated together. Inconsistency across files creates reader confusion and undermines the archive's integrity.

Issue Tracking Log: Maintain a log entry for each published issue:

Issue number and file name

Date of draft generation

Date submitted to AJ

AJ response date (or "72hr fallback" if applicable)

Model used for draft generation

Model used for 72hr check (if applicable)

Date published

Any flags raised and resolved during quality checks

Independent Review Protocol

AJ Approval Workflow

Submit draft to AJ with the topic brief

72-hour clock begins at time of submission

If AJ approves: publish as directed

If AJ requests revisions: revise and resubmit (72-hour clock resets)

If AJ does not respond within 72 hours: a. Conduct a second full quality and validity check using the configured write model b. the configured write model check must cover: voice authenticity, governance filter, research citation verification, anti-slop, and existential voice test c. If the configured write model check passes: publish d. If the configured write model check flags issues: fix flagged issues, then publish e. Log the publish in the issue tracking log with a note: "Published via 72hr fallback — the configured write model verified"

Learned Rules

This section accumulates site-specific rules derived from observing what AJ edits. Append new rules as they are learned.

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"