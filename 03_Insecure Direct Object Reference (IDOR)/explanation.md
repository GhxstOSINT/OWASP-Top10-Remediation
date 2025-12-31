# Insecure Direct Object Reference (IDOR) Explained

### The Concept
IDOR is a type of access control failure. It occurs when an application exposes a reference to an internal implementation object (like a database key, file ID, or account number) in the URL or API, but fails to verify that the user making the request actually **owns** that object.

**The Analogy:**
Imagine a hotel where the room keys are just simple metal keys with the room number stamped on them.
* **IDOR:** You are staying in Room 100. You walk up to Room 101, insert a key stamped "101", and the door opens. The lock only checked if the *key* fit, not if *you* were the guest assigned to that room.
* **Secure:** You swipe a digital card. The system checks: "Is this card assigned to Room 101?" If not, access is denied.



### The Flaw
In `vulnerable_app.py`, the code blindly trusts the input:
```python
# VULNERABLE
user_id = request.args.get('id')
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
The application assumes that if you possess the ID (e.g., ?id=1), you are authorized to see it. It essentially asks the database: "Does ID #1 exist?" instead of asking "Does the current user own ID #1?"

The Fix
In secure_app.py, we add an Authorization Check:

Python

# SECURE
# 1. Identify who is logged in (usually via session)
current_user = 2 

# 2. Compare the requested resource with the logged-in user
if int(requested_id) != current_user:
    return "403 Forbidden"
This forces the application to validate permission before fetching the data. Even if the hacker changes the URL to ?id=1, the server sees they are actually User 2, detects the mismatch, and blocks the request.


**Would you like me to generate the files for Module 4 (Command Injection) next?**