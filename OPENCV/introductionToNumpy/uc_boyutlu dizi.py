import numpy as np

x = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]] ],np.int16)
# diziyi yazar
print(x)
# 1.elemana ulasmak icin:
# ilk boyuta giriyor daha sonra ilk satirin daha sonra da 1.indexteki elemani aliyor (1)
print(x[0,0,0])
# 4 elemanina ulasmak icin -> ilk boyuta giriyor daha sonra 2 satira daha sonra da 0.indexteki elemani aliyor
print(x[0,1,0])
# 11 'e ulasmak icin 
print(x[1,1,1])