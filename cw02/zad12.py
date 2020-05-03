x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in x:
    for j in x:
        if(x[i]*x[j] == 0):
            continue
        elif(0 < x[i]*x[j] < 10):
            print(" ", x[i]*x[j], end='  | ')
        elif(9 < x[i]*x[j] < 100):
            print(" ", x[i]*x[j], end=' | ')
        else:
            print(" ", x[i]*x[j], end='| ')
    print("\n---------------------------------------------------------------------")
