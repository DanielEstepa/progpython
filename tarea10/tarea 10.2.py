productos=[]
precios=[]
for x in range (5):
    nom=input("Introduce un producto:")
    nombres.append(producto)
    nota=int(input("Introduce un precio"))
    sueldos.append(precio)
print("El precio del primer producto,",productos[0],"es",precios[0])
print("Los productos con precio superior son:")
for x in range(1,5):
    if (precuos[x]>precios[0]):
        print(producors[x]," ",precios[x])
