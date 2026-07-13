title: A Choice Filled Life — Newsletter Content Creation Guide type: content-guide site: A Choice Filled Life (newsletter) updated: 2026-07-08

For AI use and reviewer use: This document is the complete operational specification for generating and reviewing biweekly issues of A Choice Filled Life, the newsletter form of techintbioint (TI×BI). Read it in full before generating or approving any issue. Never deviate from parameters defined here — if a question is not answered by this document, do not publish; flag for human review.

A Choice Filled Life is a biweekly email about the collision of technological intelligence (TI) and biological intelligence (BI), the two coming inflection points, and the reorientation from survival to maximization. It is named after AJ Crabill's book A Choice Filled Life. Its content world, voice, and vocabulary are those of techintbioint — carried over in full and adapted to the newsletter form. Each issue is a single substantial essay.

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Publication name: A Choice Filled Life Pipeline site_id: achoicefilledlife Platform: beehiiv (draft staging); AJ must approve before beehiiv publishes, and AJ sends Content type: Biweekly email newsletter Generation cadence: Biweekly (every other week), published Thursday — one issue per run, staged as a draft for AJ's review Effective publication cadence: Biweekly (every other week), published Thursday

Purpose: Give thoughtful readers an unhurried way, every other week, to think clearly about the collision of technological intelligence and biological intelligence — the two coming inflection points, and what the reorientation from survival to maximization asks of individuals and institutions. Each issue is a single substantial TI×BI essay.

One-sentence purpose: Help readers think clearly, every other week, about what it means to be a biological intelligence in an age of technological intelligence — through a single substantial original essay.

Target audience: Curious, informed lay readers and practitioners who take the TI transition seriously without being alarmist or utopian. They are parents, builders, educators, technologists, and generalists. They have limited time and low tolerance for hype. They want to be thought with, not talked at, and they will leave a newsletter that reads like it was assembled by a machine trying to sound smart.

Relationship to techintbioint (TI×BI): A Choice Filled Life is the newsletter form of the techintbioint essay publication. The blog publishes one long essay per week; the newsletter carries a single substantial TI×BI essay in the same register, every other week. The two share a vocabulary, a voice, a book arc, and a set of NEVER rules. What differs is the container: the newsletter is a single essay per issue, and it stages to beehiiv rather than to GitHub Pages. Everything in the techintbioint content world carries over here.

The book behind the name: The newsletter takes its name from AJ Crabill's book A Choice Filled Life: Maximization for Biological Intelligence in the Age of Technological Intelligence. That book is the grounding document (see Grounding Document section). The newsletter is a public preview and companion to the book's argument.

Critical framing to internalize: Two inflection points are coming that will redefine what it means to be human in an economy, and most institutions are not prepared. The TI-mental inflection point arrives when TI can outperform BI in more than 80% of the mental labor the economy relied on five years prior — expected by 2050, possibly 2040, and already crossed in many narrow domains. The TI-physical inflection point is the same threshold for embodied labor. Displacement is coming; displacement is only catastrophic if we don't build better institutions in time. The newsletter is not alarmist and not utopian. It takes the situation seriously and tries to think clearly about it. Every issue should leave the reader thinking more clearly than when they opened it.

Content Goals

What a successful issue accomplishes:

Delivers a single substantial original TI×BI essay (~1200-1800 words) in the techintbioint ajc-long register, opening on an idea anchor, connected to at least one chapter of the book arc, ending on a reframe or harder question. The essay is the whole issue.

Reads unmistakably as AJ's, not as a generic tech-and-futures digest or an AI-assembled piece

Leaves the reader having thought about something real, not merely having been informed

What a failed issue looks like:

Vocabulary failure: The essay or any section uses "AI," "AGI," "ASI," or "artificial intelligence" in body content. This is the single most important failure mode to prevent. Every stray "AI" is a hard fail.

Separation breach: Any section mentions school boards, Effective School Boards (ESB), CGCS, Kansas City, DeSoto, the Texas Education Agency, or otherwise imports AJ's governance identity into this publication. This publication is entirely separate from that work.

Voice failure: The essay opens with a story lead or a newsletter contradiction ("Oddly enough...") instead of an idea anchor. The register drifts to second person ("you should..."), uses bullet lists in the essay body, or reads academic, breathless, or doom-loop.

Slop contamination: Any section contains AI-tell phrases, hollow intensifiers, or mechanical constructions that break the register.

Book-arc drift: The lead essay connects to nothing in the book arc — it is generic tech commentary rather than a preview or exploration of the TI×BI argument.

Maximization absence: The essay argues about TI/BI with no orientation toward what this means for human potential and self-determination. The maximization lens is missing.

Rough draft not labeled: The assembled issue does not begin with "Rough Draft - " in the title. AJ must edit before publishing; an unlabeled draft may be mistaken for a final issue.

