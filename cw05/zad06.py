class Wspak:

    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def wyswietl(tekst):
    wspak = Wspak(tekst)
    while True:
        try:
            print(next(wspak), end="")
        except StopIteration:
            break
    print()

zdanie1 = "Ala ma kota"
zdanie2 = "Iterator zwracający wartości w odwróconym porządku"

wyswietl(zdanie1)
wyswietl(zdanie2)