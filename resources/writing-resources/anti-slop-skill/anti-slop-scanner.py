#!/usr/bin/env python3
"""
Anti-Slop Scanner — AJ-Calibrated (v1.1)

Mechanical, zero-LLM-cost scanner adapted from book-autogenesis/anti-slop.md.
Calibrated for AJ Crabill's newsletter voice (ajc-short register).

DIFFERENCES from generic anti-slop:
- "not X but Y" is NOT penalized — it's AJ's signature newsletter device
  (verified: ~60 hits across 24 of 32 corpus files)
- "leverage" and "robust" are PROVISIONAL (AJ uses them at low frequency)
- "illuminate" is PROVISIONAL (AJ uses it in grounded context)
- Em-dashes and en-dashes are FLAGGED as violations (AJ's current standard is no em-dashes; use "--")

Usage:
  cat draft.txt | python3 anti-slop-scanner.py
  python3 anti-slop-scanner.py --file draft.txt --verbose

Returns:
  JSON: {"slop_penalty": 0.0, "passes": true, "details": {...}}
"""

import re
import json
import sys

# ── TIER 1: Kill on sight ──────────────────────────────────────────
# Words AJ never uses (verified: zero hits in 48k-word newsletter corpus)
TIER_1 = {
    "delve", "utilize", "facilitate", "elucidate", "endeavor",
    "encompass", "tapestry", "testament", "paradigm", "synergy",
    "holistic", "catalyze", "juxtapose", "myriad", "plethora",
    "synergize", "catalyst",
    # AI tell words AJ avoids (verified STABLE in NEVER rules audit — ajc-long)
    "pivotal", "underscore", "bolster", "multifaceted", "foster",
    "seamless", "embark", "transformative", "revolutionize",
    # NEVER rule words missing from original Tier 1 (added May 2026)
    "realm", "beacon", "harness",
}

# ── TIER 2: Suspicious in clusters ─────────────────────────────────
# Fine in isolation. 3+ in same paragraph = flagged.
# AJ-USAGE NOTES:
# - "leverage" — PROVISIONAL. AJ uses it in monitoring context (12 hits/48k).
#   Not penalized here; caught by NEVER rules if overused.
# - "robust" — PROVISIONAL. AJ used once. Not penalized here.
# - "illuminate" — PROVISIONAL. AJ uses in "illuminates options" context.
#   Not penalized here.
# - "navigate" — EXCEPTION already in NEVER rules (allowed in conflict context).
#   Not penalized here.
TIER_2 = {
    "comprehensive", "cutting-edge", "streamline", "empower",
    "enhance", "elevate", "optimize", "scalable", "intricate",
    "profound", "resonate", "cultivate", "galvanize", "cornerstone",
    "game-changer",
}

# ── TIER 3: Filler phrases ─────────────────────────────────────────
# Zero information. Delete them.
TIER_3 = [
    "it's worth noting that", "it's important to note that",
    "importantly,", "notably,", "interestingly,",
    "let's dive into", "let's explore",
    "in this section, we will", "as we can see",
    "as mentioned earlier", "in conclusion,", "to summarize,",
    "furthermore,", "moreover,", "additionally,",
    "in today's fast-paced", "in today's digital", "in today's modern",
    "at the end of the day", "it goes without saying",
    "without further ado", "when it comes to",
    "one might argue that", "in summary,",
]

# ── TRANSITION OVER-OPENER CHECK ───────────────────────────────────
# AJ uses sentence-initial conjunctions at ~1.6/1k words (newsletter).
# Over 3x that is suspicious.
TRANSITION_STARTS = [
    "Moreover,", "Furthermore,", "Additionally,", "Consequently,",
    "Ultimately,", "Therefore,", "Indeed,", "Thus,", "Subsequently,",
    "Nonetheless,", "Notably,", "In conclusion,", "In summary,",
    "Additionally,", "However,", "Nevertheless,", "Meanwhile,",
]


