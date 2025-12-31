from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # 🛑 THE VULNERABILITY:
    # We take user input and send it straight back to the browser.
    # If the input contains HTML tags (like <script>), the browser executes them.
    return f"<h1>You searched for: {query}</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5002)