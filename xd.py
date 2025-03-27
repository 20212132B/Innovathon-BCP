import pytesseract

# Especificar la ruta completa a tesseract si no está en el PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Procesar una imagen (ejemplo)
from PIL import Image
img = Image.open(r'C:\Users\natal\Downloads\Certificado cyberops.png')
text = pytesseract.image_to_string(img)

print(text)