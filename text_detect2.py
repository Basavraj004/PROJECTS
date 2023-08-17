import cv2 as cv
from PIL import Image 
from pytesseract import pytesseract

camera=cv.VideoCapture(0)


while True:
    _,image=camera.read()
    cv.imshow('text detection',image)
    if cv.waitKey(1) & 0xFF==ord('s'):
        cv.imwrite('test1.jpg',image)
        break
camera.release()
cv.destroyAllWindows()

def tesseract():
    path_to_tesseract=r"c:\Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath='test1.jpg'
    pytesseract.tesseract_cmd=path_to_tesseract
    text=pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])
tesseract()
