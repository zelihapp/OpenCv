
import numpy as np
import matplotlib.pyplot as plt

'''
N = 11
# linspace() fonksiyonu girilen aralikta veri uretmesini saglar (0 ile 10 arasinda)
# N toplam 11 sayi verir -> gormek istedigimiz veri sayisi
x = np.linspace(0,10,N)

y = x
plt.plot(x,y,"o--")
# grafigin eksenlerinin yok etmek icin axis("off") fonksiyonu kullanilir
plt.axis("off")
plt.show()
'''

# bir veri listesi olusturduk (x)
x = [9,5,7,3]
# y eksenindeki verileri de x den alir x deki verilerin 2 kati (81,25,49,9) 
plt.plot(x,[y**2 for y in x])
plt.show()