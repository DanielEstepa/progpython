cantidad=0
n=int(input("Cuantos triangulos?"))
for x in range(n):
    base=float(input("Base del triangulo"))
    altura=float(input("Altura del triangulo"))
    superficie=base*altura/2
    print("El triangulo cuya base es ",base," y la altura",altura,"tiene una superficie de:",superficie)
    if superficie>12:
        cantidad=cantidad+1

print("Cantidad de triangukos cuya superficie es superior a 12",cantidad)
