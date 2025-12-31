### 🔴 File: `13_Brute_Force/explanation.md`

```markdown
# Brute Force Attacks (Authentication Failure) Explained

### The Concept
A Brute Force attack consists of an attacker submitting many passwords or passphrases with the hope of eventually guessing correctly.

**The Analogy:**
Imagine a thief trying to open a combination lock.
* **Vulnerable:** The thief can sit there all day spinning the dial—001, 002, 003... until it opens.
* **Secure:** After 3 wrong guesses, the lock jams and sounds an alarm, preventing any more tries for 15 minutes.



### The Flaw
In `vulnerable_app.py`, the login function allows infinite attempts:
python
# VULNERABLE
if password == REAL_PASSWORD:
    return "Success"
There is no "memory" of previous failures. An attacker can write a script to try 10,000 passwords a second.

The Fix
In secure_app.py, we implement Rate Limiting:

Python

# SECURE
if failed_attempts.get(ip) >= 3:
    return "Account Locked"
We track how many times a specific IP address has failed. Once they cross a threshold, we block them. This makes brute-forcing mathematically impossible because it would take years to try a simple wordlist.