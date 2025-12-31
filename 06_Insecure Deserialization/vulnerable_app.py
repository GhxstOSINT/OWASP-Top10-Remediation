import pickle
import base64
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # 🛑 THE VULNERABILITY:
    # Taking a cookie, base64 decoding it, and passing it to pickle.loads()
    # pickle allows arbitrary object instantiation during loading.
    cookie = request.cookies.get('session')
    if cookie:
        try:
            # UNSECURE: This executes whatever code is frozen in the object
            data = pickle.loads(base64.b64decode(cookie))
            return f"Welcome back, {data['username']}!"
        except:
            return "Cookie Error"
    return "No Session Cookie Found"

if __name__ == '__main__':
    app.run(debug=True, port=5006)