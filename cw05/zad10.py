import itertools


zbior = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = itertools.combinations(zbior, 3)

for item in result:
    print(item)
