import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# A = np.array([[1, 2, 3], [7, 8, 9]])
# print(A)

# B = np.array([[1, 2, 3],
# [7, 8, 9]])
# print(B)

# A = np.array([[1, 2, \
# 3],
# [7, 8, 9]])
# print(A)

# v = np.arange(1,7)
# print(v,"\n")

# v = np.arange(1,11,3)
# print(v,"\n")

# v = np.linspace(1,3,4)
# print(v)

# X = np.ones((2,3))
# Y = np.zeros((2,3,4))
# Z = np.eye(2) # np.eye(2,2) # np.eye(2,3)
# Q = np.random.rand(2,5) # np.round(10*np.random.rand((3,3)))
#
# print(X,"\n\n",Y,"\n\n",Z,"\n\n",Q)


# A = np.array([[1, 2, 3, 4], [7, 8, 9, 10]])
# X = np.array([1, 2])
# Z = np.array([3, 4])
# U = np.block([[A], [X,Z]])
# print(U)


# V = np.block([[
# np.block([
# np.block([[np.linspace(1,3,3)],
# [np.zeros((2,3))]]) ,
# np.ones((3,1))])
# ],
# [np.array([100, 3, 1/2, 0.333])]] )
# print(V)


# # # print( V[3,3] )


# # print( V[3,:] ) # wyswietlenie 4 wiersza, numeracja od 0
# # print( V[:,2] ) # wyswietlenie 3 kolumny, numeracja od 0


# print( V[3,0:3] ) # wyswietlenie 4 wiersza i kolumn 0 1 2


# print( V[3] )

# Q = np.delete(V, 2, 0) # usuniecie wiersza
# print(Q)

# Q = np.delete(V, 2, 1) # usuniecie kolumny
# print(Q)

# v = np.arange(1,7)
# print(v)
# print( np.delete(v, 3, 0) )

# print(np.size(V)) #ile elemenów
# print(np.shape(V)) #rozmiar ile na ile

A = np.array([[1, 0, 0],
[2, 3, -1],
[0, 7, 2]] )
print(A)

B = np.array([[1, 2, 3],
[-1, 5, 2],
[2, 2, 2]] )
print(B)
#
# print( A+B )
# print( A-B )
# print( A+2 )
# print( 2*A )

# MM1 = A@B
# print(MM1)
# MM2 = B@A
# print(MM2)

# MT1 = A*B
# print(MT1)
# MT2 = B*A
# print(MT2)

# DT1 = A/B
# print(DT1)

# C = np.linalg.solve(A,MM1)
# print(C) # porownaj z macierza B
# x = np.ones((3,1))
# b = A@x
# y = np.linalg.solve(A,b)
# print(y)

# PM = np.linalg.matrix_power(A,2) # por. A@A
# PT = A**2 # por. A*A

# A.T # transpozycja
# A.transpose()
# A.conj().T # hermitowskie sprzezenie macierzy (dla m. zespolonych)
# A.conj().transpose()

# A == B
# A != B
# 2 < A
# A > B
# A < B
# A >= B
# A <= B
# np.logical_not(A)
# np.logical_and(A, B)
# np.logical_or(A, B)
# np.logical_xor(A, B)
# print( np.all(A) )
# print( np.any(A) )
# print( v > 4 )
# print( np.logical_or(v>4, v<2))
# print( np.nonzero(v>4) )
# print( v[np.nonzero(v>4) ] )

# print(np.max(A))
# print(np.min(A))
# print(np.max(A,0))
# print(np.max(A,1))
# print( A.flatten() )

###############################    Matplotlib    ##########################

import matplotlib.pyplot as plt

# x = [1,2,3]
# y = [4,6,5]
# plt.plot(x,y)
# plt.show()

# x = np.arange(0.0, 2.0, 0.01)
# y = np.sin(2.0*np.pi*x)
#
# x = np.arange(0.0, 2.0, 0.01)
# y = np.sin(2.0*3.14*x)
# plt.plot(x,y,'r:',linewidth=6)
# plt.xlabel('Czas')
# plt.ylabel('Pozycja')
# plt.title('Nasz pierwszy wykres')
# plt.grid(True)
# plt.show()

# x = np.arange(0.0, 2.0, 0.01)
# y1 = np.sin(2.0*3.14*x)
# y2 = np.cos(2.0*3.14*x)
# plt.plot(x,y1,'r:',x,y2,'g')
# plt.legend(('dane y1','dane y2'))
# plt.xlabel('Czas')
# plt.ylabel('Pozycja')
# plt.title('Wykres')
# plt.grid(True)
# plt.show()

x = np.arange(0.0, 2.0, 0.01)
y1 = np.sin(2.0*3.14*x)
y2 = np.cos(2.0*3.14*x)
y = y1*y2
l1, = plt.plot(x,y,'b')
l2,l3 = plt.plot(x,y1,'r:',x,y2,'g')
plt.legend((l2,l3,l1),('dane y1','dane y2','y1*y2'))
plt.xlabel('Czas')
plt.ylabel('Pozycja')
plt.title('Wykres ')
plt.grid(True)
plt.show()



