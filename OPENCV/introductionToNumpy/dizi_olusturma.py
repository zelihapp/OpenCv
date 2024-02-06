import numpy as np 

# dizi olusturmak icin numpy'in icindeki array() fonksiyonunu cagiriyoruz
# fonksiyonun aldigi ikinci parametre verilerin tipi 
x = np.array([1,2,3],np.int16)

print(x)
# tipini ögrenme
print(type(x))
# dizinin elemanlarina ulasma
print(x[0]);print(x[1]);print(x[2])
# son elemana erisme
print(x[-1])
# 3.indexteki elemani yazdirma print(x[3]) bu indexte eleman yok HATA!
print(x[-2])



