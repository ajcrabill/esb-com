title: TI×BI Content Generation Guide type: content-guide site: TI×BI (techintbioint) updated: 2026-07-08

LLM Configuration

Models are configured centrally -- do not hardcode model slugs in this guide. See System Administration -> Model Registry (backed by site-pipeline/config.py and the per-site overrides in pipeline_sites). The registry is the single source of truth, so the docs never drift from what the pipeline actually runs.

Roles:

Writing (drafting): the configured write model, with automatic fallback to the configured write-fallback model on error or empty output.

Everything else (research, quality checks, anti-slop scanning, council review): the configured research model.

Live web search: the configured search model.

To change any of these, edit the Model Registry (or a per-site override) -- never this section.

Site Context

Domain: techintbioint.com Tagline: "Two intelligences are colliding. One of them is you." Cadence: One essay per week, published Monday Author voice: AJ Crabill Pipeline site_id: techintbioint Pipeline site_name: TI×BI

What This Site Is

TI×BI is a weekly essay publication about the intersection of technological intelligence (TI) and biological intelligence (BI). It is the public preview for a book in progress. The book's chapter arc should inform what topics the blog explores and in what sequence.

The central argument: two inflection points are coming that will redefine what it means to be human in an economy, and most institutions are not prepared.

TI-mental inflection point: When TI can outperform BI in >80% of mental labor the economy relied on 5 years prior. Expected by 2050, possibly 2040. Many domains have already crossed it.

TI-physical inflection point: Same threshold for physical labor (embodied robots). Also by 2050.

Not predicting: Technological sapiosentience (self-aware AI), dystopia, or that all human work disappears.

Is predicting: Displacement — and displacement is only catastrophic if we don't build better institutions in time.

The site is NOT alarmist, NOT utopian. It takes the situation seriously and tries to think clearly about it.

Book Chapter Arc (TI×BI Book)

Every blog post should connect to this arc. Posts may preview a chapter, explore a concept from it, or plant a question the chapter answers.

Intro — A compelling story that sets up the premise of the book.

Survival Priority — How scarcity and fear have shaped our current education and policy systems.

The Intelligence Explosion — Rapid advancement of technological intelligence and its immediate implications for work and society.

Maximization — How individuals can leverage technological intelligence to pursue their own visions rather than just survive.

The End of Scarcity? — How technological intelligence could fundamentally alter resource allocation and economic assumptions.

Redefining Human Potential — How technological intelligence frees us to focus on uniquely human capacities like creativity, empathy, and self-actualization.

Redefining Human Development — A new educational paradigm prioritizing adaptability, critical thinking, and lifelong learning over rote skills.

The Policy Pivot — Regulatory and governance changes to enable a potential-maximizing society.

A Choice Filled Life — A world where every person can choose their path, supported by technological intelligence and smart policy.

Next Steps — Concrete action items for parents and policymakers.

Author Background (for About page / bio lines)

Grew up in foster care; attended 11 different schools before graduating

Former tech startup entrepreneur

Coding, vegan cooking, electric unicycling, mentoring young people

Has helped raise five young people, mentored dozens more

Personal motivation: the question of what world his children inherit is not abstract

Do not mention: school board work, education policy roles, Effective School Boards, CGCS, Kansas City, DeSoto, Texas Education Agency. This site is entirely separate from that work.

Core Conceptual Vocabulary

Terms to use (always)

Terms never to use except when quoting someone else

AI — say "technological intelligence" or "TI"

AGI — say "technological intelligence" or "general-purpose TI"

ASI — say "technological sapiosentience" if that's what's meant

Artificial intelligence — same rule

How the framework appears in posts (implicit, not explicit)

The maximization framework is the analytical lens, not the vocabulary. Posts don't explain the framework — they argue from it. A post on schools should argue as if the author's organizing question is "does this serve maximization?" without stopping to explain what maximization is. The framework reveals itself through the direction of the argument, not through declaration.

Essay Topics Bank

Already published

"What Is School Actually For?" (2026-05-25) — Chapter 2/7 preview: Industrial design of education, expiring purpose

"We've Been Playing the Wrong Game" (2026-06-01) — Chapter 2/4 preview: Survival vs. maximization mindset

"The Cognitive Offload You're Not Tracking" (2026-06-08) — Chapter 3/6 preview: Screen time debate is the wrong frame

"What AlphaFold Actually Taught Us" (2026-06-15) — Chapter 3 preview: Template for threshold crossings

"The Last Job Interview" (2026-06-22) — Chapter 2/3 preview: Skills being tested vs. skills being valued

Strong candidate topics (aligned to book chapters)

