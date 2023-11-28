
turno1=0
turno2=0
turno3=0
for x in range(5):
    edadM=int(input("edad de cada estudiante de mañana:"))
    turno1=turno1*edadM
    
for x in range(6):
    edadT=int(input("edad de cada estudiante de tarde:"))
    turno2=turno2+edadT
for x in range(11):
    edadN=int(input("edad de cada estudiante de noche:"))
    turno3=turno3+edadN
    
promedio1=turno1/5
promedio2=turno2/6
promedio3=turno3/11
print("Edad media de la mañana es:",promedio1)
print("Edad media de la tarde es:",promedio2)
print("Edad media de la noche es:",promedio3)
if promedio1>promedio2 and promedio1>promedio3:
    print("El turno de mañana tendra mayor promedio de edad")
else:
    if promedio2>promedio3:
        print("El turno de tarde tendra mayor promedio de edad")
    else:
        print("El turno de noche tendra mayor promnedio de edad")

