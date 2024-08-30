from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess
import signal

app = Flask(__name__)

# Global variable to store the current speech process
current_speech_process = None

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = file.filename
        file.save(filename)
        
        try:
            result = subprocess.run(['tesseract', filename, 'stdout'], capture_output=True, text=True)
            os.remove(filename)  # Clean up the temporary file
            return jsonify({'text': result.stdout})
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/speak', methods=['POST'])
def speak_text():
    global current_speech_process
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'})
    
    text = data['text']
    
    try:
        # Stop any ongoing speech process
        if current_speech_process:
            current_speech_process.terminate()
            current_speech_process.wait()

        # Start a new speech process
        current_speech_process = subprocess.Popen(['say', text])
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/stop_speak', methods=['POST'])
def stop_speak():
    global current_speech_process
    if current_speech_process:
        try:
            current_speech_process.terminate()
            current_speech_process.wait()
            current_speech_process = None
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
