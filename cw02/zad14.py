from math import sqrt

try:
    liczba = float(input("Podaj liczbę do pierwiastkowania: "))
    print("Pierwiastek wynosi: ", sqrt(liczba))
except ValueError:
    print('Podano nieprawidłową liczbę')
