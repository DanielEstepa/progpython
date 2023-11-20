from math import sqrt
numA=int(input("Introduce numero A:"))
numB=int(input("Introduce otro numero B:"))
numC=int(input("Introduce otro numero mas C:"))
aux=numB*numB-4*numA*numC
if aux<0:
    print("Soluciones conmplejas")
else:
     raiz=sqrt(aux)
     x1=(-numB+raiz)/2*numA
     x2=(-numB-raiz)/2*numA
     print("x1 es:",x1)
     print("x2 es:",x2)

