title: SLRP Blog — Content Guide type: content-guide site: studentledrp.org repo: ajcrabill/slrp-org updated: 2026-07-08

SLRP Blog Content Guide

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

studentledrp.org is AJ Crabill's site for Student-Led Restorative Practices. The blog publishes once per week, drawing from a sequential source queue. Each post takes 1–3 substantive paragraphs from the current source and deepens into the topic with an essay-length exploration of the ideas in that passage.

Posts commit directly to the repo. No approval gate. Posts appear immediately when pushed.

Grounding Document

Source: Our Tools They Deserve (OTTD) by AJ Crabill Access: Local file in Obsidian vault: Admin/Loriah Skills/slrp-org/ottd-full-text.md Usage pattern: c — pre-draft AND post-draft

Pre-draft: Before drafting, read the relevant sections of the grounding document. Use it to calibrate frame, vocabulary, and core claims before writing begins.

Post-draft: After completing all quality checks, verify the finished piece against the grounding doc: confirm no claims contradict it, vocabulary is consistent, and the piece would not confuse a reader who knows the book well. This is done as Section 8h.

Voice Register

AJ's first-person practitioner voice. AJ is writing from nearly two decades of direct field experience training students and adults in restorative practices. The register is:

Grounded in specific real incidents, schools, and students (named or described concretely)

Direct about hard truths adults don't like hearing — that adult behavior, not student deficiency, is the primary obstacle

Warm toward students; candid, not harsh, about adult failures

Willing to make claims other educators won't make ("we have never seen a restorative practices initiative fail because students were too bad")

Comfortable with long examples before arriving at the insight they carry

Skeptical of bureaucratic and retributive defaults, but not self-righteous about it

Uses the toolbox metaphor as the core explanatory frame for student behavior: students use the best tool available to them; add better tools, and watch behavior shift without coercion

Source material for voice: Our Tools They Deserve (OTTD) by AJ Crabill. The book opens chapters with specific stories, develops claims from those stories, and arrives at implications practitioners can act on. Blog posts should feel like chapters from that book — not shorter blog posts, not academic summaries.

Rhythm targets (ajc-long register):

~23 words/sentence average across the piece

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

Paragraphs: 4–8 sentences

NEVER Rules

Never use these words or phrases:

"empower" / "empowerment" — implies students were powerless rather than under-tooled

"at-risk students" — deficit frame; write about what they lacked or what happened, not what they are

"restorative justice" — use "restorative practices" (distinct frameworks; AJ is explicit about this)

"stakeholder"

"leverage" (as a verb)

"innovative" / "innovation" without a specific referent

"transformative" as a standalone claim — show the transformation, don't declare it

"paradigm shift"

"best practices" unless quoting someone

"going forward"

"It's important to note that"

"The reality is" / "The fact is" (throat-clearing openers)

"In conclusion" / "To summarize" / "In summary"

"research shows" without naming the research

"studies suggest" without naming the studies

"moving the needle"

Never use these constructions:

Second-person address ("you") directed at the reader — write about practitioners, administrators, and students in third person

Rhetorical questions as paragraph openers more than once per post

Numbered listicles ("5 ways to…", "3 things that…")

Opening with a definition ("Restorative practices are defined as…")

Opening with a statistic or data point — open with a scene or story

Exclamation marks

Ellipses (…)

Em-dashes (use a spaced double-hyphen "--" instead; unicode em-dashes ( — ) are forbidden)

Passive constructions that hide agency ("students are given tools" → "we give students tools")

Never portray students in deficit framing:

Never write "misbehaving students" — write about specific behavior or students who needed more tools

Never write "troubled students" — be specific or use neutral language

Never imply students choose bad behavior freely — always reference the toolbox frame (they used the best tool they had)

Never frame suspension or exclusion as the natural or neutral response

Never include a publication date in the visible post content or meta div — the <div class="meta"> date field must be omitted (left empty or removed entirely) from the generated HTML. Posts are meant as evergreen reference material; visible dates make them feel stale.

Oxford comma always.

Essay Generation Process

Before beginning Step 1, complete the grounding doc pre-draft alignment per Section 4.

Step 1 — Read the source queue

Open Admin/Loriah Skills/slrp-org/source-queue.md in the Obsidian vault at /Users/ajc/Documents/Obsidian Vault/.

