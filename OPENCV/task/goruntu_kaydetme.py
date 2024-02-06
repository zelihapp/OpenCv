import cv2

# videonun acilmasini saglar
video = cv2.VideoCapture("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\task\\yaziyazdirma.mp4")

# video oynatilir
while video.isOpened():
    # Birkaç kare okunur
    ret, frame = video.read()

    # eger videonun sonuna gelirse çıkış yapar
    if not ret:
        break

    cv2.imshow('Video', frame)

    # Klavyeden "q" harfi girildiginde videodan cikis yapar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # eger 's' tuşuna basılirsa o anki goruntuyu kaydeder
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('kaydedilen_goruntu.jpg', frame)
        print('Görüntü kaydedildi.')

video.release()
cv2.destroyAllWindows()