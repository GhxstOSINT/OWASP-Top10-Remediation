import os
from flask import Flask, request

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        
        # 🛑 THE VULNERABILITY:
        # The app saves the file exactly as the user named it.
        # If I upload 'exploit.py' or 'shell.php', the server saves it as executable code.
        # I can then visit /uploads/exploit.py to run it.
        if file.filename == '':
            return 'No selected file'
            
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return f'File uploaded! Access it at /uploads/{file.filename}'
        
    return '''
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# Route to serve (and execute) the uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # In a real PHP/Apache server, visiting a .php file would run it.
    # In Flask, we just return the content, but the principle is the same.
    return "File execution would happen here on a vulnerable server."

if __name__ == '__main__':
    app.run(debug=True, port=5010)