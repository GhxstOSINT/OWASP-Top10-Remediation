from flask import Flask, request

app = Flask(__name__)
balance = 100

# ✅ THE FIX: Source of Truth
# Prices are stored on the server, not trusted from the client.
PRICES = {
    "iphone": 1000,
    "candy": 1
}

@app.route('/buy', methods=['POST'])
def buy_item():
    global balance
    item = request.form.get('item')
    
    # 1. Look up the REAL price
    if item not in PRICES:
        return "Item not found"
    
    real_price = PRICES[item]
    
    if balance >= real_price:
        balance -= real_price
        return f"✅ Purchased {item} for ${real_price}. New Balance: ${balance}"
    else:
        return f"❌ Insufficient Funds. Cost: ${real_price}"

if __name__ == '__main__':
    app.run(debug=True, port=5012)