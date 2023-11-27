suma=0
entre100y300=0
otros=0
n=int(input("¿Cuantos enpleados trabajan en la empresa?:"))
x=1
while x<=n:
    sueldo=int(input("Introduce un sueldo:"))
    x=x+1
    suma=suma+sueldo
    if sueldo>=100 and sueldo<300:
        entre100y300=entre100y300+1
    else:
        otros=otros+1

print("Empleados que ganan entre 100 y 300:",entre100y300)
print("Empleados que ganan mas de 500",otros)
print("Los gastos de la empresa son:",suma)

