def cargar_candidatos():
    candidatos = []
    for _ in range(3):
        nombre_candidato = input("Nombre del candidato: ")
        votos_provincias = []
        provincia = input("Nombre de la provincia ('fin' para terminar): ")
        while provincia != 'fin':
            cantidad_votos = int(input(f"Votos para {nombre_candidato} en {provincia}: "))
            votos_provincias.append((provincia, cantidad_votos))
            provincia = input("Nombre de la provincia ('fin' para terminar): ")
        candidatos.append((nombre_candidato, votos_provincias))
    return candidatos

def imprimir_total_votos_por_candidato(candidatos):
    for nombre, provincias in candidatos:
        total_votos = sum(votos for _, votos in provincias)
        print(f"{nombre}: {total_votos} votos")

# Bloque principal
candidatos = cargar_candidatos()
print("\nNombre del candidato y votos totales:")
imprimir_total_votos_por_candidato(candidatos)

