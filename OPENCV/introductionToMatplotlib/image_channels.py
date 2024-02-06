import numpy as np 
import matplotlib.pyplot as plt 
import cv2

# resimlerin uzerindeki renk yogunluklarinin incelenmesi

path = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\introductionToMatplotlib\\map.jpg"
img = cv2.imread(path)

plt.imshow(img)
plt.show()


'''
[r,g,b]
[50,50,0]   - kirmizi
[70,70,1]   - yesil
[:,:,2]     - mavi

# tum renk degerleri 0 ile 255 arasinda degisiyor

r -> 0 - 255
g -> 0 - 255
b -> 0 - 255
'''

r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

# cekilen renk degerlerini karistirarak orijinal resmi tekrardan elde edebiliyoruz
output = np.dstack((r,g,b))
plt.imshow(output)
plt.show()

output = [img,r,g,b]
titles = ["Image","Red","Green","Blue"]

for i in range(4):     # toplam 4 deger oldugu icin
    # subplot() -> alt grafikler olusturur
    plt.subplot(2,2,i+1)
    # olusan her grafik icin eksenleri kapatacaz
    plt.axis("off")
    # grafiklerin adlari verilir
    plt.title(titles[i])
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap="gray")
    plt.show()




