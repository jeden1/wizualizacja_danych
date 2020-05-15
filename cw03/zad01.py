listaA = [ (1/i) for i in range( 1, 11)]
listaB = [ 2**i for i in range(10)]
listaC = [ i for i in listaB if i%4==0]
print(listaA ,"\n", listaB, "\n", listaC)