import pandas as pd
import math
from modelos.Aereopuerto import Aereopuerto

class lista_info_airport:
    def __init__(self, ruta_csv):
        self.datos = cargar_datos(ruta_csv)
        
def cargar_datos(ruta: str):
    df = pd.read_csv(ruta)
    aereopuertos = {}

    for i, row in df.iterrows():

        #Regresa aeropuestos origen
        codeO = row["Source Airport Code"].strip().upper()
        if codeO not in aereopuertos:
            aereopuertos[codeO] = Aereopuerto(
                codeO,
                row["Source Airport Name"],
                row["Source Airport City"],
                row["Source Airport Country"],
                row["Source Airport Latitude"],
                row["Source Airport Longitude"]
            )

        #Regresa aeropuertos destino
        codeD = row["Destination Airport Code"].strip().upper()
        if codeD not in aereopuertos:
            aereopuertos[codeD] = Aereopuerto(
                codeD,
                row["Destination Airport Name"],
                row["Destination Airport City"],
                row["Destination Airport Country"],
                row["Destination Airport Latitude"],
                row["Destination Airport Longitude"]
            )
    return aereopuertos