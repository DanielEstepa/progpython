positivo=0
negativo=0
mult15=0
sumapares=0
for x in range(10):
    n=int(input("Ingresa valor:"))
    if n>0:
        print("El numero es positivo")
        positivo=positivo+1
    else:
        print("El numero es negativo")
        negativo=negativo+1
    if n%15==0:
        print("Es multiplo de 15")
        mult15=mult15+1
    if n%2==0:
        sumapares=sumapares+n
        print("La suma de sus pares es:",sumapares)
          
