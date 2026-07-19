---
layout: base
title: "GOTB Index: Self Assessment"
description: "A free 18-question self-assessment for school board members based on the Great On Their Behalf index. Get an indicative read of where your board stands across five practice areas."
toplevel: "gotb-free"
---

<style>
/* ── Reset & base ──────────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; padding: 0; }
.gotb-wrap { max-width: 760px; margin: 0 auto; padding: 0 20px 60px; font-family: Arial, sans-serif; color: #2c3e50; }

/* ── Hero ──────────────────────────────────────────────────────────────────── */
.gotb-hero { background: #fff; border-top: 5px solid #3a6ea8; border-radius: 0 0 10px 10px; padding: 32px 32px 28px; margin-bottom: 28px; text-align: center; box-shadow: 0 2px 14px rgba(0,0,0,.06); }
.gotb-hero h1 { margin: 0 0 10px; font-size: 26px; font-weight: 800; line-height: 1.2; color: #1e3758; }
.gotb-hero p { margin: 0; font-size: 15px; color: #555; line-height: 1.6; }

/* ── Section prose ─────────────────────────────────────────────────────────── */
.gotb-section { background: #fff; border: 1px solid #e0e0e0; border-radius: 10px; padding: 28px 32px; margin-bottom: 22px; }
.gotb-section h2 { margin: 0 0 14px; font-size: 18px; color: #2c3e50; }
.gotb-section p, .gotb-section li { font-size: 14px; line-height: 1.7; color: #444; }
.gotb-section ul { padding-left: 20px; margin: 0; }
.gotb-section li { margin-bottom: 6px; }

/* ── Comparison table ──────────────────────────────────────────────────────── */
.compare-wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 18px; }
.compare-col { border-radius: 8px; padding: 20px; }
.compare-col.free { background: #f0f6ff; border: 2px solid #3a6ea8; }
.compare-col.cert { background: #f9f9f9; border: 2px solid #bbb; }
.compare-col h3 { margin: 0 0 12px; font-size: 15px; font-weight: 700; }
.compare-col.free h3 { color: #2c5282; }
.compare-col.cert h3 { color: #555; }
.compare-col ul { padding-left: 16px; margin: 0; }
.compare-col li { font-size: 13px; color: #555; margin-bottom: 7px; line-height: 1.5; }
@media (max-width: 600px) { .compare-wrap { grid-template-columns: 1fr; } }

/* ── Progress bar ──────────────────────────────────────────────────────────── */
#progress-bar-wrap { margin-bottom: 22px; }
#progress-bar-label { font-size: 12px; color: #777; margin-bottom: 5px; }
#progress-bar { background: #e0e0e0; border-radius: 6px; height: 8px; }
#progress-fill { background: #3a6ea8; height: 8px; border-radius: 6px; transition: width .35s; width: 0%; }

/* ── Steps ─────────────────────────────────────────────────────────────────── */
.gotb-step { display: none; }
.gotb-step.active { display: block; }

/* ── Area nav dots ─────────────────────────────────────────────────────────── */
#area-nav { display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; }
.area-dot { width: 26px; height: 26px; border-radius: 50%; background: #e0e0e0; border: none; cursor: pointer; transition: background .2s; }
.area-dot.done { background: #3a6ea8; }
.area-dot.current { background: #3a6ea8; outline: 3px solid #9fc3e8; }

/* ── Question cards ─────────────────────────────────────────────────────────── */
.question-card { background: #fff; border: 1px solid #e0e0e0; border-radius: 10px; padding: 24px; margin-bottom: 16px; }
.question-card .q-num { font-size: 11px; text-transform: uppercase; letter-spacing: .07em; color: #999; margin-bottom: 6px; }
.question-card .q-text { font-size: 15px; font-weight: 600; color: #2c3e50; margin: 0 0 16px; line-height: 1.5; }
.choices { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
@media (max-width: 540px) { .choices { grid-template-columns: 1fr; } }

.choice-label { display: flex; align-items: flex-start; gap: 10px; padding: 12px 14px; border-radius: 8px; border: 2px solid transparent; cursor: pointer; transition: border-color .15s, background .15s; }
.choice-label input[type=radio] { display: none; }
.choice-dot { width: 16px; height: 16px; border-radius: 50%; border: 2px solid #bbb; flex-shrink: 0; margin-top: 2px; transition: border-color .15s, background .15s; }
.choice-main { flex: 1; }
.choice-name { font-size: 13px; font-weight: 700; display: block; }
.choice-desc { font-size: 12px; color: #777; display: block; margin-top: 2px; line-height: 1.4; }

/* Tier colors */
.c0 { background: #fff5f5; border-color: #f5cbcc; }
.c0 .choice-dot { border-color: #e57373; }
.c0 .choice-name { color: #c0392b; }
.c1 { background: #fff8f0; border-color: #fce5cd; }
.c1 .choice-dot { border-color: #e07b00; }
.c1 .choice-name { color: #a05000; }
.c2 { background: #f4fbf6; border-color: #c8e6c9; }
.c2 .choice-dot { border-color: #43a047; }
.c2 .choice-name { color: #2e7d32; }
.c3 { background: #eff6ff; border-color: #bee3f8; }
.c3 .choice-dot { border-color: #3a6ea8; }
.c3 .choice-name { color: #1a4a7a; }

.choice-label.selected { box-shadow: 0 0 0 2px rgba(58,110,168,.3); }
.c0.selected { border-color: #e57373; }
.c1.selected { border-color: #e07b00; }
.c2.selected { border-color: #43a047; }
.c3.selected { border-color: #3a6ea8; }
.selected .choice-dot { background: currentColor; border-width: 4px; }
.c0.selected .choice-dot { background: #e57373; border-color: #e57373; }
.c1.selected .choice-dot { background: #e07b00; border-color: #e07b00; }
.c2.selected .choice-dot { background: #43a047; border-color: #43a047; }
.c3.selected .choice-dot { background: #3a6ea8; border-color: #3a6ea8; }

/* ── Area header ────────────────────────────────────────────────────────────── */
.area-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
.area-pill { background: #2c3e50; color: #fff; font-size: 11px; text-transform: uppercase; letter-spacing: .08em; padding: 4px 12px; border-radius: 20px; }
.area-desc { font-size: 13px; color: #666; }

/* ── Buttons ────────────────────────────────────────────────────────────────── */
.gotb-btn { display: inline-block; padding: 13px 28px; border-radius: 8px; font-size: 15px; font-weight: 700; border: none; cursor: pointer; transition: opacity .2s; }
.gotb-btn:hover { opacity: .88; }
.btn-primary { background: #3a6ea8; color: #fff; }
.btn-secondary { background: #e0e0e0; color: #2c3e50; }
.btn-row { display: flex; gap: 12px; margin-top: 20px; flex-wrap: wrap; }

/* ── Gate form ──────────────────────────────────────────────────────────────── */
#step-gate { max-width: 500px; margin: 0 auto; }
.gate-card { background: #fff; border: 1px solid #e0e0e0; border-radius: 10px; padding: 32px; }
.gate-card h2 { margin: 0 0 8px; font-size: 20px; }
.gate-card p { font-size: 14px; color: #666; margin: 0 0 24px; }
.form-field { margin-bottom: 18px; }
.form-field label { display: block; font-size: 13px; font-weight: 700; margin-bottom: 6px; color: #2c3e50; }
.form-field input { width: 100%; padding: 10px 14px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; }
.form-field input:focus { outline: 2px solid #3a6ea8; border-color: #3a6ea8; }
#gate-error { color: #c0392b; font-size: 13px; margin-top: 10px; display: none; }
#submit-btn { width: 100%; margin-top: 6px; padding: 14px; font-size: 16px; }
.privacy-note { font-size: 12px; color: #888; text-align: center; margin-top: 14px; line-height: 1.5; }
.privacy-note a { color: #3a6ea8; }

/* ── Results ────────────────────────────────────────────────────────────────── */
#step-results { max-width: 680px; margin: 0 auto; }
.results-header { background: #2c3e50; color: #fff; border-radius: 10px 10px 0 0; padding: 28px 32px; text-align: center; }
.results-header h2 { margin: 0 0 4px; font-size: 20px; }
.results-header p { margin: 0; color: #adc9e8; font-size: 13px; }
.score-circle { width: 110px; height: 110px; border-radius: 50%; margin: 20px auto 8px; display: flex; align-items: center; justify-content: center; flex-direction: column; font-weight: 800; }
.score-num { font-size: 42px; line-height: 1; }
.score-sub { font-size: 11px; opacity: .7; }
.score-tier { font-size: 16px; font-weight: 700; margin: 4px 0 0; }
.score-indicative { font-size: 12px; color: #adc9e8; margin: 4px 0 0; font-style: italic; }

.results-body { background: #fff; border: 1px solid #e0e0e0; border-top: none; border-radius: 0 0 10px 10px; padding: 28px 32px; }

/* "report emailed" callout */
.emailed-notice { background: #f0faf4; border: 1px solid #a2d4a7; border-radius: 8px; padding: 14px 18px; margin-bottom: 22px; display: flex; align-items: flex-start; gap: 12px; }
.emailed-notice .icon { font-size: 20px; flex-shrink: 0; line-height: 1.2; }
.emailed-notice p { margin: 0; font-size: 13px; color: #1a5c0a; line-height: 1.5; }

/* Gap / strength callouts */
.gap-strength { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 22px; }
@media (max-width: 540px) { .gap-strength { grid-template-columns: 1fr; } }
.gs-card { border-radius: 8px; padding: 14px 16px; }
.gs-card.gap { background: #fff8e6; border: 1px solid #f5c800; }
.gs-card.str { background: #f0faf4; border: 1px solid #a2d4a7; }
.gs-card .gs-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .05em; margin-bottom: 4px; }
.gs-card.gap .gs-label { color: #7a5500; }
.gs-card.str .gs-label { color: #1a5c0a; }
.gs-card .gs-name { font-size: 14px; font-weight: 700; color: #2c3e50; }

/* Practice area bars */
.area-bar-row { margin-bottom: 16px; }
.area-bar-label { display: flex; justify-content: space-between; font-size: 13px; font-weight: 600; color: #2c3e50; margin-bottom: 4px; }
.area-bar-track { background: #eee; border-radius: 4px; height: 10px; }
.area-bar-fill { height: 10px; border-radius: 4px; transition: width .6s; }

/* Tier legend */
.tier-legend { margin: 24px 0 20px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
@media (max-width: 540px) { .tier-legend { grid-template-columns: 1fr 1fr; } }
.tier-block { border-radius: 6px; padding: 10px 8px; text-align: center; font-size: 12px; }
.tier-block .tier-name { font-weight: 700; display: block; }
.tier-block .tier-range { display: block; opacity: .8; margin-top: 3px; }
.tier-ineff { background: #f5cbcc; color: #7a0000; }
.tier-emerg { background: #fce5cd; color: #7a3800; }
.tier-effec { background: #d9ead3; color: #1a5c0a; }
.tier-highe { background: #d0e2f3; color: #0a2d5c; }

/* Limit-of-self-scoring block */
.limit-block { background: #f8f8f8; border: 1px solid #ddd; border-radius: 8px; padding: 18px 20px; margin-top: 22px; }
.limit-block h4 { margin: 0 0 8px; font-size: 13px; text-transform: uppercase; letter-spacing: .06em; color: #555; }
.limit-block p { margin: 0; font-size: 13px; color: #555; line-height: 1.65; }

/* CTA */
.results-cta { background: #2c3e50; border-radius: 10px; padding: 28px 32px; text-align: center; margin-top: 22px; }
.results-cta h3 { margin: 0 0 8px; color: #fff; font-size: 18px; }
.results-cta p { margin: 0 0 18px; color: #adc9e8; font-size: 13px; line-height: 1.6; }
.btn-cta { display: inline-block; background: #e8a000; color: #fff; text-decoration: none; padding: 13px 28px; border-radius: 8px; font-weight: 700; font-size: 15px; }

/* Disclaimer */
.disclaimer { font-size: 11px; color: #aaa; line-height: 1.6; margin-top: 18px; text-align: center; }
</style>

<div class="gotb-wrap">

<!-- Hero -->
<div class="gotb-hero">
  <h1>GOTB Index: Self Assessment</h1>
  <p>A free 18-question self-assessment for school board members based on the Great On Their Behalf index.<br>Takes about 5 minutes. Your results are personal and private.</p>
</div>

<!-- What this covers -->
<div class="gotb-section" id="intro-section">
  <h2>What this covers</h2>
  <p>The Great On Their Behalf (GOTB) index describes five practice areas that distinguish boards whose behavior creates the conditions for improving student outcomes. This self-assessment gives you an indicative read — based on your own perception — of where your board stands today.</p>
  <ul>
    <li><strong>Focus Mindset</strong> — whether the board keeps its attention fixed on improving outcomes for students</li>
    <li><strong>Clarify Priorities</strong> — whether the board has set clear, specific goals for students and guardrails for the superintendent — in writing</li>
    <li><strong>Monitor Progress</strong> — whether the board regularly checks real evidence of progress toward its goals — and acts on what it sees</li>
    <li><strong>Align Resources</strong> — whether the board's biggest decisions line up behind its goals</li>
    <li><strong>Communicate Results</strong> — whether the board reports progress honestly and in plain language to the community it serves</li>
  </ul>

  <div class="compare-wrap">
    <div class="compare-col free">
      <h3>GOTB Index: Self Assessment (this tool)</h3>
      <ul>
        <li>Free, individual, anonymous</li>
        <li>18 questions, ~5 minutes</li>
        <li>Based on your own perception</li>
        <li>Results are indicative — a directional read, not a validated measurement</li>
        <li>Useful for personal reflection and initial orientation</li>
      </ul>
    </div>
    <div class="compare-col cert">
      <h3>GOTB Index: Certified Assessment</h3>
      <ul>
        <li>Administered by a Certified Great On Their Behalf Practitioner</li>
        <li>Whole-board assessment, evidence-based scoring</li>
        <li>Psychometrically validated instrument</li>
        <li>Nationally benchmarked results</li>
        <li>Includes team-level analysis and formal report</li>
      </ul>
    </div>
  </div>

  <div class="btn-row" style="margin-top:24px;">
    <button class="gotb-btn btn-primary" id="start-btn">Start the Assessment</button>
  </div>
</div>

<!-- ── STEP: Questions ──────────────────────────────────────────────────────── -->
<div class="gotb-step" id="step-questions">
  <div id="progress-bar-wrap">
    <div id="progress-bar-label">Question <span id="q-current">1</span> of 18</div>
    <div id="progress-bar"><div id="progress-fill"></div></div>
  </div>
  <div id="area-nav" role="navigation" aria-label="Practice area progress"></div>
  <div id="question-area"></div>
  <div class="btn-row">
    <button class="gotb-btn btn-secondary" id="prev-btn">Back</button>
    <button class="gotb-btn btn-primary" id="next-btn">Next</button>
  </div>
</div>

<!-- ── STEP: Gate ──────────────────────────────────────────────────────────── -->
<div class="gotb-step" id="step-gate">
  <div class="gate-card">
    <h2>Almost there!</h2>
    <p>Enter your details below and we'll email you a full report — including a diagnosis and first-move recommendations for each practice area.</p>
    <div class="form-field">
      <label for="gate-name">Your name</label>
      <input type="text" id="gate-name" placeholder="First and last name" autocomplete="name">
    </div>
    <div class="form-field">
      <label for="gate-district">School district</label>
      <input type="text" id="gate-district" placeholder="e.g. Springfield Unified School District" autocomplete="organization">
    </div>
    <div class="form-field">
      <label for="gate-email">Email address</label>
      <input type="email" id="gate-email" placeholder="you@example.com" autocomplete="email">
    </div>
    <p id="gate-error">Please fill in all fields with a valid email address.</p>
    <button class="gotb-btn btn-primary" id="submit-btn">Email My Results</button>
    <p class="privacy-note">By submitting, you agree to receive your results and occasional governance resources from Effective School Boards, LLC. We never sell your information. <a href="/privacy-policy/">Privacy Policy</a></p>
  </div>
</div>

<!-- ── STEP: Results ───────────────────────────────────────────────────────── -->
<div class="gotb-step" id="step-results">
  <div class="results-header">
    <h2>GOTB Index: Self Assessment Results</h2>
    <p id="results-district"></p>
    <div class="score-circle" id="score-circle">
      <span class="score-num" id="score-num">—</span>
      <span class="score-sub">out of 100</span>
    </div>
    <div class="score-tier" id="score-tier"></div>
    <div class="score-indicative">Self-reported, indicative read</div>
  </div>

  <div class="results-body">

    <!-- "Report emailed" notice -->
    <div class="emailed-notice" id="emailed-notice" style="display:none;">
      <span class="icon">&#10003;</span>
      <p>Your full report — including a diagnosis and first-move recommendations for each practice area — has been sent to <strong id="emailed-to"></strong>.</p>
    </div>

    <!-- Gap / Strength -->
    <div class="gap-strength">
      <div class="gs-card gap">
        <div class="gs-label">Your Biggest Gap</div>
        <div class="gs-name" id="gap-label">—</div>
      </div>
      <div class="gs-card str">
        <div class="gs-label">Your Strength</div>
        <div class="gs-name" id="strength-label">—</div>
      </div>
    </div>

    <!-- Practice area bars -->
    <div id="area-bars"></div>

    <!-- Tier legend -->
    <div class="tier-legend">
      <div class="tier-block tier-ineff"><span class="tier-name">Beginning (indicative)</span><span class="tier-range">0 – 39</span></div>
      <div class="tier-block tier-emerg"><span class="tier-name">Emerging (indicative)</span><span class="tier-range">40 – 69</span></div>
      <div class="tier-block tier-effec"><span class="tier-name">Effective (indicative)</span><span class="tier-range">70 – 79</span></div>
      <div class="tier-block tier-highe"><span class="tier-name">Highly Effective (indicative)</span><span class="tier-range">80 – 100</span></div>
    </div>

    <!-- Limit-of-self-scoring block (required) -->
    <div class="limit-block">
      <h4>What this free read can't tell you</h4>
      <p>This is your board's story as you see it — scored by you, in this moment. It can't tell you whether your self-rating matches what a trained observer would score, how your board compares to others nationally, or where your fellow board members quietly see things differently. The Certified Assessment — the same instrument, administered by a Certified Great On Their Behalf Practitioner — gives you a validated, nationally benchmarked measurement of your whole board.</p>
    </div>

    <!-- CTA -->
    <div class="results-cta">
      <h3>Ready for the validated read?</h3>
      <p>The Certified Assessment is psychometrically validated, whole-board, nationally benchmarked — and administered by a Certified Great On Their Behalf Practitioner. No guessing. No self-scoring.</p>
      <a class="btn-cta" href="/consultation" id="consultation-cta">Schedule a Free Consultation</a>
    </div>

    <p class="disclaimer">
      © Effective School Boards LLC. The GOTB Index: Self Assessment is a self-scored, indicative tool.<br>
      It is not a validated or benchmarked measurement and should not be used for formal evaluation or accountability decisions.<br>
      "Student outcomes don't change until adult behaviors change."™
    </p>
  </div>
</div>

</div><!-- /.gotb-wrap -->

<script>
  (function () {
    'use strict';
    var API = 'https://esbcloud.taild49f53.ts.net:8443/gotb/submit';
    var FUNNEL_API = 'https://api.gotb.effectiveschoolboards.com/api/directory/leads/inbound/gotb-free';
    var QUIZ_VERSION = 'free-v2';

    // Six sections mirroring the validated instrument's six rows, presented
    // under the five-practice brand (Clarify Priorities split into two
    // labeled sub-sections). Each question is a first-person rendering of
    // exactly one named validated indicator (crosswalk kept server-side).
    var AREAS = [
      { id: 'focus',       practice: 1, label: 'Focus Mindset',                              desc: "Keeping the board's attention on student outcomes" },
      { id: 'vg',          practice: 2, label: 'Clarify Priorities: Vision & Goals',         desc: 'Clear, measurable student-outcome goals' },
      { id: 'gg',          practice: 2, label: 'Clarify Priorities: Values & Guardrails',    desc: 'Clear limits that protect the community’s values' },
      { id: 'monitor',     practice: 3, label: 'Monitor Progress',                           desc: 'Reviewing real evidence and acting on it' },
      { id: 'align',       practice: 4, label: 'Align Resources',                            desc: 'Connecting time, talent, and treasure to your goals' },
      { id: 'communicate', practice: 5, label: 'Communicate Results',                        desc: 'Honest, plain-language reporting to the community' },
    ];

    // Three questions per section in ladder order: Emerging, Effective,
    // Highly Effective anchors.
    var QUESTIONS = [
      { area: 0, id: 'focus.e',   level: 'Emerging',         text: "When we discuss how the school system is doing, we talk about students' results, not adult activity." },
      { area: 0, id: 'focus.eff', level: 'Effective',        text: 'Our substantive board discussion centers on student outcomes, not operations.' },
      { area: 0, id: 'focus.he',  level: 'Highly Effective', text: 'When progress stalls, we hold ourselves — the board — accountable, not staff or outside factors.' },
      { area: 1, id: 'vg.e',      level: 'Emerging',         text: 'We work from a small, focused set of written student-outcome goals we can name.' },
      { area: 1, id: 'vg.eff',    level: 'Effective',        text: 'Each goal names a measurable student outcome with a baseline, a numeric target, and a date.' },
      { area: 1, id: 'vg.he',     level: 'Highly Effective', text: 'We tie board decisions back to a specific goal.' },
      { area: 2, id: 'gg.e',      level: 'Emerging',         text: "When we set guardrails, we state what the superintendent may not do — and leave the 'how' alone." },
      { area: 2, id: 'gg.eff',    level: 'Effective',        text: 'Our guardrails describe observable operating limits, not vague values.' },
      { area: 2, id: 'gg.he',     level: 'Highly Effective', text: 'We check proposed actions against our guardrails before approving them.' },
      { area: 3, id: 'mon.e',     level: 'Emerging',         text: 'We follow a monitoring calendar, reviewing the goal or guardrail scheduled for that meeting.' },
      { area: 3, id: 'mon.eff',   level: 'Effective',        text: 'We devote at least half of each meeting to monitoring progress toward student-outcome goals.' },
      { area: 3, id: 'mon.he',    level: 'Highly Effective', text: 'Our monitoring ends with a judgment: is progress sufficient, and what is the board’s next step?' },
      { area: 4, id: 'al.e',      level: 'Emerging',         text: 'When we approve an expenditure, we ask how it supports our goals.' },
      { area: 4, id: 'al.eff',    level: 'Effective',        text: "We tie the superintendent's evaluation to progress on our goals and guardrails." },
      { area: 4, id: 'al.he',     level: 'Highly Effective', text: "We decline or defer items that don't advance a goal or guardrail." },
      { area: 5, id: 'com.e',     level: 'Emerging',         text: 'We share goals and progress with the community in plain, jargon-free language.' },
      { area: 5, id: 'com.eff',   level: 'Effective',        text: 'We communicate gaps as honestly as gains, not only good news.' },
      { area: 5, id: 'com.he',    level: 'Highly Effective', text: 'We invite the community to hold us accountable for progress toward our goals.' },
    ];

    var SCALE = [
      { name: 'Beginning',        desc: 'We don’t do this',             cls: 'c0' },
      { name: 'Emerging',         desc: 'We do this sometimes',          cls: 'c1' },
      { name: 'Effective',        desc: 'We do this consistently',       cls: 'c2' },
      { name: 'Highly Effective', desc: 'This is how we always operate', cls: 'c3' },
    ];
    var BAND_NAMES = ['Beginning', 'Emerging', 'Effective', 'Highly Effective'];

    var answers    = [];
    var areaIdx    = 0;
    var qIdxInArea = 0;

    function areaQuestions(a) { return QUESTIONS.filter(function(q){ return q.area === a; }); }

    // --- v2 scoring: same skeleton as the validated instrument ---
    // Row points 0-9; a level is confirmed when its anchor scores >= 2
    // ("we do this consistently"); row band climbs the ladder cumulatively;
    // total = points/54 x 100 unweighted; composite = lower median of the six
    // row bands, capped at Monitor Progress band + 1 (the Monitor gate).
    function rowPoints(ai) {
      var qs = areaQuestions(ai), sum = 0;
      qs.forEach(function(q){ var gi = QUESTIONS.indexOf(q); if (answers[gi] >= 0) sum += answers[gi]; });
      return sum;
    }
    function rowBand(ai) {
      var qs = areaQuestions(ai);
      function conf(levelIdx) { var gi = QUESTIONS.indexOf(qs[levelIdx]); return answers[gi] >= 2; }
      if (!conf(0)) return 0;
      if (!conf(1)) return 1;
      if (!conf(2)) return 2;
      return 3;
    }
    function allBands() { return AREAS.map(function(_, i){ return rowBand(i); }); }
    function lowerMedian(bands) {
      var s = bands.slice().sort(function(a,b){ return a-b; });
      return s[Math.floor((s.length - 1) / 2)];
    }
    function monitorBand() { return rowBand(3); }
    function compositeBand() {
      return Math.min(lowerMedian(allBands()), monitorBand() + 1);
    }
    function compositeCapped() {
      return compositeBand() < lowerMedian(allBands());
    }
    function totalPoints() {
      var sum = 0;
      for (var i = 0; i < AREAS.length; i++) sum += rowPoints(i);
      return sum;
    }
    function overallScore() { return Math.round(100 * totalPoints() / 54); }
    function getRating() { return BAND_NAMES[compositeBand()] + ' (indicative)'; }

    function getUtmParams() {
      var p = new URLSearchParams(location.search);
      return { source: p.get('utm_source'), medium: p.get('utm_medium'), campaign: p.get('utm_campaign') };
    }

    function tierColorClass(band) {
      return ['tier-ineff', 'tier-emerg', 'tier-effec', 'tier-highe'][band] || 'tier-ineff';
    }

    function barColor(areaId) {
      var colors = ['#4a86c8', '#e07b00', '#d4941e', '#3a9c5b', '#8e44ad', '#2c3e50'];
      return colors[areaId];
    }

    function globalQIdx() {
      var base = 0;
      for (var a = 0; a < areaIdx; a++) base += areaQuestions(a).length;
      return base + qIdxInArea;
    }

    function renderQuestion() {
      var area = AREAS[areaIdx];
      var qs   = areaQuestions(areaIdx);
      var gIdx = globalQIdx();

      document.getElementById('q-current').textContent = gIdx + 1;
      document.getElementById('progress-fill').style.width = (((gIdx + 1) / QUESTIONS.length) * 100) + '%';

      var nav = document.getElementById('area-nav');
      nav.innerHTML = '';
      for (var a = 0; a < AREAS.length; a++) {
        var dot = document.createElement('button');
        dot.className = 'area-dot' + (a < areaIdx ? ' done' : '') + (a === areaIdx ? ' current' : '');
        dot.setAttribute('aria-label', AREAS[a].label);
        dot.setAttribute('title', AREAS[a].label);
        nav.appendChild(dot);
      }

      var html = '<div class="area-header">'
        + '<span class="area-pill">Practice ' + area.practice + ' of 5</span>'
        + '<span class="area-desc">' + area.label + ' — ' + area.desc + '</span>'
        + '</div>'
        + '<div class="question-card">'
        + '<div class="q-num">Question ' + (qIdxInArea + 1) + ' of ' + qs.length + ' in this section</div>'
        + '<div class="q-text">' + qs[qIdxInArea].text + '</div>'
        + '<div class="choices">';

      for (var c = 0; c < SCALE.length; c++) {
        var sel = answers[gIdx] === c ? ' selected' : '';
        html += '<label class="choice-label ' + SCALE[c].cls + sel + '" data-choice="' + c + '">'
          + '<input type="radio" name="q' + gIdx + '" value="' + c + '"' + (answers[gIdx] === c ? ' checked' : '') + '>'
          + '<span class="choice-dot"></span>'
          + '<span class="choice-main">'
          + '<span class="choice-name">' + SCALE[c].name + '</span>'
          + '<span class="choice-desc">' + SCALE[c].desc + '</span>'
          + '</span></label>';
      }

      html += '</div></div>';
      document.getElementById('question-area').innerHTML = html;

      var labels = document.querySelectorAll('.choice-label');
      labels.forEach(function(lbl) {
        lbl.addEventListener('click', function() {
          var ci = parseInt(this.getAttribute('data-choice'));
          answers[globalQIdx()] = ci;
          labels.forEach(function(l){ l.classList.remove('selected'); });
          this.classList.add('selected');
          var radio = this.querySelector('input[type=radio]');
          if (radio) radio.checked = true;
        });
      });

      document.getElementById('prev-btn').style.display = (areaIdx === 0 && qIdxInArea === 0) ? 'none' : '';
      document.getElementById('next-btn').textContent =
        (areaIdx === AREAS.length - 1 && qIdxInArea === qs.length - 1) ? 'See Results' : 'Next';
    }

    function goNext() {
      var gIdx = globalQIdx();
      if (answers[gIdx] < 0) {
        document.querySelectorAll('.question-card').forEach(function(c){ c.style.borderColor = '#e57373'; });
        return;
      }
      var qs = areaQuestions(areaIdx);
      if (qIdxInArea < qs.length - 1) {
        qIdxInArea++;
      } else if (areaIdx < AREAS.length - 1) {
        areaIdx++;
        qIdxInArea = 0;
      } else {
        showGate();
        return;
      }
      renderQuestion();
    }

    function goPrev() {
      if (qIdxInArea > 0) {
        qIdxInArea--;
      } else if (areaIdx > 0) {
        areaIdx--;
        qIdxInArea = areaQuestions(areaIdx).length - 1;
      }
      renderQuestion();
    }

    function showStep(id) {
      document.querySelectorAll('.gotb-step').forEach(function(s){ s.classList.remove('active'); });
      document.getElementById(id).classList.add('active');
      document.getElementById('intro-section').style.display = 'none';
    }

    function startAssessment() {
      showStep('step-questions');
      renderQuestion();
    }

    function showGate() {
      showStep('step-gate');
    }

    function showResults(name, district, email, emailSent) {
      showStep('step-results');

      var overall = overallScore();
      var band    = compositeBand();
      var rating  = getRating();

      var circle = document.getElementById('score-circle');
      circle.className = 'score-circle';
      circle.classList.add(tierColorClass(band));
      document.getElementById('score-num').textContent = overall;
      var tierEl = document.getElementById('score-tier');
      tierEl.textContent = rating;
      tierEl.className = 'score-tier';
      tierEl.style.color = ['#f5cbcc', '#fce5cd', '#a8d5b5', '#adc9e8'][band];

      // Monitor-gate annotation: the composite band never sits more than one
      // band above Monitor Progress.
      var capNote = document.getElementById('cap-note');
      if (!capNote) {
        capNote = document.createElement('p');
        capNote.id = 'cap-note';
        capNote.style.cssText = 'font-size:0.85rem;color:#666;margin:0.5rem auto 0;max-width:480px;text-align:center;';
        tierEl.parentNode.insertBefore(capNote, tierEl.nextSibling);
      }
      capNote.textContent = compositeCapped()
        ? 'Your overall band is capped by Monitor Progress — monitoring is the practice everything else depends on, so your board’s overall level can sit at most one band above it.'
        : '';

      document.getElementById('results-district').textContent = district;

      if (emailSent) {
        var notice = document.getElementById('emailed-notice');
        notice.style.display = 'flex';
        document.getElementById('emailed-to').textContent = email;
      }

      var rows = AREAS.map(function(a, i){ return { label: a.label, pts: rowPoints(i), band: rowBand(i) }; });
      var sorted = rows.slice().sort(function(a,b){ return a.pts - b.pts; });
      document.getElementById('gap-label').textContent = sorted[0].label;
      document.getElementById('strength-label').textContent = sorted[sorted.length - 1].label;

      var barsHtml = '';
      rows.forEach(function(row, i) {
        var pct = Math.round(row.pts / 9 * 100);
        barsHtml += '<div class="area-bar-row">'
          + '<div class="area-bar-label"><span>' + row.label + '</span><span>' + BAND_NAMES[row.band] + ' · ' + row.pts + ' / 9</span></div>'
          + '<div class="area-bar-track"><div class="area-bar-fill" style="width:' + pct + '%;background:' + barColor(i) + ';"></div></div>'
          + '</div>';
      });
      document.getElementById('area-bars').innerHTML = barsHtml;
    }

    function submitGate() {
      var name     = document.getElementById('gate-name').value.trim();
      var district = document.getElementById('gate-district').value.trim();
      var email    = document.getElementById('gate-email').value.trim();
      var errEl    = document.getElementById('gate-error');

      if (!name || !district || !email || !email.includes('@') || !email.includes('.')) {
        errEl.style.display = 'block';
        return;
      }
      errEl.style.display = 'none';

      var btn = document.getElementById('submit-btn');
      btn.textContent = 'Sending…';
      btn.disabled = true;

      var overall = overallScore();
      var rating  = getRating();
      var utm = getUtmParams();
      var bands = allBands();

      // Element 0 is a version/meta record; the rest are every individual
      // response, self-describing (question text + section + level + chosen
      // scale label) so the funnel admin sees exactly how someone answered.
      var fullAnswers = [{
        version: QUIZ_VERSION,
        row_points: { focus: rowPoints(0), clarify_vision_goals: rowPoints(1), clarify_values_guardrails: rowPoints(2), monitor: rowPoints(3), align: rowPoints(4), communicate: rowPoints(5) },
        row_bands: { focus: bands[0], clarify_vision_goals: bands[1], clarify_values_guardrails: bands[2], monitor: bands[3], align: bands[4], communicate: bands[5] },
        composite_band: compositeBand(),
        composite_capped_by_monitor: compositeCapped(),
        total_points: totalPoints(),
      }].concat(QUESTIONS.map(function (q, i) {
        return {
          id: q.id,
          area: AREAS[q.area].label,
          level: q.level,
          question: q.text,
          answer: answers[i] >= 0 ? SCALE[answers[i]].name : null,
          value: answers[i] >= 0 ? answers[i] : null,
        };
      }));

      var payload = {
        name: name,
        district: district,
        email: email,
        total_score: overall,
        rating: rating,
        score_focus:       Math.round(rowPoints(0) / 9 * 100),
        score_priorities:  Math.round((rowPoints(1) + rowPoints(2)) / 18 * 100),
        score_monitor:     Math.round(rowPoints(3) / 9 * 100),
        score_align:       Math.round(rowPoints(4) / 9 * 100),
        score_communicate: Math.round(rowPoints(5) / 9 * 100),
        answers:       fullAnswers,
        referrer:      document.referrer || null,
        landing_path:  location.pathname + location.search,
        source_site:   location.hostname,
        utm_source:    utm.source,
        utm_medium:    utm.medium,
        utm_campaign:  utm.campaign,
      };

      fetch(FUNNEL_API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
      .then(function(r){ return r.json(); })
      .then(function(data){
        if (!data || !data.lead_id) return;
        var cta = document.getElementById('consultation-cta');
        if (!cta) return;
        var params = new URLSearchParams({
          lead_id: data.lead_id, name: name, email: email, district: district,
        });
        cta.href = '/consultation?' + params.toString();
      })
      .catch(function(){ /* funnel capture is best-effort */ });

      fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
      .then(function(r){ return r.json(); })
      .then(function(data){
        showResults(name, district, email, !!(data && data.sent));
      })
      .catch(function(){
        showResults(name, district, email, false);
      });
    }

    document.addEventListener('DOMContentLoaded', function () {
      document.getElementById('next-btn').addEventListener('click', goNext);
      document.getElementById('prev-btn').addEventListener('click', goPrev);
      document.getElementById('submit-btn').addEventListener('click', submitGate);
      document.getElementById('gate-email').addEventListener('keydown', function(e){
        if (e.key === 'Enter') submitGate();
      });
      answers = new Array(QUESTIONS.length).fill(-1);
      document.getElementById('start-btn').addEventListener('click', startAssessment);
    });
  })();
  </script>
