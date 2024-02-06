import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3)

plt.plot(x,[y**2 for y in x])
plt.plot(x,[y**3 for y in x])
plt.plot(x,2*x)
plt.plot(x, 5.2*x)

# yapilan cizimlerin hangisine ait oldugu yazilir karisikligi engeller (hangi cizginin hangi verilere ait oldugu)
# legend() -> loc, locationdan gelir cizgilerin hangisine ait oldugunu gösteren pencere icin kullanilir 
# ust sol icin herhangi bir sey yazmaya gerek yok digerleri icin ise  -> upper right/center/left, lower right/center/left
plt.legend(['x**2','x**3','x*2','x*5.2'],loc='lower right') 
# grid() fonksiyonu ile grafigin üzerine izgaralar ekleyebiliyoruz
# print(plt.axis()) -> en buyuk ve en kucuk veriyi gosterir
plt.grid(True)
# x eksenine verilerin nereden geldigini hangi fonksiyondan geldigini gösterir
plt.xlabel('x = np.arange(3)')
# y eksenine verilerin nereden geldigini hangi fonksiyondan geldigini gösterir
plt.ylabel('y = f(x)')
# grafigin istedigimiz veriden baslayip bitmesi icin de axis() fonksiyonu kullaniliyormus 
plt.axis([0,2,0,10])
# grafigin adi title() ile yazilir
plt.title("Simple Plot")
# grafigi kaydetmek icin savefig() fonksiyonu kullanilir   # ????
#plt.savefig('("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\introductionToMatplotlib\\plt.png')

plt.show()