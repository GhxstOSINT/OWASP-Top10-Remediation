import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip_address = request.args.get('ip')
    
    # 🛑 THE VULNERABILITY:
    # Passing user input directly to the system shell.
    # The shell sees ";" as a separator between commands.
    # Input: 8.8.8.8; ls
    # Executed: ping -c 1 8.8.8.8; ls
    command = f"ping -c 1 {ip_address}"
    
    # os.popen executes the command string in the shell
    stream = os.popen(command)
    output = stream.read()
    
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.run(debug=True, port=5004)