import folium
from modelos.lista_info_aeropuertos import cargar_datos
from modelos.lista_adj_aeropuertos import lista_adyacencia
from controlador.Operaciones_Grafo import operaciones_grafo

aereopuertos = cargar_datos("flights/flights_final.csv")
adyacencia = lista_adyacencia("flights/flights_final.csv")
Opgrafo = operaciones_grafo("flights/flights_final.csv")

cambioParaGrupo = 0
mapa = folium.Map(location=[0, 0], zoom_start=2)

def punto5(Ori, Des):
    cambioParaGrupo =+1
    distancia, camino, caminoNodos = Opgrafo.caminoEntreNodos(Ori, Des)
    grupo = folium.FeatureGroup(name=cambioParaGrupo)
    for nodo in caminoNodos:
        folium.Marker(
            location=[aereopuertos[nodo].lat, aereopuertos[nodo].lon],
            popup=aereopuertos[nodo]
        ).add_to(grupo)

    grupo.add_to(mapa)
    mapa.save("mapa.html")

    folium.PolyLine(camino, tooltip=distancia).add_to(mapa)
    mapa.save("mapa.html")