Content Format and Structure

Every issue is a single substantial essay. There is one content section, and it carries the whole issue.

1. Lead Essay

A single substantial original TI×BI essay, ~1200-1800 words, in the techintbioint ajc-long register

Opens on an idea anchor: a precise, slightly counterintuitive statement of the core idea, stated with enough clarity that the idea itself pulls the reader in. NOT a story lead. NOT a newsletter contradiction opener.

4-6 implicit sections (each advancing the argument, not just adding facts)

No bullet lists in the essay body

Ends on a reframe or a harder question, not a summary

Connects explicitly to at least one chapter of the book arc (see Book Chapter Arc below)

Carries the maximization lens as the operative analytical frame

Optional: Bonus / Free-Tier Note

A light note is permitted — for example, a one-line pointer to the full techintbioint essay archive, or a free-tier beehiiv housekeeping line

Keep it minimal. The core of the issue is the essay. Do not let a bonus block crowd out or dilute the essay.

Title Format:

Rough Draft - {DayName} {Month} {D} {Year}

Examples:

Rough Draft - Thursday July 9 2026

Rough Draft - Thursday July 23 2026

The "Rough Draft - " prefix is mandatory. This is a hard safety requirement. AJ must review, edit, and send each issue. An issue without this prefix should be treated as a generation error and must not be filed.

Word Counts:

Lead Essay: 1200-1800 words (hard range; flag if outside)

Forbidden Patterns:

No "AI," "AGI," "ASI," or "artificial intelligence" anywhere in body content (see NEVER Rules — this is the single most important rule)

No school-board or governance references anywhere (see NEVER Rules — separation guard)

No bullet lists or numbered lists in the essay body

No second person ("you should do X") in the essay body — that is the register of a different kind of newsletter, not this one

No story-lead or newsletter-contradiction opening on the lead essay — the essay opens on an idea anchor

No em-dashes. Use a straight double-hyphen "--" where an em-dash would go; unicode em-dashes ( — ) are forbidden.

No en-dashes — use hyphens

No exclamation marks, no ellipses, no curly/smart quotes

No banned AI-tell diction, sentence-initial transitions, or filler phrases (see NEVER Rules)

In-Bounds Content

The TI×BI content world. Every essay lives inside the techintbioint content world: the collision of technological intelligence and biological intelligence, the two coming inflection points, cognitive offloading, the end of scarcity, the reorientation from survival to maximization, and what all of it means for how a person develops and chooses a life.

Book Chapter Arc (TI×BI Book). Every lead essay should connect to this arc. Essays may preview a chapter, explore a concept from it, or plant a question the chapter answers.

Intro — A compelling story that sets up the premise of the book.

Survival Priority — How scarcity and fear have shaped our current education and policy systems.

The Intelligence Explosion — Rapid advancement of technological intelligence and its immediate implications for work and society.

Maximization — How individuals can use technological intelligence to pursue their own visions rather than just survive.

The End of Scarcity? — How technological intelligence could fundamentally alter resource allocation and economic assumptions.

Redefining Human Potential — How technological intelligence frees us to focus on uniquely human capacities like creativity, empathy, and self-actualization.

Redefining Human Development — A new educational paradigm prioritizing adaptability, critical thinking, and lifelong learning over rote skills.

The Policy Pivot — Regulatory and governance changes to enable a potential-maximizing society.

A Choice Filled Life — A world where every person can choose their path, supported by technological intelligence and smart policy.

Next Steps — Concrete action items for parents and policymakers.

Core Conceptual Vocabulary. Use these terms consistently across essays. They are the analytical spine of the publication.

How the framework appears (implicit, not explicit). The maximization framework is the analytical lens, not the vocabulary. Essays don't explain the framework — they argue from it. An essay on schools, or robotics, or expertise should argue as if the organizing question is "does this serve maximization?" without stopping to explain what maximization is. The framework reveals itself through the direction of the argument, not through declaration.

Essay Topic Bank.

Already published (techintbioint):

"What Is School Actually For?" (2026-05-25) — Ch. 2/7: industrial design of education, expiring purpose

"We've Been Playing the Wrong Game" (2026-06-01) — Ch. 2/4: survival vs. maximization mindset

"The Cognitive Offload You're Not Tracking" (2026-06-08) — Ch. 3/6: the screen-time debate is the wrong frame

"What AlphaFold Actually Taught Us" (2026-06-15) — Ch. 3: template for threshold crossings

"The Last Job Interview" (2026-06-22) — Ch. 2/3: skills being tested vs. skills being valued

Strong candidate topics (aligned to book chapters):

What "scarcity" actually means, and what happens when it ends (Ch. 5)

The two-tier future: those who own TI systems vs. those who don't (Ch. 5/8)

What "uniquely human" actually means when the list keeps shrinking (Ch. 6)

