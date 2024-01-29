def cargar_productos():
    productos = []
    for _ in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        productos.append((nombre, precio))
    return productos

def listar_productos(productos):
    print("Lista de productos y precios:")
    for nombre, precio in productos:
        print(f"{nombre}: ${precio}")

def imprimir_productos_entre_10_y_15(productos):
    print("Productos con precios entre 10 y 15:")
    for nombre, precio in productos:
        if 10 <= precio <= 15:
            print(f"{nombre}: ${precio}")

# Bloque principal
productos = cargar_productos()
listar_productos(productos)
imprimir_productos_entre_10_y_15(productos)
