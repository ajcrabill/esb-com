Anti-Slop Scanner + Plateau Detection — Integration Guide

Anti-Slop Scanner

Path: scripts/anti-slop-scanner.py Type: Mechanical, zero-LLM-cost regex scanner Calibrated for: AJ Crabill's newsletter voice (ajc-short register)

What it checks

Tier 1 banned words (kill on sight — AJ never uses these)

Tier 2 suspicious words in clusters (3+ per paragraph)

Tier 3 filler phrases (zero information)

Structural tics (excluding contrastive negation — AJ's signature device)

Em-dashes and en-dashes (BANNED -- AJ's standard is no em-dashes; use "--"). Each unicode dash is flagged as a violation.

Transition over-openers (AJ baseline ~1.6/1k words)

How to use

# Quick check

cat draft.txt | python3 scripts/anti-slop-scanner.py

# Verbose mode for revision

cat draft.txt | python3 scripts/anti-slop-scanner.py --verbose

# Raw JSON for programmatic use

cat draft.txt | python3 scripts/anti-slop-scanner.py --json

Action thresholds

Differences from generic anti-slop (book-autogenesis)

"not X but Y" is NOT penalized (AJ's signature newsletter device)

"leverage", "robust", "illuminate" excluded from Tier 2 (AJ uses at low frequency)

"navigate" excluded (AJ uses in "navigate conflict" context)

Em-dashes and en-dashes are flagged as violations (AJ's current standard is no em-dashes; use "--")

Plateau Detection

Built into the revision loop. When running red-team + scoring gate cycles:

After each cycle, record (voice_score, fidelity_score)

If 3 consecutive cycles show all scores within ±0.03 of each other, break

Surface the best version (highest combined score)

This prevents infinite loops on pieces that are close but won't get closer.

Integration into the 4-layer pipeline

Write → Anti-Slop Scan (pre-check)

  ↓

  If slop > 3.0: voice re-alignment pass → re-scan

  ↓

Score → PASS (both ≥0.9)? → deliver

         ↓ FAIL

Red-team (3 passes + reader panel) → revise

  ↓

Re-score → PASS? → deliver

  ↓ FAIL

  ↓ (check plateau: 3 cycles stable?)

  ↓

  If plateau → deliver best version + note

  ↓

  Else → repeat red-team + revise