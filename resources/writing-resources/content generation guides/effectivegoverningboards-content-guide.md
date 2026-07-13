title: effectivegoverningboards.com Content Generation Guide type: content-guide site: effectivegoverningboards.com updated: 2026-07-08

For AI use: This document is the complete operational specification for generating weekly policy brief content on effectivegoverningboards.com. Read it in full before generating any content. Never guess at parameters not addressed here -- if a question is not answered by this document, do not publish; flag for human review.

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Domain: effectivegoverningboards.com Content type: Policy briefs Publication frequency: Weekly — one new brief per week Jekyll layout: brief

Purpose: Publish research-backed policy briefs on governing board practices applicable across all types of governing bodies. This site covers ALL governing board types — school boards, hospital boards, nonprofit boards, university trustees, corporate boards, association boards, and public agency boards. It is NOT school-board-specific. Every brief must serve the full range of governing board contexts.

One-sentence purpose: Synthesize peer-reviewed and institutional research on governing board practices to provide evidence-grounded frameworks applicable across all sectors and board types.

Target audience: Governance researchers, policy professionals, think tank analysts, governance consultants, board trainers, and sophisticated board members who want citations and methodology — not just practitioner advice. Readers may include academics studying organizational governance, analysts at foundations or policy institutes, experienced board chairs across healthcare, higher education, nonprofit, corporate, and public sector contexts, and practitioners who operate at a research-informed level.

Voice: Academic-institutional, formal, cited, objective. No personal voice. No byline. No first-person. Written in the style of a peer-reviewed policy brief — structured, evidence-grounded, restrained in claims. Assertions require citations. Tone is descriptive and analytical, never prescriptive in an advisory sense without grounding the prescription in evidence.

What distinguishes EGB from its sister sites:

schoolboardanswers.com answers practitioner questions in plain language; EGB publishes formal, cited briefs for researchers and sophisticated practitioners

creatingoutcomes.com uses Q&A format and an advisory voice; EGB uses policy brief format with APA citations and makes no claims without evidence

effectiveschoolboards.com is school-board-specific and practitioner-oriented; EGB is cross-sector and research-oriented

EGB requires verifiable citations in every brief — this is not optional and cannot be substituted with general statements about "research"

EGB requires cross-sector applicability — a brief that only applies to school boards fails the site's core mandate

EGB is a reference document site; briefs are designed to remain authoritative for years, not to comment on current events

Critical distinction to internalize: EGB is aligned with why-based governance (the principle that all governing boards should anchor their work to a clear organizational "why" — mission, purpose, intended outcomes). This framing applies across all board types. EGB is NOT aligned with the ESB (Effective School Boards) framework, which is school-board-specific. When this guide refers to "why-based" thinking, it means: every brief should ultimately address how boards can govern more purposefully in service of their mission, regardless of sector.

Content Goals:

What a successful brief accomplishes:

Synthesizes existing peer-reviewed and institutional research on a defined governance topic

Draws out practice implications that are applicable across multiple board types (school, hospital, nonprofit, university, corporate, public agency)

Presents claims only with supporting citations — every empirical assertion traces to a real published source

Advances the reader's understanding of how mission-focused governance operates in the domain under study

Serves as a reference document that governance researchers, consultants, and sophisticated practitioners can cite

Remains useful and accurate for years without needing revision (evergreen standard)

Adds to the site's library by covering a topic area not previously addressed (gap-filling function)

What a failed brief looks like:

Too school-board-specific: The brief discusses governance concepts using only school board examples, framing, or terminology without acknowledging other board types. A hospital board trustee or nonprofit board chair would read it and conclude it wasn't written for them. This is a hard fail.

Missing citations: Any empirical claim appears without a citation. The phrase "research shows" with no citation is a hard fail. "Studies suggest" with no citation is a hard fail. Vague appeals to evidence without sourcing are a hard fail.

Invented citations: A citation appears that cannot be traced to a real published source. Author does not exist, publication does not exist, or the cited work does not say what the brief claims. This is a hard fail and a credibility-destroying error.

Too conversational: The voice drifts into advisory, first-person, or practitioner-tip register. Sentences like "Boards should consider..." or "A good practice is..." without evidence are voice failures.

Advocacy disguised as evidence: The brief advances a governance philosophy or recommendation without grounding it in research. Opinion presented as finding.

Governance platitudes: Claims that sound governance-y but convey nothing specific ("boards must be accountable") without specifying to whom, for what, and via what mechanism — and without a citation to research that examines these questions.

Management topics: The brief discusses operational or management decisions rather than governance. How a CEO sets staff compensation is management. How a board sets performance expectations for the CEO is governance. The line must be clearly on the governance side.

Duplicate coverage: A brief substantially covers the same topic as an existing brief in the library. New briefs must fill gaps, not retread covered ground.

Content Format and Structure:

Every brief follows this structure in order:

Abstract — 2–3 sentences. States the topic, summarizes the research synthesis approach, and identifies the core finding or practice implication. Does not introduce new material not covered in the body.

Body sections — 4–6 thematic sections, each with an H2 header. Sections move logically from background/context → research findings → practice implications → unresolved questions or future directions. The final section is not a summary — it should advance a concluding analytical point.

References section — Minimum 5–6 APA-format citations. Headed "References" as an H2. All citations appear in the body as in-text citations before appearing in the references list. No orphaned references (a citation in the list that doesn't appear in the body). No orphaned in-text citations (a body citation that doesn't appear in the list).

Word count: Body text (abstract through final section): 1,000–1,500 words. References section: not counted in word total. Do not pad to reach 1,000 words. Do not cut useful content to stay under 1,500 words. Both bounds are targets, not hard cutoffs, but deviation beyond ±100 words should be flagged.

Required elements:

Abstract: yes, required, 2–3 sentences

H2 section headers: 4–6, required

In-text citations: required wherever an empirical claim is made

References section: required, APA format, minimum 5 citations (6 preferred)

No conclusion summary section: the brief ends with a substantive analytical section, not a recap

Forbidden patterns:

No Q&A format (questions as headers followed by answers)

No first-person singular or plural ("I," "we," "our")

No direct address to the reader ("you," "your board")

