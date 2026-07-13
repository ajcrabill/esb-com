Batch Anti-Slop Scan & Fix Workflow (Post-Production)

Run this when scanning a range of completed chapters for slop patterns after drafting, not during per-chapter production. The per-chapter anti-slop pass (in the main pipeline) handles individual chapters as they're drafted. This workflow handles the bulk cleanup pass across multiple finished chapters at once.

When to use

Scanning a batch of already-drafted chapters (e.g., chapters 11-21 after completing the first draft)

A final anti-slop sweep before polish/export

Manual structural-tell cleanup after scripts/evaluate.py hit its limits

Walkthrough

Phase 1: Load reference + inventory

skill_view('book-autogenesis')

skill_view('book-autogenesis', 'references/anti-slop.md')

Read the anti-slop reference to internalize all three tiers, fiction tells, structural tics, and telling patterns. Also note the scoring rubric — it defines what counts and how penalties accumulate.

Phase 2: Read all target files

Batch-read every chapter in the range. Use read_file with offset/limit for large files. This gives you line numbers for every subsequent edit.

Phase 3: Regex sweep for every pattern class

Use search_files (with file_glob to restrict scope) and/or terminal + grep to run bulk searches. Sweep each pattern class independently — don't try to eyeball all patterns at once.

Pattern classes to search (run separately per class):

Tier 1 banned words: delve|utilize|leverage(?!.*but it's)|facilitate|elucidate|embark|endeavor|encompass|multifaceted|tapestry|testament|paradigm|synergy|holistic|catalyze|catalyst|juxtapose|nuanced|myriad|plethora|realm|landscape

Fiction tells — "landed like": landed like (a|the|an)

Fiction tells — "the silence that followed" variants: the silence that followed (then manually filter for "was the kind that" and "was the [adj] thing" constructions)

Fiction tells — "let out a breath [they] didn't realize": let out a breath.*didn.t

Fiction tells — "felt something [verb] in [body part]": felt something (shift|loosen|tighten|twist|stir) in

Fiction tells — "felt a [surge/rush/wave/pang] of": felt a (surge|rush|wave|pang) of

Fiction tells — "felt [body part]": felt (her|his|their) (throat|chest|stomach|jaw|shoulders|pulse|heart)

Fiction tells — "could feel" (modal hedge): could feel — then manually review each hit. Legitimate uses (close physical contact, actual tactile sensation like "could feel the cold") can stay. Generic abstract sensing ("could feel the room tightening", "could feel everyone waiting") must be replaced with direct observation verbs: saw, knew, sensed, watched, registered.

Structural tics — "not X but Y" in narration: not (because|the|a|about|just) .* but (because|the|a|about|just) Then manually review each hit to distinguish dialogue (keep as character voice) from narrative (fix).

Structural tics — "those are different things" / "not the same thing": are different things|not the same thing Same dialogue vs. narrative filter.

Tier 3 transition openers: Lines starting with Moreover, Furthermore, Additionally

Telling adverbs: said (angrily|sadly|nervously|excitedly|desperately|furiously|anxiously|guiltily|bitterly|wearily|miserably)

Density/repeat checks:

the weight of (fiction tell per reference; check each instance)

a sense of

couldn.t help but

eyes widened

a knowing (smile|grin|look)

heart (pounded|hammered|thumped|raced)

Phase 4: Catalog findings per chapter

For each match, record: chapter + line number, pattern class, the exact text (old_string), what to replace it with (new_string), and the scoring penalty from the rubric.

Phase 5: Fix in-place with targeted patches

Use patch for every fix. One patch call per edit. Replacement rules:

"landed like [X]" → "hung in the air", "sat between them", "settled", "hit her like [fresh image]", or a stronger action verb without simile.

"the silence that followed was the kind that..." → shorter form without "the kind that" framing, e.g. "The silence that followed pressed against the walls."

"felt something [verb] in [body part]" → visible physical action: shoulders dropping, hands stilling, ribs contracting, jaw setting, breath hitching. Show what a reader would see.

"felt a [surge/rush/wave] of [emotion]" → action that demonstrates the emotion: sharp nod, chair pushing back, fingers pressing into palms.

"let out a breath [they] didn't realize [they] were holding" → concrete physical release: "exhaled slowly", "shoulders dropped", "hands unclenched".

"not X but Y" (narrative) → direct statement skipping the negated alternative. Just "It was Y."

"the weight of [X]" → more specific construction: "[X]'s bulk", "[X] sat heavy", "everything [X] implied", or just cut the phrase.

Critical: preserve dialogue. If text is inside quotation marks, it stays — structural tics and constructions in character speech are character voice, not authorial tells.

Critical: don't over-correct. A single "landed" without "like" is fine. "The silence that followed" without "was the kind that" is fine. Target the specific formula, not the isolated word.

Phase 6: Verify with re-search

Re-run regex sweeps from Phase 3 to confirm zero remaining hits in the target scope.

Phase 7: Write evaluation log

Write a structured JSON log to ~/Books/[project-name]/eval-logs/antislop-part[N].json:

{

  "scan_target": "chapters X-Y",

  "date": "YYYY-MM-DD",

  "chapters_scanned": ["chapter-N.md", ...],

  "summary": {

    "total_issues_found": N,

    "total_issues_fixed": N,

    "tier1_banned_words": N,

    "fiction_tells_landed_like": N,

    "fiction_tells_silence_that_followed": N,

    "fiction_tells_let_out_breath": N,

    "fiction_tells_felt_something_chest": N,

    "fiction_tells_felt_surge_of": N,

    "fiction_tells_felt_throat_tighten": N,

    "fiction_tells_felt_weight_of": N,

    "structural_tics_not_x_but_y": N

  },

  "fixes": [

    { "chapter": "chapter-N.md", "type": "fiction_tell_landed_like", "old": "original text", "new": "replacement text", "reason": "why fixed" }

  ],

  "clean_chapters": { "chapter-X.md": "No slop patterns detected" }

}

Pitfalls

Don't overcorrect dialogue. Character speech gets a pass on structural tics and "not the same thing" constructions.

"The silence stretched" is not the same as "The silence that followed was the kind that…" — the latter is the formula.

"The weight of six years in a chair" (specific metaphor) is different from "the weight of the conversation" (generic tell).

Don't cat/grep/sed for edits. Use patch — it has fuzzy matching and syntax checks.

After patching a file, re-read the full chapter section before the next patch. Stale offset views cause match failures.

Patch escaping pitfall: When old_string or new_string contain double quotes (e.g. said "Go ahead"), the patch tool may error with "escape-drift detected". This happens when the quoted text passed to the tool looks different from how the file stores it (smart vs. straight quotes, or the tool API serializes a \ before "). Fix: re-read the exact line with read_file (specifying the offset) and copy-paste the exact text verbatim — do not retype it. The read_file output shows the true bytes.

Don't hit the same category twice with a "could feel" → "felt" replacement. "She could feel the room tightening" fixed to "She felt the room tightening" still has a tell — it needs to go to "She watched the room tighten" or equivalent. Skip the intermediate step and replace with a direct observation verb or active sensory language in one edit.