import numpy as np

# cok boyutlu dizi , dizinin tüm satirlarini tek bir koseli parantez icine aliriz 
x = np.array([[1,2,3],[4,5,6]],np.int16)   
print(x)                                 # ayni zamanda 2 satir ve 3 sutundan olusan nir matris veya dizeydir
print("----------")
print(x[0])   # [1,2,3] ilk satiri verir
print("----------")
print(x[0,0])                                           # cok boyutlu dizinin ilk elemanini verir
print("----------")                                        
print(x[0]);print(x[0,0]);print(x[0,1]);print(x[0,2])  # cok boyutlu dizinin 1.satirdaki elemanlarini verir
print("----------")
print(x[1]);print(x[1,0]);print(x[1,1]);print(x[1,2])  # cok boyutlu dizinin 2.satirdaki elemanlarini verir
print("----------")
# 1 ve 4'e tek satirda cagirip erismek istiyorsak
# : her seyi tara demektir . ilk parantezin icindeki her seyi tarayacak ve bu taradiklarindan sadece 0.indextekileri alacak 
# yani 1.satirda 0.indexte ne var? (1) ve 2.satirda 0.indexte ne var? (4)
print(x[:,0])
# 2.sutundaki elemanlari almak istiyorsak 
print(x[:,1])
# 3.sutundaki elemanlari almak istiyorsak
print(x[:,2])
print("----------")
# satirlari cekme yontemi;
print(x[0,:]);print(x[1,:])






