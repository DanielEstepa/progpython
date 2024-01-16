alumnos=[]
notas=[]
for x in range (4):
    nom=input("Introduce un alumno:")
    nombres.append(nombre)
    nota=int(input("Introduce una nota"))
    sueldos.append(nota)
muybueno=0
for x in range(4):
      if notas[x]<4:
          print(alumnos[x],"Insuficiente")
      else:
          if notas[x]<=7:
              print(alumnos[x],"Bueno")
          else:
              muybueno=muybueno+1
              print(alumnos[x],"Muy buenos")
              
    
          print(nombres[x]," ",notas[x])
print("alumnos muy buenos:",muybueno)
