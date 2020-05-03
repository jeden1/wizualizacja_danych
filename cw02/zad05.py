a = input("Podaj liczbe a: ")
b = input("Podaj liczbe b: ")
c = input("Podaj liczbe c: ")

a = int(a)
b = int(b)
c = int(c)

if(0 < a <= 10 and (a > b or b > c)):
    print("Podane liczby spełniają warunki")
else:
    print("Podane liczny nie spełniają warunków")
