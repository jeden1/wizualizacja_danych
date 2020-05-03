liczba = input("Podaj liczbę w którech chcesz zsumować cyfry ją tworzące: ")
lista = list(liczba)
suma = 0

for i in range(len(lista)):
    pom = int(lista[i])
    suma += pom
print(suma)
