---
layout: base
title: "Crisis Communications One-Pager Template"
summary: "Printable crisis communications template for school boards facing a governance crisis"
toplevel: Resources
toplevellink: /resources
---

<style>
  h2 { border-bottom: 3px solid #e8a0a0; padding-bottom: 8px; margin-top: 40px; }
  h3 { margin-top: 28px; color: #2c3e50; }
  .template-intro { font-size: 1.1em; line-height: 1.6; background: #fef6f6; padding: 20px; border-left: 4px solid #e8a0a0; border-radius: 4px; }
  .fill-field { border: none; border-bottom: 2px dashed #bbb; font-family: inherit; font-size: inherit; padding: 2px 6px; min-width: 180px; background: transparent; }
  .fill-field:focus { outline: none; border-bottom-color: #c0392b; }
  .fill-area { border: 1px solid #ddd; border-radius: 6px; padding: 10px; font-family: inherit; font-size: 0.95em; width: 100%; min-height: 60px; resize: vertical; box-sizing: border-box; background: #fafafa; }
  .fill-area:focus { outline: none; border-color: #c0392b; background: #fff; }
  .norm-card { background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.06); }
  .norm-card h4 { margin-top: 0; }
  .norm-card h4 span { display: inline-block; background: #c0392b; color: #fff; border-radius: 50%; width: 28px; height: 28px; text-align: center; line-height: 28px; font-size: 0.8em; margin-right: 8px; }
  .timeline-step { position: relative; padding-left: 50px; margin: 20px 0; }
  .timeline-step:before { content: attr(data-hour); position: absolute; left: 0; top: 0; background: #c0392b; color: #fff; width: 36px; height: 24px; border-radius: 4px; text-align: center; line-height: 24px; font-size: 0.75em; font-weight: bold; }
  .timeline-step:after { content: ""; position: absolute; left: 17px; top: 28px; bottom: -24px; width: 2px; background: #ddd; }
  .timeline-step:last-child:after { display: none; }
  .role-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0; }
  @media (max-width: 600px) { .role-grid { grid-template-columns: 1fr; } }
  .role-slot { background: #f8f9fa; border: 1px solid #ddd; border-radius: 6px; padding: 12px; }
  .role-slot label { font-weight: bold; font-size: 0.85em; color: #c0392b; display: block; margin-bottom: 4px; }
  .role-slot .fill-field { min-width: 140px; width: 100%; box-sizing: border-box; }
  .statement-block { background: #f9f9f9; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; margin: 16px 0; }
  .statement-block p { margin: 8px 0; }
  .debrief-card { background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 16px 0; }
  .debrief-card ol { padding-left: 20px; }
  .debrief-card ol li { margin: 12px 0; }
  .print-actions { margin-top: 30px; text-align: center; }
  .print-actions button { background: #c0392b; color: #fff; border: none; padding: 10px 24px; border-radius: 6px; font-size: 1em; cursor: pointer; }
  .print-actions button:hover { background: #a93226; }
  .footer-note { background: #fef6f6; border-radius: 8px; padding: 20px; margin-top: 40px; text-align: center; }
  @media print {
    .print-actions button { display: none; }
    .fill-field, .fill-area { border-color: #999; }
  }
  .fillable-note { background: #fff3e0; border-radius: 6px; padding: 12px 16px; margin: 12px 0; font-size: 0.9em; }
  .checklist-item { margin: 6px 0; padding-left: 28px; position: relative; }
  .checklist-item:before { content: "☐"; position: absolute; left: 0; font-size: 18px; }
  p strong { color: #2c3e50; }
</style>

<h1>Crisis Communications One-Pager Template</h1>

<p class="template-intro">
  <strong>When the news trucks show up, every minute counts.</strong>
  This template walks your board through the first 48 hours of a governance crisis —
  who speaks, what they say, and how to maintain a unified collective voice.
  <br/><br/>
  Fill in the fields below, print it, keep it in your board folder. When crisis hits,
  you don't build the plan — you execute it.
</p>

<div class="fillable-note">
  <strong>How to use:</strong> Fill in the text fields directly on this page, then print or save as PDF.
  All fields are expandable — type your answers, check boxes as you go.
</div>

<hr/>

<h2>1. Crisis Identification</h2>

<p>
  <strong>District:</strong> <input type="text" class="fill-field" placeholder="e.g., Lincoln Unified School District"/>
</p>
<p>
  <strong>Date:</strong> <input type="text" class="fill-field" placeholder="MM/DD/YYYY"/>
</p>
<p>
  <strong>Time first alerted:</strong> <input type="text" class="fill-field" placeholder="e.g., 6:45 AM"/>
</p>
<p>
  <strong>Brief crisis description:</strong></p>
<textarea class="fill-area" placeholder="e.g., Ethics allegation against a board member reported in local media. Board member cited in a lawsuit. Closed session recording leaked. Superintendent termination vote gone public."></textarea>
</p>

<p>
  <strong>Crisis type (check one):</strong>
</p>
<div class="checklist-item">Management crisis — operational issue (bus accident, data breach, facilities failure). Board supports, does NOT direct.</div>
<div class="checklist-item">Governance crisis — structural issue (ethics allegations, board dysfunction, superintendent termination, Title IX into board conduct). Board MUST lead.</div>

<hr/>

<h2>2. First Action — Convene the Board</h2>

<p>At the first sign of a governance crisis, the board president (or designee) should:</p>

<ol>
  <li>Determine whether an emergency closed session is legally permissible under state open meetings law.</li>
  <li>If closed session is not possible, schedule a special board meeting within 24 hours.</li>
  <li>Set a single agenda item: <strong>"What is our collective statement?"</strong></li>
</ol>

<p><strong>Meeting scheduled for:</strong> <input type="text" class="fill-field" placeholder="Date / Time / Location" style="min-width:280px;"/></p>

<p><strong>Board members contacted (☐ all confirmed):</strong> <input type="text" class="fill-field" placeholder="Names / method of contact" style="min-width:280px;"/></p>

<div class="checklist-item">Board counsel/attorney notified and available for the meeting</div>
<div class="checklist-item">Superintendent briefed and operating on a parallel track (operational response)</div>

<hr/>

<h2>3. The Three Crisis Norms</h2>

<p>Every board action during a crisis should pass through these three filters:</p>

<div class="norm-card">
<h4><span>1</span> <strong>Collective Voice — One. Voice.</strong></h4>
<p>The board has discussed the situation, agreed on what can be said, and every board member says the same thing. Not the board president speaking for everyone — <em>every</em> member, <em>one</em> message.</p>
<p class="checklist-item">The board agreed on a unified statement in closed session or special meeting</p>
<p class="checklist-item">Every board member has the agreed statement in writing</p>
<p class="checklist-item">All board members understand: no freelance statements, no "off the record," no "my personal opinion"</p>
</div>

<div class="norm-card">
<h4><span>2</span> <strong>Accuracy Over Speed</strong></h4>
<p>The press wants a comment by noon. Your community wants answers now. Speed without accuracy creates a second crisis. First statement says three things only.</p>
<p class="checklist-item">The board agrees: <em>"We will not be the fastest. We will be the most accurate."</em></p>
<p class="checklist-item">No speculation, no defensiveness, no contextualizing in the first statement</p>
<p class="checklist-item">Next communication deadline is set: <input type="text" class="fill-field" placeholder="e.g., 5:00 PM today" style="min-width:140px;"/></p>
</div>

<div class="norm-card">
<h4><span>3</span> <strong>Empathy Before Explanation</strong></h4>
<p>If the crisis involves harm, the board's first public words must be empathy — not context, not explanation, not defensiveness. Let empathy land first. Explain later.</p>
<p class="checklist-item">The first public statement includes an explicit expression of empathy or regret</p>
<p class="checklist-item">No qualifying language attached to the empathy statement</p>
<p class="checklist-item">A follow-up communication is scheduled to address what happens next</p>
</div>

<hr/>

<h2>4. Crisis Response Team — Roles & Assignments</h2>

<p>Fill in the person assigned to each role. Every board should have this pre-assigned; if not, assign now.</p>

<div class="role-grid">
  <div class="role-slot">
    <label>Board President / Designated Spokesperson</label>
    <input type="text" class="fill-field" placeholder="Name" style="width:100%; box-sizing:border-box;"/>
    <span style="font-size:0.8em;color:#888;">The only public voice unless delegated by board vote</span>
  </div>
  <div class="role-slot">
    <label>Board Attorney</label>
    <input type="text" class="fill-field" placeholder="Name / Firm" style="width:100%; box-sizing:border-box;"/>
    <span style="font-size:0.8em;color:#888;">On every crisis call, privilege-protected</span>
  </div>
  <div class="role-slot">
    <label>Superintendent (Operational Response)</label>
    <input type="text" class="fill-field" placeholder="Name" style="width:100%; box-sizing:border-box;"/>
    <span style="font-size:0.8em;color:#888;">Manages operational track while board manages governance track</span>
  </div>
  <div class="role-slot">
    <label>Communications Liaison (Board ↔ Comms)</label>
    <input type="text" class="fill-field" placeholder="Name" style="width:100%; box-sizing:border-box;"/>
    <span style="font-size:0.8em;color:#888;">Coordinates between board and comms team — not the public face</span>
  </div>
  <div class="role-slot">
    <label>Communications Staff</label>
    <input type="text" class="fill-field" placeholder="Name / Dept" style="width:100%; box-sizing:border-box;"/>
    <span style="font-size:0.8em;color:#888;">Statement drafting, media monitoring, social media protocols</span>
  </div>
  <div class="role-slot">
    <label>Alternative Spokesperson (Backup)</label>
    <input type="text" class="fill-field" placeholder="Name" style="width:100%; box-sizing:border-box;"/>
    <span style="font-size:0.8em;color:#888;">If primary is unavailable or conflicted</span>
  </div>
</div>

<hr/>

<h2>5. First Public Statement Template</h2>

<p class="fillable-note">
  <strong>Use this exact structure.</strong> Do not add information you haven't verified.
  Do not speculate. Do not contextualize. Three sentences, three elements.
</p>

<div class="statement-block">
  <p><strong>Sentence 1 — We are aware.</strong></p>
  <textarea class="fill-area" placeholder="e.g., The [District Name] Board of Trustees is aware of the report regarding [brief factual description of the situation]." style="min-height:50px;"></textarea>

  <p><strong>Sentence 2 — We take it seriously.</strong></p>
  <textarea class="fill-area" placeholder="e.g., We take this matter seriously and are committed to a thorough and transparent process." style="min-height:50px;"></textarea>

  <p><strong>Sentence 3 — We will communicate again by [time].</strong></p>
  <textarea class="fill-area" placeholder="e.g., We are currently gathering the facts and will provide an update by [specific time/date]. No further comment will be made until then." style="min-height:50px;"></textarea>
</div>

<p><strong>Statement approved by board in session on:</strong> <input type="text" class="fill-field" placeholder="Date / Time"/></p>

<div class="checklist-item">Statement reviewed by board attorney before release</div>
<div class="checklist-item">Statement shared with ALL board members before release to press</div>
<div class="checklist-item">Spokesperson confirmed and briefed on what they may answer beyond the statement</div>

<hr/>

<h2>6. First 48-Hour Timeline</h2>

<div class="timeline-step" data-hour="H+0">
  <p><strong>Crisis hits</strong> — Phone starts buzzing. Reporter calls. Social media posts going viral. Pause. Do not respond yet. Start the protocol.</p>
</div>

<div class="timeline-step" data-hour="H+1">
  <p><strong>Board president convenes</strong> — Emergency closed session (if legal) or special meeting notice sent. Attorney notified. Superintendent briefed on parallel-track operation.</p>
</div>

<div class="timeline-step" data-hour="H+3">
  <p><strong>Board meets</strong> — Agenda: one item. Agree on collective statement. Approve the three-sentence release. Designate spokesperson.</p>
</div>

<div class="timeline-step" data-hour="H+4">
  <p><strong>First statement released</strong> — Through official district channels. Board president (spokesperson) reads verbatim if press conference. No Q&A beyond the statement.</p>
</div>

<div class="timeline-step" data-hour="H+12">
  <p><strong>Fact-gathering continues</strong> — Board tracks parallel with superintendent's operational response. No new public statement unless facts materially change.</p>
</div>

<div class="timeline-step" data-hour="H+24">
  <p><strong>Second communication window</strong> — Follow-up statement or update as promised. This is where you can provide next steps, investigation timeline, or process.</p>
</div>

<div class="timeline-step" data-hour="H+48">
  <p><strong>Board reconvenes</strong> — Assess: is the crisis escalating, plateauing, or de-escalating? Determine next public communication cadence. Begin documenting for post-crisis debrief.</p>
</div>

<hr/>

<h2>7. Key Media Contact Log</h2>

<table style="width:100%; border-collapse: collapse; margin: 16px 0;">
  <tr style="background:#f0f0f0;">
    <th style="padding:8px 12px; border:1px solid #ddd; text-align:left;">Outlet</th>
    <th style="padding:8px 12px; border:1px solid #ddd; text-align:left;">Reporter</th>
    <th style="padding:8px 12px; border:1px solid #ddd; text-align:left;">Contact</th>
    <th style="padding:8px 12px; border:1px solid #ddd; text-align:left;">Deadline</th>
    <th style="padding:8px 12px; border:1px solid #ddd; text-align:left;">Responded?</th>
  </tr>
  <tr>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Outlet"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Reporter"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Phone/Email"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:60px; width:100%; box-sizing:border-box;" placeholder="Time"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd; text-align:center;">☐</td>
  </tr>
  <tr>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Outlet"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Reporter"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Phone/Email"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:60px; width:100%; box-sizing:border-box;" placeholder="Time"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd; text-align:center;">☐</td>
  </tr>
  <tr>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Outlet"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Reporter"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:80px; width:100%; box-sizing:border-box;" placeholder="Phone/Email"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd;"><input type="text" class="fill-field" style="min-width:60px; width:100%; box-sizing:border-box;" placeholder="Time"/></td>
    <td style="padding:4px 8px; border:1px solid #ddd; text-align:center;">☐</td>
  </tr>
</table>

<hr/>

<h2>8. Post-Crisis Debrief</h2>

<p>A governance crisis doesn't end when the news trucks leave. It ends when the board has answered three questions — honestly, as a full governance team:</p>

<div class="debrief-card">
<ol>
  <li>
    <strong>What caused this crisis?</strong><br/>
    Was it a failure of policy, of oversight, of culture? Be honest with yourselves.
    <textarea class="fill-area" placeholder="Your notes..." style="min-height:50px;"></textarea>
  </li>
  <li>
    <strong>What systemic change prevents recurrence?</strong><br/>
    A single apology isn't a fix. What policy, practice, or norm needs to change — permanently?
    <textarea class="fill-area" placeholder="Your notes..." style="min-height:50px;"></textarea>
  </li>
  <li>
    <strong>What did we learn about ourselves?</strong><br/>
    Did we maintain collective voice? Did we put accuracy over speed? Did we lead with empathy?
    <textarea class="fill-area" placeholder="Your notes..." style="min-height:50px;"></textarea>
  </li>
</ol>
</div>

<div class="checklist-item">Post-crisis debrief scheduled on the board calendar within 30 days of crisis resolution</div>
<div class="checklist-item">Findings documented for the board's permanent records</div>
<div class="checklist-item">Revisions made to crisis response protocol based on lessons learned</div>

<hr/>

<h2>Your Guiding Question</h2>

<p style="font-size:1.2em; text-align:center; padding: 20px; background: #fef6f6; border-radius: 8px;">
  <strong>Does this serve student outcomes first?</strong><br/>
  <span style="font-size:0.8em; color:#666;">The point of surviving a crisis isn't to protect the board.<br/>It's to protect the district's ability to deliver on its mission for every student.</span>
</p>

<hr/>

<div class="print-actions">
  <button onclick="window.print()">🖨️ Print or Save as PDF</button>
  <p style="font-size:0.85em; color:#888; margin-top:8px;">Printing preserves all fillable fields as dashed-underlined blanks for handwritten use.</p>
</div>

<div class="footer-note">
<p><strong>From the desk of AJ Crabill</strong><br/>
This template is adapted from <em>"When the News Trucks Show Up"</em> — the August edition of <em>The Effective School Board Member</em> newsletter, based on the ESB Guidance Doc: Effective Governance Crisis Communications.<br/>
For board coaching, crisis communications training, and the full ESB Framework, visit <a href="https://effectiveschoolboards.com/">effectiveschoolboards.com</a>.</p>
</div>
