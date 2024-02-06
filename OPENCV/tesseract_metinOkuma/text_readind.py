from PIL import Image
import pytesseract

img = Image.open("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\tesseract_metinOkuma\\text.png")
text = pytesseract.image_to_string(img,lang="eng")
print(text)