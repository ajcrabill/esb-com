title: "School Board Report — Content Generation Guide" type: content-guide site: schoolboardreport.com updated: 2026-07-08

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

Domain: schoolboardreport.com Content type: Analysis articles Publication frequency: 3 articles per week — Monday, Wednesday, Friday Jekyll layout: article Byline: By School Board Report Staff (injected by layout template — do NOT include in content body)

One-Sentence Purpose

School Board Report publishes journalistic analysis of school board governance patterns, incidents, and structural dynamics — not news reporting, not practitioner advice, but rigorous analytical frames that help readers understand what board behavior means and why it matters.

Target Audience

Readers are sophisticated governance stakeholders: sitting board members, current and aspiring superintendents, governance advocates, education policy researchers, foundation program officers focused on governance, and well-informed community members who follow board affairs closely. This audience can handle complexity, nuance, and structural argument. They do not need to be told what a school board is. They are not looking for tips or checklists. They want analytical frames they can apply to what they observe in their own districts or the field generally.

Do not write down to this audience. Do not over-explain basic concepts. Assume the reader knows how governance works and is here for deeper analysis.

Voice Specification

The voice is journalistic, analytical, and institutional. Specific requirements:

Third person throughout. No "you" directed at the reader. No "we." The writer is an observing analyst, not a peer talking to practitioners.

Confident but not polemical. The voice makes strong analytical arguments but grounds them in evidence, observed patterns, and structural logic — not opinion or advocacy.

Not academic. No passive voice where active works. No jargon-dense sentences. Analytical rigor without academic hedging.

Not advisory. This is not a "here's what to do" publication. The analysis may imply what better governance would look like, but it does not instruct boards how to behave.

Not political. The voice does not take partisan positions. It analyzes governance decisions and their structural consequences regardless of the political valence of the underlying issue.

Institutional, not personal. There is no editorial persona. The publication speaks, not an individual columnist. Byline: "By School Board Report Staff."

Think of the voice register as: long-form governance journalism. The 74. ProPublica education coverage. Chalkbeat's deeper analysis pieces. Not op-ed. Not wire service. Not academic journal.

Distinction From Sister Sites

The system must understand how School Board Report differs from its sister properties so it never produces content that belongs on another site:

schoolboardanswers.com (SBA): Answers practitioner questions. The frame is "what should I do?" or "how does this work?" Content is advisory, practitioner-facing, often how-to. If a piece tells board members or superintendents what to do, it belongs on SBA, not SBR. SBR never instructs. SBR analyzes.

schoolboardresearch.com (SBRS): Reviews and synthesizes academic research on school board governance. The frame is "what does the research show?" Content is research-focused, evidence-summarizing, often literature-review-style. If a piece is primarily about summarizing a body of research, it belongs on SBRS. SBR may cite research, but is not structured around reviewing it.

schoolboardweekly.com (SBW): Newsletter with AJ's editorial voice. First person, personal perspective, timely commentary. SBR is institutional and staff-attributed. SBR never has AJ's voice. SBR never uses first person.

The test: Is this piece tracing a governance pattern to its structural cause and its governance consequence? If yes, it may belong on SBR. If it describes a situation without an analytical frame — it doesn't. If it advises practitioners — it doesn't. If it reviews research — it doesn't. If it's in a personal editorial voice — it doesn't.

Content Goals

What Successful Analysis Accomplishes

A successful SBR piece does all of the following:

Names a specific governance pattern or dynamic — not a topic ("curriculum conflicts") but a pattern ("boards that intervene in curriculum selection without establishing outcome-linked criteria systematically undermine superintendent authority in ways that outlast the specific conflict").

Traces the pattern to its structural cause — not "because board members are doing it wrong" but because of some structural feature: unclear role boundaries, misaligned incentives, absence of monitoring systems, electoral dynamics, procedural norms, etc.

Connects the structural cause to governance consequences — what outcomes does this pattern tend to produce? For students, for the superintendent relationship, for board cohesion, for institutional trust?

Gives the reader an analytical frame they can apply elsewhere — after reading, the reader should be able to look at a different board situation and apply the same analytical lens. The piece's value is transferable, not just informative about the specific case.

Maintains analytical tension where it exists — good governance analysis acknowledges that structural dynamics are complex, that the same pattern can produce different outcomes in different contexts, and that reasonable people can disagree about governance trade-offs without the piece collapsing into "both sides."

What Failed Analysis Looks Like

A failed SBR piece exhibits one or more of the following failures:

Description disguised as analysis: The piece describes what happened — board voted this way, superintendent resigned, policy was adopted — without ever explaining what it means structurally or why it matters as a governance pattern. Readers learn what happened but not what to think about it.

Position-taking on political questions: The piece concludes that boards should or shouldn't adopt a specific policy, take a political stance, or make a particular content decision. SBR analyzes the governance dimensions of those decisions, not the underlying political/content question.

