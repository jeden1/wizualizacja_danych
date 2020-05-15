import math

def promien(a, b, x, y):
    return(math.sqrt((x - a)**2 +(y - b)**2))

a = 4
b = 2
x = 6
y = 9
""" alternatywa dla dowolnych argumentów
a = float(input("Podaj pierwszą współrzędną środka okręgu: "))
b = float(input("Podaj drugą współrzędną środka okręgu: "))
x = float(input("Podaj pierwszą współrzędną punktu przez który przechodzi okręg: "))
y = float(input("Podaj drugą współrzędną punktu przez który przechodzi okręg: "))
"""
print(promien(a, b, x, y))