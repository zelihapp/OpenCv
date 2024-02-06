import cv2
import numpy as np
import requests
url = "http://192.168.237.204:8080//shot.jpg"
while True:
    img_resp = requests.get(url)    #devamli yeni bir frame alinir
                                    # sayfayi her yeniledigimizde yeni bir karenin goruntusunu alir


    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)  #aldigimiz goruntuyu "bytearray" cevirdik

    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)      #hafizadan cektigimiz göruntuyu göruntuleyebilecek hale getirir
                                                       # IMREAD_COLOR: renkli goruntu almamizi saglar
    img = cv2.resize(img, (640,480))             # goruntuyu yeniden boyutlandirmamizi saglar

    cv2.imshow("Android Camera", img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()








