title: Effective School Board Coach Newsletter -- Content Creation Guide type: content-guide site: effectiveschoolboardcoach updated: 2026-07-08

For AI use and reviewer use: This document is the complete operational specification for generating and reviewing monthly newsletter issues of Effective School Board Coach. Read it in full before generating or approving any issue. Never deviate from parameters defined here. If a question is not answered by this document, do not publish. Flag it for human review.

School systems exist for one reason. That reason is improving student outcomes. Boards exist to keep the system focused on that reason, and the people who coach and facilitate boards exist to help boards do that work well. This newsletter serves those people. Every parameter below is in service of helping a Practitioner help a board improve outcomes for kids.

ESB Language, Terminology & Mechanics (binding)

This section is binding for all generated content. Where anything below conflicts with older instructions in this guide, this section wins. The full standard is esb_writing_style_guide.md in the canonical guides folder.

Mechanics. No em-dashes. Where an em-dash would go, use a spaced double-hyphen ("--"), sparingly, or split the sentence. No en-dashes (use a hyphen, including in ranges like "1-2"). No semicolons in body prose. Straight quotes only. Oxford comma. No horizontal rules.

ESB terminology, never Policy Governance terms. Goals, not Ends. Guardrails, not Executive Limitations. Governing, not Governance Process. Delegation, not Board-Management Delegation. Never describe ESB as built on or adopted from Policy Governance. It is grounded in "principles of a policy-based approach to governance." Never write "SOFG," "Student Outcomes Focused Governance," "Policy Governance," "PG," "Lone Star Governance," or "LSG" (exception: SOFG only when intentionally contrasting with ESB). Use "board chair," not "board president." Use "Practitioner," not "coach," for the certified role (coaching as an activity is fine). Spell out "Any Reasonable Interpretation" (never "ARI"). Use "own conduct," not "own-conduct." Four board-adopted policy types only: Goals, Guardrails, Delegation, Governing (no "Policies About X" category). ESB is prioritized (1-3 policies) in Goals and Guardrails and exhaustive in Delegation and Governing. A Goal is always a student outcome.

