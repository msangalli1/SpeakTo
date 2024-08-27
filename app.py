from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

# Define el directorio para almacenar los archivos de audio
AUDIO_DIR = '/app/audio_files'

# Crea el directorio si no existe
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text', '')
    if text:
        tts = gTTS(text=text, lang='en')
        file_path = os.path.join(AUDIO_DIR, 'audio.mp3')
        tts.save(file_path)
        return jsonify({'message': 'Audio file created successfully', 'audio_url': f'/audio.mp3'})
    return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
