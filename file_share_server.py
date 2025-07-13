from flask import Flask, request, render_template_string, send_from_directory, redirect, url_for, session
import os

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Hardcoded credentials
USERNAME = 'guest'
PASSWORD = 'hostel123'

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>📚 Study Share | File Server</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0D1B2A;
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            margin-top: 30px;
            font-size: 2rem;
            color: #F0F0F0;
        }
        .card {
            background-color: #ffffff;
            color: #333;
            padding: 30px;
            border-radius: 15px;
            margin: 20px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            width: 300px;
        }
        .card h2 { margin-top: 0; color: #0D1B2A; }
        input[type=file] { margin: 10px 0; padding: 5px; }
        input[type=submit] {
            background-color: #1B263B;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        input[type=submit]:hover { background-color: #415A77; }
        .file-list a {
            text-decoration: none;
            color: #1B263B;
            font-weight: bold;
        }
        .file-list a:hover { text-decoration: underline; }
        footer {
            margin-top: 40px;
            font-size: 0.9rem;
            color: #aaa;
        }
    </style>
</head>
<body>
    <h1>📚 Study Share - Hostel File Server</h1>

    <div class="card">
        <h2>Upload a File</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file"><br>
            <input type="submit" value="Upload">
        </form>
    </div>

    <div class="card">
        <h2>Download Files</h2>
        <div class="file-list">
            {% for filename in files %}
                <a href="/download/{{ filename }}">{{ filename }}</a><br>
            {% endfor %}
        </div>
    </div>

    <footer>
        <p>Made with ❤️ for Hostel Sharing | By Samiksha & Dhanashri</p>
    </footer>
</body>
</html>
'''

LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🔒 Login | Study Share</title>
    <style>
        body {
            background-color: #0D1B2A;
            font-family: Arial, sans-serif;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-box {
            background: #ffffff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            color: #333;
        }
        input[type=text], input[type=password] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 6px;
            border: 1px solid #ccc;
        }
        input[type=submit] {
            width: 100%;
            background-color: #1B263B;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
        }
        input[type=submit]:hover {
            background-color: #415A77;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>🔒 Login</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return LOGIN_PAGE + '<p style="color:red;text-align:center;">Incorrect username or password!</p>'
    return LOGIN_PAGE

@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(HTML_PAGE, files=files)

@app.route('/download/<filename>')
def download_file(filename):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

