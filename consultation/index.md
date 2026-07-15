---
layout: base
title: "Free Consultation"
summary: "Consultation"
toplevel: Consultation
# toplevellink: /consultation
---

<div id="consultation-form-wrap">

Teachers need coaches to be their best. Principals need coaches to be their best. Superintendents need coaches to be their best. School boards need coaches to be their best.<br/><br/> If your school board wants support to be great on behalf of the students you serve, complete the form below for a free consultation.<br/><br/>

<form id="consultation-form">
  Name<br/><input type="text" value="" name="name" id="c-name"><br/><br/>
  Email<br/><input type="text" value="" name="email" id="c-email"><br/><br/>
  Title/Role<br/><input type="text" value="" name="title" id="c-title"><br/><br/>
  School System<br/><input type="text" value="" name="schoolsystem" id="c-schoolsystem"><br/><br/>
  Message<br/><textarea name="message" id="c-message" rows="4" cols="100">What challenge are you facing or what opportunity are you wanting to harvest?</textarea><br/><br/>
  <button type="submit" id="c-submit-btn">Send</button>
  <p id="c-error" style="display:none; color: #b3261e;">Please fill in your name and a valid email address.</p>
</form>

</div>

<div id="consultation-thanks" style="display:none;">
  <h2>Thank you</h2>
  <p>Your request has been sent. Someone from Effective School Boards will follow up with you soon.</p>
</div>

<script>
(function () {
  'use strict';

  var FUNNEL_API = 'https://api.gotb.effectiveschoolboards.com/api/directory/leads/inbound/consultation';

  // If this page was reached from the gotb-free results screen's "Schedule a
  // Free Consultation" CTA, it carries the same person's lead_id forward
  // (plus name/email/district to pre-fill) so this request merges into their
  // existing funnel row instead of creating a disconnected second one
  // (AJ, 2026-07-15).
  var params = new URLSearchParams(location.search);
  var leadId = params.get('lead_id') || '';
  if (params.get('name')) document.getElementById('c-name').value = params.get('name');
  if (params.get('email')) document.getElementById('c-email').value = params.get('email');
  if (params.get('district')) document.getElementById('c-schoolsystem').value = params.get('district');

  // The CTA itself is labeled "Schedule a Free Consultation" -- clicking it
  // should register as requesting one, not require also filling out and
  // sending the form below (AJ, 2026-07-15: "even though i click on
  // consultation, in funnel it says requested consultation: no"). Fire the
  // moment we land here with enough from the query string; the form submit
  // below still fires its own call on top of this if they go on to send it,
  // carrying whatever title/message they typed (the backend merge is
  // idempotent on the boilerplate note line + timestamp, so this doesn't
  // double up -- see funnel.record_consultation_request).
  if (leadId && params.get('name') && params.get('email')) {
    fetch(FUNNEL_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: params.get('name'), email: params.get('email'),
        schoolsystem: params.get('district') || '', lead_id: leadId,
      }),
    }).catch(function(){ /* best-effort */ });
  }

  function submitForm(e) {
    e.preventDefault();
    var name = document.getElementById('c-name').value.trim();
    var email = document.getElementById('c-email').value.trim();
    var title = document.getElementById('c-title').value.trim();
    var schoolsystem = document.getElementById('c-schoolsystem').value.trim();
    var message = document.getElementById('c-message').value.trim();
    var errEl = document.getElementById('c-error');

    if (!name || !email || !email.includes('@') || !email.includes('.')) {
      errEl.style.display = 'block';
      return;
    }
    errEl.style.display = 'none';

    var btn = document.getElementById('c-submit-btn');
    btn.textContent = 'Sending…';
    btn.disabled = true;

    var payload = { name: name, email: email, title: title, schoolsystem: schoolsystem, message: message };
    if (leadId) payload.lead_id = leadId;

    // Formspree removed (AJ, 2026-07-15: "you can remove formspree") -- the
    // portal itself now emails staff on a consultation request (see
    // esb-portal's directory/router.py _notify_consultation_request), so this
    // funnel POST is the only notification path left.
    fetch(FUNNEL_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    }).catch(function(){ /* best-effort */ });

    document.getElementById('consultation-form-wrap').style.display = 'none';
    document.getElementById('consultation-thanks').style.display = 'block';
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('consultation-form').addEventListener('submit', submitForm);
  });
})();
</script>
