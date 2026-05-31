---
layout: base
title: "Devon — CRM"
---

<style>
*{box-sizing:border-box}
.crm-nav{background:#0d6b4a;padding:10px 20px;display:flex;gap:15px;align-items:center;margin-bottom:20px}
.crm-nav a{color:white;text-decoration:none;font-size:14px;padding:5px 10px;border-radius:4px}
.crm-nav a:hover{background:rgba(255,255,255,0.2)}
.crm-nav .user{color:rgba(255,255,255,0.8);margin-left:auto;font-size:13px}
.crm-nav .logout{color:#ffcdd2;cursor:pointer}
.panel{max-width:1200px;margin:0 auto;padding:0 20px 40px}
.section{margin-bottom:30px}
.section h3{border-bottom:2px solid #0d6b4a;padding-bottom:8px;margin-bottom:15px}
.card{background:#fafafa;border:1px solid #ddd;border-radius:6px;padding:15px;margin-bottom:10px}
.card:hover{background:#f0f8f4}
.card .name{font-weight:bold;font-size:16px}
.card .meta{color:#666;font-size:13px;margin-top:4px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:15px}
.stat-row{display:grid;grid-template-columns:repeat(4,1fr);gap:15px;margin-bottom:25px}
.stat-box{text-align:center;padding:20px;border-radius:8px}
.stat-box .num{font-size:2em;font-weight:bold}
.stat-box .label{font-size:13px;color:#666;margin-top:4px}
.loading{text-align:center;padding:40px;color:#888}
.error{color:#721c24;background:#f8d7da;padding:15px;border-radius:6px;margin:20px}
</style>

<div class="crm-nav">
  <a href="/devon/crm/">Dashboard</a>
  <a href="/devon/chat/">Chat</a>
  <span class="user" id="user-display"></span>
  <a class="logout" onclick="logout()">Logout</a>
</div>

<div id="app" class="panel"><div class="loading">Loading CRM data...</div></div>

<script>
const API = 'https://esblaptop-m4.taild49f53.ts.net';

// Auth check
const token = localStorage.getItem('devon_token');
if (!token) { window.location.href = '/devon/'; return; }
document.getElementById('user-display').textContent = localStorage.getItem('devon_name') || 'User';

function logout() { localStorage.clear(); window.location.href = '/devon/'; }

async function loadDashboard() {
  const app = document.getElementById('app');
  try {
    // Stats
    const statsRes = await fetch(API + '/api/conversations/1/message', {
      method: 'POST', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({message:'overview'})
    });
    const stats = await statsRes.json();
    const nums = (stats.response || '').match(/\d[\d,]*/g) || ['0','0','0'];
    
    // Active clients
    const clientsRes = await fetch(API + '/api/conversations/1/message', {
      method: 'POST', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({message:'active clients'})
    });
    const clients = await clientsRes.json();
    
    app.innerHTML = `
      <div class="stat-row">
        <div class="stat-box" style="background:#e8f5e9;border:1px solid #c8e6c9">
          <div class="num" style="color:#2e7d32">${nums[0]||'—'}</div>
          <div class="label">School Systems</div>
        </div>
        <div class="stat-box" style="background:#e3f2fd;border:1px solid #bbdefb">
          <div class="num" style="color:#1565c0">${nums[1]||'—'}</div>
          <div class="label">People</div>
        </div>
        <div class="stat-box" style="background:#fff3e0;border:1px solid #ffe0b2">
          <div class="num" style="color:#e65100">${nums[2]||'—'}</div>
          <div class="label">Clients</div>
        </div>
        <div class="stat-box" style="background:#f3e5f5;border:1px solid #e1bee7">
          <div class="num" style="color:#6a1b9a">${(await fetch(API+'/api/conversations/1/message',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:'how many people'})}).then(r=>r.json()).then(d=>{const m=d.response||'';const n=m.match(/[\d,]+/);return n?n[0]:'—'}).catch(()=>'?'))}</div>
          <div class="label">Total Leaders</div>
        </div>
      </div>
      
      <div class="section">
        <h3>Active Clients</h3>
        <div class="grid">
          ${renderClients(clients.response || 'No active clients')}
        </div>
      </div>
      
      <div class="section">
        <h3>Quick Actions</h3>
        <a href="/devon/chat/" style="display:inline-block;padding:12px 24px;background:#0d6b4a;color:white;text-decoration:none;border-radius:6px">Chat with Devon</a>
        <a href="/devon/crm/search" style="display:inline-block;padding:12px 24px;background:#1565c0;color:white;text-decoration:none;border-radius:6px;margin-left:10px">Search Districts</a>
      </div>
    `;
  } catch(e) {
    app.innerHTML = '<div class="error">Error loading CRM data: ' + e.message + '</div>';
  }
}

function renderClients(text) {
  if (!text || text === 'No active clients') return '<div class="card">No active clients found</div>';
  const lines = text.split('\n').filter(l => l.trim() && !l.startsWith('**'));
  return lines.map(l => {
    const parts = l.replace(/^[•\s]*/, '').split('|');
    const name = parts[0] ? parts[0].trim() : 'Unknown';
    const meta = parts.slice(1).join(' | ').trim();
    return `<div class="card"><div class="name">${name}</div>${meta ? '<div class="meta">'+meta+'</div>' : ''}</div>`;
  }).join('');
}

loadDashboard();
</script>
