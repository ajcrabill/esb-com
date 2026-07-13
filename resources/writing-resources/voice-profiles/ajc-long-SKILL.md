name: ajc-long description: | AJ Crabill's book register voice profile. ~23 words/sentence avg. Distribution 21/37/28/14. Anchor: Gladwell 35% / Collins 30% / Sinek 20% / Gawande 15%. Two chapter types: persuasive/reframing (must lead with true story) and definitional/instructional (must lead direct with framework precision).

Load this profile when drafting GOTB chapters or long-form governance content in AJ's voice. Always pair with esb-fidelity for framework grounding.

metadata: author: loriah version: "1.2.0" register: book corpus-samples: 26 corpus-words: 53172 paired-with: [esb-fidelity, esb-scoring] last-reanalysis: "2026-05-27" anchor-validated: true anchor-validation-note: "Original weights confirmed stable at 4.8x corpus size (11k→53k words). Two sampling-bias corrections: colon rate (10.0→7.2/1k), parentheses (1.3→4.8/1k)." corpus-change-note: "Expanded from 11 samples/11,163 words to 26/53,172. NEVER rules audited: 34/49 STABLE, 5 adjusted, 10 provisional. Contrastive negation confirmed STABLE in book register (zero hits — different from newsletter). Governance language rules added."

ajc-long — Book Register Profile

Voice Files

All corpus and configuration files live under voice/:

Structural Invariants (Gate-Enforced)

See voice/fingerprints.md → Structural Invariants section for full detail.

Persuasive/Reframing Chapters: Lead with a true story — personal, coaching anecdote, or historical parallel with clear analog to the framework point. Bridge: "I share this story because it illustrates..." Do NOT use fictional composites.

Definitional/Instructional Chapters: Lead direct with framework precision. The clarity IS the hook. No story needed. Opening states a tension within the framework itself.

Reading This Profile

Load via skill_view('ajc-long'). Then read:

skill_view('ajc-long', 'voice/fingerprints.md') — invariants, formatting rules

skill_view('ajc-long', 'voice/toolkit.md') — optional toolkit moves

Context Sources (ESB Knowledge Base)

Before writing, load these single-file dense references for framework grounding:

~/.loriah/profiles/esby/context/esby/Knowledge/esb-glossary.md — cross-referencing glossary of ~80 ESB terms

~/.loriah/profiles/esby/context/esby/Knowledge/esb-cheatsheet.md — condensed one-file framework reference

These are always paired with the esb-fidelity skill's reference documents (framework-reference, anti-patterns, newsletter-patterns, policy-governance-principles).