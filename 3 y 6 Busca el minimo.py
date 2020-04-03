class Funcion:
    origen: list
    destino: list
    minimo: list

    def __init__(self, _origen, _destino, _minimo):
        if(_origen[1] <= _minimo[1] or _destino[1] <= _minimo[1] or not(_origen[0] <= _minimo[0] and _minimo[0] <= _destino[0])):
            print("Minimo invalido")
            exit(-1)
        self.origen = _origen
        self.destino = _destino
        self.minimo = _minimo

    def calcula(self, x):
        if(x < self.minimo[0]):
            m = (self.minimo[1] - self.origen[1])/(self.minimo[0] - self.origen[0])
            return m*(x - self.origen[0]) + self.origen[1]

        else:
            m = ( self.destino[1] - self.minimo[1])/(self.destino[0] - self.minimo[0])
            return self.minimo[1] + m*(x - self.minimo[0])

def busqueda(inicio, rango, funcion: Funcion, error):
    if(rango <= error):
        print(inicio)
        return

    f1 = funcion.calcula(inicio + rango/4)
    f2 = funcion.calcula(inicio + rango * 3/4)

    if(f1 < f2): #Mitad inferior
        busqueda(inicio, rango/2, funcion, error)
    else:
        busqueda(inicio+rango/2, rango/2, funcion, error)


funcion = Funcion([10,50], [100,50], [70,-50])

busqueda(0, 100, funcion, 0.1)