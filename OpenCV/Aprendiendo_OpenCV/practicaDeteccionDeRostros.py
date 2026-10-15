import cv2 as cv

print(cv.__file__)
print(cv.__version__)
# Cargamos el clasificador UNA sola vez, antes del bucle
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

if face_cascade.empty():
    print("No se pudo cargar el clasificador de rostros")
    exit()

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer el cuadro")
        break

    # El clasificador trabaja sobre la imagen en escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detectamos los rostros (scaleFactor=1.1, minNeighbors=4)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Dibujamos un rectángulo azul sobre cada rostro, en el cuadro a color
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow("Video", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()