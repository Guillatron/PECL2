from random import randint
import time

def rellena(botellas, tapones, n):
    libres = [i for i in range(n)]
    for i in range(n):
        botellas.append(randint(0, n))

    lon = n
    for i in range(n):
        pos = libres[randint(0, lon - 1)]
        tapones.append(botellas[pos])
        libres.remove(pos)
        lon -= 1


def robot(botellas: list, tapones: list):
    izdaT = []
    izdaB = []
    dchaT = []
    dchaB = []

    tapon = tapones[0]
    botella = 0

    for i in range(len(tapones)):
        if botellas[i] == tapon:
            botella = botellas[i]
    tapones.remove(tapon)
    botellas.remove(botella)

    for i in range(len(tapones)):
        if tapones[i] < botella:
            izdaT.append(tapones[i])
        else:
            dchaT.append(tapones[i])

        if botellas[i] < tapon:
            izdaB.append(botellas[i])
        else:
            dchaB.append(botellas[i])

    if(len(izdaB)>0): robot(izdaB, izdaT)
    if(len(dchaB)>0): robot(dchaB, dchaT)


botellas = []
tapones = []
cantidad = 100


for i in range(10):
    rellena(botellas, tapones, cantidad)
    ini = time.time()
    robot(botellas, tapones)
    fin = time.time()
    print(str(cantidad) + ": " + str(fin-ini))
    botellas.clear()
    tapones.clear()
    cantidad*=2

