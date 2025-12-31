from flask import Flask, request, escape 
# 'escape' is a function that neutralizes special characters

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # ✅ THE FIX: Context-Aware Encoding
    # The escape() function turns '<' into '&lt;'
    # The browser sees '&lt;script&gt;' and displays text, instead of running code.
    safe_query = escape(query)
    
    return f"<h1>You searched for: {safe_query}</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5002)