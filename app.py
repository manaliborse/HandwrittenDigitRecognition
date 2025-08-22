from flask import Flask, render_template, request, redirect, url_for, session
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'abc123'

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    message = None
    if 'webcam_started' in session:
        message = "Webcam detection started. Please look at the separate window."
        session.pop('webcam_started', None)
    return render_template('index.html', message=message)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return render_template('index.html', filename=file.filename)
    return redirect(url_for('index'))

@app.route('/recognize', methods=['POST'])
def recognize():
    filename = request.form['filename']
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Run the digit recognition script with uploaded image
    subprocess.run(['python', 'mnist_tflite_detection.py', img_path])
    
    # Return result images
    return render_template('index.html', filename=filename, result='05-mnist-detection.jpg')

@app.route('/start-webcam', methods=['POST'])
def start_webcam():
    # Start webcam detection script
    subprocess.Popen(['python', 'mnist_tflite_live_detection.py'])

    # Set a flag in session to show the message
    session['webcam_started'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