What "scarcity" actually means, and what happens when it ends (Ch. 5)

The two-tier future: those who own TI systems vs. those who don't (Ch. 5/8)

What "uniquely human" actually means when the list keeps shrinking (Ch. 6)

The creativity question: is it a human capacity or a cognitive function that TI can replicate? (Ch. 6)

What "learning to learn" requires that schools don't teach (Ch. 7)

The measurement problem: you can't maximize what you haven't defined (Ch. 7/8)

Local governance in the TI era: what city councils and town halls are actually for (Ch. 8)

The parenting problem: raising humans in a world that keeps changing the rules (Ch. 9)

What contribution means when it's decoupled from economic necessity (Ch. 9)

What the history of literacy teaches us about universal TI access (Ch. 5/8)

The post-work imagination problem: most utopian visions of leisure are boring (Ch. 9)

The physical labor timeline: why embodied TI is harder and slower than mental TI (Ch. 3)

What expertise means when expertise is commoditized (Ch. 3/6)

Grounding Document

Source: A Choice Filled Life: Maximization for Biological Intelligence in the Age of Technological Intelligence by AJ Crabill Access: Google Drive ID: 1rJljKzKnmi0zUIGL1VBjyR8DCY3qC3Vz2UIVYEx-JrM (read via mcp__c7e8b32b-5a12-4797-a6d1-d08c6ac76fa5__read_file_content) Usage pattern: c — pre-draft AND post-draft

Pre-draft: Before drafting, read the relevant sections of the grounding document. Use it to calibrate frame, vocabulary, and core claims before writing begins.

Post-draft: After completing all quality checks, verify the finished piece against the grounding doc: confirm no claims contradict it, vocabulary is consistent, and the piece would not confuse a reader who knows the book well. This is done as Section 8h.

Voice Register

This site uses the ajc-long (book register) with an idea anchor opening — not a story anchor, not a newsletter contradiction.

What this sounds like

Precise, direct, intellectually serious, readable. Not academic jargon. Not breathless techno-enthusiasm. Not doom-loop fear. Someone who has thought carefully about something uncomfortable and is being honest about it.

Anchor Blend

Sentence Rhythm

Average sentence ~23 words. Distribution: 22% short / 34% medium-short / 28% medium-long / 17% long. Vary deliberately — short punches after longer explanatory runs.

Person

3rd/1st person narrative/expository. NOT 2nd person ("you should do X") — that is the newsletter register. First person for personal claims. Third person for exposition.

Opening: Idea Anchor

The opening is NOT a story lead (persuasive/reframing book chapters use story leads — this site does not). The opening is NOT a newsletter contradiction opener ("Oddly enough..."). The opening IS a precise, substantive statement of the core idea — stated with enough clarity and slight counterintuitive weight that the idea itself pulls the reader in.

The idea anchor works like a Collins opening: crystallize the central claim with precision, then the essay unpacks why it's true. The clarity IS the hook.

Right: "The protein folding problem resisted solution for fifty years. A machine solved it in two years. The question worth asking is not how — it's what happens next, in every domain where the same threshold is about to be crossed."

Wrong (newsletter move): "Oddly enough, the jobs we think are safe are the ones most at risk."

Wrong (story anchor): "I was sitting in a meeting in 2018 when..."

NEVER Rules

These are non-negotiable. Every post must be scanned against them before submission.

Banned Words (AI tells — diction)

NEVER: delve, pivotal, tapestry, realm, beacon, harness, illuminate (unless clearly grounded: "illuminates options"), underscore, bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, leverage/leveraged (unless in monitoring context), robust (at most once: "deserves robust exploration"), navigate (except "navigate conflict" and "navigate it")

Banned Sentence-Initial Transitions

NEVER start a sentence with: Moreover, Furthermore, Notably, Additionally, Consequently, Ultimately, Therefore, Indeed, Thus, Subsequently, Nonetheless, In conclusion, In summary,

Banned Phrases

NEVER: "provides valuable insights", "plays a crucial role", "in today's digital age", "in the fast-paced world", "at its core", "that being said", "it's worth noting", "it's important to note", "a nuanced understanding", "opens new avenues", "paves the way", "stands as a testament", "dive into"

Punctuation Rules

NEVER em-dashes (use a spaced double-hyphen -- where an em-dash would go, sparingly, or split the sentence)

NEVER en-dashes (use hyphens)

NEVER exclamation marks

NEVER ellipses

NEVER semicolons >1 per paragraph

NEVER curly/smart quotes — use straight quotes

Structural Rules

NEVER tricolon abstractions (three abstract nouns as rhetorical flourish)

