const API = 'https://esblaptop-m4.taild49f53.ts.net';
let convId = null;

// Get or create conversation on load
fetch(API + '/api/conversations/current')
  .then(r => r.json())
  .then(d => {
    convId = d.id;
    document.getElementById('chat-messages').innerHTML = '<div class="connected">\u2713 Connected to Devon API</div>';
  })
  .catch(() => {
    document.getElementById('chat-messages').innerHTML = '<div class="offline">\u26a0 Backend API not reachable</div>';
  });

function esc(t) { const d = document.createElement('div'); d.textContent = t; return d.innerHTML; }

async function sendMsg() {
  const inp = document.getElementById('chat-input');
  const msg = inp.value.trim();
  if (!msg || !convId) return;
  inp.value = '';
  const box = document.getElementById('chat-messages');
  box.innerHTML += '<div class="msg-right"><span>' + esc(msg) + '</span></div>';
  box.scrollTop = box.scrollHeight;
  box.innerHTML += '<div class="msg-left"><span><em>Sending...</em></span></div>';
  try {
    const r = await fetch(API + '/api/conversations/' + convId + '/message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg })
    });
    const d = await r.json();
    box.innerHTML = box.innerHTML.replace(/<div class="msg-left"><span><em>Sending\.\.\.<\/em><\/span><\/div>$/, '');
    box.innerHTML += '<div class="msg-left"><span>Message recorded (id: ' + d.conversation_id + ')</span></div>';
  } catch(e) {
    box.innerHTML = box.innerHTML.replace(/<div class="msg-left"><span><em>Sending\.\.\.<\/em><\/span><\/div>$/, '');
    box.innerHTML += '<div class="msg-error"><span>Error: ' + esc(e.message) + '</span></div>';
  }
  box.scrollTop = box.scrollHeight;
}
document.addEventListener('keydown', function(e) { if (e.key === 'Enter') sendMsg(); });
