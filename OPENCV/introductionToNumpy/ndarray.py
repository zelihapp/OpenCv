import numpy as np 

# ndarray -> n-dimensional array demektir . n boyutlu dizi 

x = np.array([[-2,-1,0,5],[9,4,5,-7],[9,7,6,5]],np.int16)       # int basinda u olsaydi uint negatif sayilar -> unsigned int

print(x)
# cok boyutlu dizilere ait bazi ozelliklere erisebiliyoruz

# shape sekil demektir 2 satir 4 sutundan olustugunu soyler
print(x.shape)
# kac boyutlu oldugunu söyler ndim
print(x.ndim)
# data type yani veri tipini verir int18
print(x.dtype)
# dizinin kac elemandan olustugunu verir
print(x.size)
# transpoz ters cevirme islemini yapar 1.satiri 1.sutun yapar
print(x.T)