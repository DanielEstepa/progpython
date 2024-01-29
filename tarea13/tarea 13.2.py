def cargar_empleados():
    empleados = []
    for _ in range(5):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldos = tuple(float(input(f"Ingrese el sueldo del mes {i+1}: ")) for i in range(3))
        empleados.append([nombre, sueldos])
    return empleados

def imprimir_monto_total_por_empleado(empleados):
    for empleado in empleados:
        nombre = empleado[0]
        sueldos = empleado[1]
        monto_total = sum(sueldos)
        print(f"El monto total cobrado por {nombre} es: {monto_total}")

def imprimir_empleados_ingreso_mayor_a_10000(empleados):
    print("Empleados con ingreso trimestral mayor a 10000:")
    for empleado in empleados:
        nombre = empleado[0]
        sueldos = empleado[1]
        ingreso_trimestral = sum(sueldos)
        if ingreso_trimestral > 10000:
            print(nombre)

# Bloque principal
empleados = cargar_empleados()
imprimir_monto_total_por_empleado(empleados)
imprimir_empleados_ingreso_mayor_a_10000(empleados)
