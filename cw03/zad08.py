def ciag(a1, r, ile):
    for krok in range(ile+1):
        print(a1 + krok * r)


zapetlone = True

while (zapetlone == True):
    opcja = input("Czy chcesz wykorzystać domyślne wartości? (t/n) ")
    if( opcja == "n"):
        zapetlone = False
        a1 = int(input("Podaj wartość początkową ciągu: "))
        r = int(input("Podaj wielkość zmiany pomiędzy kolejnymi krokami: "))
        ile = int(input("Podaj ile elementów chcesz policzyć: "))
        ciag(a1, r, ile)
    elif( opcja == "t"):
        zapetlone = False
        ciag(-1, 3, 11)
    else:
        print("Nie wiem co wpisałeś :(")
        continue