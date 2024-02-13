class Operaciones:
    def __init__(self):
        self.numero1=int(input("Numero 1:"))
        self.numero2=int(input("Numero 2:"))

    def suma(self):
        resultado=self.numero1+self.numero2
        print("la suma es:",resultado)

    def resta(self):
        resultado=self.numero1-self.numero2
        print("la resta es:",resultado)

    def multiplicar(self):
        resultado=self.numero1*self.numero2
        print("la multiplicacion es:",resultado)

    def suma(self):
        resultado=self.numero1/self.numero2
        print("la division es:",resultado)

operacion=Operaciones()
operacion.suma()
operacion.resta()
operacion.multiplicar()
operacion.division()

