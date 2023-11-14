num=int(input("Ingresa un numero de uno o dos digitos:"))

if num>0:
    if num<100:
        if num>=10:
            print("El numero tiene dos cifras")
        else:
            print("El numero tiene una cifra")
    else:
        print("El numero tiene mas de dos cifras")
else:
    print("El numero es negativo")

 
