from random import randint 

macierz = [ randint(0, 50) for i in range(4) for j in range(4) if i == j]
print(macierz)