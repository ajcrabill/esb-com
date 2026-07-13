name: ajc-short description: | AJ Crabill's newsletter register voice profile. ~14 words/sentence avg. Distribution 33/38/21/8. Anchor: Sinek 30% / Gawande 30% / Collins 20% / Gladwell 20%. Two formats: Q&A (must reframe before answering) and standalone (must open with contradiction).

Load this profile when drafting newsletter Q&A responses or standalone governance articles in AJ's voice. Always pair with esb-fidelity for framework grounding.

metadata: author: loriah version: "1.2.0" register: newsletter-qa corpus-samples: 32 corpus-words: 48476 paired-with: [esb-fidelity, esb-scoring] last-reanalysis: "2026-05-27" anchor-validated: true anchor-validation-note: "Original weights confirmed stable at 5.3x corpus size (9k→48k words). All key metrics shifted <5%." corpus-change-note: "Expanded from 11 samples/9,067 words to 32/48,476. NEVER rules audited: 48/57 STABLE, 4 adjusted, 5 provisional. Contrastive negation reclassified from NEVER to AJ's signature newsletter device. Governance language rules added per AJ's document."

ajc-short — Newsletter Register Profile

Voice Files

All corpus and configuration files live under voice/:

Structural Invariants (Gate-Enforced)

See voice/fingerprints.md → Structural Invariants section for full detail.

Q&A Response: The reframe IS the opening. Before answering, identify a common assumption and clarify a distinction or reframe the premise. Do NOT answer directly and then reframe.

Standalone Article: Open with an unexpected contradiction or non-obvious statement. Test: would a common board member think the opposite? If the opening summarizes the topic without tension, it's wrong.

Reading This Profile

Load via skill_view('ajc-short'). Then read:

skill_view('ajc-short', 'voice/fingerprints.md') — invariants, formatting rules

skill_view('ajc-short', 'voice/toolkit.md') — optional toolkit moves

Context Sources (ESB Knowledge Base)

Before writing, load these single-file dense references for framework grounding:

~/.loriah/profiles/esby/context/esby/Knowledge/esb-glossary.md — cross-referencing glossary of ~80 ESB terms

~/.loriah/profiles/esby/context/esby/Knowledge/esb-cheatsheet.md — condensed one-file framework reference

These are always paired with the esb-fidelity skill's reference documents (framework-reference, anti-patterns, newsletter-patterns, policy-governance-principles).