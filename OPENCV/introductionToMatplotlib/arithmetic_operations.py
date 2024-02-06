import numpy as np 
import matplotlib.pyplot as plt 


img = plt.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\introductionToMatplotlib\\map.jpg")

# alt grafikler olusturmak icin subplot() fonksiyonu kullanilir
# ilk iki parametre grafigin kac satir ve sutundan olustugunu soyluyor
# 3.parametrede grafigin hangi siraya girilecegini söyler
plt.subplot(3,2,1)
plt.title("Image")
plt.imshow(img)


# resimlerin renk degerleri toplanir
plt.subplot(3,2,2)
plt.title("img+img")
plt.imshow(img+img)


# resimlerin renk degerleri cikarilir 0 elde edilir siyah bir ekran olusur
plt.subplot(3,2,3)
plt.title("img-img")
plt.imshow(img-img)


# goruntunun x ve y eksenine göre yansimalari elde edilir
plt.subplot(3,2,4)
np.flip("np.flip")
# 0 -> x eksenine gore yansima alir
plt.imshow(np.flip(img,0))

plt.subplot(3,2,4)
np.flip("np.flip")
# 1 -> y eksenine gore yansima alir
plt.imshow(np.flip(img,1))


plt.subplot(3,2,4)
np.flip("np.flip")
# renk formati degisir yansima almaz
plt.imshow(np.flip(img,2))

'''
# fliplr -> left to right
plt.subplot(3,2,4)
np.fliplr("np.flip")
plt.imshow(np.fliplr(img,2))

# flipud -> up to down 
plt.subplot(3,2,4)
np.flipud("np.flip")
plt.imshow(np.flipud(img,2))
'''

plt.show()
