def cargar_lista_palabras():
    lista_palabras = []
    n = int(input("Ingrese el número de palabras que desea agregar: "))
    for _ in range(n):
        palabra = input("Ingrese una palabra: ")
        lista_palabras.append(palabra)
    return lista_palabras

def mostrar_palabras_mas_de_5_caracteres(lista_palabras):
    print("Palabras con más de 5 caracteres:")
    for palabra in lista_palabras:
        if len(palabra) > 5:
            print(palabra)

# Bloque principal
palabras = cargar_lista_palabras()
mostrar_palabras_mas_de_5_caracteres(palabras)
