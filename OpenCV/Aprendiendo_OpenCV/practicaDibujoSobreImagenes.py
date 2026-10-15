import cv2 as cv
import numpy as np

img = cv.imread("starry_night.jpg")


cv.line(img, (0,0), (200,200), (255,0,0), 3)
cv.rectangle(img, (50,50), (150,150), (0,255,0), 2)
cv.circle(img, (100,100), 50, (0,0,255), -1)
cv.putText(img, "Texto", (50,50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv.imwrite("dibujos.png", img)
