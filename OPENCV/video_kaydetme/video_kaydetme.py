import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fileName = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\eye_detection\\webcam.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
frameRate = 30
resolution = (640, 480)




videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)


# VideoWriter(): 4 parametre alir ilki dosyanin adidir dosyasi bulundufumuz klasore kaydettik.
# ikinci parametre ise "codec" parametresidir. videolar ses ve goruntulerden olusur ve biz bu ses
# ve goruntuleri birlestirmek icin cesitli algoritmalar kullaniriz. codec dedigimiz kod cozuculerde
# bu algoritmalari tanirlar dolasisiyla videomu dogru bir sekilde kaydetmek icin codec degerinin
# girmemiz gerekir.
# ucuncu girecegimiz parametre ise frame parametresidir.ekrana yansıyan her şey akıcı olacak
# ve görüntüde takılmalar en az seviyede gerçekleşecektir. (?)
# 4.parametrede solution (cozunurluk) parametresidir



while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)   # her frame'i kaydetmesi icin


    cv2.imshow("Webcam Live", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# videolari isledikten sonra serbest birakmamiz gerekiyor
videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()


