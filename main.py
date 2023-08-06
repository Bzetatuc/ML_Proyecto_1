from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import zipfile
import locale

app = FastAPI(title='Proyecto Individual',
            description='Benjamin Zelaya',
            version='1.0.1')


### IDIOMA 

# Cargar los datasets
# ----------------------------------------------------
# Leer el archivo CSV
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



# DURACION 

# Cargar los datasets
# ----------------------------------------------------
# Leer el archivo CSV
df_duracion = pd.read_csv('df_duracion_Def.csv',encoding='utf-8')

@app.get("/peliculas_times/{pelicula}")
def peliculas_times(pelicula: str):
    pelicula = pelicula.lower()

    # DataFrame para obtener las filas correspondientes a la película consultada
    pelicula_info = df_duracion[df_duracion['title'].str.lower() == pelicula]

    # Verificaremos si se encontró la película
    if pelicula_info.empty:
        raise HTTPException(status_code=404, detail=f"La película '{pelicula.capitalize()}' no fue encontrada.")

    # duración y año de la película consultada
    duracion = pelicula_info.iloc[0]['runtime'].astype(int)
    año = pelicula_info.iloc[0]['release_year']

    mensaje = f"La pelicula {pelicula} tiene una duración de {duracion} minutos, del Año {año}"
    return mensaje


### FRANQUICIA 

# Cargar los datasets
# ----------------------------------------------------
# Leer el archivo CSV
df_franquicia = pd.read_csv('df_franquicia_Def.csv',encoding='utf-8')

@app.get("/franquicia/{franquicia}")
def franquicia(Franquicia: str):
    franquicia_lower = Franquicia.lower()

    # filas correspondientes a la franquicia indicada
    peliculas_franquicia = df_franquicia[df_franquicia['franquicia'].str.lower() == franquicia_lower]

    # cantidad de películas 
    cantidad_peliculas = len(peliculas_franquicia)

    # ganancia total / ganancia promedio de la franquicia
    ganancia_total = peliculas_franquicia['revenue'].sum()
    ganancia_promedio = peliculas_franquicia['revenue'].mean()

    # Formatear los montos de las ganancias
    ganancia_total_str = "u$s {:,.2f}".format(ganancia_total) #utilizo format para visulizar mejor los montos.
    ganancia_promedio_str = "u$s {:,.2f}".format(ganancia_promedio)

    resultado = f"La franquicia {Franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total_str} y una ganancia promedio de {ganancia_promedio_str} de Dolares"
    return resultado



### PAISES  

# Cargar los datasets
# ----------------------------------------------------
# Leer el archivo CSV
df_paises = pd.read_csv('df_paises_Def.csv',encoding='utf-8')

@app.get("/peliculas_por_paises/{Pais}")
def peliculas_por_paises(Pais: str):
    pais_lower = Pais.lower()

    # Llenare los valores NaN que tiene la columna con una cadena vacía
    df_paises['country_name'] = df_paises['country_name'].fillna('')

    # filas correspondientes al país
    peliculas_pais = df_paises[df_paises['country_name'].str.lower().str.contains(pais_lower)]

    # cantidad de películas producidas en el país
    cantidad_peliculas = len(peliculas_pais)

    resultado_paises = f" En {Pais} se produjeron {cantidad_peliculas} películas"
    return resultado_paises



### PRODUCTORAS EXITOSAS  

# Cargar los datasets
# ----------------------------------------------------
# Leer el archivo CSV
df_Prod_exitosas = pd.read_csv('df_prod_exitosas_Def.csv.csv',encoding='utf-8')

@app.get("/productoras_exitosas/{Productora}")
def productoras_exitosas(Productora: str):
    productora_lower = Productora.lower()

    # Rellenar los valores faltantes (NaN) en la columna 'name_companies' con una cadena vacía ('')
    df_Prod_exitosas['name_companies'] = df_Prod_exitosas['name_companies'].fillna('')

    # Filas correspondientes a la productora
    peliculas_productora = df_Prod_exitosas[df_Prod_exitosas['name_companies'].str.lower().str.contains(productora_lower)]

    # Total de revenue
    total_revenue = peliculas_productora['revenue'].sum()

    # Cantidad de películas realizadas por la productora
    cantidad_peliculas = len(peliculas_productora)

    # Formatear el revenue como moneda en dólares
    revenue_formateado = locale.currency(total_revenue, grouping=True)

    Resultado = f"La productora {Productora} ha tenido un revenue de u$s {revenue_formateado} y ha realizado {cantidad_peliculas} películas"
    return Resultado



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
