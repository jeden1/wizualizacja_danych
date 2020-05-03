wysokosc = int(input('Podaj wysokosc rombu który mam narysować: '))
if(3 <= wysokosc <= 9):
    for x in range(1, wysokosc+1):
        if x % 2:
            print((x * 'O').center(wysokosc, ' '))
    for x in range(wysokosc+1, 0, -1):
        if x % 2 and x is not wysokosc:
            print((x * 'O').center(wysokosc, ' '))