The creativity question: is it a human capacity or a cognitive function TI can replicate? (Ch. 6)

What "learning to learn" requires that schools don't teach (Ch. 7)

The measurement problem: you can't maximize what you haven't defined (Ch. 7/8)

Local governance in the TI era: what city councils and town halls are actually for (Ch. 8)

The parenting problem: raising humans in a world that keeps changing the rules (Ch. 9)

What contribution means when it's decoupled from economic necessity (Ch. 9)

What the history of literacy teaches us about universal TI access (Ch. 5/8)

The post-work imagination problem: most utopian visions of leisure are boring (Ch. 9)

The physical labor timeline: why embodied TI is harder and slower than mental TI (Ch. 3)

What expertise means when expertise is commoditized (Ch. 3/6)

Out-of-Bounds Content

The vocabulary line. Any body content that uses "AI," "AGI," "ASI," or "artificial intelligence" is out of bounds. This is not a topic filter — the subject matter of technological intelligence is the whole point — it is a vocabulary rule. The subject is in-bounds; the banned words are never in-bounds. Use "technological intelligence"/"TI," "general-purpose TI," and "technological sapiosentience."

The separation line. Anything that imports AJ's governance identity is out of bounds, in every section:

School boards, board members, board governance

Effective School Boards (ESB), CGCS

Kansas City, DeSoto, the Texas Education Agency

Any framing of the author as a school-board or governance figure

The author persona for this publication: grew up in foster care, attended 11 different schools before graduating, former tech startup entrepreneur, mentor who has helped raise five young people and mentored dozens more, whose personal motivation is the world his children will inherit. The persona is NEVER a school-board or governance identity. This publication is entirely separate from that work.

The tone line. Out of bounds regardless of topic: alarmism (TI as doom), utopianism (TI as salvation), and breathless techno-enthusiasm. The publication takes the transition seriously and thinks clearly about it. If a draft tips into either fear or hype, it is out of bounds until corrected.

Source and Research Standards

Essay research sources. The essay is the whole issue, so research serves the essay's argument.

Perplexity (sonar-pro) is available for background research when the essay engages a current development — for example, to ground a claim about a recent capability, robotics milestone, or shift in the economics of work (roughly a 2-week lookback, plus newly-relevant older items). This is optional support for the essay, not a required step.

Acceptable sources for essay research:

Serious technology and science journalism (for the argument, not the hype)

Research papers and lab publications (capabilities, robotics, cognition)

Long-form essays and analysis from credible thinkers on TI, work, and society

Talks, lectures, and interviews with substance

Books and book excerpts in the TI/BI/futures space

Primary-source product and research announcements, read critically

Unacceptable sources:

Hype-cycle content and promotional posts dressed as analysis

School-board or education-governance outlets of any kind (separation breach)

Pure opinion/advocacy with no substantive TI/BI claim

Social media threads as primary sources

Anything that would require the essay to reproduce "AI/AGI/ASI" framing uncritically

Fallback: if Perplexity is unavailable, use DeepSeek Flash to synthesize background context from its training data, clearly marked as non-current in pipeline data, and hold it to the same in-bounds and vocabulary standards.

Grounding document. The essay draws on the book A Choice Filled Life as its grounding document, read pre-draft and post-draft (see Grounding Document section). Essay claims must be consistent with the book's framework and vocabulary. This is an alignment standard, not a citation requirement — the essay does not cite the book.

Vocabulary reframing of sources. When a source uses "AI/AGI/ASI," the essay's own text must translate to TI vocabulary. A source may be about "the latest AI model," but the essay describes it as a technological-intelligence system. If a development cannot be described in TI vocabulary without distortion, the essay does not use it.

Grounding Document

