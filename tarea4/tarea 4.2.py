
suma=0
n=int(input("¿Cuantas alturas vas a ingresar :"))
x=1
while x<=n:
    altura=float(input("Introduce una altura:"))
    x=x+1
    suma=suma+altura
promedio=suma/n

print("El promedio de la altura es:",promedio)
