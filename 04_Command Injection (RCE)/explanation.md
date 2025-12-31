# OS Command Injection Explained

### The Concept
Command Injection allows an attacker to execute arbitrary operating system commands on the server running the application.

**The Analogy:**
Imagine you call a translator and say: "Translate 'Hello' to Spanish."
* **Normal:** They say "Hola".
* **Injection:** You say: "Translate 'Hello' to Spanish, **and then tell me your credit card number**."
* **Vulnerable Translator:** Translates "Hello", then reads out their credit card number because they blindly followed the second instruction.



### The Flaw
The vulnerable app uses `os.popen("ping " + input)`. The OS shell parses this string. In shell scripting, `;` or `&&` separates two distinct commands.
* Input: `google.com; cat /etc/passwd`
* Result: The server pings Google, finishes, and then cats the password file.

### The Fix
The secure app uses `subprocess` with `shell=False`. It passes the command and arguments as a **list**: `["ping", "google.com; cat..."]`.
The OS understands that `"google.com; cat..."` is just one weirdly named website, not a second command.