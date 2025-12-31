# Sensitive Data Exposure Explained

### The Concept
This vulnerability occurs when an application inadvertently exposes sensitive data, such as passwords, session tokens, or credit card data. The most common cause for beginners is **Hardcoded Secrets**.

**The Analogy:**
* **Vulnerable:** You write your ATM PIN code on the back of your debit card. Anyone who sees the card sees the secret.
* **Secure:** You memorize the PIN. It exists in your mind (Environment), not written on the physical object (Source Code).

### The Flaw
In `vulnerable_app.py`, the variables are defined as strings:
python
AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE"
When you work on a team, you use git to save your code. If you commit this file, that key is now permanently recorded in the project's history. Hackers scrape GitHub constantly looking for strings starting with AKIA to steal cloud resources for crypto mining.

### The Fix
```In secure_app.py, we use the DotEnv pattern:
Create a file named .env and put the secrets there.
Add .env to your .gitignore file.
Use os.getenv() in Python to read the values.
This way, the secure_app.py file can be shared publicly, but the .env file stays on your private computer.

