# Server-Side Request Forgery (SSRF) Explained

### The Concept
SSRF allows an attacker to induce the server-side application to make requests to an unintended location. The attacker uses the server as a proxy to access internal systems (like databases, cloud metadata, or internal admin panels) that are not exposed to the internet.



### The Flaw
In `vulnerable_app.py`, the server takes a user-supplied URL and makes a HTTP request to it:
`requests.get(user_input)`
The server blindly trusts that the user wants to visit a public website (like google.com), but fails to stop the user from asking for `localhost` or `169.254.169.254` (AWS Metadata).

### The Fix
Implement strict **Allowlisting**.
1.  Check the hostname against a list of known good domains if possible.
2.  If you must allow arbitrary URLs, parse the URL and block private IP ranges (Loopback, 10.0.0.0/8, 192.168.0.0/16).