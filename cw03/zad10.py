def zliczenie(**zakupy):
    return sum(zakupy.values())

zakupy = {"jabłka":3, "sok pomarańczowy": 1, "masło":2}
print(zliczenie(**zakupy))