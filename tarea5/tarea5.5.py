n=int(input("cuantos puntos se ingresan en total:"))
cuadrante1=0
cuadrante2=0
cuadrante3=0
cuadrante4=0
for x in range(n):
    coordenadax=float(input("Introduce el valor de eje de coordenadas x:"))
    coordenaday=float(input("Introduce el valor de eje de coordenadas y:"))
    if coordenadax>0 and coordenaday>0:
        print("Esta en el cuadrante 1")
        cuadrante1=cuadrante1+1
    else:
        if coordenadax<0 and coordenaday<0:
            print("Esta en el cuadrante 3")
            cuadrante3=cuadrante3+1
        else:
            if coordenadax>0 and coordenaday<0:
                print("Esta en el cuadrante 2")
                cuadrante2=cuadrante2+1
            else:
                if coordenadax<0 and coordenaday>0:
                        print("Esta en el cuadrante 4")
                        cuadrante4=cuadrante4+1
                
                    
print("Hay estos puntos en el cuadrante 1:",cuadrante1)
print("Hay estos puntos en el cuadrante 2:",cuadrante2)
print("Hay estos puntos en el cuadrante 3:",cuadrante3)
print("Hay estos puntos en el cuadrante 4:",cuadrante4)
