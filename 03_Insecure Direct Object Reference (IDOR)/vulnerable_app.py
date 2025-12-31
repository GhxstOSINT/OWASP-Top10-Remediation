import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/profile')
def profile():
    # 1. User asks for a user ID (e.g., ?id=1)
    user_id = request.args.get('id')
    
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()
    
    # 🛑 THE VULNERABILITY:
    # The app assumes that because you asked for ID #1, you are allowed to see it.
    # It does not check if YOU are actually User #1.
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    data = cursor.fetchone()
    
    return f"Profile Data: {data}"

if __name__ == '__main__':
    app.run(debug=True, port=5003)