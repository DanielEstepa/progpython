n=int(input("Introduce el numero de triangulos:"))
isosceles=0
escaleno=0
equilatero=0
for x in range(n):
    lado1=float(input("Introduce el lado 1 :"))
    lado2=float(input("Introduce el lado 2 :"))
    lado3=float(input("Introduce el lado 3 :"))
    if lado1==lado2 and lado1==lado3:
        print("Triangulo equilatero")
        equilatero=equilatero+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Triangulo isosceles")
            isosceles=isosceles+1
        else:
            print("Triangulo escaleno")
            escaleno=escaleno+1
print("cantidad de equilateros",equilatero)
print("cantidad de isosceles",isosceles)
print("cantidad de escalenos",escaleno)
        
