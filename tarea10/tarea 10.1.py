nombres=[]
notas=[]
for x in range (10):
    nom=input("Introduce un nombre:")
    nombres.append(nom)
    nota=int(input("Introduce una nota"))
    sueldos.append(nota)
print("alumnos aprobados")
for x in range(10):
      if notas[x]>=5:
          print(nombres[x]," ",notas[x])
print("alumnos suspensos")
for x in range(10):
      if notas[x]<5:
          print(nombres[x]," ",notas[x])
