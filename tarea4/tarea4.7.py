n=int(input("cuantos numeros?"))
pares=0
impares=0
x=1
while x<=n:
    valor=int(input("Introduce un valor:"))
    x=x+1
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
print("los numero impares son:",impares)
print("los numero pares son:",pares)
