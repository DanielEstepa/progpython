def cargar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    return (nombre, sueldo)

def empleado_con_sueldo_mayor(empleado1, empleado2):
    if empleado1[1] > empleado2[1]:
        return empleado1[0]
    else:
        return empleado2[0]

# Bloque principal
empleado1 = cargar_empleado()
empleado2 = cargar_empleado()

nombre_empleado_mayor_sueldo = empleado_con_sueldo_mayor(empleado1, empleado2)

print("El empleado con el sueldo mayor es:", nombre_empleado_mayor_sueldo)
