class Tortuga:
    def __init__(self, name):
        self.posicion_x = 0
        self.name = name

    def adelante(self, cantX):
        linea = " " * self.posicion_x
        self.posicion_x += cantX
        for i in range(cantX):
            if i == cantX-1:
                linea= linea + "→"
            else:
                linea= linea + "-"
            i=i+1
        print(linea)

    def abajo(self, cantY):
        lineaBajada = " " * self.posicion_x
        for i in range(cantY):
            if i == cantY-1:
                print(lineaBajada + "↓")
            else:
                print(lineaBajada + "|")
                i=i+1

    def reiniciar(self):
        self.posicion_x = 0
        print(f"Posición de {self.name} reiniciada.")
