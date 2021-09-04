from pytesseract import pytesseract
from PIL import Image

def imgTotext(image):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # Opening the image & storing it in an image object
    img = Image.open(image)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    a = text[:-1]
    # print(text[:-1])
    return a
