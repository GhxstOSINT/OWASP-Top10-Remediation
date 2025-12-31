from flask import Flask, request

app = Flask(__name__)

# The secret password
REAL_PASSWORD = "password123"

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    
    # 🛑 THE VULNERABILITY:
    # No rate limiting. No lockout.
    # An attacker can try 1,000,000 passwords per second.
    if password == REAL_PASSWORD:
        return "✅ Login Success"
    else:
        return "❌ Login Failed"

if __name__ == '__main__':
    app.run(debug=True, port=5013)