
from flask import Flask, request, render_template_string
import time
import random

app = Flask(__name__)

# Basit bir IP rate-limiting mekanizması
request_count = {}
RATE_LIMIT = 5  # 5 istekte ban
BAN_DURATION = 60  # 60 saniye ban süresi

@app.before_request
def limit_requests():
    ip = request.remote_addr
    current_time = time.time()
    
    if ip in request_count:
        timestamps = request_count[ip]
        # Eski istekleri temizle
        request_count[ip] = [t for t in timestamps if current_time - t < BAN_DURATION]
        
        if len(request_count[ip]) >= RATE_LIMIT:
            return "Too many requests. You are temporarily blocked.", 429
    else:
        request_count[ip] = []
    
    request_count[ip].append(current_time)

# Basit honeypot tuzağı
HONEYPOT_LINK = "/hidden-bot-trap"

@app.route(HONEYPOT_LINK)
def bot_trap():
    return "Detected as bot! Access denied.", 403

@app.route('/')
def home():
    # Honeypot linki görünmez şekilde ekleniyor
    html_content = '''
    <html>
    <head>
        <script>
            // JavaScript olmadan sayfa içeriği yüklenmeyecek (botları engellemek için)
            document.addEventListener("DOMContentLoaded", function() {
                document.getElementById("content").style.display = "block";
            });
        </script>
        <style>
            a.hidden { display: none; }
            #content { display: none; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Comic Archive</h1>
        <a href="''' + HONEYPOT_LINK + '''" class="hidden">Hidden Bot Trap</a>
        <div id="content">
            <p>Here are some comics:</p>
            <img src="https://example.com/comic1.jpg" />
            <img src="https://example.com/comic2.jpg" />
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
