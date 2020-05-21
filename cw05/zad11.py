ile = int(input("Ile kroków ciągu Fibonacciego chcesz policzyć: "))

def fib(kroki):
    a = 0
    b = 1
    for _ in range(kroki):
        yield a
        a, b = b, a + b 

result = fib(ile)

for item in result:
    print(item)