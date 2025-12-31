import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    # 1. Get user input
    username = request.args.get('username')
    
    # 2. Connect to DB
    conn = sqlite3.connect('../database.db') # Note the ../ to go up one folder
    cursor = conn.cursor()
    
    # 🛑 THE VULNERABILITY:
    # Using an 'f-string' to put input directly into the query.
    # If the user types: admin' --
    # The query becomes: SELECT * FROM users WHERE username = 'admin' --'
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return f"✅ Logged in! Data: {user}"
        else:
            return "❌ Login failed."
    except Exception as e:
        return f"Database Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)