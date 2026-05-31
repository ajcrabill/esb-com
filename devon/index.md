---
layout: base
title: "Devon — ESB Login"
---

<style>
*{box-sizing:border-box}
.login-box{max-width:400px;margin:60px auto;padding:30px;background:#fafafa;border:1px solid #ddd;border-radius:8px;text-align:center}
.login-box h2{margin-bottom:10px}
.login-box p{color:#666;margin-bottom:20px}
.login-box input{width:100%;padding:12px;border:1px solid #ccc;border-radius:6px;font-size:16px;text-align:center;margin-bottom:12px}
.login-box button{width:100%;padding:12px;background:#0d6b4a;color:#fff;border:none;border-radius:6px;font-size:16px;cursor:pointer}
.login-box .msg{margin-top:12px;padding:8px;border-radius:4px;display:none}
.login-box .error{background:#f8d7da;color:#721c24;display:block}
.login-box .success{background:#d4edda;color:#155724;display:block}
.login-box .step{display:none}
.login-box .step.active{display:block}
.otp-input{letter-spacing:4px;font-size:20px;font-weight:bold}
</style>

<div class="login-box">
  <h2>Devon</h2>
  <p>ESB Operations Assistant</p>

  <div id="step-email" class="step active">
    <input type="email" id="email-input" placeholder="Enter your email">
    <button onclick="requestOtp()">Send Login Code</button>
    <div id="msg-email" class="msg"></div>
  </div>

  <div id="step-otp" class="step">
    <p style="font-size:14px">Code sent to <span id="otp-email"></span></p>
    <input type="text" id="otp-input" class="otp-input" placeholder="000000" maxlength="6" oninput="autoVerify(this)">
    <div id="msg-otp" class="msg"></div>
  </div>
</div>

<script>
const API = 'https://esblaptop-m4.taild49f53.ts.net';

async function requestOtp() {
  const email = document.getElementById('email-input').value.trim();
  const msg = document.getElementById('msg-email');
  msg.className = 'msg';
  if (!email) { msg.textContent = 'Enter your email'; msg.className = 'msg error'; return; }
  msg.textContent = 'Sending...';
  try {
    const r = await fetch(API + '/api/auth/request', {
      method: 'POST', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({email})
    });
    const d = await r.json();
    if (r.ok) {
      document.getElementById('step-email').className = 'step';
      document.getElementById('step-otp').className = 'step active';
      document.getElementById('otp-email').textContent = email;
      document.getElementById('otp-input').focus();
    } else {
      msg.textContent = d.detail || 'Not authorized';
      msg.className = 'msg error';
    }
  } catch(e) {
    msg.textContent = 'Connection error';
    msg.className = 'msg error';
  }
}

async function autoVerify(inp) {
  if (inp.value.length === 6) {
    const email = document.getElementById('otp-email').textContent;
    const msg = document.getElementById('msg-otp');
    msg.className = 'msg';
    msg.textContent = 'Verifying...';
    try {
      const r = await fetch(API + '/api/auth/verify', {
        method: 'POST', headers: {'Content-Type':'application/json'},
        body: JSON.stringify({email, code: inp.value})
      });
      const d = await r.json();
      if (r.ok) {
        localStorage.setItem('devon_token', d.token);
        localStorage.setItem('devon_name', d.name);
        localStorage.setItem('devon_access', JSON.stringify(d.access));
        msg.textContent = 'Welcome, ' + d.name + '!';
        msg.className = 'msg success';
        setTimeout(() => {
          if (d.access.includes('/devon/crm/')) window.location.href = '/devon/crm/';
          else if (d.access.includes('/devon/chat/')) window.location.href = '/devon/chat/';
        }, 500);
      } else {
        msg.textContent = d.detail || 'Invalid code';
        msg.className = 'msg error';
        inp.value = '';
      }
    } catch(e) {
      msg.textContent = 'Connection error';
      msg.className = 'msg error';
    }
  }
}

// Check if already logged in
const token = localStorage.getItem('devon_token');
if (token) {
  fetch(API + '/api/auth/check', {
    method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify({token})
  }).then(r => {
    if (r.ok) {
      window.location.href = '/devon/crm/';
    } else {
      localStorage.removeItem('devon_token');
    }
  }).catch(() => {});
}
</script>
