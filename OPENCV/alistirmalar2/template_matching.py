import cv2
import numpy as np

image_path = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar2\\starwars.jpg"
template_path = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar2\\starwars2.jpg"

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE) # ikinci parametre resmi griye cevirir
w,h = template.shape[::-1]
#print(template.shape) -> resmin gri formatta oldugunu söylüyor. chanel degeri yok (bgr galiba?)


# cv2.matchTemplate() -> fonksiyonu bir sablonun orijinal resim icerisinde mevcut olup olmadigini kontrol eder
# 3 parametre alir . ilk parametre degeri sablonun yerlestirilecegi resimdir
# 2.parametre degeri sablondur . son parametre ise varsayilan olarak girdigimiz degiskendir.
result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

location = np.where(result >= 0.95)

for point in zip(*location[::-1]):
    cv2.rectangle(img, point, (point[0]+w, point[1]+h), (0, 255, 0), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
