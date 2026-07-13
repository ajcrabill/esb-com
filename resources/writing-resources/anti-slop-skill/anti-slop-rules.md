Anti-Slop Reference — Mechanical Detection

A field guide to AI-generated writing patterns. Use this to catch and kill slop in any manuscript. "Slop" = text that reads like unedited LLM output: low information density, predictable structure, vocabulary no human would reach for.

These patterns work as regex-based detection — zero token cost, runs before any LLM evaluation. Every draft pass should be scanned and cleaned.

Tier 1: Kill on Sight

These almost never appear in casual human writing. If you see one, rewrite the sentence.

Tier 2: Suspicious in Clusters

Fine in isolation. Three in one paragraph = rewrite the paragraph.

Tier 3: Filler Phrases (Zero Information)

These are verbal tics. LLMs insert them reflexively. Delete them on sight.

Fiction AI Tells

Regex-detectable patterns that betray machine origin in fiction prose.

Structural AI Tics

Rhetorical formulas that betray AI composition. These are patterns, not single words.

Telling Patterns (Show-Don't-Tell)

Named emotions instead of demonstrated ones.

Mechanical Slop Score

Compute these metrics per chapter. Combine into a slop_penalty (0-100).

Slop penalty thresholds:

0-15: Clean. Minimal cleanup needed.

16-30: Moderate. Run a targeted cleanup pass on identified categories.

31-50: Heavy. Require a full rewrite of the flagged sections before LLM evaluation.

51+: Critical. The chapter reads as raw AI output. Regenerate with stricter voice guidance and anti-slop constraints in the drafting prompt.