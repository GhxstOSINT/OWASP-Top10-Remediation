from flask import Flask, request

app = Flask(__name__)
# User's wallet
balance = 100

@app.route('/buy', methods=['POST'])
def buy_item():
    global balance
    item = request.form.get('item')
    # 🛑 THE VULNERABILITY:
    # The price is sent BY THE USER from the frontend form.
    # The server trusts that the user didn't change the hidden field.
    price = int(request.form.get('price'))
    
    if balance >= price:
        balance -= price
        return f"✅ Purchased {item} for ${price}. New Balance: ${balance}"
    else:
        return "❌ Insufficient Funds"

if __name__ == '__main__':
    app.run(debug=True, port=5012)