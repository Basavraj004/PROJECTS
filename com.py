
import cv2 as cv
from PIL import Image 
from pytesseract import pytesseract

print('Enter 1 for text detextion and 2 for face detection`')
n=int(input('Enter choice'))

if n==1:

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

if n==2:
# Load the cascade
    face_cascade = cv.CascadeClassifier('harr_frontal.xml')

# To capture video from webcam. 
cap = cv.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscaleFGHJKL;'
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=9)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv.imshow('img', img)

    # Stop if escape key is pressed
    k = cv.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()


