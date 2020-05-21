class Samogloski:

    def __init__(self, zdanie):
        if isinstance(zdanie, str):
            self.zdanie = zdanie
        else:
            raise TypeError
        self.index = 0
        self.end = len(zdanie)+1

    def __iter__(self):
        return self

    def __next__(self):
        samogloski = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
        while self.zdanie[self.index].lower() not in samogloski:
            self.index += 1
        buffer = self.zdanie[self.index]
        self.index += 1
        return buffer


def wyswietl(tekst):
    result = Samogloski(tekst)
    while True:
        try:
            print(next(result), end="")
        except StopIteration:
            break
    print()


zdanie = "Iterator zwracający tylko samogłoski"

wyswietl(zdanie)

'''
    def __next__(self):
        if self.index == self.end:
            raise StopIteration
        for element in self.samogloski:
            if self.zdanie[self.index].lower() == element:
                return self.zdanie[self.index]
                self.index += 1       
        self.index += 1
'''
