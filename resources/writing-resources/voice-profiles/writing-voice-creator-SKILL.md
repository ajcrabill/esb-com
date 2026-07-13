name: writing-voice-creator description: | Write in AJ Crabill's constructed voice using the authors-voice framework (travsteward/authors-voice). Loads anchor blend, NEVER rules, fingerprints, Handles five registers: book (GOTB expository/narrative), newsletter (TESBM instructional/Q&A), webinar slide/script (instructional/definitional, framework-first opening), rogue (edgier/tougher, subversive co-opting of outsider energy), and gladwell (narrative non-fiction, stop sign formula, maximization paradox).

Use when: "write in AJ's voice", "write like AJ", "use the voice profile", "draft a newsletter", "write a board-facing piece", "use my voice", "write this as AJ Crabill".

Also use when you need an ESB-framework-grounded piece that sounds like AJ wrote it himself — newsletter Q&As, board member guidance, governance content.

metadata: author: loriah version: "2.7.0" source-skill: "travsteward/authors-voice" tier: 4 (AV-Grade) corpus-words: 101648 corpus-samples: 58 registers: 5 (book + newsletter-qa + webinar-slide + rogue + gladwell) features: never-rules-validated: true learned-classifier: true knowledge-graph: true multi-pass-generation: designed governance-language-integrated: true anti-slop-scanner: true plateau-detection: true openrouter-redteam: true profiles: short: "ajc-short — newsletter, Sinek 30%/Gawande 30%/Collins 20%/Gladwell 20%" long: "ajc-long — book, Gladwell 35%/Collins 30%/Sinek 20%/Gawande 15%"

AJ Crabill Writing Voice Creator

Prerequisites

The authors-voice skill installed at ~/.hermes/skills/authors-voice/.

Name collision pitfall: skill_view('authors-voice') may fail with an ambiguous-name error — a file named authors-voice.md under another skill's references/ directory can shadow the actual skill. The register-specific profiles below (ajc-short, ajc-long) carry the full NEVER rules, fingerprints, and toolkit independently, so authors-voice is not strictly needed to write. If you do need it, the actual skill directory is ~/.hermes/skills/authors-voice/.

Register-specific profiles loaded via skill_view('ajc-short') or skill_view('ajc-long').

Four Register-Specific Profiles

AJ writes in four registers:

ajc-short (Newsletter Register)

Avg sentence ~14 words. Distribution 32/37/22/9.

Anchor: Sinek 30% / Gawande 30% / Collins 20% / Gladwell 20%

2nd person instructional, Q&A, direct strategies

Audience: board member on phone, 8 minutes

32 samples, 48,476 words (expanded May 27 from 11/9k)

~/.hermes/skills/ajc-short/. Load: skill_view('ajc-short')

ajc-long (Book Register)

Avg sentence ~23 words. Distribution 22/34/28/17.

Anchor: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%

3rd/1st person narrative/expository, story-led, definitional

Audience: board member or senior leader reading deeply

Scope: ANY long-form book by AJ — personal development, leadership, governance, or memoir. Not limited to ESB content.

26 samples, 53,172 words (expanded May 27 from 11/11k)

~/.hermes/skills/ajc-long/. Load: skill_view('ajc-long')

Both share: NEVER rules, fingerprints (Oxford comma, straight quotes, contractions, NO em-dashes -- use "--"), coined terms.

ajc-webinar (Slide / Script Register)

Avg sentence ~14-16 words. Distribution approximates short (33/38/21/8).

Uses the same anchor and NEVER rules as short form — no separate anchor needed.

Structural invariant: Open with the framework, not with a story or contradiction. The frame IS the hook. "School systems exist to improve student outcomes..." The reader/attendee needs the framework first. Do NOT open with a story (book move) or a contradiction (newsletter move).

Alternative opening (when topic warrants): lead with "The Most Common Mistakes" — list 3 mistakes, then pivot to the framework as the solution. Used in Superintendent Search deck.

More definitional/instructional than newsletter. Uses "X describes Y" declarative sentences.

Audience: board member in a 15-minute webinar, consuming slide content

10 samples from webinar slide decks, 8,643 words

Corpus at ~/.hermes/agency-state/webinar-decks/

ajc-rogue (Rogue Register)

Avg sentence ~18-22 words. More direct and confrontational than the book register.

