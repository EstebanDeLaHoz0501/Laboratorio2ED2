import pandas as pd
import math
from modelos.Aereopuerto import Aereopuerto

def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    aereopuertos = {}

    for i, row in df.iterrows():
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

def listaAdyacencia(ruta):
    df = pd.read_csv(ruta)
    adyacencia = {}  
    for i, row in df.iterrows():
        codeO = row["Source Airport Code"].strip().upper()
        codeD = row["Destination Airport Code"].strip().upper()

        La1=float(row["Source Airport Latitude"])
        La2=float(row["Destination Airport Latitude"])
        Lo1=float(row["Source Airport Longitude"])
        Lo2=float(row["Destination Airport Longitude"])

        gradoSeno1 = math.radians((La2-La1)/2)
        gradoSeno2 = math.radians((Lo2-Lo1)/2)
        gradoCoseno1 = math.radians(La1)
        gradoCoseno2 = math.radians(La2)

        a = (math.sin(gradoSeno1)**2 + math.cos(gradoCoseno1)*
            math.cos(gradoCoseno2)*math.sin(gradoSeno2)**2)
        c = 2*math.asin(math.sqrt(a))

        r=6371

        peso = r*c

        adyacencia.setdefault(codeO, [])
        adyacencia.setdefault(codeD, [])
        if (codeD, peso) not in adyacencia[codeO]:
            adyacencia[codeO].append((codeD, peso))

        if (codeO, peso) not in adyacencia[codeD]:
            adyacencia[codeD].append((codeO, peso))

    return adyacencia