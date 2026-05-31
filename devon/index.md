---
layout: base
title: "Devon — ESB Assistant"
---

<div id="devon-chat" style="max-width: 800px; margin: 0 auto; padding: 20px;">
  <h2>Devon</h2>
  <p>Your ESB operations assistant. Ask me anything about your districts, leads, or pipeline.</p>
  
  <div id="chat-messages" style="height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 15px; margin-bottom: 15px; background: #fafafa; border-radius: 8px;">
    <div style="color: #888; text-align: center; padding: 20px;">Connecting to Devon...</div>
  </div>
  
  <div style="display: flex; gap: 10px;">
    <input type="text" id="chat-input" placeholder="Type your message..." 
           style="flex: 1; padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px;">
    <button onclick="sendMessage()" 
            style="padding: 12px 24px; background: #0d6b4a; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;">
      Send
    </button>
  </div>
</div>

<script>
const API_URL = 'https://esblaptop-m4.taild49f53.ts.net';

async function sendMessage() {
  const input = document.getElementById('chat-input');
  const msg = input.value.trim();
  if (!msg) return;
  const div = document.getElementById('chat-messages');
  div.innerHTML += '<div style="text-align:right;margin:8px 0"><span style="background:#0d6b4a;color:white;padding:8px 14px;border-radius:12px;display:inline-block;max-width:70%">'+escapeHtml(msg)+'</span></div>';
  input.value = '';
  div.scrollTop = div.scrollHeight;
  div.innerHTML += '<div style="text-align:left;margin:8px 0"><span style="background:#e9ecef;padding:8px 14px;border-radius:12px;display:inline-block;max-width:70%"><em>Thinking...</em></span></div>';
  try {
    const res = await fetch(API_URL + '/api/conversations/message', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:msg})});
    const data = await res.json();
    div.innerHTML = div.innerHTML.replace(/<div style="text-align:left;margin:8px 0"><span[^>]*><em>Thinking\.\.\.<\/em><\/span><\/div>$/, '');
    div.innerHTML += '<div style="text-align:left;margin:8px 0"><span style="background:#e9ecef;padding:8px 14px;border-radius:12px;display:inline-block;max-width:70%">'+escapeHtml(data.response||JSON.stringify(data))+'</span></div>';
  } catch(e) {
    div.innerHTML = div.innerHTML.replace(/<div style="text-align:left;margin:8px 0"><span[^>]*><em>Thinking\.\.\.<\/em><\/span><\/div>$/, '');
    div.innerHTML += '<div style="text-align:left;margin:8px 0"><span style="background:#f8d7da;color:#721c24;padding:8px 14px;border-radius:12px;display:inline-block;max-width:70%">Error: '+escapeHtml(e.message)+'</span></div>';
  }
}
function escapeHtml(t){const d=document.createElement('div');d.textContent=t;return d.innerHTML;}
document.addEventListener('keydown',function(e){if(e.key==='Enter')sendMessage();});
fetch(API_URL+'/api/health').then(r=>r.json()).then(()=>{document.getElementById('chat-messages').innerHTML='<div style="color:#0d6b4a;text-align:center;padding:20px">✓ Connected to Devon API</div>';}).catch(()=>{document.getElementById('chat-messages').innerHTML='<div style="color:#856404;text-align:center;padding:20px">⚠ Backend API not reachable</div>';});
</script>
