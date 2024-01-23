def crearLista(n):
    articulos=[]
    precios=[]
    
    for x in range (n):
        precio=int(input("Introduce los precios de los articulos:"))
        articulos=input("Introduce el nombre de los articulos:")
        articulos.append(articulos)
        precios.append(precio)
    return[articulos,precios]
def verArticulos(articulos,precios):
        for x in range(len(lista)):
            print(articulos[x],":",precios[x])
            
def articuloMascaro(articulos,precio):
    mascaros=precio[0]
    pos=0
    for x in range(1,len(precio)):
        if precios[x]>mascaros:
            mascaros=precios[x]
            pos=x
    print("El articulo mas caro es:",articulos[pos],"con un precio de:",mascaros)


def aritculosMenores(articulos,precio,importe):
    for x in range(len(precios)):
        if precio[x]<importe:
            print(articulos[x],"Tiene un precio menor a ",importe,"y es",precio[x])

n=int(input("Cuantos articulos hay:?"))
articulos,precio=crearLista(n)
verArticulos(articulos,precio)
articuloMascaro(articulos,precio)
importe=int(input("Importe a comrar"))
articulosMenores(articulos,precio,importe)