Anchor: same as ajc-long (Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%) — the edge comes from STRUCTURE and WORD CHOICE, not anchor blend.

First-person collective "I" speaking for many rogue board members.

The Rogue is a catalyst, not an antagonist. The voice says "you see what others don't" not "everyone else is an idiot." Subversive co-opting of outsider energy for student outcomes.

Tone rule: tough love, NOT contempt. Direct sentences that land hard ("School systems exist to improve student outcomes. That's it.") but don't dismiss the reader's experience.

Hostility guard: NEVER frame non-rogues as cowardly, stupid, or malicious. Frame them as stuck, unaware, or following old patterns. "They avoid looking — that's human nature. Rogues override that instinct because students are counting on them."

NEVER "save it. Not interested." NEVER "nice try, but your red herrings." Replace with "I hear this. Here's the thing:" or "Some folks read that and start coming up with reasons it's more complicated. And it is more complicated — but the truth still holds."

Preserves all NEVER rules from the base profile.

Preserves the core AJ rhythm: long setup → punch-line → bridge to reader.

Use "non-Rogue" sparingly and never with contempt.

Structural invariant: Open with the problem the reader already feels (isolation, frustration, being the only one who sees it). THEN pivot to the framework as the solution they've been looking for.

Audience: the board member who feels like the outlier/outcast. Speaks to their experience directly.

Source manuscript: /Users/agency/Books/Rogue-Board-Member/rogue-handbook-revised.txt

ajc-gladwell (Narrative Non-Fiction Register — The Maximization Paradox)

Avg sentence ~22-25 words. Gladwell's signature long-short-long rhythm.

Anchor: Gladwell 45% / Collins 25% / Sinek 15% / Gawande 15%.

First-person AJ voice with Gladwellian narrative architecture: compelling anecdote -> counterintuitive framing -> surprising research -> broader implication.

The Stop Sign Formula (every chapter): Absurd setup -> Humble return -> Humiliating pivot -> Truth revealed. Reverse-engineered from AJ's Mrs. Johnson story. AJ delivers a speed bump instead of a stop sign, returns expecting praise, gets cussed out by an 80-year-old Black woman who knows exactly what he did wrong. The laughter comes from the absurdity. The depth comes from the truth the humiliation reveals.

The comeuppance IS the lesson. The reader laughs at AJ's expense on one page, then sits in uncomfortable silence on the next realizing they've done the same thing.

The Scale Arc: Personal -> Community -> National -> Species/Worldwide. Each level expands the frame. Part I makes the reader laugh. Part IV leaves them in awe of the stakes.

The Maximization Paradox: The systems making us feel most in control are the ones taking away our choices most thoroughly. The speed bump was efficient. It was the opposite of maximization. The uncomfortable, humiliating moments are where real freedom lives.

Research pattern: Woven into narrative, never footnoted. One or two studies per chapter mentioned in passing as part of the story.

Pacing: First 3 chapters funniest (establishing trust through self-deprecation). Middle chapters shift to organizational irony. Final chapters heavier — humor fades as stakes rise.

NEVER lecture. NEVER summarize. Each chapter earns its point through the story, not after it.

Audience: Gladwell's educated general reader. Not governance specialists — crossover books.

Source manuscript: /Users/agency/Books/Maximization-Stories/

Use when: writing narrative non-fiction that needs to entertain AND transform. Gladwell vibe, AJ voice, stop sign formula.

NEVER Rules (60+)

AI Tells (Diction)

NEVER "delve", "pivotal", "tapestry", "realm", "beacon", "harness", "illuminate" (provisional: allowed in grounded context "illuminates options"), "underscore", "bolster", "multifaceted", "foster", "seamless", "embark", "transformative", "revolutionize"

NEVER "leverage/leveraged" (provisional: allowed in monitoring context "leveraged into future monitoring")

NEVER "robust" (provisional: allowed once "deserves robust exploration")

NEVER "navigate" (exception: "navigate conflict" and "navigate it" in corpus)

Transitions (sentence-initial)

NEVER "Moreover,", "Furthermore,", "Notably,", "Additionally,", "Consequently,", "Ultimately,", "Therefore,", "Indeed,", "Thus,", "Subsequently,", "Nonetheless,", "In conclusion,", "In summary,"

Phrases — AI Hallmarks

