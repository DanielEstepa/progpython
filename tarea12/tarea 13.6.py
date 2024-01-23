def crearLista():
    lista=[]

    n=int(input("Cuantos elementos tienen la lista?"))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista"))
        lista.append(valor)
    return lista

def dosListas(lista):
    positivos=[]
    negativos=[]
    for x in range(len(lista)):
        if lista[x]>=0:
            positivos.append(lista[x])
        else:
            negativos.append(lista[x])
    return [positivos,negativos]

def visualizar(positivos,negativos):
    print("Positivos:",positivos)
        
    print("Negativos:",negativos)

lista=crearLista()
print(lista)
positivos,negativos=dosListas(lista)
visualizar(positivos,negativos)