NEVER soft repetition (restating the same point in slightly different words)

NEVER "I feel", "I think", "I believe" as hedging (allowed only for descriptive uses: "boards feel reactive")

NEVER "I'm not [verb] X. I'm [verb] Y." — overused structural tic

NEVER "Not just X, but Y" in narration — use direct statement instead

NEVER "There's a difference." as a standalone sentence

NEVER "Not from X, but from Y" in narration

Narrative/Expository Tells

NEVER: "a sense of [emotion]", "the weight of [abstract]", "felt a surge/wave/pang of", "couldn't help but feel", "the silence was heavy/thick"

Fingerprints (Always Apply)

Oxford comma in all lists

Contractions are natural — use them

No em-dashes: use a spaced double-hyphen -- where an em-dash would go

No unicode em-dashes ( — ) anywhere

Generation Process

Before beginning Step 1, complete the grounding doc pre-draft alignment per Section 4.

Step 1: Choose a topic and connect it to the book arc

Pick from the topic bank or surface a new angle. Identify which chapter(s) this post previews or explores. The connection should be explicit in the essay's framing — not "tech is changing things" but specifically the TI/BI distinction and the inflection point argument.

Step 2: Find the idea anchor

Every essay opens with a precise, substantive statement of the core idea — not a story, not a contradiction.

Before writing, answer:

What is the central claim of this essay in one sentence?

What makes it slightly counterintuitive or non-obvious?

Can it be stated with enough precision that the idea itself is the hook?

If you can't answer all three, the essay idea isn't sharp enough yet. Sharpen it.

Step 3: Draft the body

