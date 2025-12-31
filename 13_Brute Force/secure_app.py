import time
from flask import Flask, request

app = Flask(__name__)
REAL_PASSWORD = "password123"

# Memory to track failed attempts (IP Address -> Count)
failed_attempts = {}

@app.route('/login', methods=['POST'])
def login():
    ip = request.remote_addr
    password = request.form.get('password')
    
    # ✅ THE FIX: Rate Limiting
    # If this IP failed 3 times recently, block them.
    if failed_attempts.get(ip, 0) >= 3:
        return "⛔ Account Locked. Too many attempts."
        
    if password == REAL_PASSWORD:
        # Reset counter on success
        failed_attempts[ip] = 0
        return "✅ Login Success"
    else:
        # Increment counter on failure
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
        return "❌ Login Failed"

if __name__ == '__main__':
    app.run(debug=True, port=5013)