No conversational asides or parenthetical jokes/commentary

No advice without evidence (every prescription must cite a source)

No bullet-point lists of tips or action items (body text is analytical prose)

No "In conclusion..." or "In summary..." openers for final section

No rhetorical questions as section openers

No claims that begin "Research shows..." without an immediately following in-text citation

Jekyll front matter: Every brief begins with the following front matter block:

---

layout: brief

title: "[Full descriptive title of the brief]"

badge: "[Topic area badge — see badge values below]"

brief_number: [integer, next in sequence]

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

Badge values (topic area labels):

Board Composition

Executive Oversight

Accountability

Performance Measurement

Board Development

Stakeholder Engagement

Ethics & Conflict

Succession Planning

Resource Governance

Board-CEO Relations

Committee Structures

External Oversight

If a new topic area arises that does not fit any badge above, flag for human review before publishing.

No date field in front matter. EGB briefs are evergreen reference documents. Do not add a date: field to the front matter. The <div class="meta"> date field in the rendered brief header must also be omitted or left empty — do not display a publication date visually in the output.

Brief number: Increment from the highest existing brief_number in the library. Check the existing file set before assigning.

File naming pattern: briefs/[topic-phrase].html

Rules:

All lowercase

Hyphens between words, no underscores, no spaces

3–6 words that identify the topic

Descriptive enough that the slug alone conveys the subject

No dates in filenames

No brief numbers in filenames

Examples:

briefs/board-ceo-relationship.html

briefs/outcome-monitoring-evidence.html

briefs/budget-governance-practices.html

briefs/board-chair-role.html

briefs/board-diversity-outcomes.html

briefs/accountability-measurement.html

briefs/board-chair-succession.html

briefs/conflict-of-interest-governance.html

briefs/stakeholder-engagement-legitimacy.html

Do not reuse a slug that already exists in the library. Do not create slugs that are so similar to existing slugs that they would be confused (e.g., if board-chair-role.html exists, do not create board-chair-roles.html).

References section HTML formatting:

<h2>References</h2>

<ul class="references">

  <li>Author, A. A., &amp; Author, B. B. (Year). Title of article. <em>Journal Name</em>, <em>Volume</em>(Issue), pages. <a href="https://doi.org/xxxxx" target="_blank" rel="noopener">https://doi.org/xxxxx</a></li>

  <li>Author, C. C. (Year). <em>Title of book</em>. Publisher.</li>

</ul>

Ampersands in author names use &amp; HTML entity. Journal names and book titles use <em> tags. DOIs and URLs must be rendered as live hyperlinks: <a href="https://doi.org/xxxxx" target="_blank" rel="noopener">https://doi.org/xxxxx</a> — plain-text URLs are not acceptable. Entries are in alphabetical order by first author's last name.

In-bounds content — topic areas by governance domain:

Board Composition and Structure: director/trustee selection criteria and processes; board size and its effects on governance quality; diversity (demographic, professional, cognitive) and governance outcomes; term limits and board renewal; independence and conflict-of-interest structuring; committee design and committee-to-board authority delegation; board chair and officer roles.

Executive Oversight: CEO/executive director evaluation frameworks and processes; CEO compensation governance; succession planning for chief executives; board-CEO relationship structure and role clarity; performance expectations setting and monitoring.

Accountability and Performance Measurement: outcome monitoring frameworks; distinguishing inputs, outputs, and outcomes in governance oversight; performance data review and board interpretation; accountability to external stakeholders and regulators; setting and monitoring strategic metrics.

Resource Governance: budget governance (board's role vs. management's role); audit committee function and oversight; endowment governance (for nonprofits and universities); capital allocation decision frameworks; financial risk oversight.

Stakeholder Engagement and Legitimacy: public accountability and transparency mechanisms; community engagement in governance; stakeholder representation models; legitimacy theory and its governance applications.

Ethics, Conflicts, and Integrity: conflict of interest policy and enforcement; board ethics codes and their effectiveness; whistleblower protection and governance; related-party transaction oversight.

Board Development and Effectiveness: board training and orientation practices; board self-assessment methods; continuous education for trustees; board retreat design and facilitative governance development.

