
def transponer(origen, destino, fila, n_filas):
    if(n_filas == 1):
        for i in range(len(origen[0])):
            destino[i][fila] = origen[fila][i]
            
    else:
        n = int(n_filas / 2)
        transponer(origen, destino, fila, n)
        transponer(origen, destino, fila + n, n_filas - n)


print("Introduce una matriz n*m")
n = int(input("n: "))
m = int(input("m: "))



origen = [[[] for i in range(m)] for i in range(n)]
destino = [[ [] for i in range(n)  ] for i in range(m)]

for i in range(n):
    for e in range(m):
        origen[i][e] = input("[" + str(i) + "," + str(e) + "]: ")

transponer(origen, destino, 0, len(origen))
print(destino)

