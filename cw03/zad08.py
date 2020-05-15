def ciag(a1, r, ile):
    print(a1)
    for a1 in range(a1, ile+1):
        a1 += r
        print(a1)

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
        ciag(1, 1, 10)
    else:
        print("Nie wiem co wpisałeś :(")
        continue