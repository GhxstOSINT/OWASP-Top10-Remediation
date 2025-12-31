# Cross-Site Request Forgery (CSRF) Explained

### The Concept

CSRF tricks a logged-in user into performing an unwanted action on a trusted site.

**The Analogy:**
You are wearing a work badge (Session Cookie) that opens doors at your office.
A bad guy tapes a sign on your back that says "Kick me" (The Malicious Link).
You walk past a security guard (The Server), and he kicks you. You authenticated the action with your presence, even though you didn't intend for it to happen.

### The Flaw
Browsers automatically send cookies with every request to a domain. The vulnerable app sees the cookie and assumes the user *intentionally* clicked the "Change Password" button.

### The Fix
**CSRF Tokens:** A secret, random value is hidden in the legitimate form.
When the form is submitted, the server checks if the token is present.
The attacker cannot guess this token, so their fake form (exploit.html) will fail the check.