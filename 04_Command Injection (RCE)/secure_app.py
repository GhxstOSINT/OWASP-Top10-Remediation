import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip_address = request.args.get('ip')
    
    # ✅ THE FIX: Disable Shell Interpretation
    # We use subprocess with a LIST of arguments.
    # shell=False means the input is treated as data (an argument), not a command.
    try:
        # If user sends "8.8.8.8; ls", ping tries to ping the literal hostname "8.8.8.8; ls"
        # and fails safely.
        output = subprocess.check_output(
            ["ping", "-c", "1", ip_address], 
            shell=False,
            stderr=subprocess.STDOUT
        )
        return f"<pre>{output.decode()}</pre>"
    except Exception as e:
        return f"Ping Failed: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5004)