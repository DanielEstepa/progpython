nombres=[]
sueldos=[]
for x in range (5):
    nom=input("Introduce un nombre:")
    nombres.append(nom)
    valor=int(input("Introduce un sueldo"))
    sueldos.append(valor)
mayor=0
menor=999999
posmayor=0
posmenor=0
for x in range (5):
    if sueldo [x]>mayor:
        mayor=sueldos[x]
        posmayor=x
    if sueldo[x]<menor:
        menor=sueldos[x]
        posmenor=x
print("El sueldo mayor es:",mayor, " y pertenece",nombres[posmayor])
print("El sueldo menor es:",menor, " y pertenece",nombres[posmenor])
