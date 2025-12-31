# Unrestricted File Upload Explained

### The Concept

Many websites allow users to upload avatars or documents. If the server does not validate the file content, an attacker can upload a script (like `.php`, `.asp`, `.py`) instead of an image.

### The Flaw
The vulnerable app blindly accepts `file.save(user_filename)`.
If an attacker uploads `web_shell.php` and the server is configured to run PHP, the attacker can simply visit `website.com/uploads/web_shell.php` to take full control of the server.

### The Fix
1.  **Allowlisting:** Only allow specific extensions (`.jpg`, `.png`).
2.  **Renaming:** Never keep the user's filename. Rename the file to a random ID (e.g., `image_12345.jpg`).
3.  **Content Check:** Validate the "Magic Bytes" (file header) to ensure it really is an image, not just a script renamed to `.jpg`.