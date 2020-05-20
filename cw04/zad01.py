from random import randint


plik = open("cw04/zad01.txt", "w")
lista = []

for i in range(50):
    a = randint(1, 100)
    if a % 4 == 0:
        lista.append(a)

plik.writelines(str(lista))