Governance language to avoid (describe the specific behavior instead): "micromanage," "rubberstamp," "stay in your lane," "good/bad/right/wrong" as judgment (even affirmatives like "the right framing"), power-over framings, "district"/"school district" (say "school system" in reader-facing content -- a questioner's own words, direct quotes, and operational or data references to a specific entity may keep it), "equity" as a bare term, "achievement gap," politically-coded terms, and "non-essential activities" for what a board could otherwise do.

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Publication name: Effective School Board Coach Domain: effectiveschoolboardcoach.com Site id: effectiveschoolboardcoach Platform: beehiiv (draft staging); a human must approve before beehiiv publishes Content type: Monthly email newsletter Generation cadence: Pipeline runs once per month. The run produces one issue targeted for the next 1st Tuesday of the month. Effective publication cadence: Monthly, published the 1st Tuesday of each month

Purpose: School systems exist to improve student outcomes. Boards keep the system pointed at that purpose. This newsletter helps the people who coach and facilitate boards do that work well. It gives ESB-certified Practitioners, superintendents, board chairs, and governance facilitators practical, ESB-aligned coaching moves delivered as an actionable monthly newsletter. Each issue helps a Practitioner coach a board to distinguish governance from management, anchor its work to student outcomes, and build habits of effective oversight. It does this through Q&A, curated reads, board meeting analysis, and governance resources.

One-sentence purpose: Help the people who coach and facilitate boards move those boards toward more effective governance, through monthly Q&A, curated resources, and real board meeting analysis grounded entirely in the ESB (Effective School Boards) framework.

Target audience: The people who coach, facilitate, and support boards across the United States. That means ESB-certified Practitioners, superintendents who work to develop their boards, board chairs who lead their colleagues, and governance facilitators. Readers are not board members asking how to do their own governance work. They are the people helping a board do that work. They have limited time, real coaching decisions to make, and boards that often confuse governance with management. Some readers are new to coaching boards. Some are seasoned facilitators. The newsletter must be useful to both without talking down to either.

Voice: AJ Crabill's ESB writing standard. Plain, direct, and grounded in why school systems exist. Reading level at or below 10th grade. Short sentences. Uses "--" for parenthetical breaks, never em-dashes. Uses "we recommend" framing, never commands. Calls the ESB-certified professional a "Practitioner." Says "school system," never "district." Uses the Oxford comma, straight quotes, and natural contractions. See the Voice Register section for the full standard.

What distinguishes Effective School Board Coach from sister sites:

The Effective School Board Member (TESBM) coaches individual board members on how to do their own governance work. Effective School Board Coach is one level up. It coaches the people who coach and facilitate boards. TESBM asks "how do I, a board member, do X." This newsletter asks "how do I help a board do X."

effectivegoverningboards.com (EGB) publishes academic policy briefs with citations for governance researchers. This newsletter is practitioner-facing, written in AJ Crabill's plain ESB voice, with no citation apparatus.

schoolboardanswers.com (SBA) is a static Q&A library. This newsletter is a live monthly newsletter with current curated content, real board meeting analysis, and a coaching-of-coaches relationship embedded in tone.

creatingoutcomes.com (CO) covers outcome-focused governance in Q&A format. This newsletter covers every ESB dimension a Practitioner needs, not just outcomes, and adds current governance reads, opportunities, and real meeting analysis.

schoolboardweekly.com (SBW) is a journalism-style newsletter reporting school board news. This newsletter coaches the people who develop boards. SBW reports what boards are doing. This newsletter helps Practitioners shape what boards do.

Effective School Board Coach is ESB-framework-specific and role-specific. Its reader is the person holding the room, not the person in a board seat.

Critical framing to internalize: This newsletter exists inside a coaching relationship, but the reader is a coach. The voice is that of a trusted senior colleague speaking to a Practitioner who wants to help boards better. Every element, from Q&A answers to board meeting analysis, should reinforce that relationship. The reader should finish each issue feeling more capable of coaching a board through its next hard moment.

Content Goals

What a successful issue accomplishes:

Answers 3 to 5 practical coaching and facilitation questions in AJ Crabill's ESB voice, grounded in the ESB framework, at a level of specificity that gives the Practitioner a move they can actually use with a board.

Provides 4 curated reads, listens, or watches that a board coach or facilitator would genuinely find useful and that pass the governance-only filter, with a lean toward facilitation skill and Practitioner development.

Includes a board meeting analysis from a real recent meeting that models what a coach would observe and coach, framed as Coach Celebrates and Coach Recommends.

Surfaces one upcoming webinar or professional development opportunity relevant to people who coach and facilitate boards.

Offers bonus materials (eval PDF, video, ESB resource picks) gated for paid subscribers.

Leaves the reader feeling that reading this month's newsletter made them a better coach of boards.

What a failed issue looks like:

Voice failure: Answers drift from the ESB standard. They use em-dashes, read above a 10th-grade level, command instead of recommend, call the professional a "coach" in the role sense instead of "Practitioner," or say "district" instead of "school system." The plain ESB voice is absent.

Level failure: The answer coaches the board member directly instead of coaching the person who coaches the board. This newsletter is one level up. An answer that reads like it belongs in TESBM has missed its audience.

Governance drift: Q&A answers or reads address curriculum, staff compensation, building projects, or other management topics rather than governance and the coaching of governance. The governance and management line is not actively held.

ESB fidelity failure: Q&A answers contradict or ignore ESB framework principles, or coach a Practitioner to lead a board toward something the ESB framework prohibits, or fail to name an ESB NEVER rule when it applies.

Slop contamination: Answers contain AI-tell phrases, hollow intensifiers, or mechanical constructions that break the ESB voice.

Grounding-opener failure: An answer opens with the tactical problem instead of opening from why school systems and boards exist, then moving to the topic. Every answer grounds in purpose first.

Geographic stagnation: Multiple consecutive issues feature the same state or region for board meeting analysis. The rotation is not honored.

Dedup failure: Q&A questions substantially duplicate questions answered in the past 6 months. Fresh framing on an old issue may be acceptable after 6 or more months. Essentially the same question within 6 months is a failure.

Rough draft not labeled: The assembled newsletter title does not begin with "Rough Draft - ". AJ must edit before publishing. An unlabeled draft could be mistaken for a final issue.

Content Format and Structure

Every issue follows this structure in this order:

1. Q&A Section

3 to 5 Q&A pairs (pipeline generates 5 to 7 candidates; AJ cuts to 3 before publishing)

Each answer: 150 to 250 words

No bullets, no numbered lists, prose only

Optional ACTION ITEMS block at the end of each answer: ACTION ITEMS: [item] | [item] | [item]

Questions are the ones a board coach or facilitator asks. They are drawn from governance-only news filtered through the ESB framework and reframed one level up.

2. Interesting Reads & Listens

4 items (pipeline generates 10 candidates; AJ cuts to 4 before publishing)

Mix: articles (Education Week, The 74, Chalkbeat, NASB, AASA, and similar), podcasts, and videos, with a lean toward facilitation skill, governance coaching, and Practitioner development

Governance-only filter: no curriculum, no staff compensation, no building projects

Each item: title, source, and a short note on why a person who coaches boards would care

3. Board Meeting Analysis

Real, verified school board meeting from the geographic region assigned to this month

Time use analysis: agenda items classified by governance category

Stats table: time breakdown by category

Coach Celebrates and Coach Recommends: 2 to 3 items each, written as what a coach would observe and coach

School system identified by state only in the public newsletter (system name in pipeline data only)

Analysis generated from the actual meeting transcript via audio extraction and LLM analysis

4. Upcoming Opportunities

1 webinar or professional development event relevant to people who coach and facilitate boards

Date is always the 2nd Friday of the next calendar month

Registration link included

5. Bonus Materials (paid subscribers only)

Meeting Analysis PDF (formatted board evaluation document)

Link to the meeting video

Agenda link

Strategic plan link

2 to 3 ESB guidance PDF picks from the catalog

Eval request link for board self-evaluation

6. Free Section

The same four bonus items as plain text without links (for free subscribers)

Delimited by HTML comments for the beehiiv tier logic

Title Format:

Rough Draft - {DayName} {Month} {D} {Year}

Examples:

Rough Draft - Tuesday August 4 2026

Rough Draft - Tuesday September 1 2026

The "Rough Draft - " prefix is mandatory. This is a hard safety requirement. AJ must review and edit each issue before publishing. An issue without this prefix should be treated as a generation error.

Word Counts:

Q&A answer: 150 to 250 words (hard range; flag if outside)

Board Meeting Analysis newsletter summary: about 230 words

Reads and listens descriptions: 1 to 2 sentences each

Opportunity description: 2 to 3 sentences

Forbidden Patterns:

No bullet lists in Q&A answers

No numbered lists in Q&A answers

No academic citations or footnotes

No first-person plural framing that erases the Practitioner (the "we recommend" voice is fine; a lecturing institutional "we" is not)

No coaching the board member directly instead of coaching the person who coaches the board

No em-dashes or en-dashes anywhere; use "--" for parenthetical breaks

No curly or smart quotes; use straight quotes in HTML

No ESB NEVER rule violations (see NEVER Rules below)

No banned ESB language (see NEVER Rules below)

In-Bounds Content

Governance-Only Filter, One Level Up

Every Q&A question, every reads item, and every curated pick must pass the governance-only filter. This newsletter covers what boards should be doing as boards, and how a Practitioner helps a board get there. It does not cover what schools should be doing operationally.

In-bounds coaching and facilitation topics:

Coaching a board on goal setting: how a Practitioner helps a board set, monitor, and report on student outcome goals

Facilitating superintendent evaluation: how a Practitioner helps a board conduct an outcome-focused evaluation and keep evaluation separate from operational second-guessing

Coaching board conduct: helping a board improve decorum, manage conflicts of interest, run executive sessions, and manage public comment as a body

Coaching the board-superintendent relationship: helping the board hold role clarity, use appropriate channels, and respect authority boundaries

Facilitating strategic direction: helping a board establish direction while leaving implementation to the superintendent

Coaching community engagement: helping a board gather community values and communicate its decisions

Facilitating board self-assessment: helping a board evaluate its own governance effectiveness

Practitioner development: facilitation skill, coaching technique, running effective board retreats and work sessions

Coaching a board through transparency and public-records obligations that belong to the board

Facilitating board meeting management: consent agendas, work sessions, special meetings, executive sessions

Coaching a board through elections and onboarding of new members (governance framing only)

Helping a board understand state and federal policy that has direct board governance implications

Borderline, acceptable only with governance framing:

Budget: helping a board hold its role in approving and monitoring the budget at a strategic level, not line-item detail

Staff compensation: only helping a board set compensation policy at a strategic level, not individual salary decisions

Academic programs: only helping a board read and respond to outcome data, not helping a board make instructional decisions

The test for borderline topics: Is this about helping a board do its work as a governing body, or is it about the school system's operations? If it is operations, it is out of bounds. The board sets direction and monitors outcomes. Staff implements. The Practitioner helps the board hold that line.

ESB Framework Alignment

All Q&A content must be grounded in, or at minimum consistent with, the Effective School Boards (ESB) framework. Key ESB principles that appear often in Q&A, framed for a coach:

Student outcome goals: A Practitioner helps a board set specific, measurable goals tied to student learning outcomes, not activities, inputs, or engagement.

Governance and management: The board governs. The superintendent manages. A Practitioner helps a board stay out of directing staff, selecting programs, or making operational calls.

Superintendent evaluation: A Practitioner helps a board evaluate the superintendent on progress toward board-adopted student outcome goals, not on personality, relationships, or activity.

Board-superintendent relationship: A Practitioner helps the board communicate through the superintendent as a body, not around the superintendent through individual member directives.

The board speaks through policy: A Practitioner helps a board act as a body, through votes and policy, not through individual member action.

Community as a source of values, not a decision authority: A Practitioner helps a board gather community input on values and priorities while keeping governance decisions with the board.

Geographic Rotation

Board meeting analysis rotates across three geographic regions month to month. Each monthly issue draws from the next region in the cycle, so successive issues move through all three regions:

Month 1: West and Southwest

Month 2: Midwest and South Central

Month 3: Northeast and Southeast

The cycle repeats after Month 3. No school system should appear in the meeting analysis more than once every 90 days. School systems from the previous two issues in the same region should be avoided. This rotation ensures national coverage over time.

Out-of-Bounds Content

Management Disguised as Governance

This is the single most common failure mode, and it shows up twice for this newsletter. First, the topic itself can be operational. Second, the coaching move can be operational, coaching a Practitioner to help a board do management work. Both are out of bounds. These topics are out of bounds regardless of how they are framed:

Hard out-of-bounds:

Curriculum selection, adoption, or review (instruction is management)

Staff hiring, evaluation, or compensation (personnel is management)

School building projects, construction, facilities decisions (operations)

Program design or implementation (program design is management)

Discipline policy implementation (implementation is management)

Extracurricular activities and sports programs (operations)

Budget line-item decisions (line items are management; total budget adoption is governance)

Test: If the superintendent could make this decision without the board, it is management. If the decision requires board action by law or policy, it may be governance. If a Practitioner is being coached to help a board reach into staff action, it is management disguised as governance.

Non-Governance News

Reads items must pass the same governance-only filter. These are out of bounds for the reads search:

Curriculum debates or book challenges

Staff strikes, contract negotiations, salary disputes

Building projects and bond elections (unless the governance angle is the board's fiduciary role)

Program controversy (unless the controversy involves board conduct specifically)

Student achievement data as a standalone story (unless the story is about how the board is using, or failing to use, the data)

The test: would an education journalist cover this as a story about a board doing its governance job, or about a Practitioner helping a board do that job? If the story is really about what a school is doing, not what a board or its coach is doing, it is out of bounds.

Source and Research Standards

News and Reads Sources

Perplexity (sonar-pro) is the primary source for:

Current governance-only school board news (past ~4 weeks lookback)

Reads, listens, and watches recommendations, with a lean toward facilitation and coaching

Acceptable article sources for curated reads:

Education Week

The 74

Chalkbeat

NASB (National Association of School Boards)

AASA (School Superintendents Association)

RAND Corporation reports

Brookings Education (governance angle only)

State school board association publications

University-based education policy and governance centers

Facilitation and coaching publications with a governance application

Acceptable podcast and video sources:

School board governance podcasts

Education leadership podcasts with a governance angle

Facilitation and coaching podcasts with a governance application

Public-sector governance media

Unacceptable sources:

Opinion or advocacy pieces on curriculum, programs, or political topics

Staff union materials

Individual school system newsletters or blogs

Social media

ESB Source Documents

Q&A answers draw on the ESB source document corpus available to the pipeline. Key documents:

Board Work vs. Superintendent Work

Inputs, Outputs, and Outcomes

Effective Goal Setting Policy

Effective Goal Monitoring

Effective Superintendent Evaluation Process

Q&A answers must be consistent with these documents. When an answer touches a topic these documents cover, it should reflect the ESB framework's position, not a generic governance or coaching position.

Board Meeting Video Verification

The meeting used for the Board Meeting Analysis section must be:

A real, verifiable school board meeting (Granicus or Swagit listing, or YouTube)

Recent (within the past ~4 weeks)

From the geographic region assigned to this month

From a school system not used in the past 90 days

Reachable via URL (verified before transcript extraction)

Meeting verification uses the Granicus or Swagit listing page scrape, with a fallback to known listings. A meeting that cannot be verified as real or recent must not be used. Fall back to a known listing from the same region.

ESB PDF Catalog

2 to 3 ESB guidance PDFs from the static catalog are selected each issue based on relevance to the month's Q&A topics and reads. The selection logic uses DeepSeek Flash to match catalog items to the month's themes. If catalog Drive IDs are unpopulated, the pipeline falls back to two default items.

Grounding Document

Source: Great on Their Behalf (3rd edition) by AJ Crabill Access: Google Drive ID: 1KwiTQKLZlRDnTCzDmHaleeU3IVj_cHbsmA2s6nORdkE (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: c -- pre-draft AND post-draft

Pre-draft: Before drafting, read the relevant sections of the grounding document. Use it to calibrate frame, vocabulary, and core claims before writing begins. The book is the source of truth for what the ESB framework holds and for how a Practitioner should help a board.

Post-draft: After completing all quality checks, verify the finished piece against the grounding doc. Confirm no claims contradict it, vocabulary is consistent, and the piece would not confuse a reader who knows the book well. This is done as Section 8h.

Voice Register

Register: ajc-short-ESB-standard -- short, plain sentences, reading level at or below 10th grade, grounded in why school systems and boards exist.

The voice gate checks the AJ Crabill ESB writing standard. Threshold: score at or above 0.90. The gate scores these properties:

Grounding opener. Every answer opens from why school systems and boards exist, which is improving student outcomes, and then moves to the topic. It does not open with the tactical problem.

Reading level at or below 10th grade. Short, plain sentences. If a sentence is hard to read out loud in one breath, it is too long.

"--" for parenthetical breaks, never em-dashes. When setting off a parenthetical thought -- like this -- use "--". Never use an em-dash or an en-dash. There must be zero em-dash characters anywhere.

"we recommend" framing, never commanding. The voice recommends. It does not order. Say "we recommend the Practitioner name the pattern" rather than "name the pattern."

"Practitioner" not "coach" as the role word. The brand name is "Effective School Board Coach." The internal role word for the ESB-certified professional is "Practitioner." Use "Practitioner" or "facilitator" for the person, not "coach" as a job title.

"school system" not "district." Always.

Oxford comma, straight quotes, natural contractions. Use them consistently.

The ESB Voice, One Level Up

This newsletter uses AJ Crabill's plain ESB voice, and it points that voice at the person who coaches boards. Every Q&A answer is written as if a trusted senior ESB colleague is speaking to a Practitioner who asked a good-faith coaching question. The voice has these properties:

Purpose first. It grounds in why the work matters -- student outcomes -- before it gets tactical.

Plain and direct. Short sentences. Common words. No jargon for its own sake.

One level up. It coaches the coach. It gives the Practitioner a move to use with a board, not a move for a board member to use on their own governance.

Recommends, does not command. "We recommend" is the default frame.

Consistent ESB vocabulary. "Practitioner," "school system," "student outcome goals," "governance and management." Never the banned terms in the NEVER Rules section.

Grounding-Opener Patterns

Every Q&A answer must open by grounding in purpose, then move to the coaching question. The opener connects the tactical question back to why boards exist. Approved opener patterns (open with one of these or a close variant):

"School systems exist to improve student outcomes, and a board that drifts into operations loses time it owes to that work. So when you coach a board that keeps drifting, we recommend..."

"The point of a board is to keep the system focused on student outcomes. That is the frame to bring back to a chair who dominates the room..."

"Boards exist to serve students, not to run the building. When a board sets an activity goal instead of a student-outcome goal, the first move is to reconnect the board to why it is there..."

"Every board meeting is time that belongs to students. So the question of how to help a board use its time is really a question about outcomes..."

"Before we talk tactics, it helps to remember why the board is in the room at all. The board is there so students learn more..."

Why the grounding opener is required: Most governance mistakes happen because a board has lost sight of why it exists. A Practitioner's first job is to reconnect the board to purpose. An answer that jumps straight to tactics without grounding in purpose is not ESB coaching. It is generic facilitation advice.

Mechanical Voice Rules

These are enforced by the pre-gate scanner before the LLM quality gates run.

Hard character bans (zero tolerance):

Em-dash character. Any em-dash is a hard fail. Use "--".

En-dash character. Any en-dash is a hard fail. Use "--".

Curly or smart quotes. Use straight quotes.

AI-tell phrases that trigger a rewrite flag:

"delve into"

"in conclusion" or "in summary" as answer openers

"it is worth noting that"

"it is important to note"

"this underscores" or "this highlights"

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

This section has two parts. Part A is the set of ESB governance prohibitions. Part B is the set of ESB language bans. Both are hard. A Q&A answer must never coach a Practitioner to lead a board into a Part A violation, and must actively redirect if a question assumes one is acceptable. A Q&A answer must never use a Part B banned term.

Part A -- ESB Governance NEVER Rules

These positions appear in ESB source documents as explicit prohibitions. Answers must never coach a Practitioner to help a board do these things:

NEVER coach a board to direct staff. Describe the behavior instead: board members do not give instructions to staff other than the superintendent. A Practitioner helps the board route its direction through the superintendent as a body.

NEVER coach a board into operational decisions. Describe the behavior instead: making operational calls, selecting programs, or second-guessing implementation choices. A Practitioner helps the board stay in governance and leave implementation to staff.

NEVER coach individual board member action. Individual board members have no governance authority. Authority rests with the board as a body, through votes. A Practitioner helps individual members act through the board, not around it.

NEVER coach a board to evaluate the superintendent on non-outcome criteria. Character, likability, effort, or relationship quality are not legitimate evaluation criteria. A Practitioner helps the board evaluate on progress toward adopted student outcome goals.

NEVER coach a board to set activity or input goals. Board goals must connect to student learning outcomes, not program activities or resource deployment. A Practitioner helps the board convert activity goals into outcome goals.

When a question implicitly assumes one of these is okay, the answer must ground in purpose and redirect before answering. The answer cannot validate the false premise. Note that describing a behavior is required in place of the banned label "micromanage," which is covered in Part B.

Part B -- ESB Language Bans (Hard)

These terms are banned outright. Do not use them anywhere in any answer or in any newsletter content. Use the replacement instead.

"micromanage" and "micromanaging" -- banned. Describe the behavior. Say the board is "reaching into operations" or "second-guessing implementation" instead of naming it with the banned word.

"rubber-stamp" and "rubberstamping" -- banned. Describe the behavior. Say the board is "approving without review" or "not doing its own analysis" instead.

"stay in your lane" -- banned. Describe the behavior. Say "keep the board focused on governance work" or "help the board hold its role" instead.

good, bad, right, wrong as moral judgment -- banned. Use effective or ineffective, aligned or misaligned. Say a practice is "ineffective" or "misaligned with student outcomes," not "bad" or "wrong."

"district" -- banned. Use "school system."

"achievement gap," "equity," and coded DEI terms -- banned. Describe the gap with data instead. Say "the difference in reading scores between student groups" and name the numbers, not the coded term.

"elected" board -- banned as a qualifier. Say "any board" or "the board." Not every board is elected, and the ESB framework applies to any board.

power-over framings -- banned. Do not frame the board as exercising power over staff, or the Practitioner as exercising power over the board. Frame the work as service on behalf of students and as helping a board serve.

A single use of a Part B term is a hard fail. The pre-gate scanner blocks these terms before the LLM gates run.

Generation Process

Before beginning Step 1, complete the grounding doc pre-draft alignment per the Grounding Document section above.

Step 1 -- Video Discovery

Find a real, verified school board meeting from the region assigned to this month.

Phase A: Query Perplexity for the school system's Granicus or Swagit listing page (not a specific video URL; the listing page is stable).

Phase B: Scrape the listing page to extract the most recent non-cancelled clip URL. Verify the URL is reachable.

Fallback: use a known Granicus or Swagit listing from the KNOWN_LISTINGS regional dict.

Check the geographic log: avoid school systems used in the past 90 days.

Record the successful school system in the geographic log.

Step 1b -- School System Link Collection

Run three parallel searches for the selected meeting:

Agenda URL (scraped from the Granicus listing page near the clip ID)

Strategic plan URL (Perplexity search for the school system's strategic plan document)

YouTube URL (Perplexity search for a YouTube recording of the same meeting)

Returns: agenda_url, strategic_plan_url, strategic_plan_title, youtube_url, video_url.

Step 1c -- Eval PDF Upload

Fetch the eval PDF from esby-portal (which converts the eval docx on the fly) and push it to schoolboardreview.com/evals/ via a git commit. Returns eval_pdf_url.

Step 2 -- Time Use Analysis

Extract the meeting transcript via yt-dlp and faster-whisper audio extraction. Run a 3-stage LLM analysis:

Extract agenda items from the transcript.

Classify each item by governance category (using the Time Use Classification Guide).

Compute totals and generate coaching reflections (Coach Celebrates and Coach Recommends).

Generate an approximately 230-word HTML summary for the newsletter using DeepSeek Flash:

<h3>Board Meeting Analysis</h3>

Stats table (time by category)

Coach Celebrates section, written as what a coach would observe and affirm

Coach Recommends section, written as what a coach would suggest the board try next

The school system name is replaced by the state name only in the public newsletter.

Classification accuracy is critical. A common misclassification error is categorizing activities as goal-focused when they are not. Goal-focused means the board is reviewing student learning outcome data against its adopted goals. A board discussing attendance reports, benchmark data, or program updates is not doing goal-focused work unless those items are tied to explicit adopted student outcome goals. Consult the Time Use Classification Guide for all close calls.

Step 3 -- News Search

Query Perplexity for 20 governance-only school board news stories from the past ~4 weeks.

Strict governance-only filter (must apply, cannot be relaxed):

In-bounds: board policy, goal setting, superintendent evaluations, board conduct, transparency, community engagement policy, strategic planning, board elections, and the board-superintendent relationship

Out-of-bounds: curriculum debates, staff salaries, building projects, program implementation debates, and student activity stories

Fallback: if Perplexity fails, use DeepSeek Flash to synthesize governance news from its training data (clearly marked as non-current in pipeline data).

Step 4 -- Question Refinement

Transform news items into actionable coaching and facilitation questions phrased as what a person who coaches or facilitates boards might ask. This is the one-level-up move. Batch in groups of 10 using DeepSeek Flash.

Prioritize questions that reference states in this month's geographic region (the same region as the board meeting analysis). Return up to 15 candidate questions.

Each question should be:

Specific enough to have a real answer

Phrased from the Practitioner's or facilitator's perspective. Examples: "How do I coach a board that keeps drifting into operations?" "How do I help a chair who dominates the discussion?" "What do I do when a board sets activity goals instead of student-outcome goals?" "How do I facilitate a board through a superintendent evaluation without letting it slide into personality?"

Actually about helping a board do governance, not about what a school does operationally, and not about a board member doing their own governance work alone

Step 5 -- Deduplication

Check candidates against the past 12 months of published Q&As in the Effective School Board Coach database.

Dedup rules:

Same core coaching or governance issue within the past 6 months: skip.

Same core issue 6 to 12 months ago: skip unless the new question has a meaningfully different angle (new law, new context, a different aspect of the same issue).

Questions from 12 or more months ago are eligible for fresh treatment.

Use DeepSeek Flash for semantic similarity assessment, not just string matching. Return up to 7 non-duplicate questions.

Step 6 -- Q&A Writing

Write answers for the surviving candidate questions. Apply the full quality gate protocol (see Site-Specific Checks in the Quality Checks section below).

Model sequence: MiniMax M2.5 (attempt 1) → Claude Opus 4.8 (attempts 2 and 3, with accumulated gate feedback).

Enforce for each answer:

150 to 250 words

Opens with a grounding opener (see Voice Register section): purpose first, then the coaching move

Coaches the coach, one level up, not the board member directly

No bullets, no numbered lists

"--" for parentheticals, never em-dashes; straight quotes; contractions; Oxford comma

"we recommend" framing, never commanding

"Practitioner" not "coach" as the role word; "school system" not "district"

No Part A or Part B NEVER rule violations

Optional ACTION ITEMS block: ACTION ITEMS: [item] | [item] | [item]

The pipeline writes 5 to 7 answers. AJ cuts to 3 before publishing.

Step 7 -- Reads, Listens, Watches

Query Perplexity for 10 governance-related reads, listens, and watches, with a lean toward facilitation skill, governance coaching, and Practitioner development. Avoid the region used for the board meeting analysis this month.

Mix requirements:

4 to 5 articles from governance-approved sources

2 to 3 podcasts

2 to 3 videos

All items pass the governance-only filter (see Site Context section). All items are from the current month or recent past, not evergreen library items.

Fallback: DeepSeek Flash synthesis if Perplexity is unavailable.

The pipeline generates 10. AJ cuts to 4 before publishing.

Step 8 -- ESB PDF Selection

Select 1 to 3 ESB guidance PDFs from the static catalog most relevant to this month's Q&A topics and reads. Use DeepSeek Flash to match catalog items to the month's themes.

The catalog includes:

Board Work vs. Superintendent Work

Effective Goal Setting Policy

Effective Goal Monitoring

Effective Superintendent Evaluation Process

Inputs, Outputs, and Outcomes

Other ESB source documents (the catalog is populated after indexing)

If selection fails or Drive IDs are unpopulated, fall back to two default items.

Step 9 -- Webinar Opportunity

Generate one webinar or professional development opportunity relevant to people who coach and facilitate boards, based on the month's hottest Q&A or reads topic. Use DeepSeek Flash.

Date: always the 2nd Friday of the next calendar month (computed at runtime). Fallback: a goal-monitoring facilitation webinar.

Step 10 -- Assembly

Assemble the full newsletter HTML in this order:

Q&A section (5 to 7 Q&As, with a note to AJ to cut to 3 before publishing)

Interesting Reads & Listens (10 candidates, with a note to AJ to cut to 4)

Board Meeting Analysis (Step 2 HTML, state name only for the school system)

Upcoming Opportunities (webinar with a registration link)

Bonus Materials paid section (eval PDF, video, agenda, strategic plan, ESB PDF picks, eval request link)

Free section (the same four items as plain text, no links, delimited by HTML comments)

Title: Rough Draft - {DayName} {Month} {D} {Year}

Step 11 -- Queue

Save the assembled newsletter to the esby-portal approval queue (newsletter_drafts table in the esby-portal database) with source = "effectiveschoolboardcoach" and status = pending. Scheduled for the next 1st Tuesday of the month. Also record the run in the Effective School Board Coach tracking data.

Hard safety check: the title must start with "Rough Draft - ". If this check fails, abort and log the error. Do not save a newsletter without this prefix.

The pipeline does NOT post to beehiiv. It does NOT publish automatically. Human approval is required.

Quality Checks

Quality Check Failure Protocol

This protocol governs every check in Section 8 (8a through 8h, including all site-specific gates in 8d).

On any failure at any check:

Identify the specific violation. Which rule, which tier, which gate, and exactly what was wrong.

Revise only the affected portion of the draft to address that specific failure.

Re-run the check that failed (not the full Section 8, just the failing check).

Track the attempt count per check.

Retry limit: 3 revision-and-retry cycles per check. If a check passes on retry, continue to the next check normally.

Ultimate Failure: if a check still fails after 3 retries, declare an ULTIMATE FAILURE for that check. Stop all further quality checks immediately. Do not publish, commit, or submit the draft. Proceed to ultimate failure reporting (below), then preserve the draft and full failure log, including stage name, attempt count, the nature of each failure, and each revision attempt, in a dated file for AJ's review.

Ultimate Failure Reporting -- Effective School Board Coach: Do NOT send to beehiiv or advance for AJ approval. Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (effectiveschoolboardcoach), question or topic, which gate or check failed, attempt count, failure details, and the draft. Mark status as FAILED. AJ will review and decide whether to intervene manually.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Satisfied by the Pre-Gate plus Gate 3 in Section 8d. See the site-specific checks below. The Pre-Gate mechanical scan catches regex-flagged AI-tell phrases, the hard character bans (em-dash, en-dash, curly quotes), and the Part B language bans before the LLM gates run. Gate 3 LLM slop and AI-tell scan catches remaining AI-tell patterns not caught mechanically. Together these two gates constitute the full anti-slop requirement.

8b. Voice Check

Satisfied by Gate 1 in Section 8d. Gate 1 runs a full voice score against the ajc-short-ESB-standard profile, including the grounding opener, reading level at or below 10th grade, "--" not em-dash usage, "we recommend" framing, "Practitioner" not "coach" as the role word, "school system" not "district," the NEVER rules, and rhythm. Threshold: score at or above 0.90.

8c. ESB Governance Language Check

ESB Governance Language Check

This is a hard gate. Every Q&A answer is scanned against the ESB governance-language standard (Part B of the NEVER Rules). Reference: Google Drive ID 13O3_qNxtRVHsTDyDMXdotPLOhIMTyRe0J_1yQ9tzhOQ. The mechanical pre-gate flags these terms before the LLM gates run; this check is the LLM backstop that also catches paraphrased or implied violations, including violations inside the coaching move the answer recommends.

Banned phrases -- any occurrence fails:

"micromanage" / "micromanaging" -> describe the behavior instead (is the board reaching into operations, or directing implementation the superintendent owns?)

"rubberstamping" / "rubber stamp" -> describe whether the board exercised informed judgment against its adopted student outcome goals

"stay in your lane" -> reference the board and superintendent role distinction in policy terms

"good" / "bad" / "right" / "wrong" as a moral judgment of board behavior -> frame around effective or ineffective, aligned or misaligned with student outcome goals

"elected" as a modifier for the board or its members -> say "the board" or "any board"; governance duties do not depend on how members arrived

Banned framings -- restructure any instance found:

Board as passive recipient: any suggestion the board should simply receive, defer to, or accept the superintendent's work without its own judgment

Board as obstacle: any framing that board involvement is a problem to route around

Expertise as authority: any framing that professional staff hold more legitimate authority than the board, or that a Practitioner should coach a board to defer because staff "know better"

Conflict as dysfunction: any framing that disagreement among board members is inherently a failure rather than the normal work of a governing body

Efficiency as primary goal: any framing that speed or a short meeting is the board's main objective

Power over people: any "power over" framing of the board's authority; the board's authority is exercised through policy and monitoring, not over individuals

Education terms -- replace with specific language:

"school district" / "district" -> "school system"

"equity" -> describe the specific gap or outcome with data (reserve the term only for a direct quotation of a statute or policy)

"achievement gap" -> describe the system's outcome shortfall directly, with specific data

Politically-coded terms -> describe the specific concept: DEI, anti-racist, woke, "parents' rights" as a contested framing, SEL as a wedge term

Fails if: any banned phrase or term appears, or any banned framing is present in the answer or in the coaching move it recommends. On failure, apply the Quality Check Failure Protocol: rewrite the specific passage and re-run this check.

8d. Site-Specific Checks

Effective School Board Coach uses a four-gate quality system with a mechanical pre-gate scan. All gates apply to Q&A answers. Run the pre-gate scan first, then all four gates.

Pre-Gate: Mechanical Slop and Language-Ban Scan

Run a regex-based scan against the Q&A bank before submitting to the LLM gates.

First, the hard character and language bans (any hit is a hard fail, not a flag):

Em-dash character present: hard fail. Replace with "--".

En-dash character present: hard fail. Replace with "--".

Curly or smart quote present: hard fail. Replace with straight quotes.

Any Part B banned term present ("micromanage," "micromanaging," "rubber-stamp," "rubberstamping," "stay in your lane," "district," "achievement gap," "equity," coded DEI terms, "elected" as a board qualifier, or a power-over framing): hard fail. Rewrite per the Part B replacement.

The word "coach" used as the role word for the ESB professional (instead of "Practitioner" or "facilitator"): flag for rewrite. The brand name "Effective School Board Coach" is allowed; "the coach recommends" as a job-title reference is not.

Then flag AI-tell phrases (see Voice Register -- Mechanical Voice Rules). Any flagged answer proceeds to the LLM gates with the flag noted. If the LLM gates score it highly despite the flagged phrase, a human reviewer makes the final call on that specific phrase.

Also run the following cleanup checks at pre-gate before the LLM gates:

Check: Grounding Opener Presence Verify every Q&A answer opens by grounding in why school systems and boards exist, then moves to the coaching question (see Voice Register section). If an answer opens with the tactical problem instead of grounding in purpose, it has failed this check regardless of the quality of the rest of the answer. Flag for rewrite.

Check: One-Level-Up Presence Verify every Q&A answer coaches the person who coaches the board, not the board member directly. If the answer reads like advice to a board member about their own governance work, it has failed this check. Flag for rewrite so the answer gives the Practitioner a move to use with a board.

Check: List Detection Flag any Q&A answer containing:

A bullet-point list

A numbered list

A dashed list (using hyphens as list markers)

A lettered list (a. b. c.)

Replace with prose. Lists are a hard fail in Q&A answers.

Check: Hollow Intensifier Scan Flag all instances of: "crucial," "critical," "essential," "vital," "fundamental," "robust," "comprehensive," "transformative," "impactful" used decoratively. Replace with specific language. Ask what is actually being said, and say that instead.

Check: Action Items Formatting If action items are present, verify the format: ACTION ITEMS: [item] | [item] | [item]. No line breaks within the action items block. No bullets. Each item is a short, concrete move the Practitioner can make with a board. Not observations. Moves.

Gate 1: Voice Score (≥ 0.90)

An LLM evaluator assesses whether the answer sounds like AJ Crabill's plain ESB voice, pointed one level up at a Practitioner. This gate constitutes the full voice check requirement (see Section 8b). It penalizes:

Bullet lists or numbered lists (hard fail if present)

Any em-dash or en-dash character (hard fail if present)

Reading level above 10th grade

Missing or weak grounding opener (does not open from why school systems and boards exist)

Commanding tone instead of "we recommend" framing

Use of "coach" as the role word instead of "Practitioner" or "facilitator"

Use of "district" instead of "school system"

Any Part B banned term

Failure to honor the Part A NEVER rules in tone

Sentence rhythms that run long and academic instead of short and plain

An answer that coaches the board member directly instead of coaching the person who coaches the board

An answer that opens with the tactical problem, commands instead of recommends, or coaches the wrong audience will fail this gate regardless of the accuracy of the advice. Threshold: score at or above 0.90.

Voice Consistency (across the Q&A bank): Read the Q&A bank as a set, not as individual items. Ask whether this sounds like the same senior ESB voice speaking in each answer. If one answer is notably more formal, more casual, or more commanding than the others, flag it for tone normalization.

Gate 2: ESB Fidelity

An LLM evaluator checks the answer against ESB framework principles and the NEVER rules. Hard fails:

The answer coaches a Practitioner to help a board take individual member action that bypasses the superintendent

The answer coaches a Practitioner to help a board reach into staff work or second-guess implementation

The answer frames activity-based goals as acceptable board goals

The answer suggests the superintendent should be evaluated on criteria other than progress toward student outcome goals

The answer does not redirect when the question assumes an ESB NEVER rule is acceptable

The answer is technically correct but fails to connect the coaching move back to why it matters for student outcomes

An answer can be factually accurate and still fail ESB fidelity if it answers in a framework-agnostic way, or if it forgets to ground in purpose.

Site-Specific ESB Check A -- Geographic Reference Accuracy: If a Q&A answer references a specific state, law, or policy context, verify that the reference is accurate. State-specific governance laws vary. Inaccurate state references are a credibility failure.

Site-Specific ESB Check B -- Board vs. Member Distinction: Flag any answer that conflates "the board" (a collective body that speaks through votes) with "a board member" (an individual with no independent authority). A Practitioner helps individual members act through the board, not around it. Common error: coaching a Practitioner to have a member contact the superintendent directly as an individual is a governance error; coaching a member to raise the item at a board meeting is fine.

Site-Specific ESB Check C -- ESB NEVER Rule Compliance: Flag any Q&A answer that, on a plain reading, would leave a Practitioner thinking:

It is acceptable to coach a board to direct staff other than the superintendent

Individual board members have authority to act alone

Superintendents should be evaluated on activity, effort, or likability

Board goals about programs or activities are acceptable substitutes for student outcome goals

These are ESB NEVER rule violations. Flag and rewrite to correct.

Site-Specific ESB Check D -- Language-Ban Compliance: Confirm no Part B banned term survived the pre-gate. Confirm the answer describes a behavior in place of the banned label (for example, "reaching into operations" in place of the banned "micromanage"). Confirm the answer uses effective or ineffective and aligned or misaligned in place of moral good, bad, right, or wrong. Any survivor is a hard fail.

Gate 3: Slop and AI-Tell Scan

An LLM evaluator identifies remaining AI-tell phrases not caught by the pre-gate and assesses whether the answer sounds like a machine trying to sound authoritative. This gate, together with the Pre-Gate mechanical scan, satisfies the full anti-slop requirement (see Section 8a). Specific targets:

Generic governance or facilitation platitudes with no specificity

Vague claims about "research" or "evidence" without any specific grounding

Sentences that are structurally correct but semantically empty

Repetition of the question's premise back to the reader as if it were an insight

Gate 4: Source Document Fidelity

An LLM evaluator checks whether the answer is consistent with the ESB source documents available in the pipeline (Board Work vs. Superintendent Work, Inputs-Outputs-Outcomes, Effective Goal Monitoring, Effective Goal Setting, Effective Superintendent Evaluation Process, and others). Specific checks:

The answer does not contradict ESB source doc definitions

The answer correctly applies the governance and management distinction as defined in ESB sources

If the answer cites or implies an ESB principle, it states that principle correctly

Model Sequence for Gate Failures:

First attempt: MiniMax M2.5

Second attempt (if Gate 1 or 2 fails): Claude Opus 4.8, with Gate 1 and Gate 2 failure feedback woven into the prompt

Third attempt (if the second attempt fails): Claude Opus 4.8, with all gate feedback from both prior attempts accumulated in the prompt

After three failed attempts: the question is dropped from the candidate pool for this issue. A note is added to the quality log.

The quality score threshold is all four gates at passing level. An answer that passes Gates 2, 3, and 4 but fails Gate 1 (voice) is not publishable. The ESB voice is foundational to this newsletter.

8e. Primary Red-Team (the configured write model)

Primary Red-Team -- Single Adversarial Pass (the configured write model)

Run the draft through the configured write model with an adversarial prompt instructing it to:

Challenge every major coaching claim: is this move actually supported? Where could a knowledgeable Practitioner push back?

Find logical gaps: does the coaching advice hold together from purpose to move?

Flag unsupported assertions: any claim that needs grounding and does not have it

Identify reader-hostile moments: where would a skeptical Practitioner stop reading?

Surface structural problems: does the answer earn its recommendation or merely assert it?

Fails if: any major claim is undefended; the argument contains a logical gap; or more than 2 reader-hostile moments are identified. Revise and re-run before proceeding.

8f. Council Red-Team (multi-LLM panel)

Council Red-Team -- Multi-LLM Adversarial Panel

Spawn these 4 free OpenRouter models in parallel, each with a distinct adversarial persona. Apply the Section 8 failure protocol: if the council fails, revise the flagged section or sections, re-run only the personas that flagged a problem (not all 4), up to 3 retries.

Persona prompts:

Skeptical Practitioner (Gemini): "You are reviewing this piece as an ESB-certified Practitioner who has coached a lot of boards and watched a lot of governance advice fail in the room. Would this coaching move actually work with a real board? Is it grounded in how boards actually behave, or does it assume conditions that rarely exist? List every claim that feels untested or idealistic, quoting the exact passage."

Hostile Reader (Llama): "You are looking for something to object to. What is the weakest claim? What is most poorly supported? What would make you stop reading? Be specific. Quote the exact passage and state the exact objection."

Rival Author (DeepSeek): "Is this saying anything the field of governance coaching does not already know? Is there a genuinely useful move here, or is this a repackaging of received wisdom in different words? What would need to change for this piece to be worth reading over existing work?"

Editor (Qwen): "Is the argument tight? Are there redundant sections? Does the structure serve the argument or fight it? Does it open by grounding in purpose the way the ESB standard requires? Does the recommendation land? Would you accept this piece as submitted, or send it back with notes?"

Passing criteria: 3 of 4 models must find no major problems. If 2 or more models independently flag the same specific passage or claim, that passage fails regardless of the overall score.

8g. Existential Voice Test

Existential Voice Test

Ask: "Would this content appear unchanged on another governance education site, facilitation blog, or AI-generated newsletter?"

If yes, the voice is not distinctive enough. The piece is competent but not AJ's ESB voice. Identify 2 to 3 specific passages that read generic and revise them until they could not have been written by anyone else working in the ESB frame.

Indicators of failure:

Opens with a general statement rather than grounding in why school systems and boards exist

Commands or hedges ("it's important to consider") instead of recommending with a clear frame

Uses "district" or "coach" as the role word, or reads above a 10th-grade level

Could be published without attribution and no one would notice the absence of a byline

This test is subjective. If you would not be surprised to see this exact piece on a competitor site, it fails.

8h. Grounding Doc Post-Draft Alignment (usage c)

Grounding Doc Post-Draft Alignment

Access the grounding document (Great on Their Behalf, 3rd edition, by AJ Crabill) and verify:

No claim in the finished piece directly contradicts a claim or framework in the grounding doc.

Key terminology is consistent. If the book uses a specific term, the piece uses it the same way. This includes "school system," "Practitioner," "student outcome goals," and "governance and management."

A reader who knows the grounding doc well would not be confused or jarred by this piece.

The piece reinforces the grounding doc's core intellectual framework rather than drifting from it.

This is not a citation check. The piece does not need to cite the grounding doc. It is an alignment check: does the piece fit within the same intellectual ecosystem?

Fails if: any direct contradiction is found; any significant terminology drift exists; or the piece would confuse a reader who knows the book.

Technical Filing

Pre-Publish Checklist (Pipeline)

Title begins with "Rough Draft - " -- hard safety gate; abort if missing

All Q&A answers passed all 4 quality gates

Zero em-dash and en-dash characters anywhere in the assembled HTML

Zero Part B banned terms anywhere in the assembled HTML

Board Meeting Analysis uses the state name only (no school system name in public content)

Board meeting URL verified as reachable before transcript extraction

Geographic log updated with this run's school system

Scheduled_for date is the next 1st Tuesday of the month (not the current run date)

Saved to newsletter_drafts with source = "effectiveschoolboardcoach" and status pending

Recorded in the Effective School Board Coach tracking data with status queued

Does NOT post to beehiiv -- human approval required

Reviewer Checklist (Admin Portal)

When reviewing an Effective School Board Coach draft in the content approval portal, check:

Title starts with "Rough Draft - " followed by the correct date format

Q&A answers open by grounding in why school systems and boards exist, then move to the coaching move

Q&A answers coach the person who coaches the board, not the board member directly

Answers recommend ("we recommend"), they do not command

Answers use "Practitioner" or "facilitator," never "coach" as the role word

Answers say "school system," never "district"

No em-dash or en-dash characters anywhere; "--" is used for parentheticals

No Part B banned terms anywhere

No Q&A answer contains bullet lists or numbered lists

Board Meeting Analysis identifies only the state, not the school system name

Reads and listens items are governance-related and lean toward facilitation and coaching (not curriculum, not staff issues)

No ESB NEVER rules are violated in any Q&A answer

Webinar opportunity date is the 2nd Friday of the next month

Bonus materials section is present and properly gated

Free section is present and delimited

Approval Triggers Beehiiv Upload

When a reviewer approves a newsletter draft in the admin portal:

The draft content is uploaded to beehiiv as a draft post (not immediately sent).

The upload targets this newsletter's OWN beehiiv publication, using its own BEEHIIV_PUB_ID. This publication is distinct from TESBM's. The upload is per-source: the pipeline reads source = "effectiveschoolboardcoach" on the draft and routes it to the Effective School Board Coach publication, not to any sister publication.

AJ must then log in to beehiiv to:

Edit down Q&As to 3 before publishing

Edit down reads to 4 before publishing

Review and finalize the complete issue

Schedule or manually trigger the send

Approval in the portal does not equal a published newsletter. It means this draft is ready for AJ's final edit in beehiiv.

beehiiv Technical Requirements

Publication: the Effective School Board Coach beehiiv publication (its own BEEHIIV_PUB_ID, distinct from TESBM's and every sister source)

Status on upload: draft

Audience: free (beehiiv handles tier gating for the paid content sections)

Authors: empty array (the newsletter is unattributed in beehiiv)

Content format: content_html

Ongoing Content Integrity

Deduplication Policy

The Effective School Board Coach Q&A bank is checked against 12 months of published questions before each issue. The dedup policy:

0 to 6 months: Same core coaching or governance issue: skip. Even if the framing is slightly different, the Practitioner who read the prior answer will not benefit from this one.

6 to 12 months: Same core issue: skip unless there is a meaningfully new angle (new legislation, new ESB guidance, a coaching situation that was not the focus of the earlier answer).

12 or more months: Eligible for fresh treatment. Governance principles endure, but the reader base turns over. A Practitioner who was not reading the newsletter 12 months ago needs access to foundational ESB coaching moves.

Dedup is done semantically (LLM-assessed similarity), not by keyword matching. Two questions that ask the same thing in different words should be caught. Two questions that use the same words but address different coaching situations should not be flagged.

Geographic Rotation

Board meeting analysis must rotate across all three regions. Monitor the geographic log to ensure:

No region appears more than twice in five consecutive issues

No single state appears in back-to-back issues

No single school system appears within 90 days

If a region's Granicus or Swagit listings are exhausted or unavailable, use the known-listings fallback. If the fallback fails, flag for human selection of a meeting.

Issue Quality Tracking

Track per-issue:

Number of Q&A candidates generated

Number passing all 4 gates

Number of gate failures by gate number

Models used for each Q&A (which attempt succeeded)

Whether the board meeting video was verified or fell back to a known listing

Whether Perplexity was available (versus DeepSeek fallback used)

Gate 2 (ESB fidelity) failures accumulate signal about prompt weaknesses. High Gate 2 failure rates on a particular coaching topic type indicate the writing prompts need calibration.

Prompt Maintenance

When gate failures cluster around a particular topic type or framing, the generation prompts should be updated to address the pattern. For example: if Gate 1 repeatedly fails because answers command instead of recommend, the Step 6 writing prompt needs to front-load the "we recommend" frame. If Gate 2 repeatedly fails because answers coach the board member directly instead of the Practitioner, the Step 4 refinement prompt needs to reinforce the one-level-up framing before questions are written.

Prompt updates should be documented with the date, the failure pattern they address, and the change made.

Content Update Policy

Effective School Board Coach is a current-events-grounded newsletter, not an evergreen library. Content does not require an update once published. Each issue is of its moment. The Q&A dedup policy handles freshness across issues.

However, if ESB framework positions change (new ESB source documents, revised guidance), the Step 6 writing prompts must be updated before the next generation run, and the quality gates must be recalibrated to reflect the updated framework.

Independent Review Protocol

Approval Flow: AJ must approve before beehiiv send.

The pipeline does not post to beehiiv automatically. The assembled draft is saved to the esby-portal approval queue with source = "effectiveschoolboardcoach" and status pending. Approval in the portal uploads the draft to beehiiv as a draft post -- not a sent newsletter -- to this newsletter's own beehiiv publication. AJ must then log in to beehiiv to make final edits (cutting Q&As to 3, cutting reads to 4, reviewing the full issue) and schedule or manually trigger the send.

No issue is published without AJ's explicit action in beehiiv.

Learned Rules

(No site-specific learned rules recorded yet. Rules are appended here as AJ edits diverge from submitted drafts.)

Learned Rules -- Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version.

Identify every substantive edit AJ made. Not typos. Look for content changes, framing changes, word choice changes, and structural changes.

For each cluster of related edits, derive the governing rule.

Append the rule using this format:

Rule [N] -- [Short label] (added [date]) Rule: [The rule stated in one sentence -- what to do or not do] Why: [What the original got wrong -- what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"

End of guide. This document is authoritative for Effective School Board Coach newsletter content generation and review. When in doubt, do not publish -- flag for human review.