Op-ed voice: The piece sounds like someone's opinion rather than institutional analysis. Uses rhetorical escalation, emotional appeals, or language that signals the author is arguing a cause rather than analyzing a pattern.

Too timely without governance frame: The piece is so anchored to a specific news event — a single meeting, a single vote, a single week's headlines — that it reads as news commentary rather than governance analysis. If the news hook were removed, there would be nothing left. Timely pieces must have a durable governance frame that survives the specific triggering event becoming stale.

Too abstract without grounding: The piece makes sweeping claims about governance dynamics without connecting them to any real patterns, observed behaviors, or evidence. Theoretical analysis without grounding feels untethered and unpersuasive.

Management advice in disguise: The piece tells board members or superintendents what to do. Even if written in third person, if the clear implication is "boards should do X," it belongs on SBA.

The existential check: Could this piece appear in Education Week, The 74, or a general education policy publication without any changes? If yes, it is probably not specific enough to governance analysis. The piece must analyze governance behavior — board actions, decision structures, role boundaries, accountability mechanisms — and trace those to structural causes and consequences. Generic education policy analysis is not SBR content.

In-Bounds Content

Organizing Principle: The Analytical Frame Requirement

Every SBR piece must be structured around an analytical frame, not a topic. Before drafting, the system must be able to state in one sentence:

"This piece analyzes [specific governance pattern], which arises from [structural cause], and produces [governance consequence]."

If that sentence cannot be completed before drafting begins, the piece is not ready. Topic identification is not sufficient. The analytical frame must be established first.

Topic Clusters by Governance Domain

Board-Superintendent Boundary Dynamics

Boards that intervene in personnel decisions (hiring, firing, supervision of staff below superintendent level)

Boards that take operational positions on curriculum, vendors, or program details

Superintendent abdication — when boards expand authority because the superintendent creates a vacuum

Boards that communicate directly with staff, bypassing the superintendent

Evaluation structures that enable or constrain superintendent accountability

The structural conditions under which boards are more or less likely to overreach

Outcome Monitoring and Accountability

How boards that lack clear student outcome goals construct monitoring theater (looking at many data points without accountability for any)

Boards that conflate input monitoring (did we hire teachers?) with outcome monitoring (are students learning?)

Budget approval processes that obscure alignment between resource allocation and stated student outcome goals

Consent calendar misuse and what it signals about board engagement with accountability

Superintendent evaluation disconnected from student outcome data

Board Composition and Selection

Structural differences between appointed and elected boards and their governance consequences (not which is better — what the structural trade-offs produce)

How electoral dynamics shape board behavior: term effects, recall threats, campaign commitments that constrain governance

Board culture formation when seats turn over rapidly

The governance consequences of board member removal (recall, resignation under pressure, appointment to fill vacancy)

At-large vs. district-based representation structures and their governance implications

Conflict, Dysfunction, and Board Culture

Factionalism and its governance consequences: when board votes split reliably along persistent coalitions

Public meeting behavior as governance signal: what patterns in board meetings indicate about internal governance health

Executive session patterns: what the frequency, length, and aftermath of closed sessions reveal

The structural conditions that produce board-superintendent conflict vs. productive tension

How board culture transmits across personnel turnover

Budget Governance and Resource Alignment

Budget approval vs. budget oversight: how boards confuse these roles

How boards use budget line-item control as a proxy for policy influence

Special fund governance: how restricted/grant funds interact with board oversight

Capital project governance: structural reasons boards overinvolve themselves in construction and facilities decisions

The alignment question: do board-approved budget allocations actually reflect board-adopted outcome priorities?

Policy vs. Operations Confusion

The structural ambiguity of "policy": how boards use policy adoption to assert operational authority

Administrative regulation vs. board policy: when boards cross into administrative detail

Emergency policy-making: governance patterns in crisis moments that reveal underlying clarity (or lack thereof) about roles

What happens to institutional knowledge when board members conflate policy adoption with administrative direction

Specific Policy Domain Governance — Always Through the Governance Lens

Curriculum: The governance question is never "what should be taught" — it is "at what point in curriculum decision-making does board authority legitimately begin and end, and what happens structurally when boards operate outside those points?"

Discipline: The governance question is "how do boards establish and monitor discipline policy without becoming a board of appeals for individual cases?"

Special education: The governance question is "how do boards govern special education compliance without substituting their judgment for the superintendent's on individual student matters?"

Personnel: The governance question is "where is the structural line between board authority over superintendent performance and board intrusion into staff management?"

How to Cover Hot-Button Topics Without Taking Positions

When governance patterns involve politically charged content (book selections, DEI policies, transgender student policies, COVID protocols, etc.), SBR must cover the governance dimensions without endorsing or opposing the underlying content position.

The governing principle: Analyze the governance decision, not the content decision.

Wrong: "Boards that ban books are undermining academic freedom." (Content position.)

Wrong: "Boards that ban books are responding appropriately to community values." (Content position.)

