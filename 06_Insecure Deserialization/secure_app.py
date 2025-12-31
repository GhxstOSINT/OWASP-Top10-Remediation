import json # Use JSON instead of Pickle
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    cookie = request.cookies.get('session')
    if cookie:
        try:
            # ✅ THE FIX: Use a safe serialization format
            # JSON is just text. It cannot define classes or run code.
            # Even if the attacker modifies the JSON, it's just data.
            data = json.loads(base64.b64decode(cookie))
            return f"Welcome back, {data['username']}!"
        except:
            return "Cookie Error"
    return "No Session Cookie Found"

if __name__ == '__main__':
    app.run(debug=True, port=5006)