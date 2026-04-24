import pandas as pd
from modelos.lista_info_aeropuertos import cargar_datos
from controlador.Operaciones_Grafo import operaciones_grafo
from Mapa.mapa import aereopuertos
from Mapa.mapa import Opgrafo
def punto_4(codigo_buscado):
    # 1. Cargamos la base de datos de aeropuertos y el grafo
    # Usamos las funciones que ya definidas
    info_aeropuertos = aereopuertos
    op_grafo = Opgrafo

    # PARTE 4a: Información del aeropuerto
    # Verificamos que el código existe 
    if codigo_buscado in info_aeropuertos:
        aeropuerto = info_aeropuertos[codigo_buscado]
        print("========================================")
        print("INFORMACION DEL AEROPUERTO SELECCIONADO ")
        print("========================================")
        print(aeropuerto)
    else:
        print("Error: El código ",codigo_buscado," no se encuentra en la base de datos.")
        return

    # PARTE 4b: Caminos mínimos más largos (Top 10)
    # Ejecuta Dijkstra. Este devuelve (distancias, padre)
    # Usamos '_' para ignorar el diccionario de padres que no necesitamos aquí
    distancias, _ = op_grafo.Dijkstra(codigo_buscado)

    # Filtramos los aeropuertos que no tienen conexión (distancia infinito)
    # y eliminamos el aeropuerto de origen (distancia 0)
    conectados = {code: dist for code, dist in distancias.items() 
                  if dist != float('inf') and dist > 0}

    # Ordenamos el diccionario por distancia de mayor a menor
    # y tomamos los primeros 10 resultados
    #top_10_lejanos = sorted(conectados.items(), key=lambda x: x[1], reverse=True)[:10]
    top10 = list(conectados.items())
    for i in range(0, len(top10)):
        for j in range(i+1, len(top10)):
            if top10[i][1]>top10[j][1]:
                aux = top10[i]
                top10[i] = top10[j]
                top10[j] = aux
    top10.reverse()
    top10 = top10[:10]

    print("\n========================================")
    print("TOP 10 TRAYECTOS MAS LARGOS DESDE EL AEROPUERTO DE", codigo_buscado)
    print("========================================")
    
    for i, (codigo, km) in enumerate(top10, 1):
        if codigo in info_aeropuertos:
            dest = info_aeropuertos[codigo]
            print(i, ".", dest.name, "(", codigo, ")", sep="")
            print("   Ubicación:", dest.city, ",", dest.country)
            print("   Distancia mínima:", km, "km")
            print("   Coordenadas: (", dest.lat, ",", dest.lon, ")", sep="")
            print("-" * 30)

# --- PRUEBA DEL PROGRAMA ---
# Puedes cambiar "CGH" por el código que quieras probar
if __name__ == "__main__":
    codigo = input("Ingrese el código del aeropuerto (ej: BOG, BAQ, CGH): ").strip().upper()
    punto_4(codigo)