3–4 sections, each with an implicit H2 (use ## in markdown)

Each section advances the argument — it doesn't just add facts

Vary sentence length deliberately: short punches after longer explanatory runs

Look for the one sentence that crystallizes the essay's insight — that's the blockquote candidate

End with a reframe or harder question, not a summary

Step 4: Apply NEVER rules scan

Before finalizing, scan every paragraph:

Any banned words? (delve, pivotal, transformative, leverage, etc.) → Remove

Any sentence-initial banned transitions? (Moreover, Furthermore, etc.) → Restructure

Any em-dashes? (unicode — ) → Replace with a spaced double-hyphen -- or split the sentence

Any exclamation marks, ellipses, or curly quotes? → Remove

Tricolon abstractions? (three abstract nouns as flourish) → Remove

Soft repetition? → Consolidate

"I'm not X, I'm Y" formula? → Restructure

"Not just X, but Y" in narration? → Make direct statement

Step 5: Voice checklist

Opens with an idea anchor (not a story, not a newsletter contradiction)?

Sentences average ~23 words with deliberate variation?

3rd/1st person (not 2nd person)?

Oxford comma used throughout?

Uses "technological intelligence" not "AI" or "AGI" in body text?

Ends with a reframe or harder question (not a summary)?

Under 1,000 words?

No bullet lists in the body?

Step 6: Front matter

---

layout: post

title: "Title Goes Here"

date: YYYY-MM-DD

author: AJ Crabill

reading_time: 5   # estimate: word_count / 200

excerpt: "One sentence that works as a standalone teaser — precise, no hedging."

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

Step 7: Submit to pipeline

Submit to esby content pipeline with:

site_id: techintbioint

site_name: TI×BI

title: the post title

html_content: the rendered HTML of the post body (not full page, just the article content)

meta_json: {"date": "YYYY-MM-DD", "slug": "post-slug", "reading_time": N}

On approval: commit the .md file to /tmp/techintbioint-com/_posts/ and push to GitHub.

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

Ultimate Failure Reporting — TI×BI: Do NOT advance the piece to the Esby pipeline. Flag the failure in the Esby pipeline system with status FAILED. Attach the failure log (stage, attempt count, failure details, all revision attempts) and the draft. Notify Esby via Intercom message that a TI×BI generation failed and requires review.

After reporting, preserve the draft and the full failure log (stage, attempt count, nature of each failure, revision attempts) in a dated file for AJ's review.

8a. Anti-Slop Scan

Tier 1 — Kill on sight (any single occurrence fails; revise before proceeding): delve, utilize, facilitate, tapestry, paradigm, synergy, holistic, catalyze, juxtapose, myriad, plethora, pivotal, underscore (as verb), bolster, multifaceted, foster, seamless, embark, transformative, revolutionize, realm, beacon, harness (as verb)

Tier 2 — Suspicious in clusters (3 or more in a single paragraph = flag; revise that paragraph): comprehensive, cutting-edge, streamline, empower, enhance, elevate, optimize, scalable, intricate, profound, resonate, cultivate, galvanize, cornerstone, game-changer, robust, innovative

Tier 3 — Filler phrases (each one weakens the piece; eliminate all): "it's worth noting," "furthermore," "moreover," "additionally," "in conclusion," "to summarize," "it is important to," "one must consider," "at the end of the day," "when all is said and done," "it goes without saying," "needless to say," "this is a testament to"

Structural tics (each one that appears is a flag):

Paragraph opener is a transition word (Moreover, Furthermore, Notably, However, Additionally, Importantly, Ultimately)

Any em-dash (unicode — ); use a spaced double-hyphen -- instead

Soft repetition: same idea restated in different words within 3 consecutive paragraphs

Scoring: 0–1.5 = clean (proceed); 1.5–3.0 = minor revision needed before proceeding; >3.0 = full revision required before red-team

Site-specific additions (TI×BI (techintbioint)): The following words are banned per the site's NEVER rules and must also be treated as Tier 1 kill-on-sight for this site: illuminate (unless clearly grounded as "illuminates options"), leverage/leveraged (unless in a monitoring context), navigate (except "navigate conflict" and "navigate it"), robust (except at most once as "deserves robust exploration"). Additionally, the following banned phrases from the site's NEVER rules must be flagged and removed: "provides valuable insights," "plays a crucial role," "in today's digital age," "in the fast-paced world," "at its core," "that being said," "a nuanced understanding," "opens new avenues," "paves the way," "stands as a testament," "dive into."

8b. Voice Check

Voice Check — High Fidelity (ajc-long)

Run a full voice score against AJ's voice profile. All items below must pass. Threshold: ≥ 0.90 overall score.

NEVER rules (35% of score) — all must be clean:

Tier 1 anti-slop words (checked in 8a): any remaining instance fails

Sentence-initial transitions banned: Moreover, Furthermore, Notably, Additionally, Importantly, Ultimately, Interestingly

AI hallmark phrases banned: "It's important to note," "It's worth mentioning," "In today's world," "In the realm of," "As an AI," "certainly" / "absolutely" as empty affirmatives

Punctuation: no exclamation marks, no ellipses, no curly quotes, no em-dashes (use a spaced double-hyphen -- where an em-dash would go)

No voice hedging: never use "I feel," "I think," "I believe" as epistemic hedges (direct assertion only)

Fingerprints (20% of score) — all must be present:

Oxford comma: always (a, b, and c — never a, b and c)

Contractions: used freely throughout (it's, don't, we've, they're, etc.)

Straight quotes only: " and ' — never curly " " ' '

No em-dashes: use a spaced double-hyphen -- where an em-dash would go

Paragraph length: 4–8 sentences

Rhythm check (20% of score):

Target ~23 words/sentence average across the piece

Author blend: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

No more than 2 consecutive sentences under 10 words; no more than 2 consecutive sentences over 35 words

Reading level (10% of score):

Appropriate for a practitioner or informed lay reader; not academic, not dumbed down

Flesch-Kincaid grade 10–14 range

Register match (15% of score):

Structural invariant: this site uses an idea anchor opening — NOT a story lead, NOT a newsletter contradiction opener. The opening must be a precise, substantive statement of the core idea with enough counterintuitive weight that the idea itself pulls the reader in.

Voice is AJ's: direct, practitioner-grounded, willing to make claims others won't, comfortable with long examples before arriving at insight

3rd/1st person narration throughout — never 2nd person ("you should do X")

Ends with a reframe or harder question, not a summary

No bullet lists in the essay body

8d. Site-Specific Checks

TI Vocabulary Compliance

Every occurrence of "AI," "AGI," "ASI," or "artificial intelligence" in the body text is a hard fail. The site uses its own vocabulary exclusively:

Say "technological intelligence" or "TI" — never "AI"

Say "technological intelligence" or "general-purpose TI" — never "AGI"

Say "technological sapiosentience" — never "ASI" or "artificial superintelligence"

Book Arc Connection

The post must explicitly connect to at least one chapter in the book's arc. The connection must be present in the framing of the argument, not just in a parenthetical or a tag. If you can't identify which chapter(s) the post previews or explores, the piece is unfocused and needs reworking.

Maximization Lens

The maximization framework must be present as an analytical lens — either explicitly named or clearly operative in the direction of the argument. A post that argues about TI/BI without any orientation toward what this means for human potential and self-determination has drifted from the site's central question.

Sapiosentience Treatment

If the post touches on whether TI could become self-aware or sentient, it must treat this as an open, unresolved question. AJ's stated position: probably not before 2050, but preparation is wise. The post must not treat technological sapiosentience as settled in either direction (neither "it's definitely coming" nor "it's impossible").

Quality Bar

The quality bar is: would a thoughtful person share this essay unprompted with someone they respect? Not "is this correct" but "is this worth reading."

Essays that are correct but boring fail. Essays that are engaging but sloppy also fail. The target is clear, precise, and worth someone's Monday morning.

A post passes the quality bar when:

The idea anchor lands — a reader can say in one sentence what the essay argues, and it's interesting

The writing is demonstrably in AJ's voice (rhythm, NEVER rules, fingerprints)

It connects explicitly to the book's arc

It ends on a question or reframe the reader didn't arrive with

Author Attribution Guard

Do not mention school board work, education policy roles, Effective School Boards, CGCS, Kansas City, DeSoto, or the Texas Education Agency in any post. This site is entirely separate from that work.

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

Access the grounding document (A Choice Filled Life: Maximization for Biological Intelligence in the Age of Technological Intelligence by AJ Crabill) and verify:

No claim in the finished piece directly contradicts a claim or framework in the grounding doc

Key terminology is consistent — if the book uses a specific term, the piece uses it the same way

A reader who knows the grounding doc well would not be confused or jarred by this piece

The piece reinforces the grounding doc's core intellectual framework rather than drifting from it

This is not a citation check. The piece does not need to cite the grounding doc. It is an alignment check: does the piece fit within the same intellectual ecosystem?

Fails if: any direct contradiction is found; any significant terminology drift exists; or the piece would confuse a reader who knows the book.

Technical Filing

File location: /tmp/techintbioint-com/_posts/YYYY-MM-DD-slug.md Repo: ajcrabill/techintbioint-com on GitHub Deploy: GitHub Pages — auto-deploys from main branch

Filename format: YYYY-MM-DD-slug.md where the date is the Monday publish date and the slug is a lowercase, hyphenated version of the title (e.g., 2026-06-29-what-expertise-means.md).

Frontmatter fields (required):

---

layout: post

title: "Title Goes Here"

date: YYYY-MM-DD

author: AJ Crabill

reading_time: 5   # estimate: word_count / 200

excerpt: "One sentence that works as a standalone teaser — precise, no hedging."

---

Output format — critical: The generated file contains ONLY the front matter block followed by the article body HTML. Never output a full standalone HTML document. Do not include <!DOCTYPE html>, <html>, <head>, <style>, <nav>, <header>, <footer>, or <body> tags — these are all generated by the Jekyll layout. Generating a full HTML document instead of front matter + body will break the site and require editing every affected file by hand.

Git commands (after pipeline approval):

cd /tmp/techintbioint-com

git add _posts/YYYY-MM-DD-slug.md

git commit -m "Add: [Post Title] (YYYY-MM-DD)"

git push origin main

Date rules: All posts publish on Monday. The date: field in frontmatter is the publish Monday. Never backdate or forward-date outside the Monday cadence without explicit instruction from AJ.

Independent Review Protocol

Approval flow: Esby pipeline approval.

Submit the completed post to the Esby content pipeline using the pipeline tool with:

site_id: techintbioint

site_name: TI×BI

title: the post title

html_content: the rendered HTML of the post body (not full page, just the article content)

meta_json: {"date": "YYYY-MM-DD", "slug": "post-slug", "reading_time": N}

The post enters Esby's approval queue. Do not commit the file to the repo or push to GitHub until Esby's pipeline returns an approval signal.

If Esby pipeline approval is unavailable or does not respond within 72 hours: Run the draft through a final the configured write model adversarial pass as a fallback review, flag the 72-hour timeout in the session log, and proceed to commit only if the configured write model returns no blocking issues. Document the fallback in the post's commit message.

Learned Rules

No learned rules have been recorded yet. The first rules will be appended when AJ's published version differs substantively from what was submitted to the content approval system.

Learned Rules — Generation Protocol

Trigger: When what AJ published differs substantively from what was submitted to the content approval system, generate a new learned rule and append it here.

Process:

Compare the submitted version against the published (live) version

Identify every substantive edit AJ made — not typos; look for content changes, framing changes, word choice changes, structural changes

For each cluster of related edits, derive the governing rule

Append the rule using this format:

Rule [N] — [Short label] (added [date]) Rule: [The rule stated in one sentence — what to do or not do] Why: [What the original got wrong — what pattern triggered the edit] Pattern to avoid: [Specific construction, phrase type, or framing to watch for] Example: Original: "[verbatim or close paraphrase of what was submitted]" → Published: "[verbatim or close paraphrase of what AJ published]"