import cv2
import numpy as np

path1 = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar2\\aircraft.jpg"
path2 = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar2\\aircraft1.jpg"

img1 = cv2.imread(path1)
img1 = cv2.resize(img1,(640,550))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(640,550))

img3 = cv2.medianBlur(img1, 7)


'''
#shape metodu ile resimlerin boyutlarini ogrenebiliyoruz
if img1.shape == img2.shape:
    print("Same Size")
else:
    print("Not Same")
'''

# Eger resimlerde bir fark varsa bunlari degiskenlerde depolayacaz daha sonra karsilastirmak icin

# diff = difference
# subtract() fonksiyonu iki resmi karsilastiri ve farkli olan yerlerin rengini degistirir.
# alacagi parametreler karsilastirma yapacagi resimler olur
diff = cv2.subtract(img1, img3)

# diff'i parcalayip tek tek b,g,r degerlerine ulasilir
b,g,r = cv2.split(diff)
print(b) # sifirlardan olusan bir cikti alinir

# countNonZero() fonksiyonu diff icinde 0(sifir) olmayan degerleri bulmayi amaclar
# bu resimde bazi yerlerin farkli oldugu anlamina gelir farklilik varsa siyah olmayan yerler var

if cv2.countNonZero(b) == 0 and  cv2.countNonZero(g) == 0 and  cv2.countNonZero(r) == 0:
    print("Completely Equal")
else:
    print("NOT Completely Equal")


cv2.imshow("difference", diff)
# simsiyah bir ekran gelmesi resimler arasinda hic bir fark olmadigini gösterir.
# ayni olan yerler siyaha farkli ola yerler beyaza boyanir
'''
cv2.imshow("Aircraft",img1)
cv2.imshow("Aircraft1",img2)
'''


cv2.waitKey(0)
cv2.destroyAllWindows()