Note: current-source, current-position, and last-para-index fields tell you exactly where to pick up.

Step 2 — Open the source and locate the passage

For OTTD: Read from Admin/Loriah Skills/slrp-org/ottd-full-text.md. The file contains the full manuscript as paragraphs separated by blank lines. Navigate to last-para-index (the paragraph index where the previous post left off). Count forward from there.

For other sources: Use the Google Drive MCP (mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) with the doc ID listed in the queue.

Step 3 — Select the passage

Read forward from the tracked position. Skip:

Table of contents, part/section headers, chapter title lines

Rubric rows, scoring tables, data tables

"In this section, we will…" transitional lines

Procedural step instructions ("Step 1: Do X")

Single-sentence filler paragraphs (< 30 words)

Select when you find 1–3 paragraphs containing:

A specific story or incident (named or described concretely)

A named claim or insight about restorative practices or adult behavior

A developed argument about why something works or doesn't

A surprising counterintuitive finding from the field

The passage should be arguable — something a reader could push back on, extend, or apply to their context.

Step 4 — Update the queue before generating

Before writing the post, update source-queue.md:

Set last-para-index to the paragraph after the selected passage

Increment posts-from-current-source

If you have reached the end of a chapter (OTTD) or the end of a standalone doc, mark that source as [x] complete and advance current-position to the next source

Step 5 — Identify the anchor idea

Extract the single most important claim or insight from the selected passage. Write it in one sentence. This becomes the anchor — the idea the essay develops, challenges, contextualizes, or extends.

Step 6 — Write the essay

Opening paragraph (required pattern): Begin with a specific scene, moment, or incident — not a general claim or abstract framing. Ground the reader in something concrete. The Jasmine story, a specific training session, a conversation in a school hallway. Then introduce the anchor claim from that scene.

Development (2–4 paragraphs): Develop, contextualize, and extend the anchor idea. Draw on the source material but go further:

What does this mean for practitioners in schools?

What does it look like in real implementation?

What's the implication people miss or resist?

What does AJ's direct experience add to the claim?

Complication (1 paragraph): Name what makes this hard. What's the counter-argument? Where does the field tend to go wrong on this? What adult impulse or institutional pressure works against the insight? Don't paper over difficulty.

Close (1 paragraph): Land on a forward-facing observation — not a call to action, not a summary, not "so let's all do X." Something that leaves the reader sitting with the idea. The best closes extend the implication one step further than the reader expected.

Target length: 900–1400 words. Format: Plain prose. No subheadings. No bullet lists. No numbered sections within the essay body.

Step 7 — Write the headline and excerpt

Headline: Specific to the essay's actual argument, not just its topic. Avoid "Why X Matters" and "The Importance of Y" patterns. The headline should identify the most interesting true claim the essay makes. Examples from the book's voice: "The Toolbox Isn't Empty. It's Wrong for the Job." or "Nine Months Training Adults Before the First Student Walks In."

Excerpt: 1–2 sentences. The argument, not the topic. Should make a reader want to keep reading.

Step 8 — Build front matter and commit

Front matter format:

---

layout: post

title: "Headline Here"

author: ajc

reading_time: "N min"

excerpt: "Excerpt here."

toplevel: Blog

toplevellink: /blog

---

