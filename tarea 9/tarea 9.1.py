#Definir lista vacia
lista=[]
#Agregamos 5 elementos
for x in range(5)
    valor=int(input("Introduce un numero:"))
    lista.append(valor)
#visualizar
for x in range(5):
    if lista[x]>=7:
        print(lista[x],end=" ")
