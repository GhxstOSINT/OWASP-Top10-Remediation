# 🛡️ OWASP Top 10 Remediation Lab: The Purple Team Portfolio

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green?style=for-the-badge&logo=flask)
![Security](https://img.shields.io/badge/Security-Red%20%26%20Blue%20Team-red?style=for-the-badge)
![OWASP](https://img.shields.io/badge/OWASP-Top%2010-orange?style=for-the-badge)

## 📖 Project Overview

Welcome to the **OWASP Top 10 Remediation Lab**. This project is a hands-on cybersecurity workshop designed to bridge the gap between **Breaking** (Red Team) and **Building** (Blue Team).

In the world of cybersecurity, many beginners learn how to use tools to hack, but few understand the underlying code that makes those hacks possible—and even fewer know how to fix them.

This repository contains **13 distinct security modules**. Each module is a self-contained environment that demonstrates a specific vulnerability from the OWASP Top 10 list.

### 🎯 Learning Objectives
By exploring this repository, you will learn:
1.  **The Anatomy of an Attack:** How hackers exploit logical and syntax errors in code.
2.  **Secure Coding Practices:** How to implement industry-standard defenses (Input Validation, Parameterization, Sanitization).
3.  **Exploit Automation:** How to write Python scripts to verify vulnerabilities programmatically.

---

## 🏗️ How This Project is Structured

Every module folder (e.g., `01_SQL_Injection`) follows the exact same "Kill Chain" structure to make learning easy:

| File | Purpose | Role |
| :--- | :--- | :--- |
| **`vulnerable_app.py`** | A Flask web application intentionally coded with a specific security flaw. | 🛑 **The Victim** |
| **`exploit.py`** | A Python script that automates the attack against the vulnerable app. | ⚔️ **The Weapon** |
| **`secure_app.py`** | The patched version of the app using secure coding best practices. | 🛡️ **The Shield** |
| **`explanation.md`** | A deep-dive text file explaining the theory behind the flaw. | 🧠 **The Theory** |

---

## 🚀 Getting Started Guide

### Prerequisites
* **Python 3.x** installed on your system.
* **Git** installed.

### Installation Steps

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/OWASP-Top10-Remediation.git](https://github.com/YOUR_USERNAME/OWASP-Top10-Remediation.git)
    cd OWASP-Top10-Remediation
    ```

2.  **Install Dependencies**
    We use `Flask` for the web server and `Requests` for the attack scripts.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Initialize the Lab Database**
    Several modules (SQLi, IDOR, CSRF) require a dummy database to simulate real users.
    ```bash
    python setup_db.py
    ```
    *You should see a message: "✅ Database initialized successfully!"*

---

## 📚 Module Guide: The Vulnerabilities Explained

### 01. SQL Injection (SQLi)
* **The Flaw:** The application takes user input (like a username) and pastes it directly into a database query string.
* **The Exploit:** We inject SQL commands (`' OR '1'='1`) to trick the database into revealing all user records.
* **The Fix:** We use **Parameterized Queries**. This ensures the database treats user input strictly as data (text), never as executable code.

### 02. Reflected XSS (Cross-Site Scripting)
* **The Flaw:** The application takes input from the URL (`?q=hello`) and reflects it back to the page HTML without cleaning it.
* **The Exploit:** We inject JavaScript tags (`<script>alert(1)</script>`). When a victim visits the link, the script executes in their browser.
* **The Fix:** We use **Context-Aware Encoding** (via `escape()`). This converts special characters like `<` into safe HTML entities `&lt;`, rendering them harmless.

### 03. IDOR (Insecure Direct Object Reference)
* **The Flaw:** The app uses an ID number (like `?id=100`) to fetch a profile but fails to check if the logged-in user *owns* that ID.
* **The Exploit:** An attacker simply changes the ID in the URL to `101`, `102`, etc., to view other users' private data.
* **The Fix:** We implement an **Ownership Check**. Before returning data, the server compares the requested ID against the currently logged-in user's session ID.

### 04. OS Command Injection (RCE)
* **The Flaw:** The app takes user input (like an IP address) and passes it to a system shell command (like `ping`).
* **The Exploit:** We use command separators (`;` or `&&`) to chain a second malicious command, such as `; ls -la` or `; cat /etc/passwd`.
* **The Fix:** We use the `subprocess` library with `shell=False`. This passes arguments as a list, preventing the Operating System from interpreting special shell characters.

### 05. XML External Entity (XXE)
* **The Flaw:** The application processes XML input using an insecure parser that allows "External Entities" (references to local files).
* **The Exploit:** We send a malicious XML payload defining an entity `&file;` that points to `file:///etc/passwd`, tricking the server into returning the file content.
* **The Fix:** We explicitly **disable DTDs (Document Type Definitions) and Entity Resolution** in the XML parser settings.

### 06. Insecure Deserialization
* **The Flaw:** The app uses Python's `pickle` module to unserialize data (like a cookie) from an untrusted user. `pickle` is capable of executing arbitrary code during the loading process.
* **The Exploit:** We create a malicious Python object with a `__reduce__` method that runs a shell command, serialize it, and send it as a cookie.
* **The Fix:** We replace `pickle` with **JSON**. JSON is a data-only format; it cannot execute code or instantiate arbitrary classes.

### 07. Sensitive Data Exposure
* **The Flaw:** API keys and passwords are "Hardcoded" directly into the python source files. If the code is pushed to GitHub, the secrets are leaked.
* **The Exploit:** Attackers use automated scanners (like TruffleHog) to find specific patterns (e.g., `AWS_ACCESS_KEY`) in public repositories.
* **The Fix:** We use **Environment Variables**. Secrets are stored in a `.env` file (which is ignored by Git) and loaded dynamically at runtime.

### 08. Directory Traversal
* **The Flaw:** The app joins a folder path with a user-provided filename. It doesn't validate if the filename contains "Dot-Dot-Slash" (`../`).
* **The Exploit:** We send a filename like `../../etc/passwd` to climb out of the intended folder and read sensitive system files.
* **The Fix:** We use `secure_filename()` to strip dangerous characters and validate that the final resolved path is inside the allowed directory.

### 09. Server-Side Request Forgery (SSRF)
* **The Flaw:** The app fetches a URL provided by the user (e.g., to check if a site is online). It doesn't check where that URL points.
* **The Exploit:** We force the server to connect to internal resources, such as `http://localhost:5000/admin` or Cloud Metadata services, which are usually blocked from the outside internet.
* **The Fix:** We implement **Allowlisting** (only allow specific domains) and block requests to private IP ranges (localhost, 127.0.0.1, 10.x.x.x).

### 10. Unrestricted File Upload
* **The Flaw:** The app allows users to upload files but trusts the filename extension provided by the user.
* **The Exploit:** We upload a Python script named `exploit.py` (or PHP shell). The server saves it, and we can then visit the URL to execute the script on the server.
* **The Fix:** We validate the file extension against a strict **Allowlist** (e.g., only `.jpg`, `.png`) and rename the file to a random ID upon saving.

### 11. CSRF (Cross-Site Request Forgery)
* **The Flaw:** The server processes important requests (like "Change Password") based solely on the presence of a session cookie, without verifying the *source* of the request.
* **The Exploit:** We trick the victim into visiting a malicious site that contains a hidden form submitting a request to the vulnerable server. The browser automatically sends the victim's cookies, and the action succeeds.
* **The Fix:** We implement **Anti-CSRF Tokens**. A random, secret token is generated for every session and must be included in the form submission. The attacker cannot guess this token.

### 12. Business Logic Flaw
* **The Flaw:** The application relies on the client (the browser) to calculate prices or critical values.
* **The Exploit:** We intercept the request and change the price of an expensive item to "1". The server processes the payment because it trusts the input.
* **The Fix:** We implement a **Server-Side Source of Truth**. The server looks up the price in its own database based on the Item ID, ignoring the price sent by the user.

### 13. Brute Force (Authentication Failure)
* **The Flaw:** The login page allows an unlimited number of incorrect password attempts.
* **The Exploit:** We use a script to try thousands of passwords from a wordlist until one works.
* **The Fix:** We implement **Rate Limiting** and **Account Lockout**. If an IP address fails to login 3 times in a row, we block further attempts for a set period.

---

## ⚠️ Disclaimer
**This project is created for educational purposes only.**
The code provided in the `vulnerable_app.py` files is intentionally insecure.
* **DO NOT** run the vulnerable applications on a public server or production environment.
* **DO NOT** use the exploit scripts against targets you do not have explicit permission to test.

The author is not responsible for any misuse of the information provided in this repository.

---

## 👤 Author
**GhxstOSINT**
* **Role:** Cybersecurity Enthusiast
* **Focus:** Application Security, CTF.
* www.linkedin.com/in/akshxykumxr | github.com/GhxxstOSINT
