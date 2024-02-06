import cv2

windowName = "Live Video"
cv2.namedWindow(windowName)

cap = cv2.VideoCapture(0)

print("Width: " + str(cap.get(3)))
print("Height: " + str(cap.get(4)))
# cap.get(3) -> cap'deki goruntunun enini verir "4" yazildiginda da yuksekligini  verir

# get fonksiyonu ile bilgiler alindi ve set fonksiyonu ile de bu alinan bilgiler duzenlenir

# ilk parametre olarak cevirmek istedigimiz ekseni yatay (en) daha sonra cozunurluk degeri girilir
cap.set(3, 1280)
cap.set(4, 720)

# duzenlenmis hali: 
print("Width*: " + str(cap.get(3)))
print("Height*: " + str(cap.get(4)))

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow(windowName,frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()