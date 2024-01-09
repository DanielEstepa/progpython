#Definir lista vacia
lista=[]
#Agregamos 5 elementos
for x in range(5)
    valor=int(input("Introduce un nombre:"))
    lista.append(valor)
#visualizar
for x in range(5):
    if len(lista[x])>=5:
        print(lista[x],end=" ")
print()
