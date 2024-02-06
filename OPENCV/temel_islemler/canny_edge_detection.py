import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1) #flip goruntuyu ters ceviriyor , 1 y eksenine gore degistirir

    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow("frame", frame)
    cv2.imshow("edges",edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

#Canny fonksiyonu 3 adet parametre alir ( input (kenarlarini arayacagimiz resim) ,  minThreshold, maxThreshold )

