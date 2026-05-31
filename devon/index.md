---
layout: base
title: "Devon — ESB CRM"
---

<div style="max-width: 900px; margin: 0 auto; padding: 20px;">
  <h2>ESB CRM</h2>
  <p style="color: #666; margin-bottom: 20px;">School system data, clients, and contacts.</p>

  <div id="stats" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 30px;">
    <div class="stat-card" style="background: #f0f8f4; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #c8e6c9;">
      <div id="district-count" style="font-size: 2em; font-weight: bold; color: #0d6b4a;">—</div>
      <div style="color: #555;">School Systems</div>
    </div>
    <div class="stat-card" style="background: #e8f0fe; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #bbdefb;">
      <div id="leader-count" style="font-size: 2em; font-weight: bold; color: #1565c0;">—</div>
      <div style="color: #555;">People</div>
    </div>
    <div class="stat-card" style="background: #fff8e1; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #ffecb3;">
      <div id="client-count" style="font-size: 2em; font-weight: bold; color: #e65100;">—</div>
      <div style="color: #555;">Clients</div>
    </div>
  </div>

  <div style="margin-bottom: 30px;">
    <h3>Quick Links</h3>
    <a href="/devon/chat/" style="display: inline-block; padding: 12px 24px; background: #0d6b4a; color: white; text-decoration: none; border-radius: 6px; margin-right: 10px;">Chat with Devon</a>
  </div>

  <div style="margin-bottom: 20px;">
    <h3>Recent Clients</h3>
    <div id="client-list" style="background: #fafafa; border: 1px solid #ddd; border-radius: 8px; padding: 15px;">
      <div style="color: #888;">Loading...</div>
    </div>
  </div>
</div>

<script>
const API = 'https://esblaptop-m4.taild49f53.ts.net';

async function loadStats() {
  try {
    const r = await fetch(API + '/api/conversations/1/message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: 'overview' })
    });
    const d = await r.json();
    const m = d.response || '';
    const nums = m.match(/\d[\d,]*/g) || [];
    if (nums.length >= 2) {
      document.getElementById('district-count').textContent = nums[0];
      document.getElementById('leader-count').textContent = nums[1] || '—';
    }
  } catch(e) {
    document.getElementById('district-count').textContent = '?';
    document.getElementById('leader-count').textContent = '?';
    document.getElementById('client-count').textContent = '?';
  }

  try {
    const r = await fetch(API + '/api/conversations/1/message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: 'active clients' })
    });
    const d = await r.json();
    const box = document.getElementById('client-list');
    if (d.response) {
      box.innerHTML = '<pre style="white-space: pre-wrap; font-family: inherit; margin: 0;">' + esc(d.response) + '</pre>';
    }
  } catch(e) {}
}

function esc(t) { const d = document.createElement('div'); d.textContent = t; return d.innerHTML; }
loadStats();
</script>
