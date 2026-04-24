import pandas as pd
from modelos.lista_info_aeropuertos import cargar_datos
from controlador.Operaciones_Grafo import operaciones_grafo

def punto_4(codigo_buscado):
    # 1. Cargamos la base de datos de aeropuertos y el grafo
    # Usamos las funciones que ya definidas
    info_aeropuertos = cargar_datos("flights/flights_final.csv")
    op_grafo = operaciones_grafo("flights/flights_final.csv")

    # PARTE 4a: Información del aeropuerto
    # Verificamos que el código existe 
    if codigo_buscado in info_aeropuertos:
        aeropuerto = info_aeropuertos[codigo_buscado]
        print("========================================")
        print("INFORMACION DEL AEROPUERTO SELECCIONADO ")
        print("========================================")
        print(aeropuerto)
    else:
        print(f"Error: El código {codigo_buscado} no se encuentra en la base de datos.")
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
    top_10_lejanos = sorted(conectados.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\n========================================")
    print("TOP 10 TRAYECTOS MAS LARGOS DESDE EL AEROPUERRTO DE", codigo_buscado)
    print("========================================")
    
    for i, (codigo, km) in enumerate(top_10_lejanos, 1):
        if codigo in info_aeropuertos:
            dest = info_aeropuertos[codigo]
            print(f"{i}. {dest.name} ({codigo})")
            print(f"   Ubicación: {dest.city}, {dest.country}")
            print(f"   Distancia mínima: {km:.2f} km")
            print(f"   Coordenadas: ({dest.lat}, {dest.lon})")
            print("-" * 30)

# --- PRUEBA DEL PROGRAMA ---
# Puedes cambiar "CGH" por el código que quieras probar
if __name__ == "__main__":
    codigo = input("Ingrese el código del aeropuerto (ej: BOG, BAQ, CGH): ").strip().upper()
    punto_4(codigo)