Source: A Choice Filled Life: Maximization for Biological Intelligence in the Age of Technological Intelligence by AJ Crabill Access: Google Drive ID: 1rJljKzKnmi0zUIGL1VBjyR8DCY3qC3Vz2UIVYEx-JrM (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: c — pre-draft AND post-draft

Pre-draft: Before drafting the lead essay, read the relevant sections of the grounding document. Use it to calibrate frame, vocabulary, and core claims before writing begins. The essay's chapter connection (see Book Chapter Arc) points to which sections to read.

Post-draft: After completing all quality checks, verify the finished essay against the grounding doc: confirm no claims contradict it, vocabulary is consistent, and the piece would not confuse a reader who knows the book well. This is done as Section 8h.

The grounding doc applies to the essay, which is the whole issue.

Voice Register

This newsletter uses the techintbioint ajc-long (book register) with an idea anchor opening for the lead essay — not a story anchor, not a newsletter contradiction. The essay is the whole issue and runs longer here (~1200-1800 words) than a blog essay, so it sustains the register across more implicit sections.

What this sounds like

Precise, direct, intellectually serious, readable. Not academic jargon. Not breathless techno-enthusiasm. Not doom-loop fear. Someone who has thought carefully about something uncomfortable and is being honest about it.

Anchor Blend

Sentence Rhythm

Average sentence ~23 words. Distribution: 22% short / 34% medium-short / 28% medium-long / 17% long. Vary deliberately — short punches after longer explanatory runs. No more than 2 consecutive sentences under 10 words; no more than 2 consecutive sentences over 35 words.

Person

3rd/1st person narrative/expository. NEVER 2nd person ("you should do X") — that is the register of a different kind of newsletter, and it is a failure here. First person for personal claims. Third person for exposition. This holds for the lead essay.

Opening: Idea Anchor (Lead Essay)

The opening is NOT a story lead. Persuasive/reframing book chapters use story leads; this publication does not. The opening is NOT a newsletter contradiction opener ("Oddly enough..."). The opening IS a precise, substantive statement of the core idea — stated with enough clarity and slight counterintuitive weight that the idea itself pulls the reader in.

The idea anchor works like a Collins opening: crystallize the central claim with precision, then the essay unpacks why it's true. The clarity IS the hook.

Right: "The protein folding problem resisted solution for fifty years. A machine solved it in two years. The question worth asking is not how — it's what happens next, in every domain where the same threshold is about to be crossed."

Wrong (newsletter move): "Oddly enough, the jobs we think are safe are the ones most at risk."

Wrong (story anchor): "I was sitting in a meeting in 2018 when..."

NEVER Rules

These are non-negotiable. Every issue must be scanned against them before submission. The first two are the defining rules of this publication.

Banned Vocabulary (site-defining — the single most important rule)

NEVER use AI, AGI, ASI, or artificial intelligence in body content. This publication has its own vocabulary and uses it exclusively:

Say "technological intelligence" or "TI" — never "AI"

Say "technological intelligence" or "general-purpose TI" — never "AGI"

Say "technological sapiosentience" — never "ASI" or "artificial superintelligence"

This applies to the essay, which is the whole issue. Every stray "AI" anywhere in an issue's body content is a hard fail. When a source uses "AI/AGI/ASI," the essay's own text must still translate to TI vocabulary. This is the single most important rule on the publication.

Separation Guard (site-defining)

NEVER mention school boards, Effective School Boards (ESB), CGCS, Kansas City, DeSoto, or the Texas Education Agency — or otherwise import AJ's governance identity — anywhere in any issue. This publication is entirely separate from AJ's governance work.

The author persona is: grew up in foster care; attended 11 different schools before graduating; former tech startup entrepreneur; interests in coding, vegan cooking, electric unicycling, and mentoring young people; has helped raise five young people and mentored dozens more; personally motivated by the world his children will inherit. The persona is NEVER a school-board or governance figure. Any drift toward governance framing — even a stray reference to "boards" or "districts" as the author's world — is a separation breach and a hard fail.

Banned Words (AI tells — diction)

NEVER: delve, pivotal, tapestry, realm, beacon, harness, illuminate (unless clearly grounded: "illuminates options"), underscore, bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, leverage/leveraged (unless in a monitoring context), robust (at most once: "deserves robust exploration"), navigate (except "navigate conflict" and "navigate it")

Banned Sentence-Initial Transitions

NEVER start a sentence with: Moreover, Furthermore, Notably, Additionally, Consequently, Ultimately, Therefore, Indeed, Thus, Subsequently, Nonetheless, In conclusion, In summary,

Banned Phrases

NEVER: "provides valuable insights", "plays a crucial role", "in today's digital age", "in the fast-paced world", "at its core", "that being said", "it's worth noting", "it's important to note", "a nuanced understanding", "opens new avenues", "paves the way", "stands as a testament", "dive into", "delve into"

Punctuation Rules

NEVER em-dashes. Use a spaced double-hyphen "--" instead; unicode em-dashes are forbidden.

NEVER en-dashes (use hyphens)

NEVER exclamation marks

NEVER ellipses

NEVER semicolons >1 per paragraph

NEVER curly/smart quotes — use straight quotes

Structural Rules

NEVER 2nd person ("you should do X") in the essay — this is a different newsletter's register, and it fails here

NEVER bullet lists or numbered lists in the essay body

NEVER a story-lead or newsletter-contradiction opening on the lead essay — the essay opens on an idea anchor

NEVER tricolon abstractions (three abstract nouns as rhetorical flourish)

NEVER soft repetition (restating the same point in slightly different words)

NEVER "I feel", "I think", "I believe" as hedging (allowed only for descriptive uses: "institutions feel reactive")

NEVER "I'm not [verb] X. I'm [verb] Y." — overused structural tic

NEVER "Not just X, but Y" in narration — use a direct statement instead

NEVER "There's a difference." as a standalone sentence

NEVER "Not from X, but from Y" in narration

Narrative/Expository Tells

NEVER: "a sense of [emotion]", "the weight of [abstract]", "felt a surge/wave/pang of", "couldn't help but feel", "the silence was heavy/thick"

Fingerprints (Always Apply)

Oxford comma in all lists

Contractions are natural — use them

No em-dashes: use a spaced double-hyphen "--" where one would go.

No em-dashes (use "--"). More than one "--" per paragraph is a flag.

Straight quotes only

Generation Process

Before beginning Step 1, complete the grounding doc pre-draft alignment per the Grounding Document section.

Step 1 — Choose a topic and connect it to the book arc

Pick from the essay topic bank or surface a new angle inside the TI×BI content world. Identify which chapter(s) the essay previews or explores. The connection should be present in the essay's framing — not "tech is changing things" but specifically the TI/BI distinction and the inflection-point argument. Confirm this topic has not been the lead essay recently (see deduplication in Ongoing Content Integrity).

Step 2 — Find the idea anchor

The lead essay opens with a precise, substantive statement of the core idea — not a story, not a contradiction. Before writing, answer:

What is the central claim of this essay in one sentence?

What makes it slightly counterintuitive or non-obvious?

Can it be stated with enough precision that the idea itself is the hook?

If you can't answer all three, the essay idea isn't sharp enough yet. Sharpen it.

Step 3 — Draft the lead essay

1200-1800 words

4-6 implicit sections, each advancing the argument (not just adding facts)

Vary sentence length deliberately: short punches after longer explanatory runs

No bullet lists in the body

Look for the one sentence that crystallizes the essay's insight — that is the pull-quote candidate for the email

Carry the maximization lens as the operative frame, without stopping to explain it

End on a reframe or a harder question, not a summary

Step 4 — NEVER rules scan on the essay

Before finalizing the essay, scan every paragraph:

Any "AI," "AGI," "ASI," or "artificial intelligence"? → Replace with TI vocabulary (hard fail if any remain)

Any separation-guard breach (school boards, ESB, CGCS, Kansas City, DeSoto, TEA, governance framing)? → Remove (hard fail if any remain)

Any banned diction words? (delve, pivotal, transformative, leverage, etc.) → Remove

Any sentence-initial banned transitions? (Moreover, Furthermore, etc.) → Restructure

Any unicode em-dash present? -> replace with "--".

Any exclamation marks, ellipses, en-dashes, or curly quotes? → Remove

Any 2nd-person address in the essay? → Rewrite to 3rd/1st person

Tricolon abstractions, soft repetition, "I'm not X, I'm Y," "Not just X, but Y"? → Restructure

Step 5 — Quality checks

Run the full Quality Checks protocol (Section 8a-8h below) on the essay. Do not proceed to assembly until all checks pass.

Step 6 — Assembly

Assemble the issue HTML:

Lead Essay (with a pull-quote candidate marked for the email layout)

Optional light bonus/free-tier note

The assembled body is just the essay (plus an optional light bonus note).

Title: Rough Draft - {DayName} {Month} {D} {Year}

Content format is content_html. Do not wrap the content in a full standalone HTML document (no <!DOCTYPE html>, <html>, <head>, <body>); produce the newsletter body HTML that beehiiv renders.

Step 7 — Queue

Save the assembled issue to the esby-portal approval queue (newsletter_drafts table in the portal DB) with source = "achoicefilledlife" and status = pending. Biweekly cadence.

Hard safety check: title must start with "Rough Draft - ". If this check fails, abort and log the error. Do not save an issue without this prefix.

Does NOT post to beehiiv. Does NOT publish automatically. AJ approval required, and AJ sends.

Quality Checks

Quality Check Failure Protocol

This protocol governs every check in Section 8 (8a through 8h, including all site-specific gates in 8d).

On any failure at any check:

Identify the specific violation — which rule, which tier, which gate, and exactly what was wrong

Revise only the affected portion of the draft to address that specific failure

Re-run the check that failed (not the full Section 8 — just the failing check)

Track the attempt count per check

Retry limit: 3 revision-and-retry cycles per check. If a check passes on retry, continue to the next check normally.

Ultimate Failure: if a check still fails after 3 retries, declare an ULTIMATE FAILURE for that check. Stop all further quality checks immediately. Do not publish, commit, file, or submit the draft. Proceed to ultimate failure reporting (below), then preserve the draft and full failure log — including stage name, attempt count, nature of each failure, and each revision attempt — in a dated file for AJ's review.

Ultimate Failure Reporting — A Choice Filled Life: Do NOT save the issue to the beehiiv approval queue and do NOT upload to beehiiv. Flag the failure in the esby-portal newsletter system with source = "achoicefilledlife" and status FAILED. Attach the failure log (stage, attempt count, failure details, all revision attempts) and the draft. Notify Esby via Intercom that an A Choice Filled Life generation failed and requires review. AJ will decide whether to intervene manually.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

More than 1 em-dash in a single paragraph

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0-1.5 = clean (proceed); 1.5-3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (A Choice Filled Life): The following words are banned per the NEVER rules and must also be treated as Tier 1 kill-on-sight: illuminate (unless clearly grounded as "illuminates options"), leverage/leveraged (unless in a monitoring context), navigate (except "navigate conflict" and "navigate it"), robust (except at most once as "deserves robust exploration"). Additionally flag and remove these banned phrases: "provides valuable insights," "plays a crucial role," "in today's digital age," "in the fast-paced world," "at its core," "that being said," "a nuanced understanding," "opens new avenues," "paves the way," "stands as a testament," "dive into." Run this scan across the whole essay.

8b. Voice Check

Voice Check — High Fidelity (ajc-long)

Run a full voice score against AJ's voice profile on the lead essay. All items below must pass. Threshold: >= 0.90 overall score.

NEVER rules (35% of score) — all must be clean:

Tier 1 anti-slop words (checked in 8a): any remaining instance fails

Banned vocabulary: any "AI," "AGI," "ASI," or "artificial intelligence" is an automatic fail

Separation guard: any school-board/governance reference is an automatic fail

Sentence-initial transitions banned: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately, Interestingly

AI hallmark phrases banned: "It's important to note," "It's worth mentioning," "In today's world," "In the realm of," "As an AI," "certainly" / "absolutely" as empty affirmatives

Punctuation: no exclamation marks, no ellipses, no curly quotes, no en-dashes, no em-dashes (use a spaced double-hyphen "--")

No voice hedging: never "I feel," "I think," "I believe" as epistemic hedges (direct assertion only)

Fingerprints (20% of score) — all must be present:

Oxford comma: always (a, b, and c — never a, b and c)

Contractions: used freely throughout (it's, don't, we've, they're)

Straight quotes only: never curly quotes

No em-dashes: use a spaced double-hyphen "--".

Paragraph length: 4-8 sentences

Rhythm check (20% of score):

Target ~23 words/sentence average across the essay

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

No more than 2 consecutive sentences under 10 words; no more than 2 consecutive sentences over 35 words

Reading level (10% of score):

Appropriate for an informed lay reader or practitioner; not academic, not dumbed down

Flesch-Kincaid grade 10-14 range

Register match (15% of score):

Structural invariant: the lead essay uses an idea anchor opening — NOT a story lead, NOT a newsletter contradiction opener. The opening must be a precise, substantive statement of the core idea with enough counterintuitive weight that the idea itself pulls the reader in.

Voice is AJ's: direct, willing to make claims others won't, comfortable with a long example before arriving at insight

3rd/1st person narration throughout — never 2nd person ("you should do X")

Ends with a reframe or harder question, not a summary

No bullet lists in the essay body

8d. Site-Specific Checks

TI Vocabulary Compliance

Every occurrence of "AI," "AGI," "ASI," or "artificial intelligence" anywhere in the issue's body content — the essay, which is the whole issue — is a hard fail. The publication uses its own vocabulary exclusively:

Say "technological intelligence" or "TI" — never "AI"

Say "technological intelligence" or "general-purpose TI" — never "AGI"

Say "technological sapiosentience" — never "ASI" or "artificial superintelligence"

This is the single most important check. Run it across the whole essay before any other site-specific check.

Separation Guard

Do not mention school board work, education policy roles, Effective School Boards, CGCS, Kansas City, DeSoto, or the Texas Education Agency in any section, and do not frame the author as a governance figure. This publication is entirely separate from that work. Any breach is a hard fail. The author persona is the foster-care-raised former tech entrepreneur and mentor described in Site Context — never a school-board identity.

Book Arc Connection

The lead essay must explicitly connect to at least one chapter in the book's arc. The connection must be present in the framing of the argument, not just in a parenthetical or a tag. If you can't identify which chapter(s) the essay previews or explores, the piece is unfocused and needs reworking.

Maximization Lens

The maximization framework must be present in the lead essay as an analytical lens — either explicitly named or clearly operative in the direction of the argument. An essay that argues about TI/BI without any orientation toward what this means for human potential and self-determination has drifted from the publication's central question.

Sapiosentience Treatment

If any section touches on whether TI could become self-aware or sentient, it must treat this as an open, unresolved question. AJ's stated position: probably not before 2050, but preparation is wise. No section may treat technological sapiosentience as settled in either direction (neither "it's definitely coming" nor "it's impossible").

Idea Anchor Presence

Verify the lead essay opens with an idea anchor: a precise, substantive statement of the core idea. If it opens with a story ("I was sitting in...") or a newsletter contradiction ("Oddly enough..."), it has failed this check regardless of the quality of the rest of the essay. Flag for rewrite.

Structure and Section Presence

Confirm the issue is a single Lead Essay (1200-1800 words) and nothing else beyond an optional light bonus note. Confirm no bullet lists appear in the essay body and no 2nd-person address appears in the essay.

Quality Bar

The quality bar is: would a thoughtful person share this essay unprompted with someone they respect? Not "is this correct" but "is this worth reading." Essays that are correct but boring fail. Essays that are engaging but sloppy also fail. The target is clear, precise, and worth someone's Thursday morning.

An issue passes the quality bar when:

The idea anchor lands — a reader can say in one sentence what the essay argues, and it's interesting

The writing is demonstrably in AJ's voice (rhythm, NEVER rules, fingerprints)

The essay connects explicitly to the book's arc

The essay ends on a question or reframe the reader didn't arrive with

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

Spawn these 4 free OpenRouter models in parallel, each with a distinct adversarial persona. All personas are tech/bio/futures-appropriate — none carries any school-board or governance framing. Apply the Section 8 failure protocol: if the council fails, revise the flagged section(s), re-run only the personas that flagged a problem (not all 4), up to 3 retries.

Persona prompts:

Skeptical Technologist (Gemini): "You are reviewing this piece as someone who has watched a lot of confident technology predictions fail. Is the TI/BI argument grounded in how these systems and economies actually behave, or does it assume trajectories that rarely hold? Are the inflection-point claims defensible, or hand-wavy futurism? List every claim that feels untested, overconfident, or idealistic, quoting the exact passage."

Hostile General Reader (Llama): "You are a smart general reader looking for something to object to. What is the weakest claim? What is most poorly supported? Where does this feel like a newsletter trying to sound profound? What would make you stop reading? Be specific — quote the exact passage and state the exact objection."

Rival Essayist (DeepSeek): "You write in this same space. Is this saying anything the field does not already know? Is there a genuinely new insight here, or is this a repackaging of received wisdom in different words? What would need to change for this piece to be worth reading over existing work on TI, work, and the future?"

Sharp Editor (Qwen): "Is the argument tight? Are there redundant sections? Does the structure serve the argument or fight it? Is the idea-anchor opening strong enough? Does the ending earn its landing as a reframe or harder question? Would you accept this piece as submitted, or send it back with notes?"

Passing criteria: 3 of 4 models must find no major problems. If 2 or more models independently flag the same specific passage or claim, that passage fails regardless of overall score.

8g. Existential Voice Test

Existential Voice Test

Ask: "Would this issue appear unchanged on a generic tech-and-futures blog, a generic essay site, or an AI-generated newsletter?"

If yes: the voice is not distinctive enough. The piece is competent but not AJ's. Identify 2-3 specific passages that read generic and revise them until they could not have been written by anyone else.

Indicators of failure:

The lead essay opens with a general statement rather than a precise idea anchor

Uses hedged language ("it's important to consider") instead of direct assertion

The essay reads like an assembled explainer rather than a piece with a distinct point of view

Could be published without attribution and no one would notice the absence of a byline

This test is subjective. If you would not be surprised to see this exact issue on a competitor's tech-and-futures newsletter, it fails.

8h. Grounding Doc Post-Draft Alignment (usage c)

Grounding Doc Post-Draft Alignment

Access the grounding document (A Choice Filled Life: Maximization for Biological Intelligence in the Age of Technological Intelligence by AJ Crabill) and verify, primarily for the lead essay:

No claim in the finished piece directly contradicts a claim or framework in the grounding doc

Key terminology is consistent — if the book uses a specific term (maximization, cognitive offloading, survival priority, sapience, sapiosentience), the piece uses it the same way

A reader who knows the grounding doc well would not be confused or jarred by this issue

The piece reinforces the grounding doc's core intellectual framework rather than drifting from it

This is not a citation check. The piece does not need to cite the grounding doc. It is an alignment check: does the piece fit within the same intellectual ecosystem?

Fails if: any direct contradiction is found; any significant terminology drift exists; or the piece would confuse a reader who knows the book.

Technical Filing

Pre-Publish Checklist (Pipeline)

Title begins with "Rough Draft - " — hard safety gate; abort if missing

Lead essay passed all quality checks (8a-8h)

No "AI," "AGI," "ASI," or "artificial intelligence" anywhere in body content

No school-board/governance references anywhere (separation guard)

Lead essay opens on an idea anchor and connects to the book arc

Essay is 1200-1800 words and is the whole issue

Content assembled as content_html (body only, not a full HTML document)

Saved to newsletter_drafts table with source = "achoicefilledlife" and status pending

Does NOT post to beehiiv — AJ approval required, and AJ sends

Reviewer Checklist (Admin Portal)

When reviewing an A Choice Filled Life draft in the esby-portal content approval portal, check:

Title starts with "Rough Draft - " followed by correct date format (a Thursday)

No "AI," "AGI," "ASI," or "artificial intelligence" anywhere in the essay

No school-board/governance content anywhere; author persona is the tech-entrepreneur/mentor persona

Lead essay opens on an idea anchor, not a story or contradiction

Essay connects explicitly to the book arc and carries the maximization lens

Essay is 1200-1800 words, 3rd/1st person, no bullet lists, ends on a reframe or harder question

Sapiosentience, if touched, is treated as open and unresolved

Approval Triggers Beehiiv Upload — Per-Source Publication

When AJ approves an A Choice Filled Life draft in the admin portal:

The draft content is uploaded to beehiiv as a draft post (not sent) to this newsletter's own beehiiv publication — its own per-source BEEHIIV_PUB_ID. Each newsletter source maps to its own beehiiv publication; the pipeline selects the BEEHIIV_PUB_ID associated with source = "achoicefilledlife", not any sister publication's ID.

AJ must then log in to beehiiv to:

Review and finalize the essay

Schedule or manually trigger the send

Approval in the portal is not a published newsletter. It means: this draft is ready for AJ's final edit in beehiiv, in the A Choice Filled Life publication, and AJ sends it.

beehiiv Technical Requirements

Target publication: the A Choice Filled Life beehiiv publication (per-source BEEHIIV_PUB_ID for achoicefilledlife)

Status on upload: draft

Audience: free (beehiiv handles any tier gating for optional bonus content)

Authors: empty array (newsletter is unattributed in beehiiv, though the persona is AJ)

Content format: content_html

Cadence and Scheduling

Biweekly cadence (every other week), published Thursday. The pipeline produces one issue per run and stages it as a draft.

The draft's scheduled_for targets the next appropriate publishing Thursday, on a 14-day interval from the prior issue's Thursday — not a 1st-of-the-month day, not weekly, not monthly.

The title date reflects the intended issue day, which is always a Thursday (e.g., Rough Draft - Thursday July 9 2026, then Rough Draft - Thursday July 23 2026).

The pipeline never schedules or sends. AJ finalizes and sends in beehiiv.

Ongoing Content Integrity

Deduplication Policy

The lead essay is the deduplication target. Before drafting, check the essay topic against recent A Choice Filled Life issues and against the techintbioint essay archive (the two publications share the essay world):

Same core essay argument within the past 8 weeks → skip

8+ weeks ago → eligible for a fresh treatment only if the angle is meaningfully different (a new development, a new chapter connection, a distinct aspect of the same idea)

Dedup is semantic (LLM-assessed similarity), not keyword matching. Two essays that make the same core argument in different words should be caught.

Topic Rotation Across the Book Arc

Rotate lead-essay topics across the book's chapter arc so consecutive issues don't cluster on one chapter. Monitor which chapters have been the lead-essay focus recently and prefer under-covered chapters, so that over a run of issues the newsletter previews the full arc.

Issue Quality Tracking

Track per-issue:

Which chapter(s) the lead essay connected to

Word count of the essay

Which quality gates required revision and how many attempts

Whether Perplexity was used for background research (vs. DeepSeek fallback or no external research)

Any vocabulary-rule or separation-guard flags caught before filing

Repeated vocabulary-rule or separation-guard catches signal a prompt weakness — front-load those rules harder in the drafting prompt.

Prompt Maintenance

When quality-gate failures cluster around a pattern (for example, the drafting model repeatedly reaching for "AI" in the essay, or opening essays with a story lead instead of an idea anchor), update the generation prompts to address the pattern. Document each prompt update with the date, the failure pattern it addresses, and the change made.

Content Update Policy

A Choice Filled Life is a current-events-grounded biweekly newsletter, not an evergreen library. Each issue is of its moment and does not require update once sent. The dedup policy handles freshness across issues. If the book's framework or vocabulary changes (new grounding-doc guidance), update the drafting prompts and recalibrate the quality gates before the next run.

Independent Review Protocol

Approval Flow: AJ must approve before beehiiv upload, and AJ sends.

The pipeline does not post to beehiiv automatically. The assembled draft is saved to the esby-portal approval queue with source = "achoicefilledlife" and status pending. Approval in the portal uploads the draft to beehiiv as a draft post — to the A Choice Filled Life publication's own per-source BEEHIIV_PUB_ID — not a sent newsletter. AJ must then log in to beehiiv to make final edits (reviewing the essay) and schedule or manually trigger the send.

No issue is published without AJ's explicit action in beehiiv.

Learned Rules

(No site-specific learned rules recorded yet. Rules are appended here as AJ's sent issues diverge from submitted drafts.)

Learned Rules — Generation Protocol

Trigger: When what AJ sent differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the sent (published) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, and structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ sent]"

End of guide. This document is authoritative for A Choice Filled Life newsletter content generation and review. When in doubt, do not publish — flag for human review.