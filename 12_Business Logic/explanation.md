# Business Logic Flaws (Insecure Design) Explained

### The Concept
Business Logic vulnerabilities are not about broken code or syntax errors. They are about broken **rules**. The code works exactly as written, but the developer made a mistake in how the business process should function, allowing users to do things they shouldn't (like buying an item for $0).

**The Analogy:**
Imagine a self-checkout machine at a grocery store.
* **Secure:** The machine scans the barcode and looks up the price in the store's database.
* **Vulnerable:** You put a sticker on a TV that says "Price: $1.00". The machine reads your sticker and charges you $1.00 because it trusts the label you provided.



### The Flaw
In `vulnerable_app.py`, the server trusts the user to tell it how much the item costs:
python
# VULNERABLE
price = int(request.form.get('price'))
if balance >= price:
    balance -= price
Attackers can use tools like Burp Suite or Python to change the price in the HTTP request to "1" or even negative numbers (to add money to their wallet!).

The Fix
In secure_app.py, the server ignores the price sent by the user. It uses a Source of Truth:

Python

# SECURE
PRICES = {"iphone": 1000}
real_price = PRICES[item]
The server only looks at what item the user wants, then looks up the price itself. The user's input regarding "price" is discarded entirely.