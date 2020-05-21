zdanie = "Generator zwracający wartości w odwróconym porządku"

def wspak(zdanie):
    for i in range(len(zdanie)):
        yield zdanie[-(i+1)]

def wyswietl(tekst):
    result = wspak(tekst)
    while True:
        try:
            print(next(result), end="")
        except StopIteration:
            break
    print()

wyswietl(zdanie)
