wysokosc = -1
while(wysokosc < 0 or wysokosc > 10):
    wysokosc = int(
        input("Podaj wysokosc wiezy do zbudowania ale nie więcej niż 10 jednostek: "))

for i in range(wysokosc):
    print((i+1)*"A")
