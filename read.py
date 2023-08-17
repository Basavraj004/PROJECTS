import cv2 as cv
from numpy import true_divide
## reading image
#img=cv.imread('imgs/WIN_20220714_21_02_18_Pro.jpg')

#cv.imshow('ludo',img)

# reading video
capture=cv.VideoCapture('videos/basic2.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow ('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
