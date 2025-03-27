import os
from flask import Flask, request, jsonify, render_template
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


app = Flask(__name__)

# Ruta principal de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar la imagen
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Abrir y procesar la imagen
        image = Image.open(file)
        extracted_text = pytesseract.image_to_string(image)
        alert_message = analyze_text(extracted_text)

        return jsonify({'extracted_text': extracted_text, 'alert': alert_message})

    except Exception as e:
        return jsonify({'error': str(e)})

def analyze_text(text):
    suspicious_phrases = ['apoya a tu familia', 'tu cuenta será bloqueada', 'urgente', 'no compartas tus datos', 'Descarg']
    for phrase in suspicious_phrases:
        if phrase.lower() in text.lower():
            return '¡Alerta! Este mensaje parece ser un intento de manipulación emocional.'

    return 'Este mensaje parece seguro.'

if __name__ == '__main__':
    app.run(debug=True)
