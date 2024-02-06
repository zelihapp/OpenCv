# farenin tiklandigi yerde bir tiklanilan yer merkez olacak sekilde bir cember cizilmesi icin:

import cv2

cap = cv2.VideoCapture("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar1\\car.mp4")
circles = []

# event fare olaylarini tutar , x ve y cemberin merkez noktalarini tutar, diger iki degisken kullanilmiyor
def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))


cv2.namedWindow("Frame")
# setMouseCallback -> islemler frame uzerinden oldugu icin fonksiyona ilk "Frame" parametresi verilir
# 2.parametre olarak yapilan islemi tanimlamak icin de bir fonksiyon girilmeli (saga mi basiliyor sola mi basiliyor
# yukari veya asagi mi gibi)
cv2.setMouseCallback("Frame", mouse)

while 1:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    for center in circles:
        cv2.circle(frame, center, 20, (255, 0, 0), -1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("h"):
        circles = []

cap.release()
cv2.destroyAllWindows()