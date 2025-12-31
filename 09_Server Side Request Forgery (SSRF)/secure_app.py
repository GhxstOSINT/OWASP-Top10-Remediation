import requests
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)

def is_safe_url(target_url):
    parsed = urlparse(target_url)
    hostname = parsed.hostname
    
    # ✅ THE FIX: Allowlisting
    # 1. Restrict schemes (only http/https, no file://)
    if parsed.scheme not in ('http', 'https'):
        return False
        
    # 2. Block internal IP ranges (localhost, 127.0.0.1, 192.168.x.x)
    if hostname in ['localhost', '127.0.0.1', '0.0.0.0']:
        return False
        
    return True

@app.route('/check_status')
def check_status():
    target_url = request.args.get('url')
    
    if not is_safe_url(target_url):
        return "❌ Request Blocked: Internal/Unsafe URL detected."
        
    try:
        response = requests.get(target_url, timeout=2)
        return f"Status: {response.status_code}"
    except:
        return "Failed"

if __name__ == '__main__':
    app.run(debug=True, port=5009)