# Reflected Cross-Site Scripting (XSS) Explained

### The Concept
Reflected XSS occurs when an application receives data in an HTTP request (like a search term in the URL) and includes that data within the immediate response in an unsafe way. The script is "reflected" off the web server and executed in the victim's browser.

**The Analogy:**
Imagine a parrot that repeats everything you say.
* **Normal usage:** You say "Hello", Parrot says "Hello".
* **Attack usage:** You say "Attack the owner", and the Parrot attacks the owner because it doesn't understand context—it just repeats the command.



### The Flaw
In `vulnerable_app.py`, the code looks like this:
```python
# VULNERABLE
return f"<h1>You searched for: {query}</h1>"

```

The browser trusts whatever the server sends. If the server sends `<script>alert(1)</script>`, the browser thinks it is valid code provided by the website developers and executes it. The server failed to distinguish between **User Text** and **Executable Code**.

### The Fix

In `secure_app.py`, we use **Context-Aware Encoding**:

```python
# SECURE
safe_query = escape(query)
return f"<h1>You searched for: {safe_query}</h1>"

```

The `escape()` function converts special characters into HTML Entities before sending them to the browser:

* `<` becomes `&lt;`
* `>` becomes `&gt;`
* `"` becomes `&quot;`
* `'` becomes `&#x27;`

When the browser sees `&lt;script&gt;`, it knows to display the text characters "<script>" on the screen, but it **does not execute them** as code.