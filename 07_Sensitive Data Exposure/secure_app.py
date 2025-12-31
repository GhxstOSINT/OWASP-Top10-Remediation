import os
from flask import Flask
from dotenv import load_dotenv

# ✅ THE FIX: Environment Variables
# 1. We load variables from a hidden file called '.env'
# 2. We add '.env' to our '.gitignore' file so it NEVER gets uploaded to GitHub.
load_dotenv() 

app = Flask(__name__)

# We fetch the secrets from the Operating System environment, not the code.
DB_PASSWORD = os.getenv("DB_PASSWORD")
AWS_API_KEY = os.getenv("AWS_API_KEY")

@app.route('/connect')
def connect_db():
    if not DB_PASSWORD:
        return "❌ Error: Configuration missing. Did you create the .env file?"
        
    if DB_PASSWORD == "SuperSecretPassword123!":
        return f"✅ Connected Safely! (Key loaded from env: {AWS_API_KEY})"
    else:
        return "❌ Connection Failed"

if __name__ == '__main__':
    app.run(debug=True, port=5007)