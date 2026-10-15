import cv2 as cv
import numpy as np

img = cv.imread("starry_night.jpg")

gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite("gris.png", gris)


# Binarizar la imagen (blanco y negro)
_, threshold = cv.threshold(
    gris,
    127,
    255,
    cv.THRESH_BINARY
)

# Aplicar desenfoque
desenfoque = cv.GaussianBlur(
    img,
    (5, 5),
    0
)

# Desenfoque sobre la imagen en escala de grises
desenfoque_gris = cv.GaussianBlur(
    gris,
    (5, 5),
    0
)

# Detectar bordes
bordes = cv.Canny(
    desenfoque_gris,
    50,
    150
)

# Mostrar resultados
cv.imshow("Original", img)
cv.imshow("Grises", gris)
cv.imshow("Threshold", threshold)
cv.imshow("Desenfoque", desenfoque)
cv.imshow("Bordes", bordes)

# Esperar hasta presionar una tecla
cv.waitKey(0)

# Cerrar todas las ventanas
cv.destroyAllWindows()