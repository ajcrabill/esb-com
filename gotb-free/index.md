---
layout: base
title: "Free School Board Self-Assessment"
description: "Take the free Great On Their Behalf (GOTB) Self-Assessment to see how effective your school board is at improving student outcomes. Get your 0–100 score instantly."
summary: "GOTB Self-Assessment"
toplevel: Resources
---

<style>
#gotb-app { margin: 0 -15px; }
.gotb-step { display: none; }
.gotb-step.active { display: block; }

/* Intro */
.gotb-intro { text-align: center; padding: 40px 20px; }
.gotb-intro h2 { font-size: 2rem; color: #2c3e50; margin-bottom: 16px; }
.gotb-intro p { font-size: 1.1rem; color: #555; max-width: 620px; margin: 0 auto 28px; }
.gotb-score-sample { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin-bottom: 32px; }
.score-band { padding: 10px 20px; border-radius: 8px; font-weight: 600; font-size: 0.9rem; }
.score-band.ineff { background: #f5cbcc; color: #7a0000; }
.score-band.emerg { background: #fce5cd; color: #7a3800; }
.score-band.effec { background: #d9ead3; color: #1a5c0a; }
.score-band.highe { background: #d0e2f3; color: #0a2d5c; }

/* Progress bar */
.gotb-progress-wrap { background: #eee; border-radius: 10px; height: 8px; margin-bottom: 8px; }
.gotb-progress-bar { background: linear-gradient(90deg, #4a86c8, #2c6fad); height: 8px; border-radius: 10px; transition: width 0.4s ease; }
.gotb-progress-label { font-size: 0.82rem; color: #888; text-align: right; margin-bottom: 20px; }

/* Area header */
.gotb-area-header { background: #2c3e50; color: #fff; padding: 16px 20px; border-radius: 8px 8px 0 0; margin-bottom: 0; }
.gotb-area-header h4 { margin: 0; font-size: 1.1rem; }
.gotb-area-header .area-weight { font-size: 0.82rem; opacity: 0.75; margin-top: 2px; }

/* Question cards */
.gotb-question-card { border: 1px solid #ddd; border-radius: 0; padding: 20px; background: #fff; border-top: none; }
.gotb-question-card:last-of-type { border-radius: 0 0 8px 8px; margin-bottom: 24px; }
.gotb-question-card .q-number { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em; color: #999; margin-bottom: 4px; }
.gotb-question-card .q-text { font-size: 1rem; font-weight: 600; color: #2c3e50; margin-bottom: 14px; }

/* Answer choices */
.gotb-choices { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
@media (max-width: 600px) { .gotb-choices { grid-template-columns: 1fr; } }

.gotb-choice { position: relative; cursor: pointer; }
.gotb-choice input[type="radio"] { position: absolute; opacity: 0; width: 0; height: 0; }
.gotb-choice label {
  display: block; padding: 10px 14px; border-radius: 6px; cursor: pointer;
  border: 2px solid transparent; transition: all 0.2s; font-size: 0.87rem;
  line-height: 1.4;
}
.gotb-choice label .level-name { font-weight: 700; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; display: block; margin-bottom: 3px; }

.gotb-choice.ineff label { background: #f5cbcc; border-color: #e8a0a1; }
.gotb-choice.emerg label { background: #fce5cd; border-color: #f5c8a0; }
.gotb-choice.effec label { background: #d9ead3; border-color: #b2d4a7; }
.gotb-choice.highe label { background: #d0e2f3; border-color: #a2c4e3; }

.gotb-choice input:checked + label { border-width: 2px; box-shadow: 0 0 0 2px rgba(44,111,173,0.35); }
.gotb-choice.ineff input:checked + label { border-color: #c00; }
.gotb-choice.emerg input:checked + label { border-color: #b85c00; }
.gotb-choice.effec input:checked + label { border-color: #2a7d00; }
.gotb-choice.highe input:checked + label { border-color: #0a47a0; }

/* Navigation buttons */
.gotb-nav { display: flex; justify-content: space-between; align-items: center; margin-top: 8px; margin-bottom: 32px; }
.btn-gotb-primary { background: #2c6fad; color: #fff; border: none; padding: 12px 28px; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background 0.2s; }
.btn-gotb-primary:hover { background: #245d91; }
.btn-gotb-secondary { background: transparent; color: #2c6fad; border: 2px solid #2c6fad; padding: 10px 24px; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.2s; }
.btn-gotb-secondary:hover { background: #2c6fad; color: #fff; }
.gotb-unanswered-msg { color: #c00; font-size: 0.88rem; display: none; }

/* Gate / Lead capture */
.gotb-gate { max-width: 520px; margin: 0 auto; }
.gotb-gate h3 { font-size: 1.5rem; color: #2c3e50; margin-bottom: 8px; }
.gotb-gate .gate-sub { color: #666; margin-bottom: 24px; font-size: 0.95rem; }
.gotb-gate .score-preview { text-align: center; margin: 20px 0 28px; }
.gotb-gate .score-preview .score-circle {
  display: inline-block; width: 110px; height: 110px; border-radius: 50%;
  background: #2c3e50; color: #fff; line-height: 1.1;
  font-size: 2.4rem; font-weight: 700; text-align: center; padding-top: 24px;
}
.gotb-gate .score-preview .score-label { font-size: 0.85rem; color: #888; margin-top: 8px; }
.gotb-gate label { font-weight: 600; font-size: 0.9rem; color: #444; display: block; margin-bottom: 4px; margin-top: 14px; }
.gotb-gate input { width: 100%; padding: 10px 14px; border: 1px solid #ccc; border-radius: 6px; font-size: 0.95rem; }
.gotb-gate input:focus { outline: none; border-color: #2c6fad; box-shadow: 0 0 0 3px rgba(44,111,173,0.15); }
.gate-submit-row { margin-top: 24px; text-align: center; }
.gate-privacy { font-size: 0.78rem; color: #999; margin-top: 10px; }
.btn-gotb-submit { background: #e8a000; color: #fff; border: none; padding: 14px 36px; border-radius: 6px; font-size: 1.05rem; font-weight: 700; cursor: pointer; transition: background 0.2s; width: 100%; }
.btn-gotb-submit:hover { background: #cc8c00; }
.btn-gotb-submit:disabled { background: #ccc; cursor: default; }
.gate-error { color: #c00; font-size: 0.88rem; margin-top: 8px; display: none; }

/* Results */
.gotb-results { max-width: 680px; margin: 0 auto; }
.gotb-results h3 { font-size: 1.6rem; color: #2c3e50; margin-bottom: 6px; }
.gotb-results .results-intro { color: #555; margin-bottom: 28px; }
.total-score-block { text-align: center; padding: 28px; border-radius: 10px; margin-bottom: 28px; }
.total-score-block .big-score { font-size: 4rem; font-weight: 800; line-height: 1; }
.total-score-block .score-out-of { font-size: 1rem; opacity: 0.75; }
.total-score-block .score-label { font-size: 1.1rem; font-weight: 600; margin-top: 6px; }
.total-score-block.ineff { background: #f5cbcc; color: #7a0000; }
.total-score-block.emerg { background: #fce5cd; color: #7a3800; }
.total-score-block.effec { background: #d9ead3; color: #1a5c0a; }
.total-score-block.highe { background: #d0e2f3; color: #0a2d5c; }

/* Area score bars */
.area-scores { margin-bottom: 28px; }
.area-score-row { margin-bottom: 14px; }
.area-score-row .area-name { font-weight: 600; font-size: 0.92rem; color: #2c3e50; display: flex; justify-content: space-between; margin-bottom: 4px; }
.area-bar-bg { background: #eee; border-radius: 6px; height: 18px; overflow: hidden; }
.area-bar-fill { height: 18px; border-radius: 6px; transition: width 0.8s ease; }

/* Interpretation */
.gotb-interpretation { border-left: 4px solid #2c6fad; padding: 16px 20px; background: #f4f8fc; border-radius: 0 8px 8px 0; margin-bottom: 24px; font-size: 0.93rem; color: #333; }
.gotb-cta-block { background: #2c3e50; color: #fff; padding: 28px; border-radius: 10px; text-align: center; margin-bottom: 12px; }
.gotb-cta-block h4 { color: #fff; margin-bottom: 10px; }
.gotb-cta-block p { color: #ccc; margin-bottom: 18px; font-size: 0.92rem; }
.btn-gotb-cta { background: #e8a000; color: #fff; border: none; padding: 12px 28px; border-radius: 6px; font-size: 1rem; font-weight: 700; cursor: pointer; text-decoration: none; display: inline-block; }
.btn-gotb-cta:hover { background: #cc8c00; color: #fff; text-decoration: none; }

/* Sending overlay */
.gotb-sending { text-align: center; padding: 40px 20px; color: #555; }
.gotb-spinner { border: 3px solid #eee; border-top: 3px solid #2c6fad; border-radius: 50%; width: 40px; height: 40px; animation: spin 0.8s linear infinite; margin: 0 auto 16px; }
@keyframes spin { to { transform: rotate(360deg); } }
</style>

<div id="gotb-app">

  <!-- ── STEP: INTRO ── -->
  <div id="step-intro" class="gotb-step active">
    <div class="gotb-intro">
      <p style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.08em;color:#2c6fad;margin-bottom:8px;font-weight:600;">Free Self-Assessment</p>
      <h2>How Effective Is Your School Board?</h2>
      <p>The <strong>Great On Their Behalf (GOTB) Self-Assessment</strong> is a 20-question instrument based on the Effective School Boards framework. Answer honestly — there are no right or wrong grades, only a clearer picture of where your board stands.</p>

      <div class="gotb-score-sample">
        <div class="score-band ineff">0–39: Ineffective</div>
        <div class="score-band emerg">40–69: Emerging</div>
        <div class="score-band effec">70–79: Effective</div>
        <div class="score-band highe">80–100: Highly Effective</div>
      </div>

      <p style="font-size:0.88rem;color:#888;margin-bottom:24px;">Takes about 5–8 minutes &nbsp;•&nbsp; Results emailed to you &nbsp;•&nbsp; No purchase required</p>

      <button class="btn-gotb-primary" onclick="startAssessment()" style="font-size:1.1rem;padding:14px 40px;">Start the Assessment &rarr;</button>
    </div>

    <div style="background:#f9f9f9;border-radius:10px;padding:24px 28px;max-width:680px;margin:0 auto 20px;">
      <h5 style="margin-bottom:10px;color:#2c3e50;">What This Assessment Covers</h5>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <div style="font-size:0.88rem;color:#555;"><strong style="color:#2c3e50;">Focus Mindset</strong><br>Training, self-evaluation &amp; outcomes-clarity</div>
        <div style="font-size:0.88rem;color:#555;"><strong style="color:#2c3e50;">Clarify Priorities</strong><br>Goals, guardrails &amp; community voice</div>
        <div style="font-size:0.88rem;color:#555;"><strong style="color:#2c3e50;">Monitor Progress</strong><br>Monitoring calendar, quality &amp; data</div>
        <div style="font-size:0.88rem;color:#555;"><strong style="color:#2c3e50;">Align Resources</strong><br>Role clarity, evaluation &amp; governance</div>
        <div style="font-size:0.88rem;color:#555;"><strong style="color:#2c3e50;">Communicate Results</strong><br>Meeting structure &amp; community engagement</div>
      </div>
    </div>
  </div>

  <!-- ── STEP: QUESTIONS ── -->
  <div id="step-questions" class="gotb-step">
    <div class="gotb-progress-wrap"><div class="gotb-progress-bar" id="progress-bar" style="width:0%"></div></div>
    <div class="gotb-progress-label" id="progress-label">Question 0 of 20</div>

    <div id="questions-container"></div>

    <div class="gotb-nav">
      <button class="btn-gotb-secondary" id="btn-prev" onclick="prevArea()" style="display:none">&larr; Previous</button>
      <div>
        <span class="gotb-unanswered-msg" id="unanswered-msg">Please answer all questions before continuing.</span>
      </div>
      <button class="btn-gotb-primary" id="btn-next" onclick="nextArea()">Next &rarr;</button>
    </div>
  </div>

  <!-- ── STEP: SENDING ── -->
  <div id="step-sending" class="gotb-step">
    <div class="gotb-sending">
      <div class="gotb-spinner"></div>
      <p>Calculating your score and sending results&hellip;</p>
    </div>
  </div>

  <!-- ── STEP: GATE (Lead capture) ── -->
  <div id="step-gate" class="gotb-step">
    <div class="gotb-gate">
      <h3>You've Completed the Assessment!</h3>
      <p class="gate-sub">Enter your information below to receive your full results by email and see your score breakdown on screen.</p>

      <div class="score-preview">
        <div class="score-circle" id="gate-score-circle">—</div>
        <div class="score-label">Your score is ready</div>
      </div>

      <form id="gate-form" onsubmit="handleGateSubmit(event)" novalidate>
        <label for="gate-name">Your Name</label>
        <input type="text" id="gate-name" name="name" placeholder="First and last name" required>

        <label for="gate-district">School District</label>
        <input type="text" id="gate-district" name="district" placeholder="e.g. Lincoln Unified School District" required>

        <label for="gate-email">Email Address</label>
        <input type="email" id="gate-email" name="email" placeholder="you@example.com" required>

        <div class="gate-submit-row">
          <button type="submit" class="btn-gotb-submit" id="gate-submit-btn">Email Me My Results &rarr;</button>
          <div class="gate-error" id="gate-error">Something went wrong. Please try again.</div>
          <p class="gate-privacy">We respect your privacy. Your information will only be used to send your results and relevant school board resources. No spam, ever.</p>
        </div>
      </form>
    </div>
  </div>

  <!-- ── STEP: RESULTS ── -->
  <div id="step-results" class="gotb-step">
    <div class="gotb-results">
      <h3 id="results-headline">Your School Board Assessment Results</h3>
      <p class="results-intro" id="results-intro"></p>

      <div class="total-score-block" id="total-score-block">
        <div class="big-score" id="result-total-score">—</div>
        <div class="score-out-of">out of 100</div>
        <div class="score-label" id="result-rating">—</div>
      </div>

      <div class="area-scores" id="area-scores-container"></div>

      <div class="gotb-interpretation" id="gotb-interpretation"></div>

      <div class="gotb-cta-block">
        <h4>Want to Move the Needle?</h4>
        <p>Most boards go from their starting score to 80+ in two years — but only with a certified coach. It's not about working harder; it's about working differently.</p>
        <a href="/consultation" class="btn-gotb-cta">Schedule a Free Consultation</a>
      </div>

      <p style="font-size:0.82rem;color:#aaa;text-align:center;">Results have been sent to the email address you provided. Check your spam folder if you don't see them within a few minutes.</p>
    </div>
  </div>

</div><!-- #gotb-app -->

<script>
(function(){

var API_ENDPOINT = 'https://esbcloud.taild49f53.ts.net:8443/gotb/submit';

var AREAS = [
  { id: 'focus',       name: 'Focus Mindset',       max: 10, color: '#4a86c8' },
  { id: 'priorities',  name: 'Clarify Priorities',  max: 35, color: '#e07b00' },
  { id: 'monitor',     name: 'Monitor Progress',     max: 30, color: '#3a9c5b' },
  { id: 'align',       name: 'Align Resources',      max: 20, color: '#8e44ad' },
  { id: 'communicate', name: 'Communicate Results',  max:  5, color: '#2c3e50' },
];

var QUESTIONS = [
  // ── Area 1: Focus Mindset ──
  {
    area: 0,
    text: 'How has our board engaged with school board governance training?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board has received no training on effective school board governance in the past 36 months.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has received training on an effective school board framework within the past 36 months.' },
      { cls:'effec', label:'Effective',        text:'Board members have both received training and helped facilitate at least one governance training session in the past 12 months.' },
      { cls:'highe', label:'Highly Effective', text:'Our training program includes students presenting, new members train before their first vote, and framework training is ongoing and embedded.' },
    ]
  },
  {
    area: 0,
    text: 'How consistently does our board conduct formal self-evaluations?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board has not conducted a formal self-evaluation in the past 12 months.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has self-evaluations scheduled on a regular calendar (quarterly or annually timed near the superintendent evaluation).' },
      { cls:'effec', label:'Effective',        text:'Our board completed a self-evaluation within the past 12 months using this or an aligned instrument and voted to adopt the results.' },
      { cls:'highe', label:'Highly Effective', text:'Our self-evaluation was completed within the required timeframe AND board members shared examples of when their own behaviors hindered student goal achievement.' },
    ]
  },
  {
    area: 0,
    text: 'How clearly can our board distinguish adult inputs from student outcomes?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'I often cannot clearly tell the difference between adult inputs (what adults do or spend) and student outcomes (what students achieve).' },
      { cls:'emerg', label:'Emerging',         text:'I can distinguish adult inputs from student outcomes, though our board discussions still frequently center on inputs rather than outcomes.' },
      { cls:'effec', label:'Effective',        text:'I consistently distinguish inputs from outcomes and regularly redirect board conversations to focus on student outcomes.' },
      { cls:'highe', label:'Highly Effective', text:'Our board reliably focuses on student outcomes, and our tracked meeting-time data confirms this pattern meeting after meeting.' },
    ]
  },
  {
    area: 0,
    text: 'How does our board track and analyze how its meeting time is spent?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board does not track how meeting time is spent or what percentage focuses on student outcomes.' },
      { cls:'emerg', label:'Emerging',         text:'Our board tracks and reports quarterly on the percentage of meeting time focused on student outcomes.' },
      { cls:'effec', label:'Effective',        text:'Our board tracks meeting time AND annually reports the cost of staff governance time during our self-evaluation.' },
      { cls:'highe', label:'Highly Effective', text:'Our tracking data shows consistent year-over-year improvement in the percentage of meeting time devoted to student outcome discussions.' },
    ]
  },
  // ── Area 2: Clarify Priorities ──
  {
    area: 1,
    text: 'How well-defined are our board\'s student outcome goals?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board has no adopted student outcome goals, or our goals are vague, input-focused, or not SMART (Specific, Measurable, Achievable, Relevant, Time-bound).' },
      { cls:'emerg', label:'Emerging',         text:'Our board has adopted 1–5 SMART goals focused on student outcomes, developed with input from students, parents, staff, and community members.' },
      { cls:'effec', label:'Effective',        text:'Our goals are SMART, and the superintendent has adopted 1–3 predictive, influenceable interim goals per board goal — all focused on student outputs/outcomes (not adult inputs).' },
      { cls:'highe', label:'Highly Effective', text:'All goals span 3–5 years with yearly targets; all interim goals span 1–3 years; and every board member can recite all goals and current status from memory.' },
    ]
  },
  {
    area: 1,
    text: 'How inclusive and community-grounded was our goal development process?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our goals were created without meaningful community input, root cause analysis, or comprehensive needs assessment.' },
      { cls:'emerg', label:'Emerging',         text:'Our goals were developed with diverse community stakeholders and posted for public comment before adoption.' },
      { cls:'effec', label:'Effective',        text:'Our goal development generated genuine community ownership, and all board members agree the goals require significant organizational behavior change.' },
      { cls:'highe', label:'Highly Effective', text:'The inclusive process produced goals that authentically represent community voice and present a genuine stretch that challenges our entire organization.' },
    ]
  },
  {
    area: 1,
    text: 'Has our board adopted guardrails defining what approaches the superintendent may NOT use in pursuing goals?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board has not adopted guardrails — statements that describe a single operational approach the superintendent may not use.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has adopted 1–5 guardrails grounded in community values, each describing a single approach the superintendent may not use.' },
      { cls:'effec', label:'Effective',        text:'Our board has guardrails, and the superintendent has adopted 1–3 interim guardrails per guardrail with annual targets; all focus on outcomes, not inputs.' },
      { cls:'highe', label:'Highly Effective', text:'All guardrails span 3–5 years, are adopted through an inclusive process, and our board has also adopted guardrails on its own behavior which we evaluate quarterly.' },
    ]
  },
  {
    area: 1,
    text: 'How well-structured are our annual interim targets and milestones?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our goals do not include clear annual targets or interim milestones that can be tracked and updated throughout the year.' },
      { cls:'emerg', label:'Emerging',         text:'Our goals include identified annual targets and yearly ending points through the goal deadline.' },
      { cls:'effec', label:'Effective',        text:'Interim goal ending points are established for each year through the deadline, and interim goal status can be updated multiple times per year.' },
      { cls:'highe', label:'Highly Effective', text:'All targets are set, our board and superintendent agree that achieving them requires major organizational change, and the targets represent a genuine institutional stretch.' },
    ]
  },
  // ── Area 3: Monitor Progress ──
  {
    area: 2,
    text: 'Does our board have an adopted monitoring calendar that governs how we track goal progress?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board has no adopted monitoring calendar, or goals are not scheduled for monitoring at least 4 times per year.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has a monitoring calendar developed with superintendent input — no more than 2 goals per month, every goal monitored at least 4 times annually.' },
      { cls:'effec', label:'Effective',        text:'Our board formally adopted the monitoring calendar, and goals/guardrails/calendar have been modified no more than once during the current goal span.' },
      { cls:'highe', label:'Highly Effective', text:'Our monitoring calendar is stable and adopted, and our board invests 50%+ of total monthly public meeting minutes in effective goal monitoring.' },
    ]
  },
  {
    area: 2,
    text: 'How would you rate the quality of our board\'s monitoring conversations?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'During monitoring, board members frequently ask operational questions, discuss future plans, or make comments rather than using data to examine student results.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has received training on effective monitoring and has completed at least one practice monitoring session.' },
      { cls:'effec', label:'Effective',        text:'Our board demonstrated effective monitoring (80%+ quality score) during each monitoring conversation in the past 12 months.' },
      { cls:'highe', label:'Highly Effective', text:'Our board consistently achieves highly effective monitoring (90%+), with strategy-focused, measure-referenced, open-ended, results-oriented, time-bound questions.' },
    ]
  },
  {
    area: 2,
    text: 'How does our board use monitoring reports and data from the superintendent?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board does not receive formal monitoring reports on a calendar, or our school system achieved no interim goals in the past 12 months.' },
      { cls:'emerg', label:'Emerging',         text:'Our board receives monitoring reports per the calendar, and the superintendent\'s team has been trained on creating effective monitoring reports.' },
      { cls:'effec', label:'Effective',        text:'Our board publicly displays goal status and targets in our regular meeting room and provides time recognizing student and staff accomplishments toward goals.' },
      { cls:'highe', label:'Highly Effective', text:'Our school system achieved at least half of interim goals in the past 12 months, and monitoring reports are received per calendar with full data.' },
    ]
  },
  {
    area: 2,
    text: 'What share of our public board meeting time is devoted to effective goal monitoring?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Most of our meeting time goes to routine approvals, operational presentations, and non-monitoring topics — goal monitoring is a small fraction.' },
      { cls:'emerg', label:'Emerging',         text:'Our board monitors goals at every scheduled session, though monitoring may still represent less than a third of total meeting time.' },
      { cls:'effec', label:'Effective',        text:'Our board consistently prioritizes goal monitoring in public meetings and tracks meeting time use to continually improve.' },
      { cls:'highe', label:'Highly Effective', text:'Our board has data showing it invests 50% or more of total monthly public meeting minutes in effective goal monitoring.' },
    ]
  },
  // ── Area 4: Align Resources ──
  {
    area: 3,
    text: 'How clearly does our board maintain the distinction between board governance and superintendent management?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Board members sometimes give operational advice to staff, vote on superintendent implementation plans, or serve on operational committees outside proper protocols.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has discussed the governance vs. management distinction, and members generally agree that committees advise the board — not staff.' },
      { cls:'effec', label:'Effective',        text:'Our board has an Ethics & Conflicts of Interest Statement signed by all current members, committing to no operational advice to staff and recusal from conflicts.' },
      { cls:'highe', label:'Highly Effective', text:'Our board unanimously affirms annually that all members adhered to governing policies, honored ethical boundaries, and gave no operational advice during the past year.' },
    ]
  },
  {
    area: 3,
    text: 'How is our superintendent\'s evaluation structured?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our superintendent evaluation includes criteria beyond board goals and guardrails — such as personality traits, relationships, or non-goal accomplishments.' },
      { cls:'emerg', label:'Emerging',         text:'Our superintendent evaluation is based solely on goals, guardrails, and interim goals/guardrails.' },
      { cls:'effec', label:'Effective',        text:'Our superintendent has never gone more than 12 months without a formal evaluation, and evaluations are completed on schedule.' },
      { cls:'highe', label:'Highly Effective', text:'Our annual budget is only approved after a deliberate determination that resources are prioritized toward board goals; superintendent evaluation is goals-only and on time every year.' },
    ]
  },
  {
    area: 3,
    text: 'How robust are our board\'s governance operating procedures and delegation policies?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board lacks adopted governance operating procedures or delegation policies, or has members with undisclosed conflicts of interest.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has adopted governance operating procedures, and the superintendent provides implementation plans without requiring board approval (except where legally mandated).' },
      { cls:'effec', label:'Effective',        text:'Our board has a policy requiring information given to one member to be provided to all members.' },
      { cls:'highe', label:'Highly Effective', text:'Our board has completed a formal policy diet, reviewing all policies at least once per board member term and removing those outside the four governance categories.' },
    ]
  },
  {
    area: 3,
    text: 'How focused is the content of our public board meetings on governance-level work?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Public board meetings routinely include operational presentations, management approvals, and items that are superintendent — not board — work.' },
      { cls:'emerg', label:'Emerging',         text:'Our board is making progress separating board work from superintendent work, though meetings still include some operational content.' },
      { cls:'effec', label:'Effective',        text:'Our board consistently limits public meeting content to governance-level work and has confirmed this through formal self-evaluation.' },
      { cls:'highe', label:'Highly Effective', text:'Only board-appropriate work is discussed and acted upon in public meetings; our board invests 50%+ of meeting time in goal monitoring and quarterly affirms member conduct.' },
    ]
  },
  // ── Area 5: Communicate Results ──
  {
    area: 4,
    text: 'How efficient is our board\'s meeting structure (frequency, length, agenda discipline)?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board holds more than 5 public meetings per month, meetings regularly exceed 3 hours, or routine items are not placed on a consent agenda.' },
      { cls:'emerg', label:'Emerging',         text:'Our board uses a consent agenda for routine items, and members receive final voting materials at least 3 business days before meetings.' },
      { cls:'effec', label:'Effective',        text:'Our board holds 5 or fewer public meetings monthly, meetings rarely exceed 3 hours, agendas have 5 or fewer topics, and no last-minute edits are made within 3 business days.' },
      { cls:'highe', label:'Highly Effective', text:'Our board holds 3 or fewer public meetings monthly, meetings rarely exceed 2 hours, agendas have 3 or fewer topics, and materials arrive 7–14 days in advance.' },
    ]
  },
  {
    area: 4,
    text: 'How disciplined is our board about limiting agenda content to governance matters?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our meeting agendas include a wide mix of governance, management, and operational items with no clear discipline around what belongs at the board table.' },
      { cls:'emerg', label:'Emerging',         text:'Our board is working to limit agendas to governance-appropriate matters and has begun reducing the number of agenda topics.' },
      { cls:'effec', label:'Effective',        text:'Our board has removed policies outside the four governance categories, and agenda edits within 3 business days require a declared emergency.' },
      { cls:'highe', label:'Highly Effective', text:'Our agendas consistently contain 3 or fewer governance-level topics, all materials arrive well in advance, and meeting format transparently demonstrates our focus on student outcomes.' },
    ]
  },
  {
    area: 4,
    text: 'How actively does our board listen to and engage the community around vision and values?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board has not engaged in meaningful community listening about vision and values in the past 36 months.' },
      { cls:'emerg', label:'Emerging',         text:'Our board has received training on community vision/values listening and has begun engaging diverse stakeholders.' },
      { cls:'effec', label:'Effective',        text:'Our board regularly convenes diverse community stakeholders in structured listening sessions that directly inform our goals and guardrails.' },
      { cls:'highe', label:'Highly Effective', text:'Our goals and guardrails were adopted through an inclusive community process, and stakeholders can trace the direct line from their input to our board\'s adopted priorities.' },
    ]
  },
  {
    area: 4,
    text: 'How proactively does our board communicate goal progress and results to the community?',
    choices: [
      { cls:'ineff', label:'Ineffective',      text:'Our board does not proactively communicate goal progress or results to the community in systematic, accessible ways.' },
      { cls:'emerg', label:'Emerging',         text:'Our board makes governance decisions publicly and ensures community access to meeting materials, goals, and monitoring reports.' },
      { cls:'effec', label:'Effective',        text:'Our board publicly displays goal status and targets and regularly communicates progress through multiple accessible channels.' },
      { cls:'highe', label:'Highly Effective', text:'Our communication systems help stakeholders distinguish customer-service issues from owner issues and keep the community continuously informed of progress toward student outcome goals.' },
    ]
  },
];

// ── State ─────────────────────────────────────────
var answers = new Array(20).fill(-1);
var currentArea = 0;
var scores = {};

// ── Rendering ─────────────────────────────────────
function renderArea(areaIdx) {
  var area = AREAS[areaIdx];
  var areaQs = QUESTIONS.filter(function(q){ return q.area === areaIdx; });
  var firstQIdx = QUESTIONS.findIndex(function(q){ return q.area === areaIdx; });
  var html = '';
  html += '<div class="gotb-area-header"><h4>' + area.name + '</h4><div class="area-weight">Practice Area ' + (areaIdx+1) + ' of 5 &nbsp;·&nbsp; Up to ' + area.max + ' points</div></div>';
  areaQs.forEach(function(q, localIdx){
    var globalIdx = firstQIdx + localIdx;
    html += '<div class="gotb-question-card">';
    html += '<div class="q-number">Question ' + (globalIdx+1) + ' of 20</div>';
    html += '<div class="q-text">' + q.text + '</div>';
    html += '<div class="gotb-choices">';
    q.choices.forEach(function(c, val){
      var checked = (answers[globalIdx] === val) ? 'checked' : '';
      html += '<div class="gotb-choice ' + c.cls + '">';
      html += '<input type="radio" name="q' + globalIdx + '" id="q' + globalIdx + '_' + val + '" value="' + val + '" ' + checked + ' onchange="recordAnswer(' + globalIdx + ',' + val + ')">';
      html += '<label for="q' + globalIdx + '_' + val + '"><span class="level-name">' + c.label + '</span>' + c.text + '</label>';
      html += '</div>';
    });
    html += '</div></div>';
  });
  document.getElementById('questions-container').innerHTML = html;
  updateProgress();
  document.getElementById('btn-prev').style.display = (areaIdx === 0) ? 'none' : 'inline-block';
  document.getElementById('btn-next').textContent = (areaIdx === AREAS.length - 1) ? 'See My Score →' : 'Next →';
  document.getElementById('unanswered-msg').style.display = 'none';
  window.scrollTo(0, 0);
}

function updateProgress() {
  var answered = answers.filter(function(a){ return a >= 0; }).length;
  var pct = Math.round((answered / 20) * 100);
  document.getElementById('progress-bar').style.width = pct + '%';
  document.getElementById('progress-label').textContent = 'Question ' + answered + ' of 20 answered';
}

function recordAnswer(qIdx, val) {
  answers[qIdx] = val;
  updateProgress();
}

function startAssessment() {
  showStep('step-questions');
  renderArea(0);
}

function prevArea() {
  if (currentArea > 0) { currentArea--; renderArea(currentArea); }
}

function nextArea() {
  var firstIdx = QUESTIONS.findIndex(function(q){ return q.area === currentArea; });
  var areaQs = QUESTIONS.filter(function(q){ return q.area === currentArea; });
  var allAnswered = areaQs.every(function(_, i){ return answers[firstIdx + i] >= 0; });
  if (!allAnswered) { document.getElementById('unanswered-msg').style.display = 'inline'; return; }
  document.getElementById('unanswered-msg').style.display = 'none';
  if (currentArea < AREAS.length - 1) { currentArea++; renderArea(currentArea); }
  else { computeScores(); showGate(); }
}

// ── Scoring ────────────────────────────────────────
function computeScores() {
  scores = {};
  var total = 0;
  AREAS.forEach(function(area, areaIdx){
    var firstIdx = QUESTIONS.findIndex(function(q){ return q.area === areaIdx; });
    var areaQs = QUESTIONS.filter(function(q){ return q.area === areaIdx; });
    var rawSum = areaQs.reduce(function(sum, _, i){ return sum + answers[firstIdx + i]; }, 0);
    var maxRaw = areaQs.length * 3;
    var areaScore = Math.round((rawSum / maxRaw) * area.max * 10) / 10;
    scores[area.id] = areaScore;
    total += areaScore;
  });
  scores.total = Math.round(total);
}

function getRating(score) {
  if (score >= 80) return 'Highly Effective';
  if (score >= 70) return 'Effective';
  if (score >= 40) return 'Emerging';
  return 'Ineffective';
}

function getRatingClass(score) {
  if (score >= 80) return 'highe';
  if (score >= 70) return 'effec';
  if (score >= 40) return 'emerg';
  return 'ineff';
}

function getInterpretation(score, name) {
  var first = name ? name.split(' ')[0] : 'Your board';
  if (score >= 80) return '<strong>' + first + ', your board is operating at a high level.</strong> You\'re in the top tier — focused on student outcomes, monitoring progress rigorously, and governing with discipline. The work now is about sustaining quality and closing the remaining gaps.';
  if (score >= 70) return '<strong>' + first + ', your board is effective and has a solid foundation.</strong> There are specific areas where deeper focus will make a real difference in student outcomes. A certified coach can help your board close the gap to 80+ and sustain it.';
  if (score >= 40) return '<strong>' + first + ', your board has made a start.</strong> You\'re aware of effective governance principles, but consistent practice across all five areas is still developing. The gap to where you want to be is real — but so is the path forward with the right support.';
  return '<strong>' + first + ', your board has significant room to grow.</strong> The good news: boards that commit to this work and engage a certified coach typically move from this range to 60+ within a year. The framework gives you a clear roadmap — the question is whether your board is ready to commit.';
}

// ── Gate display ───────────────────────────────────
function showGate() {
  document.getElementById('gate-score-circle').textContent = scores.total;
  showStep('step-gate');
}

// ── Form submission ────────────────────────────────
function handleGateSubmit(e) {
  e.preventDefault();
  var name = document.getElementById('gate-name').value.trim();
  var district = document.getElementById('gate-district').value.trim();
  var email = document.getElementById('gate-email').value.trim();
  if (!name || !district || !email || !email.includes('@')) {
    document.getElementById('gate-error').style.display = 'block';
    document.getElementById('gate-error').textContent = 'Please fill in all fields with a valid email address.';
    return;
  }
  var btn = document.getElementById('gate-submit-btn');
  btn.disabled = true;
  btn.textContent = 'Sending…';
  document.getElementById('gate-error').style.display = 'none';
  showStep('step-sending');

  var rating = getRating(scores.total);
  fetch(API_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: name,
      district: district,
      email: email,
      total_score: scores.total,
      rating: rating,
      score_focus: scores.focus,
      score_priorities: scores.priorities,
      score_monitor: scores.monitor,
      score_align: scores.align,
      score_communicate: scores.communicate,
    })
  })
  .then(function(r){ return r.json(); })
  .then(function(){ showResults(name, district); })
  .catch(function(){
    // Show results even if the API call fails
    showResults(name, district);
  });
}

// ── Results display ────────────────────────────────
function showResults(name, district) {
  var rating = getRating(scores.total);
  var ratingCls = getRatingClass(scores.total);
  document.getElementById('results-headline').textContent = name + '\'s School Board Assessment';
  document.getElementById('results-intro').textContent = 'Results for ' + district;
  document.getElementById('result-total-score').textContent = scores.total;
  document.getElementById('result-rating').textContent = rating;
  document.getElementById('total-score-block').className = 'total-score-block ' + ratingCls;
  document.getElementById('gotb-interpretation').innerHTML = getInterpretation(scores.total, name);
  var barsHtml = '';
  AREAS.forEach(function(area){
    var areaScore = scores[area.id];
    var pct = Math.round((areaScore / area.max) * 100);
    barsHtml += '<div class="area-score-row">';
    barsHtml += '<div class="area-name"><span>' + area.name + '</span><span>' + areaScore + ' / ' + area.max + '</span></div>';
    barsHtml += '<div class="area-bar-bg"><div class="area-bar-fill" style="width:' + pct + '%;background:' + area.color + '"></div></div>';
    barsHtml += '</div>';
  });
  document.getElementById('area-scores-container').innerHTML = barsHtml;
  showStep('step-results');
}

function showStep(stepId) {
  document.querySelectorAll('.gotb-step').forEach(function(s){ s.classList.remove('active'); });
  document.getElementById(stepId).classList.add('active');
  window.scrollTo(0, 0);
}

})();
</script>
