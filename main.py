from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\tutej\AppData\Local\Tesseract-OCR\tesseract.exe'
img = Image.open('hello.png')
result = pytesseract.pytesseract.image_to_string(img)
print(result)
