---
layout: base
title: "Devon — Chat"
---

<div id="devon-chat" style="max-width: 800px; margin: 0 auto; padding: 20px;">
  <p><a href="/devon/" style="color:#0d6b4a;">&larr; Back to Login</a></p>
  <div id="chat-messages" style="height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 15px; margin-bottom: 15px; background: #fafafa; border-radius: 8px;">
    <div style="color: #888; text-align: center; padding: 20px;">Connecting to Devon...</div>
  </div>
  
  <div style="display: flex; gap: 10px;">
    <input type="text" id="chat-input" placeholder="Type your message..." 
           style="flex: 1; padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px;">
    <button onclick="sendMsg()" 
            style="padding: 12px 24px; background: #0d6b4a; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;">
      Send
    </button>
  </div>
</div>

<script src="chat.js"></script>
