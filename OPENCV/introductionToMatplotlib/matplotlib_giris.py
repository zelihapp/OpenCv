# matplotlib kutuphanesi aslinda bir veri gorsellestirme kutuphanesidir
# elimizdeki verileri görsellestirerek onlari daha anlamli hale getiririz

import matplotlib.pyplot as plt
import numpy as np

# arange() -> 5'e kadar sayi uretir (0,1,2,3,4) type -> ndarray
x = np.arange(5)
y = x     # y eksenine de x ekseninin degerleri atanir


# grafige dokmek (cizmek) icin plot() kullanilir , grafigi gostermek icin show() kullanilir
# cizilen grafigin figurunu degistirmek istiyorsak 3.parametre olarak "o","o-","o--" gibi ifadeler girilebilir
plt.plot(x,y,"o--") 
# ayni grafik uzerine baska veriler ile de grafik cizilebilir
plt.plot(x,-y)
plt.plot(-x,y,"o")

# grafigin adi girilmesi isin title() kullanilir
plt.title("y=x, y=-x")
plt.show()