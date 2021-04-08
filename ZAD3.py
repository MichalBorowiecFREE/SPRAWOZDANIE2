import numpy as np

#    zad 3
#################################

####   sposob 1 - wypisanie kolejnych elmentów i kolejne łączenie

# z = np.arange(1,6)
# x = np.arange(5,0, -1)
# c = np.zeros([3,2], dtype = int)
# v = np.linspace(2,2,3,dtype = int)
# b = np.linspace(-90,-70,3,dtype = int)
# n=np.array([[10],[10],[10],[10],[10]])
#
# E = np.block([[z],[x]])
# B = np.block([[v],[v],[b]])
# C = np.block([c,B])
# D = np.block([[E],[C]])
# A = np.block([D,n])

####   łaczenie w "jednej lini"

#A = np.block([np.block([[np.block([[z],[x]])],[np.block([c,np.block([[v],[v],[b]])])]]),n])

####   utworzenie macierzy "na raz"

A = np.block(
    [np.block([[np.block([[np.arange(1,6)],[np.arange(5,0, -1)]])],
    [np.block([np.zeros([3,2], dtype = int),np.block([[np.linspace(2,2,3,dtype = int)],
    [np.linspace(2,2,3,dtype = int)],[np.linspace(-90,-70,3,dtype = int)]])])]]),
    np.array([[10],[10],[10],[10],[10]])])
#print(A)


#   zad 4
#################################################

B=A[1,:]+A[3,:]
#print(B)


#   zad 5
#################################################

C =(np.max(A,0))
#print(C)

#    zad 6
##################################################

D = np.delete(B, [0,5], 0)
#print(D)

#   zad 7
##################################################

i = 0
while i < np.size(D):
  if D[i] == 4:
      D[i] = 0;
  i += 1

#print(D)

#    zad 8
###################################################

#print(C)

i = 0
j = 0
while i < np.size(C):
  if C[i] == np.max(C):
      E = np.delete(C,i,0)
  i += 1

while j < np.size(E):
  if E[j] == np.min(E):
      E = np.delete(E,j,0)
  j += 1

#print(E)

#   zad 9
#####################################################



#   zad 10
#####################################################

#print(D*E)
#print(D@E)


#   zad 11
#####################################################

def macierz(wymiar):
    X = np.random.randint(0, 10, [wymiar, wymiar])

    i = 0
    slad = 0
    while i < wymiar:
        slad = slad + X[i, i]
        i += 1

    return X, slad

print(macierz(3))



