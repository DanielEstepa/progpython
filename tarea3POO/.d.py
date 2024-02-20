class socio:
    def __init__(self):
        self.nombreSocio=input("Introduzca el nombre del socio:")
        self.antiguedadSocio=input("Introduzca la aitguedad del socio:")

    def imprimir(self):
        print(self.nombre,"tiene una antiguedad en años de",self.antiguedad)

    def verAntiguedad(self):
        return self.antiguedad

class club:
    def __init__(self):
        self.socios=[]

    def agregarSocio(self):
        socio=Socio()
        self.socios.append(socio)

    def mostarSocios(Self):
        for socio in self.socios:
            socio.imprimir()
            
    def mostrarUnsocio(self):
        pos=int(input("Introduce la posicion del socio a visualizar:"))
        if (pos<len(self.socios)):
            self.socios[pos].imprimir()
    def mostrarMayorAntiguedad(Self):
        mayor=self.socios[0]
        for socio in self.socios:
            socio.verAntiguedad()>mayor.verAntiguedad():
                mayor=socio
        print("Socio de mayor antiguedad:")
        mayor.imprimir()
        
club=club()
club.agregarSocio()
club.agregarSocio()
club.agregarSocio()
club.mostrarSocios()
club.mostrarUnsocio()
club.mostrarMayorAntiguedad()
