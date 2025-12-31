import os
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/download')
def download():
    filename = request.args.get('file')
    
    # ✅ THE FIX: Sanitize the Filename
    # 1. secure_filename() strips paths like "../" and returns just the name.
    #    "../../etc/passwd" becomes "etc_passwd" (safe).
    safe_name = secure_filename(filename)
    
    # 2. Force the path to be the absolute path of the intended folder
    reports_dir = os.path.abspath("reports")
    file_path = os.path.join(reports_dir, safe_name)
    
    # 3. Double Check: Ensure the final path is actually inside reports_dir
    # (This prevents trickery even if secure_filename fails)
    if not file_path.startswith(reports_dir):
        return "❌ Access Denied: Invalid Path"
        
    try:
        return send_file(file_path)
    except FileNotFoundError:
        return "File not found"

if __name__ == '__main__':
    app.run(debug=True, port=5008)