def calculate_slop(text):
    t = text.lower()
    words = text.split()
    word_count = len(words)
    para_count = max(1, text.count('\n\n') + 1)
    
    details = {
        "tier_1_hits": [],
        "tier_2_hits": [],
        "tier_3_hits": [],
        "structural_tics": 0,
        "em_dash_density": 0,
        "transition_over_openers": 0,
    }
    
    penalty = 0.0
    
    # ── Tier 1 words ──
    for word in TIER_1:
        hits = len(re.findall(r'\b' + re.escape(word) + r'\b', t))
        if hits:
            details["tier_1_hits"].append({"word": word, "count": hits})
            penalty += hits * 0.5
    
    # ── Tier 2 words (3+ in paragraph) ──
    paragraphs = text.split('\n\n')
    for para in paragraphs:
        t2_hits = 0
        t2_found = []
        for word in TIER_2:
            hits = len(re.findall(r'\b' + re.escape(word) + r'\b', para.lower()))
            if hits:
                t2_hits += hits
                t2_found.append(f"{word}({hits})")
        if t2_hits >= 3:
            details["tier_2_hits"].append({"paragraph_snippet": para[:80], "words": t2_found, "count": t2_hits})
            penalty += (t2_hits - 2) * 0.2  # first 2 are free
    
    # ── Tier 3 filler phrases ──
    for phrase in TIER_3:
        hits = t.count(phrase.lower())
        if hits:
            details["tier_3_hits"].append({"phrase": phrase, "count": hits})
            penalty += hits * 0.3
    
    # ── Structural tics ──
    # NOT penalized: "not X but Y" (AJ's signature newsletter device)
    # Penalized: generic structural formulas AJ doesn't use
    struct_patterns = [
        (r"\bthere's a difference between\b", 0.5),
        (r"\bthose are different things\b", 0.5),
        (r"\bwhich means either\b", 0.5),
        (r"\bnot from x, but from y\b", 0.3),
    ]
    for pattern, pval in struct_patterns:
        hits = len(re.findall(pattern, t))
        if hits:
            details["structural_tics"] += hits
            penalty += hits * pval
    
    # ── Em-dashes and en-dashes (BANNED: AJ's standard is no em-dashes; use "--") ──
    # "--" is the correct form and is NOT counted. Each unicode em/en-dash is a violation.
    em_dashes = text.count('—') + text.count('–')
    details["em_dash_density"] = em_dashes
    if em_dashes:
        penalty += em_dashes * 0.5  # Tier-1-level penalty per dash
    
    # ── Transition over-openers ──
    # Count sentence-initial banned transitions
    trans_count = 0
    for tr in TRANSITION_STARTS:
        # Count at start of sentence
        trans_count += len(re.findall(r'[.!?]\s+' + re.escape(tr), text))
        trans_count += len(re.findall(r'^' + re.escape(tr), text))
    
    expected = max(1, word_count / 1000 * 1.6)  # AJ's rate: ~1.6/1k
    if trans_count > expected * 2.5:
        details["transition_over_openers"] = trans_count
        penalty += (trans_count - expected * 2) * 0.1
    
    # ── Reading level penalty ──
    # Target: 8th grade or below, never above 10th. Long average sentences push grade level up.
    # Coarse proxy (avg sentence length); the real grade-level check runs in the drafting QA.
    sents = [s for s in re.split(r'(?<=[.!?])\s+', text) if len(s.split()) > 3]
    if sents and len(sents) >= 3:
        avg_words = sum(len(s.split()) for s in sents) / len(sents)
        if avg_words > 34:
            penalty += 0.6
        elif avg_words > 28:
            penalty += 0.3
    
    # ── Compose result ──
    result = {
        "slop_penalty": round(penalty, 2),
        "passes": penalty < 3.0,
        "action": "proceed" if penalty < 1.5 else ("review" if penalty < 3.0 else "voice_re_align"),
        "details": details,
        "stats": {
            "word_count": word_count,
        }
    }
    
    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="AJ-calibrated anti-slop scanner")
    parser.add_argument("--file", "-f", help="Read from file instead of stdin")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--json", "-j", action="store_true", help="Output raw JSON only")
    args = parser.parse_args()
    
    if args.file:
        with open(args.file) as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    
    if not text.strip():
        print(json.dumps({"slop_penalty": 0.0, "passes": True, "error": "empty input"}))
        sys.exit(0)
    
    result = calculate_slop(text)
    
    if args.json:
        print(json.dumps(result, indent=2))
    elif args.verbose:
        print(f"Slop penalty: {result['slop_penalty']}/10")
        print(f"Result: {'PASS' if result['passes'] else 'FAIL'} ({result['action']})")
        print()
        d = result['details']
        print(f"Tier 1 hits: {sum(h['count'] for h in d['tier_1_hits'])}")
        for h in d['tier_1_hits']:
            print(f"  - {h['word']}: {h['count']}x")
        print(f"Tier 2 cluster hits: {len(d['tier_2_hits'])} paragraphs")
        print(f"Tier 3 filler hits: {sum(h['count'] for h in d['tier_3_hits'])}")
        print(f"Structural tics: {d['structural_tics']}")
        print(f"Em/en-dashes (banned): {d['em_dash_density']}")
        print(f"Transition over-openers: {d['transition_over_openers']}")
    else:
        action = result['action']
        icon = "✅" if action == "proceed" else ("⚠️" if action == "review" else "🔴")
        print(f"{icon} Slop: {result['slop_penalty']}/10 — {action.upper()}")
    
    # Exit 0 if passes, 1 if fails
    sys.exit(0 if result['passes'] else 1)


if __name__ == "__main__":
    main()
