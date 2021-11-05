import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'tes/tesseract.exe'
img = Image.open("베트남기사.png")
text = pytesseract.image_to_string(img, lang="vie")
print(text)