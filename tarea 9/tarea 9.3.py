#Definir lista vacia
lista=[]
#Agregamos 5 elementos
for x in range(5)
    valor=float(input("Introduce un altura:"))
    lista.append(valor)
#visualizar promedio
suma=0
for x in range(5):
    suma=suma+lista[x]
promedio=suma/5
print("Altura media es:",promedio)
#vitualizar cuantos superan la media y los que no
s=0
Ns=0
for x in range(5):
    if lista[x]>promedio:
        s=s+1
    else:
        Ns=Ns+1

      
print("Persona superior a la media",s)


print("Persona inferior a la media",Ns)
