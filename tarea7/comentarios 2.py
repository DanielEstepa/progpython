"""Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma"""
#Daniel Estepa Quirós
#11 Diciembre 2023
#variable acumuladora,suma
suma=0
for x in range(10):
    n=int(input("Introduce un numero:"))#lectura del numero
    suma=suma+n#uso de la variable acumuladora
#El resultado final es:suma
print("La suma de todos los numeros es:",suma)
    