Right: "Boards that adopt content-restriction policies without establishing explicit criteria for review, appeal, and consistency across comparable materials create structural accountability gaps regardless of the underlying content question. Those gaps expose the board to legal risk and procedural challenge that can outlast the original policy controversy." (Governance analysis.)

The content question — whether the policy is right or wrong — is not SBR's territory. The governance question — how the board exercised its authority, what structural consequences that produced, whether the process was sound — always is.

Stylistic Models

The following existing SBR articles model the voice, structure, and analytical approach. Reference them when evaluating draft quality:

analysis/appointed-vs-elected-boards.html — models how to analyze a structural governance question (selection method) through its consequences without advocating for one model over another

analysis/superintendent-resignation-governance.html — models how to use a common event type (superintendent departure) as the entry point for structural analysis of board-superintendent dynamics

analysis/outcome-monitoring-performance.html — models how to distinguish performance theater from meaningful accountability monitoring

analysis/quiet-pattern-boards-overstep.html — models how to name a pattern that is pervasive but rarely labeled, and trace it to structural causes

analysis/rubber-stamp-boards.html — models the opposite pattern: how absence of oversight produces its own governance failures

analysis/curriculum-governance-overreach.html — models how to cover a politically charged topic through the governance lens without taking a position on the underlying content question

Out-of-Bounds Content

Political Position-Taking

SBR does not take positions on partisan questions. This includes:

Which party should control education policy

Whether specific curriculum content standards are correct

Whether specific policy positions (on gender, race, religion, sexuality, immigration, etc.) are right or wrong

Endorsement of or opposition to specific ballot measures or candidates

The line is not "avoid controversy" — SBR covers genuinely controversial governance terrain. The line is: analyze the governance dimensions, not the underlying values or political question.

Test: Is the piece taking a position that would be at home in a partisan political publication? If yes, it's out of bounds. Is the piece analyzing how a board exercised authority and what structural consequences that produced? If yes, it may be in bounds.

Individual Names in Negative Contexts

No individual names in negative contexts. This means:

No superintendent names when describing failures, controversies, resignations, or firings

No board member names when describing overreach, dysfunction, or problematic behavior

No politician names (legislators, governors, mayors) in negative contexts

No names of attorneys, advocates, or community members involved in controversies

Why: SBR is governance analysis, not accountability journalism. It is not in the business of chronicling individual actors' behavior. Its analytical value comes from pattern-level analysis that generalizes across individuals, not from exposing specific people.

