czyKontynuowac = True
lista = []
while (czyKontynuowac == True):
    zmienna = input("podaj liczbę lub wpisz 'nie' aby przerwać pętlę: ")
    if(zmienna.isnumeric() == True):
        pom = int(zmienna)
        lista.append(pom)
    elif(zmienna.upper() == "NIE"):
        czyKontynuowac = False
    else:
        print("Nie wiem co wpisałeś :(")
        continue
    print(lista)
