import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/check_status')
def check_status():
    # The user provides a URL, and the server checks if it's up.
    target_url = request.args.get('url')
    
    # 🛑 THE VULNERABILITY:
    # The server fetches ANY url the user provides.
    # An attacker can make the server look at internal resources hidden behind the firewall.
    try:
        response = requests.get(target_url, timeout=2)
        return f"Status of {target_url}: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    # We simulate a secret internal admin panel on port 9000
    # Only "localhost" (the server itself) can access this.
    @app.route('/admin')
    def admin():
        if request.remote_addr != '127.0.0.1':
            return "403 Forbidden", 403
        return "SECRET ADMIN PANEL REVEALED"
        
    app.run(debug=True, port=5009)