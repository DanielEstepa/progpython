 def cargar_lista_enteros():
    lista = []
    for x in range(5):
        num = int(input("Ingrese un número entero: "))
        lista.append(num)
    return lista

def obtener_mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return (mayor, menor)

# Bloque principal
lista_enteros = cargar_lista_enteros()
mayor, menor = obtener_mayor_menor(lista_enteros)

print("El mayor valor es:", mayor)
print("El menor valor es:", menor)
