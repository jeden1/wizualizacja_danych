tekst = ["One more time we're gonna celebrate\n","Oh yeah all right don't stop the dancing\n","One more time we're gonna celebrate\n","Oh yeah all right don't stop the dancing\n"]

with open("cw04/zad03.txt", "w") as plik:
    for line in range(len(tekst)):
        plik.writelines(tekst[line])

with open("cw04/zad03.txt", "r") as plik:
    for wiersz in plik:
        print(wiersz, end="")