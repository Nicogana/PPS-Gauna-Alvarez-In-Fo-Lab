import cv2 as cv
import sys
import os
print(os.path.getsize("starry_night.jpg"))
with open("starry_night.jpg","rb") as f:
    header = f.read(50)
print(header)
img = cv.imread("starry_night.jpg")
if img is None:
    sys.exit("No se pudo leer la imagen.")

cv.imshow("Ventana", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
cv.destroyAllWindows()
flipped = cv.flip(img, 1)
if flipped is None:
    sys.exit("No se pudo leer la imagen.")
cv.imshow("Ventana 2", flipped)
k = cv.waitKey(0)
cv.destroyAllWindows()
blur = cv.GaussianBlur(img, (5,5),0)
if blur is None:
    sys.exit("No se pudo leer la imagen.")
cv.imshow("Ventana 3", blur)
k = cv.waitKey(0)
cv.destroyAllWindows()