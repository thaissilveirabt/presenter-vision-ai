import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao acessar a câmera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Teste Camera", frame)

    tecla = cv2.waitKey(1)

    if tecla == 27:
        break

cap.release()
cv2.destroyAllWindows()