nota1=int(input("Ingresa nota 1:"))
nota2=int(input("Ingresa nota 2:"))
nota3=int(input("Ingresa nota 3:"))

suma=nota1+nota2+nota3
notaMedia=suma/3

if notaMedia>=5:
    print("EL alumno esta aprobado con una media de:",notaMedia)

else :
  print("El alumno esta suspenso con una media de :",notaMedia)
    
