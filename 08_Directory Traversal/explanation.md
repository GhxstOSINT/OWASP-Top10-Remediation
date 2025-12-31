# Directory Traversal Explained

### The Concept

Directory Traversal (or Path Traversal) allows an attacker to read files outside the directory the application intended to access. It relies on the relative path notation `../` which means "go up one folder".

### The Flaw
The application uses user input to construct a file path without validation:
`open("reports/" + "../secrets.txt")`
The filesystem resolves this to just `secrets.txt`, bypassing the "reports" restriction.

### The Fix
Always use a library function like `secure_filename()` to strip path characters (`/` or `\`) from the input. Additionally, resolve the absolute path and verify it starts with the expected directory root.