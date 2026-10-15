import cv2 as cv
import sys
import os

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir")
    exit()
while True:
    ret, frame = cap.read()
    
    if not ret: 
        print("No se pudo leer el cuadro")
        break
    cv.imshow("Video", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()