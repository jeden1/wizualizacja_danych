def badanie(a, b):
    if a > 0:
        print("Funkcja y =",a,"x +",b," jest funkcją rosnącą")
    elif a == 0:
        print("Funkcja y =",a,"x +",b," jest funkcją stałą")
    else:
        print("Funkcja y =",a,"x +",b," jest funkcją malejącą")

a = float(input("Podaj współczynnik a funkcji liniowej: "))
b = float(input("Podaj wyraz wolny b funkcji liniowej: "))
badanie(a, b)