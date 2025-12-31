import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ THE FIX: Allowlisting extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        # 1. Check extension
        if file and allowed_file(file.filename):
            
            # 2. Sanitize the name (removes special chars)
            filename = secure_filename(file.filename)
            
            # 3. (Bonus) Rename it entirely to a random UUID to prevent overwriting
            # import uuid; filename = str(uuid.uuid4()) + ".jpg"
            
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return '✅ File uploaded safely.'
        else:
            return '❌ Invalid file type! Only images allowed.'
            
    return '<form method=post enctype=multipart/form-data><input type=file name=file><input type=submit></form>'

if __name__ == '__main__':
    app.run(debug=True, port=5010)