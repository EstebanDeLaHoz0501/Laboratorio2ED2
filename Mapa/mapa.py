import folium
from modelos.lista_info_aeropuertos import cargar_datos
from modelos.lista_adj_aeropuertos import lista_adyacencia
from controlador.Operaciones_Grafo import operaciones_grafo
import webbrowser

aereopuertos = cargar_datos("flights/flights_final.csv")
adyacencia = lista_adyacencia("flights/flights_final.csv")
Opgrafo = operaciones_grafo("flights/flights_final.csv")

cambioParaGrupo = 0


def punto5(Ori, Des):
    if Ori not in adyacencia:
        return 0
    if Des not in adyacencia:
        return 0
    distancia, camino, caminoNodos = Opgrafo.caminoEntreNodos(Ori, Des)
    if distancia == None or camino == None or caminoNodos == None:
        return 1
    mapa = folium.Map(location=[0, 0], zoom_start=2)
    grupo = folium.FeatureGroup(name=cambioParaGrupo)
    for nodo in caminoNodos:
        folium.Marker(
            location=[aereopuertos[nodo].lat, aereopuertos[nodo].lon],
            popup=aereopuertos[nodo]
        ).add_to(grupo)

    grupo.add_to(mapa)
    folium.PolyLine(camino, tooltip=distancia).add_to(mapa)
    mapa.save("mapa.html")
    webbrowser.open("mapa.html")
    return 2

def punto6():
    mapa = folium.Map(location=[0, 0], zoom_start=2)
    for nodo in adyacencia:
        folium.Marker(
            location=[aereopuertos[nodo].lat, aereopuertos[nodo].lon],
            popup=aereopuertos[nodo]
        ).add_to(mapa)

    mapa.save("mapa.html")
    webbrowser.open("mapa.html")
