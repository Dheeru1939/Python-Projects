import numpy as np
import time as tm

n,k,m=10,5,7
print('Code being developed by 202204104610033')
#syntax np.random.randint(low,high="value",size=(row,column),datatype=)
matrixA = np.random.randint(0, high = 100, size=(n, k))
matrixB = np.random.randint(0, high = 100, size=(k, m))

print("matrixA \n",matrixA)
print("matrixB \n",matrixB)

if len(matrixA[1]) == len(matrixB):
    print("multiplication of matrixA and matrixB is possible.")
else:
    print("multiplication of matrixA and matrixB is not-possible.")

#practical 8.2
matrix_M = np.random.randint(0,high=1000, size=(100, 80))
matrix_V = np.random.randint(0,high=1000, size=(80, 90))


print("matrix_M",matrix_M)

print("matrix_V",matrix_V)


time1 = tm.process_time()
#syntax of numpy.dot(m1,m2)
vecmulti = np.dot(matrix_M,matrix_V)

time2 = tm.process_time()
print("Total Time: ", 1000*(time2 - time1 ) , "ms")

print(vecmulti)

zeromatrix = np.zeros((100, 90))
tic = tm.process_time()  
for i in range(len(matrix_M)):
   for j in range(len(matrix_V[0])):
     for x in range(len(matrix_M[i])):
       zeromatrix[i][j] = zeromatrix[i][j] + matrix_M[i][x] * matrix_V[x][j]
toc = tm.process_time()
print("Computation time = " + str(1000*(toc - tic )) + "ms")          
print("-------multiplication of matrix M and matrix V-------")
print(zeromatrix)
    
#practical 8.3    
m = np.indices((9,9)).sum(axis=0) % 2
print(m)    

n = 3
i = 1 + (m.shape[0]-3)
j = 1 + (m.shape[1]-3)
result = np.lib.stride_tricks.as_strided(m, shape=(i, j, n, n), strides = m.strides + m.strides)
print(result)