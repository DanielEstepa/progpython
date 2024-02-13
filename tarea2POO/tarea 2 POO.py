class agenda:
    def __init__(self):
        self.listaAgenda=[]4

    def cargar(Self):
        nombre=input("Nombre:")
        telefono=input("Telefono:")
        email=input("Email:")
        lista=[]
        lista.append(nombre)
        lista.append(telefono)
        lista.append(email)
        self.listaAgenda.append(lista)

    def lista(self):
        fot usuario in self.listaAgenda:
            print(usuario[0],":",usuario[1],"-",usuario[2])
            
    def consultaNombre(self):
        nombre=input("Nombre a consultar:")
        encontrado=0
        longitud=len(self.listaAgenda)
        indice=0
        while encontrado==0 and indice<longitud:
            if self.listaAgenda[indice][0]==nombre:
                print("Telefono:",self.listaAgenda[indice][1])
                    
    def modificar(self):
        pos=self.consultaNombre()
        telefono=input("Telefono:")
        email=input("email:")
        self.listaAgenda[pos][1]=telefono
        self.listaAgenda[pos][2]=email

    def menu(self):
        op=6
        while op!=5:
            print("1.cargar datos en la agenda")
            print("2.listar datos de la agenda")
            print("3.consultar por nombre")
            print("4.modificar telefono y email")
            print("5.Finalizar")
            op=int(input("introduce una opcion:"))
            if op==1:
                self.cargar()
            if op==2:
                self.listar()
            if op==3:
                self.consultaNombre()
            if op==4:
                self.modificar()
