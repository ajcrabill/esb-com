ANTI-SLOP REFERENCE

A field guide to AI-generated writing patterns. Used by the mechanical slop scorer (zero LLM cost) and by every drafting pass to self-check.

"Slop" = text that reads like unedited LLM output. Low information density, predictable structure, vocabulary no human would reach for.

TIER 1: Kill on sight

These almost never appear in casual human writing. If one appears, rewrite the sentence.

TIER 2: Suspicious in clusters

Fine in isolation. Three in one paragraph = rewrite.

robust, comprehensive, seamless/seamlessly, cutting-edge, innovative, streamline, empower, foster, enhance, elevate, optimize, scalable, pivotal, intricate, profound, resonate, underscore, harness, navigate (metaphorical), cultivate, bolster, galvanize, cornerstone, game-changer

TIER 3: Filler phrases

Zero information. Delete them.

"It's worth noting that..." / "It's important to note that..." / "Importantly,..." / "Notably,..." / "Interestingly,..." / "Let's dive into..." / "Let's explore..." / "In this section, we will..." / "As we can see..." / "As mentioned earlier..." / "In conclusion,..." / "To summarize,..." / "Furthermore,..." / "Moreover,..." / "Additionally,..." / "In today's [fast-paced/digital/modern] world..." / "At the end of the day..." / "It goes without saying..." / "Without further ado..." / "When it comes to..." / "One might argue that..."

FICTION-SPECIFIC AI TELLS

Prose cliches that betray machine origin:

"a sense of [emotion/sensation]"

"couldn't help but feel"

"the weight of [something]"

"the air was thick with"

"eyes widened"

"a wave of [emotion] washed over"

"a pang of [emotion]"

"heart pounded in [his/her/their] chest"

"[raven/dark/golden/silver] [hair/tresses] [spilled/cascaded/tumbled/fell]"

"piercing [blue/green/gray] eyes"

"a knowing [smile/grin/look]"

"[he/she/they] felt a [surge/rush/wave/pang] of"

"the silence [was/hung/stretched/grew] [heavy/thick/oppressive]"

"let out a breath [he/she/they] didn't [know/realize] they were holding"

"something [dark/ancient/primal] stirred"

"could feel [event/sensation]" — e.g. "She could feel the room tightening", "Amaya could feel everyone waiting". The modal hedge distances the reader from direct experience. Fix: replace with a direct observation verb (saw, knew, sensed, watched, registered) or convert to active sensory language: "She watched the room tighten", "Amaya sensed everyone waiting".

"felt something [verb] in [body part]" — e.g. "felt something twist/tighten/loosen/shift in her chest". The verb varies but the structure is always the same: naming a bodily sensation without showing it through action. Fix: show a physical action — hand going still, ribs contracting, shoulders dropping.

"[word/question/statement] landed like [metaphor]" — the "X landed like Y" cliche factory. Even when Y is a fresh image, the structure itself is a tell. Three+ instances in a manuscript means the author is reaching for this too often. Fix: replace with "hung in the air", "sat between them", "settled", or a stronger action verb that doesn't need a simile.

"the silence that followed was the kind that [story about it]" — over-explaining silence with a nested clause. "The silence that followed was the kind that made you aware of your own heartbeat." Fix: strip back. "The silence that followed was a held breath." Or just "Silence." Let the reader supply the feeling.

STRUCTURAL AI TICS

Rhetorical formulas that betray AI composition:

"I'm not saying X. I'm saying Y." (the "not X but Y" formula)

"which means either X, or Y"

"There's a difference between X and Y."

"Those are different things."

"Not just X, but Y"

"Not from X, but from Y" (in narration)

SHOW-DON'T-TELL DETECTORS

Patterns where the narrator names an emotion instead of showing it:

"[he/she/they/I] felt/was/seemed/looked/appeared [angry/sad/happy/scared/nervous/excited/jealous/guilty/anxious]"

Adverbs that tell instead of show: angrily, sadly, nervously, excitedly, desperately, furiously, anxiously, guiltily, bitterly, wearily, miserably

SCORING RUBRIC (Mechanical, zero LLM)

Each detected hit contributes to slop_penalty (0-10 scale):

Action threshold: slop_penalty > 3.0 = trigger voice re-alignment pass before revision. Target: slop_penalty < 1.5 before final polish.