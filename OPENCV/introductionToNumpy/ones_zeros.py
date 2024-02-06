# ones ve zeros dizi olusturma yöntemleridir

import numpy as np 

# bos bir dizi olusturmak icin bundan kasit elemanlari random atamak
x = np.empty([3,3],np.uint8)  # negatif sayilar girmemesi icin uint
print (x)

print("--------")
# dolu bir dizi olusturulur . fill_value'dan kasit doldurmak istedigimiz sayilar demek
y = np.full([3,3],dtype=np.uint8,fill_value=5)
print(y)

print("--------")

# birlerden olusan bir dizi olusturmak icin
z = np.ones([2,5,5],dtype=np.int8)
print(z)
print("--------")

w = np.zeros([2,3,3],dtype=np.int8)
print(w)






