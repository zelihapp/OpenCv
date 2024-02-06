import cv2

vid = cv2.VideoCapture("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\face_detection\\faces.mp4")
face_cascade = cv2.CascadeClassifier("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\face_detection\\haarcascade_frontalface_default.xml")

# videodaki her bir framei yani goruntuyu tek tek okuyup gri tona donusturup uzerinde yuz arayacaz

# Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevrilir
# cascade dosyasini kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
# "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
while 1:
    _ ,frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.4, 1)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("image", frame)
    
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()