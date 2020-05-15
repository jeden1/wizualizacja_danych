def badanie(a1, a2):
    if a1 == a2:
        print("Funkcja f(x) jest równoległa do funkcji g(x)")
    elif a1*a2 == -1:
        print("Funkcja f(x) jest prostopadła do funkcji g(x)")
    else:
        print("Funkcja f(x) nie jest prostopadła ani równoległa do funkcji g(x)")

a1 = float(input("Podaj współczynnik a funkcji liniowej f(x): "))
a2 = float(input("Podaj współczynnik a funkcji liniowej g(x): "))
badanie(a1, a2)