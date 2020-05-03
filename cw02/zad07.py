czyKontynuowac = True
while (czyKontynuowac == True):
    zmienna = input(
        "Podaj liczbę którą chcesz podnieść do kwadratulub wpisz 'nie' aby przerwać pętlę: ")
    if(zmienna.isnumeric() == True):
        pom = int(zmienna)
        print("Kwadrat liczby ", pom, " wynosi: ", pom**2)
    elif(zmienna.upper() == "NIE"):
        czyKontynuowac = False
    else:
        print("Nie wiem co wpisałeś :(")
        continue
