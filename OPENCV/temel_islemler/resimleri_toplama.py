import cv2
import numpy as np

'''
resimleri toplamak icin ayni boyutta olmalilar
cv2.circle(circle, merkez koordinatlari, yaricap, renk, )
resimleri toplamak icin kullanacagimiz fonksiyon
"add" fonksiyonudur. iki parametre alir. 
'''

circle = np.zeros((512, 512, 3), np.uint8) + 255   # beyaz tuval olusturulur
cv2.circle(circle, (256, 256), 60, (255, 0, 0), thickness=-1)

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 155), thickness=-1)

add = cv2.add(circle, rectangle)
print(add[256, 256])




cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Add", add)

cv2.waitKey(0)
cv2.destroyAllWindows()







