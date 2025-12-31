import sqlite3
from flask import Flask, request, abort

app = Flask(__name__)

# Simulate a logged-in user (In a real app, this comes from a session cookie)
CURRENT_LOGGED_IN_USER_ID = 2 

@app.route('/profile')
def profile():
    requested_id = request.args.get('id')
    
    # ✅ THE FIX: Access Control Check
    # We compare the Requested ID with the Logged-In ID.
    if int(requested_id) != CURRENT_LOGGED_IN_USER_ID:
        return "❌ 403 FORBIDDEN: You cannot view this profile."
    
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (requested_id,))
    data = cursor.fetchone()
    
    return f"✅ Profile Data: {data}"

if __name__ == '__main__':
    app.run(debug=True, port=5003)