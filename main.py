from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import zipfile



app = FastAPI(title='Proyecto Individual',
            description='Benjamin Zelaya',
            version='1.0.1')

# Cargar los datasets
# ----------------------------------------------------
# Leer el archivo CSV
df = pd.read_csv('Api_merged_data.csv',encoding='utf-8')
df_lenguage = pd.read_csv('df_Languages_Def.csv',encoding='utf-8')

# Definir la ruta de FastAPI
@app.get("/idioma/{idioma}")
def cantidad_peliculas_idioma(idioma: str):
    idioma = idioma.lower()

    # Filtrar el DataFrame para obtener las filas correspondientes al idioma consultado
    peliculas_idioma = df_lenguage[df_lenguage['original_language'].str.lower() == idioma]

    # Obtener la cantidad de películas producidas en el idioma consultado
    cantidad_peliculas = len(peliculas_idioma)

    mensaje = f"La cantidad de peliculas producidas en el idioma {idioma.capitalize()} es: {cantidad_peliculas}"
    return mensaje





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
