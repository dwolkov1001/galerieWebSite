# Основной файл приложения Flask для галереи изображений

from flask import Flask, render_template, request, redirect, url_for, flash, session
import database
import os
from werkzeug.utils import secure_filename
from PIL import Image
from math import ceil
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

app = Flask(__name__)

# Конфигурация приложения
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB

# Разрешённые форматы изображений
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY', app.config['SECRET_KEY'])
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_FROM = os.environ.get('EMAIL_FROM', EMAIL_HOST_USER)

def allowed_file(filename):
    """Проверка разрешённого формата файла"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_image(file_path):
    """Проверка, что файл действительно является изображением"""
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception:
        return False

def send_reset_email(to_email, token):
    reset_url = url_for('reset_password', token=token, _external=True)
    subject = 'Password Reset for Image Gallery'
    body = f"""Hello!

To reset your password, click the link below:
{reset_url}

If you did not request a password reset, just ignore this email."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = to_email
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            if EMAIL_USE_TLS:
                server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_FROM, [to_email], msg.as_string())
        return True
    except Exception as e:
        print('Email send error:', e)
        return False

token_serializer = URLSafeTimedSerializer(SECRET_KEY)

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    page = request.args.get('page', 1, type=int)
    per_page = 12
    all_images = [img for img in database.get_all_images() if img['user_id'] == session['user_id']]
    total = len(all_images)
    pages = ceil(total / per_page) if total else 1
    start = (page - 1) * per_page
    end = start + per_page
    images = all_images[start:end]
    return render_template('index.html', images=images, page=page, pages=pages, total=total)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        flash('Please log in to upload images.', 'error')
        return redirect(url_for('login'))
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected.', 'error')
            return redirect(request.url)
        file = request.files['file']
        caption = request.form.get('caption', '').strip()
        if file.filename == '':
            flash('No file selected.', 'error')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('Invalid file format. Allowed: PNG, JPG, JPEG, GIF', 'error')
            return redirect(request.url)
        try:
            filename = secure_filename(file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            if not validate_image(file_path):
                os.remove(file_path)
                flash('File is corrupted or not an image.', 'error')
                return redirect(request.url)
            image_id = database.add_image(filename, caption, session['user_id'])
            flash(f'Image "{filename}" uploaded successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error uploading file: {str(e)}', 'error')
            return redirect(request.url)
    return render_template('upload.html')

@app.route('/delete/<int:image_id>', methods=['POST'])
def delete_image(image_id):
    if 'user_id' not in session:
        flash('Please log in to delete images.', 'error')
        return redirect(url_for('login'))
    image = database.get_image_by_id(image_id)
    if not image or image['user_id'] != session['user_id']:
        flash('Image not found or access denied.', 'error')
        return redirect(url_for('index'))
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], image['filename'])
    error = None
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        error = f'Error deleting file: {str(e)}'
    try:
        database.delete_image(image_id)
    except Exception as e:
        error = f'Error deleting from database: {str(e)}'
    if error:
        flash(error, 'error')
    else:
        flash('Image deleted successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        password2 = request.form.get('password2', '')
        if not username or not password or not password2:
            flash('Username and password are required.', 'error')
            return redirect(request.url)
        if password != password2:
            flash('Passwords do not match.', 'error')
            return redirect(request.url)
        if database.get_user_by_username(username):
            flash('Username already exists.', 'error')
            return redirect(request.url)
        # email не обязателен, проверку уникальности не делаем если пусто
        if email and database.get_user_by_email(email):
            flash('Email already registered.', 'error')
            return redirect(request.url)
        password_hash = generate_password_hash(password)
        user_id = database.add_user(username, email if email else None, password_hash)
        if user_id:
            session['user_id'] = user_id
            session['username'] = username
            flash('Registration successful! You are now logged in.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Registration failed. Try again.', 'error')
            return redirect(request.url)
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        user = database.get_user_by_username(username)
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(request.url)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/forgot', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        user = database.get_user_by_email(email)
        if not user:
            flash('No user with this email.', 'error')
            return redirect(request.url)
        token = token_serializer.dumps(user['id'], salt='reset-password')
        if send_reset_email(email, token):
            flash('Password reset instructions sent to your email.', 'success')
        else:
            flash('Failed to send email. Contact support.', 'error')
        return redirect(url_for('login'))
    return render_template('forgot.html')

@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        user_id = token_serializer.loads(token, salt='reset-password', max_age=3600)
    except Exception:
        flash('Invalid or expired reset link.', 'error')
        return redirect(url_for('login'))
    if request.method == 'POST':
        password = request.form.get('password', '')
        password2 = request.form.get('password2', '')
        if not password or not password2:
            flash('All fields are required.', 'error')
            return redirect(request.url)
        if password != password2:
            flash('Passwords do not match.', 'error')
            return redirect(request.url)
        password_hash = generate_password_hash(password)
        database.update_user_password(user_id, password_hash)
        flash('Password has been reset. You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('reset.html')

@app.route('/image/<int:image_id>')
def view_image(image_id):
    image = database.get_image_by_id(image_id)
    if not image or (image['user_id'] != session.get('user_id')):
        flash('Image not found or access denied.', 'error')
        return redirect(url_for('index'))
    owner = database.get_user_by_id(image['user_id'])
    return render_template('image.html', image=image, owner=owner)

if __name__ == '__main__':
    app.run(debug=True) 