# XML External Entity (XXE) Explained

### The Concept
XXE is a flaw in how an application parses XML input. It allows an attacker to interfere with the application's processing of XML data, often allowing them to view files on the application server filesystem.



### The Flaw
XML has a feature called DTD (Document Type Definition) that allows defining custom variables (Entities).
In `vulnerable_app.py`, the parser allows these entities to point to **SYSTEM** paths.
* Attacker defines: `<!ENTITY secret SYSTEM "file:///etc/shadow">`
* Attacker writes: `<data>&secret;</data>`
* Server parses: Replace `&secret;` with the contents of `/etc/shadow`.

### The Fix
In `secure_app.py`, we configure the `XMLParser` to explicitly ignore DTDs and disable entity resolution (`resolve_entities=False`). The parser will throw an error or print the literal text "&secret;" instead of the file content.