Succession and Continuity: board chair succession planning; knowledge transfer in board transitions; CEO succession planning (board's role); institutional memory preservation.

External Oversight and Regulatory Environment: accreditation and governance; regulatory compliance frameworks; audit function and external auditor oversight; government reporting and accountability requirements.

Cross-sector applicability requirement: Every brief must explicitly or implicitly address governance across multiple board types. This does not mean mentioning each sector in every paragraph — it means framing findings and implications in ways that resonate across sectors.

Acceptable: A brief on CEO evaluation frameworks that draws on research from healthcare, higher education, and nonprofit sectors, and frames implications in governance terms applicable to any board with a single chief executive.

Acceptable: A brief on board diversity that cites research from corporate governance (where the majority of large-scale studies have been conducted) and explicitly notes the applicability to nonprofit and public sector boards, noting where research is thinner.

Unacceptable: A brief on superintendent evaluation that is framed entirely around K-12 contexts, uses K-12-specific terminology throughout, and would require substantial rewriting to apply to a hospital board.

How to frame for multiple board types: When citing research from one sector, explicitly note whether findings generalize. When using a term that has sector-specific meaning (e.g., "superintendent" in K-12; "medical staff bylaws" in healthcare), either use the sector-neutral term ("chief executive") or note the sector-specific variant alongside the general concept.

The three-sector check: Before finalizing a brief, ask: would a hospital board member, a nonprofit trustee, and a school board member all find this brief directly relevant without having to mentally translate it? If one of those three would struggle to see the relevance, revise the framing.

Research sourcing — prioritize citations from:

Peer-reviewed governance journals: Corporate Governance: An International Review; Journal of Corporate Finance; Nonprofit and Voluntary Sector Quarterly; Public Administration Review; Educational Administration Quarterly; Journal of Health Politics, Policy and Law; Higher Education; Governance: An International Journal of Policy, Administration, and Institutions; Journal of Policy Analysis and Management.

Institutional research publishers: RAND Corporation (rand.org); Brookings Institution (brookings.edu); Institute of Education Sciences / What Works Clearinghouse; National School Boards Association (NSBA) research publications; AASA — The School Superintendents Association; McREL International; BoardSource (nonprofit governance research); National Association of Corporate Directors (NACD); Association of Governing Boards of Universities and Colleges (AGB); The Governance Institute (healthcare governance); Harvard Kennedy School — Center for Public Leadership; Stanford Social Innovation Review (for nonprofit governance).

Government and regulatory sources: Government Accountability Office (GAO) reports; Inspector General reports; state-level education or health agency research; federal agency governance guidance documents.

Minimum citation quality bar: A source is acceptable if it (a) is published by a recognized institution or peer-reviewed journal, (b) is verifiable via DOI, ERIC, PubMed, JSTOR, Google Scholar, or direct institutional URL, and (c) actually exists and says what the brief claims.

Stylistic models — existing briefs:

Study these existing briefs to calibrate voice, structure, and citation density:

briefs/board-ceo-relationship.html — model for: how to frame the governance/management boundary clearly; tone calibration for a structurally complex topic

briefs/outcome-monitoring-evidence.html — model for: synthesizing quantitative research; how to present measurement frameworks without drifting into management prescriptions

briefs/budget-governance-practices.html — model for: covering a resource governance topic that applies equally across sectors; how to cite institutional reports alongside peer-reviewed journals

briefs/board-chair-role.html — model for: covering a specific governance role without becoming advisory; keeping claims grounded in research

briefs/board-diversity-outcomes.html — model for: using primarily corporate governance research while extending applicability to other board types; handling contested or mixed evidence

briefs/accountability-measurement.html — model for: covering accountability frameworks applicable across public and nonprofit sectors

When in doubt about voice or structure, reread one of these before drafting.

Out-of-bounds content:

School-board-only framing: A brief that is framed entirely for school boards — that uses K-12-specific terminology as default, discusses governance concepts only in K-12 contexts, and would require substantial revision to be useful to a hospital board — is out of bounds for this site.

Test: Remove all K-12 terminology from the brief. Does a coherent, useful governance document remain? If not, the brief is too school-board-specific.

Exception: A brief may focus on a sector-specific example if (a) it explicitly uses that sector as one case among several, (b) the governance principle under study applies across sectors even if the example is sector-specific, and (c) the framing language is sector-neutral where possible.

Management topics disguised as governance: The governance/management line is critical and must be actively maintained.

Governance topics (in bounds): how the board sets performance expectations for the CEO; how the board monitors outcomes against stated goals; how the board approves and oversees the budget at a strategic level; how the board selects and evaluates its chief executive; how the board ensures the organization maintains ethical standards.

Management topics (out of bounds): how a CEO or superintendent sets staff compensation levels; how program staff design service delivery; how HR processes work; curriculum decisions, clinical protocol decisions, or program design; day-to-day operational decision-making.

Opinion without evidence: EGB publishes evidence-based briefs, not advocacy. If a brief advances a governance practice recommendation, that recommendation must be grounded in research showing its association with better governance outcomes, or clearly presented as a practice-inference from theory (with the theoretical source cited). Phrases like "boards should prioritize..." or "effective governance requires..." are acceptable only when followed immediately by a citation to research that supports the claim.

Topics without verifiable research: If 5–6 verifiable citations cannot be assembled for a topic before drafting begins, the topic should be deferred or reframed. Do not draft a brief and then search for citations to fit the claims already made.

Citation requirements:

All citations use APA 7th edition format.

Journal article: Author, A. A., & Author, B. B. (Year). Title of article in sentence case. *Journal Name in Title Case*, *Volume*(Issue), pages. https://doi.org/xxxxx

Book: Author, A. A. (Year). *Title of book in sentence case*. Publisher.

Book chapter: Author, A. A. (Year). Title of chapter. In E. E. Editor (Ed.), *Title of book* (pp. xx–xx). Publisher.

Report (institutional): Organization Name. (Year). *Title of report*. Publisher/Organization. URL

In-text citation format: single author: (Smith, 2019); two authors: (Smith & Jones, 2019); three or more authors: (Smith et al., 2019); direct quote (rare; paraphrase is preferred): (Smith, 2019, p. 42).

5 citations minimum. 6 citations preferred. This is a hard requirement. A brief with fewer than 5 verifiable citations fails the quality gate and must not be published. There are no exceptions.

Acceptable citation sources: peer-reviewed journal articles in governance-adjacent fields; RAND Corporation reports; Brookings Institution reports; Institute of Education Sciences publications; National Bureau of Economic Research working papers (when citing pre-publication research; note working paper status); BoardSource research publications; National Association of Corporate Directors (NACD) research; Association of Governing Boards (AGB) research; The Governance Institute research; NSBA and AASA published research (not advocacy materials); McREL International research publications; GAO reports and federal agency research; Harvard Kennedy School and similar policy school research publications; peer-reviewed dissertations (use sparingly; note dissertation status).

Unacceptable sources: blog posts, even from well-known organizations; news articles (may appear in footnotes for factual context but do not count toward the 5-citation minimum); organizational advocacy materials that are not research publications; any source that cannot be independently verified via DOI, ERIC, PubMed, JSTOR, Google Scholar, or a direct institutional URL; any citation that does not exist — invented author names, invented journal names, invented publication years, invented DOIs; Wikipedia; any source where the AI generating the brief cannot verify the existence of the specific publication.

Hard rule — every citation must be traceable: Before a citation appears in a brief, the generating AI must be able to verify: (1) the author(s) exist and have published in this field; (2) the publication (journal, book, report) exists; (3) the specific article or chapter exists in that publication; (4) the year and volume/issue information is accurate; (5) the cited work actually supports the claim being made in the brief.

If any of these five conditions cannot be confirmed, the citation must be dropped. Fabricated citations are worse than no citations. A brief with 4 verifiable citations that acknowledges the gap is better than a brief with 6 citations where 2 are invented.

Grounding Document

Source: Why-Based Governing Boards: How Boards Fail, How Yours Can Become Effective by AJ Crabill Access: Google Drive ID: 1VZ76e4NNc6Spd6M6jAZ3gQvO3SVxOvZTri7QfkrRXhg (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: a — pre-draft only

Pre-draft only: Before drafting, read the relevant sections of the grounding document. Use it to calibrate the frame, vocabulary, and core claims before writing begins. It is a framing calibrator, not a citation source.

Voice Register

Register: ajc-long (~23 words/sentence avg, 4–8 sentence paragraphs)

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

Sentence and paragraph targets: Sentences average approximately 23 words. Paragraphs run 4–8 sentences. No extended run (3 or more consecutive) of sentences under 8 words.

Structural invariants:

Oxford comma: always (a, b, and c)

Straight quotes only (no curly quotes)

Contractions used naturally (don't, it's, we've)

No exclamation marks anywhere in the piece

No ellipses

No voice hedging: no "I feel/think/believe" as epistemic hedges

No sentence-initial transitions: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately

Note: For EGB, the academic-institutional voice requirement governs register. The ajc-long register informs the underlying prose rhythm and structure but is subordinate to the formal, cited, objective voice described in the site context above. First-person is prohibited at EGB even where ajc-long would normally permit it.

NEVER Rules

Never invent a DOI or citation — fabricated citations are worse than no citations

Never generate a brief without first confirming 5–6 verifiable citations with real DOIs

Never draft first and find citations second — citation inventory precedes drafting

Never publish with a dead (404) DOI link — zero tolerance

Never let a 4xx or 5xx HTTP response pass as a valid DOI (exception: 403 is valid — see Learned Rules LR-002)

Never leave body text making a claim after its sole supporting citation has been removed — body text review is mandatory after any citation removal

Never frame a brief exclusively in school-board terms — cross-sector applicability is a hard requirement

Never include governance platitudes without specific mechanisms, conditions, and citations

Never use first or second person anywhere in a brief

Never offer practitioner advice without a citation grounding the prescription in evidence

Never use a badge value not on the approved list — flag for human review

Never reuse an existing slug or create a slug so similar to an existing slug as to cause confusion

Never generate a full standalone HTML document — output front matter + body only

Never publish if any quality gate has failed — flag for human review

Never include a publication date in the visible post content or meta div — the <div class="meta"> date field must be omitted (left empty or removed entirely) from the generated HTML; briefs are intended as durable reference documents and visible dates undermine that

Generation Process

Step 1 — Topic Selection and Cross-Sector Applicability Check

Perform gap analysis:

Audit existing brief slugs — list all current .html files in the briefs/ directory; map each to its governance domain

Identify underrepresented topic areas — which governance domains from the site context have no briefs, or only 1–2 briefs relative to their research depth?

Identify high-value gaps — within underrepresented domains, which topics have the strongest research base (most citable, most cross-sector applicability, most likely to serve the target audience)?

Select the highest-priority gap topic that also passes the pre-draft checks below

Name three specific board types (e.g., hospital board, university board, nonprofit board) that benefit from this brief

Confirm cross-sector framing is achievable; if fewer than three board types benefit, reconsider the topic or reframe it at a higher level of abstraction

Write a one-sentence topic description and a one-sentence framing note (e.g., "This brief synthesizes research on board committee structures, drawing primarily on corporate and nonprofit governance literature, with implications for public agency and healthcare boards")

Step 2 — Research Sourcing: Identify 6–8 Real Candidate Citations Before Drafting

Search governance research literature for the selected topic

Identify 6–8 sources that appear real and relevant

For each, note: author(s), year, title, publication, and one sentence on what it contributes to the topic

Confirm that at least 5–6 are from acceptable sources

Preliminary verification: confirm author names and journal/publisher names exist (full citation verification comes in Step 5)

Do not proceed to drafting if 5 confirmable citations cannot be assembled

Cross-sector check: confirm that identified candidate citations represent at least two different board type sectors where possible

Step 3 — Abstract and Outline Generation

Draft the abstract (2–3 sentences: topic, approach, core finding or implication)

Draft section outline: 4–6 H2 headers with one sentence describing what each section will cover

Map each section to the citations it will draw on

Confirm outline covers: background/context, research findings, practice implications, and a substantive closing point (not a summary)

Check that no section is citation-free (every section should draw on at least one citation)

Step 4 — Draft Generation

Primary model: the configured write model Fallback model: Claude Opus 4.8 (use if the configured write model unavailable or if draft quality falls below standard on first generation)

Generate the full draft following the structure established in Step 3. Do not deviate from the outline without flagging the deviation. Write in academic-institutional voice throughout. Include in-text citations as drafted. Write the references section in full at the end.

Word count target: 1,000–1,500 words for body text. Flag if outside ±100 words of this range.

Step 5 — Citation Verification Pass

For every citation in the draft:

Confirm the author(s) exist and have published in this field

Confirm the publication (journal, book, or institutional report) exists

Confirm the specific article, chapter, or report exists in that publication

Confirm the year and volume/issue information is accurate

Confirm the cited work actually supports the specific claim made in the brief

Method: Cross-reference against Google Scholar, DOI lookup, ERIC (for education research), PubMed (for health governance), or direct institutional URLs (rand.org, brookings.edu, boardsource.org, etc.).

If a citation fails verification: Remove it from the brief. Revise the claim it supported to either (a) find a replacement citation or (b) remove the unsupported claim. Do not retain unverifiable citations.

After verification: Confirm the brief still has a minimum of 5 citations. If it has dropped below 5, either find additional verifiable citations or flag for human review.

Step 6 — Why-Based Alignment Check

Review every section and ask: does this section ultimately connect to how boards can govern more purposefully in service of their mission?

Why-based governance for EGB means: all governing boards have a "why" — a mission, a purpose, an intended outcome they exist to serve. Every brief should implicitly or explicitly address how the governance practice under study enables boards to maintain focus on their "why" rather than drifting into procedural, political, or self-preserving governance.

This is not a surface-level check. The connection to mission-focused governance should be substantive, not cosmetic. If a section discusses board committee structures only in terms of efficiency and workload distribution, without connecting to how committee structures enable boards to monitor mission-critical outcomes, it fails this check.

If a section fails: Revise to strengthen the connection to purpose-driven governance. Do not add a tacked-on sentence — revise the analytical framing of the section.

Step 7 — Cross-Sector Applicability Check

Review the full draft and ask:

Would a hospital board trustee find this brief relevant and useful?

Would a nonprofit board chair find this brief relevant and useful?

Would a university trustee find this brief relevant and useful?

If the answer to any of these is "no" or "only with significant mental translation," identify the section(s) causing the problem and revise:

Replace school-board-specific terminology with sector-neutral equivalents

Add sector context where a concept has sector-specific manifestations

Ensure research citations are from multiple sectors (or, if from one sector, explicitly note the cross-sector applicability of the findings)

Step 8 — Quality Checks

Run all quality checks per Section 8 (below). Complete all checks and resolve all failures before proceeding to Step 9.

Step 9 — DOI Live-Link Verification

This is a hard, non-negotiable gate. The site maintains zero tolerance for non-functional DOI links. Every DOI that appears in the published brief must resolve.

For every DOI link in the references section:

Make an HTTP HEAD request to https://doi.org/{doi}

A 302 response means the DOI is registered and valid — proceed

A 403 response means the DOI is valid but the publisher blocks bots — the article exists; treat as valid (see LR-002)

Any other response (404, timeout, connection error) means the DOI is dead

If a dead DOI is found:

First, attempt to locate the correct DOI: search Google Scholar, CrossRef (doi.org/search), or the publisher's site using the citation's author names, title, and year

If a working replacement DOI is found and confirmed to resolve to the correct paper: replace the dead DOI with the correct one in the reference list entry

If no correct DOI can be confirmed: remove the entire <li> citation entry from the references list. Also revise or remove any body text that relied solely on that citation for its claim

After all corrections:

Re-verify the total citation count

If fewer than 5 citations remain: search CrossRef (api.crossref.org) for up to 4 replacement citations relevant to the article topic — CrossRef is used here specifically because it is a different source than the perplexity-backed citation search used in Step 2. For each CrossRef candidate: (a) verify the DOI resolves via HTTP, (b) confirm the paper is relevant to the article's topic and claims. Add passing candidates to the references section in APA format with live DOI links.

Re-run HTTP verification on any replaced or added DOIs to confirm they resolve

If the citation count is still below 5 after all replacement attempts: the brief is held as pending for human review with a quality note explaining the shortfall. Do not auto-publish below 5 verified citations.

This gate cannot be skipped or deferred. A brief with a dead DOI link must not be published in any state. There are no exceptions.

Step 10 — Technical Filing

Set front matter fields: layout: brief, title:, badge: (from approved badge list), brief_number: (next in sequence)

Confirm file name follows naming convention (briefs/[topic-phrase].html)

Confirm file is placed in the briefs/ directory

Format references section in HTML per site context specification

Confirm all DOI links are rendered as live hyperlinks (Step 9 must be complete before this step)

Run Jekyll build check — confirm no front matter errors, no broken HTML, no missing closing tags

Confirm brief_number is the next integer in sequence (no gaps, no duplicates)

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

Ultimate Failure Reporting — EGB: Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (EGB), article title, which check failed, attempt count, nature of each failure, and the draft. Mark status as FAILED. Do not publish.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any unicode em-dash ( — ) or en-dash ( – ) appears; the required form is a spaced double-hyphen ("--"), used sparingly

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (effectivegoverningboards.com):

The following additional AI-tell phrases are banned at EGB and must be removed or replaced:

"delve into"

"in conclusion" / "in summary" as section openers

"it is worth noting that"

"it is important to note"

"this underscores"

"this highlights"

"plays a crucial role"

"a nuanced understanding"

"the landscape of"

"a cornerstone of"

"a paradigm"

"navigating the complexities of"

"a multifaceted approach"

"foster a culture of"

"crucial," "critical," "essential," "vital," "fundamental," "dynamic," "impactful" (when used as hollow intensifiers with no informational content)

These phrases are acceptable only if they are the only precise way to express the thought (rare). In most cases they are filler; replace with direct language.

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

Contractions used naturally (don't, it's, we've) — note: EGB's academic-institutional register means contractions should be used sparingly; apply this fingerprint with register awareness

Rhythm check:

Sentences average ~23 words; paragraphs 4–8 sentences

No extended run (3+ consecutive) of sentences under 8 words

Reading level appropriate for a practitioner audience

EGB-specific voice checks (beyond standard):

No first-person singular or plural anywhere ("I," "we," "our")

No direct address to the reader ("you," "your board")

No conversational asides or parenthetical commentary

No advice without evidence (every prescription must cite a source)

No hedging language that substitutes for evidence: "generally speaking," "often," "typically" without citation

No advocacy or enthusiasm for a governance practice without evidence support

Flag any sentence that uses first or second person, offers advice without a citation, uses conversational filler, or drifts into advocacy register — revise to restore academic-institutional register

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

EGB-Specific Check A — Governance Platitude Detection

Flag any sentence that uses governance terminology but conveys nothing specific about mechanisms, conditions, or evidence:

"Boards must be accountable." — Accountable to whom? For what? Via what mechanism? Cite evidence that a specific accountability mechanism produces a specific governance outcome.

"Effective boards engage stakeholders." — How? Under what conditions? With what effects? Source?

"Strong leadership matters for governance." — This says nothing without specifics and evidence.

Replace governance platitudes with specific, evidenced claims about governance mechanisms and their effects.

EGB-Specific Check B — Missing-Citation Claim Detection

Distinct from the vague-claim detection in 8a (which catches "research shows" constructions), this check catches declarative statements about governance practices presented as facts:

"Boards that meet more frequently make better decisions." — Citation?

"Conflict-of-interest policies reduce self-dealing on boards." — Citation?

"Board training improves governance outcomes." — Citation?

Any declarative claim about a governance practice and its effects requires a citation. Flag and cite or revise.

EGB-Specific Check C — School-Board-Only Framing Detection

Review every paragraph. Flag any paragraph where:

The only way to interpret the content is in a K-12 school board context

K-12-specific terminology is used as the default framing without acknowledgment of other board types

The governance concept described would not recognize itself in a hospital board, nonprofit board, or university board context

For each flagged paragraph: either revise to use sector-neutral framing or add explicit cross-sector context.

EGB-Specific Check D — Vague Claim Detection

Flag any empirical claim that lacks a citation:

"Research shows..." — without an immediate in-text citation: FAIL

"Studies suggest..." — without an immediate in-text citation: FAIL

"Evidence indicates..." — without an immediate in-text citation: FAIL

Any statement about governance outcomes, prevalence, effectiveness, or frequency without a citation: FAIL

Every factual assertion about the world must have a citation. Every claim about what research finds must have a citation. No exceptions.

EGB-Specific Check E — False Specificity and Unverifiable Statistics Scan

Flag any statistic, percentage, or quantified claim for which no citation is provided:

"Boards that conduct annual self-assessments are 40% more likely to..." — requires citation

"Nearly two-thirds of hospital boards report..." — requires citation

"Research from the past decade shows that..." — requires a specific citation, not a temporal sweep

Remove or properly cite all quantified claims. Do not invent statistics. Do not retain statistics whose source cannot be confirmed.

EGB-Specific Check F — Generic Opener Detection

Review the opening sentence of the abstract and the opening sentence of each section. Flag any sentence that could appear in any brief on any topic without substantive revision:

"Governing boards face numerous challenges..."

"Effective governance is essential to organizational success..."

"Research has demonstrated the importance of..."

"In today's complex environment, boards must..."

Replace with a specific, substantive opener that names the specific governance phenomenon under study.

EGB-Specific Check G — Structure Uniformity Check

Verify that not all sections follow the same sentence-length pattern or open with the same syntactic structure. Academic-institutional prose has variety. If every section opens with "The research on X suggests Y," revise openings for variety while maintaining formal register.

EGB-Specific Check H — Tidy Resolution Detection

Review the closing section. Flag if it:

Summarizes what was already said

Ends with an optimistic forward-looking statement about governance improvement without evidence

Ends with a call to action ("boards should...")

Resolves in a way that is neater or more confident than the evidence warrants

The closing section should advance a final analytical point — a synthesis, a tension, an unresolved question, or an implication that follows from the evidence presented. It should not wrap up tidily if the evidence is contested or mixed.

DOI Live-Link Verification (hard gate)

See Generation Process Step 9 for the full protocol. The short version: every DOI in the published brief must be tested via HTTP before publication. A DOI that returns 404 or fails to resolve must be corrected (replaced with the correct DOI for the same source) or the citation entry removed entirely. 302 = valid; 403 = valid (publisher bot-block; article exists); 404 or connection failure = dead; remove. This gate cannot be skipped or deferred.

Red-team checks (site-specific):

After completing all checks above, run these EGB-specific red-team checks:

Academic Credibility Test: Ask: would a governance researcher who studies this topic find the citations legitimate and the synthesis accurate? Are the cited journals and publications respected in the governance research field? Does the brief accurately characterize what the cited research found, or does it stretch findings to fit the argument? Does the brief acknowledge contested evidence or methodological limitations where they exist? Would a peer reviewer at a governance journal find the synthesis rigorous or superficial? If the answer to the last question is "superficial," identify what is missing: more citations? Engagement with contested findings? Clearer connection between evidence and implication?

Cross-Sector Test: Ask: does this brief actually apply to multiple board types, or does it only work for one board type with superficial rewording? Test by mentally removing all references to one sector and asking whether the brief still makes sense. If a hospital board trustee would need to "translate" more than a few terminology choices to find the brief useful, the cross-sector applicability is cosmetic rather than substantive. Revision: identify the governance principle that underlies the sector-specific example and reframe around that principle.

Citation Authenticity (final sweep): For each citation, confirm the author name is a real person who has published in this field; for each journal citation, confirm the journal exists and publishes governance-relevant research; for each institutional report, confirm the institution published this report; for DOIs, confirm they resolve to the correct document. This check is not redundant with Step 5 — it is a second pass, performed with adversarial intent. If a citation fails: remove it; revise or remove the claim it supported; recheck citation count; if now below 5, flag for human review.

Factual accuracy: Are the governance concepts accurately represented? Does the synthesis accurately characterize what the cited works found, without overstating or understating? Is the distinction between correlation and causation respected?

Internal consistency: Does the brief contradict itself? Does the closing section draw conclusions not supported by the body? Do section headings match section content?

Scope creep: Does the brief stay within its stated topic, or does it drift into adjacent topics that would be better covered in separate briefs?

Omission: Is there a significant body of research on this topic that the brief ignores, and if so, does that omission distort the picture?

Recency: Are the citations appropriately current? Flag any citation from before 2015 for the aging check. Pre-2016 citations are acceptable only if the cited work is foundational and still widely cited, or if no more recent research exists on the specific point.

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

Note for EGB: the existential voice test for this site also includes: "Would this content appear unchanged in a peer-reviewed policy journal or as a research brief from a recognized governance institute (BoardSource, AGB, The Governance Institute)?" If no — if it falls short of that bar because it is too conversational, too school-board-specific, or not sufficiently evidence-grounded — it fails the EGB-specific version of this test. Both directions of failure apply: too generic for AJ's voice, and too informal/narrow for EGB's institutional standard.

Technical Filing

Complete all items before publishing. No item may be skipped.

Front Matter

layout: brief — exactly as written, lowercase

title: — full descriptive title in title case, enclosed in quotes if it contains a colon

badge: — must be one of the approved badge values listed in the site context; enclosed in quotes

brief_number: — integer; verified to be next in sequence; no gaps; no duplicates with existing briefs

File

File named per convention: briefs/[topic-phrase].html — all lowercase, hyphens, 3–6 words

File placed in briefs/ directory

Slug does not duplicate or closely resemble any existing slug in the library

References Section

H2 header: <h2>References</h2> — present and correctly formatted

References in <ul class="references"> — class attribute present

Each citation in a <li> element

Journal names and book titles in <em> tags

Ampersands in author names use &amp;

DOIs and URLs rendered as live hyperlinks: <a href="https://doi.org/xxxxx" target="_blank" rel="noopener">https://doi.org/xxxxx</a> — plain text not acceptable

Every DOI tested via HTTP HEAD to doi.org — all return HTTP 302 or 403. Zero 404s or failures permitted. Any dead DOI has been corrected or the citation entry removed (per Step 9 protocol)

List in alphabetical order by first author's last name

Minimum 5 citations present (recount after any DOI-driven removals)

Every citation in the references list appears as an in-text citation in the body

Every in-text citation in the body appears in the references list

HTML Integrity

No unclosed HTML tags

No broken character entities

Front matter block delimited by --- on both sides

No YAML formatting errors in front matter

Jekyll Build Check

Run Jekyll build locally or in CI environment

Confirm no build errors

Confirm brief renders with correct layout, title, and badge

Confirm references section renders with correct formatting

If any item fails, do not publish. Fix the failure and re-run the checklist from the beginning.

Ongoing Content Integrity

EGB briefs are reference documents, not news articles. Every brief should be written to remain authoritative and useful for a minimum of three to five years without revision:

Do not reference current events or recent news as context

Do not frame governance challenges as "emerging" or "new" unless the research base supports that characterization

Do not cite governance data that reflects a specific moment in time without noting the date and acknowledging that the figure may change

Do not make predictions about governance trends

When a brief must reference time-sensitive data (e.g., survey data on board composition percentages), frame it with the citation year: "In a [year] survey, [X% of boards]..." — not as a timeless fact.

Citation aging: Preferred citation recency: within the past 10 years (2016–present as of 2026). Pre-2016 citations are acceptable if the work is foundational and still widely cited, or if no more recent research exists on the specific point. When citing pre-2015 research, note the age when relevant and verify the finding has not been superseded. When generating a new brief, if the planned topic overlaps with an existing brief that contains citations older than 10 years, flag the existing brief for a citation update review separately.

Cross-site linking rules: EGB may link to sister sites under the following strict rules: maximum 1–2 cross-site links per year per linked site; only in a list of 3 or more links (never singling out one site); the link should appear as a naturally integrated resource reference, not promotional; permitted sister sites for rare linking: effectiveschoolboards.com, whybasedboards.com (1–2 times per year, in a list of 3+); never name ESB, AJ Crabill, GOTB, or why-based governance in EGB content; never link to these as standalone featured resources.

Content update policy: When new research is published that bears on an existing brief: if superseding, flag for human review and update; if additive, flag for scheduled update review. Annual review each January. Procedure for updates: update the brief file in place (same slug, same brief_number); add a last_updated: YYYY-MM-DD field to the front matter; note major updates at the end of the brief in a "Notes on This Brief" section if changes are substantive; minor citation updates or corrections do not require a note.

Duplicate coverage prevention: Before finalizing a topic, review the full list of existing brief slugs; map the proposed topic against existing briefs; if an existing brief covers a substantially overlapping topic, reconsider or identify a distinct angle; a brief that is 60% or more thematically identical to an existing brief is a duplicate and should not be published.

Independent Review Protocol

Approval flow: Auto-publish after all quality gates pass.

Quality gates (all must pass):

Cross-sector applicability check — passed

Research sourcing check — minimum 5–6 verifiable citations confirmed

Citation verification pass — all citations in draft confirmed real and accurate

Why-based alignment check — every section connects to mission/governance purpose

Voice check (8b) — formal, academic-institutional, no conversational drift

Anti-slop cleanup (8a) — completed

ESB governance language check (8c) — completed

Site-specific checks (8d) — completed

Primary red-team (8e) — completed; no major failures

Council red-team (8f) — completed; 3 of 4 personas pass

Existential voice test (8g) — completed; passed

DOI live-link verification — every DOI tested via HTTP; all resolve (302 or 403); no dead links remain; minimum 5 working citations confirmed

Technical publishing checklist — completed

If any gate fails, do not publish. Flag the failure and the specific reason for human review.

Learned Rules

Rules derived from post-publication review — patterns found when comparing AI-generated drafts against corrections made during audit or editorial review.

LR-001 [2026-06-23] — Do not generate DOIs; verify them from real sources

Category: citation

Pattern observed: In 42 EGB briefs generated before this rule was established, 89 unique DOIs were present in the references sections. Testing each DOI via HTTP revealed that 26 (approximately 29%) returned 404 — meaning those DOIs did not resolve to any existing document. The pattern of failure was consistent with confabulation: the author names, journal names, and article titles were plausible-sounding, but the DOIs themselves led nowhere. These were not typos or formatting errors; they were invented citations that happened to carry invented but structurally valid DOI strings.

Rule: Never generate a DOI from memory or inference. DOIs must be sourced from verified lookups — CrossRef (doi.org/search or api.crossref.org), Google Scholar, PubMed, ERIC, or a direct publisher page — not composed or recalled. If a citation cannot be located via a verifiable lookup that returns a real DOI, the citation must be omitted. A citation with no DOI is preferable to a citation with a fabricated DOI.

Source: June 2026 DOI audit of all 42 EGB briefs. 26 citations removed due to 404 DOIs; 23 valid DOIs wrapped as live links.

LR-002 [2026-06-23] — Treat 403 HTTP responses as valid DOIs; treat 404 as hallucinated

Category: citation

Pattern observed: During the DOI audit, two distinct HTTP response patterns emerged. DOIs returning 403 consistently belonged to real articles behind publisher paywalls — CrossRef confirmed these DOIs as registered, and manual lookup on publisher sites confirmed the articles existed. DOIs returning 404 were unresolvable regardless of user-agent or retry behavior, and no matching article could be located through any search method.

Rule: When verifying a DOI via HTTP HEAD request: 302 (redirect to publisher) = valid; 403 (publisher paywall blocks bots) = valid — the article exists. 404 or connection failure = treat as hallucinated — remove the citation entirely. Do not assume a 403 means the DOI is invalid; publisher bot-blocking is common and does not indicate a missing document.

Source: June 2026 DOI audit. 403 responses mapped to confirmed real articles; 404 responses mapped to non-existent articles with no recoverable source.

LR-003 [2026-06-23] — Citation inventory must precede drafting; draft must not precede citation confirmation

Category: citation | accuracy

Pattern observed: The AI-generated briefs show a drafting pattern consistent with: (1) selecting a governance topic, (2) drafting the full analytical text, and (3) populating the references section afterward — at which point real citations may or may not exist for the claims already made. This backwards sequence produces citations that are constructed to fit the draft rather than claims that are grounded in real sources. The 26 removed citations were disproportionately concentrated in briefs where the body text made specific, detailed empirical claims (e.g., percentages, causal relationships, named mechanisms) that no confirmable study appears to support.

Rule: The research sourcing step (Generation Process Step 2) must produce a list of confirmed-real citations with confirmed-real DOIs before drafting begins. The draft is then written to synthesize what those real sources actually say. Never draft first and find citations second. If the citation inventory for a topic cannot reach 5 confirmed-real sources, do not draft that brief — select a different topic with a stronger verifiable research base.

Source: Pattern inferred from June 2026 DOI audit — 26 hallucinated citations removed from a set of 20 affected briefs, suggesting citation confabulation occurred at scale during the original batch generation.

LR-004 [2026-06-23] — Plausible author names and journal names do not verify a citation

Category: citation | accuracy

Pattern observed: Many of the 26 removed citations listed real governance researchers (Cornforth, Herman, Renz, Hillman, Gabrielsson) alongside plausible journal titles (Nonprofit and Voluntary Sector Quarterly, Corporate Governance: An International Review, Educational Administration Quarterly). The authors are real. The journals are real. But the specific articles did not exist — the DOIs pointed nowhere, and no matching publication could be located. The combination of real author names with invented article details was the most common failure mode.

Rule: Confirming that an author has published in a field and that a journal exists does not confirm that a specific article exists. Citation verification must confirm the specific article: the exact title, the specific volume/issue/page range, and a working DOI or direct URL. Preliminary author-and-journal plausibility checks (as described in Step 2) are necessary but not sufficient. Step 5 citation verification and the DOI live-link verification gate in Step 9 are both required before any citation is retained.

Source: June 2026 DOI audit. Removed citations included real researchers (Cornforth & Brown appearing multiple times across different briefs with different invented article details) paired with invented publication specifics.

LR-005 [2026-06-23] — When claims cannot be cited with verified sources, remove the claim — do not substitute a citation

Category: citation | accuracy

Pattern observed: Several briefs contained specific analytical claims (e.g., detailed mechanisms of term limit design, specific policy implications of recruitment screening criteria) for which no verifiable supporting research could be located after the audit. These claims had been paired with fabricated citations as if to provide the appearance of evidence. When the citations were removed, the claims remained in the brief body without support — the briefs were corrected by removing those sections as well.

Rule: An unverifiable claim must be revised or removed, not re-cited with a different invented source. If a governance claim cannot be grounded in a verifiable, real citation, the options are: (a) find a real citation that actually supports the claim; (b) reframe the claim at a level of generality that a real citation can support; or (c) remove the claim entirely. Do not retain unsupported empirical claims in the body of a brief after removing a citation that was supposed to support them. The brief may be shorter as a result — that is acceptable.

Source: June 2026 DOI audit. Two briefs (term-limits-governance.html, recruitment-screening.html) lost their entire references sections and associated body sections when all DOIs returned 404.

LR-006 [2026-06-23] — Minimum citation count must be verified with working DOIs, not nominal count

Category: citation

Pattern observed: All 42 briefs appeared to meet the 5-citation minimum at the point of generation — each had 5–6 references list entries. After the DOI audit, 20 briefs had citations removed, and some of those fell below the 5-citation threshold. The stated minimum of 5 citations was satisfied at draft time by a mix of real and fabricated citations. The real minimum — 5 verifiable citations with working DOIs or confirmed institutional URLs — was not met.

Rule: The 5-citation minimum is a minimum of verified citations, not a minimum of reference list entries. After the DOI live-link verification step removes dead-DOI citations, the remaining count must still reach 5. If post-verification count falls below 5, the brief must not be published until replacement citations are sourced and verified (per the Step 9 protocol). Counting entries in the reference list before DOI verification is not a valid quality gate.

Source: June 2026 DOI audit revealed that nominal citation counts at generation time overstated actual verifiable citation counts by including fabricated entries.

LR-007 [2026-06-23] — Use CrossRef as a different source than perplexity-backed searches; treat them as independent verification

Category: citation

Pattern observed: The Step 9 protocol specifies using CrossRef (api.crossref.org) as a replacement-citation source specifically because it is a different source than the perplexity-backed citation search used in Step 2. This distinction matters: if both citation searches use the same underlying model or source, they may produce the same confabulated citations. The audit confirmed that CrossRef lookup for replacement citations returned different results than the original generation — confirming that independent source verification catches fabrications that self-referential verification misses.

Rule: When searching for replacement citations after DOI failures (Step 9), always use CrossRef as the lookup mechanism — not a generative search that reconstructs citations from memory. CrossRef is an authoritative DOI registry; a citation that exists in CrossRef with a working DOI is confirmed real. A citation that cannot be found in CrossRef with a working DOI is suspect regardless of how plausible it appears.

Source: June 2026 DOI audit and Step 9 protocol design. The step was written to use CrossRef specifically as an independent verification source.

LR-008 [2026-06-23] — Brief body sections must be revised when their supporting citations are removed

Category: accuracy | structure

Pattern observed: When 26 citations were removed in the June 2026 audit, several briefs retained body text making specific empirical claims that those citations had purported to support. Left uncorrected, the body text would have presented unsupported claims as if they were evidence-grounded. In at least two cases (term-limits-governance.html, recruitment-screening.html), entire body sections had to be removed alongside their references because no supporting citations survived the audit.

Rule: Citation removal triggers a mandatory body-text review. For every citation removed, identify every in-text citation reference in the body that cited that source. For each such reference: either (a) replace the removed citation with a different verified citation that actually supports the same claim, or (b) revise or remove the body text that relied solely on the removed citation. Do not leave the body text citing a source that is no longer in the references section, and do not leave the body text making a claim that no longer has any citation support.

Source: June 2026 DOI audit. Body text review was required after citation removal in 20 affected briefs.

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"

End of guide. This document is authoritative. When in doubt, do not publish — flag for human review.