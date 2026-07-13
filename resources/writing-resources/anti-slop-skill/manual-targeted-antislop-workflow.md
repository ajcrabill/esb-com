Manual Targeted Anti-Slop Fix Workflow

The automated de-slop script (scripts/deslop.py) strips Tier 1 banned words only. It does NOT address fiction tells, telling patterns, or structural tics. This manual workflow fills that gap — it reads the scanner's own regex patterns, applies targeted prose-level fixes, and re-scans to confirm improvement.

Use when: the automated anti-slop scan flags slop_penalty > 3.0 and you need to bring it below threshold. Also use as a quality pass before Council review even if the score is acceptable (1.5-3.0).

The Workflow

Step 1: Read the Scanner

Open scripts/evaluate.py and read the pattern definitions at the top of the file (lines 56-88). These are the exact regex patterns the scanner uses. The manual fix pass is only as good as your understanding of what's being flagged.

Key pattern sections to inspect:

FICTION_AI_TELLS = [ ... ]     # lines 56-72

STRUCTURAL_AI_TICS = [ ... ]   # lines 74-82

TELLING_PATTERNS = [ ... ]     # lines 84-88

Step 2: Search Each Pattern Across All Chapters

Use execute_code or search_files to find every instance of each flagged pattern across the affected chapters. Do NOT rely on the automated scanner's aggregate counts — get line numbers.

import re

patterns = {

    # Copy from evaluate.py lines 56-88

    "a_sense_of": r"a sense of \w+",

    "weight_of": r"the weight of \w+",

    "felt_surge": r"(?:he|she|they) felt a (?:surge|rush|wave|pang|flicker) of",

    # ... all patterns

}

for ch_file in chapter_files:

    with open(ch_file) as f:

        text = f.read()

    for label, pat in patterns.items():

        for m in re.finditer(pat, text, re.IGNORECASE):

            line_num = text[:m.start()].count('\n') + 1

            print(f"[{label}] {ch_file}:L{line_num}: {m.group()[:80]}")

Step 3: Replace Each Pattern with Stronger Prose

For each hit, replace with prose that shows instead of tells. The specific replacement depends on context. General strategy:

Step 4: Use targeted patch() for each fix

from hermes_tools import patch

patch(path=ch_file, old_string=old_text, new_string=new_text)

Each replacement should be unique in the file. Include surrounding context lines (1-2 before/after) if needed for uniqueness. Run each patch() call individually — batch processing inside execute_code can produce unreliable results.

Step 5: Re-scan to Verify

python3 scripts/evaluate.py slop chapters/*.md

Target: slop_penalty < 1.5 (passes final). Acceptable: < 3.0 (below rewrite threshold).

If the score didn't drop enough, repeat from Step 1 — re-read the scanner output to see which patterns remain, then search and replace those.

Scoring Reference

Use this to estimate how many fixes are needed. E.g., 8 fiction tells × 0.4 + 3 structural tics × 0.5 = 4.7 points of penalty. Eliminating all of them would drop a 5.1 score to ~0.4.