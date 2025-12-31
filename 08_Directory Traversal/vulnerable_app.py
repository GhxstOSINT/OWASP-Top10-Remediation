import os
from flask import Flask, request, send_file

app = Flask(__name__)

# Create a dummy folder for reports
if not os.path.exists('reports'):
    os.makedirs('reports')
    with open('reports/daily.txt', 'w') as f:
        f.write("This is a public report.")

@app.route('/download')
def download():
    filename = request.args.get('file')
    
    # 🛑 THE VULNERABILITY:
    # We blindly join the 'reports' folder with the user's input.
    # If the user sends "../main.py", we step out of the folder.
    # Path becomes: reports/../main.py
    file_path = os.path.join("reports", filename)
    
    try:
        return send_file(file_path)
    except FileNotFoundError:
        return "File not found"

if __name__ == '__main__':
    app.run(debug=True, port=5008)