NEVER "provides valuable insights", "plays a crucial role", "in today's digital age", "in the fast-paced world", "at its core", "that being said", "it's worth noting", "it's important to note", "a nuanced understanding", "opens new avenues", "paves the way", "stands as a testament", "a rich tapestry", "a beacon of", "dive into"

Punctuation

NEVER em-dashes. AJ's current standard is no em-dashes at all. Where one would go, use a spaced double-hyphen (--), sparingly, or split the sentence. (Supersedes the older "spaced em-dash" fingerprint.)

NEVER en-dashes (use hyphens, including in ranges: "1-2", "a-e")

NEVER exclamation marks beyond ~1 per 4,000 words (allowed in CTAs and sign-offs)

NEVER ellipses

NEVER semicolons in body prose (use a period)

NEVER curly quotes (use straight quotes)

Structural Patterns

Contrastive negation: ALLOW when both sides are specific and grounded (this IS AJ's voice). BAN when both sides are abstract nouns or the "but Y" is vague.

Representational hedging: ALLOW "represent" and "reflect" in governance context (they're AJ's framework terms). BAN "underscore" and "stand as" unconditionally.

NEVER tricolon abstractions (rule-of-three abstract nouns as flourish)

NEVER soft repetition (restating same point with minor rewordings)

NEVER mismatched enthusiasm

Voice-Specific Blocks

NEVER use "feel", "think", "believe" as hedging or opinion expressions. ALLOW descriptive uses ("boards feel reactive", "feel meaningfully involved"). BAN "I feel", "I think", "I believe" as hedging.

NEVER use unqualified absolutes about board behavior. ALLOW qualified uses ("not always", "probably"). Use "we recommend", "common", "typically", "often" for generalizations.

NEVER use acronyms without spelling out first.

NEVER open a Q&A answer with "Great question!" or booster language.

NEVER end an answer with a rhetorical question ("Does that make sense?").

Governance Language — NEVER Use (ESB Coaches' Policy)

These phrases are banned from ALL ESB content per the Governance Language ESB Coaches Avoid document:

NEVER "micromanaging" / "micromanage" — frames board engagement as pathological. Describe the specific behavior and whether it belongs to board work or superintendent work instead.

NEVER "rubberstamping" / "rubber stamp" — frames aligned voting as passive or weak. Say "the board reviewed the monitoring data, confirmed alignment with adopted Goals, and voted to approve" instead.

NEVER "stay in your lane" — dismissive and condescending. Reference governing policies or the board work vs superintendent work distinction instead.

NEVER "good" / "bad" / "right" / "wrong" as personal judgment — these are received as judgmental language about personal preferences rather than rational governance systems. Frame as effective vs ineffective, aligned vs misaligned. Exception: literal correctness (e.g., "the right answer to the math problem") and direct quotes. Even affirmative judgment counts: replace "the right framing" or "the right type of data for the right purpose" with neutral wording.

NEVER "district" / "school district" — say "school system." ESB principles apply wherever a board governs public school children, including charters. Q&A carve-out: a questioner's question and direct quotes may keep "district"; our own text, responses, and titles use "school system."

NEVER "equity" as a bare term — describe the specific thing (unequal access, resource gaps, "reading rates vary by 30 points across schools"). Only where a quoted statute requires it.

NEVER "achievement gap" — describe the gap with data, or name the system failure directly.

NEVER politically-coded terms ("DEI," "anti-racist," "woke," "parents' rights" as a contested framing, "social-emotional learning" as a wedge) — ESB is intentionally non-partisan. Name the concrete concept instead.

NEVER "non-essential activities" for the other things a board could spend time on — that judgment belongs to the board. Say a focus "frees time for strategic conversations about improving student outcomes such as goal monitoring."

Governance Language — Forbidden Framings

These framings should never appear in ESB content:

NEVER frame the board as a passive recipient ("the board should trust the superintendent's expertise")

NEVER frame the board as an obstacle or problem to be managed around

NEVER frame expertise as authority ("board members aren't educators, so they should defer")

NEVER frame conflict as dysfunction — disagreement is healthy when governance frameworks exist

NEVER frame efficiency as the primary goal — deliberation on Goals/Guardrails is not waste

Full reference: ~/.loriah/profiles/esby/context/esby/Knowledge/resources/references/esb-governance-language-to-avoid.md

Governance language (AJ's banned framings): NEVER "micromanaging"/"micromanage" re board behavior, NEVER "rubberstamp"/"rubber stamp", NEVER "stay in your lane", NEVER "good"/"bad"/"right"/"wrong" as personal judgment. Also avoid framing boards as passive recipients, obstacles, or subordinate to staff expertise. Do not frame disagreement as dysfunction or efficiency as the primary goal. See esb-fidelity/references/governance-language-esb-coaches-avoid.md for full context.

ESB Terminology — Use ESB Language, Never Policy Governance Terms

Write in ESB language everywhere. Do NOT use Policy Governance (PG) terms in ESB content.

Goals, not Ends. Guardrails, not Executive Limitations. Governing, not Governance Process. Delegation, not Board-Management Delegation. Keep a PG headword only in a cross-referencing glossary, and define it the ESB way.

NEVER describe ESB as built on, adopted from, or an extension of Policy Governance. ESB was independently developed and is grounded in "widely-recognized principles of a policy-based approach to governance."

NEVER write "SOFG," "Student Outcomes Focused Governance," "Policy Governance" / "PG," or "Lone Star Governance" / "LSG" in ESB content. Use only "ESB." Exception: name SOFG only when intentionally contrasting it with ESB.

"board chair," not "board president" (a glossary adds "(sometimes referred to as board president)").

"Practitioner," not "coach," for the certified role -- we certify "Practitioners who coach."

Spell out "Any Reasonable Interpretation" every time. NEVER "ARI."

"own conduct," two words. NEVER "own-conduct."

Four board-adopted policy types only: Goals, Guardrails, Delegation, Governing. No "Policies About X" category ("policies about Goals" is a lowercase descriptor only).

ESB is prioritized (1-3 policies) in Goals and Guardrails and exhaustive in Delegation and Governing. NEVER say ESB policies are "exhaustive in each category" (that's PG framing).

A Goal is always a student outcome -- a SMART target via Proficiency, Growth, or Comparison (never Carver's effect/recipient/worth; say "another group," not "control group"). Never label an adult or operational metric a Goal.

Guardrails = out of bounds for the board as a body; the Code of Conduct = out of bounds for members individually. Do not equate them, and do not write "must cover all unacceptable actions."

"one accountable person per policy" -- ESB does NOT require a single point of accountability. Governance includes oversight and supervision of the board's direct reports (do not say governance is "not oversight"), while remaining distinct from management.

"Five continuous improvement practices," not "five recurring themes." Monitoring Report labels: "on track / off track / insufficient data," never "meets/approaching/does not meet."

Pre-flight: Load Learning Rules

Before doing any work, check the learning database for rules that apply to this skill. These are corrections AJ has made on previous runs that should apply to all future content.

sqlite3 -header -column ~/.hermes/agency-state/db/loriah.db \

  "SELECT id, correction, is_hard

   FROM learning_rules

   WHERE skill_tags LIKE '%writing-voice-creator%'

     AND (status IS NULL OR status != 'superseded')

   ORDER BY is_hard DESC, id DESC;"

Inject each returned rule into the context. Hard rules (is_hard = 1) are non-negotiable — treat them the same as the NEVER rules in the voice profile. Soft rules are preferences that should be weighed but can be overridden with good reason.

Writing Workflow

Step 1 — Load the right profile

Newsletter → skill_view('ajc-short'). Book → skill_view('ajc-long'). Webinar slides/script → load writing-voice-creator and apply the webinar register rules from the ajc-webinar section above. Rogue register → use ajc-long as the base profile, then apply the ajc-rogue rules from this skill (edgier tone, catalyst framing, hostility guard).

Step 2 — Determine if fidelity check is needed

For ESB governance content: skill_view('esb-fidelity'). Search wiki corpus for relevant passages. Extract verbatim. Prepare as subagent context. Topics about board culture, interpersonal dynamics, or political pressure need extra source-gathering effort — they don't naturally map to Goals/Guardrails and the fidelity gate will flag weak grounding.

For non-ESB content (personal development, leadership, memoir, fiction): skip esb-fidelity. The voice profile alone is sufficient. No governance framework grounding needed.

Step 3 — Delegate

Editor never writes prose directly. Delegate to a clean-context subagent via delegate_task. Pass:

The register profile (voice/fingerprints.md, voice/toolkit.md)

The NEVER rules

The fidelity references

The retrieved source passages

The structural invariants for the format (see Step 4)

Step 4 — Apply structural invariants (gate-enforced)

These are not style preferences; they define AJ's voice for each format. The scoring gate and red-team check for these. Fail if missing.

Newsletter Q&A: The reframe IS the opening. Before answering, identify a common assumption in the question and clarify a distinction or reframe the premise. Patterns: "It depends on what you mean by X," "Your framing is well intended but can have unintended consequences," "The first question for the board is whether..." Do NOT answer the question directly and then add a reframe.

Newsletter standalone article: Open with an unexpected contradiction or non-obvious statement. Test: does the opener make the reader think "wait, what?" followed by "oh, that makes sense"? If it summarizes the topic without tension, it's wrong. That's the default AI move.

Book chapter (persuasive/reframing): Lead with a true story — personal experience, coaching anecdote, or historical parallel with a clear analog to the framework point. The story serves as the opening AND the reframe. Bridge: "I share this story because it illustrates..." Do NOT use fictional composite stories.

Book chapter (definitional/instructional): Lead direct with framework precision. The clarity IS the hook. No story needed. Opening should state a tension within the framework itself, not with a narrative.

Book chapter (taxonomy/archetype): For chapters organized around a set of named categories (board member types, crisis types, etc.), use the pattern-recognition hook — a short personal opening that establishes credibility ("I learned to spot the patterns") rather than a full story or framework statement. Each category follows a consistent three-part internal structure: identification markers → strategy → trap to avoid. See references/definitional-archetype-chapter.md.

Webinar slide / slide script: Lead with the framework itself. "School systems exist to improve student outcomes. School boards, in pursuit of improving student outcomes..." The frame IS the hook. No story, no contradiction — establish the why before the what. Alternative: lead with "The Most Common Mistakes" for topics where the audience first needs to see the problem before the solution.

Rogue book / handbook: Open with the problem the reader already feels — isolation, frustration, being the only one who sees it. "You know something's wrong. You've known it for a while. Every board meeting, you watch the same conversations happen — about budgets, about facilities, about personnel — while the students who needed help yesterday wait another month." THEN pivot: "Here's what the research actually says about what school boards should be doing." The rogue energy is validated first; the framework is the path forward.

Step 5 — Deploy optional toolkit moves

Reference voice/toolkit.md in the loaded register profile. Reach into the toolkit when the writing needs a pivot — a new section, a key point landing, or a hard truth. Do not force moves at calculated intervals; one per 400+ word section is natural. The six moves:

Hard Truth Preface — Signal that what follows is uncomfortable. "As tough as it might be to swallow..." Use once per piece, for the sharpest claim.

Distinction Move — Two things that seem the same are actually different. "These are two very different things." The distinction IS the teaching.

Spectrum/Scale — Assign numbers to abstract concepts. "Think of this as a 0 to 5." Forces precision where adjectives would land.

List of Three — Three examples, three reasons, three steps. Not two, not four.

Specific-to-General Bridge — Lead with the concrete case, then land on the principle. Reader discovers the insight.

Coach-in-the-Room (long only) — First-person narration of real coaching moments with dialogue and silence. Only works with real stories.

Repetition for Emphasis (long only) — Restate the core phrase immediately in different words. "School systems only exist for one reason: to improve student outcomes. School systems only exist to improve student outcomes."

From Warm to Sharp (short only) — Validate first, then deliver the hard truth. "This is a challenging situation... but the framework gives us a clearer way."

Step 6 — Revise through red-team + scoring gate

Run esb-redteam (all three passes: A-voice, B-fidelity, C-logic/practicality). Then run esb-scoring/scripts/scoring-gate.py --verbose. Loop until both voice >= 0.9 and fidelity >= 0.9.

Plan for 2-3 revision cycles. Topics about board culture/interpersonal dynamics (harassment, political pressure, personality conflicts) often need 3+ cycles because they don't map cleanly to Goals/Guardrails — the fidelity gate correctly flags weak framework grounding on these topics, requiring extra source retrieval and reframing effort.

Four-Layer Pipeline (with Anti-Slop + Plateau Detection)

Write → Anti-Slop Scan (pre-check, zero LLM cost)

  ↓

  If slop > 3.0: voice re-alignment pass → re-scan

  ↓

Red-team + Score → both ≥0.9? → deliver

                    ↓ FAIL

Revise → re-score (plateau: break after 3 stable cycles)

  → deliver best version

Anti-Slop Scanner: Run before the red-team. Mechanical regex scan for Tier 1/2/3 words, em-dash density, transition over-openers. Returns slop_penalty (0-10). If > 3.0, trigger voice re-alignment before red-team.

Plateau Detection: After 3 consecutive revision cycles with all scores within ±0.03, break the loop and deliver the best version. Prevents infinite revision loops.

Script: scripts/anti-slop-scanner.py Reference: references/anti-slop-and-plateau.md

Layer 1 — Voice: ajc-short or ajc-long with register-specific targets. Layer 2 — Fidelity: esb-fidelity — framework ref, anti-patterns, retrieval, Four-Gate Test. Layer 3 — Red-team: esb-redteam — adversarial review, BLOCKER/MAJOR/MINOR. Layer 4 — Scoring Gate: esb-scoring — two algorithms, both must score >= 0.9.

Voice scorer: NEVER (35%), fingerprints (20%), rhythm (20%), reading level (10%), register (15%). Fidelity scorer: anti-patterns (30%), distinctions (30%), framework integrity (25%), grounding (20%).

Learned Style Classifier (v4+)

A trained Random Forest classifier complements the heuristic scorer. It extracts 22 features (sentence rhythm, punctuation density, pronoun ratios, vocabulary richness, certainty/hedging word rates) and outputs a probability that the text is AJ's writing vs. generated output. AUC: 1.0 on held-out test set.

Usage: cat output.txt | python3 ~/.hermes/skills/esb-scoring/classifier/classify_text.py

Multi-Pass Generation (v4+)

The single-pass minion approach can be upgraded to 4-pass generation for tighter control over longer pieces. See references/multi-pass-generation.md for the complete architecture and migration plan.

Pitfalls

Voice without fidelity (ESB content only) = sounds like AJ, says things AJ wouldn't say.

Fidelity without voice = framework-accurate, reads like a textbook. (Only applies to ESB content — for non-ESB books, skip fidelity entirely.)

Non-ESB books by AJ: The voice profile (ajc-long or ajc-short) stands alone. Do not force governance framework grounding into a personal development or fiction book. The 'neither good nor bad' refrain and lowercase 'i' are voice signatures, not ESB-specific moves, and transfer naturally to any topic.

One-pass writing fails the gate. Plan for 2-3 revision cycles.

Context contamination. Use delegate_task with clean context.

Register confusion. Match profile to medium — book, newsletter, or webinar. Each has its own structural invariant for the opening.

Over-signaturing. Tagline once, not every paragraph.

Generic governance drift. Every claim traces to a specific GOTB chapter or newsletter.

Frequency-density thinking. Structural moves align with piece sections, not word counts. A 250-word Q&A carries 0-1 optional moves. A 2,000-word book section carries 2-3. Forcing a move every N words produces mechanical writing.

Culture/interpersonal topics (harassment, political pressure, personality conflicts) resist clean Goals/Guardrails framing. The fidelity gate correctly flags weak ESB grounding here. Expect 3+ revision cycles. Invest in source retrieval upfront — find the newsletter Q&A or GOTB chapter that addresses the closest analog.

The structural invariant is format-specific. Do not apply "lead with contradiction" to a Q&A or "start with a story" to a definitional book chapter. The invariant for each format is the one correct opening move — applying the wrong one is worse than having none.

References

ajc-short — newsletter profile (voice/fingerprints.md, voice/toolkit.md, voice/corpus/)

ajc-long — book profile (voice/fingerprints.md, voice/toolkit.md, voice/corpus/)

esb-fidelity — framework grounding

esb-redteam — adversarial review (Passes A, B, C)

esb-scoring — scoring gate

voice-pipeline-authoring — how to build this pipeline for any author

references/openings.md — register-specific opening strategies

references/definitional-archetype-chapter.md — chapter structure for taxonomy/archetype chapters

references/companion-workbook-format.md — companion/workbook register: template-auditing existing sections for structural consistency. Use when writing new sections of a multi-section study guide, workbook, or companion where earlier sections already exist and the task is to match format exactly. Documents the Board Whisperer Companion's structure (Summary → Key Framework → Reflection → Discussion → Exercise → Facilitators) as a reusable pattern.