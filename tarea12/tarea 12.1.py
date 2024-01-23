def crearLista():
    lista=[]

    n=int(input("Cuantos elementos tienen la lista?"))
    for x in range(n):
        valor=input("Introduce un elemento de la lista")
        lista.append(valor)
    return lista

def mascaracteres(lista):
    palabra=lista[0]
    for x in range(1,len(lista)):
        if len(lista[x])>len(palabra):
            palabra=lista[x]
        return palabra
        

palabra=crearLista()
print(palabra)
print("Palabra con mas caracteres:",mascaracteres(palabra))