Filename: _posts/YYYY-MM-DD-slug-from-headline.md (use today's date) in the slrp-org repo at /tmp/slrp-org/.

Git steps:

cd /tmp/slrp-org

git add _posts/YYYY-MM-DD-slug.md

git commit -m "Add weekly post: slug"

git push origin main

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

Ultimate Failure Reporting — SLRP: Do NOT commit the post to the repo. Send a failure notification email to ajcrabill7@gmail.com with subject line: "[SLRP FAILURE] Weekly post generation failed at [stage name]". Body must include: the full draft, which check failed, number of retries attempted, and the nature of each failure. Also log the failure to Loriah's conversation journal.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any unicode em-dash ( — ) (use a spaced double-hyphen "--" instead)

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (SLRP (studentledrp.org)):

"empower" / "empowerment"

"at-risk students"

"restorative justice" (must be "restorative practices")

"stakeholder"

"leverage" (as a verb)

"best practices" (unless quoting)

"going forward"

"The reality is" / "The fact is"

"research shows" (without naming the research)

"studies suggest" (without naming the studies)

"moving the needle"

"paradigm shift" (already Tier 1 above, but explicitly banned here)

"transformative" as a standalone claim (already Tier 1 above, but usage rule applies: show it, don't declare it)

8b. Voice Check

Voice Check — High Fidelity (ajc-long)

Run a full voice score against AJ's voice profile. All items below must pass. Threshold: ≥ 0.90 overall score.

NEVER rules (35% of score) — all must be clean:

Tier 1 anti-slop words (checked in 8a): any remaining instance fails

Sentence-initial transitions banned: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately, Interestingly

AI hallmark phrases banned: "It's important to note," "It's worth mentioning," "In today's world," "In the realm of," "As an AI," "certainly" / "absolutely" as empty affirmatives

Punctuation: no exclamation marks, no ellipses, no curly quotes, no em-dashes (use a spaced double-hyphen "--" instead; unicode em-dashes ( — ) are forbidden)

No voice hedging: never use "I feel," "I think," "I believe" as epistemic hedges (direct assertion only)

Fingerprints (20% of score) — all must be present:

Oxford comma: always (a, b, and c — never a, b and c)

Contractions: used freely throughout (it's, don't, we've, they're, etc.)

Straight quotes only: " and ' — never curly " " ' '

No em-dashes: use a spaced double-hyphen "--" (word -- word); unicode em-dashes ( — ) are forbidden

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

Site-specific voice checklist items (SLRP):

The toolbox metaphor is present or consistent with: students use the best tool available; add better tools to shift behavior

No second-person address ("you") directed at the reader — practitioners, administrators, and students are in third person

No rhetorical questions as paragraph openers more than once per post

No numbered listicles ("5 ways to…", "3 things that…")

Does not open with a definition

Does not open with a statistic or data point — opens with a scene or story

No passive constructions that hide agency ("students are given tools" → "we give students tools")

No deficit framing of students — not "misbehaving students," not "troubled students," no implication of free bad-choice-making

No framing of suspension or exclusion as the natural or neutral response

8d. Site-Specific Checks

Quality Bar — Core Essay Requirements

Before proceeding to red-team, verify all of the following:

The essay makes an actual argument — a reader could disagree with the central claim

The opening paragraph is scene-specific and concrete, not abstract

The essay draws on but extends beyond the source passage (doesn't just restate it)

No NEVER words or constructions are present (cross-check against Section 6)

The voice is AJ's first-person, practitioner-grounded register

Front matter is complete and correct (no date field; <div class="meta"> date field omitted or empty in rendered output)

Word count 900–1400

No subheadings or bullets inside the essay body

The toolbox frame is intact: students as under-tooled, not deficient; adult behavior as primary obstacle

The close does not summarize — it extends the implication one step further

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

Access the grounding document (Our Tools They Deserve (OTTD) by AJ Crabill) and verify:

No claim in the finished piece directly contradicts a claim or framework in the grounding doc

Key terminology is consistent — if the book uses a specific term, the piece uses it the same way

A reader who knows the grounding doc well would not be confused or jarred by this piece

The piece reinforces the grounding doc's core intellectual framework rather than drifting from it

This is not a citation check. The piece does not need to cite the grounding doc. It is an alignment check: does the piece fit within the same intellectual ecosystem?

Fails if: any direct contradiction is found; any significant terminology drift exists; or the piece would confuse a reader who knows the book.

Technical Filing

Filename format: _posts/YYYY-MM-DD-slug-from-headline.md

Repo location: /tmp/slrp-org/ (local clone of ajcrabill/slrp-org)

Front matter fields required:

---

layout: post

title: "Headline Here"

author: ajc

reading_time: "N min"

excerpt: "Excerpt here."

toplevel: Blog

toplevellink: /blog

---

No date field. Jekyll infers the date from the filename for ordering purposes only; dates are not displayed on the site. The <div class="meta"> date field in the post header must also be omitted or left empty — do not populate or display a publication date anywhere in the rendered post.

Git steps:

cd /tmp/slrp-org

git add _posts/YYYY-MM-DD-slug.md

git commit -m "Add weekly post: slug"

git push origin main

Auto-publish: SLRP is auto-publish. No approval gate. No independent review step. Commit and push is the complete filing action.

Learned Rules

(No learned rules recorded yet. Rules are appended here as AJ's published edits diverge from submitted drafts.)

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"