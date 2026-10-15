import cv2 as cv
import numpy as np

print("OpenCV:", cv.__version__)
img = np.zeros((120, 400, 3), dtype=np.uint8)
cv.putText(img, "OpenCV OK", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)

recorte = img[50:200, 100:300]
cv.imwrite("crop.png", recorte)

redimension = cv.resize(img, (800,240))
cv.imwrite("redimension.png", redimension)

rotacion = cv.rotate(img, cv.ROTATE_180)
cv.imwrite("rotacion.png", rotacion)