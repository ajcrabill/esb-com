---
layout: base
title: "GOTB Index: Self Assessment"
description: "Take the free Great On Their Behalf Index: Self Assessment to get an approximate score for your school board's effectiveness. 20 questions, results emailed instantly."
summary: "GOTB Index: Self Assessment"
toplevel: Resources
---

<style>
#gotb-app { margin: 0 -15px; }
.gotb-step { display: none; }
.gotb-step.active { display: block; }

.gotb-intro { text-align: center; padding: 40px 20px; }
.gotb-intro h2 { font-size: 2rem; color: #2c3e50; margin-bottom: 16px; }
.gotb-intro p { font-size: 1.05rem; color: #555; max-width: 640px; margin: 0 auto 20px; }
.gotb-score-sample { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-bottom: 28px; }
.score-band { padding: 9px 18px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; }
.score-band.ineff { background: #f5cbcc; color: #7a0000; }
.score-band.emerg { background: #fce5cd; color: #7a3800; }
.score-band.effec { background: #d9ead3; color: #1a5c0a; }
.score-band.highe { background: #d0e2f3; color: #0a2d5c; }

/* Comparison box */
.gotb-comparison { display: grid; grid-template-columns: 1fr 1fr; gap: 0; border: 1px solid #ddd; border-radius: 10px; overflow: hidden; margin: 0 auto 32px; max-width: 680px; }
@media (max-width: 600px) { .gotb-comparison { grid-template-columns: 1fr; } }
.gotb-comparison-col { padding: 20px 22px; }
.gotb-comparison-col.self-col { background: #eaf3fb; border-right: 1px solid #ddd; }
.gotb-comparison-col.cert-col { background: #f9f9f9; }
@media (max-width: 600px) { .gotb-comparison-col.self-col { border-right: none; border-bottom: 1px solid #ddd; } }
.gotb-comparison-col .col-badge { display: inline-block; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; padding: 3px 9px; border-radius: 20px; margin-bottom: 10px; }
.self-col .col-badge { background: #2c6fad; color: #fff; }
.cert-col .col-badge { background: #555; color: #fff; }
.gotb-comparison-col h5 { margin: 0 0 8px; font-size: 1rem; color: #2c3e50; }
.gotb-comparison-col ul { margin: 0; padding: 0 0 0 18px; font-size: 0.87rem; color: #555; line-height: 1.7; }
.gotb-comparison-col .col-note { font-size: 0.8rem; color: #888; margin-top: 10px; font-style: italic; }

.gotb-progress-wrap { background: #eee; border-radius: 10px; height: 8px; margin-bottom: 8px; }
.gotb-progress-bar { background: linear-gradient(90deg, #4a86c8, #2c6fad); height: 8px; border-radius: 10px; transition: width 0.4s ease; }
.gotb-progress-label { font-size: 0.82rem; color: #888; text-align: right; margin-bottom: 20px; }

.gotb-area-header { background: #2c3e50; color: #fff; padding: 16px 20px; border-radius: 8px 8px 0 0; }
.gotb-area-header h4 { margin: 0; font-size: 1.1rem; }
.gotb-area-header .area-weight { font-size: 0.82rem; opacity: 0.75; margin-top: 2px; }

.gotb-question-card { border: 1px solid #ddd; padding: 20px; background: #fff; border-top: none; }
.gotb-question-card:last-of-type { border-radius: 0 0 8px 8px; margin-bottom: 24px; }
.gotb-question-card .q-number { font-size: 0.78rem; text-transform: uppercase; letter-spacing: .05em; color: #999; margin-bottom: 4px; }
.gotb-question-card .q-text { font-size: 1rem; font-weight: 600; color: #2c3e50; margin-bottom: 14px; }

.gotb-choices { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
@media (max-width: 600px) { .gotb-choices { grid-template-columns: 1fr; } }

.gotb-choice { position: relative; cursor: pointer; }
.gotb-choice input[type="radio"] { position: absolute; opacity: 0; width: 0; height: 0; }
.gotb-choice label { display: block; padding: 10px 14px; border-radius: 6px; cursor: pointer; border: 2px solid transparent; transition: all .2s; font-size: .87rem; line-height: 1.4; }
.gotb-choice label .level-name { font-weight: 700; font-size: .78rem; text-transform: uppercase; letter-spacing: .04em; display: block; margin-bottom: 3px; }
.gotb-choice.ineff label { background: #f5cbcc; border-color: #e8a0a1; }
.gotb-choice.emerg label { background: #fce5cd; border-color: #f5c8a0; }
.gotb-choice.effec label { background: #d9ead3; border-color: #b2d4a7; }
.gotb-choice.highe label { background: #d0e2f3; border-color: #a2c4e3; }
.gotb-choice input:checked + label { box-shadow: 0 0 0 2px rgba(44,111,173,.35); }
.gotb-choice.ineff input:checked + label { border-color: #c00; }
.gotb-choice.emerg input:checked + label { border-color: #b85c00; }
.gotb-choice.effec input:checked + label { border-color: #2a7d00; }
.gotb-choice.highe input:checked + label { border-color: #0a47a0; }

.gotb-nav { display: flex; justify-content: space-between; align-items: center; margin: 8px 0 32px; }
.btn-gotb-primary { background: #2c6fad; color: #fff; border: none; padding: 12px 28px; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer; }
.btn-gotb-primary:hover { background: #245d91; }
.btn-gotb-secondary { background: transparent; color: #2c6fad; border: 2px solid #2c6fad; padding: 10px 24px; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer; }
.btn-gotb-secondary:hover { background: #2c6fad; color: #fff; }
.gotb-unanswered-msg { color: #c00; font-size: .88rem; display: none; }

.gotb-gate { max-width: 520px; margin: 0 auto; }
.gotb-gate h3 { font-size: 1.5rem; color: #2c3e50; margin-bottom: 8px; }
.gotb-gate .gate-sub { color: #666; margin-bottom: 24px; font-size: .95rem; }
.gotb-gate .score-preview { text-align: center; margin: 20px 0 28px; }
.score-circle { display: inline-block; width: 110px; height: 110px; border-radius: 50%; background: #2c3e50; color: #fff; line-height: 1.1; font-size: 2.4rem; font-weight: 700; text-align: center; padding-top: 24px; box-sizing: border-box; }
.gotb-gate .score-preview .score-label { font-size: .85rem; color: #888; margin-top: 8px; }
.gotb-gate label { font-weight: 600; font-size: .9rem; color: #444; display: block; margin-bottom: 4px; margin-top: 14px; }
.gotb-gate input { width: 100%; padding: 10px 14px; border: 1px solid #ccc; border-radius: 6px; font-size: .95rem; box-sizing: border-box; }
.gotb-gate input:focus { outline: none; border-color: #2c6fad; box-shadow: 0 0 0 3px rgba(44,111,173,.15); }
.gate-submit-row { margin-top: 24px; text-align: center; }
.gate-privacy { font-size: .78rem; color: #999; margin-top: 10px; }
.btn-gotb-submit { background: #e8a000; color: #fff; border: none; padding: 14px 36px; border-radius: 6px; font-size: 1.05rem; font-weight: 700; cursor: pointer; width: 100%; }
.btn-gotb-submit:hover { background: #cc8c00; }
.btn-gotb-submit:disabled { background: #ccc; cursor: default; }
.gate-error { color: #c00; font-size: .88rem; margin-top: 8px; display: none; }

.gotb-results { max-width: 680px; margin: 0 auto; }
.gotb-results h3 { font-size: 1.6rem; color: #2c3e50; margin-bottom: 6px; }
.gotb-results .results-intro { color: #555; margin-bottom: 28px; }
.total-score-block { text-align: center; padding: 28px; border-radius: 10px; margin-bottom: 28px; }
.total-score-block .big-score { font-size: 4rem; font-weight: 800; line-height: 1; }
.total-score-block .score-out-of { font-size: 1rem; opacity: .75; }
.total-score-block .score-label { font-size: 1.1rem; font-weight: 600; margin-top: 6px; }
.total-score-block.ineff { background: #f5cbcc; color: #7a0000; }
.total-score-block.emerg { background: #fce5cd; color: #7a3800; }
.total-score-block.effec { background: #d9ead3; color: #1a5c0a; }
.total-score-block.highe { background: #d0e2f3; color: #0a2d5c; }

.area-scores { margin-bottom: 28px; }
.area-score-row { margin-bottom: 14px; }
.area-score-row .area-name { font-weight: 600; font-size: .92rem; color: #2c3e50; display: flex; justify-content: space-between; margin-bottom: 4px; }
.area-bar-bg { background: #eee; border-radius: 6px; height: 18px; overflow: hidden; }
.area-bar-fill { height: 18px; border-radius: 6px; transition: width .8s ease; }

.gotb-interpretation { border-left: 4px solid #2c6fad; padding: 16px 20px; background: #f4f8fc; border-radius: 0 8px 8px 0; margin-bottom: 24px; font-size: .93rem; color: #333; }
.gotb-cta-block { background: #2c3e50; color: #fff; padding: 28px; border-radius: 10px; text-align: center; margin-bottom: 12px; }
.gotb-cta-block h4 { color: #fff; margin-bottom: 10px; }
.gotb-cta-block p { color: #ccc; margin-bottom: 18px; font-size: .92rem; }
.btn-gotb-cta { background: #e8a000; color: #fff; border: none; padding: 12px 28px; border-radius: 6px; font-size: 1rem; font-weight: 700; text-decoration: none; display: inline-block; }
.btn-gotb-cta:hover { background: #cc8c00; color: #fff; text-decoration: none; }

.gotb-sending { text-align: center; padding: 40px 20px; color: #555; }
.gotb-spinner { border: 3px solid #eee; border-top: 3px solid #2c6fad; border-radius: 50%; width: 40px; height: 40px; animation: gotb-spin .8s linear infinite; margin: 0 auto 16px; }
@keyframes gotb-spin { to { transform: rotate(360deg); } }
</style>

<div id="gotb-app">

  <!-- ── STEP: INTRO ── -->
  <div id="step-intro" class="gotb-step active">
    <div class="gotb-intro">
      <p style="font-size:.85rem;text-transform:uppercase;letter-spacing:.08em;color:#2c6fad;margin-bottom:8px;font-weight:600;">Free Self-Assessment</p>
      <h2>Great On Their Behalf Index:<br><span style="font-size:1.4rem;font-weight:500;color:#555;">Self Assessment</span></h2>
      <p>Answer 20 questions to get an approximate 0–100 score for your school board's effectiveness across five practice areas. Results are emailed to you instantly — no purchase required.</p>

      <div class="gotb-score-sample">
        <div class="score-band ineff">0–39 · Ineffective</div>
        <div class="score-band emerg">40–69 · Emerging</div>
        <div class="score-band effec">70–79 · Effective</div>
        <div class="score-band highe">80–100 · Highly Effective</div>
      </div>

      <button id="btn-start" class="btn-gotb-primary" style="font-size:1.1rem;padding:14px 40px;">Start the Assessment &rarr;</button>
      <p style="font-size:.85rem;color:#aaa;margin-top:12px;">Takes about 5–8 minutes</p>
    </div>

    <!-- What it covers -->
    <div style="background:#f9f9f9;border-radius:10px;padding:22px 28px;max-width:680px;margin:0 auto 20px;">
      <h5 style="margin:0 0 12px;color:#2c3e50;">What This Assessment Covers</h5>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <div style="font-size:.87rem;color:#555;"><strong style="color:#2c3e50;">Focus Mindset</strong><br>Training, self-evaluation &amp; outcomes-clarity</div>
        <div style="font-size:.87rem;color:#555;"><strong style="color:#2c3e50;">Clarify Priorities</strong><br>Goals, guardrails &amp; community voice</div>
        <div style="font-size:.87rem;color:#555;"><strong style="color:#2c3e50;">Monitor Progress</strong><br>Monitoring calendar, quality &amp; data</div>
        <div style="font-size:.87rem;color:#555;"><strong style="color:#2c3e50;">Align Resources</strong><br>Role clarity, evaluation &amp; governance</div>
        <div style="font-size:.87rem;color:#555;"><strong style="color:#2c3e50;">Communicate Results</strong><br>Meeting structure &amp; community engagement</div>
      </div>
    </div>

    <!-- Self Assessment vs. Certified Assessment -->
    <div style="max-width:680px;margin:0 auto 28px;">
      <h5 style="margin:0 0 12px;color:#2c3e50;text-align:center;">Two Versions of the GOTB Index</h5>
      <div class="gotb-comparison">
        <div class="gotb-comparison-col self-col">
          <span class="col-badge">You are here</span>
          <h5>Self Assessment</h5>
          <ul>
            <li>20 questions, self-administered</li>
            <li>Completed by an individual board member</li>
            <li>Provides an approximate score and area breakdown</li>
            <li>Free — results emailed instantly</li>
            <li>A useful starting point for self-reflection</li>
          </ul>
          <p class="col-note">Scores are based on your own perceptions and may differ from the full board's perspective.</p>
        </div>
        <div class="gotb-comparison-col cert-col">
          <span class="col-badge">Full instrument</span>
          <h5>Certified Assessment</h5>
          <ul>
            <li>Psychometrically validated instrument</li>
            <li>Administered by a certified Great On Their Behalf Practitioner</li>
            <li>Completed by the full governing team</li>
            <li>Produces a validated, defensible board score</li>
            <li>Foundation for a formal improvement plan</li>
          </ul>
          <p class="col-note">Required for official GOTB certification and coaching engagements.</p>
        </div>
      </div>
    </div>

  </div><!-- /step-intro -->

  <!-- ── STEP: QUESTIONS ── -->
  <div id="step-questions" class="gotb-step">
    <div class="gotb-progress-wrap"><div class="gotb-progress-bar" id="progress-bar" style="width:0%"></div></div>
    <div class="gotb-progress-label" id="progress-label">0 of 20 answered</div>
    <div id="questions-container"></div>
    <div class="gotb-nav">
      <button class="btn-gotb-secondary" id="btn-prev" style="display:none">&#8592; Previous</button>
      <span class="gotb-unanswered-msg" id="unanswered-msg">Please answer all questions before continuing.</span>
      <button class="btn-gotb-primary" id="btn-next">Next &#8594;</button>
    </div>
  </div>

  <!-- ── STEP: SENDING ── -->
  <div id="step-sending" class="gotb-step">
    <div class="gotb-sending">
      <div class="gotb-spinner"></div>
      <p>Calculating your score and sending results&hellip;</p>
    </div>
  </div>

  <!-- ── STEP: GATE ── -->
  <div id="step-gate" class="gotb-step">
    <div class="gotb-gate">
      <h3>You've Completed the Assessment!</h3>
      <p class="gate-sub">Enter your information below to receive your full results by email and see your score breakdown on screen.</p>
      <div class="score-preview">
        <div class="score-circle" id="gate-score-circle">—</div>
        <div class="score-label">Your score is ready</div>
      </div>
      <form id="gate-form" novalidate>
        <label for="gate-name">Your Name</label>
        <input type="text" id="gate-name" placeholder="First and last name" required>
        <label for="gate-district">School District</label>
        <input type="text" id="gate-district" placeholder="e.g. Lincoln Unified School District" required>
        <label for="gate-email">Email Address</label>
        <input type="email" id="gate-email" placeholder="you@example.com" required>
        <div class="gate-submit-row">
          <button type="submit" class="btn-gotb-submit" id="gate-submit-btn">Email Me My Results &#8594;</button>
          <div class="gate-error" id="gate-error"></div>
          <p class="gate-privacy">We respect your privacy. Your information will only be used to send your results and relevant school board resources.</p>
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
        <p>Most boards go from their starting score to 80+ in about two years — but only with a certified Great On Their Behalf Practitioner. It's not about working harder; it's about working differently.</p>
        <a href="/consultation" class="btn-gotb-cta">Schedule a Free Consultation</a>
      </div>
      <p style="font-size:.82rem;color:#aaa;text-align:center;margin-top:16px;">Results have been sent to the email address you provided. Check your spam folder if you don't see them within a few minutes.</p>
    </div>
  </div>

</div><!-- #gotb-app -->

<script>
var GOTB = (function() {

  var API = 'https://esbcloud.taild49f53.ts.net:8443/gotb/submit';

  var AREAS = [
    { id: 'focus',       name: 'Focus Mindset',       max: 10, color: '#4a86c8' },
    { id: 'priorities',  name: 'Clarify Priorities',  max: 35, color: '#e07b00' },
    { id: 'monitor',     name: 'Monitor Progress',     max: 30, color: '#3a9c5b' },
    { id: 'align',       name: 'Align Resources',      max: 20, color: '#8e44ad' },
    { id: 'communicate', name: 'Communicate Results',  max:  5, color: '#2c3e50' },
  ];

  var QUESTIONS = [
    // Area 1: Focus Mindset
    { area:0, text:'How has our board engaged with school board governance training?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board has received no training on effective school board governance in the past 36 months.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has received training on an effective school board framework within the past 36 months.'},
      {cls:'effec',label:'Effective',       text:'Board members have both received training and helped facilitate at least one governance training session in the past 12 months.'},
      {cls:'highe',label:'Highly Effective',text:'Our training program includes students presenting, new members train before their first vote, and framework training is ongoing.'},
    ]},
    { area:0, text:'How consistently does our board conduct formal self-evaluations?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board has not conducted a formal self-evaluation in the past 12 months.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has self-evaluations scheduled on a regular calendar (quarterly or annually timed near the superintendent evaluation).'},
      {cls:'effec',label:'Effective',       text:'Our board completed a self-evaluation within the past 12 months using this or an aligned instrument and voted to adopt the results.'},
      {cls:'highe',label:'Highly Effective',text:'Our self-evaluation was completed within the required timeframe AND board members shared examples of when their behaviors hindered student goal achievement.'},
    ]},
    { area:0, text:'How clearly can our board distinguish adult inputs from student outcomes?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'I often cannot clearly tell the difference between adult inputs (what adults do or spend) and student outcomes (what students achieve).'},
      {cls:'emerg',label:'Emerging',        text:'I can distinguish adult inputs from student outcomes, though our board discussions still frequently center on inputs.'},
      {cls:'effec',label:'Effective',       text:'I consistently distinguish inputs from outcomes and regularly redirect board conversations to focus on student outcomes.'},
      {cls:'highe',label:'Highly Effective',text:'Our board reliably focuses on student outcomes, and our tracked meeting-time data confirms this pattern meeting after meeting.'},
    ]},
    { area:0, text:'How does our board track and analyze how its meeting time is spent?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board does not track how meeting time is spent or what percentage focuses on student outcomes.'},
      {cls:'emerg',label:'Emerging',        text:'Our board tracks and reports quarterly on the percentage of meeting time focused on student outcomes.'},
      {cls:'effec',label:'Effective',       text:'Our board tracks meeting time AND annually reports the cost of staff governance time during our self-evaluation.'},
      {cls:'highe',label:'Highly Effective',text:'Our tracking data shows consistent year-over-year improvement in the percentage of meeting time devoted to student outcome discussions.'},
    ]},
    // Area 2: Clarify Priorities
    { area:1, text:'How well-defined are our board\'s student outcome goals?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board has no adopted student outcome goals, or our goals are vague, input-focused, or not SMART.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has adopted 1–5 SMART goals focused on student outcomes, developed with input from students, parents, staff, and community members.'},
      {cls:'effec',label:'Effective',       text:'Our goals are SMART, and the superintendent has adopted 1–3 predictive, influenceable interim goals per board goal — all focused on student outcomes (not adult inputs).'},
      {cls:'highe',label:'Highly Effective',text:'All goals span 3–5 years with yearly targets; all interim goals span 1–3 years; and every board member can recite all goals and current status from memory.'},
    ]},
    { area:1, text:'How inclusive and community-grounded was our goal development process?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our goals were created without meaningful community input, root cause analysis, or comprehensive needs assessment.'},
      {cls:'emerg',label:'Emerging',        text:'Our goals were developed with diverse community stakeholders and posted for public comment before adoption.'},
      {cls:'effec',label:'Effective',       text:'Our goal development generated genuine community ownership, and all board members agree the goals require significant organizational behavior change.'},
      {cls:'highe',label:'Highly Effective',text:'The inclusive process produced goals that authentically represent community voice and present a genuine stretch that challenges our entire organization.'},
    ]},
    { area:1, text:'Has our board adopted guardrails defining what approaches the superintendent may NOT use in pursuing goals?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board has not adopted guardrails — statements describing a single operational approach the superintendent may not use.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has adopted 1–5 guardrails grounded in community values, each describing a single approach the superintendent may not use.'},
      {cls:'effec',label:'Effective',       text:'Our board has guardrails, and the superintendent has adopted 1–3 interim guardrails per guardrail with annual targets; all focus on outcomes, not inputs.'},
      {cls:'highe',label:'Highly Effective',text:'All guardrails span 3–5 years, were adopted through an inclusive process, and our board has also adopted guardrails on its own behavior evaluated quarterly.'},
    ]},
    { area:1, text:'How well-structured are our annual interim targets and milestones?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our goals do not include clear annual targets or interim milestones that can be tracked and updated throughout the year.'},
      {cls:'emerg',label:'Emerging',        text:'Our goals include identified annual targets and yearly ending points through the goal deadline.'},
      {cls:'effec',label:'Effective',       text:'Interim goal ending points are established for each year through the deadline, and interim goal status can be updated multiple times per year.'},
      {cls:'highe',label:'Highly Effective',text:'All targets are set, our board and superintendent agree achieving them requires major organizational change, and the targets represent a genuine institutional stretch.'},
    ]},
    // Area 3: Monitor Progress
    { area:2, text:'Does our board have an adopted monitoring calendar that governs how we track goal progress?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board has no adopted monitoring calendar, or goals are not scheduled for monitoring at least 4 times per year.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has a monitoring calendar developed with superintendent input — no more than 2 goals per month, every goal monitored at least 4 times annually.'},
      {cls:'effec',label:'Effective',       text:'Our board formally adopted the monitoring calendar, and goals/guardrails/calendar have been modified no more than once during the current goal span.'},
      {cls:'highe',label:'Highly Effective',text:'Our monitoring calendar is stable and adopted, and our board invests 50%+ of total monthly public meeting minutes in effective goal monitoring.'},
    ]},
    { area:2, text:'How would you rate the quality of our board\'s monitoring conversations?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'During monitoring, board members frequently ask operational questions or make comments rather than using data to examine student results.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has received training on effective monitoring and has completed at least one practice monitoring session.'},
      {cls:'effec',label:'Effective',       text:'Our board demonstrated effective monitoring (80%+ quality score) during each monitoring conversation in the past 12 months.'},
      {cls:'highe',label:'Highly Effective',text:'Our board consistently achieves highly effective monitoring (90%+), with strategy-focused, measure-referenced, open-ended, results-oriented, time-bound questions.'},
    ]},
    { area:2, text:'How does our board use monitoring reports and data from the superintendent?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board does not receive formal monitoring reports on a calendar, or our school system achieved no interim goals in the past 12 months.'},
      {cls:'emerg',label:'Emerging',        text:'Our board receives monitoring reports per the calendar, and the superintendent\'s team has been trained on creating effective monitoring reports.'},
      {cls:'effec',label:'Effective',       text:'Our board publicly displays goal status and targets in our regular meeting room and provides time recognizing student and staff accomplishments toward goals.'},
      {cls:'highe',label:'Highly Effective',text:'Our school system achieved at least half of interim goals in the past 12 months, and monitoring reports are received per calendar with full data.'},
    ]},
    { area:2, text:'What share of our public board meeting time is devoted to effective goal monitoring?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Most of our meeting time goes to routine approvals, operational presentations, and non-monitoring topics — goal monitoring is a small fraction.'},
      {cls:'emerg',label:'Emerging',        text:'Our board monitors goals at every scheduled session, though monitoring may still represent less than a third of total meeting time.'},
      {cls:'effec',label:'Effective',       text:'Our board consistently prioritizes goal monitoring in public meetings and tracks meeting time use to continually improve.'},
      {cls:'highe',label:'Highly Effective',text:'Our board has data showing it invests 50% or more of total monthly public meeting minutes in effective goal monitoring.'},
    ]},
    // Area 4: Align Resources
    { area:3, text:'How clearly does our board maintain the distinction between board governance and superintendent management?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Board members sometimes give operational advice to staff, vote on superintendent implementation plans, or serve on operational committees outside proper protocols.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has discussed the governance vs. management distinction, and members generally agree committees advise the board — not staff.'},
      {cls:'effec',label:'Effective',       text:'Our board has an Ethics & Conflicts of Interest Statement signed by all current members, committing to no operational advice to staff and recusal from conflicts.'},
      {cls:'highe',label:'Highly Effective',text:'Our board unanimously affirms annually that all members adhered to governing policies, honored ethical boundaries, and gave no operational advice during the past year.'},
    ]},
    { area:3, text:'How is our superintendent\'s evaluation structured?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our superintendent evaluation includes criteria beyond board goals and guardrails — such as personality traits, relationships, or non-goal accomplishments.'},
      {cls:'emerg',label:'Emerging',        text:'Our superintendent evaluation is based solely on goals, guardrails, and interim goals/guardrails.'},
      {cls:'effec',label:'Effective',       text:'Our superintendent has never gone more than 12 months without a formal evaluation, and evaluations are completed on schedule.'},
      {cls:'highe',label:'Highly Effective',text:'Our annual budget is only approved after a deliberate determination that resources are prioritized toward board goals; superintendent evaluation is goals-only and on time.'},
    ]},
    { area:3, text:'How robust are our board\'s governance operating procedures and delegation policies?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board lacks adopted governance operating procedures or delegation policies, or has members with undisclosed conflicts of interest.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has adopted governance operating procedures, and the superintendent provides implementation plans without requiring board approval (except where legally mandated).'},
      {cls:'effec',label:'Effective',       text:'Our board has a policy requiring information given to one member to be provided to all members.'},
      {cls:'highe',label:'Highly Effective',text:'Our board has completed a formal policy diet, reviewing all policies at least once per board member term and removing those outside the four governance categories.'},
    ]},
    { area:3, text:'How focused is the content of our public board meetings on governance-level work?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Public board meetings routinely include operational presentations, management approvals, and items that are superintendent — not board — work.'},
      {cls:'emerg',label:'Emerging',        text:'Our board is making progress separating board work from superintendent work, though meetings still include some operational content.'},
      {cls:'effec',label:'Effective',       text:'Our board consistently limits public meeting content to governance-level work and has confirmed this through formal self-evaluation.'},
      {cls:'highe',label:'Highly Effective',text:'Only board-appropriate work is discussed and acted upon in public meetings; our board invests 50%+ of meeting time in goal monitoring and quarterly affirms member conduct.'},
    ]},
    // Area 5: Communicate Results
    { area:4, text:'How efficient is our board\'s meeting structure (frequency, length, agenda discipline)?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board holds more than 5 public meetings per month, meetings regularly exceed 3 hours, or routine items are not placed on a consent agenda.'},
      {cls:'emerg',label:'Emerging',        text:'Our board uses a consent agenda for routine items, and members receive final voting materials at least 3 business days before meetings.'},
      {cls:'effec',label:'Effective',       text:'Our board holds 5 or fewer public meetings monthly, meetings rarely exceed 3 hours, agendas have 5 or fewer topics, and no last-minute edits within 3 business days.'},
      {cls:'highe',label:'Highly Effective',text:'Our board holds 3 or fewer public meetings monthly, meetings rarely exceed 2 hours, agendas have 3 or fewer topics, and materials arrive 7–14 days in advance.'},
    ]},
    { area:4, text:'How disciplined is our board about limiting agenda content to governance matters?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our meeting agendas include a wide mix of governance, management, and operational items with no clear discipline around what belongs at the board table.'},
      {cls:'emerg',label:'Emerging',        text:'Our board is working to limit agendas to governance-appropriate matters and has begun reducing the number of agenda topics.'},
      {cls:'effec',label:'Effective',       text:'Our board has removed policies outside the four governance categories, and agenda edits within 3 business days require a declared emergency.'},
      {cls:'highe',label:'Highly Effective',text:'Our agendas consistently contain 3 or fewer governance-level topics, all materials arrive well in advance, and meeting format transparently demonstrates our focus on student outcomes.'},
    ]},
    { area:4, text:'How actively does our board listen to and engage the community around vision and values?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board has not engaged in meaningful community listening about vision and values in the past 36 months.'},
      {cls:'emerg',label:'Emerging',        text:'Our board has received training on community vision/values listening and has begun engaging diverse stakeholders.'},
      {cls:'effec',label:'Effective',       text:'Our board regularly convenes diverse community stakeholders in structured listening sessions that directly inform our goals and guardrails.'},
      {cls:'highe',label:'Highly Effective',text:'Our goals and guardrails were adopted through an inclusive community process, and stakeholders can trace the direct line from their input to our adopted priorities.'},
    ]},
    { area:4, text:'How proactively does our board communicate goal progress and results to the community?', choices:[
      {cls:'ineff',label:'Ineffective',     text:'Our board does not proactively communicate goal progress or results to the community in systematic, accessible ways.'},
      {cls:'emerg',label:'Emerging',        text:'Our board makes governance decisions publicly and ensures community access to meeting materials, goals, and monitoring reports.'},
      {cls:'effec',label:'Effective',       text:'Our board publicly displays goal status and targets and regularly communicates progress through multiple accessible channels.'},
      {cls:'highe',label:'Highly Effective',text:'Our communication systems help stakeholders distinguish customer-service issues from owner issues and keep the community continuously informed of progress toward student outcome goals.'},
    ]},
  ];

  var answers = new Array(20).fill(-1);
  var currentArea = 0;
  var scores = {};

  // ── Helpers ──────────────────────────────────────
  function showStep(id) {
    document.querySelectorAll('.gotb-step').forEach(function(s){ s.classList.remove('active'); });
    document.getElementById(id).classList.add('active');
    window.scrollTo(0,0);
  }

  function getRating(s) {
    if (s>=80) return 'Highly Effective';
    if (s>=70) return 'Effective';
    if (s>=40) return 'Emerging';
    return 'Ineffective';
  }

  function getRatingCls(s) {
    if (s>=80) return 'highe';
    if (s>=70) return 'effec';
    if (s>=40) return 'emerg';
    return 'ineff';
  }

  function getInterpretation(s, name) {
    var first = (name||'Your board').split(' ')[0];
    if (s>=80) return '<strong>'+first+', your board is operating at a high level.</strong> You\'re in the top tier — focused on student outcomes, monitoring progress rigorously, and governing with discipline. The work now is sustaining quality and closing the remaining gaps.';
    if (s>=70) return '<strong>'+first+', your board is effective and has a solid foundation.</strong> There are specific areas where deeper focus will make a real difference. A certified Great On Their Behalf Practitioner can help your board push toward 80+ and sustain it.';
    if (s>=40) return '<strong>'+first+', your board has made a start.</strong> You\'re aware of effective governance principles, but consistent practice across all five areas is still developing. The gap is real — but so is the path forward with the right support.';
    return '<strong>'+first+', your board has significant room to grow.</strong> Boards that commit to this work and engage a certified practitioner typically move from this range to 60+ within a year. The framework gives you a clear roadmap — the question is whether your board is ready to commit.';
  }

  // ── Questions rendering ───────────────────────────
  function renderArea(idx) {
    var area = AREAS[idx];
    var areaQs = [], firstIdx = -1;
    QUESTIONS.forEach(function(q,i){ if(q.area===idx){ if(firstIdx<0) firstIdx=i; areaQs.push({q:q,i:i}); } });

    var html = '<div class="gotb-area-header"><h4>'+area.name+'</h4>'
      +'<div class="area-weight">Practice Area '+(idx+1)+' of 5 · Up to '+area.max+' points</div></div>';

    areaQs.forEach(function(item){
      var q=item.q, gi=item.i;
      html += '<div class="gotb-question-card">'
        +'<div class="q-number">Question '+(gi+1)+' of 20</div>'
        +'<div class="q-text">'+q.text+'</div>'
        +'<div class="gotb-choices">';
      q.choices.forEach(function(c,val){
        var chk = answers[gi]===val ? 'checked' : '';
        html += '<div class="gotb-choice '+c.cls+'">'
          +'<input type="radio" name="q'+gi+'" id="q'+gi+'_'+val+'" value="'+val+'" '+chk+'>'
          +'<label for="q'+gi+'_'+val+'"><span class="level-name">'+c.label+'</span>'+c.text+'</label>'
          +'</div>';
      });
      html += '</div></div>';
    });

    document.getElementById('questions-container').innerHTML = html;

    // Attach change handlers after render
    areaQs.forEach(function(item){
      var gi = item.i;
      for(var v=0;v<4;v++){
        (function(gIdx,val){
          var el = document.getElementById('q'+gIdx+'_'+val);
          if(el) el.addEventListener('change', function(){ recordAnswer(gIdx,val); });
        })(gi,v);
      }
    });

    updateProgress();
    document.getElementById('btn-prev').style.display = idx===0 ? 'none' : 'inline-block';
    document.getElementById('btn-next').textContent = idx===AREAS.length-1 ? 'See My Score →' : 'Next →';
    document.getElementById('unanswered-msg').style.display = 'none';
    window.scrollTo(0,0);
  }

  function updateProgress() {
    var n = answers.filter(function(a){ return a>=0; }).length;
    document.getElementById('progress-bar').style.width = Math.round(n/20*100)+'%';
    document.getElementById('progress-label').textContent = n+' of 20 answered';
  }

  function recordAnswer(gi, val) {
    answers[gi] = val;
    updateProgress();
  }

  // ── Scoring ───────────────────────────────────────
  function computeScores() {
    var total = 0;
    scores = {};
    AREAS.forEach(function(area, ai){
      var areaQs = QUESTIONS.map(function(q,i){ return {q:q,i:i}; }).filter(function(x){ return x.q.area===ai; });
      var raw = areaQs.reduce(function(s,x){ return s+answers[x.i]; }, 0);
      var aScore = Math.round(raw/(areaQs.length*3)*area.max*10)/10;
      scores[area.id] = aScore;
      total += aScore;
    });
    scores.total = Math.round(total);
  }

  // ── Navigation ────────────────────────────────────
  function startAssessment() {
    showStep('step-questions');
    renderArea(0);
  }

  function prevArea() {
    if(currentArea>0){ currentArea--; renderArea(currentArea); }
  }

  function nextArea() {
    var areaQs = QUESTIONS.map(function(q,i){return{q:q,i:i};}).filter(function(x){return x.q.area===currentArea;});
    var allDone = areaQs.every(function(x){ return answers[x.i]>=0; });
    if(!allDone){ document.getElementById('unanswered-msg').style.display='inline'; return; }
    document.getElementById('unanswered-msg').style.display='none';
    if(currentArea<AREAS.length-1){ currentArea++; renderArea(currentArea); }
    else { computeScores(); showGate(); }
  }

  function showGate() {
    document.getElementById('gate-score-circle').textContent = scores.total;
    showStep('step-gate');
  }

  // ── Submission ────────────────────────────────────
  function handleGateSubmit(e) {
    e.preventDefault();
    var name     = document.getElementById('gate-name').value.trim();
    var district = document.getElementById('gate-district').value.trim();
    var email    = document.getElementById('gate-email').value.trim();
    var errEl    = document.getElementById('gate-error');

    if(!name||!district||!email||!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)){
      errEl.textContent = 'Please fill in all fields with a valid email address.';
      errEl.style.display = 'block';
      return;
    }
    errEl.style.display = 'none';

    var btn = document.getElementById('gate-submit-btn');
    btn.disabled = true;
    btn.textContent = 'Sending…';
    showStep('step-sending');

    fetch(API, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
        name: name, district: district, email: email,
        total_score: scores.total, rating: getRating(scores.total),
        score_focus: scores.focus, score_priorities: scores.priorities,
        score_monitor: scores.monitor, score_align: scores.align,
        score_communicate: scores.communicate,
      })
    })
    .then(function(r){ return r.json(); })
    .catch(function(){ return {}; })
    .then(function(){ showResults(name, district); });
  }

  // ── Results display ───────────────────────────────
  function showResults(name, district) {
    var s = scores.total;
    var cls = getRatingCls(s);
    document.getElementById('results-headline').textContent = name+"'s School Board Assessment";
    document.getElementById('results-intro').textContent = 'Results for '+district;
    document.getElementById('result-total-score').textContent = s;
    document.getElementById('result-rating').textContent = getRating(s);
    document.getElementById('total-score-block').className = 'total-score-block '+cls;
    document.getElementById('gotb-interpretation').innerHTML = getInterpretation(s, name);

    var html = '';
    AREAS.forEach(function(area){
      var aScore = scores[area.id];
      var pct = Math.round(aScore/area.max*100);
      html += '<div class="area-score-row">'
        +'<div class="area-name"><span>'+area.name+'</span><span>'+aScore+' / '+area.max+'</span></div>'
        +'<div class="area-bar-bg"><div class="area-bar-fill" style="width:'+pct+'%;background:'+area.color+'"></div></div>'
        +'</div>';
    });
    document.getElementById('area-scores-container').innerHTML = html;
    showStep('step-results');
  }

  // ── Wire up events after DOM ready ───────────────
  document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('btn-start').addEventListener('click', startAssessment);
    document.getElementById('btn-prev').addEventListener('click', prevArea);
    document.getElementById('btn-next').addEventListener('click', nextArea);
    document.getElementById('gate-form').addEventListener('submit', handleGateSubmit);
  });

  return { startAssessment: startAssessment };
})();
</script>
