from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import os
import zipfile

# Supongamos que tienes un archivo CSV llamado "movies.csv" con la información de las películas
df_Languages = pd.read_csv("/Users/benjaminzelaya/Desktop/ML_Proyecto_Individual_Henry/FASTAPI/df_Languages_Def.csv")

def cantidad_peliculas_idioma(idioma: str):
    idioma = idioma.lower()

    # Filtrar el DataFrame para obtener las filas correspondientes al idioma consultado
    peliculas_idioma = df_Languages[df_Languages['original_language'].str.lower() == idioma]

    # Obtener la cantidad de películas producidas en el idioma consultado
    cantidad_peliculas = len(peliculas_idioma)

    mensaje = f"La cantidad de películas producidas en el idioma {idioma.capitalize()} es: {cantidad_peliculas}"
    return mensaje

app = FastAPI()

@app.get("/cantidad_peliculas/{idioma}")
def obtener_cantidad_peliculas(idioma: str):
    return cantidad_peliculas_idioma(idioma)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
