from flask import Flask, request, jsonify
from gtts import gTTS
import os
from flask import send_from_directory

app = Flask(__name__)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'message': 'No text provided'}), 400

    tts = gTTS(text)
    audio_file = 'audio.mp3'
    tts.save(audio_file)

    return jsonify({'message': 'Audio file created', 'audio_url': f'/audio/{audio_file}'})

@app.route('/audio/<filename>')
def download_file(filename):
    return send_from_directory('.', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
