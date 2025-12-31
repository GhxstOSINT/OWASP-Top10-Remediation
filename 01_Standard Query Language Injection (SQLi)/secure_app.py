import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()
    
    # ✅ THE FIX: Parameterized Queries
    # We use '?' as a placeholder.
    # The database library treats the input strictly as text, never as code.
    query = "SELECT * FROM users WHERE username = ?"
    
    # We pass the variables as a tuple (username,) separate from the query string
    cursor.execute(query, (username,))
    
    user = cursor.fetchone()
    if user:
        return f"✅ Logged in safely! Data: {user}"
    else:
        return "❌ Login failed."

if __name__ == '__main__':
    app.run(debug=True, port=5001)