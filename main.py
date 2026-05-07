import pytesseract
from PIL import Image
from pytesseract import image_to_string

# якщо PATH не налаштований, розкоментуй:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = image_to_string(Image.open("text.png"))
print(text)

