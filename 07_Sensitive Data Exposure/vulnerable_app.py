from flask import Flask

app = Flask(__name__)

# 🛑 THE VULNERABILITY:
# Hardcoding secrets directly in the source code.
# If you push this file to GitHub, the entire world sees your database password.
# Even if you delete it later, it remains in the Git "Commit History".

DB_PASSWORD = "SuperSecretPassword123!"
AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE"

@app.route('/connect')
def connect_db():
    # Simulating a database connection using the hardcoded secret
    if DB_PASSWORD == "SuperSecretPassword123!":
        return f"✅ Connected to Database! (Using insecure key: {AWS_API_KEY})"
    else:
        return "❌ Connection Failed"

if __name__ == '__main__':
    app.run(debug=True, port=5007)