What is allowed: Named published researchers and authors when citing their work. Named studies and reports. Named institutions when they are the subject of referenced research (not SBR's own negative characterization). Published works that name people can be referenced in that research context ("A study by [Researcher Name] documented that boards in [district] exhibited...") because SBR is citing external published work, not originating the characterization.

District Names in Narrative

No real district names in SBR's own narrative. When describing a governance situation observed in a real district, use descriptor-plus-state format:

"a large Texas school district"

"a mid-sized Kansas system"

"a suburban Colorado district"

"a rural Mississippi board"

Exception: When referencing published research or journalism that names specific districts, SBR can reference that named work in the context of citing the research: "A 2023 study of governance practices in Chicago Public Schools found..." — because that is citing a named external source, not SBR originating a characterization of a named district.

No Student Names

Under any circumstances. No exceptions.

News Reporting Without Analytical Frame

Describing what happened — a board voted, a superintendent resigned, a policy was adopted — without analytical frame is not SBR content. If a piece could be filed in a news archive as "here's what happened this week," it is not analysis. Every piece must have an analytical frame that makes it valuable independently of the specific news event.

Management Advice Masquerading as Governance Analysis

If a piece is actually telling boards or superintendents what to do — even in third person — it belongs on SBA. SBR describes patterns and their consequences. It does not prescribe remedies. It does not say "boards should do X." It may say "boards that do X tend to produce Y outcomes, which creates Z governance consequence" — but the analytical conclusion is not an instruction.

Overlap Rules With Sister Sites

If the piece is primarily research review: SBRS

If the piece is primarily practitioner advice: SBA

If the piece is primarily personal editorial: SBW

If the piece is primarily news: No SBR property (SBR analyzes patterns, not events)

When in doubt: can the piece be reduced to its governance analytical frame and still stand? If removing the news hook or the advisory content leaves nothing, it's not SBR.

Citation and Sourcing

The Core Rule

SBR does not use formal APA, MLA, or Chicago citations. References to research are woven into the prose. However, the underlying sourcing standards are strict:

No fabricated statistics. Do not cite a percentage, number, or finding that is not sourced to real research. If the system does not have reliable knowledge of a specific statistic, do not use it.

Named studies must be real. If the piece names a study, institution, or researcher, that study must exist and must say what the piece claims it says.

Named researchers must be real. If the piece attributes a finding to a specific researcher, that person must be a real researcher who actually conducted or published the referenced work.

Inline Reference Format

Research references are woven into sentences naturally:

"Research from the Broad Center on school board governance found that boards with formal superintendent evaluation criteria tied to student outcomes retain superintendents significantly longer."

"A 2024 analysis in Educational Administration Quarterly documented that school board conflict — defined as regular split votes on routine matters — preceded superintendent turnover at twice the base rate."

"Work by [Researcher Last Name] at [Institution] has traced the conditions under which boards expand their operational footprint following superintendent transitions."

"The Wallace Foundation's long-running study of urban district leadership noted consistent patterns in how board-superintendent relationship quality correlated with improvement trajectory."

When the system is not certain whether a specific study exists with a specific finding, it must either:

Use language that accurately characterizes what is genuinely known without fabricating the specific study: "Governance researchers have documented patterns of..." (without fabricating a named study)

Or leave the citation out and make the claim from pattern observation rather than named research

The system must never fabricate a named study to make an argument sound more authoritative.

What Research Can and Cannot Do in SBR

Research is used to support analytical claims, not to constitute them. A piece that is primarily a research summary belongs on SBRS. In SBR, research is cited to ground a pattern claim — "this isn't just observed anecdotally, there's a literature on it" — but the piece's analytical frame must come from governance reasoning, not just from aggregating what studies say.

Content Format and Structure

Lede Requirements

The lede is a single paragraph. It must accomplish all of the following:

Name the specific pattern or incident analytically — not just "school boards have been in the news" but a specific, arguable claim about what pattern the piece examines and why it matters.

Establish the governance frame immediately — the reader should understand by the end of the first paragraph that this is a governance analysis piece and what governance question it addresses.

Give the reader the piece's thesis — the reader should know what the piece argues before the end of paragraph one. SBR ledes are not scene-setting intros that build to a thesis in paragraph three. The thesis is the first thing said.

Be formatted with the CSS class .lede — see Technical Filing section for exact HTML formatting.

What a strong lede looks like: "When a school board votes to override a superintendent's staffing recommendation, it rarely describes the action as a boundary violation — instead, it frames the intervention as responsiveness, fiscal stewardship, or community accountability. But the governance literature consistently shows that boards that routinely intervene in personnel decisions below the superintendent level produce measurable damage to executive function, regardless of how the intervention is publicly framed."

What a weak lede looks like: "School boards across the country have been making headlines recently for their decisions about curriculum and hiring. Governance experts say these conflicts reflect deeper tensions about the role of the board versus the superintendent."

The weak lede describes without arguing. It hedges rather than claims. It gestures at a topic rather than naming a pattern. It would be rejected.

H2 Section Structure

Each article contains 3 to 5 H2 sections between the lede and the conclusion. Requirements:

Each section must advance the argument — not just add more examples of the same thing, but move the analysis forward. Section 1 might establish the pattern. Section 2 might trace the structural cause. Section 3 might document the governance consequences. Section 4 might examine why the pattern persists despite known consequences.

Sections are not parallel summaries — avoid structures like "District A did X / District B did X / District C did X." That's a list of examples, not advancing an argument.

Each H2 should be substantive enough to stand — roughly 150–250 words per section is the expected range.

H2 titles should be analytical, not descriptive — "The Structural Cause" is weaker than "Why Boards Overstep: Accountability Without Authority." The title should hint at the analytical content of the section.

Pullquote Guidance

Pullquotes are optional. Use them when a single sentence or two captures the piece's central analytical insight in a way that would stop a skimming reader and pull them in.

When to use: When the piece has a formulation that is analytically sharp and independently meaningful — where the pullquote could stand alone and convey something true about governance.

When not to use: When the best available candidate is just a well-written sentence that requires context. A pullquote that makes no sense without reading the surrounding paragraph is not a good pullquote.

What makes a strong pullquote: It advances the argument. It should be the kind of sentence someone quotes when sharing the piece. It should contain the analytical core, not a decorative phrase.

HTML format:

<div class="pullquote">

  The quote text goes here, as a sentence or two that can stand alone analytically.

</div>

Do not use quotation marks inside the pullquote div. Do not attribute it to anyone — it is the piece's voice, not a named source.

Conclusion Requirements

The conclusion must NOT be a summary. Do not restate what the piece covered. The conclusion must end on one of three things:

The governance implication — given the pattern analyzed, what does this mean for how governance functions or should function in the field? State it as analytical observation, not advice.

The unresolved tension — some governance dynamics have no clean resolution. Name the tension honestly. What competing structural imperatives make this pattern persistent or hard to change?

The next question — what does this analysis open up? What governance question does this pattern point toward that hasn't yet been answered? This is particularly effective for evergreen pieces where the analysis is meant to generate ongoing inquiry.

The conclusion should leave the reader with something to think about, not a sense that everything has been wrapped up and filed away.

Word Count

700 to 1,000 words. This includes the lede and conclusion but not the front matter or HTML boilerplate. Pieces under 700 words are likely underdeveloped. Pieces over 1,000 words are likely unfocused. The discipline of fitting governance analysis into this range is part of what makes SBR useful — it forces clear argument structure.

Grounding Document

Source: Great on Their Behalf (3rd edition) by AJ Crabill Access: Google Drive ID: 1KwiTQKLZlRDnTCzDmHaleeU3IVj_cHbsmA2s6nORdkE (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: a — pre-draft only

Pre-draft only: Before drafting, read the relevant sections of the grounding document. Use it to calibrate the frame, vocabulary, and core claims before writing begins. It is a framing calibrator, not a citation source.

Voice Register

Register: ajc-long Fidelity: Moderate

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

Sentence and paragraph targets:

Average sentence length: ~23 words

Paragraph length: 4–8 sentences

No extended run of 3 or more consecutive sentences under 8 words

Core fingerprints:

Oxford comma: always (a, b, and c)

Straight quotes only (no curly quotes)

Contractions used naturally (don't, it's, we've)

Reading level: Appropriate for a practitioner and policy audience — sophisticated but not academic.

Note on register vs. voice: SBR uses ajc-long register at moderate fidelity. This means the register shapes rhythm and structure, but the voice itself is institutional (third person, staff-attributed, non-personal). The ajc-long register governs sentence complexity and paragraph depth; the SBR institutional voice governs person, tone, and attributional stance.

NEVER Rules

Never use "you" directed at the reader

Never use first person ("we," "our," "I")

Never use advisory language ("boards should," "the right approach is," "to avoid this, boards must")

Never take partisan positions or endorse/oppose policy content questions

Never name individual people in negative contexts (no superintendent names in controversies, no board member names in overreach, no politician names in negative framings)

Never use real district names in SBR's own narrative (use descriptor-plus-state format: "a large Texas school district")

Never use student names under any circumstances

Never fabricate statistics, named studies, or named researchers

Never write news reporting without an analytical frame

Never produce a piece that tells boards or superintendents what to do — even in third person

Never name ESB, AJ Crabill, GOTB, or "why-based governance" explicitly in SBR content

Never link to effectiveschoolboards.com or whybasedboards.com as a standalone recommendation (only acceptable buried in a list of 3 or more external links, and only 1–2 times per year maximum)

Never use "recently," "this week," or "last month" in article content

Never include the byline in the content body (injected by template)

Never output a full standalone HTML document — output front matter plus body only; do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags

Never produce a conclusion that summarizes — end on governance implication, unresolved tension, or next question

Generation Process

Every SBR article must pass through all twelve steps in order. Steps may not be skipped. Steps that fail must result in revision and restart of subsequent steps, not publication with caveats.

Step 1: Governance Pattern Identification

State explicitly: what specific governance pattern is this piece analyzing?

The pattern must be:

Specific (not "curriculum conflict" but "boards that adopt content criteria in curriculum policy without establishing procedural consistency or appeal structures")

Observable (something that actually occurs in the field, not a theoretical possibility)

Governance-relevant (connected to board authority, accountability, role boundaries, or outcome responsibility — not just general education policy)

Output from this step: one or two sentences naming the pattern precisely.

Step 2: Analytical Frame Development

Complete the following before proceeding:

Pattern statement: What governance pattern is this piece analyzing?

Structural cause: What structural feature of board governance enables or produces this pattern? (Not "because boards are bad" — but because of role ambiguity, electoral incentives, accountability vacuum, procedural norm, etc.)

Governance consequence: What does this pattern tend to produce? Name specific consequences: superintendent tenure effects, student outcome impacts, institutional trust effects, legal or procedural consequences, board cohesion effects, etc.

Proposed thesis sentence: One sentence that a reader could quote as the piece's central claim.

If all four cannot be completed, the piece is not ready to draft. Return to Step 1.

Step 3: Research Sourcing

Before drafting, identify:

Are there real published studies, reports, or research that address this governance pattern or a closely related one?

If yes: what do they say, and can that finding be accurately represented in inline citation format?

If no named research is available: the piece can still proceed using pattern observation and structural reasoning, but must not fabricate citations to compensate.

Document sourcing status: "Named research available / Named research not available — will use observed pattern framing."

Step 4: Lede and Outline Generation

Produce:

The lede paragraph (must contain the thesis, name the pattern analytically, establish the governance frame, deploy .lede class)

A section outline: 3–5 H2 sections with working titles and one sentence describing what each section contributes to the argument

A proposed pullquote candidate (may be marked TBD until draft is complete)

A conclusion approach: which of the three conclusion types (governance implication, unresolved tension, next question) will this piece use?

Review the outline for argument progression before drafting. Each section must advance the argument — adding more examples of the same point is not advancement.

Step 5: Draft Generation

Model: the configured write model (primary). Claude Opus 4.8 (fallback if the configured write model is unavailable or produces unacceptable output).

Draft to the outline. Do not deviate from the analytical frame established in Steps 1–4 during drafting. If the draft reveals that the analytical frame was wrong or underdeveloped, stop, return to Step 2, and regenerate. Do not salvage a bad frame by softening the draft.

Word count target: 700–1,000 words. If the draft significantly exceeds or falls short, diagnose why before proceeding:

Significantly short: likely the analytical frame is underdeveloped

Significantly long: likely the piece is trying to do two pieces at once

Step 6: Analytical Rigor Check

For each H2 section, verify:

Does this section advance the argument or just add examples?

Does this section connect to the structural cause and governance consequence established in Step 2?

Is there a claim in this section, or just description?

For the piece as a whole:

Does the piece explain the mechanism (why does this governance pattern produce these outcomes?) or just assert correlation?

Is the analytical frame consistent across all sections, or does the piece drift?

Does every paragraph contribute to the argument?

If any section fails: revise that section before proceeding to Step 7.

Step 7: ESB / Why-Based Alignment Check

Verify that the piece's analysis is implicitly organized around whether board behavior serves student outcomes. This does not mean the piece must say "student outcomes" repeatedly — but the analytical evaluation of governance patterns must be grounded in whether the pattern serves the fundamental purpose of the board (improving outcomes for students) or serves other interests (political positioning, adult preferences, procedural habit, individual board member priorities).

Specific checks:

Does the piece treat outcome-aligned governance behavior as the implicit standard against which patterns are evaluated?

Does the piece avoid treating governance purely as procedural compliance without asking whether the governance behavior actually serves students?

Does the piece's analysis of consequences include student-outcome consequences, not just institutional or relational ones?

The five ESB practices (Focus, Clarify, Monitor, Align, Communicate) inform the analytical lens without ever being named in published content.

Step 8: Quality Checks

Run all quality checks in Section 8 (8a through 8g) in order. All must pass before proceeding to Step 9.

Step 9: Technical Filing

Verify all technical requirements (see Technical Filing section) before marking the piece ready to publish:

Front matter complete and correct

File named correctly

Lede formatted with .lede class

Pullquote (if used) formatted with .pullquote div

Byline NOT included in content (injected by template)

Category is an allowed value

Date display formatted correctly

Jekyll build check passes

Step 10: Red-Team Adversarial Check

Run Section 8e (Primary Red-Team) and 8f (Council Red-Team) if not already completed as part of Section 8. All failures must result in revision. After revision, re-run the red-team check for the revised claims.

Step 11: Existential Voice Test

Run Section 8g (Existential Voice Test). Final check: could this piece appear in Education Week, The 74, or a general education policy publication without changes? If yes, the piece is not specific enough to governance analysis and must be strengthened.

The piece must analyze governance behavior and trace it to structural causes and governance consequences. If the piece reads as general education policy commentary, it has failed the voice test and must be revised.

Step 12: Publish

Mark ready to publish. Auto-publish after all quality gates pass. There is no 72-hour review gate. Quality gates are embedded in this multi-step generation process. The system must apply all gates rigorously before marking a piece ready to publish. If any gate fails, the piece must be revised and re-checked, not published with the failure noted.

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

Ultimate Failure Reporting — SBR: Submit a failure report to the ESB content approval system at esby.effectiveschoolboards.com/admin/. Include: site (SBR), article title, which check failed, attempt count, nature of each failure, and the draft. Mark status as FAILED. Do not publish.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any em-dash ( — ) anywhere in the piece (em-dashes are forbidden; use a spaced double-hyphen "--" instead), and more than 1 spaced double-hyphen "--" in a single paragraph

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (SBR):

In addition to the standard tiers above, apply the following SBR-specific anti-slop checks:

Remove hollow transitional phrases: "It is important to note that," "As we have seen," "In conclusion," "It goes without saying"

Remove intensifiers that substitute for argument: "clearly," "obviously," "undeniably," "without question"

Remove hedge stacking: "may perhaps sometimes tend to" — pick the right level of certainty and state it directly

Remove redundant restatement: if a point has been made, don't make it again in different words without adding something

Remove weak paragraph openers that label rather than argue: "Another factor is..." "There is also..." — lead with the claim

Remove vague attributions: "experts say," "many observers note," "it has been argued" — say who, or cut it

Remove filler sentences that add length without adding content

"Description disguised as analysis" detection: For every paragraph, ask: is this paragraph making a claim about what governance patterns mean, or is it describing what happened? If it is primarily descriptive without analytical content, flag it. Every paragraph must do analytical work, not just add narrative detail.

Editorializing detection: Read each paragraph with the question: is this paragraph taking a side on a political or values question rather than analyzing governance dimensions? Red-flag sentences that would work equally well in a partisan advocacy document. The analytical framing must be the organizing logic, not a political or moral position.

Abstract governance principle without real-world grounding: Flag any paragraph that makes claims about governance dynamics without connecting them to any real pattern, observed behavior, or evidence — even if evidence is pattern-level rather than named-research-level. Pure abstraction without grounding is a slop pattern.

Hedge overload: If the piece qualifies every claim so thoroughly that it makes no definite claim, it has been overcorrected into uselessness. "Some boards may in certain circumstances tend to sometimes exhibit patterns that could potentially be interpreted as..." is not analysis — it is evasion. Hedge appropriately for genuine uncertainty; do not hedge to avoid making an argument.

Pullquote quality check: If the piece includes a pullquote, verify: does this pullquote advance the argument? Could this sentence appear in a different context and still convey something analytically true about governance? If the pullquote is just a well-written sentence that happens to be from the piece but doesn't contain the analytical core, replace it with a better candidate or remove the pullquote.

Length check: After removing slop, is the piece still within 700–1,000 words? Slop removal should produce a tighter, stronger piece in the same range. If removal drops it significantly below 700 words, the piece was underdeveloped — the slop was filling in for missing analytical content. Return to Step 2.

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

SBR-specific voice checks:

In addition to the standard voice check above, verify:

No "you" directed at the reader

No first-person ("we," "our," "I")

No advisory language ("boards should," "the right approach is," "to avoid this, boards must")

No partisan framing or position-taking on political questions

No academic passive-voice hedging that drains the analytical force

No tabloid escalation or rhetorical advocacy

Voice is confident and analytical, not hedged into meaninglessness and not polemical

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

Political Neutrality Test

Does this piece take a position on a partisan issue? Apply the test from both sides: would a partisan progressive find this piece is covertly advancing a conservative position? Would a partisan conservative find this piece is covertly advancing a progressive position? If either adversarial reading is sustainable, the piece has drifted into political positioning. Identify the specific claims or framing that enable the reading and revise.

Analytical Completeness Test

Does the piece show the mechanism — why does this governance pattern produce these outcomes — or does it merely assert that the pattern and outcomes co-occur? Correlation without mechanism is insufficient for SBR. The piece must explain the causal or structural logic that connects the pattern to its consequences. If the mechanism is missing, the analytical frame is incomplete. Return to Step 2.

Expert Plausibility Test

Would an experienced superintendent (with 10+ years leading multiple districts) and an experienced school board attorney broadly agree with the structural analysis, even if they would push back on specific claims or nuances? If the structural analysis would strike experienced practitioners as fundamentally wrong about how governance works, the analytical frame needs revision. The expert plausibility test is not about whether they would endorse the conclusions — it is about whether the governance structural reasoning is sound.

Evergreen Validity Test

If this is an evergreen piece: would it still make sense in 18 months without revision? If it depends on current political conditions, current news events, or specific policy debates that may resolve, it is not truly evergreen. Either revise to make it durable or classify it as timely and handle accordingly.

Content Integrity Checks

No "recently," "this week," or "last month" in article content — use specific time references instead

No real district names in SBR's own narrative — use descriptor-plus-state format

No student names under any circumstances

No fabricated statistics, named studies, or named researchers

Byline NOT in content body (injected by template)

No ESB, AJ Crabill, GOTB, or "why-based governance" named explicitly in content

Duplicate Content Check

Before publishing, verify the piece does not repeat an analytical angle already covered by an existing SBR article:

Search existing published SBR articles for pieces with similar analytical frames

If a piece on the same pattern already exists, the new piece must offer a meaningfully different analytical frame, new structural analysis, or substantially different focus — not just updated examples or different phrasing of the same argument

8e. Primary Red-Team (the configured write model)

Primary Red-Team — Single Adversarial Pass (the configured write model)

Run the draft through the configured write model with an adversarial prompt instructing it to:

Challenge every major claim: is this actually supported? Where could a knowledgeable reader push back?

Find logical gaps: does the argument hold together from premise to conclusion?

Flag unsupported assertions: any claim that needs evidence and doesn't have it

Identify reader-hostile moments: where would a skeptical reader stop reading?

Surface structural problems: does the piece earn its conclusion or merely assert it?

Apply also:

The strongest objection: What is the strongest objection a thoughtful critic would raise against the piece's central claim? Does the piece acknowledge this objection or at least not be undermined by it?

Counterexamples: What real-world governance scenarios would contradict the pattern the piece analyzes? Does the piece account for these, or does it overstate the universality of the pattern?

Unsupported leaps: Where does the piece make claims that are not supported by evidence, structural logic, or observed patterns? Flag each one.

False precision: Does the piece claim more certainty than the underlying evidence supports? Analytical confidence should be proportional to the strength of the evidence or the structural argument.

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

SBR-specific existential check: Could this piece appear in Education Week, The 74, or a general education policy publication without any changes? If yes, it is not specific enough to governance analysis. The piece must analyze governance behavior — board actions, decision structures, role boundaries, accountability mechanisms — and trace those to structural causes and consequences. Generic education policy analysis is not SBR content.

This test is subjective. If you would not be surprised to see this exact piece on a competitor site, it fails.

Technical Filing

Front Matter

Every article requires these Jekyll front matter fields:

---

layout: article

title: "Article Title Here"

category: governance-dynamics

date_display: "June 20, 2026"

---

layout: always article — never blank, never another value

title: in double quotes; specific and analytical; not a topic label but a claim or a question

category: must be one of the allowed values listed below

date_display: in double quotes; format is "Month DD, YYYY" (e.g., "June 20, 2026"); do NOT use ISO format

Allowed Category Values

governance-dynamics

board-superintendent

accountability

board-composition

budget-governance

policy-operations

board-culture

Select the most specific category that applies. If multiple apply, select the primary analytical focus.

Byline

The byline "By School Board Report Staff" is injected by the article layout template. Do NOT include it in the article content. If the byline appears in the content body, it will be duplicated in the rendered page.

Lede Formatting

The lede paragraph must be formatted with the .lede CSS class:

<p class="lede">Lede paragraph text here.</p>

This is the first content element after the front matter. It is not preceded by any other paragraph or heading.

Pullquote Formatting

If a pullquote is used:

<div class="pullquote">

  The pullquote text here, as a standalone analytical statement.

</div>

No quotation marks inside the div

No attribution

Positioned within the article body at a natural break point, typically after the second or third H2 section

H2 Section Formatting

<h2>Section Title Here</h2>

Standard HTML. No classes required. 3–5 sections per article.

File Naming and Placement

Path pattern: analysis/[topic-phrase].html

All lowercase

Words separated by hyphens

No underscores, spaces, or special characters

Descriptive of the governance pattern, not the triggering news event

File must be placed in the analysis/ directory at the Jekyll project root

Good examples:

analysis/appointed-vs-elected-boards.html

analysis/superintendent-resignation-governance.html

analysis/outcome-monitoring-performance.html

analysis/quiet-pattern-boards-overstep.html

analysis/rubber-stamp-boards.html

analysis/curriculum-governance-overreach.html

Bad examples:

analysis/board-meeting-june.html (too timely, no analytical content in name)

analysis/news.html (not descriptive)

analysis/school-board-problems.html (too vague)

analysis/Appointed-Boards.html (uppercase — must be lowercase)

The file name should be stable and not embarrassing when it persists for years. Choose topic phrases that describe the governance pattern, not the triggering event.

Output Format — Critical

The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

Jekyll Build Check

Before marking ready to publish, verify:

Front matter YAML parses without errors

category value is in the allowed list

No HTML formatting errors (unclosed tags, malformed divs)

File is in the correct directory

Filename matches the pattern

Independent Review Protocol

Approval flow: Auto-publish after all quality gates pass. There is no 72-hour review gate. Quality gates are embedded in the multi-step generation process (Generation Process section). The system must apply all gates rigorously before marking a piece ready to publish. If any gate fails, the piece must be revised and re-checked, not published with the failure noted.

Learned Rules

Ongoing Content Integrity Rules

Timely vs. Evergreen Handling

Timely pieces are anchored to a current pattern or period:

They analyze a governance pattern that is currently visible in the field — not just one event, but a recognizable pattern of events happening now

They must have a governance frame that survives the immediate news cycle — the analytical content must remain valuable for at least 90 days after publication

Avoid language that anchors the piece too specifically to a single event: "this month's school board election" will read oddly in six months. Prefer: "recent elections in which..." or "the past cycle of..."

Avoid "recently," "this week," "last month" — use specific timeframe descriptions where necessary: "in the spring 2026 election cycle" rather than "recently"

Evergreen pieces are not anchored to a specific period:

They analyze structural governance dynamics that are perennially relevant

They must be grounded in real patterns and observed governance behavior — not so abstract that they feel disconnected from actual governance practice

They must pass the evergreen validity test (Section 8d): would this piece make sense without revision in 18 months?

For both types: Never use "recently" or "this week" in article content. Specificity beats vagueness even for timely pieces. "In districts across six states that faced board recall campaigns between 2023 and 2025" is better than "recently, many districts..."

Cross-Site Linking Rules

SBR may link to sister sites under the following strict conditions:

SBR may link to effectiveschoolboards.com or whybasedboards.com a maximum of 1–2 times per year, and only when the link appears in a list of 3 or more external links. Neither site may be singled out as a standalone recommendation.

Sister sites interlink with extreme subtlety — never in a way that reads as self-promotion or cross-marketing

Never name ESB, AJ Crabill, GOTB, or "why-based governance" explicitly in SBR content under any circumstances. These are the values informing the analytical lens, not the products being marketed.

Anti-Repetition Within Pieces

Within any single article:

Do not restate the same claim in different words across sections — each section must add analytical content

Do not repeat examples — if a situation is introduced as an illustration, it should not reappear later as a second example

Do not use the conclusion to summarize — if the conclusion repeats what the piece has already said, revise it to end on governance implication, unresolved tension, or next question

Date Handling in Content

Never use: "recently," "this week," "last month," "currently," "now"

Prefer: specific time references ("in the 2024–25 academic year"), relative ranges ("over the past decade"), or timeless observation framing ("in districts where...")

For research citations, always include the year: "A 2023 study..." not "a recent study..."

Publication date is set in front matter date_display — do not repeat the publication date in the article body

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"